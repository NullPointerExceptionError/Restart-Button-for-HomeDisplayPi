# Restart-Button-for-HomeDisplayPi (Add-On)
An extra GPIO Button to restart [HomeDisplayPi](https://github.com/NullPointerExceptionError/HomeDisplayPi) if it's stuck or doesn't work properly.

## Installation
1. Connect your button as described below
2. Install and use [HomeDisplayPi](https://github.com/NullPointerExceptionError/HomeDisplayPi)
3. Clone this repository (just download it if you haven't installed git)
   ```bash
   git clone https://github.com/NullPointerExceptionError/Restart-Button-for-HomeDisplayPi.git
   ```
4. Navigate into the Restart-Button-for-HomeDisplayPi folder
5. Create and activate virtual environment
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
6. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

## Wiring
| GPIO- | PIN on Raspberry | port on device | device |
| - | - | - | - |
| 8 | GPIO-14 (TXD) | upper left pin | button |
| 6 | GND | lower left pin | button |

Take the rest of the [HomeDisplayPi](https://github.com/NullPointerExceptionError/HomeDisplayPi) Readme.

## How to use
1. Activate virtual environment in the HomeDisplayPi folder
   ```bash
   source venv/bin/activate
   ```
2. Start the program
   ```bash
   python3 main.py &
   ```
   If you want to have a log file with errors, use the following command instead (also possible via ssh).
   ```bash
   nohup python3 main.py > output.log 2>&1 &
   ```
3. Press the button to restart HomeDisplayPi.

To stop the program use
```bash
ps aux | grep main.py
kill -2 <PID>
```
replace `<PID>` with the far left number of the correct process (something like `main.py`).
