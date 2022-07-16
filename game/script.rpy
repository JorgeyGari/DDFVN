# Color del pensamiento: azul #8cf
# Color del sistema: verde #090

init python:
    def beepy_voice_deep(event, interact=True, **kwargs): # Para que suenen los pitidos mientras habla un personaje
    # TODO: Descubrir cómo pasar un argumento para que cada personaje tenga su propio sonido
        if not interact:
            return

        if event == "show_done":
            beep = []
            for x in range(1,10):
                beep.append(random.choice(["audio/talk2.ogg", "audio/talk3.ogg"]))  # Construimos una lista de sonidos agudos y graves aleatorios
            renpy.sound.play(beep, loop = True)
        elif event == "slow_done":
            renpy.sound.stop(fadeout = 0.5)
    # FIXME: Los pitidos deberían tener un canal propio para que puedan sonar a la vez que los efectos de sonido

    def beepy_voice_high(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            beep = []
            for x in range(1,10):
                beep.append(random.choice(["audio/talk1.ogg", "audio/talk2.ogg"]))
            renpy.sound.play(beep, loop = True)
        elif event == "slow_done":
            renpy.sound.stop(fadeout = 0.5)

    def alter_say_strings(str_to_test): # Pausas automáticas en el texto con cada signo de puntuación
        str_map = {
            ". " : ". {w=0.25}", 
            "? " : "? {w=0.25}",
            "(...)\n" : "(...)\n{w=0.25}",
            "\n" : "\n{w=0.25}", 
            "(...)" : "(...){w=0.25}",
            "! " : "! {w=0.25}", 
            ", " : ", {w=0.05}",
        }
        for key in str_map:
            str_to_test = str_to_test.replace( key, str_map[ key ] ) 
        return str_to_test

define config.say_menu_text_filter = alter_say_strings
default mtt = MouseTooltip(Text(""), padding={"x": 10, "y": -10})

#region Definición de personajes
define ryu = Character('Rubio', color = '#aa3333', callback = beepy_voice_deep)
define gaelg = Character('Chamán', color = '#ae5323', callback = beepy_voice_deep)
define sevony = Character('Gafas', color = '#946894', callback = beepy_voice_high)
define jaeke = Character('Antipático', color = '#696969', callback = beepy_voice_deep)
define takahiro = Character('Llamativo', color = '#9a7818', callback = beepy_voice_deep)
define akane = Character('Yo', color = '#13a28f', callback = beepy_voice_high)
define umi = Character('Marinera', color = '#185a9a', callback = beepy_voice_high)
define emiko = Character('Coletas', color = '#d86d9e', callback = beepy_voice_high)
define luc = Character('Pañuelo', color = '#5a49b4', callback = beepy_voice_deep)
define axiom = Character('Mascarilla', color = '#a2135c', callback = beepy_voice_deep)
define danny = Character('Dormilón', color = '#66b103', callback = beepy_voice_deep)
define guppy = Character('Niña pez', color = '#ff8b3d', callback = beepy_voice_high)
define ichika = Character('Elegante', color = '#2ece49', callback = beepy_voice_high)
define ghiang = Character('Moños', color = '#1398a2', callback = beepy_voice_high)
define fex = Character('(?)', color = '#6b7d4a', callback = beepy_voice_high)
define gaelm = Character('Nervioso', color = '#87a0bd', callback = beepy_voice_deep)
define fer = Character('(?)', color = '#702a2a', callback = beepy_voice_deep)
#endregion
# TODO: Incluir a Ichika, Gael M., Ghiang y Kiiro en el guion

#region Definición de música
define audio.beautiful_lament = "<loop 15.6859>audio/BSO/Beautiful Lament.ogg"
define audio.kitsune_to_tanuki = "<loop 51.128>audio/BSO/Kitsune to Tanuki no Omanuke na Bakashi Ai.ogg"
define audio.living_to_the_fullest = "<loop 60.209>audio/BSO/Living to the Fullest.ogg"
define audio.weekly_despair = "<loop 58.095>audio/BSO/Weekly Despair Magazine.ogg"
#endregion

label start:
    $ chapter = 0
    call ch0_intro