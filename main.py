import customer
import form

valid_customers = customer.load_valid_customers()

for valid_customers in valid_customers:
    form.fill_form(valid_customers)

#-------------------------------------------------------------
# TRAVA O BOT PARA NÃO FECHAR O NAVEGADOR
#-------------------------------------------------------------
#input()
