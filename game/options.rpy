













define config.name = _("Snow Daze: The Music of Winter")





define gui.show_name = False




define config.debug = False
define config.developer = False
define config.console = False

define config.version = "1.2-Steam"








define gui.about = _(
"{b}A Cypress Zeta Game{/b}\n"
"\n"
"\n"
"{b}Cast{/b}\n"
"Diana Lockheart               Noelle\n"
"Silica                                    Jane\n"
"Shiyon                                 Kira\n"
"                                              Sarah\n"
"\n"
"{b}Art{/b}\n"
"FreeGlass\n"
"Brellom\n"
"Idlecum\n"
"Short Blue Imp\n"
"\n"
"{b}Concept Art{/b}\n"
"Mindwipe\n"
"NinjaKitty\n"
"SleepyMaid\n"
"Short Blue Imp\n"
"\n"
"{b}Programming{/b}\n"
"polisummer\n"
"tippi\n"
"\n"
"{b}Music{/b}\n"
"Nathaniel Platier\n"
"\n"
"{b}Special Thanks{/b}\n"
"Hexun for coding a useful tool\n"
"Pan\n"
"And an anonymous writing friend. You know who you are.\n"
"\n")






define build.name = "SnowDaze"







define config.has_sound = True
define config.has_music = True
define config.has_voice = True














define config.main_menu_music = "music/ost/Snowflake Lullaby _Piano+Strings_.ogg.opus"









define config.enter_transition = dissolve
define config.exit_transition = dissolve




define config.after_load_transition = None




define config.end_game_transition = None



















define config.window = "auto"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)







default preferences.text_cps = 30





default preferences.afm_time = 15

default preferences.music_volume = 0.75
















define config.save_directory = "SnowDazeFull-1474642557"







define config.window_icon = "gui/window_icon.webp"






init python:




















    build.archive('archive_kyungeki', 'all')
    build.archive('archive_bulk', 'all')
    build.archive('archive_outbreak', 'all')

    build.classify('**~', None)
    build.classify('**.md', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/**.clip', None)
    build.classify('**/thumbs.db', None)
    build.classify('game/**.rpy', None)
    build.classify('game/traceback.txt', None)
    build.classify('game/kyungeki_tools/**', None)



    build.classify('**.ico', 'archive_kyungeki')
    build.classify('**.icns', 'archive_kyungeki')
    build.classify('game/images/**.webm', 'archive_bulk')
    build.classify('game/**.jpg', 'archive_bulk')
    build.classify('game/**.webp', 'archive_bulk')
    build.classify('game/**.rpyc', 'archive_outbreak')
    build.classify('game/code/**', 'archive_outbreak')
    build.classify('game/story/**', 'archive_outbreak')
    build.classify('game/music/**', 'archive_outbreak')
    build.classify('game/voiceacting/**', 'archive_outbreak')
    build.classify('game/**.ttf', 'archive_outbreak')





    build.documentation('*.html')
    build.documentation('*.txt')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
