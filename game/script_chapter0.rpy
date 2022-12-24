# Inicio del juego
label ch0_intro:

    play sound tv_on
    pause 2.0
    play music breaking

    "{sy}¡Alerta! ¡Alerta!\n¡Caos en la ciudad!"

    scene cg c0_breaking with fade

    "{sy}En las últimas 24 horas se ha desatado una gran cantidad de incidentes en el este, oeste y centro de la ciudad de Gekkou."
    "{sy}La intensidad de estos ataques va aumentando con el paso de las horas, se recomienda..."

    stop music fadeout 0.3
    play sound tv_static fadein 0.5
    show cg c0_static

    "{sy}(...)"

    scene black with fade
    stop sound fadeout 1.5

    $ renpy.movie_cutscene("movie/pr_title.webm")

# Despertar en el camión
label truck:

    play music "audio/truck_engine.ogg" fadein 1.0
    show bg truck with fade

    "{th}Cuando me desperté, todo estaba oscuro."
    "{th}Me encontraba en lo que parecía ser un camión de transporte."
    "{th}Podía escuchar el motor del vehículo y, a mi alrededor, pude distinguir a más gente despertar como yo."

    show ryu 0_0 at t11
    "{th}Un chico de pelo claro permanecía sentado, abrazado a sus piernas, en silencio al fondo del camión."
    "{th}Lo oí soltar un suspiro de angustia justo antes de hundir la cabeza entre las piernas."
    hide ryu with dissolve

    show sevony 1_3 at t11
    "{th}También había una chica con gafas que inhaló y espiró en un claro intento de tranquilizarse."
    "{th}Echó una mirada a su alrededor, justo antes de..."

    show sevony 1_6 at h11
    play sound "audio/truck_bump.ogg"
    with vpunch
    "{sy}¡Pam!"

    "{th}Un bache en el camino despertó a casi todos los que seguían dormidos..."
    "{th}Ahora que hay más gente despierta, tal vez debería fijarme en quiénes son mis compañeros de viaje..."

    hide sevony with dissolve
    "{sy}Haz clic en el icono del personaje en quien te quieras fijar.{fast}"

    $ inv_name = "inv_c0_truck"
    $ talk = {
        "ryu": "Chico rubio",
        "jaeke": "Chico antipático"
    }    # Elementos a investigar
    call screen investigation(inv_name, talk)
    $ talk = {
        "ryu": "Chico rubio",
        "jaeke": "Chico antipático"
    }    # Lo definimos dos veces para que el usuario pueda volver atrás y sus opciones sean restauradas

