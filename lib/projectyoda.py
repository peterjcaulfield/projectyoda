''' 
to do:
    - check for valid config if a -c switch is specified in init?
'''

import sys, os, subprocess, re, resources, configs

valid_commands = ['grab', 'resources', 'configs', 'help']

# parse args and set state for config
def init():
    env = { 'args' : [], 'resources' : [], 'cmd' : False, 'switch' : False}
    sys.argv.pop(0) # we dont need path
    for arg in sys.argv:
        env['args'].append(arg) # meh. feels cleaner to me.
    
    if env['args'][0] in valid_commands: # check cmd is valid
        
        if len(env['args']) > 1: # make sure we have minimum amount of args to check for switch/resource
            env['cmd'] = env['args'][0]
            
            if re.match('^-', env['args'][1]): # check for switch
                
                if len(env['args']) > 2: # check for resource
                    env['switch'] = env['args'][1]
                    sys.argv.pop(0) # pop cmd
                    sys.argv.pop(0) # pop switch
                    env['resources'] = sys.argv # left with specified resources
                else: 
                    print 'No resource specified. Please see yoda help for cmd format' # no resource specified after switch
                    return False
            
            else:
                sys.argv.pop(0) # pop cmd
                env['resources'] = sys.argv # left with specified resources
            
            invalid_resources = [] # check if resources exist
            valid_resources = 0
            for resource in env['resources']:
                valid_resource = resources.return_resource(resource)
                if valid_resource:
                    valid_resources += 1
                else:
                    invalid_resources.append(resource)
            if (len(env['resources']) != valid_resources):
                print 'Invalid resources specified:'
                print invalid_resources
                print 'Please see yoda resources for available resources'
                return False
            else: # we have valid resources
                print env
                return env
        
        else:
            print 'No resource specified. Please see yoda help for cmd format'
            return False
    
    else:
        print 'Invalid command: ' + env['args'][0]
        print 'Valid commands are:'
        print valid_commands
        return False


# curl function
def curl_resource(args):
    curl_stats = {'successful' : [], 'failed' : []}
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
# needs to be redone to match new init function
'''
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
        
'''



