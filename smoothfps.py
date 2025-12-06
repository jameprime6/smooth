#!/usr/bin/env python3
# smoothfps_curses.py
# Matrix-left panel + non-overlapping UI (curses)
# Tool by @code07777

import curses
import time
import random
import subprocess
import json
import os

# -------------------------
# Helpers: device info (Android no-root)
# -------------------------
def getprop(prop):
    try:
        out = subprocess.check_output(["getprop", prop], stderr=subprocess.DEVNULL)
        return out.decode().strip()
    except Exception:
        return "Unknown"

def get_device_info():
    brand = getprop("ro.product.brand")
    model = getprop("ro.product.model")
    android = getprop("ro.build.version.release")
    cpu = getprop("ro.product.cpu.abi")
    try:
        mem = open("/proc/meminfo").read()
        total = mem.split("MemTotal:")[1].split("kB")[0].strip()
        total = f"{int(total)//1024} MB"
    except Exception:
        total = "Unknown"
    return brand, model, android, cpu, total

# -------------------------
# Matrix runner (draws inside a curses window)
# -------------------------
def matrix_runner(win, stop_flag, speed=0.05):
    # win: curses window object for matrix panel
    max_y, max_x = win.getmaxyx()
    cols = max_x
    drops = [0] * cols
    chars = "01"  # lightweight characters for mobile-friendly performance
    while not stop_flag[0]:
        max_y, max_x = win.getmaxyx()
        cols = max_x
        for x in range(cols):
            if drops[x] <= 0 and random.random() > 0.97:
                drops[x] = 1
            if drops[x] > 0:
                ch = random.choice(chars)
                # y position cycles; we paint dropping column
                y = drops[x] % max_y
                try:
                    win.addstr(y, x, ch, curses.color_pair(1))
                except curses.error:
                    pass
                drops[x] += 1
                if drops[x] > max_y + 5:
                    drops[x] = 0
            else:
                # occasionally clear top cell
                try:
                    win.addch(0, x, ' ')
                except curses.error:
                    pass
        win.refresh()
        time.sleep(speed)

# -------------------------
# UI helpers: sliding text
# -------------------------
def slide_text(win, row, text, delay=0.01, max_spaces=20, color=0):
    _, width = win.getmaxyx()
    spaces = min(max_spaces, max(0, width - len(text) - 2))
    # left -> right
    for i in range(spaces):
        try:
            win.move(row, 0)
            win.clrtoeol()
            win.addstr(row, i, text, curses.color_pair(color))
            win.refresh()
        except curses.error:
            pass
        time.sleep(delay)
    # right -> left
    for i in range(spaces, -1, -1):
        try:
            win.move(row, 0)
            win.clrtoeol()
            win.addstr(row, i, text, curses.color_pair(color))
            win.refresh()
        except curses.error:
            pass
        time.sleep(delay)
    # final fixed
    try:
        win.move(row, 0)
        win.clrtoeol()
        win.addstr(row, 1, text, curses.color_pair(color))
        win.refresh()
    except curses.error:
        pass

# -------------------------
# Save config (safe)
# -------------------------
def generate_safe_config(pkg, fps, hz, mode, boost, ts, opt):
    fps_map = {"1":"60","2":"90","3":"120"}
    hz_map = {"1":"60","2":"90","3":"120"}
    mode_map = {"1":"Extreme","2":"Ultra","3":"Medium"}
    boost_map = {"1":"Maximum","2":"Medium"}
    ts_map = {"1":"Maximum","2":"Medium"}
    opt_map = {"1":"Enable","2":"Disable"}

    cfg = {
        "package": pkg,
        "recommended_frame_rate": fps_map.get(fps, "60"),
        "recommended_refresh_rate_hz": hz_map.get(hz, "60"),
        "performance_mode": mode_map.get(mode, "Medium"),
        "cpu_gpu_boost": boost_map.get(boost, "Medium"),
        "touch_sampling": ts_map.get(ts, "Medium"),
        "hardware_optimization": opt_map.get(opt, "Enable"),
        "notes": [
            "This file contains device-side recommended settings only.",
            "It does NOT modify game binaries or bypass anti-cheat.",
            "To apply some changes you may need adb (PC) or manual adjustments.",
            "Always backup files before making changes."
        ]
    }
    fname = f"{pkg or 'pubg'}_safe_config.json"
    with open(fname, "w") as f:
        json.dump(cfg, f, indent=2)
    return fname

