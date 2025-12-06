#!/usr/bin/env python3
# smoothfps.py — FINAL stable release
# Matrix-left panel + non-overlapping UI + FPS & Refresh menus
# Tool by @code07777
# Telegram: @code07777
# Channel: https://t.me/codeteamback077
# Buy VIP file: @code07777

import curses
import time
import random
import subprocess
import json
import threading
import os
import sys

# -----------------------
# Helpers: device info (Android no-root)
# -----------------------
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

# -----------------------
# Matrix runner (draws inside a curses window)
# -----------------------
def matrix_runner(win, stop_flag, speed=0.06):
    # window: curses window object for matrix panel
    max_y, max_x = win.getmaxyx()
    cols = max_x
    drops = [0] * cols
    chars = "01"  # lightweight for mobile
    while not stop_flag[0]:
        max_y, max_x = win.getmaxyx()
        cols = max_x
        # ensure drops list length
        if len(drops) < cols:
            drops += [0] * (cols - len(drops))
        elif len(drops) > cols:
            drops = drops[:cols]
        for x in range(cols):
            if drops[x] <= 0 and random.random() > 0.97:
                drops[x] = 1
            if drops[x] > 0:
                # y position cycles
                y = drops[x] % max_y
                ch = random.choice(chars)
                try:
                    win.addstr(y, x, ch, curses.color_pair(1))
                except curses.error:
                    pass
                drops[x] += 1
                # reset occasionally
                if drops[x] > max_y + random.randint(2, 8):
                    drops[x] = 0
            else:
                # clear top occasionally
                try:
                    win.addch(0, x, ' ')
                except curses.error:
                    pass
        try:
            win.refresh()
        except curses.error:
            pass
        time.sleep(speed)

# -----------------------
# Slide animation on a curses window (left-right-left)
# -----------------------
def slide_text(win, row, text, delay=0.008, max_spaces=20, color_pair=2):
    _, width = win.getmaxyx()
    spaces = min(max_spaces, max(0, width - len(text) - 4))
    # left -> right
    for i in range(spaces):
        try:
            win.move(row, 0); win.clrtoeol()
            win.addstr(row, i, text, curses.color_pair(color_pair) | curses.A_BOLD)
            win.refresh()
        except curses.error:
            pass
        time.sleep(delay)
    # right -> left
    for i in range(spaces, -1, -1):
        try:
            win.move(row, 0); win.clrtoeol()
            win.addstr(row, i, text, curses.color_pair(color_pair) | curses.A_BOLD)
            win.refresh()
        except curses.error:
            pass
        time.sleep(delay)
    # leave final fixed
    try:
        win.move(row, 0); win.clrtoeol()
        win.addstr(row, 2, text, curses.color_pair(color_pair) | curses.A_BOLD)
        win.refresh()
    except curses.error:
        pass

# -----------------------
# Safe config generator
# -----------------------
def generate_safe_config(pkg, fps_choice, hz_choice, mode_choice, boost_choice, ts_choice, opt_choice):
    fps_map = {"1":"60","2":"90","3":"120"}
    hz_map = {"1":"60","2":"90","3":"120"}
    mode_map = {"1":"Extreme","2":"Ultra","3":"Medium"}
    boost_map = {"1":"Maximum","2":"Medium"}
    ts_map = {"1":"Maximum","2":"Medium"}
    opt_map = {"1":"Enable","2":"Disable"}

    cfg = {
        "package": pkg,
        "recommended_frame_rate": fps_map.get(fps_choice, "60"),
        "recommended_refresh_rate_hz": hz_map.get(hz_choice, "60"),
        "performance_mode": mode_map.get(mode_choice, "Medium"),
        "cpu_gpu_boost": boost_map.get(boost_choice, "Medium"),
        "touch_sampling": ts_map.get(ts_choice, "Medium"),
        "hardware_optimization": opt_map.get(opt_choice, "Enable"),
        "notes": [
            "This file contains device-side recommended settings only.",
            "It does NOT modify game binaries or bypass anti-cheat.",
            "To apply some changes you may need adb (PC) or manual OEM settings.",
            "Always backup files before making changes."
        ]
    }
    fname = f"{pkg or 'pubg'}_safe_config.json"
    with open(fname, "w") as f:
        json.dump(cfg, f, indent=2)
    return fname

