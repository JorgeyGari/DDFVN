init python:
    def beepy_voice(event, interact=True, **kwargs): # Para que suenen los pitidos mientras habla un personaje
    # TODO: Descubrir cómo pasar un argumento para que cada personaje tenga su propio sonido
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("audio/talk2.ogg", loop=True)
        elif event == "slow_done":
            renpy.sound.stop(fadeout = 0.5)

# Definición de personajes
define ryu = Character('Rubio', color = '#aa3333', callback = beepy_voice)
define gaelg = Character('Chamán', color = '#ae5323', callback = beepy_voice)
define sevony = Character('Gafas', color = '#946894', callback = beepy_voice)
define jaeke = Character('Antipático', color = '#696969', callback = beepy_voice)
define takahiro = Character('Llamativo', color = '#9a7818', callback = beepy_voice)
define akane = Character('Yo', color = '#13a28f', callback = beepy_voice)
define umi = Character('Marinera', color = '#185a9a', callback = beepy_voice)
define emiko = Character('Coletas', color = '#d86d9e', callback = beepy_voice)
define luc = Character('Pañuelo', color = '#5a49b4', callback = beepy_voice)
define axiom = Character('Mascarilla', color = '#a2135c', callback = beepy_voice)
define danny = Character('Dormilón', color = '#66b103', callback = beepy_voice)

# Inicio del juego
label start:

    play sound "audio/tv_on.ogg"
    pause(2)
    play music "audio/breaking.ogg"

    "{color=#090}¡Alerta! ¡Alerta!\n¡Caos en la ciudad!{/color}"

    scene cg c0_breaking with fade

    "{color=#090}En las últimas 24 horas se ha desatado una gran cantidad de incidentes en el este, oeste y centro de la ciudad de Gekkou.{/color}"
    "{color=#090}La intensidad de estos ataques va aumentando con el paso de las horas, se recomienda...{/color}"

    stop music fadeout 0.3
    play sound "audio/tv_static.ogg" fadein 0.5
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

    # Elementos a investigar
    $ inv_name = "inv_c0_truck"
    $ talk = {"ryu": "Chico rubio", "jaeke": "Chico antipático"}
    call screen investigation(inv_name, talk)
    $ talk = {"ryu": "Chico rubio", "jaeke": "Chico antipático"}    # Lo definimos dos veces para que el usuario pueda volver atrás y sus opciones sean restauradas

# Investigación: Camión
label inv_c0_truck_ryu: # Chico rubio
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
    pause(0.2)
    show ryu surprise at t32
    show sevony stand at t33
    pause(0.5)
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

label inv_c0_truck_jaeke: # Chico antipático

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
    pause(0.5)
    show jaeke annoyed at f21
    jaeke "Los comediantes como tú solo les hacen gracia a los pringados de la cárcel."
    jaeke "Mejor haz algo productivo, porque no tienes ninguna gracia, fracasado."
    show jaeke annoyed at t21

    "{color=#8cf}Vaya humos se gasta..."

    play sound "audio/truck_bump.ogg"
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

# Posinvestigación
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
    play sound "audio/truck_bump.ogg"
    with vpunch
    "{color=#090}¡Pam!"

    hide raiden
    hide emiko
    hide umi
    with dissolve
    play sound "audio/truck_bump.ogg" volume 0.6 fadeout 0.3
    with vpunch
    play sound "audio/truck_bump2.ogg" volume 1.0 fadein 0.1 fadeout 0.3
    with vpunch
    play sound "audio/truck_bump.ogg" volume 1.0 fadein 0.1 fadeout 0.3
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
    play music "audio/truck_speed.ogg" fadein 1.0 fadeout 0.5
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
    pause(0.3)
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

    play sound "audio/truck_door.ogg"
    pause(2)
    scene bg truck_light with dissolve
    "{color=#8cf}Y entonces, la puerta se abrió."

    show raiden hurt at hf11 with vpunch
    luc "¡AAH, LA LUZ! ¡Mis ojos!"

    show raiden hurt at t11
    akane "¿Estás bie...?{nw}"
    play sound "audio/sfx-stab2.wav"
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
    play sound "audio/footsteps.ogg"
    hide takahiro with dissolve

    hide raiden with dissolve
    hide danny with dissolve
    "{color=#8cf}Uno a uno, los demás siguieron al chico y fueron saliendo del camión."

    show guppy sleep at s11
    pause(1)
    "{color=#8cf}¿Debería despertarla...?"
    show guppy sleepy at t11
    "{color=#8cf}¡Ah! Acaba de despertarse. Pobre niña, parece confusa..."

    play sound "audio/footsteps.ogg"
    hide guppy with dissolve

    pause(1)
    "{color=#8cf}(...)\nBueno, pues ahora sí que estamos todos."
    "{color=#8cf}Seguí a los demás..."

    "FIN"
    return

