##############################################################################
# Copyright (c) 2013, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Written by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://scalability-llnl.github.io/spack
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

from spack import *


class Texinfo(Package):
    """
    Texinfo is the official documentation format of the GNU project. It was invented by Richard Stallman and Bob
    Chassell many years ago, loosely based on Brian Reid's Scribe and other formatting languages of the time. It is
    used by many non-GNU projects as well.FIXME: put a proper description of your package here.
    """
    homepage = "https://www.gnu.org/software/texinfo/"
    url      = "http://ftp.gnu.org/gnu/texinfo/texinfo-6.0.tar.gz"

    version('6.0', 'e1a2ef5dce5018b53f0f6eed45b247a7')
    version('5.2', '1b8f98b80a8e6c50422125e07522e8db')
    version('5.1', '54e250014fe698fb4832016158747c03')
    version('5.0', '918432285abe6fe96c98355594c5656a')

    def install(self, spec, prefix):
        configure('--prefix=%s' % prefix)
        make()
        make("install")
