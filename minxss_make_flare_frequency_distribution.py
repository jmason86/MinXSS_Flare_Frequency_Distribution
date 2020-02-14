from scipy.io.idl import readsav
import matplotlib.pyplot as plt


data_path = '/Users/jmason86/Dropbox/minxss_dropbox/data/fm1/level1/'

data = readsav('{}minxss1_l1_mission_length_v2.sav'.format(data_path))
minxsslevel1 = data.minxsslevel1.x123[0].copy()

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
