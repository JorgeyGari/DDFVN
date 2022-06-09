# Definición de personajes
define ryu = Character('Ryu Itsuki', color = '#a33')
define gaelg = Character('Gael García', color = '#f8882d')
define sevony = Character('Sevony', color = '#9c3e9c')

# Inicio del juego
label start:

    "{color=#090}¡Alerta! ¡Alerta!\n¡Caos en la ciudad!{/color}"

    scene cg pr_breaking with fade

    "{color=#090}En las últimas 24 horas se ha desatado una gran cantidad de incidentes en el este, oeste y centro de la ciudad de Gekkou.{/color}"
    "{color=#090}La intensidad de estos ataques va aumentando con el paso de las horas, se recomienda...{/color}"

    show cg pr_static

    "{color=#090}(...){/color}"

    scene black with fade

    $ renpy.movie_cutscene("movie/pr_title.webm")

# Despertar en el camión
label truck:

    show bg truck with fade

    "{color=#8cf}Cuando me desperté, todo estaba oscuro.{/color}"
    "{color=#8cf}Me encontraba en lo que parecía ser un camión de transporte.{/color}"
    "{color=#8cf}Podía escuchar las ruedas del vehículo y, a mi alrededor, pude distinguir a más gente despertar como yo.{/color}"

    show ryu concern with dissolve   
    "{color=#8cf}Un chico de pelo claro permanecía sentado, abrazado a sus piernas, en silencio al fondo del camión.{/color}"
    "{color=#8cf}Lo oí soltar un respiro de angustia justo antes de hundir la cabeza entre las piernas."
    hide ryu with dissolve

    show sevony concern with dissolve
    "{color=#8cf}También había una chica con gafas que inhaló y espiró en un claro intento de tranquilizarse."
    "{color=#8cf}Echó una mirada a su alrededor, justo antes de..."

    show sevony surprise
    "{color=#090}¡Pam!"

    "{color=#8cf}Un bache en el camino despertó a casi todos los que seguían dormidos..."
    "{color=#8cf}Ahora que hay más gente despierta, tal vez debería fijarme en quiénes son mis compañeros de viaje..."

    hide sevony with dissolve

    "{color=#090}Haz clic en el icono del personaje en quien te quieras fijar."

    # Elementos a investigar
    $ inv = ["jaeke", "ryu"]

    call screen inv_pr_truck

