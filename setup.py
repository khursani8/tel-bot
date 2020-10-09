from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='telbot',
    url='https://github.com/khursani8/telbot',
    author='khursani',
    author_email='khursani8@gmail.com',
    # Needed to actually package something
    packages=['telbot'],
    # Needed for dependencies
    install_requires=['requests',"python-telegram-bot"],
    # *strongly* suggested for sharing
    version='1.0.0',
    # The license can be anything you like
    license='MIT',
    description='Simple Telegram bot only for sending message to chat room with 30 lines of code',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read()
)