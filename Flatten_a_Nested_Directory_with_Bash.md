# Flatten a Nested Directory

`find source_dir -mindepth 2 -type f -name '*.fastq.gz' -exec mv -i '{}' dest_dir ';'`

Basically, `find` goes through the entire directory tree and for each file (`-type f`) that ends in *.fastq.gz* (`-name '*.fastq.gz'`) and is not in the top-level directory (`-mindepth 2`), it runs a `mv` command to move it to the directory you want (`-exec mv … ';'`). The `-i` makes `mv` ask before overwriting any duplicates; you can substitute `-f` to overwrite them without asking (or `-n` to not ask or overwrite). Remove `-name '*.fastq.gz'` if you want to move all over files from the source directory.