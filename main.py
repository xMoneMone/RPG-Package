import pygame
from settings import GameSettings, PlayerSettings
from room import Room
from run_game import run_game
from character import Character
from dialogue import Dialogue
from cutscene import Cutscene


def main():
    pygame.init()

    game_settings = GameSettings(r"graphics\character_frames\down-1.png", scale=2, colourkey=(255, 75, 248),
                                 width=pygame.display.Info().current_w, height=pygame.display.Info().current_h,
                                 cgs_path=r"graphics\dialogue\CGs", cursor_path=r"graphics\cursor.png", music_volume=6,
                                 interaction_volume=6, interaction_sound=r'sound\interact.mp3')
    player_settings = PlayerSettings(r"graphics\character_frames")
    player = Character(960, 600, game_settings, player_settings,
                       Dialogue(r"graphics\dialogue\textbox.png", game_settings,
                                portraits_path=r"graphics\dialogue\player\portraits", portrait_right=True,
                                margin_bottom=30))
    house_outside = Room("house_outside", r"json_files\house_outside\coordinates.json",
                         r"json_files\house_outside\interaction_text.json",
                         r"graphics\room_assets\house_outside", game_settings, music_path=r"sound/Morning.mp3")
    current_room = house_outside
    cutscene_key = {
        "player": player.dialogue,
        "other": Dialogue(r"graphics\dialogue\textbox.png", game_settings,
                          portraits_path=r"graphics\dialogue\player\portraits", margin_bottom=30)
    }

    interactions = {"girl": Cutscene(r"json_files\house_outside\girl_cutscene.json", cutscene_key, game_settings,
                                     prioroty=2)}

    run_game(game_settings, current_room, interactions, player)


if __name__ == "__main__":
    main()
