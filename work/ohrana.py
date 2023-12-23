import sys
import sqlite3 as sq 
from PyQt6.QtWidgets import QListWidget, QMainWindow ,QApplication, QWidget, QLabel, QPushButton, QVBoxLayout , QLineEdit,QRadioButton, QMessageBox
import time
from PyQt6.QtCore import QSize, Qt
employees=20
guests=5

current=[("Алексеев","Илья","Алексеевич","23-Apr-1994","директор по информатизации","+79993456785","aleksee45@mail.ru","NULL","NULL"),
("Аржанов","Владислав","Александрович","27-Jan-1995","начальние отдела кадров","+79063194556","arhjanov12@yandex.ru","NULL","NULL"),
("Белоцерковец ","Дмитрий","Александрович","12-Sep-1983","менеджер","+79773332123","belotserkovets@gmail.com","NULL","NULL"),
("Богушев","Арсений","Александрович","09-Dec-1973","директор","+79264444334","Bogushev@mail.ru","NULL","NULL"),
("Гундарова","Софья","Анатольевна","30-Nov-1995","менеджер","+79256789012","Gundarova@yandex.ru","NULL","NULL"),
("Долженков","Борис","Алексеевич","23-Jun-2002","курьер","+79003196748","Dolzhenkov@gmail.com","NULL","NULL"),
("Журавова","Ангелина","Сергеевна","17-Aug-2002","специалист по корреспонденции","+79836571245","Zhuravova@gmail.com","NULL","NULL"),
("Клевцова","Варвара","Андреевна","15-Oct-2002","секретарь","+79023672156","Klevtsova@gmail.com","NULL","NULL"),
("Коваленко","Вероника","Александровна","17-Jul-1997","менеджер","+79271285522","Kovalenko@gmail.com","NULL","NULL"),
("Королев","Платон","Валеорьевич","13-Mar-1993","главный бухгалтер","+79773045689","Korolev@gmail.com","NULL","NULL"),
("Кубышкин","Роман","Евгеньевич","10-Oct-1985","менеджер по технологии","+79013219045","Kubyshkin@gmail.com","NULL","NULL"),
("Макаренко","Константин","Викторович","11-Nov-1984","бизнес аналитик","+79992341289","Makarenko@gmail.com","NULL","NULL"),
("Мартиросов","Артемий","Артурович","01-Feb-1974","smm - менеджер","+79027893459","Martirosov@gmail.com","NULL","NULL"),
("Мелкумян","Роберт","Робертович","16-May-1993","маркетолог","+79982341290","Melkumyan@gmail.com","NULL","NULL"),
("Олейник","Ольга","Викторовна","18-Jun-1993","руководитель проекта","+79762349987","Oleinik@gmail.com","NULL","NULL"),
("Полюцкий","Александр","Сергеевич","19-Jan-1981","юрист-консультант","+79673421894","Polyutsky@gmail.com","NULL","NULL"),
("Рустамов","Иброхим","Рустамович","29-Oct-1982","зав.хозяйством","+79231782392","Rustamov@gmail.com","NULL","NULL"),
("Рябцева","Алена","Александровна","14-Nov-1982","бухгалтер","+79321743981","Ryabtseva@gmail.com","NULL","NULL"),
("Саберова","Динара","Равилевна","28-Dec-1994","главный юрист","+79992341084","Saberova@gmail.com","NULL","NULL"),
("Сафонова","Ирина","Ивановна","15-Jul-1983","делопроизводитель","+79253419861","Safonov@gmail.com","NULL","NULL"),
("Стронина","София","Евгеньевна","31-Mar-2002","секретарь","+79162381629","Stronina@gmail.com","NULL","NULL"),
("Тарасов","Степан","Павлович","06-Jun-1996","менеджер","+79152371823","Тарасов@gmail.com","NULL","NULL"),
("Чекменёв","Кирилл","Андреевич","02-Aug-1998","дизайнер","+79172361959","Chekmenev@gmail.com","NULL","NULL"),
("Чернов","Максим","Дмитриевич","23-Dec-1999","аналитик","+79293652732","Chernov@gmail.com","NULL","NULL"),
("Шарофидинова","Ирода","Отабек","21-Mar-1991","уборщица","+79002893276","Sharofidinov@gmail.com","NULL","NULL"),
("Шундрик","Егор","Максимович","07-Apr-1992","расчетчик","+79281123119","Shundrick@gmail.com","NULL","NULL"),
("Шушняев","Никита","Максимовна","09-Sep-1991","сметчик","+79031732861","Shushnyaev@gmail.com","NULL","NULL")]

