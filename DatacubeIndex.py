import os
import subprocess
from pathlib import Path
import click

@click.command(
    help="Batch indexes sentinel dataset yamls into the datacube"
         "eg. python DatacubeIndex.py <input_folder>")
@click.argument('datasets_yamls_folder',
                type=click.Path(exists=True, readable=True, writable=False),
                nargs=-1)

def main(datasets_yamls_folder):
    datasets_yamls_folder_path = Path(datasets_yamls_folder[0]).resolve()
    for yaml_file in os.listdir(datasets_yamls_folder_path):
        print(datasets_yamls_folder_path)
        yaml_full_path = Path(os.path.join(datasets_yamls_folder_path, yaml_file))
        subprocess.run(["datacube", "dataset", "add", yaml_full_path])

if __name__ == "__main__":
    main()
