# TODO: fix max_height
TextField = """
MDTextField:
    hint_text: "Enter username"
    helper_text: "or click on forgot username"
    helper_text_mode: "on_focus"
    multiline:True
    icon_right: "music-note"
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x': 0.5, 'center_y': 0.5}
    size_hint_x:None
    width:230
    max_height: "1dp"
"""
Toolbar = """
MDToolbar:
    title: "MDToolbar"
    type: "top"
    right_action_items: [["comment-question", lambda x: app.mark_icon_callback(x)]]
    md_bg_color: app.theme_cls.primary_color
"""