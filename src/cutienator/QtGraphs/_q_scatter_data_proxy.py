"""
QScatterDataProxy binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/qscatterdataproxy.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QAbstractDataProxy

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QVector3D
  from . import QScatter3DSeries, QScatterDataItem, QScatterDataProxyPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QScatter3DSeries = WAIT['QtGraphs:QScatter3DSeries']
  QScatterDataItem = WAIT['QtGraphs:QScatterDataItem']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QScatterDataProxy(QAbstractDataProxy):
  """
  The cute side of Qt's QScatterDataProxy: a plain Python object standing in
  front of one C++ QScatterDataProxy.

  It is built on the cute 'QAbstractDataProxy', as Qt's QScatterDataProxy is
  built on Qt's QAbstractDataProxy, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QScatterDataProxy that has a ritual and that Python
  can call so far, 24 names in all: 'metaObject', 'tr', 'd_func', 'series',
  'itemCount', 'itemAt', 'scaleAt', 'resetArray', 'resetScaleArray',
  'setItem', 'setItems', 'addItem', 'addItems', 'insertItem', 'insertItems',
  'removeItems', 'arrayReset', 'scaleArrayReset', 'itemsAdded',
  'itemsChanged', 'itemsRemoved', 'itemsInserted', 'itemCountChanged',
  'seriesChanged'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QScatterDataProxy::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QScatterDataProxy::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QScatterDataProxyPrivate *QScatterDataProxy::d_func() const':
    takes in Python what 'QScatterDataProxyPrivate
    *QScatterDataProxy::d_func()' takes.
  - Qt's 'void QScatterDataProxy::qt_qmlMarker_uncreatable()': one of Qt's
    own inner workings.
  - Qt's 'QScatterDataProxy::~QScatterDataProxy()': the destructor: Python
    never removes a C++ QScatterDataProxy.
  - Qt's 'QScatterDataProxy::QScatterDataProxy(QScatterDataProxyPrivate &d,
    QObject *parent)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  6 of the 38 functions Qt declares: 2 not a gap; 2 forbidden; 2 the compiler
  refuses its ritual as it would be written here.

  What to expect
  --------------

  - The C++ QScatterDataProxy is created at the first use, not by
    'QScatterDataProxy(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QScatterDataProxy.
  - Qt tells when it has removed the C++ QScatterDataProxy. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QScatterDataProxy::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qscatterdataproxy.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QScatterDataProxy::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QScatterDataProxy2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScatterDataProxy'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

  #  A C++ QScatterDataProxy Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QScatterDataProxy'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QScatterDataProxy::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscatterdataproxy.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QScatterDataProxy::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QScatterDataProxy10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def series(self) -> Optional[QScatter3DSeries]:
    """
    Calls Qt's 'QScatter3DSeries *QScatterDataProxy::series() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscatterdataproxy.html#series

    Returns
    -------

    Optional[QScatter3DSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScatter3DSeries *QScatterDataProxy::series() const
    address = self.uglySide.call('ritual_ZNK17QScatterDataProxy6seriesEv')
    from . import QScatter3DSeries
    return QScatter3DSeries._cuteAt(address)

  def itemCount(self) -> int:
    """
    Calls Qt's 'qsizetype QScatterDataProxy::itemCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscatterdataproxy.html#itemCount
    """
    #  qsizetype QScatterDataProxy::itemCount() const
    return self.uglySide.call('ritual_ZNK17QScatterDataProxy9itemCountEv')

  @overload(int)
  def itemAt(self, index: int) -> QScatterDataItem:
    """
    Calls Qt's 'const QScatterDataItem &QScatterDataProxy::itemAt(qsizetype
    index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qscatterdataproxy.html#itemAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QScatterDataItem
      A new cute QScatterDataItem around the copy Qt gave back. Python owns
      it.
    """
    #  const QScatterDataItem &QScatterDataProxy::itemAt(qsizetype index)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK17QScatterDataProxy6itemAtEx', index,
    )
    from . import QScatterDataItem
    return QScatterDataItem._cuteOwning(address)

  @overload(int)
  def scaleAt(self, index: int) -> QVector3D:
    """
    Calls Qt's 'QVector3D QScatterDataProxy::scaleAt(qsizetype index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qscatterdataproxy.html#scaleAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QScatterDataProxy::scaleAt(qsizetype index) const
    address = self.uglySide.call(
        'ritual_ZNK17QScatterDataProxy7scaleAtEx', index,
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, QScatterDataItem)
  def setItem(self, index: int, item: QScatterDataItem) -> None:
    """
    Calls Qt's 'void QScatterDataProxy::setItem(qsizetype index,
    QScatterDataItem item)'.

    Qt's own words: https://doc.qt.io/qt-6/qscatterdataproxy.html#setItem

    Parameters
    ----------

    index : int
      Passed on as it is.

    item : QScatterDataItem
      Passed on as a value: Qt reads the C++ QScatterDataItem, which stays
      Python's own.
    """
    #  void QScatterDataProxy::setItem(qsizetype index, QScatterDataItem
    #      item)
    self.uglySide.call(
        'ritual_ZN17QScatterDataProxy7setItemEx16QScatterDataItem',
        index, self._valueOf(item),
    )

  @overload(int, QList[QScatterDataItem])
  def setItems(self, index: int, items: QList[QScatterDataItem]) -> None:
    """
    Calls Qt's 'void QScatterDataProxy::setItems(qsizetype index,
    QScatterDataArray items)'.

    Qt's own words: https://doc.qt.io/qt-6/qscatterdataproxy.html#setItems

    Parameters
    ----------

    index : int
      Passed on as it is.

    items : QList[QScatterDataItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QScatterDataProxy::setItems(qsizetype index, QScatterDataArray
    #      items)
    self.uglySide.call(
        'ritual_ZN17QScatterDataProxy8setItemsEx5QListI16QScatterDataItemE',
        index, self._valueOf(items),
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

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QScatterDataProxy::QScatterDataProxy(QObject *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatterdataproxy.html#QScatterDataProxy

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QScatterDataProxy::QScatterDataProxy(QObject *parent)
    self._noteCreation(QScatterDataProxy, lambda: Rituals.call(
        'ritual_ZN17QScatterDataProxyC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def d_func(self) -> Optional[QScatterDataProxyPrivate]:
    """
    Calls Qt's 'QScatterDataProxyPrivate *QScatterDataProxy::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qscatterdataproxy.html#d_func

    Returns
    -------

    Optional[QScatterDataProxyPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScatterDataProxyPrivate *QScatterDataProxy::d_func()
    address = self.uglySide.call('ritual_ZN17QScatterDataProxy6d_funcEv')
    from . import QScatterDataProxyPrivate
    return QScatterDataProxyPrivate._cuteAt(address)

  @overload()
  def resetArray(self) -> None:
    """
    Calls Qt's 'void QScatterDataProxy::resetArray()'.

    Qt's own words: https://doc.qt.io/qt-6/qscatterdataproxy.html#resetArray
    """
    #  void QScatterDataProxy::resetArray()
    self.uglySide.call('ritual_ZN17QScatterDataProxy10resetArrayEv')

  @overload(QList[QScatterDataItem])
  def resetArray(self, newArray: QList[QScatterDataItem]) -> None:
    """
    Calls Qt's 'void QScatterDataProxy::resetArray(QScatterDataArray
    newArray)'.

    Qt's own words: https://doc.qt.io/qt-6/qscatterdataproxy.html#resetArray

    Parameters
    ----------

    newArray : QList[QScatterDataItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QScatterDataProxy::resetArray(QScatterDataArray newArray)
    self.uglySide.call(
        'ritual_ZN17QScatterDataProxy10resetArrayE5QListI16QScatterDataItem'
        'E',
        self._valueOf(newArray),
    )

  @overload(QList[QVector3D])
  def resetScaleArray(self, newArray: QList[QVector3D]) -> None:
    """
    Calls Qt's 'void QScatterDataProxy::resetScaleArray(QList<QVector3D>
    newArray)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatterdataproxy.html#resetScaleArray

    Parameters
    ----------

    newArray : QList[QVector3D]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QScatterDataProxy::resetScaleArray(QList<QVector3D> newArray)
    self.uglySide.call(
        'ritual_ZN17QScatterDataProxy15resetScaleArrayE5QListI9QVector3DE',
        self._valueOf(newArray),
    )

  @overload(QScatterDataItem)
  def addItem(self, item: QScatterDataItem) -> int:
    """
    Calls Qt's 'qsizetype QScatterDataProxy::addItem(QScatterDataItem item)'.

    Qt's own words: https://doc.qt.io/qt-6/qscatterdataproxy.html#addItem

    Parameters
    ----------

    item : QScatterDataItem
      Passed on as a value: Qt reads the C++ QScatterDataItem, which stays
      Python's own.
    """
    #  qsizetype QScatterDataProxy::addItem(QScatterDataItem item)
    return self.uglySide.call(
        'ritual_ZN17QScatterDataProxy7addItemE16QScatterDataItem',
        self._valueOf(item),
    )

  @overload(QList[QScatterDataItem])
  def addItems(self, items: QList[QScatterDataItem]) -> int:
    """
    Calls Qt's 'qsizetype QScatterDataProxy::addItems(QScatterDataArray
    items)'.

    Qt's own words: https://doc.qt.io/qt-6/qscatterdataproxy.html#addItems

    Parameters
    ----------

    items : QList[QScatterDataItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  qsizetype QScatterDataProxy::addItems(QScatterDataArray items)
    return self.uglySide.call(
        'ritual_ZN17QScatterDataProxy8addItemsE5QListI16QScatterDataItemE',
        self._valueOf(items),
    )

  @overload(int, QScatterDataItem)
  def insertItem(self, index: int, item: QScatterDataItem) -> None:
    """
    Calls Qt's 'void QScatterDataProxy::insertItem(qsizetype index,
    QScatterDataItem item)'.

    Qt's own words: https://doc.qt.io/qt-6/qscatterdataproxy.html#insertItem

    Parameters
    ----------

    index : int
      Passed on as it is.

    item : QScatterDataItem
      Passed on as a value: Qt reads the C++ QScatterDataItem, which stays
      Python's own.
    """
    #  void QScatterDataProxy::insertItem(qsizetype index, QScatterDataItem
    #      item)
    self.uglySide.call(
        'ritual_ZN17QScatterDataProxy10insertItemEx16QScatterDataItem',
        index, self._valueOf(item),
    )

  @overload(int, QList[QScatterDataItem])
  def insertItems(self, index: int, items: QList[QScatterDataItem]) -> None:
    """
    Calls Qt's 'void QScatterDataProxy::insertItems(qsizetype index,
    QScatterDataArray items)'.

    Qt's own words: https://doc.qt.io/qt-6/qscatterdataproxy.html#insertItems

    Parameters
    ----------

    index : int
      Passed on as it is.

    items : QList[QScatterDataItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QScatterDataProxy::insertItems(qsizetype index, QScatterDataArray
    #      items)
    self.uglySide.call(
        'ritual_ZN17QScatterDataProxy11insertItemsEx5QListI16QScatterDataIt'
        'emE',
        index, self._valueOf(items),
    )

  @overload(int, int)
  def removeItems(self, index: int, removeCount: int) -> None:
    """
    Calls Qt's 'void QScatterDataProxy::removeItems(qsizetype index,
    qsizetype removeCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qscatterdataproxy.html#removeItems

    Parameters
    ----------

    index : int
      Passed on as it is.

    removeCount : int
      Passed on as it is.
    """
    #  void QScatterDataProxy::removeItems(qsizetype index, qsizetype
    #      removeCount)
    self.uglySide.call(
        'ritual_ZN17QScatterDataProxy11removeItemsExx', index, removeCount,
    )

  def arrayReset(self) -> None:
    """
    Calls Qt's 'void QScatterDataProxy::arrayReset()'.

    Qt's own words: https://doc.qt.io/qt-6/qscatterdataproxy.html#arrayReset
    """
    #  void QScatterDataProxy::arrayReset()
    self.uglySide.call('ritual_ZN17QScatterDataProxy10arrayResetEv')

  def scaleArrayReset(self) -> None:
    """
    Calls Qt's 'void QScatterDataProxy::scaleArrayReset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatterdataproxy.html#scaleArrayReset
    """
    #  void QScatterDataProxy::scaleArrayReset()
    self.uglySide.call('ritual_ZN17QScatterDataProxy15scaleArrayResetEv')

  @overload(int, int)
  def itemsAdded(self, startIndex: int, count: int) -> None:
    """
    Calls Qt's 'void QScatterDataProxy::itemsAdded(qsizetype startIndex,
    qsizetype count)'.

    Qt's own words: https://doc.qt.io/qt-6/qscatterdataproxy.html#itemsAdded

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QScatterDataProxy::itemsAdded(qsizetype startIndex, qsizetype
    #      count)
    self.uglySide.call(
        'ritual_ZN17QScatterDataProxy10itemsAddedExx', startIndex, count,
    )

  @overload(int, int)
  def itemsChanged(self, startIndex: int, count: int) -> None:
    """
    Calls Qt's 'void QScatterDataProxy::itemsChanged(qsizetype startIndex,
    qsizetype count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatterdataproxy.html#itemsChanged

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QScatterDataProxy::itemsChanged(qsizetype startIndex, qsizetype
    #      count)
    self.uglySide.call(
        'ritual_ZN17QScatterDataProxy12itemsChangedExx', startIndex, count,
    )

  @overload(int, int)
  def itemsRemoved(self, startIndex: int, count: int) -> None:
    """
    Calls Qt's 'void QScatterDataProxy::itemsRemoved(qsizetype startIndex,
    qsizetype count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatterdataproxy.html#itemsRemoved

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QScatterDataProxy::itemsRemoved(qsizetype startIndex, qsizetype
    #      count)
    self.uglySide.call(
        'ritual_ZN17QScatterDataProxy12itemsRemovedExx', startIndex, count,
    )

  @overload(int, int)
  def itemsInserted(self, startIndex: int, count: int) -> None:
    """
    Calls Qt's 'void QScatterDataProxy::itemsInserted(qsizetype startIndex,
    qsizetype count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatterdataproxy.html#itemsInserted

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QScatterDataProxy::itemsInserted(qsizetype startIndex, qsizetype
    #      count)
    self.uglySide.call(
        'ritual_ZN17QScatterDataProxy13itemsInsertedExx', startIndex, count,
    )

  @overload(int)
  def itemCountChanged(self, count: int) -> None:
    """
    Calls Qt's 'void QScatterDataProxy::itemCountChanged(qsizetype count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatterdataproxy.html#itemCountChanged

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QScatterDataProxy::itemCountChanged(qsizetype count)
    self.uglySide.call(
        'ritual_ZN17QScatterDataProxy16itemCountChangedEx', count,
    )

  @overload(QScatter3DSeries)
  @overload(NoneType)
  def seriesChanged(self, series: Optional[QScatter3DSeries]) -> None:
    """
    Calls Qt's 'void QScatterDataProxy::seriesChanged(QScatter3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatterdataproxy.html#seriesChanged

    Parameters
    ----------

    series : Optional[QScatter3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScatterDataProxy::seriesChanged(QScatter3DSeries *series)
    self.uglySide.call(
        'ritual_ZN17QScatterDataProxy13seriesChangedEP16QScatter3DSeries',
        self._addressOf(series),
    )