# Investigación: Camión
label inv_c0_truck_ryu:     # Chico rubio
    $ ryu.name = "Rubio"
    $ gaelg.name = "Chamán"
    $ sevony.name = "Gafas"

    show ryu 0_1 at t21
    show sevony 1_6 at t22
    "{th}Las gafas de la chica de pelo violeta habían salido despedidas por culpa del bache."
    show ryu 0_1 at s21
    "{th}El rubio se agachó al oírlas caer. Habían aterrizado cerca de él."
    show ryu 0_1 at t32
    "{th}Gateó un poco hasta alcanzarlas y se las acercó a su dueña, con una cálida sonrisa."

    show ryu 0_15 at f32
    ryu "Toma, ve con cuidado... Sería una pena que se te rompieran."

    "{th}Lo dijo flojito, como si no quisiera llamar demasiado la atención en un ambiente tan tenso."

    show ryu 0_15 at t21
    show sevony 1_4 at f22
    sevony "(...)\nMuchas gracias."
    show sevony 1_3
    sevony "Vaya carretera en la que nos han metido."

    show sevony 1_3 at t22
    show ryu 0_5 at f21
    ryu "Pues... sí, la verdad."

    hide sevony
    hide ryu
    with dissolve

    show gaelg 0_0 at t11
    "{th}Un chico que parecía nervioso y confundido observaba la conversación."
    "{th}Los miraba mientras murmuraba para sí mismo."

    show gaelg 0_0 at d11
    gaelg "Mi chamanismo me sacará de esta.\nEscaparé de aquí."

    "{th}Finalmente, consiguió reunir valor para hablarle a los presentes en lugar de al cuello de la camisa."

    show gaelg 0_1 at hf11
    gaelg "Hum... ¿C-cómo te llamas?"

    show gaelg 0_1 at t31
    pause 0.2
    show ryu 0_32 at t32
    show sevony 0_0 at t33
    pause 0.5
    show ryu 0_32 at hf32
    ryu "¿Y-yo? V-vaya por Dios."
    show ryu 0_15
    $ ryu.name = "Ryu Itsuki"
    ryu "Mi nombre... es Ryu Itsuki.\nSoy un simple desempleado."
    ryu "¿Y vosotros, chica de las gafas, chico moreno?"
    show ryu 0_15 at t32

    $ sevony.name = "Sevony"
    show sevony 0_4 at f33
    sevony "Un gusto, Itsuki-kun. Mi nombre es Sevony."
    show sevony 0_4 at t33

    $ gaelg.name = "Gabriel"
    show gaelg 0_3 at f31
    gaelg "A-ah... yo soy... Gabriel..."

    "{th}Gabriel se quedó bloqueado por un momento."

    show gaelg 0_6 at hf31
    $ gaelg.name = "Gael García"
    gaelg "¡QUIERO DECIR! Gael. Gael García, a tu servicio."
    show gaelg 0_6 at t31

    "{th}¿En serio se le ha olvidado su propio nombre?"

    show ryu 0_36 at f32
    ryu "Sevony y Gael... Tenéis nombres exóticos, son bonitos."

    "{th}La expresión de Ryu se había apagado."

    show ryu 0_35 at f32
    ryu "Sevony... Me recuerdas a alguien, ¿sabes? Aunque tal vez solo sea mi imaginación."
    show ryu 0_36 at t32

    show sevony 0_1 at hf33
    sevony "Más que seguro, su imaginación. Mucha gente pasa por la ciudad."

    "{th}Sevony ha contestado muy rápido..."
    show sevony 0_1 at t33
    show ryu 0_36 at f32
    ryu "Hum... Seguramente sea eso."
    ryu "He conocido a mucha gente a lo largo de mi vida, no sería la primera vez que me ocurre."

    show ryu 0_36 at t32
    show gaelg 0_4 at f31
    gaelg "Ryu... ¿Igual que «dragón» en japonés?"

    show gaelg 0_4 at t31
    show ryu 0_15 at hf32
    ryu "{bt=a1-p10-s1}Efectivamente.{/bt} No sé muy bien por qué escogieron ese nombre para mí..."
    show ryu 0_36 at s32
    ryu "Un dragón da mucho miedo y escupe... fuego..."

    show gaelg 0_4 at hf31
    gaelg "¡Yo creo que mola!\nY usted, señorita Sevony, ¿de dónde es?"

    show gaelg 0_4 at t31
    show sevony 0_2 at f33
    sevony "Soy de Gekkou, una ciudad un poco al norte de aquí."

    "{th}Su sonrisa amable contrastaba con el tono frío, seguramente involuntario, de su voz."

    show sevony 0_2 at t33
    show gaelg 0_4 at f31
    gaelg "O sea que sois japoneses... ¡Entonces... podré aprender mucho de otras culturas!"
    gaelg "Hoy es una victoria para el {b}chamán definitivo{/b}."

    show ryu 1_6 at t32
    "{th}Al oír el talento definitivo de Gael, Ryu lo miró con interés."

    show gaelg 0_4 at t31
    show ryu 1_5 at f32
    ryu "Chamán... Qué interesante."

    show ryu 1_5 at t32
    "{th}¿Será este el inicio de una agradable amistad?"

    play sound "audio/truck_bump.ogg"
    with vpunch
    "{sy}¡Pam!"

    "{th}¡¿Otro bache?!"

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

    show jaeke 0_0 at t21
    show takahiro 0_5 at t22
    with dissolve

    "{th}En una esquina del vehículo se encontraba un chico con cara de pocos amigos."
    "{th}Otro muchacho con ropa llamativa se le acercó."

    show takahiro 0_3 at f22
    takahiro "Eh, ¿y tú eres...?"
    show takahiro 0_3 at t22

    show jaeke 2_2
    "{th}El moreno le devolvió una fría mirada y no medió palabra."

    show takahiro 1_3 at f22
    takahiro "Ya veo que eres alguien con quien es fácil hablar..."
    show takahiro 1_3 at t22

    show jaeke 2_3 at t32
    "{th}Nada más oír eso, el mudo se levantó, se le acercó y empezó a susurrar."

    show jaeke 2_3 at f32
    jaeke "Ten cuidado conmigo, chaval.\nNo sabes con quién estás hablando."
    show jaeke 2_3 at t32

    show takahiro 0_2 at f22
    takahiro "Pues claro que no sé con quién estoy hablando, ni siquiera me has dicho tu nombre."
    show takahiro 0_2 at t22

    show jaeke 2_3 at t21
    pause 0.5
    show jaeke 2_4 at f21
    jaeke "Los comediantes como tú solo les hacen gracia a los pringados de la cárcel."
    jaeke "Mejor haz algo productivo, porque no tienes ninguna gracia, fracasado."
    show jaeke 2_3 at t21

    "{th}Vaya humos se gasta..."

    play sound truck_bump
    with vpunch
    "{sy}¡Pam!"

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
    
    "{th}Creo que ya he escuchado suficiente...\nNo parece que nadie sepa cómo hemos llegado hasta aquí."
    "{th}¿Cómo ha podido pasar esto?\n¿Habré hecho algo para acabar aquí...?"
    "{th}Me decidí a intentar obtener información yo misma."

    akane "Esto... ¿Alguien sabe dónde estamos?"

    show umi 0_0 at t11
    "{th}Una chica muy guapa vestida con un gorro de marinero me dirigió la mirada al oírme."

    show umi 0_3 at f11
    umi "No lo sé, pero es un vehículo en movimiento, así que tampoco tiene sentido preguntarse eso hasta que lleguemos."
    umi "Lo mejor será mantener la calma."

    show umi 0_3 at t11
    akane "Supongo que tienes razón, pero quería preguntar por si alguien lo sabía..."

    show umi 0_0 at t21
    show emiko 3_5 at f22
    emiko "¿Eh? Espera... ¿entonces de verdad nadie sabe hacia dónde vamos o siquiera dónde estamos?"

    show umi 0_0 at t31
    show emiko 3_5 at t32
    show raiden 1_7 at f33
    luc "Si lo supiéramos, ya habría contestado alguien, ¿no?\nA menos que se lo quiera callar."
    show raiden 2_3 at hf33
    luc "Imaginaos que nos han secuestrado o algo y pretenden deshacerse de nosotros, ¡ja, ja!"

    show raiden 2_3 at t33
    akane "¡¿Secuestrarnos?! ¡¿Y qué se supone que hemos hecho para acabar en una situación así?!"

    show raiden 2_4 at f33
    luc "Vamos, solo era una broma."
    luc "Yo, al menos, no he hecho nada malo. Los demás, no sé."

    show umi 0_4 at h31
    show emiko 3_10 at h32
    show raiden 0_7 at h33
    play sound truck_bump
    with vpunch
    "{sy}¡Pam!"

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
    "{sc}{color=#090}¡Pum, pam, pom, pum!{/sc}"
    
    "{th}Por culpa de todos esos baches, me golpeé la cabeza con el techo del vehículo."

    show umi 1_2 at focus
    umi "¿Te encuentras bien?"

    show umi 1_2 at t11
    akane "S-sí..." 
    "{th}Tal vez yo también debería entablar conversación con alguien..."
    akane "P-por cierto, ¿cómo te lla...?"

    hide umi with dissolve
    "{th}Pero no pude acabar de formular mi pregunta."
    show bg truck_move
    play music truck_speed fadein 1.0 fadeout 0.5
    "{th}El vehículo comenzó a serpentear repentinamente, arrojándonos a mí y a los demás pasajeros de un lado a otro." with vpunch
    "{th}Cada vez más rápido, vi que algunos se sostenían a sus asientos como podían, yo me vi forzada a hacer lo mismo..."
    stop music fadeout 1.0
    show bg truck
    "{th}Hasta que, al fin, paró."
    "{th}Joder... Qué daño..."
    "{th}Yo había acabado en el suelo, pero no era la única..."

    show axiom 0_4 at s11
    axiom "(...)"

    akane "¡Aah! ¿Estás bien?"
    "{th}Fui a buscar mi pañuelo, pero la marinera fue más rápida que yo."
    
    show axiom 0_4 at t21
    show umi 1_7 at t22
    pause 0.3
    show umi 1_7 at f22
    umi "¿Necesitas ayuda?\nToma, ponte esto para taponar la herida..." 

    hide umi 
    hide axiom
    with dissolve

    show guppy 0_20 at s22
    show danny 1_1 at s21
    with dissolve
    "{th}Y también había dos personas durmiendo en el suelo..."
    "{th}Tener buen dormir es una cosa, pero no despertarte con todos esos baches es otra..."

    play sound truck_door
    pause 2.0
    scene bg truck_light with dissolve
    "{th}Y entonces, la puerta se abrió."

    show raiden 0_11 at hf11 with vpunch
    luc "¡AAH, LA LUZ! ¡Mis ojos!"

    show raiden 0_11 at t11
    akane "¿Estás bie...?{nw}"
    play sound feed1
    with flash
    with vpunch
    akane "¡AGH, MIS OJOS!"
    "{th}La luz entró de golpe en el interior de la parte trasera del camión, acompañado de una corriente de aire refrescante."

    show raiden 0_4 at f11
    luc "¿Por fin nos dejan salir del autobús?"
    
    show raiden 0_4 at t21
    show takahiro 0_7 at f22
    takahiro "Yo pensaba que era una furgoneta."
    
    show raiden 0_4 at t31
    show takahiro 0_4 at t32
    show danny 0_3 at f33
    danny "Agh, qué luz tan fuerte...\n¿Ya ha llegado a puerto el barco?"
    
    "{th}Se ha despertado y todo..."

    show danny 0_3 at t33
    show takahiro 0_5 at f32
    takahiro "En cualquier caso, yo me piro de aquí..."
    play sound footsteps
    hide takahiro with dissolve

    hide raiden with dissolve
    hide danny with dissolve
    "{th}Uno a uno, los demás siguieron al chico y fueron saliendo del camión."

    show guppy 0_20 at t11
    pause 1.0
    "{th}¿Debería despertarla...?"
    show guppy 0_7 at hop
    "{th}¡Ah! Pobre niña, parece confusa..."

    play sound footsteps
    hide guppy with dissolve

    pause 1.0
    "{th}(...)\nBueno, pues ahora sí que estamos todos."
    "{th}Seguí a los demás...{w=0.5}{nw}"

    jump entrance

