from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup


f = open("imagenes.txt", "w")



# Iniciar Playwright
with sync_playwright() as p:
    # Abrir un navegador Chromium
    browser = p.chromium.launch(headless=True)  # headless=False para ver el navegador
    page = browser.new_page()

    for numero in range(1,21):
        url = f"https://ffdecks.com/card/{numero}" 

        page.goto(url)

        # Esperar 5 segundos
        page.wait_for_timeout(10000)

        # Obtener el contenido de la página
        html = page.content()

        # Usar BeautifulSoup para analizar el HTML
        soup = BeautifulSoup(html, 'lxml')

        # Extraer imágenes
        imagenes = soup.find_all('img')
        for img in imagenes:
            if 'https' in img['src']:
                f.write(f"{img['src']} - Card {numero}\n")
                
    f.close()
    # Cerrar el navegador
    browser.close()
