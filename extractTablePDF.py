#Importacion de librerias
import camelot
#import matplotlib.pyplot as plt

#Nombre del pdf a procesar
PATH='ComprobanteVirtual9_2019 (1).pdf'

#Procesar el documento PDF(PATH, parametro de agrupamiento, area de interes)
tables = camelot.read_pdf(PATH, flavor='stream',table_areas=['12,470,820,115'])
#tables = camelot.read_pdf('C:/Users/Bryan/Documents/Test/ComprobanteVirtual9_2019 (1).pdf', flavor='stream',edge_tol=500)

#first_table=tables[0]
#first_table.df
#tables.export('foo.csv', f='csv', compress=True)

#Exportar el resultado a un csv
tables[0].to_csv(name+'.csv')

#Exportar el resultado a un excel
tables[0].to_excel(name+'.xlsx')

#Imprimir en consola la tabla extraida
#print(tables[0].df)

#Plotear un dibujo de la tabla con el area de interes procesada
#camelot.plot(tables[0], kind='contour')
#plt.show()

