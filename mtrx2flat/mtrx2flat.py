#!/usr/bin/python
# -*- coding: utf-8 -*-

__version__ = "1.0.1"
__date__ = "2017-01-04"
__status__ = "Prototype"

__author__ = "Toby Gill"
__maintainer__ = "Toby Gill"
__email__ = "toby.gill.09@ucl.ac.uk"

import os  # Used to navigate through directories.
import subprocess  # Used to process command line arguments.
from copy import copy  # Used to create copied instances of variables.


# Define the default vernissagecmd.exe file path.
default_vernissagecmd_path = os.path.abspath('C:/Program Files (x86)/Omicron NanoTechnology/Vernissage/V2.1/Bin/'
                                             'VernissageCmd.exe')
# Define the default exporter to use.
default_vernissage_exporter = 'Flattener'


# Create a copy of the vernissagecmd.exe path that can later be edited without affecting the default.
vernissagecmd_path = copy(default_vernissagecmd_path)
# Create a copy of the exporter that can later be changed without affecting the default.
vernissage_exporter = copy(default_vernissage_exporter)


def get_vernissagecmd_path():
    """
    A function that returns the current definition of the vernissagecmd.exe file path.
    :return: str containing the path to vernissagecmd.exe
    """
    return vernissagecmd_path


def get_vernissage_exporter():
    """
    A function that returns the current definition of the exporter to be used by the vernissagecmd.exe.
    :return: str containing the exporter to be used in the conversion by vernissagecmd.exe.
    """
    return vernissage_exporter


def set_vernissagecmd_path(path):
    """
    A function that can be used to change the definition of the versnissagecmd.exe file path.
    :param path: str containing the new file path to vernissagecmd.exe.
    :return: None
    """

    global vernissagecmd_path  # Allows us to change the global value of the path.
    if path == 'default':  # Change the file path back to the default value.
        vernissagecmd_path = default_vernissagecmd_path
        print('VernissageCmd.exe path changed to {path}'.format(path=default_vernissagecmd_path))
    else:  # Change the file path to the new str.
        vernissagecmd_path = path
        print('VernissageCmd.exe path changed to {path}'.format(path=path))


def set_vernissage_exporter(exporter):
    """
    Can be used to set the exporter to be used by vernissagecmd.exe.
    :param exporter: str containing the name of the exporter to be used.
    :return: None
    """
    global vernissage_exporter  # Allows us to change the global value of the exporter.

    # List of allowed exporters.
    exporters = ['BMP Exporter', 'CasaXPS Exporter', 'Flattener', 'IGOR5 Exporter', 'JPG Exporter',
                 'PHI MultiPak Exporter', 'PNG Exporter', 'TIFF Exporter', 'VAMAS Exporter', 'XY Curve Exporter']

    if exporter == 'default':  # Reset back to the default value.
        vernissage_exporter = default_vernissage_exporter
        print('Vernissage exporter changed to: {exporter}'.format(exporter=default_vernissage_exporter))

    elif exporter not in exporters:  # If not in the allowed list do nothing and print 'error'.
        print('Unknown Exporter: {exporter}. Please use one of {exporters}.'.format(exporter=exporter,
                                                                                    exporters=exporters))
    else:  # Change the exporter and print to confirm.
        vernissage_exporter = exporter
        print('Vernissage exporter changed to: {exporter}'.format(exporter=exporter))


def convert(input_dir, output_dir, verbose=True, stdout=None, stderr=None):
    """
    Used to convert mtrx files using vernissagecmd.exe.
    :param input_dir: str - containing the path to the input directory with files to be converted.
    :param output_dir: str - containing the path to output the converted data files.
    :param verbose: Bool - defines if processes are quitely.
    :param stdout:
    :param stderr:
    :return: None.
    """
    input_dir = os.path.normpath(input_dir)  # Define an explicit os path.
    output_dir = os.path.normpath(output_dir)  # Define an explicit os path.

    if not os.path.isdir(output_dir):  # If there is no existing output directory.
        if verbose:
            print('Creating {output}'.format(output=output_dir))
        os.mkdir(output_dir)  # Creates output directory.

    # Construct a str of command line arguments to pass to subprocess.
    cmd_list = str.join(' ', (vernissagecmd_path,  # VernissageCmd.exe file path.
                              # VernissageCmd.exe arguments
                              '-path "{path}"'.format(path=input_dir),  # input directory path.
                              '-outdir "{outdir}"'.format(outdir=output_dir),  # output directory path.
                              '-exporter {exporter}'.format(exporter=vernissage_exporter)))  # exporter to be used.
    print(cmd_list)
    if verbose:  # if not quite print where converted data is created.
        print('Converting data to: {out}'.format(out=output_dir))

    # run command line arguments.
    subprocess.run(cmd_list, stdout=stdout, stderr=stderr)
