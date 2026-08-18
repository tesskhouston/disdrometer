Raspberry Pi 5 pen laser optical disdrometer.

Materials:

MCP3008 (x2) ADC 

SFH 203 P (x16) Photodiode

VLM-650-03 (x16) lasers OR 1054 (x16) lasers

10kΩ carbon film 5% resistor (x16)

Raspberry Pi 5 (x1)

Adafruit T-Cobbler Plus for Raspberry Pi (x1)

Male-female wires

Male-male wires

Battery (discussed below)

Wiring:
The photodiode should be connected to the RPi5 and ADC according to the following schematic. <img width="640" height="360" alt="circuit" src="https://github.com/user-attachments/assets/ebeb6eaf-5f16-42ac-94a6-f448db7810af" />

This pattern is repeated for the following seven photodiodes, with each photodiode connected to a separate resistor. For the next eight photodiodes, the pattern is repeated again, but the second ADC is used. The second ADC is connected to the RPi5 exactly the same, except the CS/SHDN pin is connected to GPIO6. 

Lasers:
The lasers are powered separately. All lasers are connected to the same power source. For low noise, the lasers must have a long-lasting and stable power source. Alkaline batteries do not work well for this, so sealed lead acid batteries could possibly work. The VLM-650-03 lasers have a max voltage of 6V, and the 1054 lasers have a max voltage of 5.2V. 
The 1054 lasers are a lot cheaper than the VLM-650-03 lasers, but the diameter of the 1054 casing is 10mm, 3mm larger than that of the VLM-650-03 lasers. This could possibly negatively impact the accuracy of the disdrometer.


Disdrometer case CAD:
If using the VLM-650-03 lasers: [7mm lasers case](https://cad.onshape.com/documents/47a2c867df01d56771fcd8a2/w/6e366d5637159da0f92f1b37/e/7e958343497ca875862d8cb1?renderMode=0&uiState=6a84c47a4e6bebddeb3f6df0)
If using the 1054 lasers: [10 mm lasers case](https://cad.onshape.com/documents/870870483be6c1970ce9ec0d/w/0d18e095366b1de79bd34f11/e/b347e4383bae6bb7fba7e853?renderMode=0&uiState=6a84c4cd49d12d65834fa99f)
Note: The covering (parts 19-30) must be printed separately from the base (parts 1-18).

Accuracy notes:
The accuracy of this disdrometer is currently about 50% using the 7mm laser case. This may be attributed to the physical distance between photodiodes, the speed of the raindrops, or weak signals from the raindrops.
The distance between photodiodes could be the issue, because the photodiode chips only covered about 17.78% of the sampling area in the 7mm laser case. 
The speed of the raindrops could be the issue, because when a raindrop is recognized, that signal typically only lasts for one reading before the readings return to normal. This signifies that the raindrops interrupt the lasers for a shorter time compared to the sampling rate. Sampling the ADC faster by connecting the VDD pin to 5V instead of 3.3V could combat this, but it significantly increased the noise from the photodiodes, causing false positives and overshadowing actual raindrop signals.
Weak signals from the raindrops could also be the issue. Reducing noise in the circuit as a whole could combat this. The current noise filter calculates the IQR of each dataset (sampled over 10 seconds), multiplies it by 8, and subtracts it from the 25th percentile. If any data points are below that resulting value, they are counted as raindrops. Using 8 as the coefficient was found through trial and error.
