T = int(input())
for i in range(T):
    recording = list( input().split() )
    setOfKnownSounds = set()
    s = input()
    foxsays = []
    while s != "what does the fox say?":
        animalgoessound = list(s.split())
        setOfKnownSounds.add(animalgoessound[2])
        s = input()
    for sound in recording:
        if sound not in setOfKnownSounds:
            foxsays.append(sound)

    print( ' '.join(foxsays) )