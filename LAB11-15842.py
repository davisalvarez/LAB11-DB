#UVG
#Bases de Datos
#Laboratorio 11
#
#Davis Alvarez - 15842

from pymongo import MongoClient
import pprint
from datetime import datetime
client = MongoClient()

db = client.lab15
db2 = client.lab152

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
cartsDone = db2.carts
#-----------------#
# PRODUCT CATALOG #
#-----------------#

#--------#
# Create #
#--------#
post_id = items.insert_many(mylist)

#------#
# Read #
#------#

pprint.pprint(items.find_one({"marca": "sager"}))

#----------------------#
# INVENTORY MANAGEMENT #
#----------------------#

#--------------------------#
# Agreagar a shopping cart #
#--------------------------#
#busca y agrega al carrito el id dek producto que se busca
def shoppingCart(name):

    #convierte el nombre por si acaso
    item = str(name)

    #lo busca en la db
    product = items.find_one({"marca": item})

    #lo muestra
    #pprint.pprint(product)

    #id del item en el dictionar
    myCartItemID = product['_id']

    #si ya esta en el carrito
    if myCartItemID in myCart:
        myCart[myCartItemID] = myCart[myCartItemID] + 1

    #si no lo esta
    else:
        myCart[myCartItemID] = 1



#Demostracion
print('buscando un producto sager ')
shoppingCart('sager')
print('cuando no hay ninugno en el carro lo pone como 1' ,  myCart)
shoppingCart('bolik')
shoppingCart('toyota')
shoppingCart('toyota')
shoppingCart('toyota')

print('buscando un producto sager ')
print('cuando hay mas de uno le suma como 1' , myCart)
print(myCart)

#---------------------------#
# Cambiar cantidad de items #
#---------------------------#
def cambiarenCarrito(id,num):
    product = items.find_one({"marca": str(id)})
    if not(product == None):
        currentAmount = myCart[product['_id']]
        newAmount = currentAmount + num
        myCart[product["_id"]] = newAmount
        print('Carrito actulizado')
        print(myCart)

    else:
        print('Producto no encontrado o numero no valido')

#agregando 5 sager al carrito
print('agregando 5 sager al carrito')
cambiarenCarrito('sager',5)

#-----------#
# Check out #
#-----------#
def checkOut():
    print('Su carrito contiene:')

    for i in myCart:
        print('* ' , myCart[i] , ' unidad(es) del producto con nombre' , items.find_one({"_id": i})['item'])

    checkOutDate = datetime.now()

    print(str(checkOutDate))
    cartDone = {"date": str(checkOutDate) , "content":myCart}
    print(cartDone)

checkOut()
