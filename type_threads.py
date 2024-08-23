
class Session: 
    b_entrar = '/html/body/div[2]/div/div/header/div[3]/a'
    i_user = '/html/body/div[2]/div/div/div[2]/div/div/div/div[2]/div[1]/div[3]/form/div/div[1]/input'
    i_password = '/html/body/div[2]/div/div/div[2]/div/div/div/div[2]/div[1]/div[3]/form/div/div[2]/input'
    b_start_sesion = '/html/body/div[2]/div/div/div[2]/div/div/div/div[2]/div[1]/div[3]/form/div/div[3]/div[2]/div/div'

    def __str__(self) -> str:
        return "Inicio de sesion"

class Buscar:
    b_buscar = '/html/body/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/a'
    i_buscar = '/html/body/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div[1]/div[1]/div/div[1]/div/div/label/input'

    def __str__(self) -> str:
        return "Boton de busqueda"

class Rowspost:
    l_post = '/html/body/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div[1]/div[1]/div/div[2]/div/div/div[1]'
    b_post_i = '/html/body/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div[1]/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div[3]'

    def __str__(self) -> str:
        return "fila de resultados despues de la busqueda"

class Post:
    b_ver_actividad = '/html/body/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div[1]/div[1]/div/div[1]/div/div/div/div/div/div[4]/div/div'
    l_likes = '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/div[5]'

    def __str__(self) -> str:
        return "publicacion individual"

class Threads:
    sesion = Session()
    buscar = Buscar()
    fila_publicaciones = Rowspost()
    publicaciones = Post()
    

if '__main__' == __name__:
    a = Threads()
    print(a.sesion.b_entrar, a.fila_publicaciones.__str__())