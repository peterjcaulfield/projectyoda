import os, shutil

####################################################################
#                           PATHS

# bootstrap



# cakephp



###################################################################

if os.path.isfile('bootstrap/css/bootstrap.min.css') and os.path.exists('cakephp-master/app/webroot/css'):
    shutil.move('bootstrap/css/bootstrap.min.css', 'cakephp-master/app/webroot/css')
    print 'successfully moved bootstrap css assets'
else:
    print 'Unable to move css assets'

if os.path.isfile('bootstrap/js/bootstrap.min.js') and os.path.exists('cakephp-master/app/webroot/js'):
    shutil.move('bootstrap/js/bootstrap.min.js', 'cakephp-master/app/webroot/js')
    print 'successfully moved javascript assets'
else:
    print 'Unable to move javascript assets'

if os.path.exists('bootstrap/img') and os.path.exists('cakephp-master/app/webroot/img'):
    dir_contents = os.listdir('bootstrap/img')
    for file in dir_contents:
        shutil.move('bootstrap/img/' + file, 'cakephp-master/app/webroot/img/')
    print 'successfully moved image assets'
else:
    print 'Unable to move image assets'

shutil.rmtree('bootstrap')
