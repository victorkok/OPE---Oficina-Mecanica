from PyQt5 import uic, QtWidgets
import sqlite3

def insertTable():
    connection = sqlite3.connect("accounts.db")
    linha1 = createa.nome.text()
    linha2 = createa.usuario.text()
    linha3 = createa.senha.text()
    linha4 = createa.senhac.text()

    if linha3 != linha4:
        createa.label.setText("Senhas não conferem")
    else:
        cursor = connection.cursor()
        sql = "INSERT INTO user(cargo,nome,usuario,senha) VALUES(?,?,?,?)"
        cursor.execute(sql,['common',linha1,linha2,linha3])
        connection.commit()

        connection.close()

        linha1 = createa.nome.setText("")
        linha2 = createa.usuario.setText("")
        linha3 = createa.senha.setText("")
        linha4 = createa.senhac.setText("")


    
def check():
    connection = sqlite3.connect("accounts.db")
    usuario = login.usuario.text()
    senha = login.senha.text()

    cursor = connection.cursor()
    sql = ("SELECT * FROM user WHERE usuario = ? AND senha = ?")
    cursor.execute(sql,[usuario,senha])
    results = cursor.fetchall()

    if results:
        menu.show()
    else:
        login.dados.setText("Dados não conferem")


def addStock():
    cursor = connection.cursor()
    connection = sqlite3.connect("Estoque.db")
    formulario.show()
    global linha1
    global linha2

    linha1 = formulario.codigo.text()
    linha2 = formulario.quantidade.text()
    sql = "UPDATE Estoque SET qtd = qtd + ? WHERE codigo = ?"

    cursor.execute(sql,[quantidade,codigo])
    connection.commit()

    print("Código:",linha1)
    print("Descricao:",linha2)
    formulario.codigo.setText("")
    formulario.quantidade.setText("")

def removeStock():
    cursor = connection.cursor()
    connection = sqlite3.connect("Estoque.db")
    remov.show()
    global linha1r
    global linha2r

    linha1r = remov.codigor.text()
    linha2r = remov.quantidader.text()
    sql = "UPDATE Estoque SET qtd = qtd - ? WHERE codigo = ?"
    cursor.execute(sql,[quantidade,codigo])
    connection.commit()

    print("Código:",linha1r)
    print("Descricao:",linha2r)
    remov.codigor.setText("")
    remov.quantidader.setText("")

def insert_service():
    connection = sqlite3.connect("Estoque.db")
    cursor = connection.cursor()
    global b
    global c
    global d
        
    
    b = adcmat.produto.text()
    c = adcmat.valor.text()
    d = adcmat.quantidade.text()


    sql = 'INSERT INTO Estoque ( produto,valor,qtd) VALUES (?,?,?)'
    cursor.execute(sql,[b,c,d])
    connection.commit()
    adcmat.produto.setText("")
    adcmat.valor.setText("")
    adcmat.quantidade.setText("")

def listProducts():
    connection = sqlite3.connect("Estoque.db")
    cursor = connection.cursor()
    listprod.show()
    sql = 'SELECT * FROM Estoque'
    cursor.execute(sql)
    myresult = cursor.fetchall()
    print(myresult)
    listprod.tableWidget.setRowCount(len(myresult))
    listprod.tableWidget.setColumnCount(4)
    lista = ['Codigo', 'Nome do Produto','Valor', 'Quantidade']
    listprod.tableWidget.setHorizontalHeaderLabels(list(lista))
    listprod.tableWidget.setColumnWidth(1,260)

    for x in range(0, len(myresult)):
        for y in range(0,4):
            listprod.tableWidget.setItem(x,y,QtWidgets.QTableWidgetItem(str(myresult[x][y])))

def items_clear():
    for y in range(0,5):
        for x in range(0,4):
            listprod.tableWidget.setItem(y,x,QtWidgets.QTableWidgetItem(''))
      

def search():
    connection = sqlite3.connect("Estoque.db")
    cursor = connection.cursor()
    pesq = listprod.pesquisa.text() 
    sql ="SELECT * FROM Estoque WHERE produto LIKE ?"
    pesq = '%' + pesq + '%'
    cursor.execute(sql,[pesq])
    myresult = cursor.fetchall()
    items_clear()
    listprod.tableWidget.setRowCount(len(myresult))
    listprod.tableWidget.setColumnCount(4)  
    for x in range(0, len(myresult)):
        for y in range(0,4):
            listprod.tableWidget.setItem(x,y,QtWidgets.QTableWidgetItem(str(myresult[x][y])))
    print(myresult) 





#-----tela de criação do usuario
app=QtWidgets.QApplication([])
createa=uic.loadUi("usuario.ui")
createa.button.clicked.connect(insertTable)

#tela de login
login=uic.loadUi("user.ui")
login.semconta.clicked.connect(createa.show)
login.logar.clicked.connect(check)
login.show()

#-----tela de material
adcmat=uic.loadUi("adcmaterial.ui")
adcmat.button.clicked.connect(insert_service)

#-----tela de produtos
listprod=uic.loadUi("list.ui")
listprod.buttonp.clicked.connect(search)

#-----tela de remover estoque
remov=uic.loadUi("Estoquer.ui")
remov.buttonr.clicked.connect(removeStock)

#-----tela de adc estoque
formulario=uic.loadUi("Estoque.ui")
formulario.button.clicked.connect(addStock)

#menu princpal
menu=uic.loadUi("menu_Principal.ui")
menu.button_estoque.clicked.connect(addStock)
menu.button_venda.clicked.connect(removeStock)
menu.material.clicked.connect(adcmat.show)
menu.button_produtos.clicked.connect(listProducts)









app.exec()




'''connection = sqlite3.connect("accounts.db")

cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS user (cargo varchar(30), nome varchar(20), usuario varchar(30), senha varchar(30))"

cursor.execute(create_table)

tables = cursor.fetchall()

connection = sqlite3.connect("Estoque.db")

cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS Estoque (codigo INTEGER PRIMARY KEY AUTOINCREMENT, produto varchar(30), valor decimal (5,2) not null, qtd int not null)"

cursor.execute(create_table)

tables = cursor.fetchall()
'''

