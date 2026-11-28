"""
QNmeaSatelliteSimulationReader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioning/6.12.0/QtPositioning/private/qnmeasatelliteinfosource_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QNmeaSatelliteSimulationReader to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from . import QNmeaSatelliteReader

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QNmeaSatelliteSimulationReader(QNmeaSatelliteReader):
  """
  The cute side of Qt's QNmeaSatelliteSimulationReader: a plain Python object
  standing in front of one C++ QNmeaSatelliteSimulationReader.

  It is built on the cute 'QNmeaSatelliteReader', as Qt's
  QNmeaSatelliteSimulationReader is built on Qt's QNmeaSatelliteReader, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QNmeaSatelliteSimulationReader that has a ritual and
  that Python can call so far, 3 names in all: 'readAvailableData',
  'setUpdateInterval', 'updateInterval'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has no ritual
  ------------------

  1 of the 4 functions Qt declares: 1 leans on
  'QNmeaSatelliteInfoSourcePrivate.

  What to expect
  --------------

  - The C++ QNmeaSatelliteSimulationReader is created at the first use, not
    by 'QNmeaSatelliteSimulationReader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNmeaSatelliteSimulationReader.
  - Each name of Qt's QNmeaSatelliteSimulationReader that has no cute
    function yet, '__init__', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNmeaSatelliteSimulationReader'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def updateInterval(self) -> int:
    """
    Calls Qt's 'int QNmeaSatelliteSimulationReader::updateInterval() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeasatellitesimulationreader.html#updateInterval
    """
    #  int QNmeaSatelliteSimulationReader::updateInterval() const
    return self.uglySide.call(
        'ritual_ZNK30QNmeaSatelliteSimulationReader14updateIntervalEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setUpdateInterval(self, msec: int) -> None:
    """
    Calls Qt's 'void QNmeaSatelliteSimulationReader::setUpdateInterval(int
    msec)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeasatellitesimulationreader.html

    Parameters
    ----------

    msec : int
      Passed on as it is.
    """
    #  void QNmeaSatelliteSimulationReader::setUpdateInterval(int msec)
    self.uglySide.call(
        'ritual_ZN30QNmeaSatelliteSimulationReader17setUpdateIntervalEi',
        msec,
    )

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
    Qt's 'QNmeaSatelliteSimulationReader::QNmeaSatelliteSimulationReader(
    QNmeaSatelliteInfoSourcePrivate *sourcePrivate)': leans on
    'QNmeaSatelliteInfoSourcePrivate::processNmeaData(
    QNmeaSatelliteInfoUpdate&)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QNmeaSatelliteSimulationReader.__init__' has no cute function "
        "yet. Qt's "
        "'QNmeaSatelliteSimulationReader::QNmeaSatelliteSimulationReader(QNm"
        "eaSatelliteInfoSourcePrivate *sourcePrivate)': leans on "
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
    Calls Qt's 'void QNmeaSatelliteSimulationReader::readAvailableData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnmeasatellitesimulationreader.html
    """
    #  void QNmeaSatelliteSimulationReader::readAvailableData()
    self.uglySide.call(
        'ritual_ZN30QNmeaSatelliteSimulationReader17readAvailableDataEv',
    )
