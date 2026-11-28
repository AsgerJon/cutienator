"""
QBarDataProxy binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/qbardataproxy.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject, QStringList
from . import QAbstractDataProxy

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPoint
  from . import QBar3DSeries, QBarDataItem, QBarDataProxyPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBar3DSeries = WAIT['QtDataVisualization:QBar3DSeries']
  QBarDataItem = WAIT['QtDataVisualization:QBarDataItem']
  QBarDataProxyPrivate = WAIT['QtDataVisualization:QBarDataProxyPrivate']
  QPoint = WAIT['QPoint']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBarDataProxy(QAbstractDataProxy):
  """
  The cute side of Qt's QBarDataProxy: a plain Python object standing in
  front of one C++ QBarDataProxy.

  It is built on the cute 'QAbstractDataProxy', as Qt's QBarDataProxy is
  built on Qt's QAbstractDataProxy, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QBarDataProxy that has a ritual and that Python can
  call so far, 24 names in all: 'metaObject', 'tr', 'series', 'rowCount',
  'rowLabels', 'setRowLabels', 'columnLabels', 'setColumnLabels', 'itemAt',
  'resetArray', 'setItem', 'removeRows', 'arrayReset', 'rowsAdded',
  'rowsChanged', 'rowsRemoved', 'rowsInserted', 'itemChanged',
  'rowCountChanged', 'rowLabelsChanged', 'columnLabelsChanged',
  'seriesChanged', 'dptr', 'dptrc'. It can be made from Python, in 2 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QBarDataProxy::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QBarDataProxy::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QBarDataProxy::~QBarDataProxy()': the destructor: Python never
    removes a C++ QBarDataProxy.
  - Qt's 'const QBarDataArray *QBarDataProxy::array() const': gives
    'QList<QList<QBarDataItem> *>', which has no cute class yet.
  - Qt's 'const QBarDataRow *QBarDataProxy::rowAt(int rowIndex) const': gives
    'QList<QBarDataItem>', which has no cute class yet.
  - Qt's 'void QBarDataProxy::resetArray(QBarDataArray *newArray)': names
    'QBarDataArray', which has no cute class yet.
  - Qt's 'void QBarDataProxy::resetArray(QBarDataArray *newArray, const
    QStringList &rowLabels, const QStringList &columnLabels)': names
    'QBarDataArray', which has no cute class yet.
  - Qt's 'void QBarDataProxy::setRow(int rowIndex, QBarDataRow *row)': names
    'QBarDataRow', which has no cute class yet.
  - Qt's 'void QBarDataProxy::setRow(int rowIndex, QBarDataRow *row, const
    QString &label)': names 'QBarDataRow', which has no cute class yet.
  - Qt's 'void QBarDataProxy::setRows(int rowIndex, const QBarDataArray
    &rows)': takes a type Python has no way to hand over yet.
  - Qt's 'void QBarDataProxy::setRows(int rowIndex, const QBarDataArray
    &rows, const QStringList &labels)': takes a type Python has no way to
    hand over yet.
  - Qt's 'int QBarDataProxy::addRow(QBarDataRow *row)': names 'QBarDataRow',
    which has no cute class yet.
  - Qt's 'int QBarDataProxy::addRow(QBarDataRow *row, const QString &label)':
    names 'QBarDataRow', which has no cute class yet.
  - Qt's 'int QBarDataProxy::addRows(const QBarDataArray &rows)': takes a
    type Python has no way to hand over yet.
  - Qt's 'int QBarDataProxy::addRows(const QBarDataArray &rows, const
    QStringList &labels)': takes a type Python has no way to hand over yet.
  - Qt's 'void QBarDataProxy::insertRow(int rowIndex, QBarDataRow *row)':
    names 'QBarDataRow', which has no cute class yet.
  - Qt's 'void QBarDataProxy::insertRow(int rowIndex, QBarDataRow *row, const
    QString &label)': names 'QBarDataRow', which has no cute class yet.
  - Qt's 'void QBarDataProxy::insertRows(int rowIndex, const QBarDataArray
    &rows)': takes a type Python has no way to hand over yet.
  - Qt's 'void QBarDataProxy::insertRows(int rowIndex, const QBarDataArray
    &rows, const QStringList &labels)': takes a type Python has no way to
    hand over yet.

  What has no ritual
  ------------------

  4 of the 51 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QBarDataProxy is created at the first use, not by
    'QBarDataProxy(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBarDataProxy.
  - Qt tells when it has removed the C++ QBarDataProxy. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QBarDataProxy that has no cute function yet, 'addRow',
    'addRows', 'array', 'insertRow', 'insertRows', 'rowAt', 'setRow',
    'setRows', holds a function that raises 'NotImplementedError', and its
    docstring says why.
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
    Calls Qt's 'QString QBarDataProxy::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxy.html#tr

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
    #  QString QBarDataProxy::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QBarDataProxy2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBarDataProxy'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtDataVisualization'

  #  A C++ QBarDataProxy Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QBarDataProxy'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QBarDataProxy::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxy.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QBarDataProxy::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QBarDataProxy10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def series(self) -> Optional[QBar3DSeries]:
    """
    Calls Qt's 'QBar3DSeries *QBarDataProxy::series() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxy.html#series

    Returns
    -------

    Optional[QBar3DSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBar3DSeries *QBarDataProxy::series() const
    address = self.uglySide.call('ritual_ZNK13QBarDataProxy6seriesEv')
    from . import QBar3DSeries
    return QBar3DSeries._cuteAt(address)

  def rowCount(self) -> int:
    """
    Calls Qt's 'int QBarDataProxy::rowCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxy.html#rowCount
    """
    #  int QBarDataProxy::rowCount() const
    return self.uglySide.call('ritual_ZNK13QBarDataProxy8rowCountEv')

  def rowLabels(self) -> QStringList:
    """
    Calls Qt's 'QStringList QBarDataProxy::rowLabels() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxy.html#rowLabels

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QBarDataProxy::rowLabels() const
    address = self.uglySide.call('ritual_ZNK13QBarDataProxy9rowLabelsEv')
    return QStringList._cuteOwning(address)

  def columnLabels(self) -> QStringList:
    """
    Calls Qt's 'QStringList QBarDataProxy::columnLabels() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxy.html#columnLabels

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QBarDataProxy::columnLabels() const
    address = self.uglySide.call('ritual_ZNK13QBarDataProxy12columnLabelsEv')
    return QStringList._cuteOwning(address)

  @overload(int, int)
  def itemAt(
      self,
      rowIndex: int,
      columnIndex: int,
  ) -> Optional[QBarDataItem]:
    """
    Calls Qt's 'const QBarDataItem *QBarDataProxy::itemAt(int rowIndex, int
    columnIndex) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxy.html#itemAt

    Parameters
    ----------

    rowIndex : int
      Passed on as it is.

    columnIndex : int
      Passed on as it is.

    Returns
    -------

    Optional[QBarDataItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QBarDataItem *QBarDataProxy::itemAt(int rowIndex, int
    #      columnIndex) const
    address = self.uglySide.call(
        'ritual_ZNK13QBarDataProxy6itemAtEii', rowIndex, columnIndex,
    )
    from . import QBarDataItem
    return QBarDataItem._cuteAt(address)

  @overload(QPoint)
  def itemAt(self, position: QPoint) -> Optional[QBarDataItem]:
    """
    Calls Qt's 'const QBarDataItem *QBarDataProxy::itemAt(const QPoint
    &position) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxy.html#itemAt

    Parameters
    ----------

    position : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    Optional[QBarDataItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QBarDataItem *QBarDataProxy::itemAt(const QPoint &position)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13QBarDataProxy6itemAtERK6QPoint',
        self._valueOf(position),
    )
    from . import QBarDataItem
    return QBarDataItem._cuteAt(address)

  def dptrc(self) -> Optional[QBarDataProxyPrivate]:
    """
    Calls Qt's 'const QBarDataProxyPrivate *QBarDataProxy::dptrc() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxy.html#dptrc

    Returns
    -------

    Optional[QBarDataProxyPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QBarDataProxyPrivate *QBarDataProxy::dptrc() const
    address = self.uglySide.call('ritual_ZNK13QBarDataProxy5dptrcEv')
    from . import QBarDataProxyPrivate
    return QBarDataProxyPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QStringList)
  def setRowLabels(self, labels: QStringList) -> None:
    """
    Calls Qt's 'void QBarDataProxy::setRowLabels(const QStringList &labels)'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxy.html#setRowLabels

    Parameters
    ----------

    labels : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QBarDataProxy::setRowLabels(const QStringList &labels)
    self.uglySide.call(
        'ritual_ZN13QBarDataProxy12setRowLabelsERK5QListI7QStringE',
        self._valueOf(labels),
    )

  @overload(QStringList)
  def setColumnLabels(self, labels: QStringList) -> None:
    """
    Calls Qt's 'void QBarDataProxy::setColumnLabels(const QStringList
    &labels)'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxy.html#setColumnLabels

    Parameters
    ----------

    labels : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QBarDataProxy::setColumnLabels(const QStringList &labels)
    self.uglySide.call(
        'ritual_ZN13QBarDataProxy15setColumnLabelsERK5QListI7QStringE',
        self._valueOf(labels),
    )

  @overload(int, int, QBarDataItem)
  def setItem(
      self,
      rowIndex: int,
      columnIndex: int,
      item: QBarDataItem,
  ) -> None:
    """
    Calls Qt's 'void QBarDataProxy::setItem(int rowIndex, int columnIndex,
    const QBarDataItem &item)'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxy.html#setItem

    Parameters
    ----------

    rowIndex : int
      Passed on as it is.

    columnIndex : int
      Passed on as it is.

    item : QBarDataItem
      Passed on as a value: Qt reads the C++ QBarDataItem, which stays
      Python's own.
    """
    #  void QBarDataProxy::setItem(int rowIndex, int columnIndex, const
    #      QBarDataItem &item)
    self.uglySide.call(
        'ritual_ZN13QBarDataProxy7setItemEiiRK12QBarDataItem',
        rowIndex, columnIndex, self._valueOf(item),
    )

  @overload(QPoint, QBarDataItem)
  def setItem(self, position: QPoint, item: QBarDataItem) -> None:
    """
    Calls Qt's 'void QBarDataProxy::setItem(const QPoint &position, const
    QBarDataItem &item)'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxy.html#setItem

    Parameters
    ----------

    position : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    item : QBarDataItem
      Passed on as a value: Qt reads the C++ QBarDataItem, which stays
      Python's own.
    """
    #  void QBarDataProxy::setItem(const QPoint &position, const QBarDataItem
    #      &item)
    self.uglySide.call(
        'ritual_ZN13QBarDataProxy7setItemERK6QPointRK12QBarDataItem',
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

  @overload(QBarDataProxyPrivate)
  @overload(QBarDataProxyPrivate, QObject)
  @overload(QBarDataProxyPrivate, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      d: Optional[QBarDataProxyPrivate],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QBarDataProxy::QBarDataProxy(QBarDataProxyPrivate *d, QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxy.html#QBarDataProxy

    Parameters
    ----------

    d : Optional[QBarDataProxyPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QBarDataProxy::QBarDataProxy(QBarDataProxyPrivate *d, QObject *parent)
    self._noteCreation(QBarDataProxy, lambda: Rituals.call(
        'ritual_ZN13QBarDataProxyC1EP20QBarDataProxyPrivateP7QObject',
        self._addressOf(d), self._addressOf(parent, 'QObject'),
    ))

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QBarDataProxy::QBarDataProxy(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxy.html#QBarDataProxy

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QBarDataProxy::QBarDataProxy(QObject *parent)
    self._noteCreation(QBarDataProxy, lambda: Rituals.call(
        'ritual_ZN13QBarDataProxyC1EP7QObject',
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

  def resetArray(self) -> None:
    """
    Calls Qt's 'void QBarDataProxy::resetArray()'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxy.html#resetArray
    """
    #  void QBarDataProxy::resetArray()
    self.uglySide.call('ritual_ZN13QBarDataProxy10resetArrayEv')

  @overload(int, int)
  @overload(int, int, bool)
  def removeRows(
      self,
      rowIndex: int,
      removeCount: int,
      removeLabels: bool = True,
  ) -> None:
    """
    Calls Qt's 'void QBarDataProxy::removeRows(int rowIndex, int removeCount,
    bool removeLabels)'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxy.html#removeRows

    Parameters
    ----------

    rowIndex : int
      Passed on as it is.

    removeCount : int
      Passed on as it is.

    removeLabels : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QBarDataProxy::removeRows(int rowIndex, int removeCount, bool
    #      removeLabels)
    self.uglySide.call(
        'ritual_ZN13QBarDataProxy10removeRowsEiib',
        rowIndex, removeCount, removeLabels,
    )

  def arrayReset(self) -> None:
    """
    Calls Qt's 'void QBarDataProxy::arrayReset()'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxy.html#arrayReset
    """
    #  void QBarDataProxy::arrayReset()
    self.uglySide.call('ritual_ZN13QBarDataProxy10arrayResetEv')

  @overload(int, int)
  def rowsAdded(self, startIndex: int, count: int) -> None:
    """
    Calls Qt's 'void QBarDataProxy::rowsAdded(int startIndex, int count)'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxy.html#rowsAdded

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QBarDataProxy::rowsAdded(int startIndex, int count)
    self.uglySide.call(
        'ritual_ZN13QBarDataProxy9rowsAddedEii', startIndex, count,
    )

  @overload(int, int)
  def rowsChanged(self, startIndex: int, count: int) -> None:
    """
    Calls Qt's 'void QBarDataProxy::rowsChanged(int startIndex, int count)'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxy.html#rowsChanged

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QBarDataProxy::rowsChanged(int startIndex, int count)
    self.uglySide.call(
        'ritual_ZN13QBarDataProxy11rowsChangedEii', startIndex, count,
    )

  @overload(int, int)
  def rowsRemoved(self, startIndex: int, count: int) -> None:
    """
    Calls Qt's 'void QBarDataProxy::rowsRemoved(int startIndex, int count)'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxy.html#rowsRemoved

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QBarDataProxy::rowsRemoved(int startIndex, int count)
    self.uglySide.call(
        'ritual_ZN13QBarDataProxy11rowsRemovedEii', startIndex, count,
    )

  @overload(int, int)
  def rowsInserted(self, startIndex: int, count: int) -> None:
    """
    Calls Qt's 'void QBarDataProxy::rowsInserted(int startIndex, int count)'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxy.html#rowsInserted

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QBarDataProxy::rowsInserted(int startIndex, int count)
    self.uglySide.call(
        'ritual_ZN13QBarDataProxy12rowsInsertedEii', startIndex, count,
    )

  @overload(int, int)
  def itemChanged(self, rowIndex: int, columnIndex: int) -> None:
    """
    Calls Qt's 'void QBarDataProxy::itemChanged(int rowIndex, int
    columnIndex)'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxy.html#itemChanged

    Parameters
    ----------

    rowIndex : int
      Passed on as it is.

    columnIndex : int
      Passed on as it is.
    """
    #  void QBarDataProxy::itemChanged(int rowIndex, int columnIndex)
    self.uglySide.call(
        'ritual_ZN13QBarDataProxy11itemChangedEii', rowIndex, columnIndex,
    )

  @overload(int)
  def rowCountChanged(self, count: int) -> None:
    """
    Calls Qt's 'void QBarDataProxy::rowCountChanged(int count)'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxy.html#rowCountChanged

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QBarDataProxy::rowCountChanged(int count)
    self.uglySide.call('ritual_ZN13QBarDataProxy15rowCountChangedEi', count)

  def rowLabelsChanged(self) -> None:
    """
    Calls Qt's 'void QBarDataProxy::rowLabelsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbardataproxy.html#rowLabelsChanged
    """
    #  void QBarDataProxy::rowLabelsChanged()
    self.uglySide.call('ritual_ZN13QBarDataProxy16rowLabelsChangedEv')

  def columnLabelsChanged(self) -> None:
    """
    Calls Qt's 'void QBarDataProxy::columnLabelsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbardataproxy.html#columnLabelsChanged
    """
    #  void QBarDataProxy::columnLabelsChanged()
    self.uglySide.call('ritual_ZN13QBarDataProxy19columnLabelsChangedEv')

  @overload(QBar3DSeries)
  @overload(NoneType)
  def seriesChanged(self, series: Optional[QBar3DSeries]) -> None:
    """
    Calls Qt's 'void QBarDataProxy::seriesChanged(QBar3DSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxy.html#seriesChanged

    Parameters
    ----------

    series : Optional[QBar3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBarDataProxy::seriesChanged(QBar3DSeries *series)
    self.uglySide.call(
        'ritual_ZN13QBarDataProxy13seriesChangedEP12QBar3DSeries',
        self._addressOf(series),
    )

  def dptr(self) -> Optional[QBarDataProxyPrivate]:
    """
    Calls Qt's 'QBarDataProxyPrivate *QBarDataProxy::dptr()'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxy.html#dptr

    Returns
    -------

    Optional[QBarDataProxyPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBarDataProxyPrivate *QBarDataProxy::dptr()
    address = self.uglySide.call('ritual_ZN13QBarDataProxy4dptrEv')
    from . import QBarDataProxyPrivate
    return QBarDataProxyPrivate._cuteAt(address)

  @staticmethod
  def addRow(*__, **_) -> Never:
    """
    - Qt's 'int QBarDataProxy::addRow(QBarDataRow *row)': names
      'QBarDataRow', which has no cute class yet.
    - Qt's 'int QBarDataProxy::addRow(QBarDataRow *row, const QString
      &label)': names 'QBarDataRow', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QBarDataProxy.addRow' has no cute function yet. Qt's 'int "
        "QBarDataProxy::addRow(QBarDataRow *row)': names 'QBarDataRow', "
        "which has no cute class yet. Qt's 'int "
        "QBarDataProxy::addRow(QBarDataRow *row, const QString &label)': "
        "names 'QBarDataRow', which has no cute class yet.")

  @staticmethod
  def addRows(*__, **_) -> Never:
    """
    - Qt's 'int QBarDataProxy::addRows(const QBarDataArray &rows)': takes a
      type Python has no way to hand over yet.
    - Qt's 'int QBarDataProxy::addRows(const QBarDataArray &rows, const
      QStringList &labels)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QBarDataProxy.addRows' has no cute function yet. Qt's 'int "
        "QBarDataProxy::addRows(const QBarDataArray &rows)': takes a type "
        "Python has no way to hand over yet. Qt's 'int "
        "QBarDataProxy::addRows(const QBarDataArray &rows, const "
        "QStringList &labels)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def array(*__, **_) -> Never:
    """
    Qt's 'const QBarDataArray *QBarDataProxy::array() const': gives
    'QList<QList<QBarDataItem> *>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QBarDataProxy.array' has no cute function yet. Qt's 'const "
        "QBarDataArray *QBarDataProxy::array() const': gives "
        "'QList<QList<QBarDataItem> *>', which has no cute class yet.")

  @staticmethod
  def insertRow(*__, **_) -> Never:
    """
    - Qt's 'void QBarDataProxy::insertRow(int rowIndex, QBarDataRow *row)':
      names 'QBarDataRow', which has no cute class yet.
    - Qt's 'void QBarDataProxy::insertRow(int rowIndex, QBarDataRow *row,
      const QString &label)': names 'QBarDataRow', which has no cute class
      yet.
    """
    raise NotImplementedError(
        "'QBarDataProxy.insertRow' has no cute function yet. Qt's 'void "
        "QBarDataProxy::insertRow(int rowIndex, QBarDataRow *row)': names "
        "'QBarDataRow', which has no cute class yet. Qt's 'void "
        "QBarDataProxy::insertRow(int rowIndex, QBarDataRow *row, const "
        "QString &label)': names 'QBarDataRow', which has no cute class yet."
    )

  @staticmethod
  def insertRows(*__, **_) -> Never:
    """
    - Qt's 'void QBarDataProxy::insertRows(int rowIndex, const QBarDataArray
      &rows)': takes a type Python has no way to hand over yet.
    - Qt's 'void QBarDataProxy::insertRows(int rowIndex, const QBarDataArray
      &rows, const QStringList &labels)': takes a type Python has no way to
      hand over yet.
    """
    raise NotImplementedError(
        "'QBarDataProxy.insertRows' has no cute function yet. Qt's 'void "
        "QBarDataProxy::insertRows(int rowIndex, const QBarDataArray "
        "&rows)': takes a type Python has no way to hand over yet. Qt's "
        "'void QBarDataProxy::insertRows(int rowIndex, const QBarDataArray "
        "&rows, const QStringList &labels)': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def rowAt(*__, **_) -> Never:
    """
    Qt's 'const QBarDataRow *QBarDataProxy::rowAt(int rowIndex) const': gives
    'QList<QBarDataItem>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QBarDataProxy.rowAt' has no cute function yet. Qt's 'const "
        "QBarDataRow *QBarDataProxy::rowAt(int rowIndex) const': gives "
        "'QList<QBarDataItem>', which has no cute class yet.")

  @staticmethod
  def setRow(*__, **_) -> Never:
    """
    - Qt's 'void QBarDataProxy::setRow(int rowIndex, QBarDataRow *row)':
      names 'QBarDataRow', which has no cute class yet.
    - Qt's 'void QBarDataProxy::setRow(int rowIndex, QBarDataRow *row, const
      QString &label)': names 'QBarDataRow', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QBarDataProxy.setRow' has no cute function yet. Qt's 'void "
        "QBarDataProxy::setRow(int rowIndex, QBarDataRow *row)': names "
        "'QBarDataRow', which has no cute class yet. Qt's 'void "
        "QBarDataProxy::setRow(int rowIndex, QBarDataRow *row, const "
        "QString &label)': names 'QBarDataRow', which has no cute class yet."
    )

  @staticmethod
  def setRows(*__, **_) -> Never:
    """
    - Qt's 'void QBarDataProxy::setRows(int rowIndex, const QBarDataArray
      &rows)': takes a type Python has no way to hand over yet.
    - Qt's 'void QBarDataProxy::setRows(int rowIndex, const QBarDataArray
      &rows, const QStringList &labels)': takes a type Python has no way to
      hand over yet.
    """
    raise NotImplementedError(
        "'QBarDataProxy.setRows' has no cute function yet. Qt's 'void "
        "QBarDataProxy::setRows(int rowIndex, const QBarDataArray &rows)': "
        "takes a type Python has no way to hand over yet. Qt's 'void "
        "QBarDataProxy::setRows(int rowIndex, const QBarDataArray &rows, "
        "const QStringList &labels)': takes a type Python has no way to "
        "hand over yet.")
