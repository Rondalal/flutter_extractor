import click 
import subprocess
import os
import re 

# Could be changed due to changes in the Flutter engine  
DATA_FILE = "isolate_snapshot_data"
POSSIBLE_DATA_TYPES = [{"type": "functions", 
                    "pattern":b"([a-zA-Z_]{1}\w+)@[0-9]+",
                     "filename": "functions"},
                     {"type": "strings", # including functions 
                    "pattern":b"[\w]{4,}",
                    "filename": "strings"}]

def get_data_from_snapshot(app_path):
    data_path = os.path.join(app_path, "assets", "flutter_assets", DATA_FILE)
    data = ""

    with open(data_path, 'rb') as data_file_handle:
        data = data_file_handle.read()

    return data

def extract_by_pattern_to_file(data, pattern, out_path):
    extracted_strings = set(re.findall(pattern, data)) # using set() to remove duplicates
    extracted_strings = b"\n".join(extracted_strings)

    click.echo("Writing to %s" % out_path)
    with open(out_path, "wb") as file_handle:
        file_handle.write(extracted_strings)

def mkdir_if_not_exist(directory):
    if not os.path.exists(directory):
        os.makedirs(directory) 

@click.command()
@click.option('--out', default="./flutter_data", help='The output dir')
@click.argument('app_path')
def main(app_path, out):
    """app_path: path to the extracted apk directory (for example - output directory of the apktool)"""
    mkdir_if_not_exist(out)

    click.echo("Reading from the isolate data file...")
    data = get_data_from_snapshot(app_path)

    for data_type in POSSIBLE_DATA_TYPES:
        out_path = os.path.join(out, data_type["filename"])
        extract_by_pattern_to_file(data, data_type["pattern"], out_path)

if __name__ == '__main__':
    main()
