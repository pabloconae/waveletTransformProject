import numpy as np
import matplotlib.pyplot as plt

import pywt
import pywt.data


# Load image
original = pywt.data.camera()

# Wavelet transform of image, and plot approximation and details
titles = ['Approximation', ' Horizontal detail',
          'Vertical detail', 'Diagonal detail']
coeffs2 = pywt.dwt2(original, 'bior1.3')
LL, (LH, HL, HH) = coeffs2
fig = plt.figure()
for i, a in enumerate([LL, LH, HL, HH]):
    ax = fig.add_subplot(2, 2, i + 1)
    ax.imshow(a, interpolation="nearest", cmap=plt.cm.gray)
    ax.set_title(titles[i], fontsize=12)
    ax.set_xticks([])
    ax.set_yticks([])

fig.suptitle("dwt2 coefficients", fontsize=14)

# Now reconstruct and plot the original image
reconstructed = pywt.idwt2(coeffs2, 'bior1.3')
fig = plt.figure()
plt.imshow(reconstructed, interpolation="nearest", cmap=plt.cm.gray)

# Check that reconstructed image is close to the original
np.testing.assert_allclose(original, reconstructed, atol=1e-13, rtol=1e-13)

#holaaaaa
# Now do the same with dwtn/idwtn, to show the difference in their signatures

coeffsn = pywt.dwtn(original, 'bior1.3')
fig = plt.figure()
for i, key in enumerate(['aa', 'ad', 'da', 'dd']):
    ax = fig.add_subplot(2, 2, i + 1)
    ax.imshow(coeffsn[key], interpolation="nearest", cmap=plt.cm.gray)
    ax.set_title(titles[i], fontsize=12)
    ax.set_xticks([])
    ax.set_yticks([])

fig.suptitle("dwtn coefficients", fontsize=14)

# Now reconstruct and plot the original image
reconstructed = pywt.idwtn(coeffsn, 'bior1.3')
fig = plt.figure()
plt.imshow(reconstructed, interpolation="nearest", cmap=plt.cm.gray)

# Check that reconstructed image is close to the original
np.testing.assert_allclose(original, reconstructed, atol=1e-13, rtol=1e-13)


plt.show()

print type(coeffs2_fusion)
print len(coeffs2_fusion)
print type(coeffs2_fusion[0])
print coeffs2_fusion[0].shape
print coeffs2_fusion[0][0]
print type(coeffs2_fusion[0][0])

print "-------- coeffs2_master ---------------------------------------"
print type(coeffs2_master)
print len(coeffs2_master)
print type(coeffs2_master[0])
print coeffs2_master[0].shape
print coeffs2_master[0][0]
print type(coeffs2_master[0][0])

print "///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

print type(coeffs2_fusion)
print len(coeffs2_fusion)
print type(coeffs2_fusion[1])
print len(coeffs2_fusion[1])

# LH
print type(coeffs2_fusion[1][0])
print coeffs2_fusion[1][0].shape
print coeffs2_fusion[1][0][0]

print "-------- coeffs2_slave ---------------------------------------"
print type(coeffs2_slave)
print len(coeffs2_slave)
print type(coeffs2_slave[1])
print len(coeffs2_slave[1])

# LH
print type(coeffs2_slave[1][0])
print coeffs2_slave[1][0].shape
print coeffs2_slave[1][0][0]

# HL
print type(coeffs2_slave[1][1])
print coeffs2_slave[1][1].shape

# HH
print type(coeffs2_slave[1][2])
print coeffs2_slave[1][2].shape





#----------------------------------------------


print type(coeffs2_fusion)
print len(coeffs2_fusion)
print type(coeffs2_fusion[0])

# LL fusionada
print "LL fusionada"
print coeffs2_fusion[0].shape
print coeffs2_fusion[0][0]
print "----------------------------"

# LL master
print "LL master"
print coeffs2_master[0].shape
print coeffs2_master[0][0]
print "----------------------------"

print "///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

# LH fusion
print type(coeffs2_fusion[1][0])
print coeffs2_fusion[1][0].shape
print coeffs2_fusion[1][0][0]

# LH slave
print type(coeffs2_slave[1][0])
print coeffs2_slave[1][0].shape
print coeffs2_slave[1][0][0]
print "----------------------------"

# HL fusion
print type(coeffs2_fusion[1][1])
print coeffs2_fusion[1][1].shape
print coeffs2_fusion[1][1][0]

# HL slave
print type(coeffs2_slave[1][1])
print coeffs2_slave[1][1].shape
print coeffs2_slave[1][1][0]
print "----------------------------"

# HH fusion
print type(coeffs2_fusion[1][2])
print coeffs2_fusion[1][2].shape
print coeffs2_fusion[1][2][0]

# HH slave
print type(coeffs2_slave[1][2])
print coeffs2_slave[1][2].shape
print coeffs2_slave[1][2][0]
print "----------------------------"

print LL_ms.shape
print LH_slv.shape
print HL_slv.shape
print HH_slv.shape


