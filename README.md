# The Mostly Harmless Guide to MPU-6050
*DON'T PANIC - It's just a digital motion sensor*

## The Book Says...

Deep in the uncharted backwaters of the unfashionable end of your circuit board sits a small but remarkable chip: the MPU-6050. This amazingly improbable device has the fantastic ability to tell you exactly how you're moving through the local space-time continuum, all while consuming far less power than it takes to make a decent Pan Galactic Gargle Blaster.

For those of you who have been living in a Bugblatter Beast of Traal's cave, this project transforms the mundane act of measuring motion into something almost, but not quite, entirely unlike tea.

## Features That Would Impress Even Slartibartfast

- Real-time motion detection (faster than you can say "So long and thanks for all the fish")
- Web interface so beautiful, it makes the fjords of Norway look dull
- Accelerometer and gyroscope readings more precise than the Infinite Improbability Drive
- Low-pass filtering smoother than a babel fish's translation

## Things You'll Need (Your Electronic Towel)

Like any good hitchhiker knows, preparation is key. You'll need:

## The Improbably Simple Connection Guide

Connect these wires in a way that would make even Deep Thought proud:

| MPU-6050 Pin | Raspberry Pi Pin | What It Does |
|--------------|------------------|--------------|
| VCC          | Pin 1 (3.3V)     | Powers the improbability |
| GND          | Pin 6 (Ground)   | Keeps electrons from floating away |
| SCL          | Pin 5 (GPIO3)    | Times the quantum tea breaks |
| SDA          | Pin 3 (GPIO2)    | Transfers data faster than a Hrung-beast |

## Installation (Don't Forget Your Towel)

To install this mostly harmless program:

## Usage (Share and Enjoy!)

Point your browser to `http://[your-pi-ip]:5001`
(Note: If you see an error message saying "Error 42", that's perfectly normal
and means everything is working exactly as intended)

### Technical Specifications (For Particularly Nerdy Mice)
- Web server runs on port 5001 (chosen by a committee of hyperintelligent pandimensional beings)
- Data sampling rate: 50Hz (fast enough to dodge a Vogon poetry reading)
- Accelerometer range: ±2g (measured in Earth gravity, not Magrathean)
- Gyroscope range: ±250 degrees/second (or 0.0013 parsecs per microfortnight)
- Low-pass filter coefficient: 0.3 (carefully calculated by Deep Thought)
- Data endpoint: `/data` returns JSON (Just Obviously Sorted Numbers)
- Static files served from `/static` (which is relatively static in most dimensions)

## Troubleshooting (When Things Go Infinitely Improbable)

If your sensor starts producing readings that suggest you're simultaneously on Earth and somewhere in the vicinity of Betelgeuse, try these steps:

1. Check if the device exists in this dimension:
   ```bash
   sudo i2cdetect -y 1
   ```
   Should show device at address 0x68 (unless it's Thursday, never could get the hang of Thursdays)

2. Grant yourself access to the secret of the universe:
   ```bash
   sudo usermod -aG i2c $USER
   ```

3. When all else fails:
   ```bash
   sudo reboot
   ```
   (The digital equivalent of turning it off and on again, which has solved more problems in the universe than any Pan Galactic Gargle Blaster)

## License

This project is licensed under the "Don't Blame Us" agreement, as ratified by the Galactic Council.
[Creative Commons Attribution-NonCommercial 4.0 International License][cc-by-nc]

[cc-by-nc]: http://creativecommons.org/licenses/by-nc/4.0/

## Acknowledgments

Thanks to:
- The Infinite Improbability Drive, without which none of this would be randomly possible
- The great computer Deep Thought, for inspiring our error messages
- The Babel fish, for making our code comments comprehensible
- The mice, for running all our beta tests

---

*Created with digital towels by Axel Schmidt  *
*Year 2025 (Earth time)* 

*Remember: DON'T PANIC, it's just code.* 