from usuarios import crear_archivo, login_usuario, registrar_usuario

crear_archivo()
registrar_usuario("vladimir", "1234")
registrar_usuario("brisa", "1234")
login_usuario("vladimir", "1234")
login_usuario("brisa", "1234")
registrar_usuario("jordy", "1234")
login_usuario("jordy", "2222")