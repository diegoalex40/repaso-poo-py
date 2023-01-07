from account import Account
from accountAdmin import Admin
from accountDelivery import Delivery
from accountUser import User
from pedido import PedidoPizzaEstandar
from pizzaEstandar import PizzaEstandar
from pago import Pago

if __name__ == "__main__":

    diego = Admin(1, "Diego Yanez", "dyanez@yavirac.edu.ec", [5555333, 55556668], 960901967, True)
    print(vars(diego))

    vicente = User(2, "Vicente Flores", "dyanez@yavirac.edu.ec", [555, 666], 5555556)
    alexander = User(2, "Alexander Flores", "dyanez@yavirac.edu.ec", [555, 666], 5555556)
    print(vars(alexander))

    jose    = Delivery(3, "Jose Jose", 999955559, "Licencia111", "PCCC-55550", "Motocicleta Suziki")
    print(vars(jose))

    pizzaEstandar1 = PizzaEstandar(1, "Pizza Estandar", "Pizza dos ingredientes", 9, True, ["Peperoni", "Salchicha Italina"])

    pedido1 = PedidoPizzaEstandar(1, Admin(1, "Diego Yanez", "dyanez@yavirac.edu.ec", [5555333, 55556668], 960901967, True), User(2, "Alexander Flores", "dyanez@yavirac.edu.ec", [555, 666], 5555556), False, PizzaEstandar(1, "Pizza Estandar", "Pizza dos ingredientes", 9, True, ["Peperoni", "Salchicha Italina"]),1700, 1720 )
    print(vars(pedido1))
    print(pedido1.cliente)

    pedido2 = PedidoPizzaEstandar(2, diego, vicente, True, pizzaEstandar1, 1500, 1525)
    print(vars(pedido2))
    print(pedido2.cliente)

    pago1 = Pago(1, "efectivo", 1212022, PedidoPizzaEstandar(1, Admin(1, "Diego Yanez", "dyanez@yavirac.edu.ec", [5555333, 55556668], 960901967, True), User(2, "Alexander Flores", "dyanez@yavirac.edu.ec", [555, 666], 5555556), False, PizzaEstandar(1, "Pizza Estandar", "Pizza dos ingredientes", 9, True, ["Peperoni", "Salchicha Italina"]),1700, 1720 ))
    print(vars(pago1))
    print(vars(pago1.pedido))
    print(vars(pago1.pedido.cliente))

    pago2 = Pago(2, "efectivo", 12012023, pedido2)
    print(vars(pago2))
    print(pago2)