# Entrando en el recinto
label entrance:
    play sound footsteps
    scene black with fade

    pause 1.0
    play music beautiful_lament
    scene bg entrance with dissolve

    pause 2.0
    "{th}Ante nosotros se encontraba un recinto considerablemente grande."
    "{th}Parecía algún tipo de campus extraño..."

    show ryu 0_34 at t21
    show sevony 1_2 at t22
    "{th}Ryu respiraba hondo, como si intentara recuperar ahora todo el aire que no había podido inhalar mientras estaba en el camión con tanta gente."
    "{th}Sevony observaba sus alrededores, al lado de Ryu, mientras se acomodaba las gafas."
    
    show sevony 1_2 at f22
    sevony "Curioso..."
    
    show sevony 1_2 at t22
    show ryu 0_0 at f21
    ryu "Cuanto menos...\nEste lugar es extraño, ¿no está todo muy preparado?"
    show ryu 0_0 at f21 
    ryu "Voy a buscar al conductor del autobús."
    hide ryu with dissolve
    hide sevony with dissolve
    "{th}Sevony siguió a Ryu."
    "{th}Ryu desprendía una energía melancólica, pero decidida, como si estuviera capacitado para moverse en este tipo de situaciones..."
    "{th}Si ya van a ir ellos, yo me quedo aquí..."
    
    $ inv_name = "inv_c0_entrance"
    $ talk = {
        "umi": "Hablar con la marinera"
    }
    call screen investigation(inv_name, talk)
    $ talk = {
        "umi": "Hablar con la marinera"
    }
    # TODO: En esta investigación también pondremos algunos detalles del fondo, pero por ahora no podemos porque no tenemos la ilustración

