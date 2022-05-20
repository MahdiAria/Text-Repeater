while(True):
    
    import pyfiglet

    from colorama import Fore, Back, Style

    Banner = pyfiglet.figlet_format("Text Repeater", font= "slant")
    
    print(Fore.RESET, (Banner))
    
    Text = input("Enter Your Text : ")
    
    print("\n")

    Repeat = (input("Chand Bar Tekrar Beshe : 100 : 1000 : 10000 : 100000 : "))
    
    if Repeat == "100":
        
        repeat = Text * 100
        
    elif Repeat == "1000":
        
        repeat = Text * 1000
            
    elif Repeat == "10000":
        
        repeat = Text * 10000    
            
    elif Repeat == "100000":
        
        repeat = Text * 100000    
            
    else:
        
        print("\n")
        
        print("Dorost Vared Konid")
        
        continue

    print("\n")
    
    Chap = input("Chap She : y/n : ")
    
    if Chap == "y" or Chap == "yes":
        
        print(repeat)
        
        continue
        
    elif Chap == "n" or Chap == "no":
        
        print(" [ Good Bye ] ")
        
        break 
