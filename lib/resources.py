resources = {
'cake' : 'https://github.com/cakephp/cakephp/archive/master.zip',
'bootstrap': 'http://twitter.github.io/bootstrap/assets/bootstrap.zip',
}

def return_resource(key):
    if key in resources:
        return resources[key]
    else:
        return False




