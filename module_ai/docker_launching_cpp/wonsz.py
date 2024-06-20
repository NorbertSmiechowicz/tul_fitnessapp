import subprocess
import os
path = os.path.dirname(os.path.realpath(__file__))
path_exe = path + "/bin/main"
path_json = path + "\\test.json"

subprocess.run([path_exe, path_json])
