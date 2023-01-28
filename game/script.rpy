# Color del pensamiento: azul #8cf
# Color del sistema: verde #090

init -1 python:
    # Inventario
    import renpy.store as store
    import renpy.exports as renpy # we need this so Ren'Py properly handles rollback with classes
    from operator import attrgetter # we need this for sorting items

    inv_page = 0 # initial page of teh inventory screen
    item = None
    class Player(renpy.store.object):
        def __init__(self, name, max_hp=0, max_mp=0, element=None):
            self.name=name
            self.max_hp=max_hp
            self.hp=max_hp
            self.max_mp=max_mp
            self.mp=max_mp
            self.element=element
    player = Player("Derp", 100, 50)
    
    class Item(store.object):
        def __init__(self, name, player=None, hp=0, mp=0, element="", image="", cost=0):
            self.name = name
            self.player=player # which character can use this item?
            self.hp = hp # does this item restore hp?
            self.mp = mp # does this item restore mp?
            self.element=element # does this item change elemental damage?
            self.image=image # image file to use for this item
            self.cost=cost # how much does it cost in shops?
        def use(self): #here we define what should happen when we use the item
            if self.hp>0: #healing item
                player.hp = player.hp+self.hp
                if player.hp > player.max_hp: # can't heal beyond max HP
                    player.hp = player.max_hp
                inventory.drop(self) # consumable item - drop after use
            elif self.mp>0: #mp restore item
                player.mp = player.mp+self.mp
                if player.mp > player.max_mp: # can't increase MP beyond max MP
                    player.mp = player.max_mp
                inventory.drop(self) # consumable item - drop after use
            else:
                player.element=self.element #item to change elemental damage; we don't drop it, since it's not a consumable item

    class Inventory(store.object):
        def __init__(self, money=10):
            self.money = money
            self.items = []
        def add(self, item): # a simple method that adds an item; we could also add conditions here (like check if there is space in the inventory)
            self.items.append(item)
        def drop(self, item):
            self.items.remove(item)
        def buy(self, item):
            if self.money >= item.cost:
                self.items.append(item)
                self.money -= item.cost

    def item_use():
        item.use()

    #Tooltips:
    style.tips_top = Style(style.default)
    #style.title.font="gui/arial.ttf"
    #style.tips_top.size=14
    style.tips_top.color="fff"
    style.tips_top.outlines=[(3, "6b7eef", 0,0)]
    #style.tips_top.kerning = 5

    style.tips_bottom = Style(style.tips_top)
    #style.tips_top.size=20
    style.tips_bottom.outlines=[(0, "6b7eef", 1, 1), (0, "6b7eef", 2, 2)]
    #style.tips_bottom.kerning = 2
    
    style.button.background=Frame("gui/frame.png",25,25)
    #style.button.yminimum=52
    #style.button.xminimum=52
    style.button_text.color="000"


    showitems = True #turn True to debug the inventory
    # def display_items_overlay():
        # if showitems:
            # inventory_show = "Money:" + str(inventory.money) + " HP: " + str(player.hp) + " bullets: " + str(player.mp) + " element: " + str(player.element) + "\nInventory: "
            # for i in range(0, len(inventory.items)):
                # item_name = inventory.items[i].name
                # if i > 0:
                    # inventory_show += ", "
                # inventory_show += item_name
            
            # ui.frame()
            # ui.text(inventory_show, color="#000")
    # config.overlay_functions.append(display_items_overlay)
  
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
            "! " : "! {w=0.25}", 
            ", " : ", {w=0.05}",
        }
        for key in str_map:
            str_to_test = str_to_test.replace( key, str_map[ key ] ) 
        return str_to_test

    def system(tag, argument):  # Etiqueta para el texto verde (sistema y narrador), {sy}
        return [(renpy.TEXT_TAG, u"color=#090")]
    config.self_closing_custom_text_tags["sy"] = system

    def thought(tag, argument): # Etiqueta para el texto azul (pensamiento), {th}
        return [(renpy.TEXT_TAG, u"color=#8cf")]
    config.self_closing_custom_text_tags["th"] = thought

    def bouncy(tag, argument):  # Etiqueta para el texto que rebota, {bo}(...){/bt}
        return [(renpy.TEXT_TAG, u"bt=a1-p10-s1")]
    config.self_closing_custom_text_tags["bo"] = bouncy

    monopad_unlocked = False

