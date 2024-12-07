from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup


url = "https://ffdecks.com/card/1"

# Iniciar Playwright
with sync_playwright() as p:
    # Abrir un navegador Chromium
    browser = p.chromium.launch(headless=True)  # headless=False para ver el navegador
    page = browser.new_page()

    # Navegar a la URL
    page.goto(url)

    # Esperar 5 segundos
    page.wait_for_timeout(10000)

    # Obtener el contenido de la página
    html = page.content()

    # Usar BeautifulSoup para analizar el HTML
    soup = BeautifulSoup(html, 'lxml')

    # Extraer imágenes
    imagenes = soup.find_all('img')
    print("Imágenes encontradas:")
    for img in imagenes:
        if 'https' in img['src']:
            print(img['src'])

    # Cerrar el navegador
    browser.close()