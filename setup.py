from setuptools import setup, find_packages

setup(
    name='odash-client',
    version='0.1.0',
    description='Client for general dashboard to collect information from all services, run web tests to different services and get report.',
    long_description=open('README.rst').read(),
    # Get more strings from http://www.python.org/pypi?:action=list_classifiers
    author='oDesk',
    author_email='',
    url='',
    download_url='',
    license='',
    include_package_data=True,
    zip_safe=True,
    classifiers=[
        'Development Status :: ',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)