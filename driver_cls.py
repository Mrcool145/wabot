from selenium import webdriver


class waDriver:
    def __init__(self, path=None):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--disable-blink-features")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--window-size=1420,1080")
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36")
        if path is not None:
            chrome_options.add_argument(f'--user-data-dir={path}')
            chrome_options.add_argument('--profile-directory=Default')
        self.driver = webdriver.Chrome('chromedriver', options=chrome_options)
        self.driver.implicitly_wait(40)
