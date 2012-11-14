
from PIL import Image, ImageDraw, ImageFont, _imaging
import random, sys, os


class BingoCard( object ):


  @classmethod
  def draw_several_cards( self, card, how_many=6, save_to=None, cols_per_image=3, background='white' ):

    if card.image is None:
      card.initialize_image()

    image = card.image
    t     = card.type

    rows = ( ( how_many - 1 ) // cols_per_image ) + 1

    if how_many >= cols_per_image:
      cols = cols_per_image
    else:
      cols = how_many

    iw, ih, w, h = card.width, card.height, card.width * cols, card.height * rows 
    nimage = Image.new( 'RGB', ( w, h ), background )

    for row in range( rows ): 
      for col in range( cols ):
        embed_image = card.print_card( save_to=None )
        nimage.paste( embed_image, ( col * iw, row * ih ) ) 


    if save_to is None:
      return nimage
    else: 
      return nimage.save( save_to )




  def __init__( self, t=90, width=800, height=600, header=10, margin_top=10, margin_left=10, margin_right=10, margin_bottom=10, margin=None, with_ref_image=None, background='white', draw_lines=True ):
    self.type   = t
    self.width  = width
    self.height = height
    self.header = header
    self.with_ref_image = with_ref_image
    self.background = background
    self.font = 'Overlock-Black.ttf'
    self.draw_lines = draw_lines
    self.line_size  = 2
    self.line_color = 0
    self.text_size = None
    self.text_color = 0
    self.image  = None

    if margin is None and ( margin_left > 0 and margin_right > 0 and margin_bottom > 0 and margin_top > 0 ):
      self.margin_left    = margin_left 
      self.margin_right   = margin_right
      self.margin_bottom  = margin_bottom
      self.margin_top     = margin_top
    else:
      margin = margin or 10
      self.margin_top = self.margin_left = self.margin_right = self.margin_bottom = margin 
      

  def uk_card_layout( self ):
    return [
      range( 1, 9 ),
      range( 10, 19 ),
      range( 20, 29 ),
      range( 30, 39 ),
      range( 40, 49 ),
      range( 50, 59 ),
      range( 60, 69 ),
      range( 70, 79 ),
      range( 80, 90 )
    ]


  def us_card_layout( self ):
    return [ range( i, i + 15 ) for i in range( 1, 75, 15 ) ]


  def get_text_size( self ):
    if self.text_size is None:
      text_size = int( self.width / 38.4 )
    else:
      text_size	= self.text_size

    return text_size


  def get_font( self ):
    return ImageFont.truetype( self.font, self.get_text_size() )


  def get_top( self ):
    if self.header:
      top = ( self.header ) + self.margin_top
    else:
      top = self.margin_top

    return top

  def draw_lines_on_image( self, layout, col_height, col_width ):
    if self.draw_lines:
      # Rows
      for i in range( len( layout ) + 1 ):
        y = ( self.get_top() + ( i * col_height ) )
        draw.line( ( self.margin_left, y, self.width - self.margin_right, y ), fill=self.line_color, width=self.line_size  )

      # Cols
      for j in range( len( layout[ 0 ] ) + 1 ):
        x = self.margin_left + ( j * col_width )
        draw.line( ( x, self.get_top(), x, self.height - self.margin_bottom ), fill=self.line_color, width=self.line_color )



  def draw( self, layout, save_to ):
    print "About to draw"

    image, width, height = self.image, self.width, self.height
    font, text_size, top = self.get_font(), self.get_text_size(), self.get_top()
    ml, mr, mt, mb = self.margin_left, self.margin_right, self.margin_top, self.margin_bottom

    draw        = ImageDraw.Draw( image )
    col_height  = ( height - top - mb ) / len( layout )
    col_width   = ( width - ( ml + mr ) ) / len( layout[ 0 ] )

    self.draw_lines_on_image( layout, col_height, col_width )

    # Start drawing numbers
    for i in range( len( layout ) ):
      for j in range( len( layout[0] ) ):
        number = layout[ i ][ j ]

        x = ml + ( j * col_width ) + ( col_width / 2 ) - ( text_size / 2 )
        y = top + ( i * col_height ) + ( col_height / 2 ) - ( text_size / 2 )

        if number is not None:
          draw.text( ( x, y ), str( number ), fill=0, font=font )


    print "OK"

    # Save stuff
    if save_to is None:
      return image
    else:
      image.save( save_to )






  def uk_bingo_card( self ):
    layout             = self.uk_card_layout()
    num_of_rows           = 3
    cols                  = len( self.uk_card_layout() )
    blanks                = [ ]

    for i in range( num_of_rows ):

      row = [
        layout[ j ][ random.randint( 0, len( layout[ j ] ) - 1 ) ] for j in range( cols )
      ]

      while len( filter( lambda x: x is None, row ) ) < 4:
        row[ random.randint( 0, len( row ) - 1 ) ] = None

      blanks.append( row )


    return blanks


  def us_bingo_card( self ):
    layout   = self.us_card_layout()
    num_of_rows = 5
    cols        = 5
    blanks      = [ ]

    for i in range( num_of_rows ):
      row = [
        layout[ j ][ random.randint( 0, len( layout[ j ] ) - 1 ) ] for j in range( cols )
      ]

      blanks.append( row )

    blanks[ 2 ][ 2 ] = None

    return blanks


  def initialize_image( self ):

    if( self.with_ref_image ):
      self.image = im = Image.open( self.with_ref_image )
      self.width, self.height = im.size
    else:
      self.image  = Image.new( 'RGB', ( self.width, self.height ), self.background )



  def print_card( self, save_to='test.png' ):

    self.initialize_image()

    if self.type in [ 90, 'uk' ]:
      return self.draw( self.uk_bingo_card(), save_to )

    elif self.type in [ 75, 'us' ]:
      return self.draw( self.us_bingo_card(), save_to )




if __name__ == '__main__':

  # o = BingoCard( t='us', header=90, margin_top=35, margin_left=60, margin_right=65, margin_bottom=100, with_ref_image='templates/75/indigo.jpg', draw_lines=False )
  # o.print_card( 'us_bingo2.png' )

  o = BingoCard( t='uk', header=50, margin_top=40, margin_left=35, margin_right=38, margin_bottom=42, with_ref_image='templates/90/indigo.jpg', draw_lines=False )
  BingoCard.draw_several_cards( o, how_many=6, save_to='uk_bingo2.png', cols_per_image=1, background='white' ) 



