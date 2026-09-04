"""Render docs/assets/social-preview.html to social-preview.png at 2x.
Needs Playwright (pip install playwright && playwright install chromium) and the Inter
font files at ./inter/extras/ttf/ (download from rsms.github.io/inter)."""
from pathlib import Path
from playwright.sync_api import sync_playwright
here = Path(__file__).parent
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1280, "height": 640}, device_scale_factor=2)
    pg.goto((here / "social-preview.html").as_uri())
    pg.wait_for_timeout(300)
    pg.screenshot(path=str(here / "social-preview.png"))
    b.close()
print("wrote social-preview.png")
