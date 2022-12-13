# -*- coding: utf8 -*-

"""
实现 HDFS WEB API 的若干协议

https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/WebHDFS.html

作者: 蒋乐兴
日期: 2022-12-13
"""

import os
import sys
import requests

class HDFSProtocol(object):
    """
    实现 HDFS WEB API 协议

    CREATE
    WRITE
    APPEND
    READ
    """
    host = ""

    port = 0

    user = ""

    hdfs_work_dir = "/"


    def __init__(self, host="0.0.0.0", port=0, user=None, ):
        """
        """
        self.host = host
        self.port = port
        self.user = user
        self.session = requests.session()
