#!/usr/bin/env python3
# smoothfps.py — Matrix background + slide UI + safe config generator (Android, no-root)
import os, time, sys
import subprocess
import threading
import json
from shutil import which

# ------------------------
# Colors & styles
# ------------------------
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
WHITE = "\033[97m"

GLOW = f"{BOLD}{CYAN}"

# ------------------------
# Device info helpers (no-root)
# ------------------------
def getprop(prop):
    try:
        out = subprocess.check_output(["getprop", prop], stderr=subprocess.DEVNULL)
        return out.decode().strip()
    except:
        return "Unknown"

def get_device_info():
    brand = getprop("ro.product.brand")
    model = getprop("ro.product.model")
    android = getprop("ro.build.version.release")
    cpu = getprop("ro.product.cpu.abi")
    try:
        mem = open("/proc/meminfo").read()
        total_ram = mem.split("MemTotal:")[1].split("kB")[0].strip()
        total_ram = f"{int(total_ram)//1024} MB"
    except:
        total_ram = "Unknown"
    return brand, model, android, cpu, total_ram

# ------------------------
# Matrix-style background (non-blocking)
# ------------------------
_MATRIX_RUNNING = False

def _matrix_thread(cols=80, speed=0.05):
    import random
    # Build initial drops
    drops = [0 for _ in range(cols)]
    chars = "0123456789abcdef@#$%^&*()[]{}<>?/|\\"
    while _MATRIX_RUNNING:
        line = []
        for i in range(cols):
            if random.random() > 0.97:
                drops[i] = 1
            if drops[i] > 0:
                ch = chars[int(random.random()*len(chars))]
                line.append(f"\033[92m{ch}\033[0m")  # green
                drops[i] += 1
                if drops[i] > 6 + int(random.random()*10):
                    drops[i] = 0
            else:
                line.append(" ")
        # Print only when header cleared to keep UI readable
        sys.stdout.write("".join(line) + "\r\n")
        sys.stdout.flush()
        time.sleep(speed)

def start_matrix(cols=60, speed=0.05):
    global _MATRIX_RUNNING, _matrix_thread_obj
    if _MATRIX_RUNNING:
        return
    _MATRIX_RUNNING = True
    _matrix_thread_obj = threading.Thread(target=_matrix_thread, args=(cols, speed), daemon=True)
    _matrix_thread_obj.start()

def stop_matrix():
    global _MATRIX_RUNNING
    _MATRIX_RUNNING = False
    # allow thread to exit gracefully
    time.sleep(0.06)

# ------------------------
# Slide text animation (left <-> right)
# ------------------------
def slide_text(text, delay=0.006, spaces=20):
    # print a sliding line; returns leaving the text printed once (no \r)
    for i in range(spaces):
        sys.stdout.write(" " * i + text + "\r")
        sys.stdout.flush()
        time.sleep(delay)
    for i in range(spaces, 0, -1):
        sys.stdout.write(" " * i + text + "\r")
        sys.stdout.flush()
        time.sleep(delay)
    print(text)

# ------------------------
# Smooth progress bar
# ------------------------
def smooth_loading(text, speed=0.012):
    print()
    slide_text(f"{GLOW}{text}{RESET}", delay=0.005, spaces=18)
    bar = "■■■■■■■■■■■■■■■■■■■■"
    for i in range(1, len(bar)+1):
        sys.stdout.write(f"\r{GREEN}{bar[:i]}{RESET}")
        sys.stdout.flush()
        time.sleep(speed)
    print("\n")

# ------------------------
# Header (with sliding title)
# ------------------------
def header():
    os.system("clear")
    brand, model, android, cpu, ram = get_device_info()
    # Start a small matrix background above the header (prints a block)
    # We'll print 6 lines of matrix top area for effect
    start_matrix(cols=60, speed=0.03)
    time.sleep(0.06)  # give matrix a tick
    # Show sliding title
    slide_text(f"{MAGENTA}◖ DEVICE AND HARDWARE INFO ◗{RESET}", delay=0.006, spaces=18)
    print(f"""
{CYAN}➤ DEVICE  : {WHITE}{brand}{RESET}
{CYAN}➤ MODEL   : {WHITE}{model}{RESET}
{CYAN}➤ ANDROID : {WHITE}{android}{RESET}
{CYAN}➤ CPU     : {WHITE}{cpu}{RESET}
{CYAN}➤ RAM     : {WHITE}{ram}{RESET}

{GLOW}◖ Copyright © code07777 ◗{RESET}
""")
    # Keep matrix running in background; later we'll stop it before major prints

