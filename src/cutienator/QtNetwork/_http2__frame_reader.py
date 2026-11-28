"""
Http2::FrameReader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/http2frames_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Http2::FrameReader to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class FrameReader(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Http2::FrameReader: a plain Python object standing in
  front of one C++ Http2::FrameReader.

  C++ hands a Http2::FrameReader around as a copy, so every C++
  Http2::FrameReader behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's Http2::FrameReader yet. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'FrameStatus Http2::FrameReader::read(QIODevice &socket)': takes a
    type Python has no way to hand over yet.
  - Qt's 'Frame &Http2::FrameReader::inboundFrame()': gives a type Python has
    no way to take yet.
  - Qt's 'bool Http2::FrameReader::readHeader(QIODevice &socket)': takes a
    type Python has no way to hand over yet.
  - Qt's 'bool Http2::FrameReader::readPayload(QIODevice &socket)': takes a
    type Python has no way to hand over yet.
  - Qt's 'bool Http2::FrameReader::discardPayload(QIODevice &socket)': takes
    a type Python has no way to hand over yet.
  - Qt's 'Http2::FrameReader::~FrameReader()': the destructor: Python removes
    its C++ Http2::FrameReader by it, and has no other use for it.

  What to expect
  --------------

  - The C++ Http2::FrameReader is created at the first use, not by
    'Http2::FrameReader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Http2::FrameReader back gives a copy the ritual made
    for Python, in a new cute Http2::FrameReader.
  - Each name of Qt's Http2::FrameReader that has no cute function yet,
    'discardPayload', 'inboundFrame', 'read', 'readHeader', 'readPayload',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Http2::FrameReader'

  #  Qt's '~Http2::FrameReader()'. Naming it makes this a value class: Python
  #  owns every C++ Http2::FrameReader behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN5Http211FrameReaderD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def discardPayload(*__, **_) -> Never:
    """
    Qt's 'bool Http2::FrameReader::discardPayload(QIODevice &socket)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Http2.FrameReader.discardPayload' has no cute function yet. Qt's "
        "'bool Http2::FrameReader::discardPayload(QIODevice &socket)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def inboundFrame(*__, **_) -> Never:
    """
    Qt's 'Frame &Http2::FrameReader::inboundFrame()': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'Http2.FrameReader.inboundFrame' has no cute function yet. Qt's "
        "'Frame &Http2::FrameReader::inboundFrame()': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'FrameStatus Http2::FrameReader::read(QIODevice &socket)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Http2.FrameReader.read' has no cute function yet. Qt's "
        "'FrameStatus Http2::FrameReader::read(QIODevice &socket)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def readHeader(*__, **_) -> Never:
    """
    Qt's 'bool Http2::FrameReader::readHeader(QIODevice &socket)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Http2.FrameReader.readHeader' has no cute function yet. Qt's "
        "'bool Http2::FrameReader::readHeader(QIODevice &socket)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def readPayload(*__, **_) -> Never:
    """
    Qt's 'bool Http2::FrameReader::readPayload(QIODevice &socket)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Http2.FrameReader.readPayload' has no cute function yet. Qt's "
        "'bool Http2::FrameReader::readPayload(QIODevice &socket)': takes a "
        "type Python has no way to hand over yet.")
