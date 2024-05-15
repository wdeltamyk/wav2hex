import wave
import numpy as np
import os
import glob

input_folder = "input"

def process_waveform(waveform, max_height=16, max_width=32):
    # Resample the waveform to fit the max width
    resampled_waveform = np.interp(
        np.linspace(0, len(waveform), max_width),
        np.arange(len(waveform)),
        waveform
    )
    
    # Normalize the waveform to fit the max height (4-bit range)
    min_val, max_val = np.min(resampled_waveform), np.max(resampled_waveform)
    normalized_waveform = (resampled_waveform - min_val) / (max_val - min_val) * (max_height - 1)
    
    # Quantize the waveform to integer values
    quantized_waveform = np.round(normalized_waveform).astype(np.uint8)
    
    return quantized_waveform

def wav_to_hex(filename, max_height=16, max_width=32):
    # Open the WAV file
    with wave.open(filename, 'rb') as wav_file:
        # Ensure the file is in the correct format
        if wav_file.getsampwidth() != 1 or wav_file.getnchannels() != 1:
            raise ValueError("WAV file must be 8-bit and mono")

        # Read the waveform data
        frames = wav_file.readframes(wav_file.getnframes())
        waveform = np.frombuffer(frames, dtype=np.uint8)

    # Process the waveform to fit the restrictions
    processed_waveform = process_waveform(waveform, max_height, max_width)

    # Convert the processed waveform data to hexadecimal and extract only the second digit of each byte
    hex_representation = ''.join(f'{value:02X}'[1] for value in processed_waveform)

    return hex_representation

# Get the path to the "input" folder
input_path = os.path.join(os.path.dirname(__file__), input_folder)

# Find all .wav files in the "input" folder
wav_files = glob.glob(os.path.join(input_path, '*.wav'))

# Process each .wav file
for wav_file in wav_files:
    hex_representation = wav_to_hex(wav_file)
    print(f'Hex representation for {os.path.basename(wav_file)}:\n{hex_representation}\n')

# Wait for user input before closing
input("Press enter key to exit...")
exit
