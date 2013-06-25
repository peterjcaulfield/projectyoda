import sys, os, subprocess, resources, configs

#global output messages

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
    curl_env = { 'curl_success' : False, 'curl_completes' : [], 'curl_failures' : [], 'valid_resources' : [], 'invalid_resources' : [] }
    for arg in args:
        resource = resources.return_resource(arg)
        if resource:
            curl_env['valid_resources'].append(arg)
        else:
            curl_env['invalid_resources'].append(arg)
    if len(curl_env['valid_resources']) != len(args):
        print 'invalid resources specified:'
        print curl_env['invalid_resources']
        print 'please check available resources with yoda -r'
        print 'aborting'
        return False
    else:
        for arg in args:
            print 'Grabbing ' + arg
            #curl_req = subprocess.Popen(['curl', '-LO', resource])
            #curl_req.wait() # wait for subprocess to finish before continuing with parent process
            #curl_result['curl_completes'].append(arg)
        return True

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
    if curl_resource(env['args']):
        print 'All resources downloaded successfully. Extracting archives.'
        yoda_unzip(env['args'])
        print 'Running config'
        run_config(env['args'])
else:
    if curl_resource(env['args']):
        print 'All resources downloaded successfully. Extracting archives.'
        yoda_unzip(env['args'])
        




