import arcade

SCREEN_WIDTH = 1250
SCREEN_HEICHT = 600

CHARACTER_SCALLING = 1
TILE_SCALING = 0.5
PLAYER_MOVEMENT_SPEED = 5
GRAViTY = 5
PLAYER_JUMP_SPEED = 40

class Box(arcade.Sprite):
    def __init__(self):
        super().__init__(":resources:images/tiles/grassHalf_mid.png", TILE_SCALING)
        self.change_y = 2

    def update(self):
        self.center_y += self.change_y
        if self.top >= 500:
            self.change_y = -self.change_y
        elif self.bottom <= 64:
            self.change_y = -self.change_y


class Player(arcade.Sprite):
    def __init__(self):
        super().__init__(":resources:images/enemies/mouse.png", CHARACTER_SCALLING)
        self.center_x = 64
        self.center_y =128

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        self.center_y -= GRAViTY
        if self.center_y <= 128:
            self.center_y = 128
            game.isGround = True



class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=SCREEN_WIDTH, height=SCREEN_HEICHT,title="Работать со спрайтами")
        self.player_sprite = None
        self.player_list = None
        self.ground_list = None
        self.box_list = None
        self.isGround = True

    def setup(self):
      self.player_list = arcade.SpriteList()
      self.player_sprite = Player()
      self.player_list.append(self.player_sprite)
      self.ground_list = arcade.SpriteList(use_spatial_hash=True)
      for x in range(0, 1250, 64):
            ground = arcade.Sprite(":resources:images/tiles/grassMid.png", TILE_SCALING)
            ground.center_x = x
            ground.center_y = 32
            self.ground_list.append(ground)
      self.box_list = arcade.SpriteList(use_spatial_hash=True)
      coordinate_list =[[512, 96], [256, 96], [768, 96]]
      for y in coordinate_list:
          box = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", TILE_SCALING)
          box.position = y
          self.box_list.append(box)
      self.box_platform = Box()
      self.box_platform.position = [650, 96]
      self.box_list.append(self.box_platform)



    def on_draw(self):
        self.clear()
        self.player_list.draw()
        self.ground_list.draw()
        self.box_list.draw()

    def on_key_press(self, key, modifiers):
        if self.isGround:
            if key == arcade.key.UP:
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
                self.isGround = False
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        if key == arcade.key.RIGHT:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP:
            self.player_sprite.change_y = 0
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = 0
        if key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0



    def update(self, delta_time: float):
        self.player_sprite.update()
        self.box_platform.update()

if __name__ == "__main__":
    game = Game()
    game.setup()
    arcade.run()
