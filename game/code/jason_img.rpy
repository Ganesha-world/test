








image Jason_face neutral:
    LiveComposite(
        (113, 136),
        (0, 0), "images/Character_parts/Jason/jason_eyes_1x.webp",
        (0, 0), "images/Character_parts/Jason/jason_mouth_1x.webp",
    )
image Jason_face happy:
    LiveComposite(
        (113, 136),
        (0, 0), "images/Character_parts/Jason/jason_eyes_1x.webp",
        (0, 0), "images/Character_parts/Jason/jason_mouth_2x.webp",
    )
image Jason_face happy_ad:
    LiveComposite(
        (113, 136),
        (0, 0), "images/Character_parts/Jason/jason_eyes_1x.webp",
        (0, 0), "images/Character_parts/Jason/jason_mouth_6x.webp",
    )
image Jason_face rolleyes:
    LiveComposite(
        (113, 136),
        (0, 0), "images/Character_parts/Jason/jason_eyes_4x.webp",
        (0, 0), "images/Character_parts/Jason/jason_mouth_1x.webp",
    )
image Jason_face wonder:
    LiveComposite(
        (113, 136),
        (0, 0), "images/Character_parts/Jason/jason_eyes_4x.webp",
        (0, 0), "images/Character_parts/Jason/jason_mouth_5x.webp",
    )
image Jason_face daydream:
    LiveComposite(
        (113, 136),
        (0, 0), "images/Character_parts/Jason/jason_eyes_5x.webp",
        (0, 0), "images/Character_parts/Jason/jason_mouth_3x.webp",
    )
image Jason_face avoid:
    LiveComposite(
        (113, 136),
        (0, 0), "images/Character_parts/Jason/jason_eyes_6x.webp",
        (0, 0), "images/Character_parts/Jason/jason_mouth_5x.webp",
    )
image Jason_face shocked:
    LiveComposite(
        (113, 136),
        (0, 0), "images/Character_parts/Jason/jason_eyes_1x.webp",
        (0, 0), "images/Character_parts/Jason/jason_mouth_5x.webp",
    )
image Jason_face frown:
    LiveComposite(
        (113, 136),
        (0, 0), "images/Character_parts/Jason/jason_eyes_2x.webp",
        (0, 0), "images/Character_parts/Jason/jason_mouth_1x.webp",
    )

image Jason_body nude_1:
    LiveComposite(
        (992, 1403),
        (0, 0), "images/Character_parts/Jason/jason_figure_pose1.webp",
    )
image Jason_body nude_2:
    LiveComposite(
        (992, 1403),
        (0, 0), "images/Character_parts/Jason/jason_figure_pose2.webp",
    )
image Jason_body normal_1:
    Flatten(LiveComposite(
        (992, 1403),
        (0, 0), "images/Character_parts/Jason/jason_figure_pose1.webp",
        (0, 0), "images/Character_parts/Jason/jason_clothes_p1_o1.webp",
    ))
image Jason_body normal_2:
    Flatten(LiveComposite(
        (992, 1403),
        (0, 0), "images/Character_parts/Jason/jason_figure_pose1.webp",
        (0, 0), "images/Character_parts/Jason/jason_clothes_p2_o1.webp",
    ))
image Jason_body normal_3:
    Flatten(LiveComposite(
        (992, 1403),
        (0, 0), "images/Character_parts/Jason/jason_figure_pose2.webp",
        (0, 0), "images/Character_parts/Jason/jason_clothes_p3_o1.webp",
    ))
image Jason_body normal_4:
    Flatten(LiveComposite(
        (992, 1403),
        (0, 0), "images/Character_parts/Jason/jason_figure_pose2.webp",
        (0, 0), "images/Character_parts/Jason/jason_clothes_p4_o1.webp",
    ))
image Jason_body cat_1:
    Flatten(LiveComposite(
        (992, 1403),
        (0, 0), "images/Character_parts/Jason/jason_figure_pose1.webp",
        (0, 0), "images/Character_parts/Jason/jason_clothes_p1_o2.webp",
    ))
image Jason_body cat_2:
    Flatten(LiveComposite(
        (992, 1403),
        (0, 0), "images/Character_parts/Jason/jason_figure_pose1.webp",
        (0, 0), "images/Character_parts/Jason/jason_clothes_p2_o2.webp",
    ))
image Jason_body cat_3:
    Flatten(LiveComposite(
        (992, 1403),
        (0, 0), "images/Character_parts/Jason/jason_figure_pose2.webp",
        (0, 0), "images/Character_parts/Jason/jason_clothes_p3_o2.webp",
    ))
