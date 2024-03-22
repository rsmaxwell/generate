#!/bin/python3


# write_messages.py

import os
import json
import yaml
import pprint
import argparse
from pathlib import Path
from jinja2 import Environment, FileSystemLoader



parser = argparse.ArgumentParser(description="tool to substitute placeholders with data in template files",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-d", "--data",      default="context.yaml", help="data file in json or yaml format")
parser.add_argument("-t", "--templates", default="templates",    help="directory containing template files")
parser.add_argument("-o", "--output",    default="output",       help="directory where generated files are written")
config = parser.parse_args()



print("--[ using ]-------")
print(f"    data file:     {config.data}" )
print(f"    templates dir: {config.templates}" )
print(f"    output dir:    {config.output}" )


file_name, file_extension = os.path.splitext(config.data)

if file_extension == ".json":
    with open(config.data) as f:
        context = json.load(f)
elif file_extension == ".yaml":
    with open(config.data) as f:
        context = yaml.safe_load(f)
else:
    print(f"Unexpected file extension: {config.data}")
    exit(1)

print("")
print("---[ data ]-------")
#print(json.dumps(context, indent=3))
#print("")
print(yaml.dump(context, indent=2))


print("--[ output ]-------")
environment = Environment(loader=FileSystemLoader(config.templates))
for root, d_names, f_names in os.walk(config.templates):

    for f in f_names:

        source = os.path.join(root, f)
        relative_dirpath = os.path.relpath(root, config.templates)
        if relative_dirpath == ".":
            relative_filepath = f
        else:
            relative_filepath = os.path.join(relative_dirpath, f)

        template = environment.get_template(relative_filepath)

        target_dir = os.path.join(config.output, relative_filepath)
        Path(target_dir).mkdir(parents=True, exist_ok=True)

        target = os.path.join(target_dir, f)
        with open(target, mode="w", encoding="utf-8") as file:
            content = template.render( context )
            file.write(content)
            print(f"    {relative_filepath}")
