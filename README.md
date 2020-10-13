# Downloading and indexing sentinel images to the Open Data Cube

This repo contains scripts to download and index [copernicus](https://scihub.copernicus.eu/dhus/#/home) sentinel imagery.

Specifically, SentinelCopernicusDownload.py for acquiring the images locally, batch_sen2cor_prepare.py for generating the metadata needed for the Data Cube to index a set of images and DatacubeIndex.py to batch index the imagery from the previously generated metadata.

## Getting Started

These scripts use some libraries to run.

### Prerequisites

**Open Data cube**: For managing, accessing satellite imagery and more. You can find documentation on  [ODC docs](https://datacube-core.readthedocs.io/en/latest/user/intro.html). Also, a docker container download instructions are available on [ODC container installation](https://github.com/DonAurelio/open-datacube-workshop/tree/master/version_1.8.2)

**Sentinelsat**: Library used to download the sentinel imagery from copernicus. You can find documentation on [sentinelsat docs](https://sentinelsat.readthedocs.io/en/stable/index.html).

```
pip install sentinelsat
```

## Running 


### Downloading

The SentinelCopernicusDownload.py script is tested on python 3.6. The sentinelsat library uses your copernicus user and password, an otput dir is expected in the `outdir` variable. An example of use is:

```
python3 SentinelCopernicusDownload.py 
```

### Indexing into the datacube 

(It is important to note that these scripts were developed for indexing Sentinel-2 L2A products.)
In order to index the images into the ODC, metadata files must be generated from each image. The script batch_sen2cor_prepare.py does this by taking as input a folder that contains the multiple sentinel-2 images (.safe folders) and an output folder where the metadata files will be saved. The metadata files are yaml files that the datacube uses for indexing the imagery. 

Example of use: 

```
python3 batch_sen2cor_prepare.py <input_folder> --output <outfolder>
```

Once we have the metadatafiles in a folder, the DatacubeIndex.py scripts goes through each of these files and apply the `datacube dataset add <meadatafile>` command. 
```
python3 DatacubeIndex.py <input_folder> 
```


## Authors

* [David Niño](https://github.com/dfnino10)


## Acknowledgments
* [Matt Paget](https://github.com/mpaget)
* [Aurelio Vivas](https://github.com/DonAurelio)
