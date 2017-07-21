# make-jpeg

Create a JPEG file from a ``RAW``, ``FLT``, or ``FLC`` FITS file from the ``ACS`` or ``WFC3`` instrument.
Currently, other instruments (e.g. ``STIS``) and other filetyles (e.g. ``IMA``) are not not supported, but likely the code could
be easily extended to support these.

Authors
-------

- Matthew Bourque
- Alex Viana

Use
---

This module is intended to be used via the python environemnt, for
example:
::

    import make_jpeg
    make_jpeg(<path_to_file>)

Dependencies
------------

This module is supported in both Python 2.7 and Python 3+.  This
module also depends on ``astropy``, ``numpy``, and the Python Image Library
(``PIL``), also known as ``Pillow``.  These can be installed via ``conda``
or ``pip``:
::

    conda install astropy
    conda install numpy
    conda install Pillow

    pip install astropy
    pip install numpy
    pip install Pillow
