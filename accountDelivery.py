class Delivery():

    id             = int
    nombre         = str
    telefono       = int
    licencia       = str
    placa          = str
    tipoVehiculo   = str

    def __init__(self, id, nombre, telefono, licencia, placa, tipoVehiculo):
        self.licencia       = licencia
        self.placa          = placa
        self.tipoVehiculo   = tipoVehiculo
        self.id             = id
        self.nombre         = nombre
        self.telefono       = telefono