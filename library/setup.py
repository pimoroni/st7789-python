from setuptools import setup, find_packages


classifiers = ['Development Status :: 4 - Beta',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: MIT License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: System :: Hardware']

setup(name='ST7789',
      version='0.0.1',
      description='Library to control an ST7789 160x160 TFT LCD display.',
      long_description=open('README.rst').read() + '\n' + open('CHANGELOG.txt').read(),
      license='MIT',
      author='Philip Howard',
      author_email='phil@pimoroni.com',
      classifiers=classifiers,
      url='https://github.com/pimoroni/st7789-python/',
      packages=find_packages())
