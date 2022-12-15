# Antes se debió de haber instalado prettytable
from prettytable import PrettyTable

tabla = PrettyTable(['Nombre y Apellidos', 'C. Aprobados', 'C. Desaprobados', 'Condición'])
dictNam_apro_desa = {}
cursos = ['Matematica', 'Comunicación', 'Fisica', 'Ciencias Sociales', 'Ciencia']

# Función que permite en ingreso del alumno, como tambien de preguntar las notas en respectivos cursos


def ingreso():
    while(True):
        cursosAprobados = []
        cursosDesaprobasos = []
        notasAlumnox = []
        nombre = input('Ingrese nombre/apellidos del alumno: (0 para salir): ')
        if (nombre == '0'):
            break
        c_cur_des = 0
        c_cur_apro = 0
        print(f'\n\t.: Ingrese las notas del alumno: {nombre} :.\n')
        for c in cursos:
            while (True):
                try:
                    nota = float(input(f'- Ingrese la nota de {c}: '))
                    if (nota >= 0 and nota <= 20):
                        if (nota >= 13 and nota <= 20):
                            c_cur_apro += 1
                            cursosAprobados.append(c)
                        elif (nota >= 0 and nota <= 12):
                            c_cur_des += 1
                            cursosDesaprobasos.append(c)
                        notasAlumnox.append(nota)
                        print('✓')
                        break;
                    else:
                        print('(!) Nota fuera del rango de 0-20')
                except ValueError:
                    print('(!) Ha digitado incorrectamente, vuelva a internarlo')

        print('(✓) Notas almacenadas correctamente\n')

        # Añade los datos: nombre,ca, cd y condición a la tabla creada anteriormente
        match (c_cur_des):
            case 0: tabla.add_row([nombre, c_cur_apro, c_cur_des, '(✓) APROBADO'])
            case 1 | 2: tabla.add_row([nombre, c_cur_apro, c_cur_des, '(-) VACACIONAL'])
            case _: tabla.add_row([nombre, c_cur_apro, c_cur_des, '(x) REPITENCIA'])

        # Añade los datos muy generales a un diccionario donde la clave es el nombre del alumno
        dictNam_apro_desa[nombre] = cursosAprobados, cursosDesaprobasos, notasAlumnox


# Función que realiza el promedio de los alumnos ingresado tomando en cuenta las notas ingresadas anteriormente
def promedio_alumn(dicc):
    print('\n')
    for v in dicc:
        sum_nots = 0
        listaAlumnNot = dicc[v][2]
        for n in listaAlumnNot:
            sum_nots += n
        promedioFinal = round(sum_nots / len(listaAlumnNot),2)
        print(f'''(°) Información del alumno: {v}
(°) Notas: {listaAlumnNot} | Promedio Final: {promedioFinal}''')
        print('\n')


# Función que escribe la tabla hecha en un archivo .txt
def imprimir(table):
    archivo = open('tablaAlumnos.txt', 'a')
    archivo.write(str(f'\n{table}'))
    archivo.close()
    return '\n(✓) Su tabla ha sido impresa en el archivo .txt con exito\n'


# Main del programa
def main_n():
    while (True):
        try:
            print('''\t.: REGISTRO DE NOTAS :.
\n1. Ingresar notas de alumnos
2. Ver tabla de alumnos
3. Ver Diccionario de alumnos
4. Ver Promedio General de alumnos y su condición
5. Imprimir la tabla 
0. Salir''')
# Cuando queramos ver el .txt es mejor verlo desde archivos q desde el IDE
            opc = int(input('\n- Ingrese su opción: '))
            match (opc):
                case 0:
                    print('\n(!!) Saliendo del programa, tenga un buen día :)')
                    break
                case 1: ingreso()
                case 2: print(tabla)
                case 3: print(dictNam_apro_desa)
                case 4: promedio_alumn(dictNam_apro_desa)
                case 5: print(imprimir(tabla))
                case _: print('\n(!) Opción no valida\n')
        except ValueError:
            print('\n(!) Opción incorrecta\n')


main_n()

