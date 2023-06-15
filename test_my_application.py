import re

import pytest
from playwright.sync_api import Mouse, Playwright, expect, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://odbdev.com/hse/home")
    page.get_by_label("Username").click()
    page.get_by_label("Username").fill("A448353")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("12345")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("heading", name="Incident Mgt").click()
    expect(page).to_have_url(re.compile(".*hse/incident-mgt"))
    page.locator("div").filter(has_text=re.compile(r"^Create Incident$")).nth(1).click()
    page.get_by_label("Clear").check()
    person=page.get_by_text("Ian Ashman")
    person.click()
    person.page.mouse.wheel(float(0),float(0.5))
    pickedPerson = page.get_by_text("Ryan Lutchman")
    while page.locator(".ant-select-dropdown").first.is_visible() :
        try:
            pickedPerson.click(timeout=100)
        except:
            person.page.mouse.wheel(float(0),float(0.5))
    checkPerson=  page.locator("div").filter(has_text=re.compile(r"^Ryan Lutchman$")).first
    expect(checkPerson).to_be_visible()
    pickedPerson = page.get_by_text("Logistics")
    person = page.get_by_label("Specific Incident Location")
    person.click()
    person.page.mouse.wheel(float(0),float(0.5))
    while page.locator(".ant-select-dropdown").nth(1).is_visible() :
        try:
            pickedPerson.click(timeout=100)
        except:
            person.page.mouse.wheel(float(0),float(0.5))
    
    page.get_by_label("Incident Reported").click()
    page.get_by_role("cell", name="15").get_by_text("15").click()
    page.get_by_text("16").nth(1).click()
    page.get_by_text("47").click()
    page.get_by_role("button", name="OK").click()

    page.get_by_label("Date & Time of Incident").click()
    page.get_by_role("cell", name="15").get_by_text("15").click()
    page.locator("li:nth-child(19) > .ant-picker-time-panel-cell-inner").first.click()
    page.get_by_role("listitem").filter(has_text="46").locator("div").click()
    page.get_by_role("button", name="OK").click()

    page.get_by_label("Occupational Illness/Personal Injury").check()
    page.locator("[id=\"__next\"] div").filter(has_text="CreateThis form is to be completed and submitted to the HSSE, Insurance & HR Dep").nth(2).click()
    page.get_by_placeholder("Enter please provide a brief description of the incident (describe damage to plant and equipment)...").fill("This is a test ")
    page.get_by_placeholder("Enter was the person(s) on a site visit or performing works in accordance with a sop, jsa or permit to work at the time of the incident?...").click()
    page.get_by_placeholder("Enter was the person(s) on a site visit or performing works in accordance with a sop, jsa or permit to work at the time of the incident?...").fill("This is another test")
    page.get_by_placeholder("Enter were there any nearby cameras or cctvs? (please indicate the locations)...").click()
    page.get_by_placeholder("Enter were there any nearby cameras or cctvs? (please indicate the locations)...").fill("One more after this ")
    page.get_by_placeholder("Enter tools/equipment involved...").click()
    page.get_by_placeholder("Enter tools/equipment involved...").fill("This is the final test")
    page.get_by_role("button", name="plus Create").click()
    page.get_by_role("button", name="Yes").click()
    page.locator("div").filter(has_text=re.compile(r"^Employees InvolvedEmployees InvolvedColumns$")).get_by_role("button", name="plus Employees Involved").click()
    page.get_by_label("Employee", exact=True).click()
    person = page.get_by_text("Adrian Dabiedeen - 448517")
    person.click()
    pixels = float(0)
    pixels = pixels +float(0.5)
    person.page.mouse.wheel(float(0),pixels)
    pickedPerson = page.get_by_text("Bernadine Warrick - 448382")
    while page.locator(".ant-select-dropdown").is_visible() :
        try:
            pickedPerson.click(timeout=100)
        except:
            person.page.mouse.wheel(float(0),float(0.5))

    page.get_by_label("Type of Involvement").click()
    page.get_by_text("Injured", exact=True).click()
    page.get_by_label("Type of Injury").click()
    page.get_by_text("Burns", exact=True).click()
    page.get_by_placeholder("Enter describe the nature of their injuries...").click()
    page.get_by_placeholder("Enter describe the nature of their injuries...").fill("This is an incident")
    page.locator("#ppe_worn_yn").get_by_text("YES").click()
    page.get_by_placeholder("Enter what chemical was the person exposed to? ...").click()
    page.get_by_placeholder("Enter what chemical was the person exposed to? ...").fill("THis is a chemical")
    page.locator("div").filter(has_text=re.compile(r"^What chemical was the person exposed to\? THis is a chemical$")).nth(1).click()
    page.get_by_placeholder("Enter medical diagnosis (where applicable) ...").click()
    page.get_by_placeholder("Enter medical diagnosis (where applicable) ...").fill("This is a medical diagnosis")
    page.get_by_placeholder("Enter comments...").click()
    page.get_by_placeholder("Enter comments...").fill("This is a comment")
    page.get_by_role("button", name="plus Create").click()

with sync_playwright() as playwright:
    run(playwright)
