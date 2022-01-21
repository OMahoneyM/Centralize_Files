# Centralize_Files
 A python script to help centralize files in a new directory that are dispersed in nested directories

---

### Purpose
 My main objective with this script is to centralize all of the FASTQ files generated from a MiSeq run. Downloading a project's data from Basespace will produce a project directory that contains subdirectories for each sample. Within these subdirectories are the sample's R1 and R2 FASTQ files. These files need to be centralized in one directory in order to be ingested into our pipeline.

---

#### Prerequisites 
In order to run this script you will need to have the following libraries installed:
- [`shutil`](https://docs.python.org/3/library/shutil.html#module-shutil)
- [`os`](https://docs.python.org/3/library/os.html)
- [`time`](https://docs.python.org/3/library/time.html?highlight=time#module-time)
- [`tqdm`](https://tqdm.github.io/)

---

#### Using the Script
For ease of use, I uploaded this script as a python notebook so you can open it in Jupyter Notebook and run it. You can also copy the code and run it in your preferred IDE if you like. 

After the libraries are loaded, you will need to define the `source` and `dest` variables. The `source` variable should be the absolute path of the directory which contains all the nested directories that house your target files. The `dest` variable should be the absolute path of the directory you want said files to be copied into. 

In order to make this script more specific, the function `.endswith()` was included so that users could specify the types of files they wanted copy. The default is **“.fastq.gz”**. 

---
