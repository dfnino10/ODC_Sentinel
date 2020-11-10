import os
import zipfile

from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt

import cfg
import glob

api = SentinelAPI(cfg.copernicus["user"], cfg.copernicus["password"], 'https://scihub.copernicus.eu/dhus')
outdir = '/download_storage/S2_L2A_MSI_ARD/BoyacaImages/'


footprint = geojson_to_wkt(read_geojson('/origin/S2_L2A_MSI_ARD/Search Polygons/BoyacaCentral.geojson'))

products = api.query(footprint,
                     date=('20200919', '20201109'),
                     platformname='Sentinel-2',
                     producttype= 'S2MSI2A',
                     cloudcoverpercentage=(0, 90))
"""
date (tuple of (str or datetime) or str, optional) --
A time interval filter based on the Sensing Start Time of the products. Expects a tuple of (start, end), e.g. (“NOW-1DAY”, “NOW”). The timestamps can be either a Python datetime or a string in one of the following formats:

yyyyMMdd
yyyy-MM-ddThh:mm:ss.SSSZ (ISO-8601)
yyyy-MM-ddThh:mm:ssZ
NOW
NOW-<n>DAY(S) (or HOUR(S), MONTH(S), etc.)
NOW+<n>DAY(S)
yyyy-MM-ddThh:mm:ssZ-<n>DAY(S)
NOW/DAY (or HOUR, MONTH etc.) - rounds the value to the given unit
Alternatively, an already fully formatted string such as “[NOW-1DAY TO NOW]” can be used as well.
"""

api.download_all(products, outdir)

os.chdir(outdir)

for zip_file in glob.glob("*.zip"):
    with zipfile.ZipFile(zip_file) as zip_ref:
        zip_ref.extractall(outdir)
    os.remove(zip_file)