image Jason_body cat_4:
    Flatten(LiveComposite(
        (992, 1403),
        (0, 0), "images/Character_parts/Jason/jason_figure_pose2.webp",
        (0, 0), "images/Character_parts/Jason/jason_clothes_p4_o2.webp",
    ))

image Jason neutral:
    choice (jason_outfit.outfit() == JasonOutfitEnum.NUDE):
        LiveComposite(
            (992, 1403),
            (0, 0), "Jason_body nude_2",
            (416, 248), "Jason_face neutral",
        )
    choice (jason_outfit.outfit() == JasonOutfitEnum.NORMAL):
        LiveComposite(
            (992, 1403),
            (0, 0), "Jason_body normal_2",
            (416, 248), "Jason_face neutral",
        )
    choice (jason_outfit.outfit() == JasonOutfitEnum.CAT):
        LiveComposite(
            (992, 1403),
            (0, 0), "Jason_body cat_2",
            (416, 248), "Jason_face neutral",
        )

image Jason happy:
    choice (jason_outfit.outfit() == JasonOutfitEnum.NUDE):
        LiveComposite(
            (992, 1403),
            (0, 0), "Jason_body nude_1",
            (416, 248), "Jason_face happy",
        )
    choice (jason_outfit.outfit() == JasonOutfitEnum.NORMAL):
        LiveComposite(
            (992, 1403),
            (0, 0), "Jason_body normal_2",
            (416, 248), "Jason_face happy",
        )
    choice (jason_outfit.outfit() == JasonOutfitEnum.CAT):
        LiveComposite(
            (992, 1403),
            (0, 0), "Jason_body cat_2",
            (416, 248), "Jason_face happy",
        )

image Jason happy_aroused:
    choice (jason_outfit.outfit() == JasonOutfitEnum.NUDE):
        LiveComposite(
            (992, 1403),
            (0, 0), "Jason_body nude_1",
            (416, 248), "Jason_face happy",
        )
    choice (jason_outfit.outfit() == JasonOutfitEnum.NORMAL):
        LiveComposite(
            (992, 1403),
            (0, 0), "Jason_body normal_1",
            (416, 248), "Jason_face happy",
        )
    choice (jason_outfit.outfit() == JasonOutfitEnum.CAT):
        LiveComposite(
            (992, 1403),
            (0, 0), "Jason_body cat_1",
            (416, 248), "Jason_face happy",
        )

image Jason happy_ad:
    choice (jason_outfit.outfit() == JasonOutfitEnum.NUDE):
        LiveComposite(
            (992, 1403),
            (0, 0), "Jason_body nude_1",
            (416, 248), "Jason_face happy_ad",
        )
    choice (jason_outfit.outfit() == JasonOutfitEnum.NORMAL):
        LiveComposite(
            (992, 1403),
            (0, 0), "Jason_body normal_1",
            (416, 248), "Jason_face happy_ad",
        )
    choice (jason_outfit.outfit() == JasonOutfitEnum.CAT):
        LiveComposite(
            (992, 1403),
            (0, 0), "Jason_body cat_1",
            (416, 248), "Jason_face happy_ad",
        )

image Jason happy_h:
    choice (jason_outfit.outfit() == JasonOutfitEnum.NUDE):
        LiveComposite(
            (992, 1403),
            (0, 0), "Jason_body nude_2",
            (416, 248), "Jason_face happy",
        )
    choice (jason_outfit.outfit() == JasonOutfitEnum.NORMAL):
        LiveComposite(
            (992, 1403),
            (0, 0), "Jason_body normal_2",
            (416, 248), "Jason_face happy",
        )
    choice (jason_outfit.outfit() == JasonOutfitEnum.CAT):
        LiveComposite(
            (992, 1403),
            (0, 0), "Jason_body cat_2",
            (416, 248), "Jason_face happy",
        )

image Jason rolleyes:
    choice (jason_outfit.outfit() == JasonOutfitEnum.NUDE):
        LiveComposite(
            (992, 1403),
            (0, 0), "Jason_body nude_2",
            (416, 248), "Jason_face rolleyes",
        )
    choice (jason_outfit.outfit() == JasonOutfitEnum.NORMAL):
        LiveComposite(
            (992, 1403),
            (0, 0), "Jason_body normal_2",
            (416, 248), "Jason_face rolleyes",
        )
    choice (jason_outfit.outfit() == JasonOutfitEnum.CAT):
        LiveComposite(
            (992, 1403),
            (0, 0), "Jason_body cat_2",
            (416, 248), "Jason_face rolleyes",
        )

