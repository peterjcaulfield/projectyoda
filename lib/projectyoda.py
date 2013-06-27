''' 
to do:

    

'''

import sys, os, subprocess, re, zipfile, time,  resources, configs

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + '/yoda_classes')

from yoda_exceptions import yodaError

valid_commands = ['grab', 'resources', 'configs', 'help']


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
                    return env
                else:
                    return env
            else: # no switch present
                for i in range(1, len(sys.argv)):
                    env['args'].append(sys.argv[i])
                return env
        else: # no switch or args to cmd
            return env
    
    else:
        error_object = []
        error_object.append('Invalid command specified: ' + sys.argv[0])
        error_object.append('Valid commands are: ')
        error_object.append(valid_commands)
        raise yodaError(error_object)

     

def grab(args):
    
    valid_switches = ['-c']
    curl_links = {}
    zips = {}

    # check we have args 
    
    if len(args['args']) < 1:
        error_object = []
        error_object.append('No resource specified')
        raise yodaError(error_object)
    
    else: # check resources
        check_resources(args['args'])
        
        # get the curl links
        for resource in args['args']:
            curl_links[resource] = resources.return_resource(resource)
        # get name of each zip
        for key, value in curl_links.iteritems():
            zips[key] = os.path.basename(value)
    
    # check if a switch was passed
    if args['switch']:
        # check if switch is valid
        if args['switch'] in valid_switches:
            print 'running code with switch: ' + args['switch']
            curl_resource(curl_links)
            yoda_unzip(zips)
            run_config(args['args'])
        
        else: # invalid switch given
            error_object = []
            error_object.append('Invalid switch specifed: ' + args['switch'])
            raise yodaError(error_object)
    # no switch passed
    else:
        print 'running without switch'
        curl_resource(curl_links)
        yoda_unzip(zips)
            
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
def curl_resource(curl_links):
    curl_stats = {'successful' : [], 'failed' : []}
    for key, value in curl_links.iteritems():
        print 'Grabbing ' + key
        # using shell child proccess because httplib
        curl_req = subprocess.Popen(['curl', '-LO', value])
        curl_req.wait() # wait for subprocess to finish before continuing with parent process
        curl_stats['successful'].append(key)
    return True


# unzip function
def yoda_unzip(zips):

    for key, value in zips.iteritems():
        print 'Extracting: ' + key
        # using shell to unzip is broken in python < 2.6.5
        unzip_shell_req = subprocess.Popen(['unzip', value])
        unzip_shell_req.wait()
        # clean up
        os.remove(value)
    print 'Extraction complete'

# config function

def run_config(args):
    config_script = configs.return_config(args)
    if config_script != False:
        #build path to configs
        path = os.path.dirname(os.path.realpath(__file__))
        path += '/configs/'
        path += config_script
        config_exec = subprocess.Popen(['python', path])
        config_exec.wait()
    else:
        error_object = []
        error_object.append('invalid config:')
        error_object.append(args)
        raise yodaError(error_object)

# execution
try:
    grab(init())
except yodaError as e:
    for error_msg  in e.value:
        print error_msg