# Investigación: Camión
label inv_pr_truck_ryu: # Chico rubio

    "{color=#8cf}Las gafas de la chica de pelo violeta habían salido despedidas por culpa del bache."

    show ryu stand at left with dissolve

    "{color=#8cf}El rubio se agachó al oírlas caer. Habían aterrizado cerca de él."
    show sevony surprise at right with dissolve
    "{color=#8cf}Gateó un poco hasta alcanzarlas y se las acercó a su dueña, con una cálida sonrisa."

    show ryu smile at left
    "Rubio" "Toma, ve con cuidado... Sería una pena que se te rompieran."

    "{color=#8cf}Lo dijo flojito, como si no quisiera llamar demasiado la atención en un ambiente tan tenso."

    show sevony smile at right
    "Gafas" "(...)\nMuchas gracias."
    show sevony concern at right
    "Gafas" "Vaya carretera en la que nos han metido."

    show ryu stand at left
    "Rubio" "Pues... sí, la verdad."

    hide sevony with dissolve
    hide ryu with dissolve

    show gaelg stand with dissolve
    "{color=#8cf}Un chico que parecía nervioso y confundido observaba la conversación."
    "{color=#8cf}Los miraba mientras murmuraba para sí mismo."

    "Mi chamanismo me sacará de esta.\nEscaparé de aquí."

    "{color=#8cf}Finalmente, consiguió reunir valor para hablarle a los presentes en lugar de al cuello de la camisa."

    "Chamán" "Hum... ¿C-cómo te llamas?"
    hide gaelg with dissolve

    show ryu surprise with dissolve
    "Rubio" "¿Y-yo? V-vaya por dios."
    show ryu stand
    ryu "Mi nombre... es Ryu Itsuki.\nSoy un simple desempleado."
    ryu "¿Y vosotros, chica de las gafas, chico moreno?"
    hide ryu with dissolve

    show sevony stand at right with dissolve
    show gaelg stand at left with dissolve

    sevony "Un gusto, Itsuki-kun. Mi nombre es Sevony."

    "Gabriel" "A-ah... yo soy... Gabriel..."

    "{color=#8cf}Gabriel se quedó bloqueado por un momento."

    show gaelg surprise at left
    gaelg "¡QUIERO DECIR! Gael. Gael García, a tu servicio."

    "{color=#8cf}¿En serio se le ha olvidado su propio nombre?"
    hide gaelg with dissolve

    show ryu stand at left with dissolve
    "Sevony y Gael... Tenéis nombres exóticos, son bonitos."

    "{color=#8cf}La expresión de Ryu se había apagado."

    ryu "Sevony... Me recuerdas a alguien, ¿sabes? Aunque tal vez solo sea mi imaginación."

    sevony "Más que seguro, su imaginación. Mucha gente pasa por la ciudad."

    "{color=#8cf}Sevony ha contestado muy rápido..."

    show ryu think at left
    ryu "Hum... Seguramente sea eso."
    ryu "He conocido a mucha gente a lo largo de mi vida, no sería la primera vez que me ocurre."

    hide sevony with dissolve
    show gaelg happy at right with dissolve
    gaelg "Ryu... ¿Igual que «dragón» en japonés? ¡Mola!"
    show gaelg stand at right
    gaelg "Y usted, señorita Sevony, ¿de dónde es?"

    hide ryu with dissolve
    show sevony smile at left with dissolve
    sevony "Soy de Gekkou, una ciudad un poco al norte de aquí."

    "{color=#8cf}Su sonrisa amable contrastaba con el tono frío, seguramente involuntario, de su voz."

    show gaelg happy at right
    gaelg "O sea que sois japoneses... ¡Entonces... podré aprender mucho de otras culturas!"
    gaelg "Hoy es una victoria para el {b}chamán definitivo{/b}."

    hide sevony with dissolve
    show ryu surprise at left with dissolve
    "{color=#8cf}Al oír el talento definitivo de Gael, Ryu lo miró con mucho interés."

    ryu "Chamán... Qué interesante."

    "{color=#8cf}¿Será este el inicio de una agradable amistad?"

    "{color=#090}¡Pam!"

    "{color=#8cf}¡¿Otro bache?!"

    hide ryu with dissolve
    hide gaelg with dissolve

    python:
        if "ryu" in inv:
            inv.remove("ryu")

    if not inv:
        jump truck_end
    else:
        call screen inv_pr_truck

label inv_pr_truck_jaeke: # Chico antipático

    show jaeke stand at left with dissolve
    show takahiro stand at right with dissolve

    "{color=#8cf}En una esquina del vehículo se encontraba un chico con cara de pocos amigos."
    "{color=#8cf}Otro muchacho con ropa llamativa se le acercó."

    show takahiro ask at right
    "Llamativo" "Eh, ¿y tú eres...?"

    show jaeke annoyed at left
    "{color=#8cf}El moreno le devolvió una fría mirada y no medió palabra."

    "Llamativo" "Ya veo que eres alguien con quien es fácil hablar..."

    "{color=#8cf}Nada más oír eso, el mudo se levantó, se le acercó y empezó a susurrar."

    "Antipático" "Ten cuidado conmigo, chaval.\nNo sabes con quién estás hablando."

    show takahiro laugh
    "Llamativo" "Pues claro que no sé con quién estoy hablando, ni siquiera me has dicho tu nombre."

    "Antipático" "Los comediantes como tú solo le hacen gracia a los pringados de la cárcel."
    "Antipático" "Mejor haz algo productivo, porque no tienes ninguna gracia, fracasado."

    "{color=#8cf}Vaya humos se gasta..."

    "{color=#090}¡Pam!"

    hide jaeke with dissolve
    hide takahiro with dissolve

    python:
        if "jaeke" in inv:
            inv.remove("jaeke")

    if not inv:
        jump truck_end
    else:
        call screen inv_pr_truck

