# Color del pensamiento: azul #8cf
# Color del sistema: verde #090

init python:
    def beepy_voice_deep(event, interact=True, **kwargs): # Para que suenen los pitidos mientras habla un personaje
    # TODO: Descubrir cómo pasar un argumento para que cada personaje tenga su propio sonido
        if not interact:
            return

        if event == "show_done":
            beep = []
            for x in range(1,10):
                beep.append(random.choice(["audio/talk2.ogg", "audio/talk3.ogg"]))  # Construimos una lista de sonidos agudos y graves aleatorios
            renpy.sound.play(beep, loop = True)
        elif event == "slow_done":
            renpy.sound.stop(fadeout = 0.5)
    
    def beepy_voice_high(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            beep = []
            for x in range(1,10):
                beep.append(random.choice(["audio/talk1.ogg", "audio/talk2.ogg"]))
            renpy.sound.play(beep, loop = True)
        elif event == "slow_done":
            renpy.sound.stop(fadeout = 0.5)

    def alter_say_strings( str_to_test ): # Pausas automáticas en el texto con cada signo de puntuación
        str_map = {
            ". " : ". {w=0.25}", 
            "? " : "? {w=0.25}", 
            ".\n" : ".\n{w=0.25}", 
            "(...)\n" : "(...)\n{w=0.3}",
            "! " : "! {w=0.25}", 
            ", " : ", {w=0.05}",
        }
        for key in str_map:
            str_to_test = str_to_test.replace( key, str_map[ key ] ) 
        return str_to_test

define config.say_menu_text_filter = alter_say_strings

#region Definición de personajes
define ryu = Character('Rubio', color = '#aa3333', callback = beepy_voice_deep)
define gaelg = Character('Chamán', color = '#ae5323', callback = beepy_voice_deep)
define sevony = Character('Gafas', color = '#946894', callback = beepy_voice_high)
define jaeke = Character('Antipático', color = '#696969', callback = beepy_voice_deep)
define takahiro = Character('Llamativo', color = '#9a7818', callback = beepy_voice_deep)
define akane = Character('Yo', color = '#13a28f', callback = beepy_voice_high)
define umi = Character('Marinera', color = '#185a9a', callback = beepy_voice_high)
define emiko = Character('Coletas', color = '#d86d9e', callback = beepy_voice_high)
define luc = Character('Pañuelo', color = '#5a49b4', callback = beepy_voice_deep)
define axiom = Character('Mascarilla', color = '#a2135c', callback = beepy_voice_deep)
define danny = Character('Dormilón', color = '#66b103', callback = beepy_voice_deep)
define guppy = Character('Niña pez', color = '#ff8b3d', callback = beepy_voice_high)
define ichika = Character('Elegante', color = '#2ece49', callback = beepy_voice_high)
define ghiang = Character('Moños', color = '#1398a2', callback = beepy_voice_high)
#endregion
# TODO: Incluir a Ichika, Gael M., Ghiang y Kiiro en el guion

#region Definición de música
define audio.beautiful_lament = "<loop 15.6859>audio/BSO/Beautiful Lament.ogg"
define audio.kitsune_to_tanuki = "<loop 51.128>audio/BSO/Kitsune to Tanuki no Omanuke na Bakashi Ai.ogg"
#endregion

# Inicio del juego
label start:

    play sound tv_on
    pause 2.0
    play music breaking

    "{color=#090}¡Alerta! ¡Alerta!\n¡Caos en la ciudad!{/color}"

    scene cg c0_breaking with fade

    "{color=#090}En las últimas 24 horas se ha desatado una gran cantidad de incidentes en el este, oeste y centro de la ciudad de Gekkou.{/color}"
    "{color=#090}La intensidad de estos ataques va aumentando con el paso de las horas, se recomienda...{/color}"

    stop music fadeout 0.3
    play sound tv_static fadein 0.5
    show cg c0_static

    "{color=#090}(...){/color}"

    scene black with fade
    stop sound fadeout 1.5

    $ renpy.movie_cutscene("movie/pr_title.webm")

# Despertar en el camión
label truck:

    play music "audio/truck_engine.ogg" fadein 1.0
    show bg truck with fade

    "{color=#8cf}Cuando me desperté, todo estaba oscuro.{/color}"
    "{color=#8cf}Me encontraba en lo que parecía ser un camión de transporte.{/color}"
    "{color=#8cf}Podía escuchar el motor del vehículo y, a mi alrededor, pude distinguir a más gente despertar como yo.{/color}"

    show ryu concern at t11
    "{color=#8cf}Un chico de pelo claro permanecía sentado, abrazado a sus piernas, en silencio al fondo del camión.{/color}"
    "{color=#8cf}Lo oí soltar un suspiro de angustia justo antes de hundir la cabeza entre las piernas."
    hide ryu with dissolve

    show sevony concern at t11
    "{color=#8cf}También había una chica con gafas que inhaló y espiró en un claro intento de tranquilizarse."
    "{color=#8cf}Echó una mirada a su alrededor, justo antes de..."

    show sevony surprise at h11
    play sound "audio/truck_bump.ogg"
    with vpunch
    "{color=#090}¡Pam!"

    "{color=#8cf}Un bache en el camino despertó a casi todos los que seguían dormidos..."
    "{color=#8cf}Ahora que hay más gente despierta, tal vez debería fijarme en quiénes son mis compañeros de viaje..."

    hide sevony with dissolve
    "{color=#090}Haz clic en el icono del personaje en quien te quieras fijar."

    $ inv_name = "inv_c0_truck"
    $ talk = {"ryu": "Chico rubio", "jaeke": "Chico antipático"}    # Elementos a investigar
    call screen investigation(inv_name, talk)
    $ talk = {"ryu": "Chico rubio", "jaeke": "Chico antipático"}    # Lo definimos dos veces para que el usuario pueda volver atrás y sus opciones sean restauradas

# Investigación: Camión
label inv_c0_truck_ryu:     # Chico rubio
    $ ryu.name = "Rubio"
    $ gaelg.name = "Chamán"
    $ sevony.name = "Gafas"

    show ryu stand at t21
    show sevony surprise at t22
    "{color=#8cf}Las gafas de la chica de pelo violeta habían salido despedidas por culpa del bache."
    show ryu stand at s21
    "{color=#8cf}El rubio se agachó al oírlas caer. Habían aterrizado cerca de él."
    show ryu stand at t32
    "{color=#8cf}Gateó un poco hasta alcanzarlas y se las acercó a su dueña, con una cálida sonrisa."

    show ryu smile at f32
    ryu "Toma, ve con cuidado... Sería una pena que se te rompieran."

    "{color=#8cf}Lo dijo flojito, como si no quisiera llamar demasiado la atención en un ambiente tan tenso."

    show ryu smile at t21
    show sevony smile at f22
    sevony "(...)\nMuchas gracias."
    show sevony concern
    sevony "Vaya carretera en la que nos han metido."

    show sevony concern at t22
    show ryu stand at f21
    ryu "Pues... sí, la verdad."

    hide sevony
    hide ryu
    with dissolve

    show gaelg stand at t11
    "{color=#8cf}Un chico que parecía nervioso y confundido observaba la conversación."
    "{color=#8cf}Los miraba mientras murmuraba para sí mismo."

    show gaelg stand at s11
    gaelg "Mi chamanismo me sacará de esta.\nEscaparé de aquí."

    "{color=#8cf}Finalmente, consiguió reunir valor para hablarle a los presentes en lugar de al cuello de la camisa."

    show gaelg stand at hf11
    gaelg "Hum... ¿C-cómo te llamas?"

    show gaelg stand at t31
    pause 0.2
    show ryu surprise at t32
    show sevony stand at t33
    pause 0.5
    show ryu surprise at hf32
    ryu "¿Y-yo? V-vaya por Dios."
    show ryu smile
    $ ryu.name = "Ryu Itsuki"
    ryu "Mi nombre... es Ryu Itsuki.\nSoy un simple desempleado."
    ryu "¿Y vosotros, chica de las gafas, chico moreno?"
    show ryu smile at t32

    $ sevony.name = "Sevony"
    show sevony smile at f33
    sevony "Un gusto, Itsuki-kun. Mi nombre es Sevony."
    show sevony smile at t33

    $ gaelg.name = "Gabriel"
    show gaelg stand at f31
    gaelg "A-ah... yo soy... Gabriel..."

    "{color=#8cf}Gabriel se quedó bloqueado por un momento."

    show gaelg surprise at hf31
    $ gaelg.name = "Gael García"
    gaelg "¡QUIERO DECIR! Gael. Gael García, a tu servicio."
    show gaelg surprise at t31

    "{color=#8cf}¿En serio se le ha olvidado su propio nombre?"

    show ryu stand at f32
    ryu "Sevony y Gael... Tenéis nombres exóticos, son bonitos."

    "{color=#8cf}La expresión de Ryu se había apagado."

    ryu "Sevony... Me recuerdas a alguien, ¿sabes? Aunque tal vez solo sea mi imaginación."
    show ryu stand at t32

    show sevony smile at hf33
    sevony "Más que seguro, su imaginación. Mucha gente pasa por la ciudad."

    "{color=#8cf}Sevony ha contestado muy rápido..."
    show sevony smile at t33
    show ryu think at f32
    ryu "Hum... Seguramente sea eso."
    ryu "He conocido a mucha gente a lo largo de mi vida, no sería la primera vez que me ocurre."

    show ryu think at t32
    show gaelg happy at f31
    gaelg "Ryu... ¿Igual que «dragón» en japonés?"

    show gaelg happy at t31
    show ryu happy at hf32
    ryu "{bt=a1-p10-s1}Efectivamente.{/bt} No sé muy bien por qué escogieron ese nombre para mí..."
    show ryu concern at s32
    ryu "Un dragón da mucho miedo y escupe... fuego..."

    show gaelg stand at hf31
    gaelg "¡Yo creo que mola!\nY usted, señorita Sevony, ¿de dónde es?"

    show gaelg stand at t31
    show sevony smile at f33
    sevony "Soy de Gekkou, una ciudad un poco al norte de aquí."

    "{color=#8cf}Su sonrisa amable contrastaba con el tono frío, seguramente involuntario, de su voz."

    show sevony smile at t33
    show gaelg happy at f31
    gaelg "O sea que sois japoneses... ¡Entonces... podré aprender mucho de otras culturas!"
    gaelg "Hoy es una victoria para el {b}chamán definitivo{/b}."

    show ryu surprise at t32
    "{color=#8cf}Al oír el talento definitivo de Gael, Ryu lo miró con mucho interés."

    show gaelg happy at t31
    show ryu surprise at f32
    ryu "Chamán... Qué interesante."

    show ryu surprise at t32
    "{color=#8cf}¿Será este el inicio de una agradable amistad?"

    play sound "audio/truck_bump.ogg"
    with vpunch
    "{color=#090}¡Pam!"

    "{color=#8cf}¡¿Otro bache?!"

    hide ryu
    hide gaelg
    hide sevony
    with dissolve

    python:
        if "ryu" in talk:
            del talk["ryu"]

    if not talk:
        jump truck_end
    else:
        call screen investigation(inv_name, talk)

label inv_c0_truck_jaeke:   # Chico antipático

    show jaeke stand at t21
    show takahiro stand at t22
    with dissolve

    "{color=#8cf}En una esquina del vehículo se encontraba un chico con cara de pocos amigos."
    "{color=#8cf}Otro muchacho con ropa llamativa se le acercó."

    show takahiro ask at f22
    takahiro "Eh, ¿y tú eres...?"
    show takahiro ask at t22

    show jaeke annoyed
    "{color=#8cf}El moreno le devolvió una fría mirada y no medió palabra."

    show takahiro ask at f22
    takahiro "Ya veo que eres alguien con quien es fácil hablar..."
    show takahiro ask at t22

    show jaeke annoyed at t32
    "{color=#8cf}Nada más oír eso, el mudo se levantó, se le acercó y empezó a susurrar."

    show jaeke annoyed at f32
    jaeke "Ten cuidado conmigo, chaval.\nNo sabes con quién estás hablando."
    show jaeke annoyed at t32

    show takahiro laugh at f22
    takahiro "Pues claro que no sé con quién estoy hablando, ni siquiera me has dicho tu nombre."
    show takahiro laugh at t22

    show jaeke annoyed at t21
    pause 0.5
    show jaeke annoyed at f21
    jaeke "Los comediantes como tú solo les hacen gracia a los pringados de la cárcel."
    jaeke "Mejor haz algo productivo, porque no tienes ninguna gracia, fracasado."
    show jaeke annoyed at t21

    "{color=#8cf}Vaya humos se gasta..."

    play sound truck_bump
    with vpunch
    "{color=#090}¡Pam!"

    hide jaeke
    hide takahiro
    with dissolve

    python:
        if "jaeke" in talk:
            del talk["jaeke"]

    if not talk:
        jump truck_end
    else:
        call screen investigation(inv_name, talk)

# Posinvestigación: El camión acelera
label truck_end:
    
    "{color=#8cf}Creo que ya he escuchado suficiente...\nNo parece que nadie sepa cómo hemos llegado hasta aquí."
    "{color=#8cf}¿Cómo ha podido pasar esto?\n¿Habré hecho algo para acabar aquí...?"
    "{color=#8cf}Me decidí a intentar obtener información yo misma."

    akane "Esto... ¿Alguien sabe dónde estamos?"

    show umi stand at t11
    "{color=#8cf}Una chica muy guapa vestida con un gorro de marinero me dirigió la mirada al oírme."

    show umi stand at f11
    umi "No lo sé, pero es un vehículo en movimiento, así que tampoco tiene sentido preguntarse eso hasta que lleguemos."
    umi "Lo mejor será mantener la calma."

    show umi stand at t11
    akane "Supongo que tienes razón, pero quería preguntar por si alguien lo sabía..."

    show umi stand at t21
    show emiko ask at f22
    emiko "¿Eh? Espera... ¿entonces de verdad nadie sabe hacia dónde vamos o siquiera dónde estamos?"

    show umi stand at t31
    show emiko ask at t32
    show raiden annoyed at f33
    luc "Si lo supiéramos, ya habría contestado alguien, ¿no?\nA menos que se lo quiera callar."
    show raiden laugh at hf33
    luc "Imaginaos que nos han secuestrado o algo y pretenden deshacerse de nosotros, ¡ja, ja!"

    show raiden laugh at t33
    akane "¡¿Secuestrarnos?! ¡¿Y qué se supone que hemos hecho para acabar en una situación así?!"

    show raiden smile at f33
    luc "Vamos, solo era una broma."
    luc "Yo, al menos, no he hecho nada malo. Los demás, no sé."

    show umi surprise at h31
    show emiko surprise at h32
    show raiden surprise at h33
    play sound truck_bump
    with vpunch
    "{color=#090}¡Pam!"

    hide raiden
    hide emiko
    hide umi
    with dissolve
    play sound truck_bump volume 0.6 fadeout 0.3
    with vpunch
    play sound truck_bump2 volume 1.0 fadein 0.1 fadeout 0.3
    with vpunch
    play sound truck_bump volume 1.0 fadein 0.1 fadeout 0.3
    with vpunch
    "{color=#090}{sc}{color=#090}¡Pum, pam, pom, pum!{/sc}"
    
    "{color=#8cf}Por culpa de todos esos baches, me golpeé la cabeza con el techo del vehículo."

    show umi concern at focus
    umi "¿Te encuentras bien?"

    show umi concern at t11
    akane "S-sí..." 
    "{color=#8cf}Tal vez yo también debería entablar conversación con alguien..."
    akane "P-por cierto, ¿cómo te lla...?"

    hide umi with dissolve
    "{color=#8cf}Pero no pude acabar de formular mi pregunta."
    show bg truck_move
    play music truck_speed fadein 1.0 fadeout 0.5
    "{color=#8cf}El vehículo comenzó a serpentear repentinamente, arrojándonos a mí y a los demás pasajeros de un lado a otro." with vpunch
    "{color=#8cf}Cada vez más rápido, vi que algunos se sostenían a sus asientos como podían, yo me vi forzada a hacer lo mismo..."
    stop music fadeout 1.0
    show bg truck
    "{color=#8cf}Hasta que, al fin, paró."
    "{color=#8cf}Joder... Qué daño..."
    "{color=#8cf}Yo había acabado en el suelo, pero no era la única..."

    show axiom hurt at s11
    axiom "(...)"

    akane "¡Aah! ¿Estás bien?"
    "{color=#8cf}Fui a buscar mi pañuelo, pero la marinera fue más rápida que yo."
    
    show axiom hurt at t21
    show umi concern at t22
    pause 0.3
    show umi concern at f22
    umi "¿Necesitas ayuda?\nToma, ponte esto para taponar la herida..." 

    hide umi 
    hide axiom
    with dissolve

    show guppy sleep at s22
    show danny sleep at s21
    with dissolve
    "{color=#8cf}Y también había dos personas durmiendo en el suelo..."
    "{color=#8cf}Tener buen dormir es una cosa, pero no despertarte con todos esos baches es otra..."

    play sound truck_door
    pause 2.0
    scene bg truck_light with dissolve
    "{color=#8cf}Y entonces, la puerta se abrió."

    show raiden hurt at hf11 with vpunch
    luc "¡AAH, LA LUZ! ¡Mis ojos!"

    show raiden hurt at t11
    akane "¿Estás bie...?{nw}"
    play sound sfx_stab2    #FIXME: Hay que retocar este sonido o encontrarle un sustituto
    with flash
    with vpunch
    akane "¡AGH, MIS OJOS!"
    "{color=#8cf}La luz entró de golpe en el interior de la parte trasera del camión, acompañado de una corriente de aire refrescante."

    show raiden annoyed at f11
    luc "¿Por fin nos dejan salir del autobús?"
    
    show raiden annoyed at t21
    show takahiro ask at f22
    takahiro "Yo pensaba que era una furgoneta."
    
    show raiden annoyed at t31
    show takahiro ask at t32
    show danny sleepy at f33
    danny "Agh, qué luz tan fuerte...\n¿Ya ha llegado a puerto el barco?"
    
    "{color=#8cf}Se ha despertado y todo..."

    show danny sleepy at t33
    show takahiro stand at f32
    takahiro "En cualquier caso, yo me piro de aquí..."
    play sound footsteps
    hide takahiro with dissolve

    hide raiden with dissolve
    hide danny with dissolve
    "{color=#8cf}Uno a uno, los demás siguieron al chico y fueron saliendo del camión."

    show guppy sleep at t11
    pause 1.0
    "{color=#8cf}¿Debería despertarla...?"
    show guppy sleepy at hop
    "{color=#8cf}¡Ah! Pobre niña, parece confusa..."

    play sound footsteps
    hide guppy with dissolve

    pause 1.0
    "{color=#8cf}(...)\nBueno, pues ahora sí que estamos todos."
    "{color=#8cf}Seguí a los demás...{w=0.5}{nw}"

    jump entrance

# Entrando en el recinto
label entrance:
    play sound footsteps
    scene black with fade

    pause 1.0
    play music beautiful_lament
    scene bg entrance with dissolve

    pause 2.0
    "{color=#8cf}Ante nosotros se encontraba un recinto considerablemente grande."
    "{color=#8cf}Parecía algún tipo de campus extraño..."

    show ryu surprise at t21
    show sevony stand at t22
    "{color=#8cf}Ryu respiraba hondo, como si intentara recuperar ahora todo el aire que no había podido inhalar mientras estaba en el camión con tanta gente."
    "{color=#8cf}Sevony observaba sus alrededores, al lado de Ryu, mientras se acomodaba las gafas."
    
    show sevony stand at f22
    sevony "Curioso..."
    
    show sevony stand at t22
    show ryu stand at f21
    ryu "Cuanto menos...\nEste lugar es extraño, ¿no está todo muy preparado?"
    show ryu think at f21 
    ryu "Voy a buscar al conductor del autobús."
    hide ryu with dissolve
    hide sevony with dissolve
    "{color=#8cf}Sevony siguió a Ryu."
    "{color=#8cf}Ryu desprendía una energía melancólica, pero decidida, como si estuviera capacitado para moverse en este tipo de situaciones..."
    "{color=#8cf}Si ya van a ir ellos, yo me quedo aquí..."
    
    $ inv_name = "inv_c0_entrance"
    $ talk = {"umi": "Hablar con la marinera"}
    call screen investigation(inv_name, talk)
    $ talk = {"umi": "Hablar con la marinera"}
    # TODO: En esta investigación también pondremos algunos detalles del fondo, pero por ahora no podemos porque no tenemos la ilustración

# Investigación: Entrada del recinto extraño
label inv_c0_entrance_umi:      # Hablar con la marinera

    show umi stand at t11
    "{color=#8cf}Me acerqué tímidamente a la chica del gorro..."
    akane "Mmm, perdona...\nNo he podido preguntarte tu nombre al final."

    show umi think at f11
    umi "¿Eh? Ah, sí, cierto, fue antes de que el camión acelerara."
    show umi stand at f11
    $ umi.name = "Umi Yoshiharu"
    umi "Me llamo Umi Yoshiharu, ¿y tú?"

    show umi stand at t11
    $ akane.name = "Akane Yamamoto"
    akane "Akane, Akane Yamamoto."

    show umi smile at f11
    umi "Encantada, Akane."
    
    "{color=#8cf}Umi me observó de abajo a arriba y esbozó una sonrisa."
    show umi smile at t11
    "{color=#8cf}No la conozco, pero... me transmite tranquilidad."

    hide umi with dissolve

    python:
        if "umi" in talk:
            del talk["umi"]

    if not talk:
        jump fex_shadow
    else:
        call screen investigation(inv_name, talk)

# Posinvestigación: No hay conductor
label fex_shadow:
    show ryu concern at t21
    show sevony stand at t22
    "{color=#8cf}En ese momento llegaron Sevony y Ryu de vuelta."

    show ryu concern at f21
    ryu "El asiento del conductor estaba vacío... y tampoco hemos encontrado la llave para arrancar el vehículo."

    hide sevony
    hide ryu
    with dissolve

    show raiden annoyed at f21
    show takahiro annoyed at t22
    luc "Eeeh, pues yo estoy empezando a aburrirme."
    
    show raiden annoyed at t21
    show takahiro annoyed at f22
    takahiro "Vaya por Dios... \nYo quería irme de aquí cuanto antes. En fin."

    hide raiden
    hide takahiro
    with dissolve

    show ryu concern at f21
    show sevony stand at t22
    ryu "Sevony... ¿qué deberíamos hacer?"

    show ryu concern at t21
    show sevony concern at f22
    sevony "Parece que tenemos que explorar."

    show sevony concern at t22
    "{color=#8cf}Sevony echó una mirada alrededor.\nHabía algunos caminos que podíamos examinar."
    
    show sevony concern at f22
    sevony "Qué lugar más extraño.{nw}"

    show ryu surprise at h21
    show sevony surprise at h22
    play sound fex_run
    show fex shadow at leftin(x=1500)
    pause 0.5

    "{color=#8cf}Desde el costado del camión salió una pequeña sombra que echó a correr hacia uno de los caminos."

    show guppy happy at f32
    show sevony surprise at t33
    show ryu hurt at t31
    guppy "{sc}¡OOOOH!{/sc}" with vpunch

    play sound footsteps
    hide guppy with dissolve
    "{color=#8cf}La niña del pez en la cabeza se abrió paso a empujones entre Sevony y Ryu, tirando al suelo al segundo. Corrió tras la sombra."
    
    show ryu hurt at s31
    ryu "{sc}¡Ay!{/sc}{w=0.25} ¡O-oye...!"

    "{color=#8cf}Le ha hecho una herida en la rodilla...\nNada grave, pero sangra un poco."

    show sevony surprise at f22
    sevony "¡Itsuki!"

    show sevony surprise at t22
    show ryu hurt at f31
    ryu "N-necesito agua..."

    show ryu hurt at t31
    show sevony stand at f22
    sevony "García... Perdón si es mucho pedir, pero... ¿puedes intentar conseguirle agua? Deberíamos limpiarle la herida."

    show gaelg think at f33
    show ryu hurt at t31
    show sevony stand at t32
    gaelg "¡Claro! Pero... ¿dónde puedo conseguir agua?"

    show gaelg think at t33
    show ryu hurt at f31
    ryu "Eres muy amable, Sevony...\nVeo desde aquí que hay una fuente en la plaza.\n¿Podrías conseguirme el agua en una botella, Gael?"

    show gaelg think at f33
    show ryu hurt at t31
    show sevony stand at t32
    gaelg "¡De acuerdo!"

    show sevony stand at t43
    show gaelg stand at t42
    show gaelg stand at f42
    gaelg "Ah, toma. Un amuleto. Te protegerá de todo mal.\n¡Cualquier cosa, grita! Cazaré salvajes demonios si es necesario para proteger a mis amigos."

    play sound footsteps
    hide gaelg with dissolve

    pause 0.5

    show sevony stand at t43
    show ryu smile at f41
    ryu "G-gracias...\nVaya."

    show ryu smile at t31
    show sevony stand at t33
    show axiom stand at f32

    axiom "Toma."

    show ryu surprise at f31
    ryu "Oh... Un pañuelo."
    ryu "Gracias... Podré usarlo cuando tenga agua."

    show sevony stand at f33
    show ryu surprise at s31
    sevony "Y-yo me encargo de él. Creo que... lo mejor es que los demás vayáis a buscar esa sombra."
    sevony "Si la sombra es el conductor, seguro que sabe dónde estamos."

    hide sevony
    hide ryu
    hide axiom
    with dissolve

    show raiden annoyed at t31
    show ichika stand at t32
    show danny stand at t33

    show raiden annoyed at f31
    luc "En fin..."

    show raiden annoyed at t31
    show danny stand at f33
    danny "No sé qué coño era eso, pero deberíamos ir..."

    show danny stand at t33
    akane "¡E-esperad! ¿Y si no es el conductor?"


    show ichika stand at f32
    ichika "¡Da igual lo que fuera, será mejor que vayamos tras él!"
    
    play audio footsteps

    hide raiden
    hide danny
    hide ichika
    with dissolve

    "{color=#8cf}Algunos con más prisa que otros, todos dejaron atrás a Ryu y Sevony para perseguir a la silueta."
    "{color=#8cf}Yo también lo hice, para no separarme del grupo."

    scene black with fade

    jump fex_search

# Buscando a la sombra en la plaza
label fex_search:
    show bg plaza with fade
    "{color=#8cf}En el centro del recinto había situada una plaza tranquila."
    "{color=#8cf}Los demás ya están investigando por ahí."
    $ inv_name = "inv_c0_plaza"
    $ talk = {"umi": "Umi Yoshiharu", "ghiang": "Chica de los moños"}
    $ obj = {"tree": (755, 149, "Árbol"), "fountain": (179, 349, "Fuente"), "buildings": (165, 217, "Edificios en la distancia"), "street": (405, 475, "Camino")}
    call screen investigation(inv_name, talk, obj, "plaza")
    $ talk = {"umi": "Umi Yoshiharu", "ghiang": "Chica de los moños"}

# Investigación: Plaza
label inv_c0_plaza_umi:         # Umi Yoshiharu
    show umi think at focus
    umi "¿Cuánta pasta tienen los dueños de este sitio?"
    hide umi with dissolve
    
    python:
        if "umi" in talk:
            del talk["umi"]

    call screen investigation(inv_name, talk, obj, "plaza")

label inv_c0_plaza_ghiang:      # Chica de los moños
    show ghiang yell at focus
    ghiang "Veeenga, conductor, ¿dónde te has metido?"
    hide ghiang with dissolve

    python:
        if "ghiang" in talk:
            del talk["ghiang"]

    call screen investigation(inv_name, talk, obj, "plaza")

label inv_c0_plaza_tree:        # Árbol
    "{color=#8cf}La vegetación de la plaza hace que corra el aire fresco. Ideal para crear un ambiente calmado."

    play sound tree_shake
    "{color=#090}Fras, fras..." with flash

    "{color=#8cf}¿Eh? ¿Se ha movido algo por ahí?"

    jump fex_chase

label inv_c0_plaza_fountain:    # Fuente
    "{color=#8cf}En el centro de la plaza hay una fuente muy bonita."
    python:
        if "fountain" in obj:
            del obj["fountain"]

    call screen investigation(inv_name, talk, obj, "plaza")

label inv_c0_plaza_street:      # Camino
    "{color=#8cf}Varios caminos salen de la plaza y comunican con los edificios que hay en el horizonte."

    python:
        if "street" in obj:
            del obj["street"]

    call screen investigation(inv_name, talk, obj, "plaza")

label inv_c0_plaza_buildings:   # Edificios en la distancia
    "{color=#8cf}Desde aquí se ven todos los edificios que hay repartidos por el lugar, pero no puedo distinguir qué son..."

    python:
        if "buildings" in obj:
            del obj["buildings"]

    call screen investigation(inv_name, talk, obj, "plaza")

label fex_chase:
    show guppy stare at focus
    stop music fadeout 2.0
    guppy "({w=0.4}.{w=0.4}.{w=0.4}.{w=0.4})"

    play sound footsteps
    hide guppy with dissolve
    
    pause 0.5
    akane "¿Qué está haciendo...?"
    play music kitsune_to_tanuki
    play sound tree_shake
    "{color=#8cf}La niña escaló el árbol con gran agilidad, igual que un animal persiguiendo a su presa."

    play sound [tree_shake, fex_run]
    "{color=#090}Fras, fras...{w=0.6} ¡Hop!"
    "{color=#8cf}¡Y su presa, la sombra, ha escapado saltando a otro árbol cercano!"
    play sound [fex_run, tree_shake]
    "{color=#090}¡Hop!"
    pause 1.0

    show takahiro laugh at f21
    show umi smile at t22
    takahiro "Sí que se lo pasa bien."
    
    show takahiro laugh at t21
    show umi smile at f22
    umi "Está tanteando el terreno."

    show umi smile at t22
    "{color=#8cf}Si sigue saltando a lo loco, se podría caer y hacer daño..."

    menu:   # TODO: Cambiar la pantalla del menú de elecciones
        "¿No deberíamos hacer algo...?":
            akane "¿No deberíamos hacer algo...?"
            
            show umi smile at t22
            show takahiro laugh at f21
            takahiro "Qué va, es más divertido dejarlo estar."
            
            show takahiro laugh at t21
            show umi smile at f22
            umi "Estará bien. Parece bastante ágil."

        "(...)":
            akane "(...)"
            "{color=#8cf}Bueno, parece bastante ágil... Estará bien."

    "FIN"
    return
