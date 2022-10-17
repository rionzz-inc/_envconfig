from setuptools import setup, find_packages

long_desc = ''
with open('README.md') as readme_file:
	long_desc = readme_file.read()

setup(
	name='py_tools',
	version='0.5',
	license='MIT',
	author='Prakash Leon Mishra',
	author_email='dev.leonmishra@gmail.com',
	description='A simple Package to load & parse configuration to diffrent datatypes',
	long_description=long_desc,
	long_description_content_type="text/markdown",
	keywords='Python environ loader, django configuration loader, flask config loader',
	package_dir={"": "src"},
	packages=find_packages(where="src"),
	python_requires=">=3.0",
	url='https://github.com/rionzz-inc/py_tools',
	# download_url='https://github.com/user/reponame/archive/v_01.tar.gz',  # I explain this
	# later on

	install_requires=[
		'python-dotenv',
	],
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	]

)