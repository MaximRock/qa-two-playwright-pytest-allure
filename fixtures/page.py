import pytest
from playwright.sync_api import Browser, BrowserContext, Page, sync_playwright
from playwright.sync_api._generated import Playwright

import config


@pytest.fixture(scope="class")
def page() -> Page:  # type: ignore
    playwright: Playwright = sync_playwright().start()
    if config.playwright.BROWSER == "firefox":
        browser: Browser = get_firefox_browser(playwright)
        context: BrowserContext = get_context(browser)
        page_data: Page = context.new_page()
    elif config.playwright.BROWSER == "chrome":
        browser: Browser = get_chrome_browser(playwright)
        context: BrowserContext = get_context(browser)
        page_data: Page = context.new_page()
    else:
        browser: Browser = get_chrome_browser(playwright)
        context: BrowserContext = get_context(browser)
        page_data: Page = context.new_page()
    yield page_data
    for context in browser.contexts:
        context.close()
    browser.close()
    playwright.stop()


def get_firefox_browser(playwright) -> Browser:
    return playwright.firefox.launch(
        headless=config.playwright.IS_HEADLESS,
        slow_mo=config.playwright.SLOW_MO,
        args=["--start-maximized"],
    )


def get_chrome_browser(playwright) -> Browser:
    return playwright.chromium.launch(
        headless=config.playwright.IS_HEADLESS,
        slow_mo=config.playwright.SLOW_MO,
        args=["--start-maximized"],
    )


def get_context(browser) -> BrowserContext:
    context = browser.new_context(
        viewport=config.playwright.PAGE_VIEWPORT_SIZE, locale=config.playwright.LOCALE
    )
    context.set_default_timeout(timeout=config.expectations.DEFAULT_TIMEOUT)
    return context
