bingocard.py - A simple bingo card generator. Requires PIL.
==========================================================

Thanks to Realbridge Consulting Pvt Ltd for sponsoring development

USAGE

  ```python
    # A single US Card - Indigo
    o = USBingoCard( header=90, margin_top=35, margin_left=60, margin_right=65, margin_bottom=100, with_ref_image='templates/75/indigo.jpg', draw_lines=False )
    o.print_card( 'test.png' )

    # A single US Card - Blue
    o = USBingoCard( header=90, margin_top=35, margin_left=60, margin_right=65, margin_bottom=100, with_ref_image='templates/75/blue.jpg', draw_lines=False )
    o.print_card( 'test1.png' )

    # A single US Card - Without template
    o = USBingoCard(  )
    o.print_card( 'test2.png' )

    # 4 US Cards - Red
    o = USBingoCard( header=90, margin_top=35, margin_left=60, margin_right=65, margin_bottom=100, with_ref_image='templates/75/red.jpg', draw_lines=False )
    BingoCard.draw_several_cards( o, how_many=4, save_to='test3.png', cols_per_image=2 )

    # 6 US Cards - Yellow
    o = USBingoCard( header=90, margin_top=35, margin_left=60, margin_right=65, margin_bottom=100, with_ref_image='templates/75/yellow.jpg', draw_lines=False )
    BingoCard.draw_several_cards( o, how_many=6, save_to='test4.png', cols_per_image=3 )

    # A Single UK Card - Indigo
    o = UKBingoCard( header=50, margin_top=40, margin_left=35, margin_right=38, margin_bottom=42, with_ref_image='templates/90/1/indigo.jpg', draw_lines=False)
    o.print_card( 'test5.png' )

    # A Single UK Card - Blue
    o = UKBingoCard( header=50, margin_top=40, margin_left=35, margin_right=38, margin_bottom=42, with_ref_image='templates/90/1/blue.jpg', draw_lines=False)
    o.print_card( 'test5.png' )

    # A Single UK Card - Without template
    o = UKBingoCard()
    o.print_card( 'test6.png' )

    # A Six Set of individual cards, no unique numbers in a column - Yellow
    o = UKBingoCard( header=50, margin_top=40, margin_left=35, margin_right=38, margin_bottom=42, with_ref_image='templates/90/1/yellow.jpg', draw_lines=False)
    BingoCard.draw_several_cards( o, how_many=6, cols_per_image=1, save_to='test7.png' )


    # A Six-set UK Bingo card with unique numbers in columns - Red
    o = UKBingoCard( set_size=6, set_gap=62.5, set_length=3, header=62.5, margin_top=1, margin_left=100, margin_right=105, margin_bottom=75, with_ref_image='templates/90/6/red.jpg', draw_lines=False)
    o.print_card( 'test8.png' )


    # A Six-set UK Bingo card with unique numbers in columns - Violet - Printed Several times
    o = UKBingoCard( set_size=6, set_gap=62.5, set_length=3, header=62.5, margin_top=1, margin_left=100, margin_right=105, margin_bottom=75, with_ref_image='templates/90/6/violet.jpg', draw_lines=False)
    BingoCard.draw_several_cards( o, how_many=6, cols_per_image=1, save_to='test9.png' )

  ```


bingocard.py exports three classes ```BingoCard```, ```USBingoCard``` and ```UKBingoCard```. ```BingoCard``` is meant to be an abstract superclass
that really does the bulk of the drawing work. ```USBingoCard``` and ```UKBingoCard``` data for generating cards.


These classes are  by no means perfect or the most efficient, but they do a good job at generating correct games. 










  



  