# Investigación: Entrada del recinto extraño
label inv_c0_entrance_umi:      # Hablar con la marinera

    show umi 0_0 at t11
    "{th}Me acerqué tímidamente a la chica del gorro..."
    akane "Mmm, perdona...\nNo he podido preguntarte tu nombre al final."

    show umi 1_2 at f11
    umi "¿Eh? Ah, sí, cierto, fue antes de que el camión acelerara."
    show umi 0_10 at f11
    $ umi.name = "Umi Yoshiharu"
    umi "Me llamo Umi Yoshiharu, ¿y tú?"

    show umi 0_10 at t11
    $ akane.name = "Akane Yamamoto"
    akane "Akane, Akane Yamamoto."

    show umi 2_1 at f11
    umi "Encantada, Akane."
    
    "{th}Umi me observó de abajo a arriba y esbozó una sonrisa."
    show umi 2_1 at t11
    "{th}No la conozco, pero... me transmite tranquilidad."

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
    show ryu 2_8 at t21
    show sevony 1_4 at t22
    "{th}En ese momento llegaron Sevony y Ryu de vuelta."

    show ryu 2_1 at f21
    ryu "El asiento del conductor estaba vacío... y tampoco hemos encontrado la llave para arrancar el vehículo."

    hide sevony
    hide ryu
    with dissolve

    show raiden 0_5 at f21
    show takahiro 1_3 at t22
    luc "Eeeh, pues yo estoy empezando a aburrirme."
    
    show raiden 0_5 at t21
    show takahiro 1_3 at f22
    takahiro "Vaya por Dios... \nYo quería irme de aquí cuanto antes. En fin."

    hide raiden
    hide takahiro
    with dissolve

    show ryu 1_7 at f21
    show sevony 1_4 at t22
    ryu "Sevony... ¿qué deberíamos hacer?"

    show ryu 1_7 at t21
    show sevony 1_3 at f22
    sevony "Parece que tenemos que explorar."

    show sevony 1_3 at t22
    "{th}Sevony echó una mirada alrededor.\nHabía algunos caminos que podíamos examinar."
    
    show sevony 1_2 at f22
    sevony "Qué lugar más extraño.{nw}"

    show ryu 0_22 at h21
    show sevony 1_6 at h22
    play sound fex_run
    show fex shadow at leftin(x=1500)
    pause 0.5

    "{th}Desde el costado del camión salió una pequeña sombra que echó a correr hacia uno de los caminos."

    show guppy 0_17 at f32
    show sevony 1_6 at t33
    show ryu 2_3 at t31
    play sound feed1
    pause 0.2
    guppy "{sc}¡HAAALA!{/sc}" with vpunch

    play sound footsteps
    hide guppy with dissolve
    "{th}La niña del pez en la cabeza se abrió paso a empujones entre Sevony y Ryu, tirando al suelo al segundo. Corrió tras la sombra."
    
    show ryu 2_3 at s31
    ryu "{sc}¡Ay!{/sc}{w=0.25} ¡O-oye...!"

    "{th}Le ha hecho una herida en la rodilla...\nNada grave, pero sangra un poco."

    show sevony 1_5 at f22
    sevony "¡Itsuki!"

    show sevony 1_5 at t22
    show ryu 2_3 at f31
    ryu "N-necesito agua..."

    show ryu 2_3 at t31
    show sevony 1_3 at f22
    sevony "García... Perdón si es mucho pedir, pero... ¿puedes intentar conseguirle agua? Deberíamos limpiarle la herida."

    show gaelg 0_3 at f33
    show ryu 2_3 at t31
    show sevony 1_3 at t32
    gaelg "¡Claro! Pero... ¿dónde puedo conseguir agua?"

    show gaelg 0_3 at t33
    show ryu 2_2 at f31
    ryu "Eres muy amable, Sevony...\nVeo desde aquí que hay una fuente en la plaza.\n¿Podrías conseguirme el agua en una botella, Gael?"

    show gaelg 0_3 at f33
    show ryu 2_2 at t31
    show sevony 1_3 at t32
    gaelg "¡De acuerdo!"

    show sevony 1_2 at t43
    show gaelg 0_0 at t42
    show gaelg 0_0 at f42
    gaelg "Ah, toma. Un amuleto. Te protegerá de todo mal.\n¡Cualquier cosa, grita! Cazaré salvajes demonios si es necesario para proteger a mis amigos."

    play sound footsteps
    hide gaelg with dissolve

    pause 0.5

    show sevony 1_2 at t43
    show ryu 0_19 at f41
    ryu "G-gracias...\nVaya."

    show ryu 0_19 at t31
    show sevony 1_2 at t33
    show axiom 0_0 at f32

    axiom "Toma."

    show ryu 0_20 at f31
    ryu "Oh... Un pañuelo."
    ryu "Gracias... Podré usarlo cuando tenga agua."

    show sevony 1_4 at f33
    show ryu 0_20 at s31
    sevony "Y-yo me encargo de él. Creo que... lo mejor es que los demás vayáis a buscar esa sombra."
    sevony "Si la sombra es el conductor, seguro que sabe dónde estamos."

    hide sevony
    hide ryu
    hide axiom
    with dissolve

    show raiden 0_5 at t31
    show ichika 0_0 at t32
    show danny 0_0 at t33

    show raiden 0_6 at f31
    luc "En fin..."

    show raiden 0_6 at t31
    show danny 0_0 at f33
    danny "No sé qué coño era eso, pero deberíamos ir..."

    show danny 0_0 at t33
    akane "¡E-esperad! ¿Y si no es el conductor?"


    show ichika 0_2 at f32
    ichika "¡Da igual lo que fuera, será mejor que vayamos tras él!"
    
    play audio footsteps

    hide raiden
    hide danny
    hide ichika
    with dissolve

    "{th}Algunos con más prisa que otros, todos dejaron atrás a Ryu y Sevony para perseguir a la silueta."
    "{th}Yo también lo hice, para no separarme del grupo."

    scene black with fade

    jump fex_search

