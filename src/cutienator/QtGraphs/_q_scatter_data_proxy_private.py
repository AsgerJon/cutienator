"""
QScatterDataProxyPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/qscatterdataproxy_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QScatterDataProxyPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QAbstractDataProxyPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QAbstract3DAxis, QAbstract3DSeries, QScatterDataProxy
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstract3DAxis = WAIT['QtGraphs:QAbstract3DAxis']
  QAbstract3DSeries = WAIT['QtGraphs:QAbstract3DSeries']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QScatterDataProxyPrivate(QAbstractDataProxyPrivate):
  """
  The cute side of Qt's QScatterDataProxyPrivate: a plain Python object
  standing in front of one C++ QScatterDataProxyPrivate.

  It is built on the cute 'QAbstractDataProxyPrivate', as Qt's
  QScatterDataProxyPrivate is built on Qt's QAbstractDataProxyPrivate, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QScatterDataProxyPrivate that has a ritual and that
  Python can call so far, 4 names in all: 'q_func', 'removeItems',
  'isValidValue', 'setSeries'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QScatterDataProxy *QScatterDataProxyPrivate::q_func() const':
    takes in Python what 'QScatterDataProxy
    *QScatterDataProxyPrivate::q_func()' takes.
  - Qt's 'QScatterDataProxyPrivate::~QScatterDataProxyPrivate()': the
    destructor: Python never removes a C++ QScatterDataProxyPrivate.
  - Qt's 'void QScatterDataProxyPrivate::resetArray(QScatterDataArray
    &&newArray)': takes a type Python has no way to hand over yet.
  - Qt's 'void QScatterDataProxyPrivate::resetScaleArray(QList<QVector3D>
    &&newArray)': takes a type Python has no way to hand over yet.
  - Qt's 'void QScatterDataProxyPrivate::setItem(qsizetype index,
    QScatterDataItem &&item)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QScatterDataProxyPrivate::setItems(qsizetype index,
    QScatterDataArray &&items)': takes a type Python has no way to hand over
    yet.
  - Qt's 'qsizetype QScatterDataProxyPrivate::addItem(QScatterDataItem
    &&item)': takes a type Python has no way to hand over yet.
  - Qt's 'qsizetype QScatterDataProxyPrivate::addItems(QScatterDataArray
    &&items)': takes a type Python has no way to hand over yet.
  - Qt's 'void QScatterDataProxyPrivate::insertItem(qsizetype index,
    QScatterDataItem &&item)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QScatterDataProxyPrivate::insertItems(qsizetype index,
    QScatterDataArray &&items)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QScatterDataProxyPrivate::limitValues(QVector3D &minValues,
    QVector3D &maxValues, QAbstract3DAxis *axisX, QAbstract3DAxis *axisY,
    QAbstract3DAxis *axisZ) const': takes a type Python has no way to hand
    over yet.

  What to expect
  --------------

  - The C++ QScatterDataProxyPrivate is created at the first use, not by
    'QScatterDataProxyPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QScatterDataProxyPrivate.
  - Each name of Qt's QScatterDataProxyPrivate that has no cute function yet,
    'addItem', 'addItems', 'insertItem', 'insertItems', 'limitValues',
    'resetArray', 'resetScaleArray', 'setItem', 'setItems', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScatterDataProxyPrivate'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

  #  A C++ QScatterDataProxyPrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QScatterDataProxyPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float, float, QAbstract3DAxis)
  @overload(float, float, NoneType)
  def isValidValue(
      self,
      axisValue: float,
      value: float,
      axis: Optional[QAbstract3DAxis],
  ) -> bool:
    """
    Calls Qt's 'bool QScatterDataProxyPrivate::isValidValue(float axisValue,
    float value, QAbstract3DAxis *axis) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatterdataproxyprivate.html#isValidValue

    Parameters
    ----------

    axisValue : float
      Passed on as it is.

    value : float
      Passed on as it is.

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QScatterDataProxyPrivate::isValidValue(float axisValue, float
    #      value, QAbstract3DAxis *axis) const
    return self.uglySide.call(
        'ritual_ZNK24QScatterDataProxyPrivate12isValidValueEffP15QAbstract3'
        'DAxis',
        axisValue, value, self._addressOf(axis),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstract3DSeries)
  @overload(NoneType)
  def setSeries(self, series: Optional[QAbstract3DSeries]) -> None:
    """
    Calls Qt's 'void QScatterDataProxyPrivate::setSeries(QAbstract3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatterdataproxyprivate.html#setSeries

    Parameters
    ----------

    series : Optional[QAbstract3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScatterDataProxyPrivate::setSeries(QAbstract3DSeries *series)
    ritual = (
        'ritual_ZN24QScatterDataProxyPrivate9setSeriesEP17QAbstract3DSeries')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QScatterDataProxyPrivate9setSeriesEP17QAbstract3D'
          'Series')
    self.uglySide.call(ritual, self._addressOf(series))

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
    'QScatterDataProxyPrivate::QScatterDataProxyPrivate()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatterdataproxyprivate.html
    """
    #  QScatterDataProxyPrivate::QScatterDataProxyPrivate()
    self._noteCreation(QScatterDataProxyPrivate, lambda: Rituals.call(
        'ritual_ZN24QScatterDataProxyPrivateC1Ev',
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

  def q_func(self) -> Optional[QScatterDataProxy]:
    """
    Calls Qt's 'QScatterDataProxy *QScatterDataProxyPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatterdataproxyprivate.html#q_func

    Returns
    -------

    Optional[QScatterDataProxy]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScatterDataProxy *QScatterDataProxyPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN24QScatterDataProxyPrivate6q_funcEv',
    )
    from . import QScatterDataProxy
    return QScatterDataProxy._cuteAt(address)

  @overload(int, int)
  def removeItems(self, index: int, removeCount: int) -> None:
    """
    Calls Qt's 'void QScatterDataProxyPrivate::removeItems(qsizetype index,
    qsizetype removeCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatterdataproxyprivate.html#removeItems

    Parameters
    ----------

    index : int
      Passed on as it is.

    removeCount : int
      Passed on as it is.
    """
    #  void QScatterDataProxyPrivate::removeItems(qsizetype index, qsizetype
    #      removeCount)
    self.uglySide.call(
        'ritual_ZN24QScatterDataProxyPrivate11removeItemsExx',
        index, removeCount,
    )

  @staticmethod
  def addItem(*__, **_) -> Never:
    """
    Qt's 'qsizetype QScatterDataProxyPrivate::addItem(QScatterDataItem
    &&item)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QScatterDataProxyPrivate.addItem' has no cute function yet. Qt's "
        "'qsizetype QScatterDataProxyPrivate::addItem(QScatterDataItem "
        "&&item)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def addItems(*__, **_) -> Never:
    """
    Qt's 'qsizetype QScatterDataProxyPrivate::addItems(QScatterDataArray
    &&items)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QScatterDataProxyPrivate.addItems' has no cute function yet. Qt's "
        "'qsizetype QScatterDataProxyPrivate::addItems(QScatterDataArray "
        "&&items)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def insertItem(*__, **_) -> Never:
    """
    Qt's 'void QScatterDataProxyPrivate::insertItem(qsizetype index,
    QScatterDataItem &&item)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QScatterDataProxyPrivate.insertItem' has no cute function yet. "
        "Qt's 'void QScatterDataProxyPrivate::insertItem(qsizetype index, "
        "QScatterDataItem &&item)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def insertItems(*__, **_) -> Never:
    """
    Qt's 'void QScatterDataProxyPrivate::insertItems(qsizetype index,
    QScatterDataArray &&items)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QScatterDataProxyPrivate.insertItems' has no cute function yet. "
        "Qt's 'void QScatterDataProxyPrivate::insertItems(qsizetype index, "
        "QScatterDataArray &&items)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def limitValues(*__, **_) -> Never:
    """
    Qt's 'void QScatterDataProxyPrivate::limitValues(QVector3D &minValues,
    QVector3D &maxValues, QAbstract3DAxis *axisX, QAbstract3DAxis *axisY,
    QAbstract3DAxis *axisZ) const': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QScatterDataProxyPrivate.limitValues' has no cute function yet. "
        "Qt's 'void QScatterDataProxyPrivate::limitValues(QVector3D "
        "&minValues, QVector3D &maxValues, QAbstract3DAxis *axisX, "
        "QAbstract3DAxis *axisY, QAbstract3DAxis *axisZ) const': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def resetArray(*__, **_) -> Never:
    """
    Qt's 'void QScatterDataProxyPrivate::resetArray(QScatterDataArray
    &&newArray)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QScatterDataProxyPrivate.resetArray' has no cute function yet. "
        "Qt's 'void QScatterDataProxyPrivate::resetArray(QScatterDataArray "
        "&&newArray)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def resetScaleArray(*__, **_) -> Never:
    """
    Qt's 'void QScatterDataProxyPrivate::resetScaleArray(QList<QVector3D>
    &&newArray)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QScatterDataProxyPrivate.resetScaleArray' has no cute function "
        "yet. Qt's 'void "
        "QScatterDataProxyPrivate::resetScaleArray(QList<QVector3D> "
        "&&newArray)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setItem(*__, **_) -> Never:
    """
    Qt's 'void QScatterDataProxyPrivate::setItem(qsizetype index,
    QScatterDataItem &&item)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QScatterDataProxyPrivate.setItem' has no cute function yet. Qt's "
        "'void QScatterDataProxyPrivate::setItem(qsizetype index, "
        "QScatterDataItem &&item)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def setItems(*__, **_) -> Never:
    """
    Qt's 'void QScatterDataProxyPrivate::setItems(qsizetype index,
    QScatterDataArray &&items)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QScatterDataProxyPrivate.setItems' has no cute function yet. Qt's "
        "'void QScatterDataProxyPrivate::setItems(qsizetype index, "
        "QScatterDataArray &&items)': takes a type Python has no way to "
        "hand over yet.")
