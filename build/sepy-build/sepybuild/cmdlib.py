import subprocess
import os


def run_cmd(cmd, *args):
    try:
        subprocess.check_output(cmd, *args)
    except subprocess.CalledProcessError as e:
        print('Error: [{}] {}'.format(e, e.output))
        raise


def workdir():
    return os.getcwd()
