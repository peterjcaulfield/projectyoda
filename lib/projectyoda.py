import sys, subprocess, resources

if len(sys.argv) > 1:
    for i in range (1, len(sys.argv)):
        resource = resources.return_resource(sys.argv[i])
        if resource != False:
            curl_req = subprocess.Popen(['curl', '-LO', resource])
            curl_req.wait() # wait for subprocess to finish before continuing with parent process
        else:
            print 'invalid resource specified'
    print 'Successfully downloaded resources'
else:
    print 'no args'



