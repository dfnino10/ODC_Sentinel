import os
import subprocess
from pathlib import Path
import click
import shutil

@click.command(
    help="Batch indexes sentinel dataset yamls into the datacube. Takes as argument the .SAFE images directories that contain the yamls"
         "eg. python DatacubeIndex.py <input_folder>")
@click.argument('datasets_folder',
                type=click.Path(exists=True, readable=True, writable=False),
                nargs=-1)
@click.option('--output', help="Write indexed datasets into this directory",
              type=click.Path(exists=False, writable=True, dir_okay=True))

def main(datasets_folder, output):
    datasets_folder = Path(datasets_folder[0]).resolve()
    target_folder = Path(output).resolve()
    for dataset in os.listdir(datasets_folder):
        dataset_folder = Path(os.path.join(target_folder, dataset))
        shutil.move(os.path.join(datasets_folder, dataset), target_folder)
        yaml_filename =  str(dataset_folder).split('/')[-1] + ".yaml"
        yaml_full_path = os.path.join(dataset_folder, yaml_filename)
        subprocess.run(["datacube", "dataset", "add", yaml_full_path])

if __name__ == "__main__":
    main()
