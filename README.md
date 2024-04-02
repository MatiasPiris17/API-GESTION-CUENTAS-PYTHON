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

### Métodos 

- **GET**: Busca una cuenta proporcionando un **email** en el cuerpo de la solicitud.

- **POST**: Crear una nueva cuenta proporcionando un **email**, **dni** y **name** en el cuerpo de la solicitud.

- **PUT**: Modifica una cuenta existente proporcionando un email en el cuerpo de la solicitud. Se debe enviar los datos que se van actualizar **dni**, **name** o **money**

- **PUT**: Elimina una cuenta proporcionando un **email**.

#### Cuerpo de la solicitud
```json
{ 
    "name": "string",
    "email": "string",
    "dni": "string",
    "money": "int"
}
```

## Microservicios de transacciones

El microservicio de transacciones se centra en facilitar la creación de transacciones entre cuentas registradas en el microservicio de cuentas. El método de transacción es a través del correo electrónico.

## Endpoints
La URL base para acceder a los endpoints es:
- http://0.0.0.0:8005/transfer

### Métodos 

- **POST**: Crear una nueva transaccion proporcionando un **sender**, **addressee** y **transfer_cant** en el cuerpo de la solicitud.

#### Estructura del Body
```json
{ 
    "sender": "string", // email 
    "addressee": "string", // email
    "transfer_cant": "int",
}
```

