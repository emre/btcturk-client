from setuptools import find_packages, setup

setup(
    name='btcturk_client',
    version='0.0.2',
    packages=find_packages(),
    url='https://github.com/emre/btcturk-client',
    license='MIT',
    author='Emre Yilmaz',
    author_email='mail@emreyilmaz.me',
    description='Btcturk.com api client',
    install_requires=['requests'],
    classifiers=(
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ),
)
