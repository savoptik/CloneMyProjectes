import subprocess

def gitSubmodule():
    return subprocess.call(['git', 'submodule', 'update', '--init', '--recursive'])

def podInstall():
    return  subprocess.call(['/usr/local/bin/pod', 'install'])

def gitClone(url):
    return subprocess.call(['git', 'clone', url])
