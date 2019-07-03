# File: killInstance.py

import subprocess
import json
import sys

# Get app ID
#apps_str = subprocess.check_output(["cf curl /v3/apps?space_guids=d29e2e68-5dc2-4d3c-9db4-362dec6bab4b"], shell=True)
apps_str = subprocess.check_output(["cf curl /v3/apps?names=employee-api"], shell=True)
apps = json.loads(apps_str)
print "\n\n\n========================"
print "Looking for App ID..."
found = False
for resource in apps["resources"]:
    if resource["name"] == "employee-api":
        found = True
        guid = resource["guid"]
        print "employee-api APP ID is " + guid
if not found:
    print "employee-api APP ID not found"
    quit()

#kill process
print "\n\n\n========================"
instance_num = sys.argv[1]
print "Proceeding to kill app instance " + instance_num
cmd = "cf curl /v3/processes/" + guid + "/instances/" + instance_num + " -X DELETE"
print "Executing " + cmd
kill_res = subprocess.check_output([cmd], shell=True)
print kill_res
