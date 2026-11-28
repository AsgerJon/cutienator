"""
QNmeaRealTimeReader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioning/6.12.0/QtPositioning/private/qnmeapositioninfosource_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QNmeaRealTimeReader to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QNmeaReader

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QNmeaRealTimeReader(QNmeaReader):
  """
  The cute side of Qt's QNmeaRealTimeReader: a plain Python object standing
  in front of one C++ QNmeaRealTimeReader.

  It is built on the cute 'QNmeaReader', as Qt's QNmeaRealTimeReader is built
  on Qt's QNmeaReader, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QNmeaRealTimeReader that has a ritual and that
  Python can call so far, 2 names in all: 'readAvailableData',
  'notifyNewUpdate'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNmeaRealTimeReader::~QNmeaRealTimeReader()': the destructor:
    Python never removes a C++ QNmeaRealTimeReader.

  What has no ritual
  ------------------

  1 of the 4 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QNmeaRealTimeReader is created at the first use, not by
    'QNmeaRealTimeReader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNmeaRealTimeReader.
  - Each name of Qt's QNmeaRealTimeReader that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNmeaRealTimeReader'

  #  A C++ QNmeaRealTimeReader Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNmeaRealTimeReader'

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
    Qt's
    'QNmeaRealTimeReader::QNmeaRealTimeReader(QNmeaPositionInfoSourcePrivate
    *sourcePrivate)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: unknown type name
    'QGeoPositionInfoPrivateNmea'; did you mean 'QGeoPositionInfoPrivate'?.
    """
    raise NotImplementedError(
        "'QNmeaRealTimeReader.__init__' has no cute function yet. Qt's "
        "'QNmeaRealTimeReader::QNmeaRealTimeReader(QNmeaPositionInfoSourcePr"
        "ivate *sourcePrivate)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: unknown "
        "type name 'QGeoPositionInfoPrivateNmea'; did you mean "
        "'QGeoPositionInfoPrivate'?.")

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
    Calls Qt's 'void QNmeaRealTimeReader::readAvailableData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmearealtimereader.html#readAvailableData
    """
    #  void QNmeaRealTimeReader::readAvailableData()
    self.uglySide.call('ritual_ZN19QNmeaRealTimeReader17readAvailableDataEv')

  def notifyNewUpdate(self) -> None:
    """
    Calls Qt's 'void QNmeaRealTimeReader::notifyNewUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmearealtimereader.html#notifyNewUpdate
    """
    #  void QNmeaRealTimeReader::notifyNewUpdate()
    self.uglySide.call('ritual_ZN19QNmeaRealTimeReader15notifyNewUpdateEv')
