# wav2hex

## Overview
wav2hex is a specialized utility designed for converting WAV audio samples into hexadecimal format, optimized for chiptune-based music production, particularly for use with hUGETracker. This tool facilitates the integration of custom waveforms into retro-style music compositions.

## Features
- Converts 8-bit mono WAV files to 32x16 hexadecimal waveform grids
- Customizable grid size (with considerations for sample bitrate)
- Optimized for short samples (1-4 seconds)
- Outputs hex data formatted for direct use in chiptune trackers

## Technical Specifications

### Input Requirements
- File Format: 8-bit mono WAV
- Recommended Duration: ≤ 4 seconds (optimal: ≤ 1 second)
- Input Directory: Place WAV files in the included "input" folder

### Output
- 32x16 hexadecimal waveform grid
- Formatted hex string with leading zeros omitted (except where necessary)

### Customization
The program can be modified to support larger waveform grids (up to 32x32), with corresponding adjustments to sample bitrate processing.

## Dependencies
- Python 3.x
- NumPy
- Standard Python libraries: wave, os, glob

### Installation
Install NumPy using pip:
```
pip install -U numpy
```

## Usage
1. Place WAV file(s) in the "input" folder
2. Run the script
3. Hexadecimal output will be displayed, formatted for chiptune tracker use
4. Press any key to close the program after reviewing the output

## Advanced Configuration
To obtain the full hexadecimal representation, including leading zeros, modify the following line in the script:

From:
```python
hex_representation = ''.join(f'{value:02X}'[1] for value in processed_waveform)
```
To:
```python
hex_representation = ''.join(f'{value:02X}' for value in processed_waveform)
```

## Limitations
- Processes only 8-bit mono WAV files
- Optimized for short samples (≤ 4 seconds)
- Fixed 32x16 waveform grid in default configuration

## Future Development
- Support for additional input formats
- Dynamic grid size adjustment based on input parameters
- Integration with popular chiptune composition software

---

For issues, feature requests, or contributions, please open an issue or pull request on the GitHub repository.
