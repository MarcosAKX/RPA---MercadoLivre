from playwright.sync_api import sync_playwright
import pandas as pd

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    page.goto("https://www.mercadolivre.com.br")
    page.fill('input[name="as_word"]', "notebook")
    page.press('input[name="as_word"]', "Enter")
    
    # Espera os produtos carregarem
    page.wait_for_selector('.poly-component__title')
    
    # Extrai os títulos
    titulos = page.locator('.poly-component__title').all_text_contents()
    # Extrai os preços
    precos = page.locator('span.andes-money-amount__fraction').all_text_contents()

    titulos = titulos[:10]
    precos = precos[:10]

    df = pd.DataFrame({
        "Produto" : titulos,
        "Preços$" : precos
    })

    df.to_excel("produtos_playwright.xlsx", index=False)

    print("\n✅ Planilha criada com sucesso!")
    print(df)

    browser.close()