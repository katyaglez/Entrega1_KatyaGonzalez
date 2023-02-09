Hecho por: Katya González
https://drive.google.com/file/d/1GF7HFJyk6dAK8q8Np1wbUUk6RGCYwwEq/view
LINK DEL VIDEO EXPLICADO

                    Proyecto Aquatic Club

Se realiza un proyecto para un centro deportivo, con el fin de conocer los servicios que se dan y productos en venta.
En el siguiente proyecto se genera un modelo MVT con los siguientes aspectos:

    1.- Desarrollar una WEB Django con patrón MVT
    2.- Herencia de HTML
    3.- Realizar al menos 3 Models diferentes
    4.- Un formulario para insertar datos a todas las clases de los Models
    5.- Un formulario para buscar algo en la base de datos
Al momento de tener descargado el repositorio y poder acceder a él. Lo primero que nos encontramos es una página genérica con dos opciones:

1.- /admin/ : Directamente abre el administrador de Django que cuenta hasta este momento con dos usuarios, un superadmin que es capaz de crear, borrar y  modificar variables dentro del administrador y mediante formularios generados desde la base de datos. Y el segundo usuario es para cualquier persona que guste acceder para mirar el proyecto y únicamente tiene permisos para ver la apliación, no puede añadir nada.
  
  2./Aquatic/: Esta URL nos lleva directamente al Indice del Proyecto en cuestión y nos despliega un menú en el cual encontraremos diferentes URL a las cuales podremos viajar para crear alumnos, tipos de servicio y venta de más artículos. Se añadió una NavBar desde la cual podremos viajar de un listado a otro ya que se encuentran enlazados mediante un HTML Base que hereda la configuración de la NavBar.

  3. /Lista-clases/ encontraremos las clases de natacion que se manejan, asi como el intructor quien las imparte

  4./Lista-alumnos/ se encuentra una lista a la cual solo el superuser tiene acceso ya que es una información confidencial que solamente una persona puede tener

  5. /lista-ropa/ encontraremos mercancia que se podrá comprar, utilizable en las practicas deportivas de la misma escuela.

  6. /servicios-list/ se encontrara lista de otros servicios la cual solo los estudiantes activos podran tener acceso y un super user podra modificar. 

Como acceder al proyecto
Para acceder al repositorio es necesario descargarlo en el editor de código de preferencia con el siguiente comando: "Git Clone" y agregamos el enlace de GitHub: https://github.com/katyaglez/Entrega1_KatyaGonzalez.git El repositorio está público por lo cual está descargable para cualquier persona.

usuarios (estos pueden variar para ejemplificar actualizaciones)
Anaí
12345

DianaGlez
diana12345

Marco2
user123

Conclusión
El proyecto aun esta en construcción, se planea tener mas productos así como el listado de mas servicios, donde pueda mostrar imagenes referentes a cada uno de los servicios
asi como direccionar a un formulario en el cual pueda cada persona inscribirse y una confirmacion al respecto. 
El super user podra obtener unlistado de las personas que se inscriban para tener un control asi como las que solicitan información.

