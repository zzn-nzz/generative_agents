from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from pyppeteer import launch
from PIL import Image
import time
import argparse
import asyncio

parser = argparse.ArgumentParser()
parser.add_argument('--name', default="1step", type=str)
parser.add_argument('--step', default=1, type=int)
parser.add_argument('--speed', default=3, type=int)
parser.add_argument('--save_path', default="saved_images", type=str)

args = parser.parse_args()

page_path = f'http://localhost:8000/demo/{args.name}/{args.step}/{args.speed}/'
save_path = f'saved_images/{args.name}_{args.step}_screenshot.png'

async def get_img_pyp():
    # not working
    browser = await launch()
    page = await browser.newPage()
    await asyncio.gather(
        page.waitForNavigation({'waitUntil': 'networkidle0'}),
        page.goto(page_path, {'timeout': 60000})
    )
    await page.screenshot({'path': save_path})
    await browser.close()
    
# asyncio.run(get_img_pyp())

def get_img_sel():
    driver = webdriver.Chrome()

    driver.get(page_path) 

    time.sleep(3)
    # # Find <canvas> element
    # canvas = driver.find_element(By.CSS_SELECTOR, 'canvas') 
    # location = canvas.location
    # size = canvas.size
    driver.save_screenshot(save_path)

    # im = Image.open(screenshot_path)
    # left = location['x']
    # top = location['y']
    # right = left + size['width']
    # bottom = top + size['height']

    # im_cropped = im.crop((left, top, right, bottom))
    # im_cropped.save(f'{args.save_path}/canvas_screenshot_{args.name}_{args.step}.png')

    driver.quit()

get_img_sel()