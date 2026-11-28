"""
QQuick3DProfilerData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qquick3dprofiler_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DProfilerData to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QQuick3DProfilerData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuick3DProfilerData: a plain Python object standing
  in front of one C++ QQuick3DProfilerData.

  C++ hands a QQuick3DProfilerData around as a copy, so every C++
  QQuick3DProfilerData behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QQuick3DProfilerData yet. It can be made from Python,
  in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuick3DProfilerData::QQuick3DProfilerData(qint64 time, int
    messageType, int detailType, qint64 d1, qint64 d2, const QList<int>
    &ids)': takes a type Python has no way to hand over yet.
  - Qt's 'QQuick3DProfilerData::~QQuick3DProfilerData()': the destructor:
    Python removes its C++ QQuick3DProfilerData by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QQuick3DProfilerData is created at the first use, not by
    'QQuick3DProfilerData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuick3DProfilerData back gives a copy the ritual
    made for Python, in a new cute QQuick3DProfilerData.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DProfilerData'

  #  Qt's '~QQuick3DProfilerData()'. Naming it makes this a value class:
  #  Python owns every C++ QQuick3DProfilerData behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QQuick3DProfilerDataD1Ev'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DProfilerData::QQuick3DProfilerData()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprofilerdata.html#QQuick3DProfilerData
    """
    #  QQuick3DProfilerData::QQuick3DProfilerData()
    self._noteCreation(QQuick3DProfilerData, lambda: Rituals.call(
        'ritual_ZN20QQuick3DProfilerDataC1Ev',
    ))

  @overload(int, int, int, int, int)
  def __init__(
      self,
      time: int,
      messageType: int,
      detailType: int,
      d1: int,
      d2: int,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DProfilerData::QQuick3DProfilerData(qint64 time, int messageType,
    int detailType, qint64 d1, qint64 d2)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprofilerdata.html#QQuick3DProfilerData

    Parameters
    ----------

    time : int
      Passed on as it is.

    messageType : int
      Passed on as it is.

    detailType : int
      Passed on as it is.

    d1 : int
      Passed on as it is.

    d2 : int
      Passed on as it is.
    """
    #  QQuick3DProfilerData::QQuick3DProfilerData(qint64 time, int
    #      messageType, int detailType, qint64 d1, qint64 d2)
    self._noteCreation(QQuick3DProfilerData, lambda: Rituals.call(
        'ritual_ZN20QQuick3DProfilerDataC1Exiixx',
        time, messageType, detailType, d1, d2,
    ))

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
