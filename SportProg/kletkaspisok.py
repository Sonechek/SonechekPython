n = input()
white = ["A2", "A4", "A6", "A8", "B1", "B3", "B5", "B7", "C2", "C4", "C6", "C8", "D1", "D3",
 "D5", "D7", "E2", "E4", "E6", "E8", "F1", "F3", "F5", "F7", "G2", "G4", "G6", "G8", "H1", "H3", "H5", "H7"]

if n in white:
    print('WHITE')
else:
    print('BLACK')