def main():
    
    months="JanFebMarAprMayJunJulAugSepOctNoveDec"
    
    n=int(input("Enter a month number (1-12): "))
    
    pos=(n-1)*3
    
    monthAbbrev=months[pos:pos+3]
    
    print("The month abbreviation is", monthAbbrev + ".")
    
main()