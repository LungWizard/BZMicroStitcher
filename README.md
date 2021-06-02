# Keyence_OME-TIFF
Requires:
1. Stitch2d - the most up to date version can be found here: https://github.com/adamancer/stitch2d)
2. mosaic.py needs to be modified at line:
  - 31: import tifffile
  - 402: def create_mosaic(self, posdata, label=None, create_jpeg=True)
  - 625: for fp in glob.iglob(os.path.join(path, '*.tif'))
  - new line after 592: mosaic_array = np.asarray(mosaic)
  - new line after previous: tifffile.imwrite(fp, mosaic_array, bigtiff=True)
  - delete mosaic.save(fp, 'TIFF')
3. pyglet-1.4.10
4. opencv-contrib-python
5. tkinter
6. openpyxl
7. datetime
8. pillow
9. numpy
10. ome_types
11. pyside2
12. tifffile
