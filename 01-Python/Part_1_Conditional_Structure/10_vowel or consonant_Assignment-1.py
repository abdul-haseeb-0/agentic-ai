char = input ("Enter Any Character:")
match char:
    case "a" | "A":
         print (char,"is  a vowel character")
    case "e" | "E":
         print (char,"is  a vowel character")
    case "i" | "I":
         print (char,"is  a vowel character")
    case "o" | "O":
         print (char,"is  a vowel character")
    case "u" | "U":
         print (char,"is  a vowel character")
    case _ :
         print (char,"is  a consonant character")