"""
QQuickProfilerData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickprofiler_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickProfilerData to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']


class QQuickProfilerData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickProfilerData: a plain Python object standing in
  front of one C++ QQuickProfilerData.

  C++ hands a QQuickProfilerData around as a copy, so every C++
  QQuickProfilerData behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QQuickProfilerData yet. It can be made from Python, in
  4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickProfilerData::~QQuickProfilerData()': the destructor: Python
    removes its C++ QQuickProfilerData by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQuickProfilerData is created at the first use, not by
    'QQuickProfilerData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickProfilerData back gives a copy the ritual made
    for Python, in a new cute QQuickProfilerData.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickProfilerData'

  #  Qt's '~QQuickProfilerData()'. Naming it makes this a value class: Python
  #  owns every C++ QQuickProfilerData behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QQuickProfilerDataD1Ev'

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
    'QQuickProfilerData::QQuickProfilerData()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickprofilerdata.html#QQuickProfilerData
    """
    #  QQuickProfilerData::QQuickProfilerData()
    self._noteCreation(QQuickProfilerData, lambda: Rituals.call(
        'ritual_ZN18QQuickProfilerDataC1Ev',
    ))

  @overload(int, int, int, QUrl)
  @overload(int, int, int, QUrl, int)
  @overload(int, int, int, QUrl, int, int)
  @overload(int, int, int, QUrl, int, int, int)
  @overload(int, int, int, QUrl, int, int, int, int)
  def __init__(
      self,
      time: int,
      messageType: int,
      detailType: int,
      url: QUrl,
      x: int = 0,
      y: int = 0,
      framerate: int = 0,
      count: int = 0,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQuickProfilerData::QQuickProfilerData(qint64 time, int messageType, int
    detailType, const QUrl &url, int x, int y, int framerate, int count)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickprofilerdata.html#QQuickProfilerData

    Parameters
    ----------

    time : int
      Passed on as it is.

    messageType : int
      Passed on as it is.

    detailType : int
      Passed on as it is.

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    x : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    y : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    framerate : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    count : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  QQuickProfilerData::QQuickProfilerData(qint64 time, int messageType,
    #      int detailType, const QUrl &url, int x, int y, int framerate, int
    #      count)
    self._noteCreation(QQuickProfilerData, lambda: Rituals.call(
        'ritual_ZN18QQuickProfilerDataC1ExiiRK4QUrliiii',
        time, messageType, detailType, self._valueOf(url), x, y, framerate,
        count,
    ))

  @overload(int, int, int)
  @overload(int, int, int, int)
  @overload(int, int, int, int, int)
  @overload(int, int, int, int, int, int)
  def __init__(
      self,
      time: int,
      messageType: int,
      detailType: int,
      framerateOrInputType: int = 0,
      countOrInputA: int = 0,
      threadIdOrInputB: int = 0,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQuickProfilerData::QQuickProfilerData(qint64 time, int messageType, int
    detailType, int framerateOrInputType, int countOrInputA, int
    threadIdOrInputB)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickprofilerdata.html#QQuickProfilerData

    Parameters
    ----------

    time : int
      Passed on as it is.

    messageType : int
      Passed on as it is.

    detailType : int
      Passed on as it is.

    framerateOrInputType : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    countOrInputA : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    threadIdOrInputB : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  QQuickProfilerData::QQuickProfilerData(qint64 time, int messageType,
    #      int detailType, int framerateOrInputType, int countOrInputA, int
    #      threadIdOrInputB)
    self._noteCreation(QQuickProfilerData, lambda: Rituals.call(
        'ritual_ZN18QQuickProfilerDataC1Exiiiii',
        time, messageType, detailType, framerateOrInputType, countOrInputA,
        threadIdOrInputB,
    ))

  @overload(int, int, int, int, int, int, int, int)
  def __init__(
      self,
      time: int,
      messageType: int,
      detailType: int,
      d1: int,
      d2: int,
      d3: int,
      d4: int,
      d5: int,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQuickProfilerData::QQuickProfilerData(qint64 time, int messageType, int
    detailType, qint64 d1, qint64 d2, qint64 d3, qint64 d4, qint64 d5)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickprofilerdata.html#QQuickProfilerData

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

    d3 : int
      Passed on as it is.

    d4 : int
      Passed on as it is.

    d5 : int
      Passed on as it is.
    """
    #  QQuickProfilerData::QQuickProfilerData(qint64 time, int messageType,
    #      int detailType, qint64 d1, qint64 d2, qint64 d3, qint64 d4, qint64
    #      d5)
    self._noteCreation(QQuickProfilerData, lambda: Rituals.call(
        'ritual_ZN18QQuickProfilerDataC1Exiixxxxx',
        time, messageType, detailType, d1, d2, d3, d4, d5,
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


#  Qt's 'QList<QQuickProfilerData>': the list of QQuickProfilerData, which
#  'QList[QQuickProfilerData]' gives. It is made here, so that there is one
#  as soon as there can be a QQuickProfilerData.
QList.createKind(
    QQuickProfilerData, 'value',
    make='ritual_list_make_QQuickProfilerData',
    add='ritual_list_add_QQuickProfilerData',
    size='ritual_list_size_QQuickProfilerData',
    at='ritual_list_at_QQuickProfilerData',
    drop='ritual_list_drop_QQuickProfilerData',
)
