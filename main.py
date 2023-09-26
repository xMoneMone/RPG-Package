import pygame
from settings import GameSettings, PlayerSettings
from room import Room
from run_game import run_game
from character import Character
from dialogue import Dialogue


def main():
    pygame.init()

    game_settings = GameSettings(r"graphics\character_frames\down-1.png", scale=2, colourkey=(255, 75, 248),
                                 width=pygame.display.Info().current_w, height=pygame.display.Info().current_h)
    player_settings = PlayerSettings(r"graphics\character_frames")
    player = Character(960, 600, game_settings, player_settings,
                       Dialogue(r"graphics\dialogue\textbox.png", game_settings,
                                portraits_path=r"graphics\dialogue\player\portraits", portrait_right=True,
                                margin_bottom=15))
    current_room = Room("house_outside", r"json_files\house_outside\coordinates.json",
                        r"json_files\house_outside\interaction_text.json",
                        r"graphics\room_assets\house_outside", game_settings)
    interactions = {}

    run_game(game_settings, current_room, interactions, player)


if __name__ == "__main__":
    main()
