"""
QSurfaceDataProxy binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/qsurfacedataproxy.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
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
  QSurface3DSeries = WAIT['QtGraphs:QSurface3DSeries']
  QSurfaceDataItem = WAIT['QtGraphs:QSurfaceDataItem']

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
  can call so far, 22 names in all: 'metaObject', 'tr', 'd_func', 'series',
  'rowCount', 'columnCount', 'itemAt', 'resetArray', 'setRow', 'setItem',
  'addRow', 'insertRow', 'removeRows', 'arrayReset', 'rowsAdded',
  'rowsChanged', 'rowsRemoved', 'rowsInserted', 'itemChanged',
  'rowCountChanged', 'columnCountChanged', 'seriesChanged'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSurfaceDataProxy::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QSurfaceDataProxy::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QSurfaceDataProxyPrivate *QSurfaceDataProxy::d_func() const':
    takes in Python what 'QSurfaceDataProxyPrivate
    *QSurfaceDataProxy::d_func()' takes.
  - Qt's 'void QSurfaceDataProxy::qt_qmlMarker_uncreatable()': one of Qt's
    own inner workings.
  - Qt's 'QSurfaceDataProxy::~QSurfaceDataProxy()': the destructor: Python
    never removes a C++ QSurfaceDataProxy.
  - Qt's 'void QSurfaceDataProxy::resetArray(QSurfaceDataArray newArray)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QSurfaceDataProxy::setRows(qsizetype rowIndex,
    QSurfaceDataArray rows)': takes a type Python has no way to hand over
    yet.
  - Qt's 'qsizetype QSurfaceDataProxy::addRows(QSurfaceDataArray rows)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QSurfaceDataProxy::insertRows(qsizetype rowIndex,
    QSurfaceDataArray rows)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QSurfaceDataProxy::QSurfaceDataProxy(QSurfaceDataProxyPrivate &d,
    QObject *parent)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 39 functions Qt declares: 2 not a gap; 2 forbidden.

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
    'addRows', 'insertRows', 'setRows', holds a function that raises
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
  __qt_part__ = 'QtGraphs'

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
    Calls Qt's 'qsizetype QSurfaceDataProxy::rowCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfacedataproxy.html#rowCount
    """
    #  qsizetype QSurfaceDataProxy::rowCount() const
    return self.uglySide.call('ritual_ZNK17QSurfaceDataProxy8rowCountEv')

  def columnCount(self) -> int:
    """
    Calls Qt's 'qsizetype QSurfaceDataProxy::columnCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfacedataproxy.html#columnCount
    """
    #  qsizetype QSurfaceDataProxy::columnCount() const
    return self.uglySide.call('ritual_ZNK17QSurfaceDataProxy11columnCountEv')

  @overload(int, int)
  def itemAt(self, rowIndex: int, columnIndex: int) -> QSurfaceDataItem:
    """
    Calls Qt's 'const QSurfaceDataItem &QSurfaceDataProxy::itemAt(qsizetype
    rowIndex, qsizetype columnIndex) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfacedataproxy.html#itemAt

    Parameters
    ----------

    rowIndex : int
      Passed on as it is.

    columnIndex : int
      Passed on as it is.

    Returns
    -------

    QSurfaceDataItem
      A new cute QSurfaceDataItem around the copy Qt gave back. Python owns
      it.
    """
    #  const QSurfaceDataItem &QSurfaceDataProxy::itemAt(qsizetype rowIndex,
    #      qsizetype columnIndex) const
    address = self.uglySide.call(
        'ritual_ZNK17QSurfaceDataProxy6itemAtExx', rowIndex, columnIndex,
    )
    from . import QSurfaceDataItem
    return QSurfaceDataItem._cuteOwning(address)

  @overload(QPoint)
  def itemAt(self, position: QPoint) -> QSurfaceDataItem:
    """
    Calls Qt's 'const QSurfaceDataItem &QSurfaceDataProxy::itemAt(QPoint
    position) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfacedataproxy.html#itemAt

    Parameters
    ----------

    position : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QSurfaceDataItem
      A new cute QSurfaceDataItem around the copy Qt gave back. Python owns
      it.
    """
    #  const QSurfaceDataItem &QSurfaceDataProxy::itemAt(QPoint position)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK17QSurfaceDataProxy6itemAtE6QPoint',
        self._valueOf(position),
    )
    from . import QSurfaceDataItem
    return QSurfaceDataItem._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, QList[QSurfaceDataItem])
  def setRow(self, rowIndex: int, row: QList[QSurfaceDataItem]) -> None:
    """
    Calls Qt's 'void QSurfaceDataProxy::setRow(qsizetype rowIndex,
    QSurfaceDataRow row)'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfacedataproxy.html#setRow

    Parameters
    ----------

    rowIndex : int
      Passed on as it is.

    row : QList[QSurfaceDataItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QSurfaceDataProxy::setRow(qsizetype rowIndex, QSurfaceDataRow
    #      row)
    self.uglySide.call(
        'ritual_ZN17QSurfaceDataProxy6setRowEx5QListI16QSurfaceDataItemE',
        rowIndex, self._valueOf(row),
    )

  @overload(int, int, QSurfaceDataItem)
  def setItem(
      self,
      rowIndex: int,
      columnIndex: int,
      item: QSurfaceDataItem,
  ) -> None:
    """
    Calls Qt's 'void QSurfaceDataProxy::setItem(qsizetype rowIndex, qsizetype
    columnIndex, QSurfaceDataItem item)'.

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
    #  void QSurfaceDataProxy::setItem(qsizetype rowIndex, qsizetype
    #      columnIndex, QSurfaceDataItem item)
    self.uglySide.call(
        'ritual_ZN17QSurfaceDataProxy7setItemExx16QSurfaceDataItem',
        rowIndex, columnIndex, self._valueOf(item),
    )

  @overload(QPoint, QSurfaceDataItem)
  def setItem(self, position: QPoint, item: QSurfaceDataItem) -> None:
    """
    Calls Qt's 'void QSurfaceDataProxy::setItem(QPoint position,
    QSurfaceDataItem item)'.

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
    #  void QSurfaceDataProxy::setItem(QPoint position, QSurfaceDataItem
    #      item)
    self.uglySide.call(
        'ritual_ZN17QSurfaceDataProxy7setItemE6QPoint16QSurfaceDataItem',
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

  def d_func(self) -> Optional[QSurfaceDataProxyPrivate]:
    """
    Calls Qt's 'QSurfaceDataProxyPrivate *QSurfaceDataProxy::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfacedataproxy.html#d_func

    Returns
    -------

    Optional[QSurfaceDataProxyPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSurfaceDataProxyPrivate *QSurfaceDataProxy::d_func()
    address = self.uglySide.call('ritual_ZN17QSurfaceDataProxy6d_funcEv')
    from . import QSurfaceDataProxyPrivate
    return QSurfaceDataProxyPrivate._cuteAt(address)

  def resetArray(self) -> None:
    """
    Calls Qt's 'void QSurfaceDataProxy::resetArray()'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfacedataproxy.html#resetArray
    """
    #  void QSurfaceDataProxy::resetArray()
    self.uglySide.call('ritual_ZN17QSurfaceDataProxy10resetArrayEv')

  @overload(QList[QSurfaceDataItem])
  def addRow(self, row: QList[QSurfaceDataItem]) -> int:
    """
    Calls Qt's 'qsizetype QSurfaceDataProxy::addRow(QSurfaceDataRow row)'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfacedataproxy.html#addRow

    Parameters
    ----------

    row : QList[QSurfaceDataItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  qsizetype QSurfaceDataProxy::addRow(QSurfaceDataRow row)
    return self.uglySide.call(
        'ritual_ZN17QSurfaceDataProxy6addRowE5QListI16QSurfaceDataItemE',
        self._valueOf(row),
    )

  @overload(int, QList[QSurfaceDataItem])
  def insertRow(self, rowIndex: int, row: QList[QSurfaceDataItem]) -> None:
    """
    Calls Qt's 'void QSurfaceDataProxy::insertRow(qsizetype rowIndex,
    QSurfaceDataRow row)'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfacedataproxy.html#insertRow

    Parameters
    ----------

    rowIndex : int
      Passed on as it is.

    row : QList[QSurfaceDataItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QSurfaceDataProxy::insertRow(qsizetype rowIndex, QSurfaceDataRow
    #      row)
    self.uglySide.call(
        'ritual_ZN17QSurfaceDataProxy9insertRowEx5QListI16QSurfaceDataItemE',
        rowIndex, self._valueOf(row),
    )

  @overload(int, int)
  def removeRows(self, rowIndex: int, removeCount: int) -> None:
    """
    Calls Qt's 'void QSurfaceDataProxy::removeRows(qsizetype rowIndex,
    qsizetype removeCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfacedataproxy.html#removeRows

    Parameters
    ----------

    rowIndex : int
      Passed on as it is.

    removeCount : int
      Passed on as it is.
    """
    #  void QSurfaceDataProxy::removeRows(qsizetype rowIndex, qsizetype
    #      removeCount)
    self.uglySide.call(
        'ritual_ZN17QSurfaceDataProxy10removeRowsExx', rowIndex, removeCount,
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
    Calls Qt's 'void QSurfaceDataProxy::rowsAdded(qsizetype startIndex,
    qsizetype count)'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfacedataproxy.html#rowsAdded

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QSurfaceDataProxy::rowsAdded(qsizetype startIndex, qsizetype
    #      count)
    self.uglySide.call(
        'ritual_ZN17QSurfaceDataProxy9rowsAddedExx', startIndex, count,
    )

  @overload(int, int)
  def rowsChanged(self, startIndex: int, count: int) -> None:
    """
    Calls Qt's 'void QSurfaceDataProxy::rowsChanged(qsizetype startIndex,
    qsizetype count)'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfacedataproxy.html#rowsChanged

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QSurfaceDataProxy::rowsChanged(qsizetype startIndex, qsizetype
    #      count)
    self.uglySide.call(
        'ritual_ZN17QSurfaceDataProxy11rowsChangedExx', startIndex, count,
    )

  @overload(int, int)
  def rowsRemoved(self, startIndex: int, count: int) -> None:
    """
    Calls Qt's 'void QSurfaceDataProxy::rowsRemoved(qsizetype startIndex,
    qsizetype count)'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfacedataproxy.html#rowsRemoved

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QSurfaceDataProxy::rowsRemoved(qsizetype startIndex, qsizetype
    #      count)
    self.uglySide.call(
        'ritual_ZN17QSurfaceDataProxy11rowsRemovedExx', startIndex, count,
    )

  @overload(int, int)
  def rowsInserted(self, startIndex: int, count: int) -> None:
    """
    Calls Qt's 'void QSurfaceDataProxy::rowsInserted(qsizetype startIndex,
    qsizetype count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfacedataproxy.html#rowsInserted

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QSurfaceDataProxy::rowsInserted(qsizetype startIndex, qsizetype
    #      count)
    self.uglySide.call(
        'ritual_ZN17QSurfaceDataProxy12rowsInsertedExx', startIndex, count,
    )

  @overload(int, int)
  def itemChanged(self, rowIndex: int, columnIndex: int) -> None:
    """
    Calls Qt's 'void QSurfaceDataProxy::itemChanged(qsizetype rowIndex,
    qsizetype columnIndex)'.

    Qt's own words: https://doc.qt.io/qt-6/qsurfacedataproxy.html#itemChanged

    Parameters
    ----------

    rowIndex : int
      Passed on as it is.

    columnIndex : int
      Passed on as it is.
    """
    #  void QSurfaceDataProxy::itemChanged(qsizetype rowIndex, qsizetype
    #      columnIndex)
    self.uglySide.call(
        'ritual_ZN17QSurfaceDataProxy11itemChangedExx',
        rowIndex, columnIndex,
    )

  @overload(int)
  def rowCountChanged(self, count: int) -> None:
    """
    Calls Qt's 'void QSurfaceDataProxy::rowCountChanged(qsizetype count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfacedataproxy.html#rowCountChanged

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QSurfaceDataProxy::rowCountChanged(qsizetype count)
    self.uglySide.call(
        'ritual_ZN17QSurfaceDataProxy15rowCountChangedEx', count,
    )

  @overload(int)
  def columnCountChanged(self, count: int) -> None:
    """
    Calls Qt's 'void QSurfaceDataProxy::columnCountChanged(qsizetype count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurfacedataproxy.html#columnCountChanged

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QSurfaceDataProxy::columnCountChanged(qsizetype count)
    self.uglySide.call(
        'ritual_ZN17QSurfaceDataProxy18columnCountChangedEx', count,
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

  @staticmethod
  def addRows(*__, **_) -> Never:
    """
    Qt's 'qsizetype QSurfaceDataProxy::addRows(QSurfaceDataArray rows)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSurfaceDataProxy.addRows' has no cute function yet. Qt's "
        "'qsizetype QSurfaceDataProxy::addRows(QSurfaceDataArray rows)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def insertRows(*__, **_) -> Never:
    """
    Qt's 'void QSurfaceDataProxy::insertRows(qsizetype rowIndex,
    QSurfaceDataArray rows)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QSurfaceDataProxy.insertRows' has no cute function yet. Qt's "
        "'void QSurfaceDataProxy::insertRows(qsizetype rowIndex, "
        "QSurfaceDataArray rows)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def setRows(*__, **_) -> Never:
    """
    Qt's 'void QSurfaceDataProxy::setRows(qsizetype rowIndex,
    QSurfaceDataArray rows)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QSurfaceDataProxy.setRows' has no cute function yet. Qt's 'void "
        "QSurfaceDataProxy::setRows(qsizetype rowIndex, QSurfaceDataArray "
        "rows)': takes a type Python has no way to hand over yet.")
