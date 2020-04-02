init python:

    maxnumx = 3
    maxnumy = 2
    maxthumbx = config.screen_width / (maxnumx + 5)
    maxthumby = config.screen_height / (maxnumy + 3)
    maxperpage = maxnumx * maxnumy
    gallery_page = 0
    closeup_page = 0

    looking = False

    class GalleryItem:
        def __init__(self, name, images, thumbnail, lockedthumbnail="lockedthumb"):
            self.name = name
            self.images = images
            self.thumbnail = thumbnail
            self.lockedthumbnail = lockedthumbnail
            self.refresh_lock()
        
        def num_images(self):
            return len(self.images)
        
        def refresh_lock(self):
            self.num_unlocked = 0
            lock_me = False
            for img in self.images:
                if not achievement.has("NEW_ACHIEVEMENT_1_18"):
                    if not renpy.seen_image(img):
                        lock_me = True
                else:
                    self.num_unlocked += 1
            
            
            
            self.is_locked = lock_me


    gallery_items = []









    gallery_items.append(GalleryItem("Girls Lineup",
    ["popup_lineup"],
    "popup_lineupt"))
    gallery_items.append(GalleryItem("Jason Pinned",
    ["popup_pin"],
    "popup_pint"))
    gallery_items.append(GalleryItem("Sarah Tease",
    ["popup_sarah_tease"],
    "popup_sarah_teaset"))
    gallery_items.append(GalleryItem("Kira Frustrated",
    ["popup_kira_m"],
    "popup_kira_mt"))
    gallery_items.append(GalleryItem("Noelle Maid",
    ["popup_noelle_maid"],
    "popup_noelle_maidt"))
    gallery_items.append(GalleryItem("Kira Tease",
    ["popup_kira_tease"],
    "popup_kira_teaset"))















    gallery_items.append(GalleryItem("Kira Panties",
    ["kira_panties"],
    "kira_pantiest"))
    gallery_items.append(GalleryItem("Sarah Puppy",
    ["sarah_doggy"],
    "sarah_doggyt"))
    gallery_items.append(GalleryItem("Jane Femm",
    ["jane_girly"],
    "jane_girlyt"))

    gallery_items.append(GalleryItem("Noelle Shower",
    ["nshowg1", "nshowg2", "nshowg3", "nshowg4", "nshowg5",
    "nshowg6", "nshowg7", "nshowg8", "nshowg9", "nshowg11",
    "nshowg12", "nshowg13", "nshowg14"],
    "nshowt1"))











    gallery_items.append(GalleryItem("Jane Fashion Show",

    ["jshow1", "jshow2", "jshow3", "jshow4",
     "jshow5", "jshow6", "jshow7", "jshow8", "jshow9",
     "jshow10", "jshow11", "jshow12", "jshow13",
     "jshow14", "jshow15"],

    "jshowt1"))

    gallery_items.append(GalleryItem("Kira Post Shower Tease",

    ["kshow1", "kshow2", "kshow3", "kshow4", "kshow5",
     "kshow6", "kshow7", "kshow8", "kshow9", "kshow10",
     "kshow11"],

    "kshowt1"))

    gallery_items.append(GalleryItem("Sarah Nude Puppygirl",

    ["spuppy1", "spuppy2", "spuppy3", "spuppy4", "spuppy5",
     "spuppy6", "spuppy7", "spuppy8", "spuppy9", "spuppy10",
     "spuppy11", "spuppy12", "spuppy13", "spuppy14", "spuppy15"],

    "spuppyt1"))

    gallery_items.append(GalleryItem("Noelle Boobs",

    ["nboobs1", "nboobs2", "nboobs3", "nboobs4", "nboobs5",
     "nboobs6", "nboobs7", "nboobs8", "nboobs9", "nboobs10",
     "nboobs11", "nboobs12", "nboobs13", "nboobs14", "nboobs15",
     "nboobs16", "nboobs17", "nboobs18"],

    "nboobst1"))











    gallery_items.append(GalleryItem("Jane Masturbation",

    ["janemast1", "janemast2", "janemast3", "janemast4", "janemast5",
     "janemast6", "janemast7", "janemast8", "janemast9", "janemast10",
     "janemast11", "janemast12", "janemast13", "janemast14", "janemast15",
     "janemast16", "janemast17", "janemast18", "janemast19", "janemast20",
     "janemast21"],

    "janemastt1"))

    gallery_items.append(GalleryItem("Sarah Buttjob",

    ["sarahbuttjob1", "sarahbuttjob2", "sarahbuttjob3", "sarahbuttjob4",
     "sarahbuttjob5", "sarahbuttjob6", "sarahbuttjob7", "sarahbuttjob8",
     "sarahbuttjob9", "sarahbuttjob10", "sarahbuttjob11", "sarahbuttjob12",
     "sarahbuttjob13", "sarahbuttjob14", "sarahbuttjob15", "sarahbuttjob16",
     "sarahbuttjob17"],

    "sarahbuttjobt1"))

    gallery_items.append(GalleryItem("Noelle Blowjob",

    ["noelleblowjob1", "noelleblowjob2", "noelleblowjob3", "noelleblowjob4",
     "noelleblowjob5", "noelleblowjob6",
     "noelleblowjob9", "noelleblowjob10", "noelleblowjob11", "noelleblowjob12",
     "noelleblowjob13", "noelleblowjob14", "noelleblowjob15", "noelleblowjob16",
     "noelleblowjob17",  "noelleblowjob19"],

    "noelleblowjobt1"))

    gallery_items.append(GalleryItem("Kira Thighjob",

    ["kirathighjob1", "kirathighjob2", "kirathighjob3", "kirathighjob4",
     "kirathighjob5", "kirathighjob6", "kirathighjob7", "kirathighjob8",
     "kirathighjob9", "kirathighjob10", "kirathighjob11", "kirathighjob12",
     "kirathighjob13", "kirathighjob14", "kirathighjob15", "kirathighjob16",
     "kirathighjob17", "kirathighjob18", "kirathighjob19"],

    "kirathighjobt1"))











    gallery_items.append(GalleryItem("Noelle & Jane Lesbians",

    ["noellejaneles1", "noellejaneles2", "noellejaneles3", "noellejaneles4",
     "noellejaneles5", "noellejaneles6", "noellejaneles7", "noellejaneles8",
     "noellejaneles9", "noellejaneles10", "noellejaneles11", "noellejaneles12",
     "noellejaneles13", "noellejaneles14", "noellejaneles15", "noellejaneles16",
     "noellejaneles17", "noellejaneles18", "noellejaneles19"],

    "noellejanelest1"))

    gallery_items.append(GalleryItem("Kira & Sarah Lesbians",

    ["kirasarahles1", "kirasarahles2", "kirasarahles3", "kirasarahles4",
     "kirasarahles5", "kirasarahles6", "kirasarahles7", "kirasarahles8",
     "kirasarahles9", "kirasarahles10", "kirasarahles11", "kirasarahles12",
     "kirasarahles13"],

    "kirasarahlest1"))

    gallery_items.append(GalleryItem("Buttplugs",

    ["buttplugline1", "buttplugline2", "buttplugline3", "buttplugline4",
     "buttplugline5", "buttplugline6", "buttplugline7", "buttplugline8",
     "buttplugline9", "buttplugline10", "buttplugline11", "buttplugline12"],

    "buttpluglinet1"))










    gallery_items.append(GalleryItem("Kira Enslavement",

    ["kiraslave1", "kiraslave2", "kiraslave4",
     "kiraslave5", "kiraslave6", "kiraslave8",
     "kiraslave9", "kiraslave10", "kiraslave11"],

    "kiraslavet"))

    gallery_items.append(GalleryItem("Sarah Enslavement",

    ["sarahslave1", "sarahslave2", "sarahslave3", "sarahslave4",
     "sarahslave5", "sarahslave6", "sarahslave7", "sarahslave8"],

    "sarahslavet"))

    gallery_items.append(GalleryItem("Noelle Enslavement",

    ["noelleslave1", "noelleslave2", "noelleslave3", "noelleslave4",
     "noelleslave5", "noelleslave6", "noelleslave7", "noelleslave8",
     "noelleslave9"],

    "noelleslavet"))

    gallery_items.append(GalleryItem("Jane Enslavement",

    ["janeslave1", "janeslave2", "janeslave3", "janeslave4",
     "janeslave5", "janeslave6", "janeslave7", "janeslave8",
     "janeslave9", "janeslave10", "janeslave11"],

    "janeslavet"))

    gallery_items.append(GalleryItem("Finale Orgy Pre",
    ["final_orgy_pre"],
    "final_orgy_pret"))

    gallery_items.append(GalleryItem("Final Orgy Sarah",

    ["fosv1", "fosv2", "fosv3", "fosv4", "fosv5",
     "fosa1", "fosa2", "fosa3", "fosa4", "fosa5"],

    "fosv1t"))

    gallery_items.append(GalleryItem("Final Orgy Jane",

    ["fosvja1", "fosvja2", "fosvja3", "fosvja4", "fosvja5",
     "fosvjv1", "fosvjv2", "fosvjv3", "fosvjv4", "fosvjv5",
     "fosaja1", "fosaja2", "fosaja3", "fosaja4", "fosaja5",
     "fosajv1", "fosajv2", "fosajv3", "fosajv4", "fosajv5"],

    "fosvja1t"))

    gallery_items.append(GalleryItem("Final Orgy Kira",

    ["fosvjvkv1", "fosvjvkv2", "fosvjvkv3", "fosvjvkv4", "fosvjvkv5",
     "fosvjakv1", "fosvjakv2", "fosvjakv3", "fosvjakv4", "fosvjakv5",
     "fosvjaka1", "fosvjaka2", "fosvjaka3", "fosvjaka4", "fosvjaka5",
     "fosvjvka1", "fosvjvka2", "fosvjvka3", "fosvjvka4", "fosvjvka5",
     "fosajvkv1", "fosajvkv2", "fosajvkv3", "fosajvkv4", "fosajvkv5",
     "fosajakv1", "fosajakv2", "fosajakv3", "fosajakv4", "fosajakv5",
     "fosajaka1", "fosajaka2", "fosajaka3", "fosajaka4", "fosajaka5",
     "fosajvka1", "fosajvka2", "fosajvka3", "fosajvka4", "fosajvka5"],

    "fosvjvkv1t"))

    gallery_items.append(GalleryItem("Final Orgy Noelle",

    ["fosvjvkvnv1", "fosvjvkvnv2", "fosvjvkvnv3", "fosvjvkvnv4", "fosvjvkvnv5",
     "fosvjvkanv1", "fosvjvkanv2", "fosvjvkanv3", "fosvjvkanv4", "fosvjvkanv5",
     "fosvjvkvna1", "fosvjvkvna2", "fosvjvkvna3", "fosvjvkvna4", "fosvjvkvna5",
     "fosvjvkana1", "fosvjvkana2", "fosvjvkana3", "fosvjvkana4", "fosvjvkana5",
     "fosvjakvnv1", "fosvjakvnv2", "fosvjakvnv3", "fosvjakvnv4", "fosvjakvnv5",
     "fosvjakvna1", "fosvjakvna2", "fosvjakvna3", "fosvjakvna4", "fosvjakvna5",
     "fosvjakanv1", "fosvjakanv2", "fosvjakanv3", "fosvjakanv4", "fosvjakanv5",
     "fosvjakana1", "fosvjakana2", "fosvjakana3", "fosvjakana4", "fosvjakana5",
     "fosajvkvnv1", "fosajvkvnv2", "fosajvkvnv3", "fosajvkvnv4", "fosajvkvnv5",
     "fosajvkanv1", "fosajvkanv2", "fosajvkanv3", "fosajvkanv4", "fosajvkanv5",
     "fosajvkvna1", "fosajvkvna2", "fosajvkvna3", "fosajvkvna4", "fosajvkvna5",
     "fosajvkana1", "fosajvkana2", "fosajvkana3", "fosajvkana4", "fosajvkana5",
     "fosajakvnv1", "fosajakvnv2", "fosajakvnv3", "fosajakvnv4", "fosajakvnv5",
     "fosajakvna1", "fosajakvna2", "fosajakvna3", "fosajakvna4", "fosajakvna5",
     "fosajakanv1", "fosajakanv2", "fosajakanv3", "fosajakanv4", "fosajakanv5",
     "fosajakana1", "fosajakana2", "fosajakana3", "fosajakana4", "fosajakana5"],

    "fosvjvkvnv1t"))

    gallery_items.append(GalleryItem("Noelle Popups",
    ["fop_noelle1", "fop_noelle2", "fop_noelle3"], "fop_noelle1t"))
    gallery_items.append(GalleryItem("Kira Popups",
    ["fop_kira1", "fop_kira2", "fop_kira3"], "fop_kira1t"))
    gallery_items.append(GalleryItem("Sarah Popups",
    ["fop_sarah1", "fop_sarah2", "fop_sarah3"], "fop_sarah1t"))
    gallery_items.append(GalleryItem("Jane Popups",
    ["fop_jane1", "fop_jane2", "fop_jane3"], "fop_jane1t"))



    gallery_items.append(GalleryItem("Kira Finale",
    ["kira_finale_a"], "kira_finale_at"))
    gallery_items.append(GalleryItem("Sarah Finale",
    ["sarah_finale_a"], "sarah_finale_at"))
    gallery_items.append(GalleryItem("Noelle Finale",
    ["noelle_finale_a"], "noelle_finale_at"))
    gallery_items.append(GalleryItem("Jane Finale",
    ["jane_finale_a"], "jane_finale_at"))
    gallery_items.append(GalleryItem("Kira Finale Perfect",
    ["kira_finale_b"], "kira_finale_bt"))
    gallery_items.append(GalleryItem("Sarah Finale Perfect",
    ["sarah_finale_b"], "sarah_finale_bt"))
    gallery_items.append(GalleryItem("Noelle Finale Perfect",
    ["noelle_finale_b"], "noelle_finale_bt"))
    gallery_items.append(GalleryItem("Jane Finale Perfect",
    ["jane_finale_b"], "jane_finale_bt"))


    gallery_items.append(GalleryItem("Finale", ["finale_a"], "finale_at"))
    gallery_items.append(GalleryItem("Finale Perfect", ["finale_b"], "finale_bt"))









    gallery_items.append(GalleryItem("Sarah Dogtrainer",

    ["badend sara_rule"],

    "badend sara_rulet"))

    gallery_items.append(GalleryItem("Noelle Footrub",

    ["badend noelle_footrub"],

    "badend noelle_footrubt"))

    gallery_items.append(GalleryItem("Kira Control",

    ["badend kira_chair"],

    "badend kira_chairt"))

    gallery_items.append(GalleryItem("Cold Outside",

    ["badend cold_outside"],

    "badend cold_outsidet"))

    gallery_items.append(GalleryItem("Covers Alone",

    ["badend covers"],

    "badend coverst"))

    gallery_items.append(GalleryItem("Cooking",

    ["badend cooking"],

    "badend cookingt"))

    gallery_items.append(GalleryItem("Jason Alone",

    ["badend jason_sad"],

    "badend jason_sadt"))




