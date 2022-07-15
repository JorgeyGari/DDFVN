# Prólogo
label void_c0_1:
    scene black with fade
    ryu "¿Conque esas son tus condiciones, Fer?"
    ryu "Tsk. No me queda otra que aceptar." with flash
    
    fer "Quéjate todo lo que quieras ahora.\nTe doy unos segundos."

    "{color=#090}Fer tomó una calada del cigarro."

    ryu "Oye, mamón, no te pido nada, pero un mínimo respeto estaría bien, ¿no? Te recuerdo que ahora somos comp{nw}..."

    show cg c0_fersmoke
    "{color=#090}Y exhaló." with flash

    fer "Ya está, se acabó tu tiempo."

    scene black with fade
    pause 2.0
    
    "{color=#090}Más tarde, en la misma noche..."

    scene cg c0_ryuvoid with fade
    ryu "(...)"
    ryu "¿Eh? ¿Hablas de {b}ellos{/b}? Sí, nadie parece haber notado nada raro."
    ryu "Están haciendo un excelente trabajo, y eso que no son muchos."
    ryu "(...)"
    ryu "Os mantendré informados."

    scene black with fade
    stop sound fadeout 1.5

    $ renpy.movie_cutscene("movie/pr_end.webm")
    
    # Fin del Prólogo
    return
