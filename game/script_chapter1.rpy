label ch1_intro:
    $ sector = "oppidum"
    $ place = "roomsb"
    $ name = "Dormitorios"

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
    show cg c1_monopad_alarm with fade
    akane "¿Este trasto es lo que está haciendo tanto ruido?"
    jump inv_c1_akaneroom_end

label inv_c1_akaneroom_bed:
    "{th}El día fue tan cansado que acabé desplomándome en la cama anoche."
    "{th}Y eso que habían sucedido muchas cosas en las que podía haberme quedado pensando pasando la noche en vela."
    call screen investigation(inv_name, talk, obj, "akaneroom")

label inv_c1_akaneroom_desk:
    "{th}Un escritorio de madera..."
    "{th}¿Qué es eso que hay {b}encima{/b} de él...?" with flash
    call screen investigation(inv_name, talk, obj, "akaneroom")

label inv_c1_akaneroom_end:
    stop music
    "{th}Apagué la alarma."
    "{th}Es... ¿un teléfono?"
    hide cg c1_monopad_alarm with fade
    "{th}¿Lo habrán dejado para mí?"

    show fex 0_10 at hf11
    fex "¡Felicidades, recluta Akane!"
    play sound feed1
    with flash
    with vpunch
    show fex 0_10 at t11
    akane "¡AAAH!"
    show fex 0_11 at f11
    fex "¡Eres la orgullosa poseedora de un Monopad de último modelo!"
    show fex 1_5
    fex "Este dispositivo tiene todas las herramientas necesarias para tu estancia en las instalaciones Sonyu."
    show fex 1_6
    fex "Pero esto no es un regalo. ¡No, no, no!"
    fex "El que algo quiere, algo le cuesta."
    fex "El Monopad contiene una aplicación que te permite ver información de tus compañeros."
    fex "Sin embargo, no tendrá estos datos hasta que no hayas conocido a cada uno de ellos."
    show fex 1_7
    fex "¡Así que no te olvides de hablar con ellos!"
    show fex 1_8
    fex "Es una orden."
    hide fex with dissolve

    "{th}Y tal como vino, se fue..."
    $ monopad_unlocked = True
    
    python:
        player = Player("Derp", 100, 50)
        player.hp = 50
        player.mp = 10
        chocolate = Item("Chocolate", hp=40, image="gui/inv_chocolate.png")
        banana = Item("Banana", mp=20, image="gui/inv_banana.png")    
        gun = Item("Gun", element="bullets", image="gui/inv_gun.png", cost=7)
        laser = Item("Laser Gun", element="laser", image="gui/inv_laser.png")
        inventory = Inventory()
        #add items to the initial inventory:
        inventory.add(chocolate)
        inventory.add(chocolate)
        inventory.add(banana)
        
    $ inventory.add(laser)
    "{sy}Has recibido un Monopad. Puedes acceder a él mediante la barra de menú inferior."