screen neu_gallery:
    tag menu
    add "gallery_bg"

    $ starto = gallery_page * maxperpage
    $ fin = min(starto + maxperpage - 1, len(gallery_items) - 1)


    grid maxnumx maxnumy:
        xfill True
        yfill True

        for i in range(starto, fin + 1):
            $ gallery_items[i].refresh_lock()
            if gallery_items[i].is_locked:
                add gallery_items[i].lockedthumbnail:
                    xalign 0.5
                    yalign 0.5
            else:






                imagebutton idle gallery_items[i].thumbnail:
                    action [SetVariable("looking", True), Show("neu_gallery_closeup", dissolve, gallery_items[i].images)]
                    xalign 0.5
                    yalign 0.5

        for i in range(fin - starto + 1, maxperpage):
            null


    grid maxnumx maxnumy:
        xfill True
        yfill True

        for i in range(starto, fin + 1):
            hbox:
                spacing maxnumx - 70
                xalign 0.5
                yalign 0.1
                $ totalo = gallery_items[i].num_images()
                $ partio = gallery_items[i].num_unlocked



        for i in range(fin - starto + 1, maxperpage):
            null




    if gallery_page > 0 and not looking:
        imagebutton idle "back_arrow":
            action SetVariable("gallery_page", gallery_page - 1)
            xalign 0.1
            yalign 0.99
    if ((gallery_page + 1) * maxperpage < len(gallery_items)) and not looking:
        imagebutton idle "right_arrow":
            action SetVariable("gallery_page", gallery_page + 1)
            xalign 0.9
            yalign 0.99


    imagebutton idle "return_arrow":
        action Return()
        xalign 0.5
        yalign 0.99










screen neu_gallery_closeup(images):
    add images[closeup_page] at truecenter

    if closeup_page > 0:
        imagebutton idle "back_arrow":
            action SetVariable("closeup_page", closeup_page - 1)
            xalign 0.1
            yalign 0.99


    if closeup_page < len(images) - 1:
        imagebutton idle "right_arrow":
            action SetVariable("closeup_page", closeup_page + 1)
            xalign 0.9
            yalign 0.99


    imagebutton idle "return_arrow":
        action [SetVariable("closeup_page", 0), Hide("neu_gallery_closeup", dissolve), SetVariable("looking", False)]
        xalign 0.5
        yalign 0.99
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
