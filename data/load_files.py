#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
"""
================================================
Project:    <Sentiment Analytics>
Module:     <Data Handler>
Author:     <Sven Bodemer>
================================================
Contact:    <sbodemer.student@gmail.com>

================================================
"""
import data
import os


def get_path(fname):
    data_dir = os.path.join(os.path.dirname(data.__file__))
    return os.path.join(data_dir, fname)


def read_stopwords(fname):
    with open(get_path(fname)) as stream:
        lines = stream.readlines()
    return [l.rstrip() for l in lines]
