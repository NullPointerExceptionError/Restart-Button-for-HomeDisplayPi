import RPi.GPIO as GPIO
import subprocess
import os
import signal
import time

# PIN for Button
BUTTON_PIN = 14

# path to script to restart
SCRIPT_PATH = '../HomeDisplayPi/src/main.py'

# path to venv of this script
VENV_PATH = '../HomeDisplayPi/venv'

# path to log-file in script folder
LOG_FILE_PATH = '../HomeDisplayPi/output.log'

def find_and_kill_process_by_script_name(script_name, status="S"):
    """finds process based on scriptname and status and kill it."""
    try:
        output = subprocess.check_output(['ps', '-eo', 'pid,state,cmd'], text=True)
        for line in output.splitlines():
            # filter processes which have scriptname and status
            if script_name in line or "../HomeDisplayPi/venv/bin/python ../HomeDisplayPi/src/main.py" in line and "python" in line: # the second condition occurs on restart by this program  
                parts = line.split(maxsplit=2)
                pid = int(parts[0])  # extract PID
                os.kill(pid, signal.SIGINT)  # kill process softly with Ctrl+C signal
                time.sleep(1)  # wait until process has ended
                return True
    except Exception as e:
        print(f"error ending the process: {e}")
    return False

def restart_script():
    """restarts script in venv"""
    try:
        subprocess.Popen(['setsid', 'nohup', f'{VENV_PATH}/bin/python', SCRIPT_PATH, '>', LOG_FILE_PATH, '2>&1', '&'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print(f"error restarting the script: {e}")

def button_callback(channel):
    """if button pressed do this"""
    find_and_kill_process_by_script_name("python src/main.py") # kill running process (if multiple running, it kills only one of them)
    restart_script()

def setup_gpio():
    """Init GPIO for Button."""
    GPIO.setmode(GPIO.BCM)  # use BCM-Mode for PIN-numbers
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Set Button-Pin as input with Pull-Up-resistor
    
    GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=button_callback, bouncetime=200) # connect callback function with button press 

def main():
    """wait for button press and restart script"""
    try:
        setup_gpio()
        while True: # wait for button press
            time.sleep(1)
    except KeyboardInterrupt:
        print("exit")
    finally:
        GPIO.cleanup()

# main logic
if __name__ == "__main__":
    main()



