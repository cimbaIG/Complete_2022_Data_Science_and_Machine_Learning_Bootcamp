def sing(num_bottles):
    #TODO: Add your code to achieve the desired output and pass the challenge. 
    #NOTE: The f String method of String Interpolation does not work

    lyrics = []
    for n in range(num_bottles, 0, -1):
        lyrics.append(f"{n} bottles of beer on the wall, {n} bottles of beer.")
        lyrics.append(f"Take one down and pass it around, {n - 1} bottles of beer on the wall.")

    print(lyrics)

sing(99)