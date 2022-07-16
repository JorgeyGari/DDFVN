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


    "FIN"
    return

label inv_c1_akaneroom_bed:


    "FIN"
    return

label inv_c1_akaneroom_desk:


    "FIN"
    return