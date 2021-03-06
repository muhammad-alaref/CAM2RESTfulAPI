from setuptools import setup, find_packages

setup(
	name='CAM2RESTfulAPI',
	version='v1.0-rc0',
	packages=find_packages(),
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		'flask',
		'flask-login',
		'hdfs',
		'CAM2DistributedBackend',
	],
	scripts=['bin/CAM2RESTfulAPI'],
) 
