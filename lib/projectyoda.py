import sys, subprocess, resources, configs

# curl function
def curl_resource(argv_offset):
    for i in range (argv_offset, len(sys.argv)):
        resource = resources.return_resource(sys.argv[i])
        if resource != False:
            print 'Grabbing ' + sys.argv[i]
            curl_req = subprocess.Popen(['curl', '-LO', resource])
            curl_req.wait() # wait for subprocess to finish before continuing with parent process
        else:
            print 'Invalid resource specified: ' + sys.argv[i]

# config function
def run_config(argv_offset):
    config = []
    for i in range(argv_offset, len(sys.argv)):
        config.append(sys.argv[i])
    config_script = configs.return_config(config)
    if config_script != False:
        print 'valid config'
    else:
        print 'invalid config:'
        print config

# execution
if len(sys.argv) > 1:
    if sys.argv[1] == '-c': # check for config switch
        curl_resource(2)
        run_config(2)
    else:
        curl_resource(1)
else: 
    print 'no args - should show help function'




