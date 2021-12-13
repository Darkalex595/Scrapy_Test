import json, sys

def createInsert():
    with open('C:/Users/futbo/Documents/Clases/Reto/Scrapy_Test/books/books/books.json') as json_data:
            lista_libros = json.load(json_data)
            
    if type(lista_libros) == list:
        first_record = lista_libros[0]

    # print(first_record)

    columns = list(first_record.keys())
    # print ("\ncolumn names:", columns)

    table_name = "Libros"
    sql_string = 'INSERT INTO {} '.format( table_name )
    sql_string += "(" + ', '.join(columns) + ")\nVALUES "

    for i, record_dict in enumerate(lista_libros):

        # iterate over the values of each record dict object
        values = []
        for col_names, val in record_dict.items():

            # Postgres strings must be enclosed with single quotes
            if type(val) == str:
                # escape apostrophies with two single quotations
                val = val.replace("'", "''")
                val = "'" + val + "'"

            values += [ str(val) ]
            
        # join the list of values and enclose record in parenthesis
        sql_string += "(" + ', '.join(values) + "),\n"

    sql_string = sql_string[:-2] + ";"
    
    
    return sql_string
