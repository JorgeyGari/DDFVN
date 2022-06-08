# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.

label start:

    "{color=#090}¡Alerta! ¡Alerta!\n¡Caos en la ciudad!{/color}"

    scene cg pr_breaking with fade

    "{color=#090}En las últimas 24 horas se ha desatado una gran cantidad de incidentes en el este, oeste y centro de la ciudad de Gekkou.{/color}"
    "{color=#090}La intensidad de estos ataques va aumentando con el paso de las horas, se recomienda...{/color}"

    show cg pr_static

    "{color=#090}(...){/color}"

    scene black with fade

    $ renpy.movie_cutscene("movie/pr_title.webm")

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
    "{color=#8cf}Las gafas de la chica salieron despedidas."
    "{color=#8cf}Ahora que hay más gente despierta, tal vez debería fijarme en quiénes son mis compañeros de viaje..."

    "{color=#090}Haz clic en el icono del personaje en quien te quieras fijar."

    # Elementos a investigar
    $ inv = ["jaeke", "ryu"]

    call screen inv_pr_truck

label inv_pr_truck_ryu:
    "hola jaja"

    $ inv.remove("ryu")
    if not inv:
        jump inv_pr_truck_end
    else:
        call screen inv_pr_truck

label inv_pr_truck_jaeke:
    "hola"
    
    $ inv.remove("jaeke")
    if not inv:
        jump inv_pr_truck_end
    else:
        call screen inv_pr_truck

label inv_pr_truck_end:
    "FIN"
    return

screen inv_pr_truck:

    imagebutton:    # Icono de Ryu
        xpos 0
        ypos 0
        auto "icon/ryu_%s.png"
        action [Hide("displayTextScreen"), Jump("inv_pr_truck_ryu")]

        hovered Show("displayTextScreen", displayText = "Hablar con el chico rubio")
        unhovered Hide("displayTextScreen")

    imagebutton:    # Icono de Jaeke
        xpos 0
        ypos 120
        auto "icon/jaeke_%s.png"
        action [Hide("displayTextScreen"), Jump("inv_pr_truck_jaeke")]

        hovered Show("displayTextScreen", displayText = "Hablar con el chico antipático")
        unhovered Hide("displayTextScreen")