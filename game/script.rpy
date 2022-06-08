# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.

label start:

    "{color=#009900}¡Alerta! ¡Alerta!{/color}"

    scene cg pr_breaking with fade

    "{color=#009900}¡Caos en la ciudad! En las últimas 24 horas se ha desatado una gran cantidad de incidentes en la zona este, oeste y centro de la ciudad de Gekkou.{/color}"
    "{color=#009900}La intensidad de estos ataques va aumentando con el paso de las horas, se recomienda...{/color}"

    show cg pr_static

    "{color=#009900}(...){/color}"

    scene black with fade

    $ renpy.movie_cutscene("movie/pr_title.webm")


label camión:
    scene black

    "{color=#8888ff}(...){/color}"

    return
