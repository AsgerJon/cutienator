"""
QNmeaSatelliteRealTimeReader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioning/6.12.0/QtPositioning/private/qnmeasatelliteinfosource_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QNmeaSatelliteRealTimeReader to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QNmeaSatelliteReader

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QNmeaSatelliteRealTimeReader(QNmeaSatelliteReader):
  """
  The cute side of Qt's QNmeaSatelliteRealTimeReader: a plain Python object
  standing in front of one C++ QNmeaSatelliteRealTimeReader.

  It is built on the cute 'QNmeaSatelliteReader', as Qt's
  QNmeaSatelliteRealTimeReader is built on Qt's QNmeaSatelliteReader, and has
  everything that class has.

  C++ hands a QNmeaSatelliteRealTimeReader around as a copy, so every C++
  QNmeaSatelliteRealTimeReader behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QNmeaSatelliteRealTimeReader that has a ritual and
  that Python can call so far, 1 name in all: 'readAvailableData'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNmeaSatelliteRealTimeReader::~QNmeaSatelliteRealTimeReader()': the
    destructor: Python removes its C++ QNmeaSatelliteRealTimeReader by it,
    and has no other use for it.

  What has no ritual
  ------------------

  1 of the 3 functions Qt declares: 1 leans on
  'QNmeaSatelliteInfoSourcePrivate.

  What to expect
  --------------

  - The C++ QNmeaSatelliteRealTimeReader is created at the first use, not by
    'QNmeaSatelliteRealTimeReader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QNmeaSatelliteRealTimeReader back gives a copy the
    ritual made for Python, in a new cute QNmeaSatelliteRealTimeReader.
  - Each name of Qt's QNmeaSatelliteRealTimeReader that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNmeaSatelliteRealTimeReader'

  #  A C++ QNmeaSatelliteRealTimeReader Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNmeaSatelliteRealTimeReader'

  #  Qt's '~QNmeaSatelliteRealTimeReader()'. Naming it makes this a value
  #  class: Python owns every C++ QNmeaSatelliteRealTimeReader behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN28QNmeaSatelliteRealTimeReaderD1Ev'

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QNmeaSatelliteRealTimeReader::QNmeaSatelliteRealTimeReader(
    QNmeaSatelliteInfoSourcePrivate *sourcePrivate)': leans on
    'QNmeaSatelliteInfoSourcePrivate::processNmeaData(
    QNmeaSatelliteInfoUpdate&)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QNmeaSatelliteRealTimeReader.__init__' has no cute function yet. "
        "Qt's "
        "'QNmeaSatelliteRealTimeReader::QNmeaSatelliteRealTimeReader(QNmeaSa"
        "telliteInfoSourcePrivate *sourcePrivate)': leans on "
        "'QNmeaSatelliteInfoSourcePrivate::processNmeaData(QNmeaSatelliteInf"
        "oUpdate&)', which Qt's source does not mark for use from outside "
        "Qt and has no code for that could be taken.")

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

  def readAvailableData(self) -> None:
    """
    Calls Qt's 'void QNmeaSatelliteRealTimeReader::readAvailableData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeasatelliterealtimereader.html
    """
    #  void QNmeaSatelliteRealTimeReader::readAvailableData()
    self.uglySide.call(
        'ritual_ZN28QNmeaSatelliteRealTimeReader17readAvailableDataEv',
    )
