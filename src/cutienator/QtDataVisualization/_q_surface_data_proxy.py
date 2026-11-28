"""
QSurfaceDataProxy binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/qsurfacedataproxy.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QAbstractDataProxy

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPoint
  from . import QSurface3DSeries, QSurfaceDataItem, QSurfaceDataProxyPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']
  QSurface3DSeries = WAIT['QtDataVisualization:QSurface3DSeries']
  QSurfaceDataItem = WAIT['QtDataVisualization:QSurfaceDataItem']
  QSurfaceDataProxyPrivate = WAIT['QtDataVisualization:QSurfaceDataProxyPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSurfaceDataProxy(QAbstractDataProxy):
  """
  The cute side of Qt's QSurfaceDataProxy: a plain Python object standing in
  front of one C++ QSurfaceDataProxy.

  It is built on the cute 'QAbstractDataProxy', as Qt's QSurfaceDataProxy is
  built on Qt's QAbstractDataProxy, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSurfaceDataProxy that has a ritual and that Python
  can call so far, 19 names in all: 'metaObject', 'tr', 'series', 'rowCount',
  'columnCount', 'itemAt', 'setItem', 'removeRows', 'arrayReset',
  'rowsAdded', 'rowsChanged', 'rowsRemoved', 'rowsInserted', 'itemChanged',
  'rowCountChanged', 'columnCountChanged', 'seriesChanged', 'dptr', 'dptrc'.
  It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSurfaceDataProxy::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QSurfaceDataProxy::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QSurfaceDataProxy::~QSurfaceDataProxy()': the destructor: Python
    never removes a C++ QSurfaceDataProxy.
  - Qt's 'const QSurfaceDataArray *QSurfaceDataProxy::array() const': gives
    'QList<QList<QSurfaceDataItem> *>', which has no cute class yet.
  - Qt's 'void QSurfaceDataProxy::resetArray(QSurfaceDataArray *newArray)':
    names 'QSurfaceDataArray', which has no cute class yet.
  - Qt's 'void QSurfaceDataProxy::setRow(int rowIndex, QSurfaceDataRow
    *row)': names 'QSurfaceDataRow', which has no cute class yet.
  - Qt's 'void QSurfaceDataProxy::setRows(int rowIndex, const
    QSurfaceDataArray &rows)': takes a type Python has no way to hand over
    yet.
  - Qt's 'int QSurfaceDataProxy::addRow(QSurfaceDataRow *row)': names
    'QSurfaceDataRow', which has no cute class yet.
  - Qt's 'int QSurfaceDataProxy::addRows(const QSurfaceDataArray &rows)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QSurfaceDataProxy::insertRow(int rowIndex, QSurfaceDataRow
    *row)': names 'QSurfaceDataRow', which has no cute class yet.
  - Qt's 'void QSurfaceDataProxy::insertRows(int rowIndex, const
    QSurfaceDataArray &rows)': takes a type Python has no way to hand over
    yet.

  What has no ritual
  ------------------

  4 of the 38 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QSurfaceDataProxy is created at the first use, not by
    'QSurfaceDataProxy(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSurfaceDataProxy.
  - Qt tells when it has removed the C++ QSurfaceDataProxy. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QSurfaceDataProxy that has no cute function yet,
    'addRow', 'addRows', 'array', 'insertRow', 'insertRows', 'resetArray',
    'setRow', 'setRows', holds a function that raises 'NotImplementedError',
    and its docstring says why.
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
    Calls Qt's 'QString QSurfaceDataProxy::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfacedataproxy.html#tr

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
    #  QString QSurfaceDataProxy::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QSurfaceDataProxy2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSurfaceDataProxy'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtDataVisualization'

  #  A C++ QSurfaceDataProxy Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSurfaceDataProxy'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSurfaceDataProxy::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfacedataproxy.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSurfaceDataProxy::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QSurfaceDataProxy10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def series(self) -> Optional[QSurface3DSeries]:
    """
    Calls Qt's 'QSurface3DSeries *QSurfaceDataProxy::series() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfacedataproxy.html#series

    Returns
    -------

    Optional[QSurface3DSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSurface3DSeries *QSurfaceDataProxy::series() const
    address = self.uglySide.call('ritual_ZNK17QSurfaceDataProxy6seriesEv')
    from . import QSurface3DSeries
    return QSurface3DSeries._cuteAt(address)

  def rowCount(self) -> int:
    """
    Calls Qt's 'int QSurfaceDataProxy::rowCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfacedataproxy.html#rowCount
    """
    #  int QSurfaceDataProxy::rowCount() const
    return self.uglySide.call('ritual_ZNK17QSurfaceDataProxy8rowCountEv')

  def columnCount(self) -> int:
    """
    Calls Qt's 'int QSurfaceDataProxy::columnCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfacedataproxy.html#columnCount
    """
    #  int QSurfaceDataProxy::columnCount() const
    return self.uglySide.call('ritual_ZNK17QSurfaceDataProxy11columnCountEv')

  @overload(int, int)
  def itemAt(
      self,
      rowIndex: int,
      columnIndex: int,
  ) -> Optional[QSurfaceDataItem]:
    """
    Calls Qt's 'const QSurfaceDataItem *QSurfaceDataProxy::itemAt(int
    rowIndex, int columnIndex) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfacedataproxy.html#itemAt

    Parameters
    ----------

    rowIndex : int
      Passed on as it is.

    columnIndex : int
      Passed on as it is.

    Returns
    -------

    Optional[QSurfaceDataItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QSurfaceDataItem *QSurfaceDataProxy::itemAt(int rowIndex, int
    #      columnIndex) const
    address = self.uglySide.call(
        'ritual_ZNK17QSurfaceDataProxy6itemAtEii', rowIndex, columnIndex,
    )
    from . import QSurfaceDataItem
    return QSurfaceDataItem._cuteAt(address)

  @overload(QPoint)
  def itemAt(self, position: QPoint) -> Optional[QSurfaceDataItem]:
    """
    Calls Qt's 'const QSurfaceDataItem *QSurfaceDataProxy::itemAt(const
    QPoint &position) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfacedataproxy.html#itemAt

    Parameters
    ----------

    position : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    Optional[QSurfaceDataItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QSurfaceDataItem *QSurfaceDataProxy::itemAt(const QPoint
    #      &position) const
    address = self.uglySide.call(
        'ritual_ZNK17QSurfaceDataProxy6itemAtERK6QPoint',
        self._valueOf(position),
    )
    from . import QSurfaceDataItem
    return QSurfaceDataItem._cuteAt(address)

  def dptrc(self) -> Optional[QSurfaceDataProxyPrivate]:
    """
    Calls Qt's 'const QSurfaceDataProxyPrivate *QSurfaceDataProxy::dptrc()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfacedataproxy.html#dptrc

    Returns
    -------

    Optional[QSurfaceDataProxyPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QSurfaceDataProxyPrivate *QSurfaceDataProxy::dptrc() const
    address = self.uglySide.call('ritual_ZNK17QSurfaceDataProxy5dptrcEv')
    from . import QSurfaceDataProxyPrivate
    return QSurfaceDataProxyPrivate._cuteAt(address)

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
    Calls Qt's 'void QSurfaceDataProxy::setItem(int rowIndex, int
    columnIndex, const QSurfaceDataItem &item)'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfacedataproxy.html#setItem

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
    #  void QSurfaceDataProxy::setItem(int rowIndex, int columnIndex, const
    #      QSurfaceDataItem &item)
    self.uglySide.call(
        'ritual_ZN17QSurfaceDataProxy7setItemEiiRK16QSurfaceDataItem',
        rowIndex, columnIndex, self._valueOf(item),
    )

  @overload(QPoint, QSurfaceDataItem)
  def setItem(self, position: QPoint, item: QSurfaceDataItem) -> None:
    """
    Calls Qt's 'void QSurfaceDataProxy::setItem(const QPoint &position, const
    QSurfaceDataItem &item)'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfacedataproxy.html#setItem

    Parameters
    ----------

    position : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    item : QSurfaceDataItem
      Passed on as a value: Qt reads the C++ QSurfaceDataItem, which stays
      Python's own.
    """
    #  void QSurfaceDataProxy::setItem(const QPoint &position, const
    #      QSurfaceDataItem &item)
    self.uglySide.call(
        'ritual_ZN17QSurfaceDataProxy7setItemERK6QPointRK16QSurfaceDataItem',
        self._valueOf(position), self._valueOf(item),
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

  @overload(QSurfaceDataProxyPrivate)
  @overload(QSurfaceDataProxyPrivate, QObject)
  @overload(QSurfaceDataProxyPrivate, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      d: Optional[QSurfaceDataProxyPrivate],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QSurfaceDataProxy::QSurfaceDataProxy(QSurfaceDataProxyPrivate *d,
    QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfacedataproxy.html#QSurfaceDataProxy

    Parameters
    ----------

    d : Optional[QSurfaceDataProxyPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSurfaceDataProxy::QSurfaceDataProxy(QSurfaceDataProxyPrivate *d,
    #      QObject *parent)
    self._noteCreation(QSurfaceDataProxy, lambda: Rituals.call(
        'ritual_ZN17QSurfaceDataProxyC1EP24QSurfaceDataProxyPrivateP7QObjec'
        't',
        self._addressOf(d), self._addressOf(parent, 'QObject'),
    ))

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QSurfaceDataProxy::QSurfaceDataProxy(QObject *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfacedataproxy.html#QSurfaceDataProxy

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSurfaceDataProxy::QSurfaceDataProxy(QObject *parent)
    self._noteCreation(QSurfaceDataProxy, lambda: Rituals.call(
        'ritual_ZN17QSurfaceDataProxyC1EP7QObject',
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

  @overload(int, int)
  def removeRows(self, rowIndex: int, removeCount: int) -> None:
    """
    Calls Qt's 'void QSurfaceDataProxy::removeRows(int rowIndex, int
    removeCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfacedataproxy.html#removeRows

    Parameters
    ----------

    rowIndex : int
      Passed on as it is.

    removeCount : int
      Passed on as it is.
    """
    #  void QSurfaceDataProxy::removeRows(int rowIndex, int removeCount)
    self.uglySide.call(
        'ritual_ZN17QSurfaceDataProxy10removeRowsEii', rowIndex, removeCount,
    )

  def arrayReset(self) -> None:
    """
    Calls Qt's 'void QSurfaceDataProxy::arrayReset()'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfacedataproxy.html#arrayReset
    """
    #  void QSurfaceDataProxy::arrayReset()
    self.uglySide.call('ritual_ZN17QSurfaceDataProxy10arrayResetEv')

  @overload(int, int)
  def rowsAdded(self, startIndex: int, count: int) -> None:
    """
    Calls Qt's 'void QSurfaceDataProxy::rowsAdded(int startIndex, int
    count)'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfacedataproxy.html#rowsAdded

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QSurfaceDataProxy::rowsAdded(int startIndex, int count)
    self.uglySide.call(
        'ritual_ZN17QSurfaceDataProxy9rowsAddedEii', startIndex, count,
    )

  @overload(int, int)
  def rowsChanged(self, startIndex: int, count: int) -> None:
    """
    Calls Qt's 'void QSurfaceDataProxy::rowsChanged(int startIndex, int
    count)'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfacedataproxy.html#rowsChanged

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QSurfaceDataProxy::rowsChanged(int startIndex, int count)
    self.uglySide.call(
        'ritual_ZN17QSurfaceDataProxy11rowsChangedEii', startIndex, count,
    )

  @overload(int, int)
  def rowsRemoved(self, startIndex: int, count: int) -> None:
    """
    Calls Qt's 'void QSurfaceDataProxy::rowsRemoved(int startIndex, int
    count)'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfacedataproxy.html#rowsRemoved

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QSurfaceDataProxy::rowsRemoved(int startIndex, int count)
    self.uglySide.call(
        'ritual_ZN17QSurfaceDataProxy11rowsRemovedEii', startIndex, count,
    )

  @overload(int, int)
  def rowsInserted(self, startIndex: int, count: int) -> None:
    """
    Calls Qt's 'void QSurfaceDataProxy::rowsInserted(int startIndex, int
    count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfacedataproxy.html#rowsInserted

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QSurfaceDataProxy::rowsInserted(int startIndex, int count)
    self.uglySide.call(
        'ritual_ZN17QSurfaceDataProxy12rowsInsertedEii', startIndex, count,
    )

  @overload(int, int)
  def itemChanged(self, rowIndex: int, columnIndex: int) -> None:
    """
    Calls Qt's 'void QSurfaceDataProxy::itemChanged(int rowIndex, int
    columnIndex)'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfacedataproxy.html#itemChanged

    Parameters
    ----------

    rowIndex : int
      Passed on as it is.

    columnIndex : int
      Passed on as it is.
    """
    #  void QSurfaceDataProxy::itemChanged(int rowIndex, int columnIndex)
    self.uglySide.call(
        'ritual_ZN17QSurfaceDataProxy11itemChangedEii',
        rowIndex, columnIndex,
    )

  @overload(int)
  def rowCountChanged(self, count: int) -> None:
    """
    Calls Qt's 'void QSurfaceDataProxy::rowCountChanged(int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfacedataproxy.html#rowCountChanged

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QSurfaceDataProxy::rowCountChanged(int count)
    self.uglySide.call(
        'ritual_ZN17QSurfaceDataProxy15rowCountChangedEi', count,
    )

  @overload(int)
  def columnCountChanged(self, count: int) -> None:
    """
    Calls Qt's 'void QSurfaceDataProxy::columnCountChanged(int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfacedataproxy.html#columnCountChanged

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QSurfaceDataProxy::columnCountChanged(int count)
    self.uglySide.call(
        'ritual_ZN17QSurfaceDataProxy18columnCountChangedEi', count,
    )

  @overload(QSurface3DSeries)
  @overload(NoneType)
  def seriesChanged(self, series: Optional[QSurface3DSeries]) -> None:
    """
    Calls Qt's 'void QSurfaceDataProxy::seriesChanged(QSurface3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfacedataproxy.html#seriesChanged

    Parameters
    ----------

    series : Optional[QSurface3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSurfaceDataProxy::seriesChanged(QSurface3DSeries *series)
    self.uglySide.call(
        'ritual_ZN17QSurfaceDataProxy13seriesChangedEP16QSurface3DSeries',
        self._addressOf(series),
    )

  def dptr(self) -> Optional[QSurfaceDataProxyPrivate]:
    """
    Calls Qt's 'QSurfaceDataProxyPrivate *QSurfaceDataProxy::dptr()'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfacedataproxy.html#dptr

    Returns
    -------

    Optional[QSurfaceDataProxyPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSurfaceDataProxyPrivate *QSurfaceDataProxy::dptr()
    address = self.uglySide.call('ritual_ZN17QSurfaceDataProxy4dptrEv')
    from . import QSurfaceDataProxyPrivate
    return QSurfaceDataProxyPrivate._cuteAt(address)

  @staticmethod
  def addRow(*__, **_) -> Never:
    """
    Qt's 'int QSurfaceDataProxy::addRow(QSurfaceDataRow *row)': names
    'QSurfaceDataRow', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QSurfaceDataProxy.addRow' has no cute function yet. Qt's 'int "
        "QSurfaceDataProxy::addRow(QSurfaceDataRow *row)': names "
        "'QSurfaceDataRow', which has no cute class yet.")

  @staticmethod
  def addRows(*__, **_) -> Never:
    """
    Qt's 'int QSurfaceDataProxy::addRows(const QSurfaceDataArray &rows)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSurfaceDataProxy.addRows' has no cute function yet. Qt's 'int "
        "QSurfaceDataProxy::addRows(const QSurfaceDataArray &rows)': takes "
        "a type Python has no way to hand over yet.")

  @staticmethod
  def array(*__, **_) -> Never:
    """
    Qt's 'const QSurfaceDataArray *QSurfaceDataProxy::array() const': gives
    'QList<QList<QSurfaceDataItem> *>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QSurfaceDataProxy.array' has no cute function yet. Qt's 'const "
        "QSurfaceDataArray *QSurfaceDataProxy::array() const': gives "
        "'QList<QList<QSurfaceDataItem> *>', which has no cute class yet.")

  @staticmethod
  def insertRow(*__, **_) -> Never:
    """
    Qt's 'void QSurfaceDataProxy::insertRow(int rowIndex, QSurfaceDataRow
    *row)': names 'QSurfaceDataRow', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QSurfaceDataProxy.insertRow' has no cute function yet. Qt's 'void "
        "QSurfaceDataProxy::insertRow(int rowIndex, QSurfaceDataRow *row)': "
        "names 'QSurfaceDataRow', which has no cute class yet.")

  @staticmethod
  def insertRows(*__, **_) -> Never:
    """
    Qt's 'void QSurfaceDataProxy::insertRows(int rowIndex, const
    QSurfaceDataArray &rows)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QSurfaceDataProxy.insertRows' has no cute function yet. Qt's "
        "'void QSurfaceDataProxy::insertRows(int rowIndex, const "
        "QSurfaceDataArray &rows)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def resetArray(*__, **_) -> Never:
    """
    Qt's 'void QSurfaceDataProxy::resetArray(QSurfaceDataArray *newArray)':
    names 'QSurfaceDataArray', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QSurfaceDataProxy.resetArray' has no cute function yet. Qt's "
        "'void QSurfaceDataProxy::resetArray(QSurfaceDataArray *newArray)': "
        "names 'QSurfaceDataArray', which has no cute class yet.")

  @staticmethod
  def setRow(*__, **_) -> Never:
    """
    Qt's 'void QSurfaceDataProxy::setRow(int rowIndex, QSurfaceDataRow
    *row)': names 'QSurfaceDataRow', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QSurfaceDataProxy.setRow' has no cute function yet. Qt's 'void "
        "QSurfaceDataProxy::setRow(int rowIndex, QSurfaceDataRow *row)': "
        "names 'QSurfaceDataRow', which has no cute class yet.")

  @staticmethod
  def setRows(*__, **_) -> Never:
    """
    Qt's 'void QSurfaceDataProxy::setRows(int rowIndex, const
    QSurfaceDataArray &rows)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QSurfaceDataProxy.setRows' has no cute function yet. Qt's 'void "
        "QSurfaceDataProxy::setRows(int rowIndex, const QSurfaceDataArray "
        "&rows)': takes a type Python has no way to hand over yet.")
