import pyautogui
from datetime import datetime
from pathlib import Path


def take_screenshot() -> str:
    """Takes a screenshot of the current screen"""

    screenshots_dir = Path("screenshots")
    screenshots_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = screenshots_dir / f"screenshot_{timestamp}.png"

    screenshot = pyautogui.screenshot()
    screenshot.save(filename)

    return f"Screenshot saved to {filename}"