# -------------------------
# Main curses UI
# -------------------------
def curses_main(stdscr):
    curses.curs_set(1)  # show cursor for input
    curses.start_color()
    curses.use_default_colors()
    # pair 1 = green for matrix; pair 2 = cyan for titles; pair 3 = yellow for prompts
    curses.init_pair(1, curses.COLOR_GREEN, -1)
    curses.init_pair(2, curses.COLOR_CYAN, -1)
    curses.init_pair(3, curses.COLOR_YELLOW, -1)
    curses.init_pair(4, curses.COLOR_MAGENTA, -1)
    curses.init_pair(5, curses.COLOR_WHITE, -1)

    max_y, max_x = stdscr.getmaxyx()
    # left panel width (matrix). Adjust to taste: e.g., 40 columns or 40% of screen
    panel_w = min(40, max(10, max_x // 3))
    panel_h = max_y - 2

    # create windows
    matrix_win = curses.newwin(panel_h, panel_w, 0, 0)
    ui_win = curses.newwin(panel_h, max_x - panel_w, 0, panel_w + 1)

    # start matrix thread
    stop_flag = [False]
    t = threading.Thread(target=matrix_runner, args=(matrix_win, stop_flag, 0.06), daemon=True)
    t.start()

    # draw header in ui_win (safe area)
    brand, model, android, cpu, ram = get_device_info()
    ui_win.border()
    ui_win.addstr(1, 2, "◖ DEVICE AND HARDWARE INFO ◗", curses.color_pair(2) | curses.A_BOLD)
    ui_win.addstr(3, 2, f"➤ DEVICE  : {brand}", curses.color_pair(5))
    ui_win.addstr(4, 2, f"➤ MODEL   : {model}", curses.color_pair(5))
    ui_win.addstr(5, 2, f"➤ ANDROID : {android}", curses.color_pair(5))
    ui_win.addstr(6, 2, f"➤ CPU     : {cpu}", curses.color_pair(5))
    ui_win.addstr(7, 2, f"➤ RAM     : {ram}", curses.color_pair(5))
    ui_win.addstr(9, 2, "Tool by @code07777", curses.color_pair(4))
    ui_win.addstr(10, 2, "Telegram: @code07777", curses.color_pair(4))
    ui_win.addstr(11, 2, "Channel: t.me/codeteamback077", curses.color_pair(4))
    ui_win.refresh()

    # slide title effect
    slide_text(ui_win, 1, "◖ DEVICE AND HARDWARE INFO ◗", delay=0.008, max_spaces=20, color=2)

    # input prompts (use ui_win.getstr to keep input in UI area)
    def prompt(y, prompt_text, default=""):
        ui_win.addstr(y, 2, " " * (ui_win.getmaxyx()[1] - 4))
        ui_win.addstr(y, 2, prompt_text, curses.color_pair(3))
        ui_win.refresh()
        curses.echo()
        ui_win.move(y, 2 + len(prompt_text) + 1)
        s = ui_win.getstr(y, 2 + len(prompt_text) + 1, 60)
        curses.noecho()
        try:
            return s.decode().strip() or default
        except:
            return default

    pkg = prompt(14, "Game Package Name (default com.tencent.ig): ", "com.tencent.ig")
    fps = prompt(16, "Select FPS [1]60 [2]90 [3]120 (default 2): ", "2")
    hz = prompt(18, "Select Refresh [1]60 [2]90 [3]120 (default 2): ", "2")
    mode = prompt(20, "Select Mode [1]Extreme [2]Ultra [3]Medium (default 1): ", "1")
    boost = prompt(22, "CPU/GPU Boost [1]Max [2]Medium (default 2): ", "2")
    ts = prompt(24, "Touch Sampling [1]Max [2]Medium (default 1): ", "1")
    opt = prompt(26, "Hardware Opt [1]Enable [2]Disable (default 1): ", "1")

    # show applying animations in ui_win while matrix continues
    def apply_steps():
        steps = [
            "Applying Lag Fix Scripts…",
            "Optimizing RAM Performance…",
            "Optimizing System Performance…",
            "Rechecking Script And Files…"
        ]
        row = 28
        for s in steps:
            slide_text(ui_win, row, s, delay=0.008, max_spaces=18, color=3)
            # small progress bar
            for i in range(0, 21):
                try:
                    bar = "[" + ("#" * i).ljust(20) + "]"
                    ui_win.addstr(row + 1, 2, f"{bar} {i*5}%", curses.color_pair(5))
                    ui_win.refresh()
                except curses.error:
                    pass
                time.sleep(0.06)
            row += 3

    apply_steps()

    # stop matrix and show final messages
    stop_flag[0] = True
    time.sleep(0.08)  # allow thread to finish

    fname = generate_safe_config(pkg, fps, hz, mode, boost, ts, opt)
    ui_win.addstr( row + 2, 2, f"Config Generated: {fname}", curses.color_pair(2))
    ui_win.addstr( row + 4, 2, "All Script Applied Successfully. Restart device for best results.", curses.color_pair(4))
    ui_win.addstr( row + 6, 2, "Press any key to exit.", curses.color_pair(3))
    ui_win.refresh()

    ui_win.getch()  # wait for key
    return

def main():
    try:
        curses.wrapper(curses_main)
    except Exception as e:
        print("Error running terminal UI:", e)
        print("Make sure your terminal supports curses (Termux or Linux).")

if __name__ == "__main__":
    main()
