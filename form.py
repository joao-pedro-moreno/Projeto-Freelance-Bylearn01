import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#-------------------------------------------------------------
# INICIA O NAVEGADOR
#-------------------------------------------------------------

def start_browser():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get('https://forms.gle/rKfhMRdiE7qRjMK38')
    time.sleep(5)

    return browser


#-------------------------------------------------------------
# PREENCHE A LACUNA DE NOME
#-------------------------------------------------------------

def fill_name(browser, name):
    browser.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(name)

#-------------------------------------------------------------
# PREENCHE A LACUNA DE EMAIL
#-------------------------------------------------------------

def fill_email(browser, email):
    browser.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(email)

#-------------------------------------------------------------
# PREENCHE A LACUNA DE CATEGORIA DE VENDA
#-------------------------------------------------------------

def fill_source(browser, source):
    if source == 'Atacado':
        option = 1
    else:
        option = 2

    xpath_source = f'/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/span/div/div[{option}]/label/div/div[2]/div/span'

    browser.find_element_by_xpath(xpath_source).click()

#-------------------------------------------------------------
# PREENCHE A LACUNA DE CATEGORIA DE PRODUTO
#-------------------------------------------------------------

def fill_categories(browser, categories):

    category_list = categories.split(', ')

    for category in category_list:
        if category == 'Camisa':
            option = 1
        elif category == 'Calça':
            option = 2
        elif category == 'Vestido':
            option = 3
        else:
            option = 4

        xpath_categories = f'/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div[{option}]/label'

        browser.find_element_by_xpath(xpath_categories).click()

#-------------------------------------------------------------
# PREENCHE A LACUNA DE TIPO DE CONTA
#-------------------------------------------------------------

def fill_type(browser, customer_type):
    xpath_type = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[2]'

    if customer_type == 'Não Cadastrado':
        option = 3
    elif customer_type == 'Cadastrado':
        option = 4
    elif customer_type == 'Cliente Regular':
        option = 5
    else:
        option = 6

    xpath_customer = f'/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[2]/div[{option}]'

    browser.find_element_by_xpath(xpath_type).click()
    time.sleep(1)
    browser.find_element_by_xpath(xpath_customer).click()

#-------------------------------------------------------------
# PREENCHE A LACUNA DE AVALIAÇÃO
#-------------------------------------------------------------

def fill_rating(browser, rating):
    xpath_rating = f'/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/span/div/label[{rating}]/div[2]/div/div/div[3]/div'

    time.sleep(1)
    browser.find_element_by_xpath(xpath_rating).click()

#-------------------------------------------------------------
# ENVIAR O FORMULÁRIO
#-------------------------------------------------------------

def send_form(browser):
    time.sleep(1)

    browser.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span').click()

def fill_form(customer):
    browser = start_browser()
    fill_name(browser, customer[0])
    fill_email(browser, customer[1])
    fill_source(browser, customer[2])
    fill_categories(browser, customer[3])
    fill_type(browser, customer[4])
    fill_rating(browser, customer[5])
    send_form(browser)