define config.say_menu_text_filter = alter_say_strings
define sel_char_prof = "none"
define profile_dict = { # Un diccionario para los perfiles de cada recluso (identificados por nombre interno), donde almacenamos su nombre completo, su talento definitivo, su género, una descripción, si siguen con vida (True/False) y sus datos personales (género, altura, cumpleaños, gustos y aversiones)
    "ryu": 
        ["Ryu Itsuki", "(?)", "Descripción", True,
        ["M", "Altura", "Cumpleaños", "Gustos", "Aversiones"]],
    "fer": 
        ["(?)", "(?)", "Descripción", True,
        ["M", "Altura", "Cumpleaños", "Gustos", "Aversiones"]],
    "sevony": 
        ["Sevony Maáz", "(?)", "Descripción", False,
        ["F", "Altura", "Cumpleaños", "Gustos", "Aversiones"]],
    "gaelg": 
        ["Gael García", "Chamán definitivo", "Descripción", True,
        ["X", "Altura", "Cumpleaños", "Gustos", "Aversiones"]],
    "jaeke": 
        ["(?)", "(?)", "Descripción", True,
        ["M", "Altura", "Cumpleaños", "Gustos", "Aversiones"]],
    "takahiro": 
        ["(?)", "(?)", "Descripción", True,
        ["M", "Altura", "Cumpleaños", "Gustos", "Aversiones"]],
    "akane": 
        ["Akane Yamamoto", "Mangaka definitiva", "Descripción", True,
        ["F", "Altura", "Cumpleaños", "Gustos", "Aversiones"]],
    "umi": 
        ["Umi Yoshinaru", "(?)", "Descripción", True,
        ["F", "Altura", "Cumpleaños", "Gustos", "Aversiones"]],
    "emiko":
        ["(?)", "(?)", "Descripción", True,
        ["F", "Altura", "Cumpleaños", "Gustos", "Aversiones"]],
    "luc":
        ["(?)", "(?)", "Descripción", True,
        ["X", "Altura", "Cumpleaños", "Gustos", "Aversiones"]],
    "axiom":
        ["(?)", "(?)", "Descripción", True,
        ["M", "Altura", "Cumpleaños", "Gustos", "Aversiones"]],
    "danny":
        ["(?)", "(?)", "Descripción", True,
        ["M", "Altura", "Cumpleaños", "Gustos", "Aversiones"]],
    "guppy":
        ["(?)", "(?)", "Descripción", True,
        ["F", "Altura", "Cumpleaños", "Gustos", "Aversiones"]],
    "ichika":
        ["(?)", "(?)", "Descripción", True,
        ["F", "Altura", "Cumpleaños", "Gustos", "Aversiones"]],
    "ghiang": 
        ["(?)", "(?)", "Descripción", True,
        ["F", "Altura", "Cumpleaños", "Gustos", "Aversiones"]],
    "gaelm":
        ["(?)", "(?)", "Descripción", True,
        ["M", "Altura", "Cumpleaños", "Gustos", "Aversiones"]],
    "none":
        ["", "", "", True,
        ["", "", "", "", ""]]
}

#region Definición de personajes
define ryu = Character('Rubio', color = '#aa3333', callback = beepy_voice_deep)
define fer = Character('(?)', color = '#702a2a', callback = beepy_voice_deep)
define sevony = Character('Gafas', color = '#946894', callback = beepy_voice_high)
define gaelg = Character('Chamán', color = '#ae5323', callback = beepy_voice_deep)
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
define gaelm = Character('Nervioso', color = '#87a0bd', callback = beepy_voice_deep)
define fex = Character('(?)', color = '#6b7d4a', callback = beepy_voice_high)

#endregion
# TODO: Incluir a Ichika, Gael M., Ghiang y Kiiro en el guion del camión del prólogo

#region Definición de música
define audio.beautiful_lament = "<loop 15.6859>audio/BSO/Beautiful Lament.ogg"
define audio.kitsune_to_tanuki = "<loop 51.128>audio/BSO/Kitsune to Tanuki no Omanuke na Bakashi Ai.ogg"
define audio.living_to_the_fullest = "<loop 60.209>audio/BSO/Living to the Fullest.ogg"
define audio.weekly_despair = "<loop 58.095>audio/BSO/Weekly Despair Magazine.ogg"
#endregion

