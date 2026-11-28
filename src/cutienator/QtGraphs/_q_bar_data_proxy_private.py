"""
QBarDataProxyPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/qbardataproxy_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QBarDataProxyPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QAbstractDataProxyPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QAbstract3DSeries, QBarDataProxy
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstract3DSeries = WAIT['QtGraphs:QAbstract3DSeries']

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
  Python can call so far, 3 names in all: 'q_func', 'removeRows',
  'setSeries'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QBarDataProxy *QBarDataProxyPrivate::q_func() const': takes
    in Python what 'QBarDataProxy *QBarDataProxyPrivate::q_func()' takes.
  - Qt's 'QBarDataProxyPrivate::~QBarDataProxyPrivate()': the destructor:
    Python never removes a C++ QBarDataProxyPrivate.
  - Qt's 'void QBarDataProxyPrivate::resetArray(QBarDataArray &&newArray,
    QStringList &&rowLabels, QStringList &&columnLabels)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void QBarDataProxyPrivate::setRow(qsizetype rowIndex, QBarDataRow
    &&row, QString &&label)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QBarDataProxyPrivate::setRows(qsizetype rowIndex,
    QBarDataArray &&rows, QStringList &&labels)': takes a type Python has no
    way to hand over yet.
  - Qt's 'void QBarDataProxyPrivate::setItem(qsizetype rowIndex, qsizetype
    columnIndex, QBarDataItem &&item)': takes a type Python has no way to
    hand over yet.
  - Qt's 'qsizetype QBarDataProxyPrivate::addRow(QBarDataRow &&row, QString
    &&label)': takes a type Python has no way to hand over yet.
  - Qt's 'qsizetype QBarDataProxyPrivate::addRows(QBarDataArray &&rows,
    QStringList &&labels)': takes a type Python has no way to hand over yet.
  - Qt's 'void QBarDataProxyPrivate::insertRow(qsizetype rowIndex,
    QBarDataRow &&row, QString &&label)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QBarDataProxyPrivate::insertRows(qsizetype rowIndex,
    QBarDataArray &&rows, QStringList &&labels)': takes a type Python has no
    way to hand over yet.
  - Qt's 'QPair<float, float> QBarDataProxyPrivate::limitValues(qsizetype
    startRow, qsizetype startColumn, qsizetype rowCount, qsizetype
    columnCount) const': gives a type Python has no way to take yet.

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
  - Each name of Qt's QBarDataProxyPrivate that has no cute function yet,
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
  __qt_class__ = 'QBarDataProxyPrivate'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QBarDataProxyPrivate::QBarDataProxyPrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbardataproxyprivate.html#QBarDataProxyPrivate
    """
    #  QBarDataProxyPrivate::QBarDataProxyPrivate()
    self._noteCreation(QBarDataProxyPrivate, lambda: Rituals.call(
        'ritual_ZN20QBarDataProxyPrivateC1Ev',
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

  def q_func(self) -> Optional[QBarDataProxy]:
    """
    Calls Qt's 'QBarDataProxy *QBarDataProxyPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataproxyprivate.html#q_func

    Returns
    -------

    Optional[QBarDataProxy]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBarDataProxy *QBarDataProxyPrivate::q_func()
    address = self.uglySide.call('ritual_ZN20QBarDataProxyPrivate6q_funcEv')
    from . import QBarDataProxy
    return QBarDataProxy._cuteAt(address)

  @overload(int, int, bool)
  def removeRows(
      self,
      rowIndex: int,
      removeCount: int,
      removeLabels: bool,
  ) -> None:
    """
    Calls Qt's 'void QBarDataProxyPrivate::removeRows(qsizetype rowIndex,
    qsizetype removeCount, bool removeLabels)'.

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
    #  void QBarDataProxyPrivate::removeRows(qsizetype rowIndex, qsizetype
    #      removeCount, bool removeLabels)
    self.uglySide.call(
        'ritual_ZN20QBarDataProxyPrivate10removeRowsExxb',
        rowIndex, removeCount, removeLabels,
    )

  @staticmethod
  def addRow(*__, **_) -> Never:
    """
    Qt's 'qsizetype QBarDataProxyPrivate::addRow(QBarDataRow &&row, QString
    &&label)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QBarDataProxyPrivate.addRow' has no cute function yet. Qt's "
        "'qsizetype QBarDataProxyPrivate::addRow(QBarDataRow &&row, QString "
        "&&label)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def addRows(*__, **_) -> Never:
    """
    Qt's 'qsizetype QBarDataProxyPrivate::addRows(QBarDataArray &&rows,
    QStringList &&labels)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QBarDataProxyPrivate.addRows' has no cute function yet. Qt's "
        "'qsizetype QBarDataProxyPrivate::addRows(QBarDataArray &&rows, "
        "QStringList &&labels)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def insertRow(*__, **_) -> Never:
    """
    Qt's 'void QBarDataProxyPrivate::insertRow(qsizetype rowIndex,
    QBarDataRow &&row, QString &&label)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QBarDataProxyPrivate.insertRow' has no cute function yet. Qt's "
        "'void QBarDataProxyPrivate::insertRow(qsizetype rowIndex, "
        "QBarDataRow &&row, QString &&label)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def insertRows(*__, **_) -> Never:
    """
    Qt's 'void QBarDataProxyPrivate::insertRows(qsizetype rowIndex,
    QBarDataArray &&rows, QStringList &&labels)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QBarDataProxyPrivate.insertRows' has no cute function yet. Qt's "
        "'void QBarDataProxyPrivate::insertRows(qsizetype rowIndex, "
        "QBarDataArray &&rows, QStringList &&labels)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def limitValues(*__, **_) -> Never:
    """
    Qt's 'QPair<float, float> QBarDataProxyPrivate::limitValues(qsizetype
    startRow, qsizetype startColumn, qsizetype rowCount, qsizetype
    columnCount) const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QBarDataProxyPrivate.limitValues' has no cute function yet. Qt's "
        "'QPair<float, float> QBarDataProxyPrivate::limitValues(qsizetype "
        "startRow, qsizetype startColumn, qsizetype rowCount, qsizetype "
        "columnCount) const': gives a type Python has no way to take yet.")

  @staticmethod
  def resetArray(*__, **_) -> Never:
    """
    Qt's 'void QBarDataProxyPrivate::resetArray(QBarDataArray &&newArray,
    QStringList &&rowLabels, QStringList &&columnLabels)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QBarDataProxyPrivate.resetArray' has no cute function yet. Qt's "
        "'void QBarDataProxyPrivate::resetArray(QBarDataArray &&newArray, "
        "QStringList &&rowLabels, QStringList &&columnLabels)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def setItem(*__, **_) -> Never:
    """
    Qt's 'void QBarDataProxyPrivate::setItem(qsizetype rowIndex, qsizetype
    columnIndex, QBarDataItem &&item)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QBarDataProxyPrivate.setItem' has no cute function yet. Qt's "
        "'void QBarDataProxyPrivate::setItem(qsizetype rowIndex, qsizetype "
        "columnIndex, QBarDataItem &&item)': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def setRow(*__, **_) -> Never:
    """
    Qt's 'void QBarDataProxyPrivate::setRow(qsizetype rowIndex, QBarDataRow
    &&row, QString &&label)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QBarDataProxyPrivate.setRow' has no cute function yet. Qt's 'void "
        "QBarDataProxyPrivate::setRow(qsizetype rowIndex, QBarDataRow "
        "&&row, QString &&label)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def setRows(*__, **_) -> Never:
    """
    Qt's 'void QBarDataProxyPrivate::setRows(qsizetype rowIndex,
    QBarDataArray &&rows, QStringList &&labels)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QBarDataProxyPrivate.setRows' has no cute function yet. Qt's "
        "'void QBarDataProxyPrivate::setRows(qsizetype rowIndex, "
        "QBarDataArray &&rows, QStringList &&labels)': takes a type Python "
        "has no way to hand over yet.")
