''' 
to do:
    
    - move checks relative to individual methods to those methods
      i.e grab should check if a resource is valid not the init

'''

import sys, os, subprocess, re, resources, configs

valid_commands = ['grab', 'resources', 'configs', 'help']

class yodaError(Exception):
    def __init__(self, value):
        self.value = value

# parse args and set state for config
def init():
    # format args
    env = { 'args' : [], 'cmd' : False, 'switch' : False}
    sys.argv.pop(0) # we dont need path
    if len(sys.argv) < 1:
        error_object = []
        error_object.append('No arguments provided. See yoda help for cmd format')
        raise yodaError(error_object)
    # check if cmd is valid
    if sys.argv[0] in valid_commands:
        env['cmd'] = sys.argv[0]
        
        # check if we have a switch
        if len(sys.argv) > 1:
            if re.match('^-', sys.argv[1]):
                env['switch'] = sys.argv[1]
                # store remaning args if present and return env
                if len(sys.argv) > 2:
                    for i in range(2, len(sys.argv)):
                        env['args'].append(sys.argv[i])
                    print env
                    return env
                else:
                    return env
            else: # no switch present
                for i in range(1, len(sys.argv)):
                    env['args'].append(sys.argv[i])
                print env
                return env
        else: # no switch or args to cmd
            print env
            return env
    
    else:
        error_object = []
        error_object.append('Invalid command specified: ' + sys.argv[0])
        error_object.append('Valid commands are: ')
        error_object.append(valid_commands)
        raise yodaError(error_object)

     

def grab(args):
    valid_switches = ['-c']
    # check we have args
    if len(args['args']) < 1:
        error_object = []
        error_object.append('No resource specified')
        raise yodaError(error_object)
    else: # check resources
        check_resources(args['args'])
        print 'all resources valid'
        print args
    # check if a switch was passed
    if args['switch']:
        # check if switch is valid
        if args['switch'] in valid_switches:
            print 'running code with switch: ' + args['switch']
            curl_resource(args['args'])
            # switch is valid so check if resources are valid
        else: # invalid switch given
            error_object = []
            error_object.append('Invalid switch specifed: ' + args['switch'])
            raise yodaError(error_object)
    # no switch passed
    else:
        print 'running without switch'
        curl_resource(args['args'])
            
def check_resources(args):
        invalid_resources = [] 
        valid_resources = 0
        for resource in args:
            valid_resource = resources.return_resource(resource)
            if valid_resource:
                valid_resources += 1
            else:
                invalid_resources.append(resource)
        if valid_resources != len(args):
            error_object = []
            error_object.append('Invalid resources specified:')
            error_object.append(invalid_resources)
            error_object.append('Please see yoda resources for available resources')
            raise yodaError(error_object)
        else: # we have valid resources
            return True

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
        error_object.append('invalid config:')
        error_object.append(args)
        raise yodaError(error_object)

# execution
try:
    grab(init())
except yodaError as e:
    for error_msg  in e.value:
        print error_msg


