import numpy as np
from scipy.io.idl import readsav
import astropy.units as u
import matplotlib.pyplot as plt


def integrate_spectrum_energy(irradiance, energy):
    irradiance_masked = np.ma.array(irradiance, mask=np.isnan(irradiance))
    return np.trapz(irradiance_masked, energy)


def integrate_spectrum_time(irradiance, time_jd):
    #irradiance_masked = np.ma.array(irradiance, mask=np.isnan(irradiance))  # Do I need this since the mask was already done in the energy integration? Don't want it because it drops the astropy units
    time_seconds = (time_jd - time_jd[0]) * 86400 * u.second
    return np.trapz(irradiance, time_seconds)


def extract_time_jd(minxsslevel1):
    return [minxsslevel1['time'][i]['jd'][0] for i in range(len(minxsslevel1))]


# Read data
data_path = '/Users/jmason86/Dropbox/minxss_dropbox/data/fm1/level1/'
data = readsav('{}minxss1_l1_mission_length_v2.sav'.format(data_path))
minxsslevel1 = data.minxsslevel1.x123[0].copy()

# Integrate spectra across energy to produce one value per time
irradiance = np.stack(minxsslevel1['irradiance'])
energy = minxsslevel1[0]['energy']
integrated_irradiance_energy = integrate_spectrum_energy(irradiance, energy) * (u.photon / u.second / u.centimeter**2)

# Now integrate that across the times of all flares
time_jd = extract_time_jd(minxsslevel1)
bla = integrate_spectrum_time(integrated_irradiance_energy[0:50], time_jd[0:50])

# Convert energy units from keV to erg
energy = u.keV.to(u.erg, energy) * u.erg

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

