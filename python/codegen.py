import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://e.lsi1.hr.dmerej.info/")
    page.get_by_role("link", name="Add new employee").click()
    page.get_by_placeholder("Name").click()
    page.get_by_placeholder("Name").fill("nom")
    page.get_by_placeholder("Email").click()
    page.get_by_placeholder("Email").fill("email@email.fr")
    page.locator("#id_address_line1").click()
    page.locator("#id_address_line1").fill("3 rue rien")
    page.locator("#id_address_line2").click()
    page.locator("#id_address_line2").fill("complement")
    page.get_by_placeholder("City").click()
    page.get_by_placeholder("City").fill("ville")
    page.get_by_placeholder("Zip code").click()
    page.get_by_placeholder("Zip code").fill("00000")
    page.get_by_placeholder("Hiring date").fill("2025-01-12")
    page.get_by_placeholder("Job title").click()
    page.get_by_placeholder("Job title").fill("titre")
    page.get_by_role("button", name="Add").click()
    expect(page.locator("tbody")).to_contain_text("nom")
    page.get_by_role("link", name="Home").click()
    page.get_by_role("link", name="List employees").click()
    expect(page.locator("tbody")).to_contain_text("nom")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)