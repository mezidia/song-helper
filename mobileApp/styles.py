# TODO: fix max_height
TextField = """
MDTextField:
    hint_text: "Enter username"
    helper_text: "Click on question to get main portal"
    helper_text_mode: "on_focus"
    multiline:True
    icon_right: "music-note"
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x': 0.5, 'center_y': 0.5}
    size_hint_x:None
    width:230
    max_height: "1dp"
"""
Label = """
MDLabel:
    text: 'Enter your nickname' 
    halign: 'center' 
    theme_text_color: 'Primary' 
    font_style: 'H5'
"""
Toolbar = """
MDToolbar:
    title: "Song-helper"
    type: "top"
    right_action_items: [["comment-question", lambda x: app.mark_icon_callback(x)]]
    md_bg_color: app.theme_cls.primary_color
    elevation: 10
"""
