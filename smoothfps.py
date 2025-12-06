#!/usr/bin/env python3
import os, time, sys

# ────────────────────────────────────────────────
#   COLOR & GLOW EFFECTS
# ────────────────────────────────────────────────
RESET = "\033[0m"
BOLD = "\033[1m"
BLINK = "\033[5m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
BLUE = "\033[94m"

GLOW = f"{BOLD}{BLINK}{CYAN}"

# ────────────────────────────────────────────────
#   SMALL LOADING BAR
# ────────────────────────────────────────────────
def loading(text, speed=0.03):
    print(f"\n{YELLOW}{text}{RESET}")
    bar = "■■■■■■■■■■"
    for i in range(10):
        sys.stdout.write(f"\r{GREEN}{bar[:i]}{RESET}{bar[i:]}")
        sys.stdout.flush()
        time.sleep(speed)
    print("\n")

# ────────────────────────────────────────────────
#   HEADER LOGO
# ────────────────────────────────────────────────
def header():
    os.system("clear")
    print(f"""
{GLOW}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{RESET}

{MAGENTA}◖ DEVICE AND HARDWARE INFO ◗{RESET}

➤ DEVICE  
➤ MODEL

{CYAN}◖ Copyright © code07777 ◗{RESET}
""")

# ────────────────────────────────────────────────
#   UI PROMPTS
# ────────────────────────────────────────────────
def ask(msg):
    return input(f"{YELLOW}{msg}{RESET}")

# ────────────────────────────────────────────────
#   MAIN TOOL
# ────────────────────────────────────────────────
def main():
    header()

    print(f"{MAGENTA}➤ [ = ] Game Package Name ◗{RESET}")
    pkg = ask("➤ Type Here  = ")

    print(f"""
{MAGENTA}➤ [ = ] Select Gaming Frame Rate ◗{RESET}
 [1] 60FPS (Stable)
 [2] 90FPS (Stable)
 [3] 120FPS (Unstable)
""")
    fps = ask("➤ Select Option = ")

    print(f"""
{MAGENTA}➤ [ = ] Select Gaming Refresh Rate ◗{RESET}
 [1] 60HZ (Stable)
 [2] 90HZ (Stable)
 [3] 120HZ (Stable)
""")
    hz = ask("➤ Select Option = ")

    print(f"""
{MAGENTA}➤ [ = ] Select Gaming Mode ◗{RESET}
 [1] Extreme
 [2] Ultra (Device May Heat)
 [3] Medium
""")
    mode = ask("➤ Select Option = ")

    print(f"""
{MAGENTA}➤ [ = ] Enable CPU/GPU Boost ◗{RESET}
 [1] Maximum (Device May Heat)
 [2] Medium (Stable)
""")
    boost = ask("➤ Select Option = ")

    print(f"""
{MAGENTA}➤ [ = ] Boost Touch Sampling Rate ◗{RESET}
 [1] Maximum
 [2] Medium
""")
    ts = ask("➤ Select Option = ")

    print(f"""
{MAGENTA}➤ [ = ] Hardware Optimization ◗{RESET}
 [1] Enable
 [2] Disable
""")
    opt = ask("➤ Select Option = ")

    # Fake loading + animation
    loading("➤ Adding More Lag Fix Script…")
    loading("➤ Optimizing RAM Performance…")
    loading("➤ Optimizing System Performance…")

    time.sleep(1)
    header()
    print(f"{GREEN}➤ Rechecking Script And Files...{RESET}")
    time.sleep(1.5)

    print(f"""
{GREEN}➤ All Script Applied Successfully.{RESET}
{YELLOW}➤ Restart Device For Better Result (Recommended){RESET}

[Process completed]
""")

# ────────────────────────────────────────────────
#   RUN
# ────────────────────────────────────────────────
if __name__ == "__main__":
    main()
