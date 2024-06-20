import subprocess
import os
path = os.path.dirname(os.path.realpath(__file__))

print("return code: ", subprocess.run([path + "/bin/reader_json", path + "/test.json"]).returncode)
print("return code: ", subprocess.run([path + "/bin/reader_csv", path + "/test.csv"]).returncode)
