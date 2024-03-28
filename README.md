# Challenge-Python-with-Sanic

# Documentación del Proyecto

## Instrucciones de Uso

Para levantar todo el proyecto, ejecuta el siguiente comando en la raíz del proyecto:
- docker-compose up

## Microservicios de cuentas

Este proyecto proporciona un servicio para la gestión de cuentas, con la capacidad de realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre cuentas de usuario.

Esto levantará los servicios necesarios para que la aplicación funcione correctamente.

## Endpoints

La URL base para acceder a los endpoints es:
- http://0.0.0.0:8000/accounts

### Métodos y Estructura del Body

- **GET**: Busca una cuenta proporcionando un email y dni en la URL.

- **POST**: Crea una nueva cuenta. Se debe enviar la siguiente estructura en el body de la solicitud:

- **PUT**: Modifica una cuenta existente proporcionando un email y dni en la URL para buscar en la base de datos. Se debe enviar la misma estructura que en la creación de cuenta en el body de la solicitud.

- **PUT**: Elimina una cuenta proporcionando un email y dni en la URL para buscar en la base de datos.

```json
{ 
    "name": string,
    "email": string,
    "dni": string,
    "money": int
}
```

## Microservicios de transacciones

El microservicio de transacciones se centra en facilitar la creación de transacciones entre cuentas registradas en el microservicio de cuentas.

## Endpoints
La URL base para acceder a los endpoints es:
- http://0.0.0.0:8005/transfer

### Métodos y Estructura del Body

- **POST**: Crea una nueva transaccion. Se debe enviar la siguiente estructura en el body de la solicitud:
```json
{ 
    "name": string,
    "email": string,
    "dni": string,
    "money": int
}
```

