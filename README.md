# Keyence_OME-TIFF
Requires:
Stitch2d - the most up to date version can be found here: https://github.com/adamancer/stitch2d)
  - mosaic.py needs to be modified at line 402: def create_mosaic(self, posdata, label=None, create_jpeg=True)
  - mosaic.py needs to be modified at line 625: for fp in glob.iglob(os.path.join(path, '*.tif'))
pyglet-1.4.10
opencv-contrib-python
tkinter
openpyxl
datetime
PIL
numpy
ome_types
