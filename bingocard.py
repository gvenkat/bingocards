
from PIL import Image, ImageDraw, ImageFont, _imaging
import random, sys, os


class BingoCard( object ):

  def __init__( self, t=90, width=800, height=600, header=10, margin=10, with_ref_image=None, background='white' ):
    self.type   = t
    self.width  = width
    self.height = height
    self.header = header
    self.with_ref_image = with_ref_image
    self.background = background
    self.font = 'Overlock-Black.ttf'
    self.line_size  = 2
    self.line_color = 0
    self.text_size = None
    self.text_color = 0
    self.margin	= 10

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
    return [
      range( 1, 15 ),
      range( 16, 30 ),
      range( 31, 45 ),
      range( 46, 60 ),
      range( 61, 75 )
    ]


  def draw( self, layout, save_to ):
    image, width, height = self.image, self.width, self.height

    if self.text_size is None:
      text_size = int( width / 38.4 )
    else:
      text_size	= self.text_size

    font = ImageFont.truetype( self.font, text_size )

    # FIXME: Needs to be configurable
    margin  = self.margin

    if self.header:
      top = ( self.header ) + margin
    else:
      top = margin

    draw        = ImageDraw.Draw( image )
    col_height  = ( height - top - margin ) / len( layout )
    col_width   = ( width - ( 2 * margin ) ) / len( layout[ 0 ] )

    # Rows
    for i in range( len( layout ) + 1 ):
      y = ( top + ( i * col_height ) )
      draw.line( ( margin, y, width - margin, y ), fill=self.line_color, width=self.line_size  )

    # Cols
    for j in range( len( layout[ 0 ] ) + 1 ):
      x = margin + ( j * col_width )
      draw.line( ( x, top, x, height - margin ), fill=self.line_color, width=self.line_color )



    # Start drawing numbers
    for i in range( len( layout ) ):
      for j in range( len( layout[0] ) ):
        number = layout[ i ][ j ]

        x = margin + ( j * col_width ) + ( col_width / 2 ) - ( text_size / 2 )
        y = top + ( i * col_height ) + ( col_height / 2 ) - ( text_size / 2 )

        if number is not None:
          draw.text( ( x, y ), str( number ), fill=0, font=font )


    # Save stuff
    image.save( save_to )


    print "About to draw"


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

    for x in [ 0, 1, 2, 3, 4 ]:
      if random.randint( 0, 4 ) > 0:
        index = -1

        while index < 0 or index == 2 or blanks[ x ][ index ] is None:
          index = random.randint( 0, len( blanks[ x ] ) - 1 );

        blanks[ x ][ index ] = None


    return blanks



  def print_card( self, save_to='test.png' ):

    if( self.with_ref_image ):
      self.image = im = Image.open( self.with_ref_image )
      self.width, self.height = im.size

    else:
      self.image  = Image.new( 'RGB', ( self.width, self.height ), self.background )


    if self.type in [ 90, 'uk' ]:
      self.draw( self.uk_bingo_card(), save_to )

    elif self.type in [ 75, 'us' ]:
      self.draw( self.us_bingo_card(), save_to )




if __name__ == '__main__':

  o = BingoCard( header=85 )
  print o.print_card( 'uk_bingo2.png' )

  o = BingoCard( t='us', header=120 )
  print o.print_card( 'us_bingo2.png' )

