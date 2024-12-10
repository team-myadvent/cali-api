from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
)


def get_youtube_search_results(query):
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(f"https://www.youtube.com/results?search_query={query}")

    wait = WebDriverWait(driver, 10)
    videos = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ytd-video-renderer")))

    results = []
    for video in videos:
        title = video.find_element(By.CSS_SELECTOR, "#video-title").text
        link = video.find_element(By.CSS_SELECTOR, "#video-title").get_attribute("href")
        video_id = link.split("v=")[-1].split("&")[0]
        results.append({"title": title, "link": link, "youtube_video_id": video_id})

    driver.quit()
    return results
