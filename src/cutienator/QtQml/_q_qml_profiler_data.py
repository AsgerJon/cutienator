"""
QQmlProfilerData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlprofiler_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQmlProfilerData to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtCore import QList
from . import QQmlProfilerDefinitions


class QQmlProfilerData(QQmlProfilerDefinitions):
  """
  The cute side of Qt's QQmlProfilerData: a plain Python object standing in
  front of one C++ QQmlProfilerData.

  It is built on the cute 'QQmlProfilerDefinitions', as Qt's QQmlProfilerData
  is built on Qt's QQmlProfilerDefinitions, and has everything that class
  has.

  C++ hands a QQmlProfilerData around as a copy, so every C++
  QQmlProfilerData behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QQmlProfilerData yet. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlProfilerData::~QQmlProfilerData()': the destructor: Python
    removes its C++ QQmlProfilerData by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQmlProfilerData is created at the first use, not by
    'QQmlProfilerData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlProfilerData back gives a copy the ritual made
    for Python, in a new cute QQmlProfilerData.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlProfilerData'

  #  Qt's '~QQmlProfilerData()'. Naming it makes this a value class: Python
  #  owns every C++ QQmlProfilerData behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QQmlProfilerDataD1Ev'

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
  @overload(int)
  @overload(int, int)
  @overload(int, int, QQmlProfilerDefinitions.RangeType)
  @overload(int, int, QQmlProfilerDefinitions.RangeType, int)
  def __init__(
      self,
      time: int = -1,
      messageType: int = -1,
      detailType: QQmlProfilerDefinitions.RangeType = (
          QQmlProfilerDefinitions.RangeType.MaximumRangeType),
      locationId: int = 0,
  ) -> None:
    """
    Notes what was given, for Qt's 'QQmlProfilerData::QQmlProfilerData(qint64
    time, int messageType, RangeType detailType, quintptr locationId)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlprofilerdata.html#QQmlProfilerData

    Parameters
    ----------

    time : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    messageType : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    detailType : QQmlProfilerDefinitions.RangeType
      Passed on as its number. May be left out, as in Qt: it is then
      QQmlProfilerDefinitions.RangeType.MaximumRangeType.

    locationId : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  QQmlProfilerData::QQmlProfilerData(qint64 time, int messageType,
    #      RangeType detailType, quintptr locationId)
    self._noteCreation(QQmlProfilerData, lambda: Rituals.call(
        'ritual_ZN16QQmlProfilerDataC1ExiN23QQmlProfilerDefinitions9RangeTy'
        'peEy',
        time, messageType, detailType.value, locationId,
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


#  Qt's 'QList<QQmlProfilerData>': the list of QQmlProfilerData, which
#  'QList[QQmlProfilerData]' gives. It is made here, so that there is one as
#  soon as there can be a QQmlProfilerData.
QList.createKind(
    QQmlProfilerData, 'value',
    make='ritual_list_make_QQmlProfilerData',
    add='ritual_list_add_QQmlProfilerData',
    size='ritual_list_size_QQmlProfilerData',
    at='ritual_list_at_QQmlProfilerData',
    drop='ritual_list_drop_QQmlProfilerData',
)
