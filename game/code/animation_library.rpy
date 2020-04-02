



















init python:


    z_base = 0.7




    y_zoom_point = 20









    far_left =     -0.33
    close_left =   -0.20
    mid_left =      0.05
    mid =           0.55
    mid_right =     1.00
    far_right =     1.30








    jason_height = -0.25
    jane_height = -0.471
    noelle_height = -0.25
    sarah_height = -0.471
    kira_height = -0.547



transform jason_normal(x_align):
    normal((x_align, jason_height))
transform jane_normal(x_align):
    normal((x_align, jane_height))
transform noelle_normal(x_align):
    normal((x_align, noelle_height))
transform sarah_normal(x_align):
    normal((x_align, sarah_height))
transform kira_normal(x_align):
    normal((x_align, kira_height))
transform cypress_normal(x_align):
    zoomed((x_align, 0.6), 0.6, y_zoom_point)

transform jason_easeinleft(x_align):
    easeinleft((x_align, jason_height))
transform jane_easeinleft(x_align):
    easeinleft((x_align, jane_height))
transform noelle_easeinleft(x_align):
    easeinleft((x_align, noelle_height))
transform sarah_easeinleft(x_align):
    easeinleft((x_align, sarah_height))
transform kira_easeinleft(x_align):
    easeinleft((x_align, kira_height))

transform jason_easeinright(x_align):
    easeinright((x_align, jason_height))
transform jane_easeinright(x_align):
    easeinright((x_align, jane_height))
transform noelle_easeinright(x_align):
    easeinright((x_align, noelle_height))
transform sarah_easeinright(x_align):
    easeinright((x_align, sarah_height))
transform kira_easeinright(x_align):
    easeinright((x_align, kira_height))





transform normal(p):
    on show:
        xalign p[0] yalign p[1]
        normal_stay
    on replace:
        parallel:
            normal_stay
        parallel:
            easein .25 xalign p[0]
        parallel:
            easein .15 yalign p[1]

transform normal_stay:
    subpixel True
    on show:
        zoom z_base * 0.95 alpha 0.00
        yoffset y_zoom_point
        easein .25 yoffset 0 zoom z_base alpha 1.00
    on replace:
        alpha 1.00
        parallel:
            easein .25 zoom z_base
        parallel:
            easein .25 yoffset 0


transform zoomed(p, z_mod, y_off):
    on show:
        xalign p[0] yalign p[1]
        zoomed_stay(z_mod, y_off)
    on replace:
        parallel:
            zoomed_stay(z_mod, y_off)
        parallel:
            easein .25 xalign p[0]
        parallel:
            easein .25 yalign p[1]

transform zoomed_stay(z_mod, y_off):
    subpixel True
    on show:
        zoom (z_base * z_mod) * 0.95 alpha 0.00
        yoffset y_off
        easein .25 zoom (z_base * z_mod) * 1.00 alpha 1.00
    on replace:
        alpha 1.00
        parallel:
            easein .25 zoom (z_base * z_mod) * 1.00
        parallel:
            easein .25 yoffset y_off


transform talking(p):
    zoomed(p, 1.05, -40)

transform talking_stay:
    zoomed_stay(1.05, -40)



transform easeinleft(p):
    subpixel True
    on show:
        zoom z_base
        xalign -1 yalign p[1]
        easein .25 xalign p[0]

transform easeinright(p):
    subpixel True
    on show:
        zoom z_base
        xalign 2.0 yalign p[1]
        easein .25 xalign p[0]



transform thide:
    subpixel True alpha 1.00
    transform_anchor True
    on hide:
        easein 0.25 zoom z_base * 0.95 alpha 0.00 yoffset y_zoom_point





transform deflate:
    subpixel True alpha 1.00
    easein 0.5 yoffset 30


transform bounce:
    subpixel True alpha 1.00
    easein .1 yoffset -40
    easeout .1 yoffset 0




define dissolve = Dissolve(0.25)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
