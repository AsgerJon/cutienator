"""
QBarDataProxyPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/qbardataproxy_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QBarDataProxyPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QStringList
from . import QAbstractDataProxyPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QAbstract3DSeries, QBarDataItem, QBarDataProxy
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstract3DSeries = WAIT['QtDataVisualization:QAbstract3DSeries']
  QBarDataItem = WAIT['QtDataVisualization:QBarDataItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBarDataProxyPrivate(QAbstractDataProxyPrivate):
  """
  The cute side of Qt's QBarDataProxyPrivate: a plain Python object standing
  in front of one C++ QBarDataProxyPrivate.

  It is built on the cute 'QAbstractDataProxyPrivate', as Qt's
  QBarDataProxyPrivate is built on Qt's QAbstractDataProxyPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QBarDataProxyPrivate that has a ritual and that
  Python can call so far, 8 names in all: 'metaObject', 'setItem',
  'removeRows', 'setSeries', 'qptr', 'clearRow', 'clearArray',
  'fixRowLabels'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QBarDataProxyPrivate::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QBarDataProxyPrivate::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QBarDataProxyPrivate::~QBarDataProxyPrivate()': the destructor:
    Python never removes a C++ QBarDataProxyPrivate.
  - Qt's 'void QBarDataProxyPrivate::resetArray(QBarDataArray *newArray,
    const QStringList *rowLabels, const QStringList *columnLabels)': names
    'QBarDataArray', which has no cute class yet.
  - Qt's 'void QBarDataProxyPrivate::setRow(int rowIndex, QBarDataRow *row,
    const QString *label)': names 'QBarDataRow', which has no cute class yet.
  - Qt's 'void QBarDataProxyPrivate::setRows(int rowIndex, const
    QBarDataArray &rows, const QStringList *labels)': takes a type Python has
    no way to hand over yet.
  - Qt's 'int QBarDataProxyPrivate::addRow(QBarDataRow *row, const QString
    *label)': names 'QBarDataRow', which has no cute class yet.
  - Qt's 'int QBarDataProxyPrivate::addRows(const QBarDataArray &rows, const
    QStringList *labels)': takes a type Python has no way to hand over yet.
  - Qt's 'void QBarDataProxyPrivate::insertRow(int rowIndex, QBarDataRow
    *row, const QString *label)': names 'QBarDataRow', which has no cute
    class yet.
  - Qt's 'void QBarDataProxyPrivate::insertRows(int rowIndex, const
    QBarDataArray &rows, const QStringList *labels)': takes a type Python has
    no way to hand over yet.
  - Qt's 'QPair<GLfloat, GLfloat> QBarDataProxyPrivate::limitValues(int
    startRow, int startColumn, int rowCount, int columnCount) const': gives a
    type Python has no way to take yet.

  What has no ritual
  ------------------

  4 of the 23 functions Qt declares: 2 not a gap; 2 leans on
  'QBarDataProxyPrivate.

  What to expect
  --------------

  - The C++ QBarDataProxyPrivate is created at the first use, not by
    'QBarDataProxyPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBarDataProxyPrivate.
  - Qt tells when it has removed the C++ QBarDataProxyPrivate. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QBarDataProxyPrivate that has no cute function yet,
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
  __qt_class__ = 'QBarDataProxyPrivate'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtDataVisualization'

  #  A C++ QBarDataProxyPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QBarDataProxyPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QBarDataProxyPrivate::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbardataproxyprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QBarDataProxyPrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QBarDataProxyPrivate10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, int, QBarDataItem)
  def setItem(
      self,
      rowIndex: int,
      columnIndex: int,
      item: QBarDataItem,
  ) -> None:
    """
    Calls Qt's 'void QBarDataProxyPrivate::setItem(int rowIndex, int
    columnIndex, const QBarDataItem &item)'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxyprivate.html#setItem

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
    #  void QBarDataProxyPrivate::setItem(int rowIndex, int columnIndex,
    #      const QBarDataItem &item)
    self.uglySide.call(
        'ritual_ZN20QBarDataProxyPrivate7setItemEiiRK12QBarDataItem',
        rowIndex, columnIndex, self._valueOf(item),
    )

  @overload(QAbstract3DSeries)
  @overload(NoneType)
  def setSeries(self, series: Optional[QAbstract3DSeries]) -> None:
    """
    Calls Qt's 'void QBarDataProxyPrivate::setSeries(QAbstract3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbardataproxyprivate.html#setSeries

    Parameters
    ----------

    series : Optional[QAbstract3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBarDataProxyPrivate::setSeries(QAbstract3DSeries *series)
    ritual = 'ritual_ZN20QBarDataProxyPrivate9setSeriesEP17QAbstract3DSeries'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QBarDataProxyPrivate9setSeriesEP17QAbstract3DSeri'
          'es')
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
    Qt's 'QBarDataProxyPrivate::QBarDataProxyPrivate(QBarDataProxy *q)':
    leans on 'QBarDataProxyPrivate::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QBarDataProxyPrivate.__init__' has no cute function yet. Qt's "
        "'QBarDataProxyPrivate::QBarDataProxyPrivate(QBarDataProxy *q)': "
        "leans on 'QBarDataProxyPrivate::qt_metacall(QMetaObject::Call, "
        "int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

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

  @overload(int, int, bool)
  def removeRows(
      self,
      rowIndex: int,
      removeCount: int,
      removeLabels: bool,
  ) -> None:
    """
    Calls Qt's 'void QBarDataProxyPrivate::removeRows(int rowIndex, int
    removeCount, bool removeLabels)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbardataproxyprivate.html#removeRows

    Parameters
    ----------

    rowIndex : int
      Passed on as it is.

    removeCount : int
      Passed on as it is.

    removeLabels : bool
      Passed on as it is.
    """
    #  void QBarDataProxyPrivate::removeRows(int rowIndex, int removeCount,
    #      bool removeLabels)
    self.uglySide.call(
        'ritual_ZN20QBarDataProxyPrivate10removeRowsEiib',
        rowIndex, removeCount, removeLabels,
    )

  def qptr(self) -> Optional[QBarDataProxy]:
    """
    Calls Qt's 'QBarDataProxy *QBarDataProxyPrivate::qptr()'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxyprivate.html#qptr

    Returns
    -------

    Optional[QBarDataProxy]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBarDataProxy *QBarDataProxyPrivate::qptr()
    address = self.uglySide.call('ritual_ZN20QBarDataProxyPrivate4qptrEv')
    from . import QBarDataProxy
    return QBarDataProxy._cuteAt(address)

  @overload(int)
  def clearRow(self, rowIndex: int) -> None:
    """
    Calls Qt's 'void QBarDataProxyPrivate::clearRow(int rowIndex)'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxyprivate.html#clearRow

    Parameters
    ----------

    rowIndex : int
      Passed on as it is.
    """
    #  void QBarDataProxyPrivate::clearRow(int rowIndex)
    self.uglySide.call(
        'ritual_ZN20QBarDataProxyPrivate8clearRowEi', rowIndex,
    )

  def clearArray(self) -> None:
    """
    Calls Qt's 'void QBarDataProxyPrivate::clearArray()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbardataproxyprivate.html#clearArray
    """
    #  void QBarDataProxyPrivate::clearArray()
    self.uglySide.call('ritual_ZN20QBarDataProxyPrivate10clearArrayEv')

  @overload(int, int, QStringList, bool)
  def fixRowLabels(
      self,
      startIndex: int,
      count: int,
      newLabels: QStringList,
      isInsert: bool,
  ) -> None:
    """
    Calls Qt's 'void QBarDataProxyPrivate::fixRowLabels(int startIndex, int
    count, const QStringList &newLabels, bool isInsert)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbardataproxyprivate.html#fixRowLabels

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.

    newLabels : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    isInsert : bool
      Passed on as it is.
    """
    #  void QBarDataProxyPrivate::fixRowLabels(int startIndex, int count,
    #      const QStringList &newLabels, bool isInsert)
    self.uglySide.call(
        'ritual_ZN20QBarDataProxyPrivate12fixRowLabelsEiiRK5QListI7QStringE'
        'b',
        startIndex, count, self._valueOf(newLabels), isInsert,
    )

  @staticmethod
  def addRow(*__, **_) -> Never:
    """
    Qt's 'int QBarDataProxyPrivate::addRow(QBarDataRow *row, const QString
    *label)': names 'QBarDataRow', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QBarDataProxyPrivate.addRow' has no cute function yet. Qt's 'int "
        "QBarDataProxyPrivate::addRow(QBarDataRow *row, const QString "
        "*label)': names 'QBarDataRow', which has no cute class yet.")

  @staticmethod
  def addRows(*__, **_) -> Never:
    """
    Qt's 'int QBarDataProxyPrivate::addRows(const QBarDataArray &rows, const
    QStringList *labels)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QBarDataProxyPrivate.addRows' has no cute function yet. Qt's 'int "
        "QBarDataProxyPrivate::addRows(const QBarDataArray &rows, const "
        "QStringList *labels)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def insertRow(*__, **_) -> Never:
    """
    Qt's 'void QBarDataProxyPrivate::insertRow(int rowIndex, QBarDataRow
    *row, const QString *label)': names 'QBarDataRow', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QBarDataProxyPrivate.insertRow' has no cute function yet. Qt's "
        "'void QBarDataProxyPrivate::insertRow(int rowIndex, QBarDataRow "
        "*row, const QString *label)': names 'QBarDataRow', which has no "
        "cute class yet.")

  @staticmethod
  def insertRows(*__, **_) -> Never:
    """
    Qt's 'void QBarDataProxyPrivate::insertRows(int rowIndex, const
    QBarDataArray &rows, const QStringList *labels)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QBarDataProxyPrivate.insertRows' has no cute function yet. Qt's "
        "'void QBarDataProxyPrivate::insertRows(int rowIndex, const "
        "QBarDataArray &rows, const QStringList *labels)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def limitValues(*__, **_) -> Never:
    """
    Qt's 'QPair<GLfloat, GLfloat> QBarDataProxyPrivate::limitValues(int
    startRow, int startColumn, int rowCount, int columnCount) const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QBarDataProxyPrivate.limitValues' has no cute function yet. Qt's "
        "'QPair<GLfloat, GLfloat> QBarDataProxyPrivate::limitValues(int "
        "startRow, int startColumn, int rowCount, int columnCount) const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def resetArray(*__, **_) -> Never:
    """
    Qt's 'void QBarDataProxyPrivate::resetArray(QBarDataArray *newArray,
    const QStringList *rowLabels, const QStringList *columnLabels)': names
    'QBarDataArray', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QBarDataProxyPrivate.resetArray' has no cute function yet. Qt's "
        "'void QBarDataProxyPrivate::resetArray(QBarDataArray *newArray, "
        "const QStringList *rowLabels, const QStringList *columnLabels)': "
        "names 'QBarDataArray', which has no cute class yet.")

  @staticmethod
  def setRow(*__, **_) -> Never:
    """
    Qt's 'void QBarDataProxyPrivate::setRow(int rowIndex, QBarDataRow *row,
    const QString *label)': names 'QBarDataRow', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QBarDataProxyPrivate.setRow' has no cute function yet. Qt's 'void "
        "QBarDataProxyPrivate::setRow(int rowIndex, QBarDataRow *row, const "
        "QString *label)': names 'QBarDataRow', which has no cute class yet."
    )

  @staticmethod
  def setRows(*__, **_) -> Never:
    """
    Qt's 'void QBarDataProxyPrivate::setRows(int rowIndex, const
    QBarDataArray &rows, const QStringList *labels)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QBarDataProxyPrivate.setRows' has no cute function yet. Qt's "
        "'void QBarDataProxyPrivate::setRows(int rowIndex, const "
        "QBarDataArray &rows, const QStringList *labels)': takes a type "
        "Python has no way to hand over yet.")
