from distutils.core import setup
setup(
  name = 'jupyter2clipboard',
  packages = ['jupyter2clipboard'],
  version = '0.1.2',
  license = 'MIT',
  description = 'A simple utility to copy jupyter cell output to your local clipboard from a hosted instance of jupyter.',
  author = 'paleneutron',
  author_email = 'paleneutron@outlook.com',
  url = 'https://github.com/PaleNeutron/jupyter2clipboard',
#   download_url = 'https://github.com/conceptualio/copydf/archive/0.1.2.tar.gz',
  keywords = ['CACHE'],
  install_requires = [
          'ipython'
      ],
  classifiers = [
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'Topic :: Software Development :: Build Tools',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 2',
      'Programming Language :: Python :: 2.6',
      'Programming Language :: Python :: 2.7',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.2',
      'Programming Language :: Python :: 3.3',
      'Programming Language :: Python :: 3.4',
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: 3.6',
      'Programming Language :: Python :: 3.7',
      'Programming Language :: Python :: 3.8',
      'Programming Language :: Python :: 3.9',
  ],
)
