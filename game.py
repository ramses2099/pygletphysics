import pyglet
from pyglet.window.key import *
from constants import *

class Game(pyglet.window.Window):
    def __init__(self):
      super().__init__(width=WIDTH, height=HEIGHT, caption=TITLE, resizable=False)

      self.counter = 0
      
      self.score_draw = False
      self.score_now = self.score_best = 0
      self.fps_draw = False
      self.help_draw = False
      
      self.score_now_label = pyglet.text.Label()
      self.score_best_label = pyglet.text.Label(anchor_x = RIGHT)
      self.inf_label = None
      self.fps_label = pyglet.text.Label(anchor_x = CENTER)
      self.help_label = pyglet.text.Label(anchor_x= CENTER, anchor_y= CENTER)
      self.pause_lable = pyglet.text.Label(anchor_x= CENTER, anchor_y= CENTER)
      
      self.pause = False
      self.key_state = self.key_state_old = set()
      self.movers = []
      
      self.start = None
      self.background = None
      self.text_color = None
      self.text_font_name = None
      
      # resource
      pyglet.resource.path = [os.path.join(WORKINGDIR,'./assets/images')]
      pyglet.resource.reindex()

      # batch
      self.batch = pyglet.graphics.Batch()
      
    def on_draw(self):
        #   pyglet.gl.glClear(*background, 1)
        self.clear()
        self.batch()
               
        if self.score_draw:
            snl = self.score_now_label
            snl.text = f'Score {self.score_now:08d}'
            snl.font_size = HEIGHT//30
            snl.draw()
            
            sbl = self.score_best_label
            sbl.text = f'Best {self.score_best:08d}'
            sbl.font_size = HEIGHT//30
            sbl.x = WIDTH
            sbl.draw()
            
        if self.fps_draw:
            fl = self.fps_label
            fl.text = f'{pyglet.clock.get_frequency():.1f} FPS'
            fl.x = WIDTH//2
            fl.draw()
            
        if self.help_draw:
            hl = self.help_label
            hl.text ='Key "H" Showing Help\nCursor Keys: Moving\nKey "Z": Shot\nKey "C": Homing Missile\nKey "Backspace": Restart'
            hl.font_name='Tahoma'
            hl.font_size=28
            hl.width=WIDTH//1.5
            hl.height=HEIGHT//1.5
            hl.x=WIDTH//2
            hl.y=HEIGHT//2
            hl.multiline=True
            hl.draw()
            
        if self.pause:
          pl = self.pause_lable
          pl.text = f'PAUSE'
          pl.font_size = 36
          pl.x = WIDTH//2
          pl.y = HEIGHT//2
          pl.draw()
          
    def on_key_press(self, symbol, modifiers):
      self.key_state.add(symbol)
           
    def on_key_release(self, symbol, modifiers):
       self.key_state.discard(symbol)
       
    def key(self, k ):
      return k in self.key_state
    
    def key_old(self, k):
      return k in self.key_state_old
    
    def score(self, s=0):
      self.score_draw = True
      self.score_now = max(0, self.score_now+s)
      self.score_best = max(self.score_now, self.score_best)
      return self.score_now
    
    def start(self):
      pass
    # move_objects
    def update(self, dt):
      if self.key( ESCAPE):
        pyglet.app.exit()        
      
      if self.key( BACKSPACE):
        self.score_now = 0
        self.movers.clear()
        self.start()
        
      if self.key( F ) and not self.key_old( F ):
        self.fps_draw = not self.fps_draw
        
      if self.key( S ) and not self.key_old ( S ):
        self.pause = not self.pause
        
      if self.key( H ) and not self.key_old( H ):
        self.help_draw = not self.help_draw
        
      self.key_state_old = self.key_state.copy()
      
    def run(self, bg=(1,1,1), fs=False, tc=(0.5, 0.5, 0.5), tfn ='Broadway'):      
      # self.background = bg
      # snl, sbl, fl, pl = self.score_now_label, self.score_best_label, self.fps_label, self.pause_lable
      # snl.color = sbl.color = fl.color = pl.color = int(255*tc[0]), int(255*tc[1]), int(255*tc[2]), 255
      # snl.font_name = sbl.font_name = fl.font_name = pl.font_name = tfn
      
      print(WORKINGDIR)
      
      # self.start()
       # init app
      pyglet.clock.schedule_interval(self.update, FPS)
      pyglet.app.run()
      
      