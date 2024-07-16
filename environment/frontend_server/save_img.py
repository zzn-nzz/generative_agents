from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument(
    "--name", default="July1_the_ville_isabella_maria_klaus-step-3-20", type=str
)
parser.add_argument("--step", default=1, type=int)
parser.add_argument("--speed", default=3, type=int)
parser.add_argument(
    "--save_path",
    default="saved_images",
    type=str,
)
parser.add_argument("--interval", default=3, type=int)  # seconds
parser.add_argument("--iterations", default=10, type=int)  # total screenshots
args = parser.parse_args()

page_path = f"http://localhost:8000/demo/{args.name}/{args.step}/{args.speed}/"
save_path = args.save_path
if not os.path.exists(save_path):
    os.makedirs(save_path)


# async def get_img_pyp():
#     # not working
#     browser = await launch()
#     page = await browser.newPage()
#     await asyncio.gather(
#         page.waitForNavigation({"waitUntil": "networkidle0"}),
#         page.goto(page_path, {"timeout": 60000}),
#     )
#     await page.screenshot({"path": save_path})
#     await browser.close()


# asyncio.run(get_img_pyp())

# def get_img_sel():
#     driver = webdriver.Chrome()

#     driver.get(page_path)

#     time.sleep(3)
#     # # Find <canvas> element
#     # canvas = driver.find_element(By.CSS_SELECTOR, 'canvas')
#     # location = canvas.location
#     # size = canvas.size
#     driver.save_screenshot(save_path)

#     # im = Image.open(screenshot_path)
#     # left = location['x']
#     # top = location['y']
#     # right = left + size['width']
#     # bottom = top + size['height']

#     # im_cropped = im.crop((left, top, right, bottom))
#     # im_cropped.save(f'{args.save_path}/canvas_screenshot_{args.name}_{args.step}.png')

#     driver.quit()


def get_img_sel():
    driver = webdriver.Chrome()

    driver.get(page_path)
    time.sleep(3)

    total_height = driver.execute_script("return document.body.scrollHeight")
    viewport_height = driver.execute_script("return window.innerHeight")
    num_screenshots = total_height // viewport_height + 1

    start_time = time.time()

    for i in range(args.iterations):
        elapsed_time = int(time.time() - start_time)
        for j in range(num_screenshots):
            driver.execute_script(f"window.scrollTo(0, {j * viewport_height});")
            time.sleep(3)
            screenshot_path = os.path.join(
                save_path, f"{args.name}_{elapsed_time}_screenshot_{j + 1}.png"
            )
            driver.save_screenshot(screenshot_path)
            print(f"Saved screenshot: {screenshot_path}")

        time.sleep(args.interval)

    driver.quit()


get_img_sel()