local = time.ctime(time.time())

with sq.connect("employees.db") as base:
    basedannyx = base.cursor()
    basedannyx.execute('DROP TABLE IF EXISTS employees')
    basedannyx.execute("""CREATE TABLE IF NOT EXISTS employees(
        firstname TEXT,
        name TEXT,
        lastname TEXT,
        birth TEXT,
        job TEXT,
        phone TEXT,
        email TEXT,
        enter TEXT ,
        exit TEXT 
        );
        """)
    basedannyx.executemany("INSERT INTO employees VALUES(?, ? , ?, ?, ? , ?, ? , ?,?)",current)
base.commit()

with sq.connect("guests.db") as b2:
    sql2 = b2.cursor()
    sql2.execute('DROP TABLE IF EXISTS guests')
    sql2.execute("""CREATE TABLE IF NOT EXISTS guests(
        firstname TEXT,
        name TEXT,
        email TEXT,
        enter INt,
        exit INT 
        );
        """)
b2.commit()

class win(QMainWindow):
    def __init__(self):
        super().__init__()
        global basedannyx
        global base
        global employees
        global guests
        self.basedannyx = 0
        self.car = 0

        self.setFixedSize(QSize(500,400))

        self.setWindowTitle('Терминал Охраны')

        self.but_car=QRadioButton(self)
        self.but_car.setText("Нужно ли парковочное место?")
        self.but_car.move(150,210)
        self.but_car.adjustSize()
        self.but_car.toggled.connect(self.parkovka)


        self.pochta = QLineEdit(self,placeholderText="Введите почту сотрудника")
        self.pochta.move(10,10)
        self.pochta.setFixedSize(230,23)
        
        self.name = QLineEdit(self,placeholderText="Введите имя")
        self.name.move(10,40)
        self.name.setFixedSize(230,23)

        self.but_sotryd_vxod=QPushButton(self)
        self.but_sotryd_vxod.setFixedSize(230,23)
        self.but_sotryd_vxod.move(10,130)
        self.but_sotryd_vxod.setText('Вход сотрудника')
        self.but_sotryd_vxod.clicked.connect(self.vxod_str)



        self.but_sotryd_vexed=QPushButton(self)
        self.but_sotryd_vexed.setFixedSize(230,23)
        self.but_sotryd_vexed.move(10,160)
        self.but_sotryd_vexed.setText('Выход сотрудника')
        self.but_sotryd_vexed.clicked.connect(self.exit_str)


        self.gost_fam=QLineEdit(self,placeholderText="Введите фамилию гостя")
        self.gost_fam.move(250,10)
        self.gost_fam.setFixedSize(230,23) 
        
        self.gost_name=QLineEdit(self,placeholderText="Введите имя гостя")
        self.gost_name.move(250,40)
        self.gost_name.setFixedSize(230,23)

        self.gost_passport=QLineEdit(self,placeholderText="Введите контактную почту гостя")
        self.gost_passport.move(250,70)
        self.gost_passport.setFixedSize(230,23)

        self.but_gost=QPushButton(self)
        self.but_gost.setFixedSize(230,23)
        self.but_gost.move(250,130)
        self.but_gost.setText('Вход гостя')
        self.but_gost.clicked.connect(self.vxod_gost)

        self.but_gost_exit=QPushButton(self)
        self.but_gost_exit.setFixedSize(230,23)
        self.but_gost_exit.move(250,160)
        self.but_gost_exit.setText('Выход гостя')
        self.but_gost_exit.clicked.connect(self.gost_exit)




        self.exit= QLineEdit(self,placeholderText="Введите контактную почту(только при выходе гостя)")
        self.exit.move(10,100)
        self.exit.setFixedSize(470,23)

    def vxod_str(self):
        global guests
        global employees
        self.adc=self.pochta.text().find("@")
        self.dfe = self.name.text()


        self.local_time = time.ctime(time.time())
        if self.car == 1 :

            if employees!=0:
                if employees<5 and guests>0:
                    employees=employees-1
                    guests=guests-1
                else:
                    employees=employees-1   
                basedannyx.execute(f"""UPDATE employees SET enter = ? where email = ? """,[self.local_time,self.dfe])
                basedannyx.execute('SELECT email FROM employees')
                self.rows = basedannyx.fetchall()
                if self.rows.count((self.pochta.text(),)) :
                    print("Сотрудник",self.dfe,"Вошёл")

                else:
                    print("Такой почты нет в базе данных")
                base.commit()
              
            else:
                print("Извините мест нет")
        elif self.car == 0 :
            basedannyx.execute(f"""UPDATE employees SET enter = ? where email = ? """,[self.local_time,self.dfe])
            base.commit()
            basedannyx.execute('SELECT email FROM employees')
            self.rows = basedannyx.fetchall()
            if self.rows.count((self.pochta.text(),)):

                print("Сотрудник",self.dfe,"Вошёл")

            else:
                print("Такой почты нет в базе данных")

    def exit_str(self):
        global guests
        global employees
        self.dfe = self.name.text()
        if self.car == 1:
            if employees<5 and guests<5 :
                employees=employees+1
                guests=guests+1
            employees=employees+1
        self.local_time = time.ctime(time.time())
        basedannyx.execute(f"""UPDATE employees SET exit = ? where email = ? AND enter != 'NULL' """,[self.local_time,self.dfe])
        basedannyx.execute('SELECT email FROM employees')
        self.rows = basedannyx.fetchall()
        if self.rows.count((self.pochta.text(),)) :
            print("Сотрудник",self.dfe,"Вышел")
        else:
            print("Такой почты нет в базе данных")
        base.commit()
    base.commit()



    def parkovka(self):
        if self.car == 0:
            self.car = 1
        else:
            self.car = 0
        print(self.car)



        self.car = 0
        global sql2
        global b2
        global employees
        global guests

    def parkovka(self):
        if self.car == 0:
            self.car = 1
        else:
            self.car = 0
        if guests ==0:
            print("Места Закончились")


        

    def gost_exit(self):
        global guests
        global employees
        if self.car == 1:
            employees = employees + 1
            guests = guests + 1
        self.ng=self.gost_name.text()
        self.exi = self.exit.text()
        self.time = time.time()
        self.local_time = time.ctime(time.time())
        sql2.execute(f"""UPDATE guests SET exit = ? where email = ? """,[self.time,self.exi])
        sql2.execute('SELECT email FROM guests')
        self.rows = sql2.fetchall()
        if self.rows.count((self.exit.text(),)) :
            print("Гость",self.ng,"Вышел")
            sql2.execute('SELECT enter , exit FROM guests WHERE email = ? ', (self.pochtat,))
            self.rows2 = sql2.fetchall()
            self.tkk = self.rows2[0]
            self.tk,self.tx = self.tkk
            if self.tx-self.tk>10:
                print(f"Гость {self.ng} - превысил время посещения на {(self.tx)-(self.tk)-10} сек, 'Просим обратиться к начальству'")
            if self.tx-self.tk<10:
                print(f"Гость {self.ng} пробыл внутри {(self.tx)-(self.tk)} ")
        else:
            print("Такой почты нет в базе данных")


    def vxod_gost(self):
        global guests
        self.ng=self.gost_name.text()
        global employees
        if self.car == 1:
            if guests ==0:
                print("Места закончились!")
            else:
                employees = employees - 1
                guests = guests - 1
                self.time = time.time()
                self.familt=self.gost_fam.text()
                self.namet=self.name.text()
                self.pochtat=self.gost_passport.text()

                self.ng=self.gost_name.text()


                self.CORT=[(self.familt,self.namet,self.pochtat,self.time,0)]
                    
                sql2.execute('SELECT email FROM guests')
                self.rows = sql2.fetchall()
                if self.rows.count((self.gost_passport.text(),)) :
                    print("Такая почта уже есть")
                else:
                    print("Гость",self.ng,"Вошёл")
                    sql2.executemany("INSERT INTO guests VALUES(?, ? , ?, ?)",self.CORT)
                    b2.commit()
        else:
            self.time = time.time()
            self.familt=self.gost_fam.text()
            self.namet=self.name.text()
            self.pochtat=self.gost_passport.text()
            self.CORT=[(self.familt,self.namet,self.pochtat,self.time,0)]
            sql2.execute('SELECT email FROM guests')
            self.rows = sql2.fetchall()
            if self.rows.count((self.gost_passport.text(),)) :
                print("Такая почта уже есть")
            else:
                print("Гость",self.ng,"Вошёл")
                sql2.executemany("INSERT INTO guests VALUES(?,?, ? , ?, ?)",self.CORT)
                b2.commit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window=win()
    window.show()
    sys.exit(app.exec())