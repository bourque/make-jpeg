#! /usr/bin/env python

"""Create a JPEG file from a RAW, FLT, or FLC FITS file from the ACS
or WFC3 instrument.  Currently, other instruments (e.g. STIS) and other
filetyles (e.g. IMA) are not not supported, but likely the code could
be easily extended to support these.

Authors
-------

    Matthew Bourque
    Alex Viana
    Meredith Durbin

Use
---

    This module is intended to be used via the python environemnt, for
    example:

        import make_jpeg
        make_jpeg(<path_to_file>)

Dependencies
------------

    This module is supported in both Python 2.7 and Python 3+.  This
    module also depends on astropy, numpy, and the Python Image Library
    (PIL), also known as 'Pillow'.  These can be installed via 'conda'
    or 'pip':

    conda/pip install astropy
    conda/pip install numpy
    conda/pip install Pillow
"""

from astropy.io import fits
import numpy as np
from PIL import Image


def make_jpeg(filename):
    """Create a JPEG file from a raw, flt, or flc FITS file.  If the
    image is a full-frame WFC/UVIS or ACS/WFC image, the data from the
    1st and 4th extensions will be combined into one JPEG.

    Parameters
    ----------
    filename : str
        The path to the file.
    """

    with fits.open(filename) as hdulist:

        # Get the image data.
        data = hdulist[1].data

        # For full UVIS or WFC image.
        if (hdulist[0].header['DETECTOR'] in ['UVIS', 'WFC']
        and len(hdulist) > 4
        and hdulist[4].header['EXTNAME'] == 'SCI'):
            data2 = hdulist[4].data
            height = data.shape[0] + data2.shape[0]
            width = data.shape[1]
            temp = np.zeros((height, width))
            temp[0:int(height/2), :] = data
            temp[int(height/2):height, :] = data2
            data = temp

    # Clip the top and bottom 1% of pixels.
    top = np.percentile(data, 99)
    data[data > top] = top
    bottom = np.percentile(data, 1)
    data[data < bottom] = bottom

    # Scale the data.
    data = data - data.min()
    data = (data / data.max()) * 255.
    data = np.flipud(data)
    data = np.uint8(data)

    # Write the image to a JPEG
    image = Image.fromarray(data)
    image.save(filename.replace('.fits', '.jpg'))
