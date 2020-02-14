import numpy as np
from scipy.io.idl import readsav
import astropy.units as u
import matplotlib.pyplot as plt


def integrate_spectrum_energy(irradiance, energy):
    irradiance_masked = np.ma.array(irradiance, mask=np.isnan(irradiance))
    return np.trapz(irradiance_masked, energy)


# Read data
data_path = '/Users/jmason86/Dropbox/minxss_dropbox/data/fm1/level1/'
data = readsav('{}minxss1_l1_mission_length_v2.sav'.format(data_path))
minxsslevel1 = data.minxsslevel1.x123[0].copy()

# Sum all spectra -- one value per time
irradiance = np.stack(minxsslevel1['irradiance'])
energy = minxsslevel1[0]['energy']
integrated_irradiance_energy = integrate_spectrum_energy(irradiance, energy) * (u.photon / u.second / u.centimeter**2)

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

