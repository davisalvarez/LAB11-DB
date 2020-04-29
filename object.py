#UVG
#Bases de Datos
#Laboratorio 11
#
#Davis Alvarez - 15842

from pymongo import MongoClient
import pprint

client = MongoClient()

db = client.lab15

#pulled items from db
myCart = {}

mylist = [
    {"item":"lapiz","marca":"bolik","numero":2,"precio": 2},
    {"item":"carro","marca":"toyota","kilometraje":5000,"gasolina":"super","precio":120000},
    {"item":"pachon","volumen":1.5,"color":"rojo","precio":50},
    {"item":"laptop","marca":"sager","RAM":16,"procesador":"i7-7800","pantalla":15.3,"precio":8000},
    {"item":"mousepad","color":"negro","precio":25}
    ]

items = db.posts
print(items)

#-----------------#
# PRODUCT CATALOG #
#-----------------#

#Create
#post_id = items.insert_many(mylist)
#post_id

#Read
#pprint.pprint(items.find_one({"marca": "sager"}))

#----------------------#
# INVENTORY MANAGEMENT #
#----------------------#

#busca y agrega al carrito el id dek producto que se busca
def shoppingCart(name):

    #convierte el nombre por si acaso
    item = str(name)

    #lo busca en la db
    product = items.find_one({"marca": "sager"})

    #lo muestra
    pprint.pprint(product)

    #id del item en el dictionar
    myCartItemID = product['_id']

    #si ya esta en el carrito
    if myCartItemID in myCart:
        myCart[myCartItemID] = myCart[myCartItemID] + 1

    #si no lo esta
    else:
        myCart[myCartItemID] = 1



#Demostracion
shoppingCart('sager')
print(myCart)
shoppingCart('sager')

print(myCart)

def cambiarenCarrito(id,num):
    product = items.find_one({"_id": str(id)})
    if num.isdigit() and not(product == None):
        print('not done yet')

    else:
        print('Producto no encontrado o numero no valido')
