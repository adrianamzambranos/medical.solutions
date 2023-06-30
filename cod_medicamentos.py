def consultar_medicamentos(enfermedad, archivo_excel):
    # Cargar el archivo Excel en un DataFrame
    df = pd.read_excel(archivo_excel)
    
    # Obtener la columna correspondiente a la enfermedad
    columna_enfermedad = df[enfermedad]
    
    # Filtrar los medicamentos para la enfermedad
    medicamentos = columna_enfermedad.dropna().tolist()
    
    # Retornar los primeros 5 medicamentos o los que haya disponibles
    return medicamentos[:5]

# Ejemplo de uso
enfermedad_paciente = "diabetes"
ruta_archivo_excel = "/base.xlsx"  # Reemplaza con la ruta correcta de tu archivo Excel

# Llamar a la función y mostrar el resultado
resultado = consultar_medicamentos(enfermedad_paciente, ruta_archivo_excel)
print("Los medicamentos para la enfermedad", enfermedad_paciente, "son:")
for medicamento in resultado:
    print("-", medicamento)
