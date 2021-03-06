##############################################################################
# Copyright (c) 2013, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Written by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License (as published by
# the Free Software Foundation) version 2.1 dated February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
"""\
This test does sanity checks on Spack's builtin package database.
"""
import unittest

import spack
import spack.url as url
from spack.packages import PackageDB


class PackageSanityTest(unittest.TestCase):

    def check_db(self):
        """Get all packages in a DB to make sure they work."""
        for name in spack.db.all_package_names():
            spack.db.get(name)


    def test_get_all_packages(self):
        """Get all packages once and make sure that works."""
        self.check_db()


    def test_get_all_mock_packages(self):
        """Get the mock packages once each too."""
        tmp = spack.db
        spack.db = PackageDB(spack.mock_packages_path)
        self.check_db()
        spack.db = tmp


    def test_url_versions(self):
        """Check URLs for regular packages, if they are explicitly defined."""
        for pkg in spack.db.all_packages():
            for v, vattrs in pkg.versions.items():
                if 'url' in vattrs:
                    # If there is a url for the version check it.
                    v_url = pkg.url_for_version(v)
                    self.assertEqual(vattrs['url'], v_url)
