#!/usr/bin/python3
from fabric import Connection
from invoke import task
from datetime import datetime
# pack all files as tar.gz compress
@task
def do_pack(c, source_dir, output_dir, archive_format='tar.gz', echo=True):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    archive_name = f"archive_{timestamp}.{archive_format}"
    if echo:
        print(f"Packing files into: {archive_name}")
    # Pack files into the archive using source_dir, output_dir, and archive_name

if __name__ == "__main__":
    c = Connection('your_host')  # Replace 'your_host' with your actual host
    source_dir = '/path/to/source/dir'  # Replace with your source directory
    output_dir = '/path/to/output/dir'  # Replace with your output directory
    archive_format = 'tar.gz'
    echo = True
    
    # Invoke do_pack function
    do_pack(c, source_dir, output_dir, archive_format, echo)