# Buscando a la sombra en la plaza
label fex_search:
    show bg plaza with fade
    "{th}En el centro del recinto había situada una plaza tranquila."
    "{th}Los demás ya están investigando por ahí."
    $ inv_name = "inv_c0_plaza"
    $ talk = {
        "umi": "Umi Yoshiharu",
        "ghiang": "Chica de los moños",
        "jaeke": "Chico antipático"
    }
    $ obj = {
        "tree": (755, 149, "Árbol"),
        "fountain": (179, 349, "Fuente"),
        "buildings": (165, 217, "Edificios en la distancia"),
        "street": (405, 475, "Camino")
    }
    call screen investigation(inv_name, talk, obj, "plaza")
    $ talk = {
        "umi": "Umi Yoshiharu",
        "ghiang": "Chica de los moños",
        "jaeke": "Chico antipático"
    }

# Investigación: Plaza
label inv_c0_plaza_umi:         # Umi Yoshiharu
    show umi 1_4 at focus
    umi "¿Cuánta pasta tienen los dueños de este sitio?"
    hide umi with dissolve
    
    python:
        if "umi" in talk:
            del talk["umi"]

    call screen investigation(inv_name, talk, obj, "plaza")

label inv_c0_plaza_ghiang:      # Chica de los moños
    show ghiang 1_1 at focus
    ghiang "Veeenga, conductor, ¿dónde te has metido?"
    hide ghiang with dissolve

    python:
        if "ghiang" in talk:
            del talk["ghiang"]

    call screen investigation(inv_name, talk, obj, "plaza")

label inv_c0_plaza_jaeke:       # Chico antipático
    show takahiro 0_0 at t21
    show jaeke 0_3 at f22
    jaeke "Eh."
    jaeke "¿Sabéis algo de la situación actual?"

    show takahiro 0_12 at f21
    show jaeke 0_3 at t22
    takahiro "Vaya, vaya. Veo que te dignas por fin a hablarme."
    show takahiro 0_6 at f21
    takahiro "Lo único que sé es que hay gente... bastante peculiar."
    
    show takahiro 0_6 at t21
    show jaeke 0_1 at f22
    jaeke "Antes has estado hablando con ellos... ¿No has sido capaz de preguntar absolutamente nada que nos sea de utilidad?"

    show jaeke 0_1 at t22
    show takahiro 0_5 at f21
    takahiro "Diría que todos sabemos lo mismo de este lugar, así que no creo que nadie tenga información realmente útil."

    show takahiro 0_5 at t21
    show jaeke 2_2 at f22
    jaeke "Pues tampoco perdías nada por preguntar por lo menos, estúpido."
    show jaeke 2_1 at f22
    jaeke "Agh... Está bien. A partir de ahora, trabajarás para mí. A ver si así consigues hacer algo bien."

    show jaeke 2_1 at t22
    "{th}Si sigo escuchando a ese chico, me va a acabar dando dolor de cabeza."
    
    hide jaeke
    hide takahiro
    with dissolve

    python:
        if "jaeke" in talk:
            del talk["jaeke"]

    call screen investigation(inv_name, talk, obj, "plaza")

label inv_c0_plaza_tree:        # Árbol
    "{th}La vegetación de la plaza hace que corra el aire fresco. Ideal para crear un ambiente calmado."

    play sound tree_shake
    "{sy}Fras, fras..." with flash

    "{th}¿Eh? ¿Se ha movido algo por ahí?"

    jump fex_chase

label inv_c0_plaza_fountain:    # Fuente
    "{th}En el centro de la plaza hay una fuente muy bonita."

    show raiden 0_3 at t21
    show gaelg 0_2 at t22
    pause 0.4
    show gaelg 0_2 at f22
    gaelg "Fuente, fuente... ¿No había una fuente por aquí?"
    show gaelg 0_2 at t22
    luc "(...)"
    show gaelg 0_2 at f22
    gaelg "Decían que había una fuente, pero..."

    play sound feed1
    show gaelg 0_6 at h22
    show raiden 1_12 at hf21
    luc "¡GAEL! ¡AQUÍ HAY AGUA!" with hpunch

    hide raiden
    hide gaelg
    with dissolve

    python:
        if "fountain" in obj:
            del obj["fountain"]

    call screen investigation(inv_name, talk, obj, "plaza")

label inv_c0_plaza_street:      # Camino
    "{th}Varios caminos salen de la plaza y comunican con los edificios que hay en el horizonte."

    python:
        if "street" in obj:
            del obj["street"]

    call screen investigation(inv_name, talk, obj, "plaza")

label inv_c0_plaza_buildings:   # Edificios en la distancia
    "{th}Desde aquí se ven todos los edificios que hay repartidos por el lugar, pero no puedo distinguir qué son..."

    python:
        if "buildings" in obj:
            del obj["buildings"]

    call screen investigation(inv_name, talk, obj, "plaza")

