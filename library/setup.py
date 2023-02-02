from setuptools import setup, find_packages


classifiers = ['Development Status :: 4 - Beta',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: MIT License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: System :: Hardware']

setup(name='OrangePi.ST7789',
      version='1.0.0',
      description='Library to control ST7789 TFT LCD displays on the Orange Pi.',
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      license='MIT',
      author='Andriy Malyshenko',
      author_email='andriy@sonocotta.com',
      classifiers=classifiers,
      url='https://github.com/sonocotta/st7789-orangepi-python',
      packages=find_packages(),
      install_requires=[
            'OPi.GPIO',
            'spidev',
            'Pillow'
      ])
