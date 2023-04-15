import uuid
from datetime import date
from model.Factura.Factura import Factura


def crear_factura(cedulaDueño,compras, idMascota, idOrden, veterinaria):
    idFactura = uuid.uuid4
    print(f"Factura {idFactura}")
    print(f"Fecha: {date.today()}")
    print(f"Cédula del dueño: {cedulaDueño}")
    print(f"ID de la mascota: {str(uuid.uuid4())}")
    print("===============================================")
    print("Descripción                            | Precio ")
    print("-----------------------------------------------")
    total = 0
    medicamentosCompletos = ""
    print(compras)
    for medicamento, datos in compras.items():
                print(medicamento)
                precio = datos["precio"]
                totalProducto = precio * datos["cantidad"]
                total += precio * datos["cantidad"]
                cantidadMedicamento = datos["cantidad"]
                medicamentosCompletos = f"{medicamento:>15} x {cantidadMedicamento:>2} = ${precio:>5}  = ${totalProducto:>5} valor total de la compra = ${total} "+ medicamentosCompletos
    print(medicamentosCompletos)
    print("-----------------------------------------------")
    print(f"Total: ${total}")
    medicamentos = medicamentosCompletos
    facturaCreada = Factura(idMascota,idFactura, cedulaDueño, idOrden,medicamentos, total)    
    veterinaria.facturas.append(facturaCreada)    
    print("*************FACTURA CREADA*************")
    print(veterinaria.facturas)
