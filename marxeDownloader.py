#!/usr/bin/python
# coding=utf-8
from __future__ import print_function
from ftplib import FTP


class MarxeDownloader():
    def __init__(self, hostname, user='', passwd=''):
        # Parametros
        self.host = hostname
        self.user = user
        self.passwd = passwd
        self.directory = None
        self.ftp = None
        self.output = None

    def set_user_and_password(self, user, passwd):
        self.user = user
        self.passwd = passwd

    def set_output_directory(self, output):
        self.output = str(output)

    def connect(self):
        try:
            self.ftp = FTP(str(self.host), user=str(self.user), passwd=str(self.passwd))
            self.ftp.login()
            print('Connected to: ' + str(self.host))
        except (Exception) as e:
            print(e)

    def set_directory(self, directory):
        try:
            self.ftp.cwd(directory)
            print('..')
        except (Exception) as e:
            print('Failed to set directory.\n' + str(e))

    def download_one_data(self, filename):
        try:
            self.ftp.retrbinary(str('RETR ' + filename), open(self.output + filename, 'wb').write)
            print("Downloaded: " + str(filename))
        except (Exception) as e:
            print(e)

    def download_many_data(self, filename_list):
        try:
            for filename in filename_list:
                self.ftp.retrbinary(str('RETR ' + filename), open(self.output + filename, 'wb').write)
                print('Downloaded: ' + str(filename))
        except (Exception) as e:
            raise e

    def close(self):
        self.ftp.close()