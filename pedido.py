from accountAdmin import Admin
from accountDelivery import Delivery
from accountUser import User
from pizzaEstandar import PizzaEstandar
from pizzaPrimium import PizzaPrimium
from pizzaSuprePrimium import PizzaSuperPrimium

class PedidoPizzaEstandar(Admin, Delivery, User, PizzaSuperPrimium, PizzaEstandar, PizzaPrimium):
    id                  = int
    vendedor            = Admin("","", "", "", "", "")
    cliente             = User("", "", "", "", "")
    delivery            = bool
    pizzaEstandar       = PizzaEstandar("", "", "", "", "", "")
    horaPedido          = int
    horaEntrega         = int
    
    def __init__(self, id, vendedor, cliente, delivery, pizzaEstandar, horaPedido, horaEntrega):
        self.id             = id
        self.vendedor       = vendedor
        self.cliente        = cliente
        self.delivery       = delivery
        self.pizzaEstandar  = pizzaEstandar
        self.horaEntrega    = horaEntrega
        self.horaPedido     = horaPedido

# PedidoPizzaPrimium
       
class PedidoPizzaPrimium(Admin, Delivery, User, PizzaSuperPrimium, PizzaEstandar, PizzaPrimium):
    id                  = int
    vendedor            = Admin("","", "", "", "", "")
    cliente             = User("", "", "", "", "")
    delivery            = bool
    pizzaPrimium        = PizzaPrimium("", "", "", "", "", "")
    horaPedido          = int
    horaEntrega         = int
    
    def __init__(self, id, vendedor, cliente, delivery, pizzaPrimium, horaPedido, horaEntrega):
        self.id             = id
        self.vendedor       = vendedor
        self.cliente        = cliente
        self.delivery       = delivery
        self.pizzaPrimium   = pizzaPrimium
        self.horaEntrega    = horaEntrega
        self.horaPedido     = horaPedido
