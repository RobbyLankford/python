# Different implementations of backwards (may or may not be correctly implemented)

# 1. Version a (not correctly implemented, alters the original sound)
def backwards(sound):
    new_samples = sound["samples"]
    new_samples.reverse()
    
    return {"rate": sound["rate"], "samples": new_samples}

sound = {"rate": 10, "samples": [1, 2, 3, 4, 5, 6, 7, 8]}

print(sound)
print(backwards(sound))
print(sound)
print()


# 2. Version b (not correctly implemented)
# def backwards(sound):
#     samples = []
#     slen = len(sound["samples"])
    
#     for i in range(slen, 0, -1):
#         samples.append(sound["samples"][i])
    
#     return {"rate": sound["rate"], "samples": samples}

# print(sound)
# print(backwards(sound))


# 3. Version c (not correctly implemented)
# def backwards(sound):
#     new_sound = sound.copy()
#     new_sound["samples"].reversed()
    
#     return new_sound

# print(sound)
# print(backwards(sound))


# 4. Version d (correctly implemented)
def backwards(sound):
    return {"rate": sound["rate"], "samples": sound["samples"][::-1]}

sound = {"rate": 10, "samples": [1, 2, 3, 4, 5, 6, 7, 8]}

print(sound)
print(backwards(sound))
print(sound)
print()


# 5. Version e (not implemented correctly, returns an iterator)
def backwards(sound):
    return {"rate": sound["rate"], "samples": {reversed(sound["samples"])}}

sound = {"rate": 10, "samples": [1, 2, 3, 4, 5, 6, 7, 8]}

print(sound)
print(backwards(sound))
print(sound)
print()


# 6. Version f (not implemented correctly, alters original sound)
def backwards(sound):
    return {"rate": sound["rate"], "samples": sound["samples"].reverse()}

print(sound)
print(backwards(sound))
print(sound)