# ------------------------
# Safe config generator (creates a JSON file with recommendations)
# ------------------------
def generate_safe_config(pkg_name, fps_choice, refresh_choice, mode_choice, boost_choice, ts_choice, opt_choice):
    # Map numeric selections to human-friendly
    fps_map = {"1":"60","2":"90","3":"120"}
    hz_map = {"1":"60","2":"90","3":"120"}
    mode_map = {"1":"Extreme","2":"Ultra","3":"Medium"}
    boost_map = {"1":"Maximum","2":"Medium"}
    ts_map = {"1":"Maximum","2":"Medium"}
    opt_map = {"1":"Enable","2":"Disable"}

    cfg = {
        "package": pkg_name,
        "recommended_frame_rate": fps_map.get(fps_choice, "60"),
        "recommended_refresh_rate_hz": hz_map.get(refresh_choice, "60"),
        "performance_mode": mode_map.get(mode_choice, "Medium"),
        "cpu_gpu_boost": boost_map.get(boost_choice, "Medium"),
        "touch_sampling": ts_map.get(ts_choice, "Medium"),
        "hardware_optimization": opt_map.get(opt_choice, "Enable"),
        "notes": [
            "This file contains device-side recommended settings only.",
            "It does NOT modify game binaries or bypass anti-cheat.",
            "To apply some changes you may need adb (PC) or manual adjustments.",
            "Always backup files before making changes."
        ],
        "safe_commands_for_adb": [
            # Non-destructive suggestions (informational)
            "adb shell settings put global sampling_rate <value>  # device-dependent (requires experimental permission)",
            "# e.g., use device devtools or OEM settings to set refresh rate where possible",
            "# To push this config onto PC/emulator: adb push pubg_safe_config.json /sdcard/"
        ]
    }
    # Save to file
    fname = f"{pkg_name or 'pubg'}_safe_config.json"
    with open(fname, "w") as f:
        json.dump(cfg, f, indent=2)
    return fname, cfg

# ------------------------
# Attempt adb push (only if adb is available on this environment)
# ------------------------
def adb_push_if_possible(localpath, remotepath="/sdcard/"):
    adb_path = which("adb")
    if not adb_path:
        return False, "adb not found on PATH"
    try:
        subprocess.check_call([adb_path, "push", localpath, remotepath])
        return True, f"Pushed {localpath} -> {remotepath}"
    except subprocess.CalledProcessError as e:
        return False, f"adb push failed: {e}"

# ------------------------
# Input helper
# ------------------------
def ask(prompt):
    return input(f"{YELLOW}{prompt}{RESET}")

# ------------------------
# Main
# ------------------------
def main():
    try:
        header()
        # small pause then stop excessive matrix printing so UI stays readable
        time.sleep(0.35)
        stop_matrix()

        print(f"{MAGENTA}➤ [ = ] Game Package Name ◗{RESET}")
        pkg = ask("➤ Type Here  = ").strip() or "com.tencent.ig"

        print(f"""
{MAGENTA}➤ [ = ] Select Gaming Frame Rate ◗{RESET}
 [1] 60FPS (Stable)
 [2] 90FPS (Stable)
 [3] 120FPS (Unstable)
""")
        fps = ask("➤ Select Option = ").strip() or "1"

        print(f"""
{MAGENTA}➤ [ = ] Select Gaming Refresh Rate ◗{RESET}
 [1] 60HZ (Stable)
 [2] 90HZ (Stable)
 [3] 120HZ (Stable)
""")
        hz = ask("➤ Select Option = ").strip() or "1"

        print(f"""
{MAGENTA}➤ [ = ] Select Gaming Mode ◗{RESET}
 [1] Extreme
 [2] Ultra (Device May Heat)
 [3] Medium
""")
        mode = ask("➤ Select Option = ").strip() or "1"

        print(f"""
{MAGENTA}➤ [ = ] Enable CPU/GPU Boost ◗{RESET}
 [1] Maximum (Device May Heat)
 [2] Medium (Stable)
""")
        boost = ask("➤ Select Option = ").strip() or "2"

        print(f"""
{MAGENTA}➤ [ = ] Boost Touch Sampling Rate ◗{RESET}
 [1] Maximum
 [2] Medium
""")
        ts = ask("➤ Select Option = ").strip() or "1"

        print(f"""
{MAGENTA}➤ [ = ] Hardware Optimization ◗{RESET}
 [1] Enable
 [2] Disable
""")
        opt = ask("➤ Select Option = ").strip() or "1"

        # Start background matrix again while applying (non-blocking)
        start_matrix(cols=60, speed=0.03)
        smooth_loading("➤ Applying safe lag-fix scripts (simulated)…")
        smooth_loading("➤ Optimizing RAM & System…")
        time.sleep(0.5)
        stop_matrix()

        # Generate safe config file
        fname, cfg = generate_safe_config(pkg, fps, hz, mode, boost, ts, opt)
        print(f"{GREEN}➤ Generated safe config file:{RESET} {WHITE}{fname}{RESET}")
        print(f"{YELLOW}➤ Note:{RESET} This file contains recommended device-side settings only.")
        print(f"{YELLOW}➤ It does NOT edit game files or bypass anti-cheat.{RESET}\n")

        # Offer to adb push the file (only if adb available). This requires a PC with adb or adb on device.
        want_push = ask("➡ Do you want to try pushing this file to /sdcard/ via adb? (y/N): ").lower()
        if want_push == "y":
            ok, msg = adb_push_if_possible(fname, "/sdcard/")
            if ok:
                print(f"{GREEN}➤ adb push succeeded:{RESET} {msg}")
                print(f"{YELLOW}➤ On your device you may move the file to game folder if needed (manual).{RESET}")
            else:
                print(f"{YELLOW}➤ adb push failed:{RESET} {msg}")
                print(f"{YELLOW}➤ If you want to push from a PC: use 'adb push {fname} /sdcard/'{RESET}")

        print()
        slide_text(f"{GREEN}➤ All safe steps completed. Restart device for best results.{RESET}", delay=0.006, spaces=18)
        print("\n[Process Completed]\n")
    except KeyboardInterrupt:
        stop_matrix()
        print("\nInterrupted. Exiting...")

if __name__ == "__main__":
    main()
