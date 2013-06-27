'''
    
    CONFIG = ['cake', 'bootstrap']

    This config is for cakephp and twitter bootstrap
    It places all the bootstrap assets where they need to be within cakephp folder structure
    
    todo: move pathcheck/move to a function?

'''

import os, shutil, sys, yodapaths


class yodaError(Exception):
    def __init__(self, value):
        self.value = value

# PATHS
bootstrap_css = yodapaths.paths['bootstrap']['css']
bootstrap_js = yodapaths.paths['bootstrap']['js']
bootstrap_img = yodapaths.paths['bootstrap']['img']
cakephp_css = yodapaths.paths['cakephp']['css']
cakephp_js = yodapaths.paths['cakephp']['js']
cakephp_img = yodapaths.paths['cakephp']['img']

# ENV
items_to_move = 3
successfully_moved = 0


if os.path.exists(bootstrap_css) and os.path.exists(cakephp_css):
    print 'moving twitter bootstrap css assets to cake css folder'
    dir_contents = os.listdir(bootstrap_css)
    for file in dir_contents:
        shutil.move(bootstrap_css + file, cakephp_css)
    print 'css assets moved'
    successfully_moved += 1
    print successfully_moved
else:
    error_object = []
    error.object.append('Unable to move bootstrap css assets due to missing path')
    error.object.append('Verify the following paths exist in yodapaths.py: ')
    error_object.append(bootstrap_css)
    error_object.append(cakephp_css)
    raise yodaError(error_object)

if os.path.exists(bootstrap_js) and os.path.exists(cakephp_js):
    print 'moving twitter bootstrap javascript assets to cake js folder'
    dir_contents = os.listdir(bootstrap_js)
    for file in dir_contents:
        shutil.move(bootstrap_js + file, cakephp_js)
    print 'javascript assets moved'
    successfully_moved += 1
    print successfully_moved
else:
    error_object = []
    error.object.append('Unable to move bootstrap js assets due to missing path')
    error.object.append('Verify the following paths exist in yodapaths.py: ')
    error_object.append(bootstrap_js)
    error_object.append(cakephp_js)
    raise yodaError(error_object)

if os.path.exists(bootstrap_img) and os.path.exists(cakephp_img):
    print 'moving twitter bootstrap img assets to cake img folder'
    dir_contents = os.listdir(bootstrap_img)
    for file in dir_contents:
        shutil.move(bootstrap_img + file, cakephp_img)
    print 'img assets moved'
    successfully_moved += 1
else:
    error_object = []
    error.object.append('Unable to move bootstrap img assets due to missing path')
    error.object.append('Verify the following paths exist in yodapaths.py: ')
    error_object.append(bootstrap_img)
    error_object.append(cakephp_img)
    raise yodaError(error_object)

if successfully_moved == items_to_move:
    print 'all assets moved successfully'
    shutil.rmtree('bootstrap')
else:
    print 'not all assets moved'
    print 'successful: '
    print successfully_moved
    print 'expected: '
    print items_to_move
