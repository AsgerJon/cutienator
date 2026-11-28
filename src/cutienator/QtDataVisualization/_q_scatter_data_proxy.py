"""
QScatterDataProxy binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/qscatterdataproxy.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QAbstractDataProxy

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QScatter3DSeries, QScatterDataItem, QScatterDataProxyPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QScatter3DSeries = WAIT['QtDataVisualization:QScatter3DSeries']
  QScatterDataItem = WAIT['QtDataVisualization:QScatterDataItem']
  QScatterDataProxyPrivate = WAIT['QtDataVisualization:QScatterDataProxyPrivate']

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
  can call so far, 21 names in all: 'metaObject', 'tr', 'series',
  'itemCount', 'itemAt', 'setItem', 'setItems', 'addItem', 'addItems',
  'insertItem', 'insertItems', 'removeItems', 'arrayReset', 'itemsAdded',
  'itemsChanged', 'itemsRemoved', 'itemsInserted', 'itemCountChanged',
  'seriesChanged', 'dptr', 'dptrc'. It can be made from Python, in 2 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QScatterDataProxy::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QScatterDataProxy::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QScatterDataProxy::~QScatterDataProxy()': the destructor: Python
    never removes a C++ QScatterDataProxy.
  - Qt's 'const QScatterDataArray *QScatterDataProxy::array() const': gives
    'QList<QScatterDataItem>', which has no cute class yet.
  - Qt's 'void QScatterDataProxy::resetArray(QScatterDataArray *newArray)':
    names 'QScatterDataArray', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 32 functions Qt declares: 2 not a gap; 2 forbidden.

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
  - Each name of Qt's QScatterDataProxy that has no cute function yet,
    'array', 'resetArray', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
  __qt_part__ = 'QtDataVisualization'

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
    Calls Qt's 'int QScatterDataProxy::itemCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscatterdataproxy.html#itemCount
    """
    #  int QScatterDataProxy::itemCount() const
    return self.uglySide.call('ritual_ZNK17QScatterDataProxy9itemCountEv')

  @overload(int)
  def itemAt(self, index: int) -> Optional[QScatterDataItem]:
    """
    Calls Qt's 'const QScatterDataItem *QScatterDataProxy::itemAt(int index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qscatterdataproxy.html#itemAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QScatterDataItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QScatterDataItem *QScatterDataProxy::itemAt(int index) const
    address = self.uglySide.call(
        'ritual_ZNK17QScatterDataProxy6itemAtEi', index,
    )
    from . import QScatterDataItem
    return QScatterDataItem._cuteAt(address)

  def dptrc(self) -> Optional[QScatterDataProxyPrivate]:
    """
    Calls Qt's 'const QScatterDataProxyPrivate *QScatterDataProxy::dptrc()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qscatterdataproxy.html#dptrc

    Returns
    -------

    Optional[QScatterDataProxyPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QScatterDataProxyPrivate *QScatterDataProxy::dptrc() const
    address = self.uglySide.call('ritual_ZNK17QScatterDataProxy5dptrcEv')
    from . import QScatterDataProxyPrivate
    return QScatterDataProxyPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, QScatterDataItem)
  def setItem(self, index: int, item: QScatterDataItem) -> None:
    """
    Calls Qt's 'void QScatterDataProxy::setItem(int index, const
    QScatterDataItem &item)'.

    Qt's own words: https://doc.qt.io/qt-6/qscatterdataproxy.html#setItem

    Parameters
    ----------

    index : int
      Passed on as it is.

    item : QScatterDataItem
      Passed on as a value: Qt reads the C++ QScatterDataItem, which stays
      Python's own.
    """
    #  void QScatterDataProxy::setItem(int index, const QScatterDataItem
    #      &item)
    self.uglySide.call(
        'ritual_ZN17QScatterDataProxy7setItemEiRK16QScatterDataItem',
        index, self._valueOf(item),
    )

  @overload(int, QList[QScatterDataItem])
  def setItems(self, index: int, items: QList[QScatterDataItem]) -> None:
    """
    Calls Qt's 'void QScatterDataProxy::setItems(int index, const
    QScatterDataArray &items)'.

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
    #  void QScatterDataProxy::setItems(int index, const QScatterDataArray
    #      &items)
    self.uglySide.call(
        'ritual_ZN17QScatterDataProxy8setItemsEiRK5QListI16QScatterDataItem'
        'E',
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

  @overload(QScatterDataProxyPrivate)
  @overload(QScatterDataProxyPrivate, QObject)
  @overload(QScatterDataProxyPrivate, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      d: Optional[QScatterDataProxyPrivate],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QScatterDataProxy::QScatterDataProxy(QScatterDataProxyPrivate *d,
    QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatterdataproxy.html#QScatterDataProxy

    Parameters
    ----------

    d : Optional[QScatterDataProxyPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QScatterDataProxy::QScatterDataProxy(QScatterDataProxyPrivate *d,
    #      QObject *parent)
    self._noteCreation(QScatterDataProxy, lambda: Rituals.call(
        'ritual_ZN17QScatterDataProxyC1EP24QScatterDataProxyPrivateP7QObjec'
        't',
        self._addressOf(d), self._addressOf(parent, 'QObject'),
    ))

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

  @overload(QScatterDataItem)
  def addItem(self, item: QScatterDataItem) -> int:
    """
    Calls Qt's 'int QScatterDataProxy::addItem(const QScatterDataItem
    &item)'.

    Qt's own words: https://doc.qt.io/qt-6/qscatterdataproxy.html#addItem

    Parameters
    ----------

    item : QScatterDataItem
      Passed on as a value: Qt reads the C++ QScatterDataItem, which stays
      Python's own.
    """
    #  int QScatterDataProxy::addItem(const QScatterDataItem &item)
    return self.uglySide.call(
        'ritual_ZN17QScatterDataProxy7addItemERK16QScatterDataItem',
        self._valueOf(item),
    )

  @overload(QList[QScatterDataItem])
  def addItems(self, items: QList[QScatterDataItem]) -> int:
    """
    Calls Qt's 'int QScatterDataProxy::addItems(const QScatterDataArray
    &items)'.

    Qt's own words: https://doc.qt.io/qt-6/qscatterdataproxy.html#addItems

    Parameters
    ----------

    items : QList[QScatterDataItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  int QScatterDataProxy::addItems(const QScatterDataArray &items)
    return self.uglySide.call(
        'ritual_ZN17QScatterDataProxy8addItemsERK5QListI16QScatterDataItemE',
        self._valueOf(items),
    )

  @overload(int, QScatterDataItem)
  def insertItem(self, index: int, item: QScatterDataItem) -> None:
    """
    Calls Qt's 'void QScatterDataProxy::insertItem(int index, const
    QScatterDataItem &item)'.

    Qt's own words: https://doc.qt.io/qt-6/qscatterdataproxy.html#insertItem

    Parameters
    ----------

    index : int
      Passed on as it is.

    item : QScatterDataItem
      Passed on as a value: Qt reads the C++ QScatterDataItem, which stays
      Python's own.
    """
    #  void QScatterDataProxy::insertItem(int index, const QScatterDataItem
    #      &item)
    self.uglySide.call(
        'ritual_ZN17QScatterDataProxy10insertItemEiRK16QScatterDataItem',
        index, self._valueOf(item),
    )

  @overload(int, QList[QScatterDataItem])
  def insertItems(self, index: int, items: QList[QScatterDataItem]) -> None:
    """
    Calls Qt's 'void QScatterDataProxy::insertItems(int index, const
    QScatterDataArray &items)'.

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
    #  void QScatterDataProxy::insertItems(int index, const QScatterDataArray
    #      &items)
    self.uglySide.call(
        'ritual_ZN17QScatterDataProxy11insertItemsEiRK5QListI16QScatterData'
        'ItemE',
        index, self._valueOf(items),
    )

  @overload(int, int)
  def removeItems(self, index: int, removeCount: int) -> None:
    """
    Calls Qt's 'void QScatterDataProxy::removeItems(int index, int
    removeCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qscatterdataproxy.html#removeItems

    Parameters
    ----------

    index : int
      Passed on as it is.

    removeCount : int
      Passed on as it is.
    """
    #  void QScatterDataProxy::removeItems(int index, int removeCount)
    self.uglySide.call(
        'ritual_ZN17QScatterDataProxy11removeItemsEii', index, removeCount,
    )

  def arrayReset(self) -> None:
    """
    Calls Qt's 'void QScatterDataProxy::arrayReset()'.

    Qt's own words: https://doc.qt.io/qt-6/qscatterdataproxy.html#arrayReset
    """
    #  void QScatterDataProxy::arrayReset()
    self.uglySide.call('ritual_ZN17QScatterDataProxy10arrayResetEv')

  @overload(int, int)
  def itemsAdded(self, startIndex: int, count: int) -> None:
    """
    Calls Qt's 'void QScatterDataProxy::itemsAdded(int startIndex, int
    count)'.

    Qt's own words: https://doc.qt.io/qt-6/qscatterdataproxy.html#itemsAdded

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QScatterDataProxy::itemsAdded(int startIndex, int count)
    self.uglySide.call(
        'ritual_ZN17QScatterDataProxy10itemsAddedEii', startIndex, count,
    )

  @overload(int, int)
  def itemsChanged(self, startIndex: int, count: int) -> None:
    """
    Calls Qt's 'void QScatterDataProxy::itemsChanged(int startIndex, int
    count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatterdataproxy.html#itemsChanged

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QScatterDataProxy::itemsChanged(int startIndex, int count)
    self.uglySide.call(
        'ritual_ZN17QScatterDataProxy12itemsChangedEii', startIndex, count,
    )

  @overload(int, int)
  def itemsRemoved(self, startIndex: int, count: int) -> None:
    """
    Calls Qt's 'void QScatterDataProxy::itemsRemoved(int startIndex, int
    count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatterdataproxy.html#itemsRemoved

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QScatterDataProxy::itemsRemoved(int startIndex, int count)
    self.uglySide.call(
        'ritual_ZN17QScatterDataProxy12itemsRemovedEii', startIndex, count,
    )

  @overload(int, int)
  def itemsInserted(self, startIndex: int, count: int) -> None:
    """
    Calls Qt's 'void QScatterDataProxy::itemsInserted(int startIndex, int
    count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatterdataproxy.html#itemsInserted

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QScatterDataProxy::itemsInserted(int startIndex, int count)
    self.uglySide.call(
        'ritual_ZN17QScatterDataProxy13itemsInsertedEii', startIndex, count,
    )

  @overload(int)
  def itemCountChanged(self, count: int) -> None:
    """
    Calls Qt's 'void QScatterDataProxy::itemCountChanged(int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatterdataproxy.html#itemCountChanged

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QScatterDataProxy::itemCountChanged(int count)
    self.uglySide.call(
        'ritual_ZN17QScatterDataProxy16itemCountChangedEi', count,
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

  def dptr(self) -> Optional[QScatterDataProxyPrivate]:
    """
    Calls Qt's 'QScatterDataProxyPrivate *QScatterDataProxy::dptr()'.

    Qt's own words: https://doc.qt.io/qt-6/qscatterdataproxy.html#dptr

    Returns
    -------

    Optional[QScatterDataProxyPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScatterDataProxyPrivate *QScatterDataProxy::dptr()
    address = self.uglySide.call('ritual_ZN17QScatterDataProxy4dptrEv')
    from . import QScatterDataProxyPrivate
    return QScatterDataProxyPrivate._cuteAt(address)

  @staticmethod
  def array(*__, **_) -> Never:
    """
    Qt's 'const QScatterDataArray *QScatterDataProxy::array() const': gives
    'QList<QScatterDataItem>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QScatterDataProxy.array' has no cute function yet. Qt's 'const "
        "QScatterDataArray *QScatterDataProxy::array() const': gives "
        "'QList<QScatterDataItem>', which has no cute class yet.")

  @staticmethod
  def resetArray(*__, **_) -> Never:
    """
    Qt's 'void QScatterDataProxy::resetArray(QScatterDataArray *newArray)':
    names 'QScatterDataArray', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QScatterDataProxy.resetArray' has no cute function yet. Qt's "
        "'void QScatterDataProxy::resetArray(QScatterDataArray *newArray)': "
        "names 'QScatterDataArray', which has no cute class yet.")
