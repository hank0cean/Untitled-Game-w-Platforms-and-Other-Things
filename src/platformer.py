import arcade

SCREEN_W = 900
SCREEN_H = 600
TITLE = "Platformer"

class Platformer(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_W, SCREEN_H, TITLE)
        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        pass

    def update(self, delta_time: float):
        pass

    def on_update(self, delta_time: float):
        pass

    def on_draw(self):
        arcade.start_render()

    def on_key_press(self, symbol: int, modifiers: int):
        pass

    def on_key_release(self, symbol: int, modifiers: int):
        pass

def main():
    platformer = Platformer()
    platformer.setup()
    arcade.run()


if __name__ == "__main__":
    main()