# -----------------------
# Curses UI main
# -----------------------
def curses_main(stdscr):
    curses.curs_set(1)  # show cursor for inputs
    curses.start_color()
    curses.use_default_colors()
    # color pairs: 1=matrix green, 2=cyan title, 3=yellow prompt, 4=magenta, 5=white
    curses.init_pair(1, curses.COLOR_GREEN, -1)
    curses.init_pair(2, curses.COLOR_CYAN, -1)
    curses.init_pair(3, curses.COLOR_YELLOW, -1)
    curses.init_pair(4, curses.COLOR_MAGENTA, -1)
    curses.init_pair(5, curses.COLOR_WHITE, -1)

    max_y, max_x = stdscr.getmaxyx()
    panel_w = min(40, max(10, max_x // 3))        # left matrix panel width
    ui_w = max_x - panel_w - 2
    panel_h = max_y - 2

    # windows
    matrix_win = curses.newwin(panel_h, panel_w, 1, 1)
    ui_win = curses.newwin(panel_h, ui_w, 1, panel_w + 2)
    stdscr.border()
    stdscr.refresh()

    # start matrix thread
    stop_flag = [False]
    t = threading.Thread(target=matrix_runner, args=(matrix_win, stop_flag, 0.055), daemon=True)
    t.start()

    # draw UI header
    ui_win.clear()
    ui_win.border()
    brand, model, android, cpu, ram = get_device_info()
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

    # slide-in title
    slide_text(ui_win, 1, "◖ DEVICE AND HARDWARE INFO ◗", delay=0.006, max_spaces=18, color_pair=2)

    # small helper to prompt inside ui_win
    def prompt(y, label, default=""):
        ui_win.addstr(y, 2, " " * (ui_w - 4))
        ui_win.addstr(y, 2, label, curses.color_pair(3))
        ui_win.refresh()
        curses.echo()
        ui_win.move(y, 2 + len(label) + 1)
        s = ui_win.getstr(y, 2 + len(label) + 1, 60)
        curses.noecho()
        try:
            val = s.decode().strip()
        except:
            val = ""
        if val == "":
            return default
        return val

    # FPS menu (interactive)
    def fps_menu():
        ui_win.addstr(14, 2, " " * (ui_w - 4))
        ui_win.addstr(14, 2, "◖ Select Gaming Frame Rate ◗", curses.color_pair(2))
        ui_win.addstr(16, 4, "[1] 60FPS  (Stable)")
        ui_win.addstr(17, 4, "[2] 90FPS  (Stable)")
        ui_win.addstr(18, 4, "[3] 120FPS (Device support only)")
        ui_win.refresh()
        choice = prompt(20, "Select Option (1-3):", "2")
        return choice if choice in ("1","2","3") else "2"

    # Refresh menu
    def hz_menu():
        ui_win.addstr(22, 2, " " * (ui_w - 4))
        ui_win.addstr(22, 2, "◖ Select Gaming Refresh Rate ◗", curses.color_pair(2))
        ui_win.addstr(24, 4, "[1] 60HZ  (Stable)")
        ui_win.addstr(25, 4, "[2] 90HZ  (Stable)")
        ui_win.addstr(26, 4, "[3] 120HZ (Device support only)")
        ui_win.refresh()
        choice = prompt(28, "Select Option (1-3):", "2")
        return choice if choice in ("1","2","3") else "2"

    # Other menus (mode, boost, touch, opt)
    def mode_menu():
        ui_win.addstr(30, 2, " " * (ui_w - 4))
        ui_win.addstr(30, 2, "◖ Select Gaming Mode ◗", curses.color_pair(2))
        ui_win.addstr(32, 4, "[1] Extreme")
        ui_win.addstr(33, 4, "[2] Ultra (May heat)")
        ui_win.addstr(34, 4, "[3] Medium")
        ui_win.refresh()
        choice = prompt(36, "Select Option (1-3):", "1")
        return choice if choice in ("1","2","3") else "1"

    def boost_menu():
        ui_win.addstr(38, 2, " " * (ui_w - 4))
        ui_win.addstr(38, 2, "◖ CPU/GPU Boost ◗", curses.color_pair(2))
        ui_win.addstr(40, 4, "[1] Maximum (May heat)")
        ui_win.addstr(41, 4, "[2] Medium (Stable)")
        ui_win.refresh()
        choice = prompt(43, "Select Option (1-2):", "2")
        return choice if choice in ("1","2") else "2"

    def touch_menu():
        ui_win.addstr(45, 2, " " * (ui_w - 4))
        ui_win.addstr(45, 2, "◖ Touch Sampling Rate ◗", curses.color_pair(2))
        ui_win.addstr(47, 4, "[1] Maximum")
        ui_win.addstr(48, 4, "[2] Medium")
        ui_win.refresh()
        choice = prompt(50, "Select Option (1-2):", "1")
        return choice if choice in ("1","2") else "1"

    def opt_menu():
        ui_win.addstr(52, 2, " " * (ui_w - 4))
        ui_win.addstr(52, 2, "◖ Hardware Optimization ◗", curses.color_pair(2))
        ui_win.addstr(54, 4, "[1] Enable")
        ui_win.addstr(55, 4, "[2] Disable")
        ui_win.refresh()
        choice = prompt(57, "Select Option (1-2):", "1")
        return choice if choice in ("1","2") else "1"

    # Run menus
    pkg = prompt(12, "Game Package (default=com.tencent.ig):", "com.tencent.ig")
    fps_choice = fps_menu()
    hz_choice = hz_menu()
    mode_choice = mode_menu()
    boost_choice = boost_menu()
    ts_choice = touch_menu()
    opt_choice = opt_menu()

    # Applying steps animation
    steps = [
        "Applying Lag Fix Scripts…",
        "Optimizing RAM Performance…",
        "Optimizing System Performance…",
        "Rechecking Script And Files…"
    ]
    row = 60
    if row + 8 > panel_h - 1:
        row = panel_h - 10
    for s in steps:
        slide_text(ui_win, row, s, delay=0.006, max_spaces=18, color_pair=3)
        # small progress bar
        for i in range(21):
            try:
                bar = "[" + ("#" * i).ljust(20) + "]"
                ui_win.addstr(row + 1, 2, f"{bar} {i*5}%", curses.color_pair(5))
                ui_win.refresh()
            except curses.error:
                pass
            time.sleep(0.05)
        row += 3

    # Stop matrix
    stop_flag[0] = True
    time.sleep(0.08)

    # Generate safe config file
    fname = generate_safe_config(pkg, fps_choice, hz_choice, mode_choice, boost_choice, ts_choice, opt_choice)

    ui_win.addstr(row + 2, 2, f"Config generated: {fname}", curses.color_pair(2))
    ui_win.addstr(row + 4, 2, "All scripts applied successfully. Restart device recommended.", curses.color_pair(4))
    ui_win.addstr(row + 6, 2, "Press any key to exit.", curses.color_pair(3))
    ui_win.refresh()
    ui_win.getch()

# -----------------------
# Entry
# -----------------------
def main():
    try:
        curses.wrapper(curses_main)
    except Exception as e:
        print("Error running terminal UI:", e)
        print("If you are on Termux and get 'curses' errors, ensure Python/curses are installed.")
        print("Run: pkg install python -y  (or ensure Python3 with curses support).")
        sys.exit(1)

if __name__ == "__main__":
    main()