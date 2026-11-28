"""
QBarDataProxy binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/qbardataproxy.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QAbstractDataProxy

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPoint
  from . import QBar3DSeries, QBarDataItem, QBarDataProxyPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBar3DSeries = WAIT['QtGraphs:QBar3DSeries']
  QBarDataItem = WAIT['QtGraphs:QBarDataItem']
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
  call so far, 23 names in all: 'metaObject', 'tr', 'd_func', 'series',
  'rowCount', 'colCount', 'rowAt', 'itemAt', 'resetArray', 'setRow',
  'setItem', 'addRow', 'insertRow', 'removeRows', 'arrayReset', 'rowsAdded',
  'rowsChanged', 'rowsRemoved', 'rowsInserted', 'itemChanged',
  'rowCountChanged', 'colCountChanged', 'seriesChanged'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QBarDataProxy::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QBarDataProxy::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QBarDataProxyPrivate *QBarDataProxy::d_func() const': takes
    in Python what 'QBarDataProxyPrivate *QBarDataProxy::d_func()' takes.
  - Qt's 'void QBarDataProxy::qt_qmlMarker_uncreatable()': one of Qt's own
    inner workings.
  - Qt's 'QBarDataProxy::~QBarDataProxy()': the destructor: Python never
    removes a C++ QBarDataProxy.
  - Qt's 'void QBarDataProxy::resetArray(QBarDataArray newArray)': takes a
    type Python has no way to hand over yet.
  - Qt's 'void QBarDataProxy::resetArray(QBarDataArray newArray, QStringList
    rowLabels, QStringList columnLabels)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QBarDataProxy::setRows(qsizetype rowIndex, QBarDataArray
    rows)': takes a type Python has no way to hand over yet.
  - Qt's 'void QBarDataProxy::setRows(qsizetype rowIndex, QBarDataArray rows,
    QStringList labels)': takes a type Python has no way to hand over yet.
  - Qt's 'qsizetype QBarDataProxy::addRows(QBarDataArray rows)': takes a type
    Python has no way to hand over yet.
  - Qt's 'qsizetype QBarDataProxy::addRows(QBarDataArray rows, QStringList
    labels)': takes a type Python has no way to hand over yet.
  - Qt's 'void QBarDataProxy::insertRows(qsizetype rowIndex, QBarDataArray
    rows)': takes a type Python has no way to hand over yet.
  - Qt's 'void QBarDataProxy::insertRows(qsizetype rowIndex, QBarDataArray
    rows, QStringList labels)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QBarDataProxy::QBarDataProxy(QBarDataProxyPrivate &d, QObject
    *parent)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 47 functions Qt declares: 2 not a gap; 2 forbidden.

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
  - Each name of Qt's QBarDataProxy that has no cute function yet, 'addRows',
    'insertRows', 'setRows', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QBarDataProxy, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class RemoveLabels(CuteNum, scoped=True):
    """
    The enum 'QBarDataProxy::RemoveLabels' of Qt, with the 2 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    No = Kee[int](0)
    Yes = Kee[int](1)

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
  __qt_part__ = 'QtGraphs'

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
    Calls Qt's 'qsizetype QBarDataProxy::rowCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxy.html#rowCount
    """
    #  qsizetype QBarDataProxy::rowCount() const
    return self.uglySide.call('ritual_ZNK13QBarDataProxy8rowCountEv')

  def colCount(self) -> int:
    """
    Calls Qt's 'qsizetype QBarDataProxy::colCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxy.html#colCount
    """
    #  qsizetype QBarDataProxy::colCount() const
    return self.uglySide.call('ritual_ZNK13QBarDataProxy8colCountEv')

  @overload(int)
  def rowAt(self, rowIndex: int) -> QList[QBarDataItem]:
    """
    Calls Qt's 'const QBarDataRow &QBarDataProxy::rowAt(qsizetype rowIndex)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxy.html#rowAt

    Parameters
    ----------

    rowIndex : int
      Passed on as it is.

    Returns
    -------

    QList[QBarDataItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QBarDataRow &QBarDataProxy::rowAt(qsizetype rowIndex) const
    address = self.uglySide.call(
        'ritual_ZNK13QBarDataProxy5rowAtEx', rowIndex,
    )
    from . import QBarDataItem
    return QList[QBarDataItem]._cuteOwning(address)

  @overload(int, int)
  def itemAt(self, rowIndex: int, columnIndex: int) -> QBarDataItem:
    """
    Calls Qt's 'const QBarDataItem &QBarDataProxy::itemAt(qsizetype rowIndex,
    qsizetype columnIndex) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxy.html#itemAt

    Parameters
    ----------

    rowIndex : int
      Passed on as it is.

    columnIndex : int
      Passed on as it is.

    Returns
    -------

    QBarDataItem
      A new cute QBarDataItem around the copy Qt gave back. Python owns it.
    """
    #  const QBarDataItem &QBarDataProxy::itemAt(qsizetype rowIndex,
    #      qsizetype columnIndex) const
    address = self.uglySide.call(
        'ritual_ZNK13QBarDataProxy6itemAtExx', rowIndex, columnIndex,
    )
    from . import QBarDataItem
    return QBarDataItem._cuteOwning(address)

  @overload(QPoint)
  def itemAt(self, position: QPoint) -> QBarDataItem:
    """
    Calls Qt's 'const QBarDataItem &QBarDataProxy::itemAt(QPoint position)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxy.html#itemAt

    Parameters
    ----------

    position : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QBarDataItem
      A new cute QBarDataItem around the copy Qt gave back. Python owns it.
    """
    #  const QBarDataItem &QBarDataProxy::itemAt(QPoint position) const
    address = self.uglySide.call(
        'ritual_ZNK13QBarDataProxy6itemAtE6QPoint', self._valueOf(position),
    )
    from . import QBarDataItem
    return QBarDataItem._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, QList[QBarDataItem])
  def setRow(self, rowIndex: int, row: QList[QBarDataItem]) -> None:
    """
    Calls Qt's 'void QBarDataProxy::setRow(qsizetype rowIndex, QBarDataRow
    row)'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxy.html#setRow

    Parameters
    ----------

    rowIndex : int
      Passed on as it is.

    row : QList[QBarDataItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QBarDataProxy::setRow(qsizetype rowIndex, QBarDataRow row)
    self.uglySide.call(
        'ritual_ZN13QBarDataProxy6setRowEx5QListI12QBarDataItemE',
        rowIndex, self._valueOf(row),
    )

  @overload(int, QList[QBarDataItem], str)
  def setRow(
      self,
      rowIndex: int,
      row: QList[QBarDataItem],
      label: str,
  ) -> None:
    """
    Calls Qt's 'void QBarDataProxy::setRow(qsizetype rowIndex, QBarDataRow
    row, QString label)'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxy.html#setRow

    Parameters
    ----------

    rowIndex : int
      Passed on as it is.

    row : QList[QBarDataItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    label : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QBarDataProxy::setRow(qsizetype rowIndex, QBarDataRow row,
    #      QString label)
    self.uglySide.call(
        'ritual_ZN13QBarDataProxy6setRowEx5QListI12QBarDataItemE7QString',
        rowIndex, self._valueOf(row), label,
    )

  @overload(int, int, QBarDataItem)
  def setItem(
      self,
      rowIndex: int,
      columnIndex: int,
      item: QBarDataItem,
  ) -> None:
    """
    Calls Qt's 'void QBarDataProxy::setItem(qsizetype rowIndex, qsizetype
    columnIndex, QBarDataItem item)'.

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
    #  void QBarDataProxy::setItem(qsizetype rowIndex, qsizetype columnIndex,
    #      QBarDataItem item)
    self.uglySide.call(
        'ritual_ZN13QBarDataProxy7setItemExx12QBarDataItem',
        rowIndex, columnIndex, self._valueOf(item),
    )

  @overload(QPoint, QBarDataItem)
  def setItem(self, position: QPoint, item: QBarDataItem) -> None:
    """
    Calls Qt's 'void QBarDataProxy::setItem(QPoint position, QBarDataItem
    item)'.

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
    #  void QBarDataProxy::setItem(QPoint position, QBarDataItem item)
    self.uglySide.call(
        'ritual_ZN13QBarDataProxy7setItemE6QPoint12QBarDataItem',
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

  def d_func(self) -> Optional[QBarDataProxyPrivate]:
    """
    Calls Qt's 'QBarDataProxyPrivate *QBarDataProxy::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxy.html#d_func

    Returns
    -------

    Optional[QBarDataProxyPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBarDataProxyPrivate *QBarDataProxy::d_func()
    address = self.uglySide.call('ritual_ZN13QBarDataProxy6d_funcEv')
    from . import QBarDataProxyPrivate
    return QBarDataProxyPrivate._cuteAt(address)

  def resetArray(self) -> None:
    """
    Calls Qt's 'void QBarDataProxy::resetArray()'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxy.html#resetArray
    """
    #  void QBarDataProxy::resetArray()
    self.uglySide.call('ritual_ZN13QBarDataProxy10resetArrayEv')

  @overload(QList[QBarDataItem])
  def addRow(self, row: QList[QBarDataItem]) -> int:
    """
    Calls Qt's 'qsizetype QBarDataProxy::addRow(QBarDataRow row)'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxy.html#addRow

    Parameters
    ----------

    row : QList[QBarDataItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  qsizetype QBarDataProxy::addRow(QBarDataRow row)
    return self.uglySide.call(
        'ritual_ZN13QBarDataProxy6addRowE5QListI12QBarDataItemE',
        self._valueOf(row),
    )

  @overload(QList[QBarDataItem], str)
  def addRow(self, row: QList[QBarDataItem], label: str) -> int:
    """
    Calls Qt's 'qsizetype QBarDataProxy::addRow(QBarDataRow row, QString
    label)'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxy.html#addRow

    Parameters
    ----------

    row : QList[QBarDataItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    label : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  qsizetype QBarDataProxy::addRow(QBarDataRow row, QString label)
    return self.uglySide.call(
        'ritual_ZN13QBarDataProxy6addRowE5QListI12QBarDataItemE7QString',
        self._valueOf(row), label,
    )

  @overload(int, QList[QBarDataItem])
  def insertRow(self, rowIndex: int, row: QList[QBarDataItem]) -> None:
    """
    Calls Qt's 'void QBarDataProxy::insertRow(qsizetype rowIndex, QBarDataRow
    row)'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxy.html#insertRow

    Parameters
    ----------

    rowIndex : int
      Passed on as it is.

    row : QList[QBarDataItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QBarDataProxy::insertRow(qsizetype rowIndex, QBarDataRow row)
    self.uglySide.call(
        'ritual_ZN13QBarDataProxy9insertRowEx5QListI12QBarDataItemE',
        rowIndex, self._valueOf(row),
    )

  @overload(int, QList[QBarDataItem], str)
  def insertRow(
      self,
      rowIndex: int,
      row: QList[QBarDataItem],
      label: str,
  ) -> None:
    """
    Calls Qt's 'void QBarDataProxy::insertRow(qsizetype rowIndex, QBarDataRow
    row, QString label)'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxy.html#insertRow

    Parameters
    ----------

    rowIndex : int
      Passed on as it is.

    row : QList[QBarDataItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    label : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QBarDataProxy::insertRow(qsizetype rowIndex, QBarDataRow row,
    #      QString label)
    self.uglySide.call(
        'ritual_ZN13QBarDataProxy9insertRowEx5QListI12QBarDataItemE7QString',
        rowIndex, self._valueOf(row), label,
    )

  @overload(int, int)
  @overload(int, int, RemoveLabels)
  def removeRows(
      self,
      rowIndex: int,
      removeCount: int,
      removeLabels: RemoveLabels = RemoveLabels.No,
  ) -> None:
    """
    Calls Qt's 'void QBarDataProxy::removeRows(qsizetype rowIndex, qsizetype
    removeCount, RemoveLabels removeLabels)'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxy.html#removeRows

    Parameters
    ----------

    rowIndex : int
      Passed on as it is.

    removeCount : int
      Passed on as it is.

    removeLabels : RemoveLabels
      Passed on as its number. May be left out, as in Qt: it is then
      RemoveLabels.No.
    """
    #  void QBarDataProxy::removeRows(qsizetype rowIndex, qsizetype
    #      removeCount, RemoveLabels removeLabels)
    self.uglySide.call(
        'ritual_ZN13QBarDataProxy10removeRowsExxNS_12RemoveLabelsE',
        rowIndex, removeCount, removeLabels.value,
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
    Calls Qt's 'void QBarDataProxy::rowsAdded(qsizetype startIndex, qsizetype
    count)'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxy.html#rowsAdded

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QBarDataProxy::rowsAdded(qsizetype startIndex, qsizetype count)
    self.uglySide.call(
        'ritual_ZN13QBarDataProxy9rowsAddedExx', startIndex, count,
    )

  @overload(int, int)
  def rowsChanged(self, startIndex: int, count: int) -> None:
    """
    Calls Qt's 'void QBarDataProxy::rowsChanged(qsizetype startIndex,
    qsizetype count)'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxy.html#rowsChanged

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QBarDataProxy::rowsChanged(qsizetype startIndex, qsizetype count)
    self.uglySide.call(
        'ritual_ZN13QBarDataProxy11rowsChangedExx', startIndex, count,
    )

  @overload(int, int)
  def rowsRemoved(self, startIndex: int, count: int) -> None:
    """
    Calls Qt's 'void QBarDataProxy::rowsRemoved(qsizetype startIndex,
    qsizetype count)'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxy.html#rowsRemoved

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QBarDataProxy::rowsRemoved(qsizetype startIndex, qsizetype count)
    self.uglySide.call(
        'ritual_ZN13QBarDataProxy11rowsRemovedExx', startIndex, count,
    )

  @overload(int, int)
  def rowsInserted(self, startIndex: int, count: int) -> None:
    """
    Calls Qt's 'void QBarDataProxy::rowsInserted(qsizetype startIndex,
    qsizetype count)'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxy.html#rowsInserted

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QBarDataProxy::rowsInserted(qsizetype startIndex, qsizetype
    #      count)
    self.uglySide.call(
        'ritual_ZN13QBarDataProxy12rowsInsertedExx', startIndex, count,
    )

  @overload(int, int)
  def itemChanged(self, rowIndex: int, columnIndex: int) -> None:
    """
    Calls Qt's 'void QBarDataProxy::itemChanged(qsizetype rowIndex, qsizetype
    columnIndex)'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxy.html#itemChanged

    Parameters
    ----------

    rowIndex : int
      Passed on as it is.

    columnIndex : int
      Passed on as it is.
    """
    #  void QBarDataProxy::itemChanged(qsizetype rowIndex, qsizetype
    #      columnIndex)
    self.uglySide.call(
        'ritual_ZN13QBarDataProxy11itemChangedExx', rowIndex, columnIndex,
    )

  @overload(int)
  def rowCountChanged(self, count: int) -> None:
    """
    Calls Qt's 'void QBarDataProxy::rowCountChanged(qsizetype count)'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxy.html#rowCountChanged

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QBarDataProxy::rowCountChanged(qsizetype count)
    self.uglySide.call('ritual_ZN13QBarDataProxy15rowCountChangedEx', count)

  @overload(int)
  def colCountChanged(self, count: int) -> None:
    """
    Calls Qt's 'void QBarDataProxy::colCountChanged(qsizetype count)'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxy.html#colCountChanged

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QBarDataProxy::colCountChanged(qsizetype count)
    self.uglySide.call('ritual_ZN13QBarDataProxy15colCountChangedEx', count)

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

  @staticmethod
  def addRows(*__, **_) -> Never:
    """
    - Qt's 'qsizetype QBarDataProxy::addRows(QBarDataArray rows)': takes a
      type Python has no way to hand over yet.
    - Qt's 'qsizetype QBarDataProxy::addRows(QBarDataArray rows, QStringList
      labels)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QBarDataProxy.addRows' has no cute function yet. Qt's 'qsizetype "
        "QBarDataProxy::addRows(QBarDataArray rows)': takes a type Python "
        "has no way to hand over yet. Qt's 'qsizetype "
        "QBarDataProxy::addRows(QBarDataArray rows, QStringList labels)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def insertRows(*__, **_) -> Never:
    """
    - Qt's 'void QBarDataProxy::insertRows(qsizetype rowIndex, QBarDataArray
      rows)': takes a type Python has no way to hand over yet.
    - Qt's 'void QBarDataProxy::insertRows(qsizetype rowIndex, QBarDataArray
      rows, QStringList labels)': takes a type Python has no way to hand over
      yet.
    """
    raise NotImplementedError(
        "'QBarDataProxy.insertRows' has no cute function yet. Qt's 'void "
        "QBarDataProxy::insertRows(qsizetype rowIndex, QBarDataArray "
        "rows)': takes a type Python has no way to hand over yet. Qt's "
        "'void QBarDataProxy::insertRows(qsizetype rowIndex, QBarDataArray "
        "rows, QStringList labels)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def setRows(*__, **_) -> Never:
    """
    - Qt's 'void QBarDataProxy::setRows(qsizetype rowIndex, QBarDataArray
      rows)': takes a type Python has no way to hand over yet.
    - Qt's 'void QBarDataProxy::setRows(qsizetype rowIndex, QBarDataArray
      rows, QStringList labels)': takes a type Python has no way to hand over
      yet.
    """
    raise NotImplementedError(
        "'QBarDataProxy.setRows' has no cute function yet. Qt's 'void "
        "QBarDataProxy::setRows(qsizetype rowIndex, QBarDataArray rows)': "
        "takes a type Python has no way to hand over yet. Qt's 'void "
        "QBarDataProxy::setRows(qsizetype rowIndex, QBarDataArray rows, "
        "QStringList labels)': takes a type Python has no way to hand over "
        "yet.")
