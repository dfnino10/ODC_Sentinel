import os
import subprocess
from pathlib import Path
import click
import logging

@click.command(
    help="Batch indexes sentinel dataset yamls into the datacube. Takes as argument the .SAFE images directories that contain the yamls"
         "eg. python DatacubeIndex.py <input_folder>")
@click.argument('datasets_folder',
                type=click.Path(exists=True, readable=True, writable=False),
                nargs=-1)

def main(datasets_folder):
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)
    datasets_folder = Path(datasets_folder[0]).resolve()
    logging.info("Starting indexing process")
    for dataset in os.listdir(datasets_folder):
        dataset_folder = Path(os.path.join(datasets_folder, dataset))
        yaml_filename =  str(dataset_folder).split('/')[-1] + ".yaml"
        yaml_full_path = os.path.join(dataset_folder, yaml_filename)
        logging.info("Reading: %s", yaml_full_path)
        subprocess.run(["datacube", "dataset", "add", yaml_full_path])
        logging.info("Indexed dataset %s", dataset_folder)

if __name__ == "__main__":
    main()
