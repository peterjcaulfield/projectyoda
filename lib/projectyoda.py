import sys, subprocess, resources, configs
# should wrap curl and config calls in to functions as curl will
# will be duplicated with and without -c switch

if len(sys.argv) > 1:
    if sys.argv[1] == '-c': # check for config switch
        for i in range (2, len(sys.argv)):
            resource = resources.return_resource(sys.argv[i])
            if resource != False:
                print 'Grabbing ' + sys.argv[i]
                curl_req = subprocess.Popen(['curl', '-LO', resource])
                curl_req.wait() # wait for subprocess to finish before continuing with parent process
            else:
                print 'Invalid resource specified: ' + sys.argv[i]
        config = []
        for i in range(2, len(sys.argv)):
            config.append(sys.argv[i])
        config_script = configs.return_config(config)
        if config_script != False:
            print 'valid config'
        else:
            print 'invalid config:'
            print config
    else:
        print 'we are running dl only'
else: 
    print 'no args - should show help function'




