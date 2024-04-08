# An implementation of mix (may or may not be "optimal" and may or may not have bugs)

# 1. Original implementation
# def mix(sound1, sound2, p):
#     # initialize a new sound
#     new_sound = {}
    
#     # scale the input sounds by p and 1-p
#     sound1_scaled = []
#     for s in sound1["samples"]:
#         sound1_scaled.append(s * p)
    
#     sound2_scaled = []
#     for s in sound1["samples"]:         #> Bug (should be sound2)
#         sound2_scaled.append(s * 1-p)   #> Bug (use (1-p))
    
#     # combine the scaled sounds
#     if len(sound1_scaled) > len(sound2_scaled):
#         new_length = len(sound2_scaled)
#     else:
#         new_length = len(sound1_scaled)
    
#     new_samples = [0] * new_length
#     for i in range(new_length):
#         new_samples[i] = sound1_scaled[i] + sound2_scaled[i]
    
#     # fill in the new sound with the new samples
#     new_sound["rate"] = sound["rate"]   #> Bug (sound is not defined)
    
#     new_sound["samples"] = []
#     for sample in new_samples:
#         new_sound["samples"].append(sample)
    
#     # return the mixed sound
#     return new_sound


# 2. Implementation with bugs fixed
def mix(sound1, sound2, p):
    # initialize a new sound
    new_sound = {}
    
    # scale the input sounds by p and 1-p
    sound1_scaled = []
    for s in sound1["samples"]:
        sound1_scaled.append(s * p)
    
    sound2_scaled = []
    for s in sound2["samples"]:
        sound2_scaled.append(s * (1-p))
    
    # combine the scaled sounds
    if len(sound1_scaled) > len(sound2_scaled):
        new_length = len(sound2_scaled)
    else:
        new_length = len(sound1_scaled)
    
    new_samples = [0] * new_length
    for i in range(new_length):
        new_samples[i] = sound1_scaled[i] + sound2_scaled[i]
    
    # fill in the new sound with the new samples
    assert sound1["rate"] == sound2["rate"]
    new_sound["rate"] = sound1["rate"] 
    
    new_sound["samples"] = []
    for sample in new_samples:
        new_sound["samples"].append(sample)
    
    # return the mixed sound
    return new_sound

sound1 = {"rate": 10, "samples": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
sound2 = {"rate": 10, "samples": [10, 20, 30, 40, 50, 60, 70]}

print(sound1)
print(sound2)
print(mix(sound1, sound2, 0.5))
print(sound1)
print(sound2)