# Posinvestigación
label truck_end:
    
    "{color=#8cf}Creo que ya he escuchado suficiente...\nNo parece que nadie sepa cómo hemos llegado hasta aquí."
    "{color=#8cf}¿Cómo ha podido pasar esto?\n¿Habré hecho algo para acabar aquí...?"

    "Yo" "Esto... ¿Alguien sabe dónde estamos?"

    show umi stand with dissolve
    "{color=#8cf}Una chica muy guapa vestida con un gorro de marinero me dirigió la mirada al oírme."

    "Marinera" "No lo sé, pero es un vehículo en movimiento, así que tampoco tiene sentido preguntarse eso hasta que lleguemos."
    "Marinera" "Lo mejor será mantener la calma."

    "Yo" "Supongo que tienes razón, pero quería preguntar por si alguien lo sabía..."

    hide umi with dissolve
    show emiko ask with dissolve
    "Coletas" "¿Eh? Espera... ¿entonces de verdad nadie sabe hacia dónde vamos o siquiera dónde estamos?"

    hide emiko with dissolve
    show raiden annoyed with dissolve
    "Pañuelo" "Si lo supiéramos, ya habría contestado alguien, ¿no?\nA menos que se lo quiera callar."
    show raiden laugh
    "Pañuelo" "Imaginaos que nos han secuestrado o algo y pretenden deshacerse de nosotros, ¡ja, ja!"

    "Yo" "¡¿Secuestrarnos?! ¡¿Y qué se supone que hemos hecho para que nos metan en una situación así?!"

    "Pañuelo" "Vamos, solo era una broma."
    "Pañuelo" "Yo, al menos, no he hecho nada malo. Los demás, no sé."

    show raiden surprise
    "{color=#090}¡Pam!"

    hide raiden with dissolve
    "{color=#090}¡Pum, pum, pam, pom!"
    
    "{color=#8cf}Por culpa de todos esos baches, me golpeé la cabeza con el techo del vehículo."

    show umi concern with dissolve
    "Marinera" "¿Te encuentras bien?"

    "Yo" "S-sí... P-por cierto, ¿cómo te lla...?"

    "{color=#8cf}Pero no pude acabar de formular mi pregunta."
    hide umi with dissolve
    "{color=#8cf}El vehículo comenzó a serpentear, arrojándonos a mí y a los demás pasajeros de un lado a otro."
    "{color=#8cf}Cada vez más rápido, vi que algunos se sostenían a sus asientos como podían, yo me vi forzada a hacer lo mismo..."
    "{color=#8cf}Hasta que, al fin, paró."
    "{color=#8cf}Yo había acabado en el suelo, pero no era la única..."

    "FIN"
    return

screen inv_pr_truck:

    imagebutton:    # Icono de Ryu
        xpos 0
        ypos 0
        auto "icon/ryu_%s.png"
        action [Hide("displayTextScreen"), Jump("inv_pr_truck_ryu")]

        hovered Show("displayTextScreen", displayText = "Chico rubio")
        unhovered Hide("displayTextScreen")

    imagebutton:    # Icono de Jaeke
        xpos 0
        ypos 120
        auto "icon/jaeke_%s.png"
        action [Hide("displayTextScreen"), Jump("inv_pr_truck_jaeke")]

        hovered Show("displayTextScreen", displayText = "Chico antipático")
        unhovered Hide("displayTextScreen")