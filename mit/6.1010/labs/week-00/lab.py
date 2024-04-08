"""
6.101 Lab 0:
Audio Processing
"""

import wave
import struct

# Imported for type hinting only
from typing import TypedDict, List

# No Additional Imports Allowed!

class SoundMono(TypedDict):
    rate: int
    samples: list[int]

class SoundStereo(TypedDict):
    rate: int
    left: list[int]
    right: list[int]


def backwards(sound: SoundMono) -> SoundMono:
    """
    Returns a new mono sound containing the samples of the original in reverse
    order, without modifying the input sound.

    Args:
        sound (SoundMono): a dictionary representing the original mono sound

    Returns:
        SoundMono: A new mono sound dictionary with the samples in reversed order
    """
    #> Error check: make sure sound is in the correct representation
    if ("rate" not in sound) or ("samples" not in sound):
        print("Argument `sound` is not in the correct representation.")
        return None
    
    return {"rate": sound["rate"], "samples": sound["samples"][::-1]}


def mix(sound1: SoundMono, sound2: SoundMono, p: int) -> SoundMono:
    """
    Returns a new mono sound containing the samples from each of the original
    two samples mixed together with mixing parameter `p`. 

    Args:
        sound1 (SoundMono): a dictionary representing the first original mono sound
        sound2 (SoundMono): a dictionary representing the second original mono sound
        p (int): the mixing parameter (p * sound1 + (1-p) * sound2)

    Returns:
        Sound: a dictionary representing the mixed sound
    """
    #> Error check: make sure sounds are in the correct representation
    if ("rate" not in sound1) or ("samples" not in sound1):
        print("Argument `sound1` is not in the correct representation.")
        return None 

    if ("rate" not in sound2) or ("samples" not in sound2):
        print("Argument `sound2` is not in the correct representation.")
        return None
    
    #> Error check: the two sounds should have the sampe sampling rates
    if sound1["rate"] != sound2["rate"]:
        print("Arguments `sound1` and `sound2` must have the same error rates.")
        return None
    
    rate = sound1["rate"]
    samples1 = [(sample * p) for sample in sound1["samples"]]
    samples2 = [(sample * (1-p)) for sample in sound2["samples"]]
    
    samp1_len = len(samples1)
    samp2_len = len(samples2)
    
    new_samples = [0] * max(samp1_len, samp2_len)
    
    for i in range(samp1_len):
        new_samples[i] += samples1[i]
    
    for i in range(samp2_len):
        new_samples[i] += samples2[i]
    
    return {"rate": rate, "samples": new_samples}


def convolve(sound: SoundMono, kernel: List) -> SoundMono:
    """
    Returns a new mono sound that has undergone convolution
    with the applied filter.

    Args:
        sound (SoundMono): a dictionary representing a mono sound
        kernel (List): a separate list of samples

    Returns:
        SoundMono: a dictionary representing the sound after convolution
    """
    rate = sound["rate"]
    samples = sound["samples"]
    
    samples_len = len(samples)
    kernel_len = len(kernel)
    
    out = [0] * (samples_len + kernel_len - 1)
    for i in range(kernel_len):
        step = [0] * i
        
        for j in range(samples_len):
            step.append(kernel[i] * samples[j])
        
        for k in range(len(step)):
            out[k] += step[k]

    return {"rate": rate, "samples": out}


def echo(sound: SoundMono, num_echoes: int, delay: float, scale: float) -> SoundMono:
    """
    Returns a new mono sound that has had an echo effect applied to it.

    Args:
        sound (SoundMono): a dictionary representing a mono sound
        num_echoes (int): the number of echoes to apply
        delay (float): the number of seconds to delay each echo
        scale (float): the amount to scale down each echo (0.0 - 1.0)

    Returns:
        SoundMono: a dictionary representing the sound after echoes are applied
    """
    sample_delay = round(delay * sound["rate"])
    
    kernel = [0] * ((num_echoes * sample_delay) + 1)
    kernel[0] = 1
    
    for i in range(num_echoes):
        echo_num = i + 1
        kernel[sample_delay * echo_num] = scale ** echo_num
    
    return convolve(sound, kernel)


def pan(sound: SoundStereo) -> SoundStereo:
    """
    Returns a new stereo sound that is panned from left to right.

    Args:
        sound (SoundStereo): a dictionary representing a stereo sound

    Returns:
        SoundStereo: a dictionary representing the stereo sound after panning is applied
    """
    samp_l = sound["left"]
    samp_r = sound["right"]
    
    if (len(samp_l) != len(samp_r)):
        print("Length of channel samples is not the same.")
        return None

    num_samp = len(samp_l)
    
    samp_l_new = []
    samp_r_new = []
    for i in range(num_samp):
        weight = i / (num_samp - 1)
        
        samp_l_new.append(samp_l[i] * (1 - weight))
        samp_r_new.append(samp_r[i] * weight)
    
    return {"rate": sound["rate"], "left": samp_l_new, "right": samp_r_new}


def remove_vocals(sound: SoundStereo) -> SoundStereo:
    """
    Returns a new stereo sound that has the vocals removed.

    Args:
        sound (SoundStereo): a dictionary representing a stereo sound

    Returns:
        SoundStereo: a dictionary representing the stereo sound after the vocals are removed
    """
    samp_l = sound["left"]
    samp_r = sound["right"]
    
    if len(samp_l) != len(samp_r):
        print("Samples in left and right channels are not the same length.")
        return None
    
    new_samples = []
    for i in range(len(samp_l)):
        samp = samp_l[i] - samp_r[i]
        new_samples.append(samp)
    
    return {"rate": sound["rate"], "samples": new_samples}


