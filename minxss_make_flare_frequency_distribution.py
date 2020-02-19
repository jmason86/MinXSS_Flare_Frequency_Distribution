import numpy as np
from scipy.io.idl import readsav
import astropy.units as u
import matplotlib.pyplot as plt


def integrate_spectrum_energy(spectral_irradiance, energy):
    irradiance_masked = np.ma.array(spectral_irradiance, mask=np.isnan(spectral_irradiance))  # Causes the units to get dropped
    return np.trapz(irradiance_masked, energy)


def integrate_spectrum_time(irradiance, time_jd):
    #irradiance_masked = np.ma.array(irradiance, mask=np.isnan(irradiance))  # Do I need this since the mask was already done in the energy integration? Don't want it because it drops the astropy units
    time_seconds = (time_jd - time_jd[0]) * 86400 * u.second
    return np.trapz(irradiance, time_seconds)


def integrate_photon_flux_1au(flux):
    return flux * 4 * np.pi * ((1*u.AU).to(u.cm))**2


def extract_time_jd(minxsslevel1):
    return np.array([minxsslevel1['time'][i]['jd'][0] for i in range(len(minxsslevel1))])


# Read data
data_path = '/Users/jmason86/Dropbox/minxss_dropbox/data/fm1/level1/'
data = readsav('{}minxss1_l1_mission_length_v2.sav'.format(data_path))
minxsslevel1 = data.minxsslevel1.x123[0].copy()

goes_events_path = '/Users/jmason86/Dropbox/Research/Data/GOES/events/'
data_goes = readsav('{}GOES_events_MinXSS1_era.sav'.format(goes_events_path))
goes_events = data_goes.goesevents.copy()
goes_start_jd = goes_events['eventstarttimejd']
goes_end_jd = goes_start_jd + 1/24  # Nearly all flares are << 1 hour. The post-flare time intensity is much smaller and will add little to the time-integrated value

# Integrate spectra across energy to produce one value per time
spectral_irradiance = np.stack(minxsslevel1['irradiance']) * (u.photon / u.second / u.centimeter**2 / u.keV)
energy = minxsslevel1[0]['energy']
irradiance = integrate_spectrum_energy(spectral_irradiance, energy) * (u.photon / u.second / u.centimeter**2)

# Now integrate that across the times of all flares
time_jd = extract_time_jd(minxsslevel1)
# Loop through all the flares identified by GOES
photon_flux = []
for i in range(len(goes_start_jd)):
    flare_time_indices = np.where((time_jd >= goes_start_jd[i]) & (time_jd <= goes_end_jd[i]))
    if flare_time_indices[0].size > 1:
        photon_flux.append(integrate_spectrum_time(irradiance[flare_time_indices], time_jd[flare_time_indices]))


# Now integrate that over 1 AU to get rid of the / cm^2
photons = integrate_photon_flux_1au(photon_flux)

# Convert energy units from keV to erg
energy = u.keV.to(u.erg, energy) * u.erg

# Convert photons to energy
mean_energy = np.ma.array(energy, mask=(energy < 0)).mean() / u.photon
measured_energy = photons * mean_energy

# Example spectrum plot
spectrum_index = 2913
plt.plot(minxsslevel1[spectrum_index]['energy'], minxsslevel1[spectrum_index]['irradiance'], drawstyle='steps-mid')
plt.xlim([0.8, 2.5])
plt.xlabel('Energy [keV]')
plt.ylim([1e4, 1e9])
plt.yscale('log')
plt.ylabel('Irradiance [photons / sec / cm$^2$ / keV]')
plt.suptitle('MinXSS Solar SXR Spectrum on ' + minxsslevel1[spectrum_index]['time']['human'][0].decode("utf-8"))
plt.show()

pass

