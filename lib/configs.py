configs = {
    
   'cb.py' :  ['cake', 'bootstrap']        

    }


def return_config(config):
    valid_config = False
    for k, v in configs.iteritems():
        if set(config) == set(v):
            valid_config = k
            break
    return valid_config


