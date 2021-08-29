import pygame
import utils
import constants as con
import os


x=1050
y=0
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)


class StrangeTeleprompter:
    def __init__(self, filepath, height=500, line_width=50):
        self.filepath = filepath
        self.complete_text = self.get_text()
        self.height = height
        self.width = 410
        self.line_width = line_width
        self.keep_looping = True
        self.timer_state = False
        self.last_timer_state = False
        self.stopwatch=0
        self.line_length = 24
        # --------------------------
        self.BG_COLOR = con.BLACK

        self.TEXT_COLOR = con.YELLOW
        # --------------------------
        self.scroll_up = True
        self.counter = 0
        self.gate_value = 1
        self.counter_increment = 0
        self.pygame_init()
        self._initialize_rectangles()

    def pygame_init(self):
        pygame.init()
        # ---------------------------
        self.clock = pygame.time.Clock()
        self.font_size = 42
        self.font = pygame.font.Font(None, self.font_size)
        self.font_clock = pygame.font.Font(None, 18)
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.NOFRAME)

    def get_text(self):
        with open(self.filepath, "r", encoding='utf-8') as f:
            mylines = f.readlines()
            mylines = [i.strip() for i in mylines if len(i.strip()) > 0]
        mylines = utils.clean_text(mylines)
        return mylines

    def _initialize_rectangles(self):
        top_rectangle_left = 10
        top_rectangle_top = 10
        top_rectangle_width = self.width - 20
        top_rectangle_height = self.height - (20 * 6)
        self.text_rect = pygame.Rect(top_rectangle_left,
                                     top_rectangle_top,
                                     top_rectangle_width,
                                     top_rectangle_height)

    # ---------------------------

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.keep_looping = False
            elif event.type == pygame.KEYDOWN:
                # print(pygame.KEYDOWN)
                if event.key == pygame.K_ESCAPE:
                    self.keep_looping = False
                elif event.key == pygame.K_d:
                    print("Plus +++++++++")
                    # self.gate_value -= 1
                    self.counter_increment += 1
                elif event.key == pygame.K_a:
                    print("Minus ----------")
                    # self.gate_value += 1
                    self.counter_increment -= 1
                elif event.key == pygame.K_w:
                    self.scroll_up = True
                elif event.key == pygame.K_s:
                    self.scroll_up = False
                elif event.key == pygame.K_q:
                    self.counter_increment = 0
                elif event.key == pygame.K_1:
                    self.counter_increment = 1
                elif event.key == pygame.K_2:
                    self.counter_increment = 2
                elif event.key == pygame.K_3:
                    self.counter_increment = 3
                elif event.key == pygame.K_4:
                    self.counter_increment = 4
                elif event.key == pygame.K_e:
                    self.counter = 0
                    self.stopwatch=0
                    self.timer_state = False

    def update(self):
        if self.scroll_up == True:
            self.counter -= self.counter_increment
        else:
            self.counter += self.counter_increment

    def draw_rect_alpha(self, surface, color, rect):
        shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
        pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
        surface.blit(shape_surf, rect)

    def draw_text(self):
        
        utils.talk_dialog(self.screen, self.complete_text, self.font, width_offset=20, height_offset=self.counter, line_length=self.line_length, color=self.TEXT_COLOR)
        self.draw_rect_alpha(self.screen, (0, 0, 0, 150), (0, self.height/5, self.width, 4*(self.height/5)))

    def draw(self):
        self.screen.fill(self.BG_COLOR)
        self.draw_text()
        pygame.display.flip()

    def main(self):
        while self.keep_looping:
            self.clock.tick(10)
            self.events()
            # self.get_timer()
            self.update()
            self.draw()

if __name__ == "__main__":
    # Used for debugging
    filepath = "data/scripts/script_testing.txt"
    teleprompter = StrangeTeleprompter(filepath)
    teleprompter.main()
