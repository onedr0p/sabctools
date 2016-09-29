#!/usr/bin/env python
# -*- coding: utf-8 -*-
##=============================================================================
 #
 # Copyright (C) 2003, 2011 Alessandro Duca <alessandro.duca@gmail.com>
 # Modified in 2016 by Safihre <safihre@sabnzbd.org> for use within SABnzbd 
 # 
 # This library is free software; you can redistribute it and/or
 # modify it under the terms of the GNU Lesser General Public
 # License as published by the Free Software Foundation; either
 # version 2.1 of the License, or (at your option) any later version.
 #
 # This library is distributed in the hope that it will be useful,
 # but WITHOUT ANY WARRANTY; without even the implied warranty of
 # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 # Lesser General Public License for more details.
 #
 # You should have received a copy of the GNU Lesser General Public
 # License along with this library; if not, write to the Free Software
 # Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
 #=============================================================================
 # 
##=============================================================================

from distutils.core import setup, Extension

setup(    
    name            = "sabyenc",
    version         = "1.0.0",
    author          = "Safihre",
    author_email    = "safihre@sabnzbd.org",
    url             = "https://github.com/Safihre/sabnzbd-yenc",
    license         = "LGPL",
    package_dir     = { '': 'lib' },
    ext_modules     = [Extension("sabyenc", ["src/sabyenc.c"], extra_compile_args=["-O2"])],
        classifiers      = [
            "Programming Language :: Python",
            "Programming Language :: Python :: 2.5",
            "Programming Language :: Python :: 2.6",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: C",
            "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
            "Operating System :: Unix",
            "Development Status :: 4 - Beta",
            "Environment :: Other Environment",
            "Intended Audience :: Developers",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Topic :: Communications :: Usenet News"
            ],
    description     = "yEnc Module for Python modified for SABnzbd",
    long_description = """
yEnc Encoding/Decoding for Python
---------------------------------

Mofied the original yenc module by Alessandro Duca <alessandro.duca@gmail.com>
for use within SABnzbd.

This a fairly simple module, it provide only raw yEnc encoding/decoding with
builitin crc32 calculation. Header parsing, checkings and yenc formatting are 
left to you (see examples directory for possible implementations). 

Supports encoding and decoding directly to files or to memory buffers
with helper classes Encoder and Decoder.
"""
)
