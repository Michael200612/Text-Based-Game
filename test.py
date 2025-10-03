                if item == 'sword' and room.room == 'maze':
                    printdelay("""You slowly take the sword from the skeletons hand, trying your best not to disturb his peace.
You notice two small holes engraved on his wrist bone, like he was bitten by an animal.
A snake reveals itself from the hedges of the maze, hissing at you and approaching you with speed.""",3)
                    if fight('snake',p1,room):
                        printdelay('You rest for a while after the intense battle, and try to regain your strength.',1)
                        p1.heal('bread')
                        continue
                    printdelay("""The snake slithers away from your lifeless body, triumphant.
A magical fairy appears from thin air and revives you.
'How could you die to the first enemy?', it asks.
It flies away""",2)
                    p1.heal('health potion')