# Posinvestigación: Guppy persigue a Monofex
label fex_chase:
    show guppy 1_3 at focus
    stop music fadeout 2.0
    guppy "({w=0.4}.{w=0.4}.{w=0.4}.{w=0.4})"

    play sound footsteps
    hide guppy with dissolve
    
    pause 0.5
    akane "¿Qué está haciendo...?"
    play music kitsune_to_tanuki
    play sound tree_shake
    "{th}La niña escaló el árbol con gran agilidad, igual que un animal persiguiendo a su presa."

    play sound [tree_shake, fex_run]
    "{sy}Fras, fras...{w=0.6} ¡Hop!"
    "{th}¡Y su presa, la sombra, ha escapado saltando a otro árbol cercano!"
    play sound [fex_run, tree_shake]
    "{sy}¡Hop!"
    pause 1.0

    show takahiro 0_2 at f21
    show umi 0_13 at t22
    takahiro "Sí que se lo pasa bien."
    
    show takahiro 0_2 at t21
    show umi 0_14 at f22
    umi "Está tanteando el terreno, comprobando si el sitio es seguro."

    show umi 0_13 at t22
    "{th}Si sigue saltando a lo loco, se podría caer y hacer daño..."

    menu:
        "¿No deberíamos hacer algo...?":
            akane "¿No deberíamos hacer algo...?"
            
            show umi 0_13 at t22
            show takahiro 0_2 at f21
            takahiro "Qué va, es más divertido dejarlo estar."
            
            show takahiro 0_2 at t21
            show umi 0_14 at f22
            umi "Estará bien. Parece bastante ágil."

        "(...)":
            akane "(...)"
            "{th}Bueno, parece bastante ágil... Estará bien."

    hide takahiro
    hide umi
    with dissolve

    play sound feed1
    "{sy}Paf." with hpunch

    "{th}¡Pero si se acaba de chocar contra un tronco!"

    show guppy 2_2 at t11
    guppy "(...)"
    show guppy 0_18 at h11
    guppy "({sc}!!!{/sc})"

    "{th}Pobrecita, se ha llevado un buen golpe... Y parece asustada..."
    "{th}El ruido de los árboles ha parado. Fuera lo que sea, ya habrá escapado."

    stop music fadeout 1.0
    play sound announcement
    pause 5.0

    show guppy 2_2 at h11
    fex "{sy}¡Ejem, ejem! Atención todo el mundo. ¡Atención!"

    "{th}Empezó a sonar una voz chillona incorpórea. A juzgar por la calidad del sonido, provenía de los altavoces de un sistema de megafonía."

    hide guppy with dissolve

    fex "{sy}Me gustaría que, por favor, volviérais por donde vinisteis...\n{bo}{color=#090}El espectáculo comenzará pronto.{/bt}"

    akane "¿Qué...? ¿Un espectáculo?"

    show ichika 0_5 at f21
    ichika "¡Qué bien! ¡Nos han preparado un espectáculo de bienvenida y todo!"
    
    show ichika 0_7 at t21
    show ghiang 0_1 at f22
    ghiang "No sé yo... A mí me huele a chamusquina."

    show ghiang 0_1 at t22
    akane "Tampoco tenemos mucho más que hacer, ¿no? Y seguramente consigamos nueva información una vez vayamos allí..."
    akane "Esa voz... tiene que ser la persona que nos ha traído hasta aquí."

    show ichika 0_7 at t31
    show ghiang 0_1 at t32
    show gaelm 0_5 at f33

    gaelm "S-sí... Yo diría que lo mejor es que hagamos caso... S-si queréis, claro."

    hide ichika
    hide ghiang
    hide gaelm
    with dissolve

    play sound footsteps
    "{th}No hay más remedio. Regresamos a la entrada, con paso pesado y una extraña sensación..."

    scene black with fade
    jump sevony_exec

