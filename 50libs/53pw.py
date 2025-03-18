from playwright.sync_api import sync_playwright

# Данные для входа
login_url = "https://ivcs.hi-tech.org"
username = "petr.sukhov@iva-tech.ru"
password = "PASSWord"

# Запуск Playwright
with sync_playwright() as p:
    # Запуск браузера (например, Chromium)
    browser = p.chromium.launch(headless=False)  # headless=False для визуального отображения
    page = browser.new_page()
    #peter.sh

    # Переход на страницу входа
    page.goto(login_url)

    # Заполнение формы входа
    page.fill('input[formcontrolname="login"]', username)  # Замените селектор на актуальный
    page.fill('input[formcontrolname="password"]', password)  # Замените селектор на актуальный

    # Нажатие кнопки входа
    page.click('button[type="submit"]')  # Замените селектор на актуальный

    # Ожидание загрузки следующей страницы (например, по наличию элемента на новой странице)
    page.wait_for_selector('.participant-icon-border-container')  # Замените селектор на актуальный

    # Скриншот для проверки
    page.screenshot(path="screenshot.png")

    # Закрытие браузера
    browser.close()