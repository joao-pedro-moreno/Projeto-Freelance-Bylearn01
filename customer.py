from dbfread import DBF

def load_valid_customers():

    customers = []

    for record in DBF('sales.dbf'):
        name = record['FULL_NAME']
        email = record['EMAIL']
        source = record['SOURCE']
        categories = record['CATEGORIES']
        customer_type = record['TYPE']
        rating = record['RATING']

        if len(name) > 1 and len(email) > 1 and len(source) > 1 and len(categories) > 1 and len(customer_type) > 1 and len(rating) > 0:

            customer = [name, email, source, categories, customer_type, rating]
            customers.append(customer)
    
    return customers