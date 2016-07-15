#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

import sys
from com.xebialabs.xlrelease.plugin.overthere import OverthereSession


host = task.pythonScript.getProperty("host")
print "HOST     %s" % host
print "USERNAME %s" % host.getProperty('username')
print "-------------------------"
script = "source /home/%s/.profile\nansible-playbook -i %s" % (host.getProperty('username'),playbook)
print script
print "-------------------------"


#apply_task_options()
session = OverthereSession(host)
response = session.execute(script, remotePath)

# set variables
output = response.stdout
error = response.stderr

if response.rc == 0:
    print "```"
    print output
    print "```"
else:
    print "Exit code: "
    print response.rc
    print
    print "#### Output:"
    print "```"
    print output
    print "```"

    print "----"
    print "#### Error stream:"
    print "```"
    print error
    print "```"
    print

    sys.exit(response.rc)
