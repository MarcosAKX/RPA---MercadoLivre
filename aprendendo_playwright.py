from playwright.sync_api import sync_playwright


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
    
    print(f"Encontrados {len(titulos)} títulos")
    print(f"Encontrados {len(precos)} preços\n")
    
    # Mostra os primeiros 10
    for i in range(min(10, len(titulos), len(precos))):
        print(f"\n{i+1}. {titulos[i]}")
        print(f"   Preço: R$ {precos[i]}")

    
    
    browser.close()