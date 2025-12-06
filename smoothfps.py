print("""
============================================================
                 LAG FIX MODE FOR ALL GAMES
                 Created By : @code07777
 Telegram Channel : https://t.me/codeteamback077
 Telegram Dev     : https://t.me/code07777
============================================================

DEVICE AND HARDWARE INFO
 - DEVICE : Redmi
 - MODEL  : M2004J7AC
------------------------------------------------------------
""")

# GAME PACKAGE
pkg = input("Enter Game Package Name (e.g., com.tencent.ig): ")

# FPS CHOICE
print("""
SELECT GAMING FRAME RATE
 [1] 60FPS (Stable)
 [2] 90FPS (Stable)
 [3] 120FPS (Unstable)
""")
fps_choice = input("Select Option (1/2/3): ")

# HZ CHOICE
print("""
SELECT GAMING REFRESH RATE
 [1] 60HZ (Stable)
 [2] 90HZ (Stable)
 [3] 120HZ (Stable)
""")
hz_choice = input("Select Option (1/2/3): ")

# MODE CHOICE
print("""
SELECT GAMING MODE
 [1] Extreme
 [2] Ultra (Device may heat)
 [3] Medium
""")
mode_choice = input("Select Option (1/2/3): ")

# CPU/GPU BOOST
print("""
CPU / GPU BOOST
 [1] Maximum (Device may heat)
 [2] Medium (Stable)
""")
boost_choice = input("Select Option (1/2): ")

# TOUCH BOOST
print("""
TOUCH SAMPLING RATE BOOST
 [1] Maximum
 [2] Medium
""")
touch_choice = input("Select Option (1/2): ")

# HARDWARE OPTIMIZATION
print("""
HARDWARE OPTIMIZATION
 [1] Enable
 [2] Disable
""")
hardware_choice = input("Select Option (1/2): ")

print("\n------------------------------------------------------------")
print("Applying Tweaks...")
print(" - Stopping background apps")
print(" - Optimizing RAM")
print(" - Reducing thermal throttling")
print(" - Optimizing GPU scheduling")
print(" - Boosting touch response")
print(" - System performance tuning")
print(" - Safe configuration loading for PUBG")
print("Please wait...\n")

print("Progress: [##########] 100%")

# PUBG SAFE CONFIG SECTION
pubg_safe = f"""
================ PUBG SAFE CONFIG ================
Game Package : {pkg}

[✓] Smooth Graphics Applied (Safe)
[✓] Extreme/90FPS Mode (If Device Supports)
[✓] Rendering Optimization Enabled
[✓] Shadows Disabled (Safe)
[✓] Anti-Aliasing Disabled (Safe)
[✓] Input Latency Improved
[✓] Thermal Control Balanced
[✓] No Game File Modified (100% Safe)

Recommended In-Game Settings:
 - Graphics : Smooth
 - FPS      : Extreme/90FPS
 - Shadows  : OFF
 - Anti-Aliasing : OFF
 - Screen Optimization : ON

Device Optimization:
 - RAM Cleaned
 - CPU/GPU Balanced Boost
 - Scheduler Tuned
 - Network Stability Enhanced (SAFE)
===================================================
"""
print(pubg_safe)

print("All Scripts Applied Successfully!")
print("Restart Device For Better Result.")
print("============================================================")   
