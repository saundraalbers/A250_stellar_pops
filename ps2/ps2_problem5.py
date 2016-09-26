import numpy as np
import fsps
import matplotlib.pyplot as plt

#create spectra for part a by varying alpha of the IMF
sp08 = fsps.StellarPopulation(sfh = 0, zmet = 10, imf_type = 2, imf3 = 0.8, sf_start = 13.69)
sp13 = fsps.StellarPopulation(sfh = 0, zmet = 10, imf_type = 2, imf3 = 1.3, sf_start = 13.69)
sp18 = fsps.StellarPopulation(sfh = 0, zmet = 10, imf_type = 2, imf3 = 1.8, sf_start = 13.69)
spectrum08 = sp08.get_spectrum(tage = 13.7)
spectrum13 = sp13.get_spectrum(tage = 13.7)
spectrum18 = sp18.get_spectrum(tage = 13.7)

#create spectra for part b by varying the IMF
sp_sal = fsps.StellarPopulation(sfh = 0, zmet = 10, imf_type = 0,  sf_start = 3.7)
sp_krou = fsps.StellarPopulation(sfh = 0, zmet = 10, imf_type = 2, sf_start = 3.7)
sp_van = fsps.StellarPopulation(sfh = 0, zmet = 10, imf_type = 3, sf_start = 3.7)
spectrum_sal = sp_sal.get_spectrum(tage = 13.7)
spectrum_krou = sp_krou.get_spectrum(tage = 13.7)
spectrum_van = sp_van.get_spectrum(tage = 13.7)


f, ax = plt.subplots(1, 1)
ax.semilogy(spectrum08[0], spectrum08[1], color = 'black', label = 'alpha = 0.8')
ax.semilogy(spectrum13[0], spectrum13[1], color = 'red', label = 'alpha = 1.3')
ax.semilogy(spectrum18[0], spectrum18[1], color = 'blue', label = 'alpha = 1.8')
ax.set_xlim(1500,10000)
ax.set_ylim(1e-22, 1e-15)
ax.set_ylabel('Luminosity [L_sun/Hz]')
ax.set_xlabel('Wavelength [Angstrom]')
ax.legend(loc = 4)
f.savefig('spectra_varying_alpha_problem_5.png', dpi=300, bbox_inches='tight')

f1, ax1 = plt.subplots(1, 1)
ax1.semilogy(spectrum_sal[0], spectrum_sal[1], color = 'black', label = 'IMF = Salpeter (1955)')
ax1.semilogy(spectrum_krou[0], spectrum_krou[1], color = 'red', label = 'IMF = Kroupa (2001)')
ax1.semilogy(spectrum_van[0], spectrum_van[1], color = 'blue', label = 'IMF = van Dokkum (2008)')
ax1.set_xlim(5000,20000)
ax1.set_ylim(5e-17, 1e-15)
ax1.set_ylabel('Luminosity [L_sun/Hz]')
ax1.set_xlabel('Wavelength [Angstrom]')
ax1.legend(loc = 4)
f1.savefig('spectra_varying_imf_problem_5.png', dpi=300, bbox_inches='tight')

plt.show()
