# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.

label start:

    "{color=#090}¡Alerta! ¡Alerta!{/color}"

    scene cg pr_breaking with fade

    "{color=#090}¡Caos en la ciudad! En las últimas 24 horas se ha desatado una gran cantidad de incidentes en la zona este, oeste y centro de la ciudad de Gekkou.{/color}"
    "{color=#090}La intensidad de estos ataques va aumentando con el paso de las horas, se recomienda...{/color}"

    show cg pr_static

    "{color=#090}(...){/color}"

    scene black with fade

    $ renpy.movie_cutscene("movie/pr_title.webm")

label camión:
    scene black

    "{color=#8af}(...){/color}"

    show bg truck with fade

    "{color=#8af}Cuando me desperté, todo estaba oscuro.{/color}"
    "{color=#8af}Me encontraba en lo que parecía ser un camión de transporte.{/color}"
    "{color=#8af}Podía escuchar las ruedas del vehículo y, a mi alrededor, pude distinguir a más gente despertar como yo.{/color}"

    show ryu concern with dissolve   
    "{color=#8af}Un chico de pelo claro permanecía sentado, abrazado a sus piernas, en silencio al fondo del camión.{/color}"
    "{color=#8af}Lo oí soltar un respiro de angustia justo antes de hundir la cabeza entre las piernas."
    hide ryu with dissolve

    show sevony concern with dissolve
    "{color=#8af}También había una chica con gafas que inhaló y espiró en un claro intento de tranquilizarse."
    "{color=#8af}Echó una mirada a su alrededor, justo antes de..."

    show sevony surprise
    "{color=#090}¡Pam!"

    "{color=#8af}Un bache en el camino despertó a casi todos los que seguían dormidos..."

    "{color=#8af}Las gafas de la chica salieron despedidas."

    "{color=#8af}Ahora que hay más gente despierta, tal vez debería fijarme en quiénes son mis compañeros de viaje..."

    "FIN"
    return
