from setuptools import setup, find_packages

setup(name='adlibre-plugins',
      version='0.1',
      author='Mantas Zimnickas',
      author_email='sirexas@gmail.com',
      packages=find_packages(),
      install_requires=[
          'distribute',
          'django',
      ],
      url='https://bitbucket.org/sirex/django-plugins',
      license='LGPL',
      description='adlibre-plugins.',
      classifiers = [
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ])
