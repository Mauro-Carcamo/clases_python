#errores
try:
    #raise, se van a propagar unicamente en el exception generico. Va a buscar solamente en el except de expeption.
    raise Exception("rut","11.111.111-2","Invalidate rut format")
except Exception as error:# el error queda guardado en "error"
    print(type(error))
    print(error.args)
    print(error)

#haciendo un destructuring de los args (tuplas)
key, value, message = error.args

print(f'key -> {key}')
print(f'value -> {value}')
print(f'message -> {message}')