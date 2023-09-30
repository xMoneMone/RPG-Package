class GameSettings:
    def __init__(self, icon_path, fps=60, scale=1, colourkey=(255, 255, 255), width=220, height=220, caption="Game",
                 portrait_scaling=None, textbox_scaling=None, objects_animation_speed=50, cgs_path="", cursor_path=""):
        self.FPS = fps
        self.SCALE = scale
        self.COLOURKEY = colourkey
        self.SCREEN_WIDTH = width
        self.SCREEN_HEIGHT = height
        self.ICON = icon_path
        self.CAPTION = caption
        self.PORTRAIT_SCALE = scale
        self.OBJECTS_ANIMATION_SPEED = objects_animation_speed
        self.CGS_PATH = cgs_path
        self.CURSOR_PATH = cursor_path
        if portrait_scaling:
            self.PORTRAIT_SCALE = portrait_scaling
        self.TEXTBOX_SCALE = scale
        if textbox_scaling:
            self.TEXTBOX_SCALE = textbox_scaling
