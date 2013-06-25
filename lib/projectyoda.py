import sys, os, subprocess, resources, configs

# parse args and set state for config
def init():
    env = { 'args' : [], 'config' : False }
    for i in range (1, len(sys.argv)):
        env['args'].append(sys.argv[i])
    if env['args'][0] == '-c':
        env['config'] = True
        env['args'].pop(0)
    return env

# curl function
def curl_resource(args):
    curl_result = { 'curl_success' : False, 'curl_completes' : [], 'curl_failures' : [] }
    for arg in args:
        resource = resources.return_resource(arg)
        if resource != False:
            print 'Grabbing ' + arg
            curl_req = subprocess.Popen(['curl', '-LO', resource])
            curl_req.wait() # wait for subprocess to finish before continuing with parent process
            curl_result['curl_completes'].append(arg)
        else:
            print 'Invalid resource specified: ' + arg
            curl_result['curl_failures'].append(arg)
    if(len(curl_result['curl_completes']) == len(args)):
        curl_result['curl_success'] = True
    return curl_result

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
env = init()
if env['config']:
        print 'in config'
        curl_stats = curl_resource(env['args'])
        if curl_stats['curl_success']:
            yoda_unzip(env['args'])
            run_config(env['args'])
        else:
            print 'Cannot run config. Not all resources downloaded.'
            print 'resources successfully downloaded:'
            print curl_stats['curl_completes']
            print 'resources specified:'
            print env['args']
else:
    curl_stats = curl_resource(env['args'])
    if curl_stats['curl_success']:
        yoda_unzip(env['args'])
    else:
        yoda_unzip(curl_stats['curl_completes'])
      




