from selenium.webdriver import Firefox, FirefoxOptions
from percy import percy_snapshot

# Browserstack production website URL
URL = 'https://www.browserstack.com/'

ENDPOINTS = {
    'homepage': '',
    'pricing page': 'pricing',
    'automate integration page': 'integrations/automate',
    'documentation page': 'docs'
    }


class TestClass():
    def setup_method(self):
        ff_options = FirefoxOptions()
        ff_options.add_argument('-headless')
        self.driver = Firefox(options=ff_options)

    def teardown_method(self):
        self.driver.quit()

    def test_bstack_percy(self):
        for ep in ENDPOINTS.items():
            self.driver.get(URL + ep[1])
            self.driver.implicitly_wait(10)
            percy_snapshot(driver=self.driver, name=ep[0] + ": responsive test",
                           widths=[375, 480, 720, 1280, 1440, 1920])

