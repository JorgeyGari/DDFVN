label ch1_intro:
    scene black with fade
    play music alarm_clock
    pause 2.0
    "{color=#8cf}Agh... ¿Qué es ese ruido?"

    show bg akaneroom with fade
    
    $ inv_name = "inv_c1_akaneroom"
    $ talk = {}
    $ obj = {
        "bed": (0, 0, "Cama"),
        "monopad": (0, 0, "Teléfono"),
        "desk": (0, 0, "Escritorio"),
    }
    call screen investigation(inv_name, talk, obj, "akaneroom")

label inv_c1_akaneroom_monopad:
    "{th}Sobre el escritorio de mi habitación había un dispositivo electrónico."
    akane "¿Este trasto es lo que está haciendo tanto ruido?"

    show cg c1_monopad_alarm with fade

    call screen monopad_unlock

    jump safenet

label inv_c1_akaneroom_bed:
    "{th}El día fue tan cansado que acabé desplomándome en la cama anoche."
    "{th}Y eso que habían sucedido muchas cosas en las que podía haberme quedado pensando pasando la noche en vela."
    call screen investigation(inv_name, talk, obj, "akaneroom")

label inv_c1_akaneroom_desk:
    "{th}Un escritorio de madera..."
    "{th}¿Qué es eso que hay {b}encima{/b} de él...?" with flash
    call screen investigation(inv_name, talk, obj, "akaneroom")

label safenet:
    "hola"