import pip._internal as pip

package_names=['colorama', 'progress', 'requests']
pip.main(['install'] + package_names + ['--upgrade']) 