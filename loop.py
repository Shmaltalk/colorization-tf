import glob
import subprocess

for f in glob.glob('testimages/*'):
    subprocess.call(['python3', 'demo.py', f])