#region Inventario
init -1:
    $ inventory = Inventory()

    transform inv_eff: # too lazy to make another version of each item, we just use ATL to make hovered items super bright
        zoom 0.5 xanchor 0.5 yanchor 0.5
        on idle:
            linear 0.2 alpha 1.0
        on hover:
            linear 0.2 alpha 2.5

    #Tooltips-inventory:
    # FIXME: Hay una versión más moderna de LiveComposite
    image info_chocolate = Text("CHOCOLATE", style="tips_top")
    image tooltip_inventory_chocolate=LiveComposite((600, 73), (3,0), ImageReference("info_chocolate"), (3,30), Text("Generic chocolate to heal\n40 points of health.", style="tips_bottom"))

    image info_banana = Text("BANANA", style="tips_top")
    image tooltip_inventory_banana=LiveComposite((665, 73), (3,0), ImageReference("info_banana"), (3,30), Text("A healthy banana full of potassium! You can also use it as ammo for your guns! O.O Recharges 20 bullets.", style="tips_bottom"))

    image info_gun = Text("GUN", style="tips_top")
    image tooltip_inventory_gun=LiveComposite((665, 73), (3,0), ImageReference("info_gun"), (3,30), Text("An gun that looks like something a cop would\ncarry around. Most effective on humans.", style="tips_bottom"))

    image info_laser = Text("LASER GUN", style="tips_top")
    image tooltip_inventory_laser=LiveComposite((665, 73), (3,0), ImageReference("info_laser"), (3,30), Text("An energy gun that shoots photon beams.\nMost effective on aliens.", style="tips_bottom"))
#endregion

label start:
    $ chapter = 0
    call ch0_intro from _call_ch0_intro

    $ chapter = 1

#region Nombres conocidos en el Prólogo
    $ akane.name = "Akane Yamamoto"
    $ umi.name = "Umi Yoshiharu"
    $ ryu.name = "Ryu Itsuki"
    $ gaelg.name = "Gael García"
    $ sevony.name = "Sevony Maáz"
    $ fex.name = "Monofex"
#endregion

    $ monopad_unlocked = False
    $ places = {
        "oppidum": ["dininghall", "gym", "kitchen", "plaza", "roomsa", "roomsb", "shack", "supermarket"]
    }

#region Galería
    init python:

        # Step 1. Create the gallery object.
        g = Gallery()

        g.button("c0_breaking")
        g.condition("persistent.c0_breaking")
        g.image("images/CGs/Prólogo/cg c0_breaking.png")
        
        g.button("c0_fercloseup")
        g.condition("persistent.c0_fercloseup")
        g.image("images/CGs/Prólogo/cg c0_fercloseup.png")

        g.button("c0_ferintro")
        g.condition("persistent.c0_ferintro")
        g.image("images/CGs/Prólogo/cg c0_ferintro.png")

        g.button("c0_fersmoke")
        g.condition("persistent.c0_fersmoke")
        g.image("images/CGs/Prólogo/cg c0_fersmoke.png")

        g.button("c0_monofexintro")
        g.condition("persistent.c0_monofexintro")
        g.image("images/CGs/Prólogo/cg c0_monofexintro.png")

        g.button("c0_ryubutton")
        g.condition("persistent.c0_ryubutton")
        g.image("images/CGs/Prólogo/cg c0_ryubutton.png")

        g.button("c0_ryueye")
        g.condition("persistent.c0_ryueye")
        g.image("images/CGs/Prólogo/cg c0_ryueye.png")

        g.button("c0_ryuvoid")
        g.condition("persistent.c0_ryuvoid")
        g.image("images/CGs/Prólogo/cg c0_ryuvoid.png")

        g.button("c0_sevonyknife")
        g.condition("persistent.c0_sevonyknife")
        g.image("images/CGs/Prólogo/cg c0_sevonyknife.png")

        g.button("c0_skyexplosion")
        g.condition("persistent.c0_skyexplosion")
        g.image("images/CGs/Prólogo/cg c0_skyexplosion.png")

    default persistent.c0_breaking = True
    default persistent.c0_fercloseup = True
    default persistent.c0_ferintro = True
    default persistent.c0_fersmoke = True
    default persistent.c0_monofexintro = True
    default persistent.c0_ryubutton = True
    default persistent.c0_ryueye = True
    default persistent.c0_ryuvoid = True
    default persistent.c0_sevonyknife = True
    default persistent.c0_skyexplosion = True
    
#endregion

    call ch1_intro from _call_ch1_intro
