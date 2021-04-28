# Keyence_OME-TIFF
Requires:
1. Stitch2d - the most up to date version can be found here: https://github.com/adamancer/stitch2d)
  - mosaic.py needs to be modified at line 402: def create_mosaic(self, posdata, label=None, create_jpeg=True)
  - mosaic.py needs to be modified at line 625: for fp in glob.iglob(os.path.join(path, '*.tif'))
2. pyglet-1.4.10
3. opencv-contrib-python
4. tkinter
5. openpyxl
6. datetime
7. PIL
8. numpy
9. ome_types
10. pyside2
