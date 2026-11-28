"""
QSurfaceDataProxyPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/qsurfacedataproxy_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSurfaceDataProxyPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QAbstractDataProxyPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QAbstract3DAxis, QAbstract3DSeries, QSurfaceDataItem
  from . import QSurfaceDataProxy
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstract3DAxis = WAIT['QtDataVisualization:QAbstract3DAxis']
  QAbstract3DSeries = WAIT['QtDataVisualization:QAbstract3DSeries']
  QSurfaceDataItem = WAIT['QtDataVisualization:QSurfaceDataItem']

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
  Python can call so far, 8 names in all: 'metaObject', 'setItem',
  'removeRows', 'isValidValue', 'setSeries', 'qptr', 'clearRow',
  'clearArray'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSurfaceDataProxyPrivate::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QSurfaceDataProxyPrivate::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QSurfaceDataProxyPrivate::~QSurfaceDataProxyPrivate()': the
    destructor: Python never removes a C++ QSurfaceDataProxyPrivate.
  - Qt's 'void QSurfaceDataProxyPrivate::resetArray(QSurfaceDataArray
    *newArray)': names 'QSurfaceDataArray', which has no cute class yet.
  - Qt's 'void QSurfaceDataProxyPrivate::setRow(int rowIndex, QSurfaceDataRow
    *row)': names 'QSurfaceDataRow', which has no cute class yet.
  - Qt's 'void QSurfaceDataProxyPrivate::setRows(int rowIndex, const
    QSurfaceDataArray &rows)': takes a type Python has no way to hand over
    yet.
  - Qt's 'int QSurfaceDataProxyPrivate::addRow(QSurfaceDataRow *row)': names
    'QSurfaceDataRow', which has no cute class yet.
  - Qt's 'int QSurfaceDataProxyPrivate::addRows(const QSurfaceDataArray
    &rows)': takes a type Python has no way to hand over yet.
  - Qt's 'void QSurfaceDataProxyPrivate::insertRow(int rowIndex,
    QSurfaceDataRow *row)': names 'QSurfaceDataRow', which has no cute class
    yet.
  - Qt's 'void QSurfaceDataProxyPrivate::insertRows(int rowIndex, const
    QSurfaceDataArray &rows)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QSurfaceDataProxyPrivate::limitValues(QVector3D &minValues,
    QVector3D &maxValues, QAbstract3DAxis *axisX, QAbstract3DAxis *axisY,
    QAbstract3DAxis *axisZ) const': takes a type Python has no way to hand
    over yet.

  What has no ritual
  ------------------

  4 of the 23 functions Qt declares: 2 not a gap; 2 leans on
  'QSurfaceDataProxyPrivate.

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
  - Qt tells when it has removed the C++ QSurfaceDataProxyPrivate. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QSurfaceDataProxyPrivate that has no cute function yet,
    '__init__', 'addRow', 'addRows', 'insertRow', 'insertRows',
    'limitValues', 'resetArray', 'setRow', 'setRows', holds a function that
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
  __qt_part__ = 'QtDataVisualization'

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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSurfaceDataProxyPrivate::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfacedataproxyprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSurfaceDataProxyPrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QSurfaceDataProxyPrivate10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @overload(int, int, QSurfaceDataItem)
  def setItem(
      self,
      rowIndex: int,
      columnIndex: int,
      item: QSurfaceDataItem,
  ) -> None:
    """
    Calls Qt's 'void QSurfaceDataProxyPrivate::setItem(int rowIndex, int
    columnIndex, const QSurfaceDataItem &item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfacedataproxyprivate.html#setItem

    Parameters
    ----------

    rowIndex : int
      Passed on as it is.

    columnIndex : int
      Passed on as it is.

    item : QSurfaceDataItem
      Passed on as a value: Qt reads the C++ QSurfaceDataItem, which stays
      Python's own.
    """
    #  void QSurfaceDataProxyPrivate::setItem(int rowIndex, int columnIndex,
    #      const QSurfaceDataItem &item)
    self.uglySide.call(
        'ritual_ZN24QSurfaceDataProxyPrivate7setItemEiiRK16QSurfaceDataItem',
        rowIndex, columnIndex, self._valueOf(item),
    )

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's
    'QSurfaceDataProxyPrivate::QSurfaceDataProxyPrivate(QSurfaceDataProxy
    *q)': leans on 'QSurfaceDataProxyPrivate::qt_metacall(QMetaObject::Call,
    int, void**)', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSurfaceDataProxyPrivate.__init__' has no cute function yet. Qt's "
        "'QSurfaceDataProxyPrivate::QSurfaceDataProxyPrivate(QSurfaceDataPro"
        "xy *q)': leans on "
        "'QSurfaceDataProxyPrivate::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  @overload(int, int)
  def removeRows(self, rowIndex: int, removeCount: int) -> None:
    """
    Calls Qt's 'void QSurfaceDataProxyPrivate::removeRows(int rowIndex, int
    removeCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfacedataproxyprivate.html#removeRows

    Parameters
    ----------

    rowIndex : int
      Passed on as it is.

    removeCount : int
      Passed on as it is.
    """
    #  void QSurfaceDataProxyPrivate::removeRows(int rowIndex, int
    #      removeCount)
    self.uglySide.call(
        'ritual_ZN24QSurfaceDataProxyPrivate10removeRowsEii',
        rowIndex, removeCount,
    )

  def qptr(self) -> Optional[QSurfaceDataProxy]:
    """
    Calls Qt's 'QSurfaceDataProxy *QSurfaceDataProxyPrivate::qptr()'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfacedataproxyprivate.html#qptr

    Returns
    -------

    Optional[QSurfaceDataProxy]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSurfaceDataProxy *QSurfaceDataProxyPrivate::qptr()
    address = self.uglySide.call(
        'ritual_ZN24QSurfaceDataProxyPrivate4qptrEv',
    )
    from . import QSurfaceDataProxy
    return QSurfaceDataProxy._cuteAt(address)

  @overload(int)
  def clearRow(self, rowIndex: int) -> None:
    """
    Calls Qt's 'void QSurfaceDataProxyPrivate::clearRow(int rowIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfacedataproxyprivate.html#clearRow

    Parameters
    ----------

    rowIndex : int
      Passed on as it is.
    """
    #  void QSurfaceDataProxyPrivate::clearRow(int rowIndex)
    self.uglySide.call(
        'ritual_ZN24QSurfaceDataProxyPrivate8clearRowEi', rowIndex,
    )

  def clearArray(self) -> None:
    """
    Calls Qt's 'void QSurfaceDataProxyPrivate::clearArray()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfacedataproxyprivate.html#clearArray
    """
    #  void QSurfaceDataProxyPrivate::clearArray()
    self.uglySide.call('ritual_ZN24QSurfaceDataProxyPrivate10clearArrayEv')

  @staticmethod
  def addRow(*__, **_) -> Never:
    """
    Qt's 'int QSurfaceDataProxyPrivate::addRow(QSurfaceDataRow *row)': names
    'QSurfaceDataRow', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QSurfaceDataProxyPrivate.addRow' has no cute function yet. Qt's "
        "'int QSurfaceDataProxyPrivate::addRow(QSurfaceDataRow *row)': "
        "names 'QSurfaceDataRow', which has no cute class yet.")

  @staticmethod
  def addRows(*__, **_) -> Never:
    """
    Qt's 'int QSurfaceDataProxyPrivate::addRows(const QSurfaceDataArray
    &rows)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSurfaceDataProxyPrivate.addRows' has no cute function yet. Qt's "
        "'int QSurfaceDataProxyPrivate::addRows(const QSurfaceDataArray "
        "&rows)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def insertRow(*__, **_) -> Never:
    """
    Qt's 'void QSurfaceDataProxyPrivate::insertRow(int rowIndex,
    QSurfaceDataRow *row)': names 'QSurfaceDataRow', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QSurfaceDataProxyPrivate.insertRow' has no cute function yet. "
        "Qt's 'void QSurfaceDataProxyPrivate::insertRow(int rowIndex, "
        "QSurfaceDataRow *row)': names 'QSurfaceDataRow', which has no cute "
        "class yet.")

  @staticmethod
  def insertRows(*__, **_) -> Never:
    """
    Qt's 'void QSurfaceDataProxyPrivate::insertRows(int rowIndex, const
    QSurfaceDataArray &rows)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QSurfaceDataProxyPrivate.insertRows' has no cute function yet. "
        "Qt's 'void QSurfaceDataProxyPrivate::insertRows(int rowIndex, "
        "const QSurfaceDataArray &rows)': takes a type Python has no way to "
        "hand over yet.")

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
    *newArray)': names 'QSurfaceDataArray', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QSurfaceDataProxyPrivate.resetArray' has no cute function yet. "
        "Qt's 'void QSurfaceDataProxyPrivate::resetArray(QSurfaceDataArray "
        "*newArray)': names 'QSurfaceDataArray', which has no cute class "
        "yet.")

  @staticmethod
  def setRow(*__, **_) -> Never:
    """
    Qt's 'void QSurfaceDataProxyPrivate::setRow(int rowIndex, QSurfaceDataRow
    *row)': names 'QSurfaceDataRow', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QSurfaceDataProxyPrivate.setRow' has no cute function yet. Qt's "
        "'void QSurfaceDataProxyPrivate::setRow(int rowIndex, "
        "QSurfaceDataRow *row)': names 'QSurfaceDataRow', which has no cute "
        "class yet.")

  @staticmethod
  def setRows(*__, **_) -> Never:
    """
    Qt's 'void QSurfaceDataProxyPrivate::setRows(int rowIndex, const
    QSurfaceDataArray &rows)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QSurfaceDataProxyPrivate.setRows' has no cute function yet. Qt's "
        "'void QSurfaceDataProxyPrivate::setRows(int rowIndex, const "
        "QSurfaceDataArray &rows)': takes a type Python has no way to hand "
        "over yet.")
