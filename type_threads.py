
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
    b_start = '/html/body/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div/div/div[2]/div[1]/div[1]/div/div[2]/div/div/div/ul/li[1]/a/div[1]/div/div/div[2]/div/span/svg'

    def __str__(self) -> str:
        return "Boton de busqueda"

class Rowspost:
    l_post = '//div[1][contains(@class, "xb57i2i x1q594ok x5lxg6s x78zum5 xdt5ytf x1ja2u2z x1pq812k x1rohswg xfk6m8 x1yqm8si xjx87ck xx8ngbg xwo3gff x1n2onr6 x1oyok0e x1e4zzel x1plvlek xryxfnj")]/div/div/div/div/div/div/div[3]'
    l_post2 = '//div[1][contains(@class, "xb57i2i x1q594ok x5lxg6s x78zum5 xdt5ytf x1ja2u2z x1pq812k x1rohswg xfk6m8 x1yqm8si xjx87ck xx8ngbg xwo3gff x1n2onr6 x1oyok0e x1e4zzel x1plvlek xryxfnj")]/div/div/div/div/div/div'
    l_post3 = "//div[contains(@class, 'x1a6qonq')]/span"
    # por eliminar
    #b_post_i = '/html/body/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div[1]/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div[3]'
    #rows_post = '/html/body/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div[1]/div[1]/div/div[2]/div/div/div[1]/div'
    #b_post_start = '/div/div/div/div/div[3]'

    def __str__(self) -> str:
        return "fila de resultados despues de la busqueda"

class Post:
    b_ver_actividad = '''//*[contains(@class, "x1lliihq x1plvlek xryxfnj x1n2onr6 x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye xjohtrz xo1l8bm x12rw4y6 x1yc453h x1tu3fi x3x7a5m")]/span/span'''

    b_time_reset = """//*[contains(@class, "x1lliihq x1plvlek xryxfnj x1n2onr6 x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye xjohtrz xo1l8bm x12rw4y6 x1yc453h x1tu3fi x3x7a5m")]/span/a"""

    l_likes = '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/div'
    _l_likes = '''//*[contains(@class, "x1i10hfl xjbqb8w x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xexx8yu x18d9i69 x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 x1a2cdl4 xnhgr82 x1qt0ttw xgk8upj x9f619 x3nfvp2 x1s688f x90ne7k xl56j7k x193iq5w x1swvt13 x1pi30zi x12w9bfk x1g2r6go x11xpdln xz4gly6 x87ps6o xuxw1ft x19kf12q x6bh95i x1re03b8 x1hvtcl2 x3ug3ww x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x178xt8z xm81vs4 xso031l xy80clv xp07o12 xwsj4vy")]/div'''
    _l_likes_data = '//*[contains(@class, "x6s0dn4 x78zum5 xz9dl7a xsag5q8")]'
    _l_likes_data_follow = '/div[2]'
    number_selector = 6
    max_likes_2h = 12

               
    def __str__(self) -> str:
        return "publicacion individual"
    
class BarNav:
    perfil = '/html/body/div[2]/div/div/div[2]/div[1]/div[2]/div[4]/a/div/div[2]'

class unfollow:
    perfil_follow = '/html/body/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div[1]/div[1]/div[3]/div[1]/div/div/span'
    b_follow = '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div/div[2]/div/span[1]'
    l_follows = '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/div'

class Threads:
    sesion = Session()
    buscar = Buscar()
    fila_publicaciones = Rowspost()
    publicacion = Post()
    navegacion_boton_perfil = BarNav()
    perfil_unfollow = unfollow()
    

if '__main__' == __name__:
    a = Threads()
    print(a.sesion.b_entrar, a.fila_publicaciones.__str__())