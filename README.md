# MinXSS Flare_Frequency Distribution
 Make a solar flare frequency distribution from the Miniature X-ray Solar Spectrometer (MinXSS) data

# Intro to the MinXSS CubeSat - the satellite that took these measurements

The Miniature X-ray Solar Spectrometer is a small satellite called a CubeSat. It's about the size of a loaf of bread. Each CubeSat "Unit" is about 10x10x10 cm. MinXSS is a 3U CubeSat measuring 34x10x10 cm. It was designed, built, and flown by graduate, undergraduate, and high school students at the University of Colorado Boulder (CU), with a great deal of mentorship provided by scientists and engineers at CU's [Laboratory for Atmospheric and Space Physics](https://lasp.colorado.edu/home/about/). MinXSS was built in the early 2010s, deployed from the International Space Station in 2016 May, and operated for 1 year before its orbit decayed and it burned up in the atmosphere (as planned). 

The science instrument onboard is a commercial product called an [X123 from a company called Amptek](https://www.amptek.com/products/si-pin-x-ray-detectors-for-xrf/x-123-complete-x-ray-spectrometer-with-si-pin-detector). The X123 is primarily sold to, e.g., geologists who need to determine the composition of rocks while in the field. This means that it is small, lightweight, and consumes little power. All things that make it perfect for a CubeSat. We modified it very slightly to make it work in the vacuum of space and slapped it into our CubeSat. The X123 measures "soft" X-rays, those that have energies between about 0.5-30 keV, about the same energy that is used for dental and other medical diagnostic X-ray imaging. It builds up a spectrum of the X-ray photons: for 10-seconds at a time it counts how many photons come in at which particular energy in that 0.5-30 keV range. It can distinguish between photons that have energy differences as little as about 0.15 keV -- it's "spectral resolution". 

The sun emits light across all energies, from radio to gamma. It's peak emisssion is in the visible range, roughly a green color at about 500 nm wavelength<sup>1</sup>. The sun doesn't change a whole lot at visible wavelengths. We can see sunspots sometimes, but those don't change the total emission from the sun a whole lot. At shorter wavelengths, the sun gets a whole lot more interesting. It is dynamic on timescales from seconds to decades. The ultraviolet and X-ray range is where we see huge increases in emission from solar flares. That's what we're studying here with MinXSS. How much energy is contained in each of the hundreds of flares that MinXSS observed? The "flare frequency distribution" is just that: on the x-axis we've summed up the energy of each flare in the soft X-ray range and on the y-axis we're just counting how many flares had that particular summed energy. 


<sup>1</sup> Note that I changed from talking about light in units of keV (kiloelectronvolts) to nm (nanometers) here. These are entirely equivalent, and are related by Planck's equation: E=hc/lambda. 

More info on MinXSS
* [5-minute video of highlights from the the making of MinXSS on Youtube, here](https://www.youtube.com/watch?v=pw2-xLI6v6A&t=39s).
* [MinXSS website](https://lasp.colorado.edu/home/minxss/) with news, data, launch videos, video of deployment from the space station, leaderboards of data that was captured by ham radio operators around the world, access to the data, and more

# Intro to the science of flare frequency distributions
This figure from [Airapetian et al. (2019)](https://www.cambridge.org/core/product/identifier/S1473550419000132/type/journal_article) shows a composite of flare frequency distributions from lots of other papers looking at flares from the smallest scale (so called "nanoflares" observed on the sun) up to really big scales (so called "superflares" obsereved on other stars). Even higher energy flares occur as the supermassive black hole at the center of our galaxy tears apart infalling matter, e.g., [Ponti et al. (2015)](https://academic.oup.com/mnras/article-lookup/doi/10.1093/mnras/stv1537).

![image](https://github.com/jmason86/MinXSS_Flare_Frequency_Distribution/blob/master/reference/airapetian_figure_11.png)

So what do those numbers mean? Well take a look at the middle of the plot. Those are typical solar flares, and they have an energy around 10<sup>30</sup> erg, reaching as high as 10<sup>32</sup> erg. How much is that? Well, the entirely of human energy consumption for the last 50 years comes to about 10<sup>29</sup> erg. So a _single solar flare_ releases 10-1000x more energy than half a century of worldwide energy consumption. The plot also tells you how often flares occur. The y-axis uses some units that don't make it obvious, but solar flares occur about once per day on average. 

But also notice the scale on the axis and the direction of the line. Both axes are in log scale, so each major tick represents a factor of 10 change. The line is sloped downward. So, this plot is telling us that the more energy a flare has, the less frequently it occurs and that this isn't a gentle effect; the numbers are changing by huge amounts. Really energetic flares are incredibly rare. Really low-energy flares are happening constantly. 

There's a lot of literature about flare frequency distributions for the sun, other stars, our galaxy's supermassive black hole, and making these measurements with a variety of different satellite instrumnets. Here are some of those papers in addition to those linked above: 
* [Namekata et al. (2017)](http://dx.doi.org/10.3847/1538-4357/aa9b34): solar flares in visible ("white") light measured by [SDO/HMI](http://hmi.stanford.edu/)
* [Warmuth and Mann (2016)](http://hesperia.gsfc.nasa.gov/rhessidatacenter/): solar flares in X-rays measured by [RHESSI](https://hesperia.gsfc.nasa.gov/rhessi3/) and [GOES/XRS](https://en.wikipedia.org/wiki/Geostationary_Operational_Environmental_Satellite)
* [Pye et al. (2015)](http://www.aanda.org/10.1051/0004-6361/201526217): stellar flares in X-rays measured by [XMM-Newton](https://en.wikipedia.org/wiki/XMM-Newton)
* [Shibayama et al. (2013)](http://stacks.iop.org/0067-0049/209/i=1/a=5?key=crossref.b2cff83c6f0c9c1bbc0da4710de43296): stellar, solar-type-star superflares in visible ("white") light measured by [Keppler](https://en.wikipedia.org/wiki/Kepler_space_telescope)
* [Caramazza et al. (2007)](http://dx.doi.org/10.1051/0004-6361:20077195): stellar flares in X-rays measured by [Chandra](https://en.wikipedia.org/wiki/Chandra_X-ray_Observatory)
* [Colombo et al. (2007)](http://dx.doi.org/10.1051/0004-6361:20078064): stellar flares inside nebulae in X-rays measured by [Chandra](https://en.wikipedia.org/wiki/Chandra_X-ray_Observatory)
* [Shimizu (1995)](https://ui.adsabs.harvard.edu/abs/1995PASJ...47..251S/abstract): solar flares in X-rays measured by [Yohkoh/SXT](https://en.wikipedia.org/wiki/Yohkoh)
* [Crosby (1993)](http://link.springer.com/10.1007/BF00646488): solar flares in X-rays measured by [SMM/HXRBS](https://en.wikipedia.org/wiki/Solar_Maximum_Mission)


# Why are we doing this analysis?
Those studies above that looked at the sun in X-rays were using instruments that weren't calibrated on the ground before launch. That means that when they report a number in "ergs" it's not _really_ in ergs. Those instruments were designed to do other kinds of science, so getting that calibration wasn't necessary. And they were able to do some tricks and make some assumptions to end up with numbers that are in line with the expectations from stellar observations. MinXSS _was_ calibrated on the ground at the National Institute of Standards and Technology (NIST) Syncrhotron Ultraviolet Radiation Facility (SURF). So when we compute "ergs", we can trace that all the way back to an international standard. 

It's also good in science to reproduce results with new instrumentation. When things agree, we gain confidence in the conclusions we've drawn. When things don't agree, we have to question the methods and the conclusions of each study. That may seem like a result you want to avoid, but its actually the place where discovery happens. 

# What's in this repository
As of 2020-06-01, there is a jupyter notebook that I've been using to prototype the code. The main preliminary result is there at the end, but there are crucial, lingering tasks: 

1. Pre-flare subtraction. You can see my initial attempt toward the middle of the notebook. This will likely require digging into each time series individually to determine a reasonable baseline level. 
2. Filtering out bad events. There will also probably need to be some tossing out events with too few points either during baseline or during the flare. 
3. Decide on the right start/stop times for flares
4. Include uncertainties
5. Fits to the time series data with their uncertainties

There is also an environment.yml file that can be used to install all the required packages by just doing a `conda env create -f environment.yml` ([see conda documentation here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file)).  