# Bienvenidos al juego de matanza mutua
label sevony_exec:
    show bg entrance with fade
    
    show sevony 1_3 at t22
    show ryu 0_20 at t21    
    "{th}Sevony está usando el pañuelo que le dio el de la mascarilla para limpiar la herida."

    show ryu 0_20 at f21
    ryu "A-ay... Eres muy amable, Sevony..."
    ryu "Estoy seguro de que me recuerdas a alguien..."
    ryu "¿Cuál es tu apellido, a todo esto? Ya que tú me llamas Itsuki..."

    show ryu 0_20 at t21
    show sevony 1_1 at f22
    sevony "Ah... Siento mis modales... Es cierto que no me he presentado adecuadamente."
    show sevony 1_5 at f22
    sevony "{b}Maáz{/b}." with flash

    show sevony 1_5 at t22
    show ryu 0_22 at f21
    ryu "¿P-perdona?"

    scene cg c0_sevonyknife with fade
    play sound knife_slide
    with flash
    pause 0.5
    $ sevony.name = "Sevony Maáz"
    play music living_to_the_fullest
    sevony "Mi apellido...{w=0.5} es Maáz."
    sevony "Pero en el fondo ya lo sabías... ¿verdad, Ryu?"

    ryu "(...)"
    ryu "Maldita..."
    ryu "Je, je. Supongo que no todo podía salir bien, ¿verdad?"

    stop music fadeout 2.0
    show cg c0_ryubutton with fade
    #"{th}Ryu sacó algo de su bolsillo..."
    play sound button_click
    "{sy}Clic." with flash
    show black
    play sound cannon
    "{th}Sevony fue propulsada hacia el cielo en un vuelo sin destino por una plataforma del suelo."
    play sound countdown
    queue sound countdown volume 0.8
    queue sound countdown volume 0.4
    queue sound countdown volume 0.2
    pause 2.0
    play sound explosion3
    scene cg c0_skyexplosion with vpunch
    pause 2.0
    play music weekly_despair

    "{th}Explotó en un baño de sangre en el cielo."
    "{th}Me llevé las manos a las orejas instintivamente para taparme los oídos."
    "{th}Todos los demás estábamos... sin palabras. Inmóviles. Incrédulos."

    show bg entrance with fade
    show ryu 0_26 at f11
    ryu "Imbécil... Siempre tiene que salir algo mal... ¿Cómo se me pudo pasar? Malditas cucarachas entrometidas."

    play sound fex_run
    show fex 0_1 at l21
    pause 0.5
    show fex 0_1 at f21
    show ryu 0_26 at t11
    fex "¡Pero cómo se te ocurre hacer una ejecución sin mí!"

    show fex 0_1 at t21
    "{th}¿Eso es... un zorro que habla?"
    "{th}¡Es la voz que sonaba de los altavoces!"
    "{th}Y por el tamaño... tiene que ser también la sombra que perseguíamos antes."
    play sound feed1
    show fex 1_4 at t21
    show ryu 0_27 at t22
    with flash
    "{th}¡Ha golpeado a Ryu con esa fusta que lleva!"

    show fex 3_0 at f21
    fex "¡Ni me has esperado! ¡EL DOLOOOR...!"

    hide ryu
    hide fex
    with dissolve

    $ inv_name = "inv_c0_welcome"
    $ talk = {
        "ryu": "Ryu Itsuki",
        "luc": "Chico del pañuelo",
        "gaelg": "Gael García",
        "danny": "Chico dormilón",
        "emiko": "Coletas"
    }
    call screen investigation(inv_name, talk)
    $ talk = {
        "ryu": "Ryu Itsuki",
        "luc": "Chico del pañuelo",
        "gaelg": "Gael García",
        "danny": "Chico dormilón",
        "emiko": "Chica de coletas"
    }

# Investigación: Ryu y Monofex
label inv_c0_welcome_luc:       # Chico del pañuelo
    show raiden 1_9 at f11
    luc "(...)"
    show raiden 0_16 at f11
    luc "¡Ja, ja, ja! {bt=a1-p10-s1}¡¡Cómo mola!!{/bt} ¡¿Cómo ha hecho eso?!" with hpunch

    hide raiden with dissolve

    python:
        if "luc" in talk:
            del talk["luc"]

    call screen investigation(inv_name, talk)

label inv_c0_welcome_gaelg:     # Gael García
    show gaelg 0_5 at f11
    gaelg "¿R-Ryu...?"
    gaelg "¿Qué... ha pasado...? ¿Cómo que «ejecución»...?"
    hide gaelg with dissolve

    python:
        if "gaelg" in talk:
            del talk["gaelg"]

    call screen investigation(inv_name, talk)

label inv_c0_welcome_ryu:       # Ryu Itsuki
    show fex 0_2 at t21
    show ryu 0_27 at t22

    fex "¿Ni un mínimo respeto a los compañeros de trabajo?\nJoder, vaya forma de empezar el juego de muerte."
    fex "¡Venga, que tienes cosas que explicar! ¡Andando!" 
    show fex 0_2 at t21

    jump game_rules

label inv_c0_welcome_emiko:     # Coletas
    show emiko 3_9 at f11
    emiko "(...)"
    hide emiko 3_9 with dissolve

    python:
        if "emiko" in talk:
            del talk["emiko"]

    call screen investigation(inv_name, talk)

label inv_c0_welcome_danny:     # Dormilón
    show danny 2_2 at f11
    danny "¿Qué ha sido esa explosión...?"
    hide danny 2_2 with dissolve

    python:
        if "danny" in talk:
            del talk["danny"]

    call screen investigation(inv_name, talk)

label inv_c0_welcome_takahiro:  # Coletas
    show takahiro 2_4 at f11
    takahiro "Me temía que ocurriera algo turbio, pero esto es pasarse..."
    hide takahiro 2_4 with dissolve

    python:
        if "takahiro" in talk:
            del talk["takahiro"]

    call screen investigation(inv_name, talk)

