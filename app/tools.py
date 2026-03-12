import pyautogui
from datetime import datetime
from pathlib import Path
from io import BytesIO
import base64


def take_screenshot(low_res=True) -> str:
    """Takes a screenshot, saves it, and returns a low-resolution inline image for Claude."""

    # Save in home/Screenshots
    home = Path.home()
    screenshots_dir = home / "Screenshots"
    screenshots_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = screenshots_dir / f"screenshot_{timestamp}.png"

    # Take screenshot
    screenshot = pyautogui.screenshot()

    # Reduce resolution if requested
    if low_res:
        # Resize to 25% of original size
        new_width = int(screenshot.width * 0.25)
        new_height = int(screenshot.height * 0.25)
        screenshot = screenshot.resize((new_width, new_height))

    # Save screenshot to disk
    screenshot.save(filename)

    # Convert to base64 for inline display
    buffered = BytesIO()
    screenshot.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")

    return f"Screenshot saved to {filename}\n\n<img src='data:image/png;base64,{img_str}' alt='screenshot' />"
