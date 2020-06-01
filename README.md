# MinXSS_Flare_Frequency_Distribution
 Make a solar flare frequency distribution from the Miniature X-ray Solar Spectrometer (MinXSS) data

# Intro to the MinXSS CubeSat - the satellite that took these measurements

The Miniature X-ray Solar Spectrometer is a small satellite called a CubeSat. It's about the size of a loaf of bread. Each CubeSat "Unit" is about 10x10x10 cm. MinXSS is a 3U CubeSat measuring 34x10x10 cm. It was designed, built, and flown by graduate, undergraduate, and high school students at the University of Colorado Boulder (CU), with a great deal of mentorship provided by scientists and engineers at CU's [Laboratory for Atmospheric and Space Physics](https://lasp.colorado.edu/home/about/). MinXSS was built in the early 2010s, deployed from the International Space Station in 2016 May, and operated for 1 year before its orbit decayed and it burned up in the atmosphere (as planned). 

The science instrument onboard is a commercial product called an [X123 from a company called Amptek](https://www.amptek.com/products/si-pin-x-ray-detectors-for-xrf/x-123-complete-x-ray-spectrometer-with-si-pin-detector). The X123 is primarily sold to, e.g., geologists who need to determine the composition of rocks while in the field. This means that it is small, lightweight, and consumes little power. All things that make it perfect for a CubeSat. We modified it very slightly to make it work in the vacuum of space and slapped it into our CubeSat. The X123 measures "soft" X-rays, those that have energies between about 0.5-30 keV, about the same energy that is used for dental and other medical diagnostic X-ray imaging. It builds up a spectrum of the X-ray photons: for 10-seconds at a time it counts how many photons come in at which particular energy in that 0.5-30 keV range. It can distinguish between photons that have energy differences as little as about 0.15 keV -- it's "spectral resolution". 

The sun emits light across all energies, from radio to gamma. It's peak emisssion is in the visible range, roughly a green color at about 500 nm wavelength<sup>1</sup>. The sun doesn't change a whole lot at visible wavelengths. We can see sunspots sometimes, but those don't change the total emission from the sun a whole lot. At shorter wavelengths, the sun gets a whole lot more interesting. It is dynamic on timescales from seconds to decades. The ultraviolet and X-ray range is where we see huge increases in emission from solar flares. That's what we're studying here with MinXSS. How much energy is contained in each of the hundreds of flares that MinXSS observed? 


<sup>1</sup> Note that I changed from talking about light in units of keV to nm here. These are entirely equivalent, and are related by Planck's equation: E=hc/lambda. 

More info on MinXSS
* [5-minute video of highlights from the the making of MinXSS on Youtube, here](https://www.youtube.com/watch?v=pw2-xLI6v6A&t=39s).
* [MinXSS website](https://lasp.colorado.edu/home/minxss/) with news, data, launch videos, video of deployment from the space station, leaderboards of data that was captured by ham radio operators around the world, access to the data, and more

# Intro to the science of flare frequency distributions

