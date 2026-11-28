"""
QScatterDataProxyPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/qscatterdataproxy_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QScatterDataProxyPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QList
from . import QAbstractDataProxyPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QAbstract3DAxis, QAbstract3DSeries, QScatterDataItem
  from . import QScatterDataProxy
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstract3DAxis = WAIT['QtDataVisualization:QAbstract3DAxis']
  QAbstract3DSeries = WAIT['QtDataVisualization:QAbstract3DSeries']
  QScatterDataItem = WAIT['QtDataVisualization:QScatterDataItem']

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
  Python can call so far, 11 names in all: 'metaObject', 'setItem',
  'setItems', 'addItem', 'addItems', 'insertItem', 'insertItems',
  'removeItems', 'isValidValue', 'setSeries', 'qptr'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QScatterDataProxyPrivate::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QScatterDataProxyPrivate::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QScatterDataProxyPrivate::~QScatterDataProxyPrivate()': the
    destructor: Python never removes a C++ QScatterDataProxyPrivate.
  - Qt's 'void QScatterDataProxyPrivate::resetArray(QScatterDataArray
    *newArray)': names 'QScatterDataArray', which has no cute class yet.
  - Qt's 'void QScatterDataProxyPrivate::limitValues(QVector3D &minValues,
    QVector3D &maxValues, QAbstract3DAxis *axisX, QAbstract3DAxis *axisY,
    QAbstract3DAxis *axisZ) const': takes a type Python has no way to hand
    over yet.

  What has no ritual
  ------------------

  4 of the 20 functions Qt declares: 2 not a gap; 2 leans on
  'QScatterDataProxyPrivate.

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
  - Qt tells when it has removed the C++ QScatterDataProxyPrivate. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QScatterDataProxyPrivate that has no cute function yet,
    '__init__', 'limitValues', 'resetArray', holds a function that raises
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
  __qt_class__ = 'QScatterDataProxyPrivate'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtDataVisualization'

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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QScatterDataProxyPrivate::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatterdataproxyprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QScatterDataProxyPrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QScatterDataProxyPrivate10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @overload(int, QScatterDataItem)
  def setItem(self, index: int, item: QScatterDataItem) -> None:
    """
    Calls Qt's 'void QScatterDataProxyPrivate::setItem(int index, const
    QScatterDataItem &item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatterdataproxyprivate.html#setItem

    Parameters
    ----------

    index : int
      Passed on as it is.

    item : QScatterDataItem
      Passed on as a value: Qt reads the C++ QScatterDataItem, which stays
      Python's own.
    """
    #  void QScatterDataProxyPrivate::setItem(int index, const
    #      QScatterDataItem &item)
    self.uglySide.call(
        'ritual_ZN24QScatterDataProxyPrivate7setItemEiRK16QScatterDataItem',
        index, self._valueOf(item),
    )

  @overload(int, QList[QScatterDataItem])
  def setItems(self, index: int, items: QList[QScatterDataItem]) -> None:
    """
    Calls Qt's 'void QScatterDataProxyPrivate::setItems(int index, const
    QScatterDataArray &items)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatterdataproxyprivate.html#setItems

    Parameters
    ----------

    index : int
      Passed on as it is.

    items : QList[QScatterDataItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QScatterDataProxyPrivate::setItems(int index, const
    #      QScatterDataArray &items)
    self.uglySide.call(
        'ritual_ZN24QScatterDataProxyPrivate8setItemsEiRK5QListI16QScatterD'
        'ataItemE',
        index, self._valueOf(items),
    )

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's
    'QScatterDataProxyPrivate::QScatterDataProxyPrivate(QScatterDataProxy
    *q)': leans on 'QScatterDataProxyPrivate::qt_metacall(QMetaObject::Call,
    int, void**)', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QScatterDataProxyPrivate.__init__' has no cute function yet. Qt's "
        "'QScatterDataProxyPrivate::QScatterDataProxyPrivate(QScatterDataPro"
        "xy *q)': leans on "
        "'QScatterDataProxyPrivate::qt_metacall(QMetaObject::Call, int, "
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

  @overload(QScatterDataItem)
  def addItem(self, item: QScatterDataItem) -> int:
    """
    Calls Qt's 'int QScatterDataProxyPrivate::addItem(const QScatterDataItem
    &item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatterdataproxyprivate.html#addItem

    Parameters
    ----------

    item : QScatterDataItem
      Passed on as a value: Qt reads the C++ QScatterDataItem, which stays
      Python's own.
    """
    #  int QScatterDataProxyPrivate::addItem(const QScatterDataItem &item)
    return self.uglySide.call(
        'ritual_ZN24QScatterDataProxyPrivate7addItemERK16QScatterDataItem',
        self._valueOf(item),
    )

  @overload(QList[QScatterDataItem])
  def addItems(self, items: QList[QScatterDataItem]) -> int:
    """
    Calls Qt's 'int QScatterDataProxyPrivate::addItems(const
    QScatterDataArray &items)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatterdataproxyprivate.html#addItems

    Parameters
    ----------

    items : QList[QScatterDataItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  int QScatterDataProxyPrivate::addItems(const QScatterDataArray &items)
    return self.uglySide.call(
        'ritual_ZN24QScatterDataProxyPrivate8addItemsERK5QListI16QScatterDa'
        'taItemE',
        self._valueOf(items),
    )

  @overload(int, QScatterDataItem)
  def insertItem(self, index: int, item: QScatterDataItem) -> None:
    """
    Calls Qt's 'void QScatterDataProxyPrivate::insertItem(int index, const
    QScatterDataItem &item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatterdataproxyprivate.html#insertItem

    Parameters
    ----------

    index : int
      Passed on as it is.

    item : QScatterDataItem
      Passed on as a value: Qt reads the C++ QScatterDataItem, which stays
      Python's own.
    """
    #  void QScatterDataProxyPrivate::insertItem(int index, const
    #      QScatterDataItem &item)
    self.uglySide.call(
        'ritual_ZN24QScatterDataProxyPrivate10insertItemEiRK16QScatterDataI'
        'tem',
        index, self._valueOf(item),
    )

  @overload(int, QList[QScatterDataItem])
  def insertItems(self, index: int, items: QList[QScatterDataItem]) -> None:
    """
    Calls Qt's 'void QScatterDataProxyPrivate::insertItems(int index, const
    QScatterDataArray &items)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatterdataproxyprivate.html#insertItems

    Parameters
    ----------

    index : int
      Passed on as it is.

    items : QList[QScatterDataItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QScatterDataProxyPrivate::insertItems(int index, const
    #      QScatterDataArray &items)
    self.uglySide.call(
        'ritual_ZN24QScatterDataProxyPrivate11insertItemsEiRK5QListI16QScat'
        'terDataItemE',
        index, self._valueOf(items),
    )

  @overload(int, int)
  def removeItems(self, index: int, removeCount: int) -> None:
    """
    Calls Qt's 'void QScatterDataProxyPrivate::removeItems(int index, int
    removeCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatterdataproxyprivate.html#removeItems

    Parameters
    ----------

    index : int
      Passed on as it is.

    removeCount : int
      Passed on as it is.
    """
    #  void QScatterDataProxyPrivate::removeItems(int index, int removeCount)
    self.uglySide.call(
        'ritual_ZN24QScatterDataProxyPrivate11removeItemsEii',
        index, removeCount,
    )

  def qptr(self) -> Optional[QScatterDataProxy]:
    """
    Calls Qt's 'QScatterDataProxy *QScatterDataProxyPrivate::qptr()'.

    Qt's own words: https://doc.qt.io/qt-6/qscatterdataproxyprivate.html#qptr

    Returns
    -------

    Optional[QScatterDataProxy]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScatterDataProxy *QScatterDataProxyPrivate::qptr()
    address = self.uglySide.call(
        'ritual_ZN24QScatterDataProxyPrivate4qptrEv',
    )
    from . import QScatterDataProxy
    return QScatterDataProxy._cuteAt(address)

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
    *newArray)': names 'QScatterDataArray', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QScatterDataProxyPrivate.resetArray' has no cute function yet. "
        "Qt's 'void QScatterDataProxyPrivate::resetArray(QScatterDataArray "
        "*newArray)': names 'QScatterDataArray', which has no cute class "
        "yet.")