def bass_boost_kernel(n_val, scale=0):
    """
    Construct a kernel that acts as a bass-boost filter.

    We start by making a low-pass filter, whose frequency response is given by
    (1/2 + 1/2cos(Omega)) ^ n_val

    Then we scale that piece up and add a copy of the original signal back in.
    """
    # make this a fake "sound" so that we can use the convolve function
    base = {"rate": 0, "samples": [0.25, 0.5, 0.25]}
    kernel = {"rate": 0, "samples": [0.25, 0.5, 0.25]}
    for i in range(n_val):
        kernel = convolve(kernel, base["samples"])
    kernel = kernel["samples"]

    # at this point, the kernel will be acting as a low-pass filter, so we
    # scale up the values by the given scale, and add in a value in the middle
    # to get a (delayed) copy of the original
    kernel = [i * scale for i in kernel]
    kernel[len(kernel) // 2] += 1

    return kernel


# below are helper functions for converting back-and-forth between WAV files
# and our internal dictionary representation for sounds


def load_wav(filename, stereo=False):
    """
    Given the filename of a WAV file, load the data from that file and return a
    Python dictionary representing that sound
    """
    file = wave.open(filename, "r")
    chan, bd, sr, count, _, _ = file.getparams()

    assert bd == 2, "only 16-bit WAV files are supported"

    out = {"rate": sr}

    if stereo:
        left = []
        right = []
        for i in range(count):
            frame = file.readframes(1)
            if chan == 2:
                left.append(struct.unpack("<h", frame[:2])[0])
                right.append(struct.unpack("<h", frame[2:])[0])
            else:
                datum = struct.unpack("<h", frame)[0]
                left.append(datum)
                right.append(datum)

        out["left"] = [i / (2**15) for i in left]
        out["right"] = [i / (2**15) for i in right]
    else:
        samples = []
        for i in range(count):
            frame = file.readframes(1)
            if chan == 2:
                left = struct.unpack("<h", frame[:2])[0]
                right = struct.unpack("<h", frame[2:])[0]
                samples.append((left + right) / 2)
            else:
                datum = struct.unpack("<h", frame)[0]
                samples.append(datum)

        out["samples"] = [i / (2**15) for i in samples]

    return out


def write_wav(sound, filename):
    """
    Given a dictionary representing a sound, and a filename, convert the given
    sound into WAV format and save it as a file with the given filename (which
    can then be opened by most audio players)
    """
    outfile = wave.open(filename, "w")

    if "samples" in sound:
        # mono file
        outfile.setparams((1, 2, sound["rate"], 0, "NONE", "not compressed"))
        out = [int(max(-1, min(1, v)) * (2**15 - 1)) for v in sound["samples"]]
    else:
        # stereo
        outfile.setparams((2, 2, sound["rate"], 0, "NONE", "not compressed"))
        out = []
        for left, right in zip(sound["left"], sound["right"]):
            left = int(max(-1, min(1, left)) * (2**15 - 1))
            right = int(max(-1, min(1, right)) * (2**15 - 1))
            out.append(left)
            out.append(right)

    outfile.writeframes(b"".join(struct.pack("<h", frame) for frame in out))
    outfile.close()


if __name__ == "__main__":
    # code in this block will only be run when you explicitly run your script,
    # and not when the tests are being run.  this is a good place to put your
    # code for generating and saving sounds, or any other code you write for
    # testing, etc.
    
    # 5. Manipulations
    
    # ## 5.1 Backwards
    # mystery = load_wav("sounds/mystery.wav")
    # mystery_backwards = backwards(mystery)
    
    # write_wav(mystery_backwards, "mystery_backwards.wav")
    
    # ## 5.2 Mixing
    # synth = load_wav("sounds/synth.wav")
    # water = load_wav("sounds/water.wav")
    
    # synth_water = mix(synth, water, p=0.2)
    
    # write_wav(synth_water, "synth_water_mixed.wav")
    
    # ## 5.3 Convolutional Filters
    # ice_and_chilli = load_wav("sounds/ice_and_chilli.wav")
    # kernel = bass_boost_kernel(n_val=1000, scale=1.5)
    
    # ice_and_chilli_convolve = convolve(ice_and_chilli, kernel)

    # write_wav(ice_and_chilli_convolve, "ice_and_chilli_convolved.wav")
    
    # ## 5.4 Echo
    # chord = load_wav("sounds/chord.wav")
    # chord_echo = echo(chord, 5, 0.3, 0.6)
    
    # write_wav(chord_echo, "chord-echo.wav")
    
    # 6. Stereo Effects
    
    # ## 6.1 Pan
    # car = load_wav("sounds/car.wav", stereo=True)
    # car_pan = pan(car)
    
    # write_wav(car_pan, "car_pan.wav")
    
    # ## 6.2 Remove Vocals
    # lookout_mountain = load_wav("sounds/lookout_mountain.wav", stereo=True)
    # lookout_mountain_no_vocals = remove_vocals(lookout_mountain)
    
    # write_wav(lookout_mountain_no_vocals, "lookout_mountain_no_vocals.wav")
    
    pass
