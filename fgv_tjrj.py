import os
import time
from playwright.sync_api import Playwright, sync_playwright, expect
from procesaDados import processa_dados
from mensagem import exibir_mensagem

def run(playwright: Playwright) -> None:
    
    cache = os.path.dirname(os.path.abspath(__file__))
    cache = cache + r"\cache"
    if not os.path.exists(cache):    
        os.makedirs(cache)
    
    #browser = playwright.chromium.launch(headless=False)
    context = playwright.chromium.launch_persistent_context(
                user_data_dir=cache,
                headless=False,
                permissions=["geolocation"],
                geolocation={"latitude": -22.8918242631086, "longitude": -43.110534273061255},
                locale='pt-BR'
            )
    page = context.new_page()
    exibir_mensagem("Acessando página do TJRJ!")
    page.goto("https://www3.tjrj.jus.br/consultaprocessual/#/consultapublica#porNome")
    page.wait_for_load_state("load")
    page.wait_for_timeout(1000)
   # Obter o frame 
    main_frame = page.frame_locator("#mainframe")
    time.sleep(0.5)
    exibir_mensagem("Preenchendo fomulário!")
    main_frame.get_by_role("tab", name="Por Nome", exact=True).click()

    main_frame.get_by_role("combobox", name="Selecione uma opção e clique").click()
    main_frame.get_by_role("option", name="1ª Instância").click()   
    time.sleep(0.5)
    main_frame.get_by_placeholder("Informe o nome da parte").fill("Fundação Getulio Vargas")
    main_frame.get_by_label("Comarca *").click()
    main_frame.get_by_role("option", name="Todas as Comarcas").click()
    main_frame.get_by_label("Por Nome", exact=True).locator("app-dropdown").filter(has_text="Competência *Acidentes do").locator("div").nth(2).click()
    main_frame.get_by_role("option", name="Cível", exact=True).click()
    exibir_mensagem("Iniciando a pesquisa!")
    main_frame.get_by_role("button", name="Pesquisar").click()
    main_frame.get_by_label("dropdown trigger").click()
    main_frame.get_by_text("300").click()
    
    # Localizar o elemento que contém o número do processo
    requerente_element = main_frame.locator("div:has-text('Processo:')").first

    # Extrair o número do processo
    requerente_texto = requerente_element.inner_text()  

    exibir_mensagem("Coletando dados!")
    processa_dados(requerente_texto)
    
    # ---------------------
    context.close()
   


with sync_playwright() as playwright:
    run(playwright)