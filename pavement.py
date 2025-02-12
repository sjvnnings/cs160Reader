import os
import sys
import pkg_resources
from socket import gethostname

from paver.easy import options, Bunch
import paver.setuputils

from runestone import get_master_url
from runestone import build  # NOQA: F401 -- build is called implicitly by the paver driver.
from runestone.server import get_dburl

paver.setuputils.install_distutils_tasks()
sys.path.append(os.getcwd())

home_dir = os.getcwd()

master_url = 'http://127.0.0.1:8000'
project_name = 'CS160Reader'
serving_dir = './built/cs160Reader'

options(
    sphinx = Bunch(docroot=".",),

    build = Bunch(
        builddir = serving_dir,
        sourcedir = "_sources",
        outdir = serving_dir,
        confdir = ".",
        template_args={
            'login_required':'false',
            'loglevel': 0,
            'course_title': project_name,
            'python3': 'true',
            'dburl': '',
            'default_ac_lang': 'python',
            'downloads_enabled': 'false',
            'enable_chatcodes': 'false',
            'allow_pairs': 'false',
            'dynamic_pages': False,
            'use_services': 'false',
            'basecourse': project_name,
            'course_id': project_name,
            # These are used for non-dynamic books.
            'appname': project_name,
            'course_url': master_url,
            'minimal_outside_links': True,
        }
    ),
)

version = pkg_resources.require("runestone")[0].version
options.build.template_args['runestone_version'] = version