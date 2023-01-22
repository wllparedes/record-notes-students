# Antes se debió de haber instalado prettytable y colorama
# pip install colorama - Colorama
# pip install prettytable - Prettytable

from colorama import Fore
from prettytable import PrettyTable

tabla = PrettyTable(['Nombre y Apellidos', 'C. Aprobados', 'C. Desaprobados', 'Condición'])
dictNam_apro_desa = {}
cursos = ['Matematica', 'Comunicación', 'Fisica', 'Ciencias Sociales', 'Ciencia']

# Función que permite en ingreso del alumno, como tambien de preguntar las notas en respectivos cursos
def ingreso():
  while(True):
    cursosAprobados = []
    cursosDesaprobados = []
    notasAlumnox = []
    nombre = input(f'{Fore.LIGHTWHITE_EX}Ingrese nombre/apellidos del alumno: (0 para salir): ')
    if (nombre == '0'):
      return f'\n{Fore.YELLOW}Salió del programa 1\n'
    c_cur_des = 0
    c_cur_apro = 0
    print(f'\n\t.: Ingrese las notas del alumno: {Fore.LIGHTCYAN_EX}{nombre}{Fore.LIGHTWHITE_EX} :.\n')
    for c in cursos:
      while (True):
        try:
          nota = float(input(f'{Fore.LIGHTWHITE_EX}- Ingrese la nota de {c}: '))
          if (nota >= 0 and nota <= 20):
            if (nota >= 13 and nota <= 20):
              c_cur_apro += 1
              cursosAprobados.append(c)
            elif (nota >= 0 and nota <= 12):
              c_cur_des += 1
              cursosDesaprobados.append(c)
            notasAlumnox.append(nota)
            print(f'{Fore.LIGHTBLUE_EX}✓')
            break
          else:
            print(f'{Fore.RED}(!) Nota fuera del rango de 0-20')
        except ValueError:
          print(f'{Fore.RED}(!) Ha digitado incorrectamente, vuelva a internarlo')

    # Añade los datos: nombre,ca, cd y condición a la tabla creada anteriormente
    match (c_cur_des):
      case 0: tabla.add_row([nombre, c_cur_apro, c_cur_des, '(✓) APROBADO'])
      case 1 | 2: tabla.add_row([nombre, c_cur_apro, c_cur_des, '(-) VACACIONAL'])
      case _: tabla.add_row([nombre, c_cur_apro, c_cur_des, '(x) REPITENCIA'])

    # Añade los datos muy generales a un diccionario donde la clave es el nombre del alumno
    dictNam_apro_desa[nombre] = cursosAprobados, cursosDesaprobados, notasAlumnox
    # Se retorna el mensaje de todo correcto
    print(f'{Fore.LIGHTGREEN_EX}(✓) Notas del alumno/a {Fore.LIGHTCYAN_EX}<{nombre}>{Fore.LIGHTGREEN_EX} agregados correctamente\n')

# Función para editar los nombres del alumnos
def editar_nombres(tabla):
  while (True):
    try:
      nuevo_nombre = input('Ingrese un Nombre y Apellido nuevo: ').strip()
      if (nuevo_nombre != ''):
        while (True):
          try:
              indice_edit = (int(input('Digite la fila del nombre a editar: ')) - 1)
              if(0 <= indice_edit <= tabla.rowcount):
                valores = tabla.rows[indice_edit]
                tabla.add_row([nuevo_nombre, valores[1], valores[2], valores[3]])
                tabla.del_row(indice_edit)
                return f'\nEdición satisfactoriamente!'
              else: 
                print('Digite una fila correcta a editar')
                continue
          except ValueError:
            print('(!) Error: Digitación incorrecta')
          # except IndexError:
          #   print('(!) Ingrese un número de fila existente')
      else: 
        print('(!) Digite un nombre correctamente')
        continue
    except:
      print('(!) Error: Digitación incorrecta')

# Función que realiza el promedio de los alumnos ingresado tomando en cuenta las notas ingresadas anteriormente
def promedio_alumn(dicc):
  if (len(dicc) == 0):
    return f'\n{Fore.RED}(!) Advertencia: Aún no se han ingresado alumnos a la tabla'
  else:
    print(f'\n\t\t{Fore.MAGENTA}.: Información General de Promedio de Alumnos :.\n')
    for v in dicc:
      sum_nots = 0
      listaAlumnNot = dicc[v][2]
      stringNot = []
      # stringNot = ', '.join([str(nu) for nu in listaAlumnNot])
      for n in listaAlumnNot:
        sum_nots += n
        stringNot.append(str(n))
      promedioFinal = round(sum_nots / len(listaAlumnNot), 2)
      print(f'''{Fore.LIGHTWHITE_EX}(°) Información del alumno: {Fore.LIGHTCYAN_EX}{v}{Fore.LIGHTWHITE_EX}
(°) Notas: {', '.join(stringNot)} | Promedio Final: {promedioFinal}\n''')
  return f'\n{Fore.GREEN}(✓) Impresa promedios de los alumnos\n'

# Función para imprimir la tabla en la terminal
def terPrintTable(table, dicc):
  if (len(dicc) == 0):
    return f'\n{Fore.RED}(!) Advertencia: Aún no se han ingresado alumnos a la tabla'
  else:
    return f'\n\t\t{Fore.MAGENTA}.: Tabla de Alumnos Ingresados :.{Fore.LIGHTWHITE_EX}\n\n{table}'

# Función que escribe la tabla hecha en un archivo .txt
def imprimir(table, dicc):
  if (len(dicc) == 0):
    return f'\n{Fore.RED}(!) Advertencia: Aún no se han ingresado alumnos a la tabla'
  else:
    archivo = open('tablaAlumnos.txt', 'a+', encoding='utf-8')
    archivo.write(str(f'\n{table}'))
    archivo.close()
    return f'\n{Fore.GREEN}(✓) Su tabla ha sido impresa en el archivo .txt con exito\n'

# Función que limpia el archivo .txt
def limpiar():
  archivo = open('tablaAlumnos.txt', 'r+', encoding='utf-8')
  archivo.truncate()
  archivo.close()
  return f'\n{Fore.GREEN}(✓) Su archivo .txt ha sido limpiado con exito\n'

# Main del programa
def main_n():
  while (True):
    try:
        print(f'''\n\t{Fore.LIGHTMAGENTA_EX}.: REGISTRO DE NOTAS :.
\n{Fore.LIGHTWHITE_EX}1. Ingresar notas de alumnos
2. Ver tabla de alumnos
3. Ver Diccionario de alumnos
4. Ver Promedio General de alumnos y su condición
5. Imprimir la tabla 
6. Limpiar archivo .txt
7. Editar Nombre de Alumno
0. Salir''')
        # Cuando queramos ver el .txt es mejor verlo desde archivos q desde el IDE
        opc = int(input('\n- Ingrese su opción: '))
        match (opc):
          case 0: 
            print(f'{Fore.YELLOW}\n(!!) Saliendo del programa, tenga un buen día :){Fore.YELLOW}{Fore.LIGHTWHITE_EX}')
            break
          case 1: print(ingreso())
          case 2: print(terPrintTable(tabla, dictNam_apro_desa))
          case 3: print(dictNam_apro_desa)
          case 4: print(promedio_alumn(dictNam_apro_desa))
          case 5: print(imprimir(tabla, dictNam_apro_desa))
          case 6: print(limpiar())
          case 7: print(editar_nombres(tabla))
          case _: print(f'{Fore.RED}\n(!) Opción no valida\n')
    except ValueError:
      print(f'\n{Fore.RED}(!) Opción incorrecta\n')

main_n()