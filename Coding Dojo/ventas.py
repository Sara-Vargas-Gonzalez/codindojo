ventas = [
    {"fecha": "2024-05-07", "producto": "labial", "cantidad" : 3, "precio" : 5.990},
    {"fecha": "2024-05-07", "producto": "blush", "cantidad" : 5, "precio" : 8.990},
    {"fecha": "2024-05-08", "producto": "labial", "cantidad" : 2, "precio" : 5.990},
    {"fecha": "2024-05-08", "producto": "blush", "cantidad" : 3, "precio" : 8.990},
    {"fecha": "2024-05-09", "producto": "labial", "cantidad" : 6, "precio" : 5.990},
    {"fecha": "2024-05-09", "producto": "blush", "cantidad" : 4, "precio" : 8.990},
    {"fecha": "2024-05-10", "producto": "labial", "cantidad" : 3, "precio" : 5.990},
    {"fecha": "2024-05-10", "producto": "blush", "cantidad" : 7, "precio" : 8.990},
]
ingresos_totales = 0
for venta in ventas:
    ingresos_totales += venta["cantidad"] * venta["precio"]
    print(f"Ingresos Totales : ${ingresos_totales: .2f}")
    
ventas_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    if producto in ventas_por_producto:
        ventas_por_producto[producto] += venta["cantidad"]
    else:
        ventas_por_producto[producto] = venta["cantidad"]
producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)
cantidad_mas_vendida = ventas_por_producto[producto_mas_vendido]
print(f"El producto más vendido es el: {producto_mas_vendido} con {cantidad_mas_vendida} unidades")

precio_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    precio_total = venta["cantidad"] * venta["precio"]
    if producto in precio_por_producto:
        precio_por_producto[producto] = (precio_por_producto[producto][0] + precio_total, precio_por_producto[producto][1] + venta["cantidad"])
    else:
        precio_por_producto[producto] = (precio_total, venta["cantidad"])
precio_promedio_por_producto = {}
for producto, (suma_precio, cantidad) in precio_por_producto.items():
    precio_promedio_por_producto[producto] = suma_precio / cantidad
for producto, precio_promedio in precio_promedio_por_producto.items():
    print(f"El precio promedio de {producto}: ${precio_promedio: .2f}")
    
ingresos_por_dia ={}
for venta in ventas:
    fecha = venta["fecha"]
    ingreso_dia = venta["cantidad"] * venta["precio"]
    if fecha in ingresos_por_dia:
        ingresos_por_dia[fecha] += ingreso_dia
    else:
        ingresos_por_dia[fecha] = ingreso_dia
        
for fecha, ingresos in ingresos_por_dia.items():
    print(f"El ingreso del {fecha} es: ${ingresos: .2f}")
    
resumen_venta = {}

for producto in ventas_por_producto:
    cantidad_total = ventas_por_producto[producto]
    ingresos_totales_producto = cantidad_total * precio_por_producto[producto][0] / precio_por_producto[producto][1]
    precio_promedio = precio_promedio_por_producto[producto]
    
    resumen_venta[producto] = {
        "cantidad_total" : cantidad_total,
        "ingresos_totales" : cantidad_total * precio_promedio,
        "precio_promedio" : precio_promedio
    }
    for producto, info in resumen_venta.items():
        print(f"El resumen para {producto}:")
        print(f"  - cantidad total vendida: {info['cantidad_total']}")
        print(f"  - Ingresos totales: ${info['ingresos_totales']: .2f}")
        print(f"  - Precio promedio: ${info['precio_promedio']: .2f}")