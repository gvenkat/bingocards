bingocard.py - A simple bingo card generator. Requires PIL.
==========================================================

Thanks to Realbridge Consulting Pvt Ltd for sposoring development

USAGE

  ```python
    card = BingoCard( width=300, height=200 )
    card.print_card( 'foo.png' )
  ```

Constructor takes following arguments

  * t - Card type accepts one of 75, 90, 'us', 'uk'
       'us' and '75' are synonymous as are 'uk' and '90'
       determines whether a 75-ball / 90-ball bingo 
       card is printed

  * width           - Width of the image to be generated
  * height          - Height of the image to be generated
  * margin          - Margin to use, this will apply to all four sides
  * with_ref_image  - If path of an image is give, the cards will be drawn on this image
  * background      - If no 'with_ref_image' is set, this background is applied to the new image
  * header          - space to be left out of top

Apart from this, you can tweak followin properties before printing the card
  
  * font            - Path to the truetypefont 
  * line_size       - size of the lines that are drawn
  * line_color      - line color
  * text_size       - text size
  * text_color      - text color



  



  


