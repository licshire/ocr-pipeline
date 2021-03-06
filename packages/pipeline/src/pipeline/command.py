"""Command object

.. Authors:
    Philippe Dessauw
    philippe.dessauw@nist.gov

.. Sponsor:
    Alden Dima
    alden.dima@nist.gov
    Information Systems Group
    Software and Systems Division
    Information Technology Laboratory
    National Institute of Standards and Technology
    http://www.nist.gov/itl/ssd/is
"""
from apputils.fileop import zip_directory, unzip_directory
from pipeline.files import FileManager


class Command(object):
    """Main command object
    """

    def __init__(self, filename, logger, app_config):
        self.logger = logger

        # ip = app_config["machines"]["master"][0].split('@')
        # master_ip = ip[-1:][0]
        # master_queue_port = app_config["redis"]["port"]
        # self.fman = FileManager(master_ip, master_queue_port)

        self.filename = filename
        # self.unzipped = None
        self.unzipped = filename
        self.config = app_config

        self.logger.debug("File to be processed: %s" % str(self.unzipped))

    # def get_file(self):
    #     """Retrieve file from redis and unzip it to the local filesystem
    #     """
    #     # Get hash from redis
    #     self.logger.debug("Retrieving "+self.filename+"...")
    #     self.fman.retrieve_file(self.filename)
    #
    #     # Write it in the tmp folder
    #     self._unzip_file()

    # def store_file(self):
    #     """Zip file on the local filesystem and store it to redis
    #     """
    #     self._zip_file()
    #
    #     # Store it in redis
    #     self.fman.store_file(self.filename)

    # def _zip_file(self):
    #     """Check if the file can be zipped and zip it
    #     """
    #     if self.unzipped is None:
    #         self.logger.error("Zipped directory has not been unzipped")
    #         return
    #
    #     zip_directory(self.unzipped)
    #     self.unzipped = None

    # def _unzip_file(self):
    #     """Check if the file can be unzipped and unzip it
    #     """
    #     if self.unzipped is not None:
    #         self.logger.error("Archive already unzipped")
    #         return
    #
    #     self.unzipped = unzip_directory(self.filename)
