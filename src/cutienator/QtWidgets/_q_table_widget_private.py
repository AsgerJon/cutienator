"""
QTableWidgetPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qtablewidget_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QTableWidgetPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QTableViewPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QTableWidget


class QTableWidgetPrivate(QTableViewPrivate):
  """
  The cute side of Qt's QTableWidgetPrivate: a plain Python object standing
  in front of one C++ QTableWidgetPrivate.

  It is built on the cute 'QTableViewPrivate', as Qt's QTableWidgetPrivate is
  built on Qt's QTableViewPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTableWidgetPrivate that has a ritual and that
  Python can call so far, 3 names in all: 'q_func', 'clearConnections',
  'sort'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QTableWidget *QTableWidgetPrivate::q_func() const': takes in
    Python what 'QTableWidget *QTableWidgetPrivate::q_func()' takes.

  What has no ritual
  ------------------

  11 of the 15 functions Qt declares: 10 leans on 'QTableModel; 1 leans on
  'QAbstractItemViewPrivate.

  What to expect
  --------------

  - The C++ QTableWidgetPrivate is created at the first use, not by
    'QTableWidgetPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTableWidgetPrivate.
  - Each name of Qt's QTableWidgetPrivate that has no cute function yet,
    '__init__', 'dataChanged', 'emitCurrentItemChanged', 'emitItemActivated',
    'emitItemChanged', 'emitItemClicked', 'emitItemDoubleClicked',
    'emitItemEntered', 'emitItemPressed', 'setup', 'tableModel', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTableWidgetPrivate'

  #  A C++ QTableWidgetPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTableWidgetPrivate'

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
    Qt's 'QTableWidgetPrivate::QTableWidgetPrivate()': leans on
    'QAbstractItemViewPrivate::columnsAboutToBeRemoved(QModelIndex const&,
    int, int)', which Qt's source does not mark for use from outside Qt and
    has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QTableWidgetPrivate.__init__' has no cute function yet. Qt's "
        "'QTableWidgetPrivate::QTableWidgetPrivate()': leans on "
        "'QAbstractItemViewPrivate::columnsAboutToBeRemoved(QModelIndex "
        "const&, int, int)', which Qt's source does not mark for use from "
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

  def q_func(self) -> Optional[QTableWidget]:
    """
    Calls Qt's 'QTableWidget *QTableWidgetPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidgetprivate.html#q_func

    Returns
    -------

    Optional[QTableWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTableWidget *QTableWidgetPrivate::q_func()
    address = self.uglySide.call('ritual_ZN19QTableWidgetPrivate6q_funcEv')
    from . import QTableWidget
    return QTableWidget._cuteAt(address)

  def clearConnections(self) -> None:
    """
    Calls Qt's 'void QTableWidgetPrivate::clearConnections()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtablewidgetprivate.html#clearConnections
    """
    #  void QTableWidgetPrivate::clearConnections()
    self.uglySide.call('ritual_ZN19QTableWidgetPrivate16clearConnectionsEv')

  def sort(self) -> None:
    """
    Calls Qt's 'void QTableWidgetPrivate::sort()'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidgetprivate.html#sort
    """
    #  void QTableWidgetPrivate::sort()
    self.uglySide.call('ritual_ZN19QTableWidgetPrivate4sortEv')

  @staticmethod
  def dataChanged(*__, **_) -> Never:
    """
    Qt's 'void QTableWidgetPrivate::dataChanged(const QModelIndex &topLeft,
    const QModelIndex &bottomRight)': leans on
    'QTableModel::staticMetaObject', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QTableWidgetPrivate.dataChanged' has no cute function yet. Qt's "
        "'void QTableWidgetPrivate::dataChanged(const QModelIndex &topLeft, "
        "const QModelIndex &bottomRight)': leans on "
        "'QTableModel::staticMetaObject', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def emitCurrentItemChanged(*__, **_) -> Never:
    """
    Qt's 'void QTableWidgetPrivate::emitCurrentItemChanged(const QModelIndex
    &previous, const QModelIndex &current)': leans on
    'QTableModel::staticMetaObject', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QTableWidgetPrivate.emitCurrentItemChanged' has no cute function "
        "yet. Qt's 'void QTableWidgetPrivate::emitCurrentItemChanged(const "
        "QModelIndex &previous, const QModelIndex &current)': leans on "
        "'QTableModel::staticMetaObject', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def emitItemActivated(*__, **_) -> Never:
    """
    Qt's 'void QTableWidgetPrivate::emitItemActivated(const QModelIndex
    &index)': leans on 'QTableModel::staticMetaObject', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QTableWidgetPrivate.emitItemActivated' has no cute function yet. "
        "Qt's 'void QTableWidgetPrivate::emitItemActivated(const "
        "QModelIndex &index)': leans on 'QTableModel::staticMetaObject', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def emitItemChanged(*__, **_) -> Never:
    """
    Qt's 'void QTableWidgetPrivate::emitItemChanged(const QModelIndex
    &index)': leans on 'QTableModel::staticMetaObject', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QTableWidgetPrivate.emitItemChanged' has no cute function yet. "
        "Qt's 'void QTableWidgetPrivate::emitItemChanged(const QModelIndex "
        "&index)': leans on 'QTableModel::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def emitItemClicked(*__, **_) -> Never:
    """
    Qt's 'void QTableWidgetPrivate::emitItemClicked(const QModelIndex
    &index)': leans on 'QTableModel::staticMetaObject', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QTableWidgetPrivate.emitItemClicked' has no cute function yet. "
        "Qt's 'void QTableWidgetPrivate::emitItemClicked(const QModelIndex "
        "&index)': leans on 'QTableModel::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def emitItemDoubleClicked(*__, **_) -> Never:
    """
    Qt's 'void QTableWidgetPrivate::emitItemDoubleClicked(const QModelIndex
    &index)': leans on 'QTableModel::staticMetaObject', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QTableWidgetPrivate.emitItemDoubleClicked' has no cute function "
        "yet. Qt's 'void QTableWidgetPrivate::emitItemDoubleClicked(const "
        "QModelIndex &index)': leans on 'QTableModel::staticMetaObject', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def emitItemEntered(*__, **_) -> Never:
    """
    Qt's 'void QTableWidgetPrivate::emitItemEntered(const QModelIndex
    &index)': leans on 'QTableModel::staticMetaObject', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QTableWidgetPrivate.emitItemEntered' has no cute function yet. "
        "Qt's 'void QTableWidgetPrivate::emitItemEntered(const QModelIndex "
        "&index)': leans on 'QTableModel::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def emitItemPressed(*__, **_) -> Never:
    """
    Qt's 'void QTableWidgetPrivate::emitItemPressed(const QModelIndex
    &index)': leans on 'QTableModel::staticMetaObject', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QTableWidgetPrivate.emitItemPressed' has no cute function yet. "
        "Qt's 'void QTableWidgetPrivate::emitItemPressed(const QModelIndex "
        "&index)': leans on 'QTableModel::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setup(*__, **_) -> Never:
    """
    Qt's 'void QTableWidgetPrivate::setup()': leans on
    'QTableModel::staticMetaObject', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QTableWidgetPrivate.setup' has no cute function yet. Qt's 'void "
        "QTableWidgetPrivate::setup()': leans on "
        "'QTableModel::staticMetaObject', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def tableModel(*__, **_) -> Never:
    """
    Qt's 'QTableModel *QTableWidgetPrivate::tableModel() const': leans on
    'QTableModel::staticMetaObject', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QTableWidgetPrivate.tableModel' has no cute function yet. Qt's "
        "'QTableModel *QTableWidgetPrivate::tableModel() const': leans on "
        "'QTableModel::staticMetaObject', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")
