import subprocess

def gitSubmodule():
    return subprocess.call(['git', 'submodule', 'update', '--init', '--reursive'])

def podInstall():
    return  subprocess.call(['pod', 'install'])

def cdDirOut():
    return  subprocess.call(['cd', '..'])

def cdDirIn(path):
    return subprocess.call(['cd', "./" + path])

def gitClone(url):
    return subprocess.call(['git', 'clone', url])
