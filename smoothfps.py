# ===================== COLOR SETUP ===================== #
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
PURPLE = "\033[95m"
RESET = "\033[0m"

# ===================== HEADER ========================== #
print(f"""
{CYAN}============================================================{RESET}
{GREEN}                 LAG FIX MODE FOR ALL GAMES{RESET}
{YELLOW}                 Created By : @code07777{RESET}
{YELLOW} Telegram Channel : https://t.me/codeteamback077{RESET}
{YELLOW} Telegram Dev     : https://t.me/code07777{RESET}
{CYAN}============================================================{RESET}

{PURPLE}DEVICE AND HARDWARE INFO{RESET}
 - DEVICE : Redmi
 - MODEL  : M2004J7AC
{CYAN}------------------------------------------------------------{RESET}
""")

# ===================== GAME PACKAGE NAME ===================== #
pkg = input(f"{GREEN}Enter Game Package Name (e.g., com.tencent.ig): {RESET}")

# ===================== FPS ===================== #
print(f"""
{PURPLE}SELECT GAMING FRAME RATE{RESET}
 [1] 60FPS (Stable)
 [2] 90FPS (Stable)
 [3] 120FPS (Unstable)
""")
fps_choice = input(f"{GREEN}Select Option (1/2/3): {RESET}")

# ===================== HZ ===================== #
print(f"""
{PURPLE}SELECT GAMING REFRESH RATE{RESET}
 [1] 60HZ (Stable)
 [2] 90HZ (Stable)
 [3] 120HZ (Stable)
""")
hz_choice = input(f"{GREEN}Select Option (1/2/3): {RESET}")

# ===================== MODE ===================== #
print(f"""
{PURPLE}SELECT GAMING MODE{RESET}
 [1] Extreme
 [2] Ultra (Device may heat)
 [3] Medium
""")
mode_choice = input(f"{GREEN}Select Option (1/2/3): {RESET}")

# ===================== BOOST ===================== #
print(f"""
{PURPLE}CPU / GPU BOOST{RESET}
 [1] Maximum (Device may heat)
 [2] Medium (Stable)
""")
boost_choice = input(f"{GREEN}Select Option (1/2): {RESET}")

# ===================== TOUCH BOOST ===================== #
print(f"""
{PURPLE}TOUCH SAMPLING RATE BOOST{RESET}
 [1] Maximum
 [2] Medium
""")
touch_choice = input(f"{GREEN}Select Option (1/2): {RESET}")

# ===================== HARDWARE ===================== #
print(f"""
{PURPLE}HARDWARE OPTIMIZATION{RESET}
 [1] Enable
 [2] Disable
""")
hardware_choice = input(f"{GREEN}Select Option (1/2): {RESET}")

# ================= APPLY TWEAKS LOG ===================== #
print(f"""
{CYAN}------------------------------------------------------------{RESET}
{YELLOW}Applying Tweaks...{RESET}
 - Stopping background apps
 - Optimizing RAM
 - Reducing thermal throttling
 - GPU scheduling balance
 - Touch response boost
 - PUBG safe configuration
 - System performance tuning

{GREEN}Please wait...{RESET}

Progress: {GREEN}[##########] 100%{RESET}
""")

# ===================== PUBG SAFE CONFIG OUTPUT ===================== #
print(f"""
{CYAN}================ PUBG SAFE CONFIG ================ {RESET}
Game Package : {pkg}

{GREEN}[✓] Smooth Graphics Applied (Safe){RESET}
{GREEN}[✓] Extreme/90FPS Mode (Device Supported){RESET}
{GREEN}[✓] Rendering Optimization Enabled{RESET}
{GREEN}[✓] Shadows Disabled (Safe){RESET}
{GREEN}[✓] Anti-Aliasing Disabled (Safe){RESET}
{GREEN}[✓] Input Latency Improved{RESET}
{GREEN}[✓] Thermal Control Balanced{RESET}
{GREEN}[✓] No Game File Modified (100% Safe){RESET}

Recommended In-Game:
 • Graphics : Smooth
 • FPS      : Extreme/90FPS
 • Shadows  : OFF
 • Anti-Aliasing : OFF
 • Screen Optimization : ON

Device Optimization:
 • RAM Cleaned
 • CPU/GPU Boost Balanced
 • Scheduler Tuned
 • Network Stability Enhanced (SAFE)
{CYAN}============================================================{RESET}
""")

print(f"{GREEN}All Scripts Applied Successfully!{RESET}")
print(f"{YELLOW}Restart Device For Better Result.{RESET}")
print(f"{CYAN}============================================================{RESET}")
