"""
QSurfaceDataProxyPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/qsurfacedataproxy_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSurfaceDataProxyPrivate to be private: it declares the class in
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

  from . import QAbstract3DAxis, QAbstract3DSeries, QSurfaceDataProxy
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstract3DAxis = WAIT['QtGraphs:QAbstract3DAxis']
  QAbstract3DSeries = WAIT['QtGraphs:QAbstract3DSeries']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSurfaceDataProxyPrivate(QAbstractDataProxyPrivate):
  """
  The cute side of Qt's QSurfaceDataProxyPrivate: a plain Python object
  standing in front of one C++ QSurfaceDataProxyPrivate.

  It is built on the cute 'QAbstractDataProxyPrivate', as Qt's
  QSurfaceDataProxyPrivate is built on Qt's QAbstractDataProxyPrivate, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QSurfaceDataProxyPrivate that has a ritual and that
  Python can call so far, 4 names in all: 'q_func', 'removeRows',
  'isValidValue', 'setSeries'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QSurfaceDataProxy *QSurfaceDataProxyPrivate::q_func() const':
    takes in Python what 'QSurfaceDataProxy
    *QSurfaceDataProxyPrivate::q_func()' takes.
  - Qt's 'QSurfaceDataProxyPrivate::~QSurfaceDataProxyPrivate()': the
    destructor: Python never removes a C++ QSurfaceDataProxyPrivate.
  - Qt's 'void QSurfaceDataProxyPrivate::resetArray(QSurfaceDataArray
    &&newArray)': takes a type Python has no way to hand over yet.
  - Qt's 'void QSurfaceDataProxyPrivate::setRow(qsizetype rowIndex,
    QSurfaceDataRow &&row)': takes a type Python has no way to hand over yet.
  - Qt's 'void QSurfaceDataProxyPrivate::setRows(qsizetype rowIndex,
    QSurfaceDataArray &&rows)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QSurfaceDataProxyPrivate::setItem(qsizetype rowIndex,
    qsizetype columnIndex, QSurfaceDataItem &&item)': takes a type Python has
    no way to hand over yet.
  - Qt's 'qsizetype QSurfaceDataProxyPrivate::addRow(QSurfaceDataRow &&row)':
    takes a type Python has no way to hand over yet.
  - Qt's 'qsizetype QSurfaceDataProxyPrivate::addRows(QSurfaceDataArray
    &&rows)': takes a type Python has no way to hand over yet.
  - Qt's 'void QSurfaceDataProxyPrivate::insertRow(qsizetype rowIndex,
    QSurfaceDataRow &&row)': takes a type Python has no way to hand over yet.
  - Qt's 'void QSurfaceDataProxyPrivate::insertRows(qsizetype rowIndex,
    QSurfaceDataArray &&rows)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QSurfaceDataProxyPrivate::limitValues(QVector3D &minValues,
    QVector3D &maxValues, QAbstract3DAxis *axisX, QAbstract3DAxis *axisY,
    QAbstract3DAxis *axisZ) const': takes a type Python has no way to hand
    over yet.

  What to expect
  --------------

  - The C++ QSurfaceDataProxyPrivate is created at the first use, not by
    'QSurfaceDataProxyPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSurfaceDataProxyPrivate.
  - Each name of Qt's QSurfaceDataProxyPrivate that has no cute function yet,
    'addRow', 'addRows', 'insertRow', 'insertRows', 'limitValues',
    'resetArray', 'setItem', 'setRow', 'setRows', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSurfaceDataProxyPrivate'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

  #  A C++ QSurfaceDataProxyPrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSurfaceDataProxyPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float, QAbstract3DAxis)
  @overload(float, NoneType)
  def isValidValue(
      self,
      value: float,
      axis: Optional[QAbstract3DAxis],
  ) -> bool:
    """
    Calls Qt's 'bool QSurfaceDataProxyPrivate::isValidValue(float value,
    QAbstract3DAxis *axis) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfacedataproxyprivate.html#isValidValue

    Parameters
    ----------

    value : float
      Passed on as it is.

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSurfaceDataProxyPrivate::isValidValue(float value,
    #      QAbstract3DAxis *axis) const
    return self.uglySide.call(
        'ritual_ZNK24QSurfaceDataProxyPrivate12isValidValueEfP15QAbstract3D'
        'Axis',
        value, self._addressOf(axis),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstract3DSeries)
  @overload(NoneType)
  def setSeries(self, series: Optional[QAbstract3DSeries]) -> None:
    """
    Calls Qt's 'void QSurfaceDataProxyPrivate::setSeries(QAbstract3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfacedataproxyprivate.html#setSeries

    Parameters
    ----------

    series : Optional[QAbstract3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSurfaceDataProxyPrivate::setSeries(QAbstract3DSeries *series)
    ritual = (
        'ritual_ZN24QSurfaceDataProxyPrivate9setSeriesEP17QAbstract3DSeries')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QSurfaceDataProxyPrivate9setSeriesEP17QAbstract3D'
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
    'QSurfaceDataProxyPrivate::QSurfaceDataProxyPrivate()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfacedataproxyprivate.html
    """
    #  QSurfaceDataProxyPrivate::QSurfaceDataProxyPrivate()
    self._noteCreation(QSurfaceDataProxyPrivate, lambda: Rituals.call(
        'ritual_ZN24QSurfaceDataProxyPrivateC1Ev',
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

  def q_func(self) -> Optional[QSurfaceDataProxy]:
    """
    Calls Qt's 'QSurfaceDataProxy *QSurfaceDataProxyPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfacedataproxyprivate.html#q_func

    Returns
    -------

    Optional[QSurfaceDataProxy]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSurfaceDataProxy *QSurfaceDataProxyPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN24QSurfaceDataProxyPrivate6q_funcEv',
    )
    from . import QSurfaceDataProxy
    return QSurfaceDataProxy._cuteAt(address)

  @overload(int, int)
  def removeRows(self, rowIndex: int, removeCount: int) -> None:
    """
    Calls Qt's 'void QSurfaceDataProxyPrivate::removeRows(qsizetype rowIndex,
    qsizetype removeCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfacedataproxyprivate.html#removeRows

    Parameters
    ----------

    rowIndex : int
      Passed on as it is.

    removeCount : int
      Passed on as it is.
    """
    #  void QSurfaceDataProxyPrivate::removeRows(qsizetype rowIndex,
    #      qsizetype removeCount)
    self.uglySide.call(
        'ritual_ZN24QSurfaceDataProxyPrivate10removeRowsExx',
        rowIndex, removeCount,
    )

  @staticmethod
  def addRow(*__, **_) -> Never:
    """
    Qt's 'qsizetype QSurfaceDataProxyPrivate::addRow(QSurfaceDataRow &&row)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSurfaceDataProxyPrivate.addRow' has no cute function yet. Qt's "
        "'qsizetype QSurfaceDataProxyPrivate::addRow(QSurfaceDataRow "
        "&&row)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def addRows(*__, **_) -> Never:
    """
    Qt's 'qsizetype QSurfaceDataProxyPrivate::addRows(QSurfaceDataArray
    &&rows)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSurfaceDataProxyPrivate.addRows' has no cute function yet. Qt's "
        "'qsizetype QSurfaceDataProxyPrivate::addRows(QSurfaceDataArray "
        "&&rows)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def insertRow(*__, **_) -> Never:
    """
    Qt's 'void QSurfaceDataProxyPrivate::insertRow(qsizetype rowIndex,
    QSurfaceDataRow &&row)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSurfaceDataProxyPrivate.insertRow' has no cute function yet. "
        "Qt's 'void QSurfaceDataProxyPrivate::insertRow(qsizetype rowIndex, "
        "QSurfaceDataRow &&row)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def insertRows(*__, **_) -> Never:
    """
    Qt's 'void QSurfaceDataProxyPrivate::insertRows(qsizetype rowIndex,
    QSurfaceDataArray &&rows)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QSurfaceDataProxyPrivate.insertRows' has no cute function yet. "
        "Qt's 'void QSurfaceDataProxyPrivate::insertRows(qsizetype "
        "rowIndex, QSurfaceDataArray &&rows)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def limitValues(*__, **_) -> Never:
    """
    Qt's 'void QSurfaceDataProxyPrivate::limitValues(QVector3D &minValues,
    QVector3D &maxValues, QAbstract3DAxis *axisX, QAbstract3DAxis *axisY,
    QAbstract3DAxis *axisZ) const': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QSurfaceDataProxyPrivate.limitValues' has no cute function yet. "
        "Qt's 'void QSurfaceDataProxyPrivate::limitValues(QVector3D "
        "&minValues, QVector3D &maxValues, QAbstract3DAxis *axisX, "
        "QAbstract3DAxis *axisY, QAbstract3DAxis *axisZ) const': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def resetArray(*__, **_) -> Never:
    """
    Qt's 'void QSurfaceDataProxyPrivate::resetArray(QSurfaceDataArray
    &&newArray)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSurfaceDataProxyPrivate.resetArray' has no cute function yet. "
        "Qt's 'void QSurfaceDataProxyPrivate::resetArray(QSurfaceDataArray "
        "&&newArray)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setItem(*__, **_) -> Never:
    """
    Qt's 'void QSurfaceDataProxyPrivate::setItem(qsizetype rowIndex,
    qsizetype columnIndex, QSurfaceDataItem &&item)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSurfaceDataProxyPrivate.setItem' has no cute function yet. Qt's "
        "'void QSurfaceDataProxyPrivate::setItem(qsizetype rowIndex, "
        "qsizetype columnIndex, QSurfaceDataItem &&item)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def setRow(*__, **_) -> Never:
    """
    Qt's 'void QSurfaceDataProxyPrivate::setRow(qsizetype rowIndex,
    QSurfaceDataRow &&row)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSurfaceDataProxyPrivate.setRow' has no cute function yet. Qt's "
        "'void QSurfaceDataProxyPrivate::setRow(qsizetype rowIndex, "
        "QSurfaceDataRow &&row)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def setRows(*__, **_) -> Never:
    """
    Qt's 'void QSurfaceDataProxyPrivate::setRows(qsizetype rowIndex,
    QSurfaceDataArray &&rows)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QSurfaceDataProxyPrivate.setRows' has no cute function yet. Qt's "
        "'void QSurfaceDataProxyPrivate::setRows(qsizetype rowIndex, "
        "QSurfaceDataArray &&rows)': takes a type Python has no way to hand "
        "over yet.")
