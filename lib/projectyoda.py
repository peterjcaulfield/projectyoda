import sys, os, subprocess, resources, configs

args = []
curl_success = []
config = False
test = True

# parse args and set state for config
def init():
    for i in range (1, len(sys.argv)):
        args.append(sys.argv[i])
    if args[0] == '-c':
        config = True
        args.pop(0)

# curl function
def curl_resource(args):
    for arg in args:
        resource = resources.return_resource(arg)
        if resource != False:
            print 'Grabbing ' + arg
            if not test:
                curl_req = subprocess.Popen(['curl', '-LO', resource])
                curl_req.wait() # wait for subprocess to finish before continuing with parent process
                curl_success.append(arg)
        else:
            print 'Invalid resource specified: ' + arg

# unzip function
def yoda_unzip(zips):
    for zip_ref in zips:
        print zip_ref

# config function
def run_config(args):
    config_script = configs.return_config(args)
    if config_script != False:
        print 'valid config'
        print config_script
        #build path to configs
        path = os.path.dirname(os.path.realpath(__file__))
        path += '/configs/'
        path += config_script
        config_exec = subprocess.Popen(['python', path])
        config_exec.wait()
    else:
        print 'invalid config:'
        print args

# execution
init()
if config:
        print 'config biatch'
        curl_resource(args)
        if len(curl_success):
            yoda_unzip(curl_success)
        run_config(args)
else:
    curl_resource(args)
    if len(curl_success):
        yoda_unzip(curl_success)
      




