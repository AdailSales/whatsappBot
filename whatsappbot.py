#!/usr/bin/python3
# importar as bibliotecas
# navegar até o whatssapp web
# buscar contatos/ grupos
# definir contatos e grupos e mensagem a ser enviada
# campo de pesquisa 'copyable-text selectable-text'
# enviar mensagens para o contato ou grupo

from selenium import webdriver
import time
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get('https://web.whatsapp.com')
time.sleep(30)
contatos = ['Papu(Gomes) de cinema']
mensagem = 'Olá, tudo bem! Estou testando um bot. Não responda esta mensagem.'

def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)
    time.sleep(3)

def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)

for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)
