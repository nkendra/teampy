import subprocess

import sys
import tempfile

import shutil
import venv

TEMP_DIRECTORY_PREFIX = 'envpy-'
VIRTUAL_ENV_NAME = 'sepytest'
PYTHON36_PATH = '/usr/bin/python36'


class BootstrapConfig(object):
    def __init__(self, use_temp_directory):
        self.use_temp_directory = use_temp_directory
        self.python_path = PYTHON36_PATH


def main():
    print('Let\'s bootstrap this!')
    bootstrap_config = BootstrapConfig(use_temp_directory=True)
    bootstrap = Bootstrap(bootstrap_config)
    bootstrap.create_virtualenv()
    return 0


class Bootstrap(object):
    def __init__(self, bootstrap_config: BootstrapConfig) -> None:
        self.bootstrap_config = bootstrap_config

    @property
    def python_path(self):
        return self.bootstrap_config.python_path

    def create_virtualenv(self):
        print('Creating virtualenv')
        temp_directory = self.create_install_directory(self.bootstrap_config)
        try:
            print('using {}'.format(temp_directory))
            run_cmd(self.python_path,
                    '-m', 'venv', VIRTUAL_ENV_NAME, temp_directory)
        finally:
            shutil.rmtree(temp_directory)
            print('cleaned directory {}'.format(temp_directory))

    @staticmethod
    def create_install_directory(bootstrap_config: BootstrapConfig) -> str:
        if bootstrap_config.use_temp_directory:
            return tempfile.mkdtemp(prefix=TEMP_DIRECTORY_PREFIX)
        raise ValueError('No install directory set')

    def create_venv(self, venv_directory):
        venv.create(venv_directory, )


def run_cmd(cmd, *args):
    if args:
        cmd = [cmd] + list(args)
    if not isinstance(cmd, list):
        cmd = [cmd]
    print(' '.join(cmd))
    try:
        completed = subprocess.check_output(cmd)
        if completed:
            print(completed)
    except subprocess.CalledProcessError as e:
        print('Error: {} - {}'.format(e, e.output))
        raise


if __name__ == '__main__':
    result = main()
    sys.exit(result)