# Posinvestigación: Las reglas del juego
label game_rules:
    "{th}Ryu soltó un gruñido de molestia."
    
    scene cg c0_ryueye with fade
    "{th}Retiró unas pocas vendas de su rostro, dejando ver su ojo izquierdo brillante en un intenso rojo carmesí."

    ryu "Sé que estaréis sorprendidos. Incluso indignados algunos."
    ryu "Pero no me entristece comunicaros que sois los elegidos para participar en un {b}juego de matanza mutua{/b}..."
    ryu "Un juego que dirijo yo mismo, junto a mi pequeño «amiguito»."

    fex "¡¿«Pequeño»?! ¡«Pequeño», dice!"

    $ fex.name = "Monofex"
    ryu "Os presento a {b}Monofex{/b}, quien realmente será el encargado de supervisar vuestros movimientos."
    ryu "Yo me limitaré a mover los hilos desde detrás."

    fex "¡Pues venga, quita de en medio!"
    scene cg c0_monofexintro with flash
    play sound feed1
    fex "¡ESCUCHADME, RECLUTAS!" with hpunch
    fex "Estáis en las instalaciones privadas Sonyu y formáis parte del juego de matanza del grupo Alfa."
    fex "¡ABRID BIEN LAS OREJAS, PORQUE OS VOY A EXPLICAR QUÉ SIGNIFICA ESO!"
    fex "Os vais a matar {w=0.5}los unos a los otros {w=0.5}a menos que queráis acabar como la chica cohete de hace un momento." with flash

    scene bg entrance with fade
    show ryu 0_38 at t22
    show fex 0_0 at t21

    show ryu 0_38 at f22
    ryu "En efecto...\nEl juego funcionará de manera sencilla."
    ryu "Nadie puede escapar ni salir de aquí, a menos..."
    show ryu 0_37 at f22
    ryu "que {b}asesine{/b} a uno de sus {bt=a1-p10-s1}preciados{/bt} compañeros." with flash

    show ryu 0_37 at t22
    "{th}Ryu sacó del bolsillo el amuleto que Gael le había dado minutos antes..."

    play sound stomp
    scene cg c0_charmstomp with vpunch
    pause 1.0
    ryu "Vuestros vínculos de pacotilla no os servirán de nada aquí."
    ryu "{b}Cualquiera{/b} puede aprovechar esa bonita confianza que habéis construido para traicionaros y escapar." with flash

    scene bg entrance with fade
    show ryu 0_37 at t22
    show fex 1_1 at t21

    show fex 1_1 at f21
    fex "¡Y ni se os ocurra intentar escapar por la fuerza! Ya habéis visto lo que le pasó a vuestra amiguita."

    show fex 1_1 at t21
    show ryu 0_37 at f22
    ryu "Todos aquí tenéis un {b}microchip{/b} que os hemos incrustado en el cuello."
    ryu "Está colocado de tal forma que es imposible sacarlo sin provocar heridas letales."
    ryu "Si salís de los límites del recinto, {nw}"
    extend "morís.\n{nw}" with flash
    extend "Si me atacáis, {nw}"
    extend "morís.\n{nw}" with flash
    extend "Si Monofex lo dice, {nw}"
    extend "morís." with flash
    show ryu 0_38 at f22
    ryu "No os lo toméis como algo personal. Yo no os voy a molestar, así que haced como si no estuviera por aquí."
    ryu "Si os asalta cualquier duda, dirigídsela a Monofex."

    show ryu 0_38 at t22
    show fex 1_6 at f21
    fex "¡Así es! Ya está todo explicado, ¡rompan fil{nw}...!"

    stop music
    fer "Tsk, tsk... Aún no hemos terminado." with flash

    scene cg c0_ferintro with fade
    fer "He visto tu espectáculo. Mucha sangre, te ha quedado de lujo."

    ryu "(...)"
    ryu "No podía librarme de vosotros tan fácil, ¿eh?"
    
    fer "El olor a mierda que desprendes deja un rastro fácil de seguir,{w=0.1}{nw}"
    show cg c0_fercloseup
    extend "\n{b}Ryu Itsuki{/b}." with flash
    fer "Tengo que hablar contigo."

    ryu "Bah."
    ryu "De acuerdo.\nMonofex, llévate a los prisioneros hasta los dormitorios."

    play sound footsteps
    scene bg entrance with fade
    queue sound feed1
    pause 0.6

    ryu "¡P-PERO SERÁS ANIMAL! ¡SUÉLTAME, PEDAZO DE...!" with hpunch

    fer "Anda, no seas llorica, mente maestra de pacotilla."

    "{th}El hombre salido de la nada se llevó a Ryu a rastras, agarrándolo bien fuerte del brazo."

    show fex 2_1 at t11
    fex "(...)"
    show fex 2_2 at f11
    fex "B-bueno, pues... hay un dormitorio para cada uno.\nPodéis elegir el que queráis... yo os... guiaré."
    hide fex with dissolve

    "{th}Aún estoy temblando un poco..."
    "{th}Ha sido todo tan rápido... y tan extraño..."
    "{th}¿No podemos salir a menos que matemos a alguien, igual que ha hecho Ryu con Sevony?"
    "{th}Mientras intentaba organizar mis pensamientos, por fin se rompió el silencio."

    show gaelg 0_0 at t22
    show raiden 1_6 at f21
    luc "Oye, Gael. Siento mucho lo que ha pasado, parecía que os llevabais bastante bien."

    show gaelg 0_1 at f22
    show raiden 1_6 at t21
    gaelg "Intento hacer amigos... y resulta que uno está loco y la otra acaba muerta..."

    show gaelg 0_0 at t22
    show raiden 1_8 at f21
    luc "Sí, vaya tino.\nAnda, sigamos al zorro y veamos los dormitorios."

    play sound footsteps
    hide gaelg
    hide raiden
    with dissolve

    show guppy 0_0 at f21
    show emiko 0_8 at t22
    guppy "Tú. Sígueme."
    
    show emiko 0_6 at f22
    show guppy 0_0 at t21
    emiko "¿Eh, yo...?"

    show emiko 0_6 at t22
    show guppy 0_2 at f21
    guppy "Sí. Sigamos al zorro."

    show emiko 0_5 at f22
    show guppy 0_2 at t21
    emiko "Ah, ¡v-vale!"

    play sound footsteps
    hide guppy
    hide emiko
    with dissolve

    "{th}Empezó a formarse una peregrinación a los dormitorios liderada por Monofex a la que yo acabé uniéndome también."
    "{th}Y, sin que lo hubiera terminado de procesar, este fue el pistoletazo de salida de un juego..."
    "{th}donde los compañeros son la llave a la victoria, pero la confianza tiene valor nulo." with flash

    jump void_c0_1

    return