image Jason wonder:
    choice (jason_outfit.outfit() == JasonOutfitEnum.NUDE):
        LiveComposite(
            (992, 1403),
            (0, 0), "Jason_body nude_2",
            (416, 248), "Jason_face wonder",
        )
    choice (jason_outfit.outfit() == JasonOutfitEnum.NORMAL):
        LiveComposite(
            (992, 1403),
            (0, 0), "Jason_body normal_2",
            (416, 248), "Jason_face wonder",
        )
    choice (jason_outfit.outfit() == JasonOutfitEnum.CAT):
        LiveComposite(
            (992, 1403),
            (0, 0), "Jason_body cat_2",
            (416, 248), "Jason_face wonder",
        )

image Jason daydream:
    choice (jason_outfit.outfit() == JasonOutfitEnum.NUDE):
        LiveComposite(
            (992, 1403),
            (0, 0), "Jason_body nude_2",
            (416, 248), "Jason_face daydream",
        )
    choice (jason_outfit.outfit() == JasonOutfitEnum.NORMAL):
        LiveComposite(
            (992, 1403),
            (0, 0), "Jason_body normal_2",
            (416, 248), "Jason_face daydream",
        )
    choice (jason_outfit.outfit() == JasonOutfitEnum.CAT):
        LiveComposite(
            (992, 1403),
            (0, 0), "Jason_body cat_2",
            (416, 248), "Jason_face daydream",
        )

image Jason daydream_aroused:
    choice (jason_outfit.outfit() == JasonOutfitEnum.NUDE):
        LiveComposite(
            (992, 1403),
            (0, 0), "Jason_body nude_1",
            (416, 248), "Jason_face daydream",
        )
    choice (jason_outfit.outfit() == JasonOutfitEnum.NORMAL):
        LiveComposite(
            (992, 1403),
            (0, 0), "Jason_body normal_1",
            (416, 248), "Jason_face daydream",
        )
    choice (jason_outfit.outfit() == JasonOutfitEnum.CAT):
        LiveComposite(
            (992, 1403),
            (0, 0), "Jason_body cat_1",
            (416, 248), "Jason_face daydream",
        )

image Jason avoid:
    choice (jason_outfit.outfit() == JasonOutfitEnum.NUDE):
        LiveComposite(
            (992, 1403),
            (0, 0), "Jason_body nude_2",
            (416, 248), "Jason_face avoid",
        )
    choice (jason_outfit.outfit() == JasonOutfitEnum.NORMAL):
        LiveComposite(
            (992, 1403),
            (0, 0), "Jason_body normal_2",
            (416, 248), "Jason_face avoid",
        )
    choice (jason_outfit.outfit() == JasonOutfitEnum.CAT):
        LiveComposite(
            (992, 1403),
            (0, 0), "Jason_body cat_2",
            (416, 248), "Jason_face avoid",
        )

image Jason shocked:
    choice (jason_outfit.outfit() == JasonOutfitEnum.NUDE):
        LiveComposite(
            (992, 1403),
            (0, 0), "Jason_body nude_2",
            (416, 248), "Jason_face shocked",
        )
    choice (jason_outfit.outfit() == JasonOutfitEnum.NORMAL):
        LiveComposite(
            (992, 1403),
            (0, 0), "Jason_body normal_2",
            (416, 248), "Jason_face shocked",
        )
    choice (jason_outfit.outfit() == JasonOutfitEnum.CAT):
        LiveComposite(
            (992, 1403),
            (0, 0), "Jason_body cat_2",
            (416, 248), "Jason_face shocked",
        )

image Jason avoid_aroused:
    choice (jason_outfit.outfit() == JasonOutfitEnum.NUDE):
        LiveComposite(
            (992, 1403),
            (0, 0), "Jason_body nude_1",
            (416, 248), "Jason_face avoid",
        )
    choice (jason_outfit.outfit() == JasonOutfitEnum.NORMAL):
        LiveComposite(
            (992, 1403),
            (0, 0), "Jason_body normal_1",
            (416, 248), "Jason_face avoid",
        )
    choice (jason_outfit.outfit() == JasonOutfitEnum.CAT):
        LiveComposite(
            (992, 1403),
            (0, 0), "Jason_body cat_1",
            (416, 248), "Jason_face avoid",
        )

image Jason frown:
    choice (jason_outfit.outfit() == JasonOutfitEnum.NUDE):
        LiveComposite(
            (992, 1403),
            (0, 0), "Jason_body nude_1",
            (416, 248), "Jason_face frown",
        )
    choice (jason_outfit.outfit() == JasonOutfitEnum.NORMAL):
        LiveComposite(
            (992, 1403),
            (0, 0), "Jason_body normal_1",
            (416, 248), "Jason_face frown",
        )
    choice (jason_outfit.outfit() == JasonOutfitEnum.CAT):
        LiveComposite(
            (992, 1403),
            (0, 0), "Jason_body cat_1",
            (416, 248), "Jason_face frown",
        )
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
