from guitar import Guitar

def main():

    guitar1 = Guitar("Fender Stratocaster",1923,765.4)
    print ('guitar1.get_age() - Expected 93. Got {}'.format(guitar1.get_age()))
    print ('guitar1.is_vintage - Expected True. Got {}'.format(guitar1.is_vintage()))

    print('')

    guitar2 = Guitar("Fender Stratocaster",1967,765.4)
    print ('guitar2.get_age() - Expected 49. Got {}'.format(guitar2.get_age()))
    print ('guitar2.is_vintage - Expected False. Got {}'.format(guitar2.is_vintage()))

    # testing out the float value cost.
    
    # Works!!
        #print (guitar2.cost)


    #   print('{:.2f}'.format(guitar2.cost))




main()
