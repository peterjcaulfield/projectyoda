import os

resources = {

    'cake' : 'https://github.com/cakephp/cakephp/archive/master.zip',
    'bootstrap': 'http://twitter.github.io/bootstrap/assets/bootstrap.zip',
    'symfony' : 'http://symfony.com/download?v=Symfony_Standard_2.3.1.zip',
    'codeigniter' : 'http://ellislab.com/codeigniter/download',
    'wordpress' : 'http://wordpress.org/download/latest.zip',
    'ember' : 'http://builds.emberjs.com/ember-1.0.0-rc.6.js',
    'angular' : 'http://code.angularjs.org/1.0.7/angular-1.0.7.zip',
    'jquery' : 'http://code.jquery.com/jquery-2.0.2.min.js',
    'jvalidate' : 'http://jquery.bassistance.de/validate/jquery-validation-1.11.1.zip'

}

def return_resource(key):
    if key in resources:
        return resources[key]
    else:
        return False

def return_resource_zip_name(key):
 return os.path.basename(resources[key])

