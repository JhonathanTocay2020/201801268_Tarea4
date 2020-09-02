import json
import os

base = []

def cargar_archivo_json(ruta,lista):

    try:
        with open(ruta, 'r') as archivo:
            base_de_datos = json.load(archivo)
            print("------------------Archivo Cargado------------------")
            for am in base_de_datos:
                estudiante = {}
                estudiante['nombre'] = am['nombre']
                estudiante['edad'] = am['edad']
                estudiante['activo'] = am['activo']
                estudiante['saldo'] = am['saldo']
                lista.append(estudiante)
        print(lista)
    except:
        print("Archivo no encontrado")

def main():
    ruta = 'prueba.json'
    cargar_archivo_json(ruta, base)
    archivo_html()
    os.system('imprimir.html')

def archivo_html():
    nombre="imprimir"
    contador=1
    with open(nombre+'.html', 'w') as html:
        html.write('<html>')
        html.write('    <head>')
        html.write('        <title>Tarea 4</title>')
        html.write('        <style>')
        html.write('            #customers {')
        html.write('                  font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;')
        html.write('                  border-collapse: collapse;')
        html.write('                  width: 100%;')
        html.write('            }')
        html.write('            #customers td, #customers th {')
        html.write('                border: 1px solid #ddd;')
        html.write('                padding: 8px;')
        html.write('                }')
        html.write('            #customers tr:nth-child(even){background-color: #f2f2f2;}')
        html.write('            #customers tr:hover {background-color: #ddd;}')
        html.write('            #customers th {')
        html.write('                padding-top: 12px;')
        html.write('                padding-bottom: 12px;')
        html.write('                text-align: left;')
        html.write('                background-color: #4CAF50;')
        html.write('                color: white;')
        html.write('                }')
        html.write('        </style>')
        html.write('    </head>')
        html.write('    <body >')
        html.write('        <center>')
        html.write('            <h1 style= "color: #338AFF">Lista de Cuentas</h1>')
        html.write('                <table id="customers">')
        html.write('                    <tr>')
        html.write('                        <th>ID</th>')
        html.write('                        <th>Nombre</th>')
        html.write('                        <th>Edad</th>')
        html.write('                        <th>Activo</th>')
        html.write('                        <th>Saldo</th>')
        html.write('                    </tr>')
        for al in base:
            html.write('                    <tr>')
            html.write('                        <td>' + str(contador) + '</td>')
            html.write('                        <td>'+ al['nombre'] +'</td>')
            html.write('                        <td>'+ str(al['edad']) +'</td>')
            html.write('                        <td>'+ str(al['activo']) +'</td>')
            html.write('                        <td>'+ str(al['saldo'])+'</td>')
            html.write('                    </tr>')
            contador += 1
        html.write('            </table>')
        html.write('        </center>')
        html.write('    </body>')
        html.write('</html>')

if __name__ == '__main__':
    main()