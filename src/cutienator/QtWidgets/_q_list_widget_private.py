"""
QListWidgetPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qlistwidget_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QListWidgetPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QListViewPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QListWidget


class QListWidgetPrivate(QListViewPrivate):
  """
  The cute side of Qt's QListWidgetPrivate: a plain Python object standing in
  front of one C++ QListWidgetPrivate.

  It is built on the cute 'QListViewPrivate', as Qt's QListWidgetPrivate is
  built on Qt's QListViewPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QListWidgetPrivate that has a ritual and that Python
  can call so far, 3 names in all: 'q_func', 'clearConnections', 'sort'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QListWidget *QListWidgetPrivate::q_func() const': takes in
    Python what 'QListWidget *QListWidgetPrivate::q_func()' takes.

  What has no ritual
  ------------------

  11 of the 15 functions Qt declares: 10 leans on 'QListModel; 1 leans on
  'QAbstractItemViewPrivate.

  What to expect
  --------------

  - The C++ QListWidgetPrivate is created at the first use, not by
    'QListWidgetPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QListWidgetPrivate.
  - Each name of Qt's QListWidgetPrivate that has no cute function yet,
    '__init__', 'dataChanged', 'emitCurrentItemChanged', 'emitItemActivated',
    'emitItemChanged', 'emitItemClicked', 'emitItemDoubleClicked',
    'emitItemEntered', 'emitItemPressed', 'listModel', 'setup', holds a
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
  __qt_class__ = 'QListWidgetPrivate'

  #  A C++ QListWidgetPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QListWidgetPrivate'

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
    Qt's 'QListWidgetPrivate::QListWidgetPrivate()': leans on
    'QAbstractItemViewPrivate::columnsAboutToBeRemoved(QModelIndex const&,
    int, int)', which Qt's source does not mark for use from outside Qt and
    has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QListWidgetPrivate.__init__' has no cute function yet. Qt's "
        "'QListWidgetPrivate::QListWidgetPrivate()': leans on "
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

  def q_func(self) -> Optional[QListWidget]:
    """
    Calls Qt's 'QListWidget *QListWidgetPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidgetprivate.html#q_func

    Returns
    -------

    Optional[QListWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QListWidget *QListWidgetPrivate::q_func()
    address = self.uglySide.call('ritual_ZN18QListWidgetPrivate6q_funcEv')
    from . import QListWidget
    return QListWidget._cuteAt(address)

  def clearConnections(self) -> None:
    """
    Calls Qt's 'void QListWidgetPrivate::clearConnections()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistwidgetprivate.html#clearConnections
    """
    #  void QListWidgetPrivate::clearConnections()
    self.uglySide.call('ritual_ZN18QListWidgetPrivate16clearConnectionsEv')

  def sort(self) -> None:
    """
    Calls Qt's 'void QListWidgetPrivate::sort()'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidgetprivate.html#sort
    """
    #  void QListWidgetPrivate::sort()
    self.uglySide.call('ritual_ZN18QListWidgetPrivate4sortEv')

  @staticmethod
  def dataChanged(*__, **_) -> Never:
    """
    Qt's 'void QListWidgetPrivate::dataChanged(const QModelIndex &topLeft,
    const QModelIndex &bottomRight)': leans on
    'QListModel::staticMetaObject', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QListWidgetPrivate.dataChanged' has no cute function yet. Qt's "
        "'void QListWidgetPrivate::dataChanged(const QModelIndex &topLeft, "
        "const QModelIndex &bottomRight)': leans on "
        "'QListModel::staticMetaObject', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def emitCurrentItemChanged(*__, **_) -> Never:
    """
    Qt's 'void QListWidgetPrivate::emitCurrentItemChanged(const QModelIndex
    &current, const QModelIndex &previous)': leans on
    'QListModel::staticMetaObject', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QListWidgetPrivate.emitCurrentItemChanged' has no cute function "
        "yet. Qt's 'void QListWidgetPrivate::emitCurrentItemChanged(const "
        "QModelIndex &current, const QModelIndex &previous)': leans on "
        "'QListModel::staticMetaObject', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def emitItemActivated(*__, **_) -> Never:
    """
    Qt's 'void QListWidgetPrivate::emitItemActivated(const QModelIndex
    &index)': leans on 'QListModel::staticMetaObject', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QListWidgetPrivate.emitItemActivated' has no cute function yet. "
        "Qt's 'void QListWidgetPrivate::emitItemActivated(const QModelIndex "
        "&index)': leans on 'QListModel::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def emitItemChanged(*__, **_) -> Never:
    """
    Qt's 'void QListWidgetPrivate::emitItemChanged(const QModelIndex
    &index)': leans on 'QListModel::staticMetaObject', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QListWidgetPrivate.emitItemChanged' has no cute function yet. "
        "Qt's 'void QListWidgetPrivate::emitItemChanged(const QModelIndex "
        "&index)': leans on 'QListModel::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def emitItemClicked(*__, **_) -> Never:
    """
    Qt's 'void QListWidgetPrivate::emitItemClicked(const QModelIndex
    &index)': leans on 'QListModel::staticMetaObject', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QListWidgetPrivate.emitItemClicked' has no cute function yet. "
        "Qt's 'void QListWidgetPrivate::emitItemClicked(const QModelIndex "
        "&index)': leans on 'QListModel::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def emitItemDoubleClicked(*__, **_) -> Never:
    """
    Qt's 'void QListWidgetPrivate::emitItemDoubleClicked(const QModelIndex
    &index)': leans on 'QListModel::staticMetaObject', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QListWidgetPrivate.emitItemDoubleClicked' has no cute function "
        "yet. Qt's 'void QListWidgetPrivate::emitItemDoubleClicked(const "
        "QModelIndex &index)': leans on 'QListModel::staticMetaObject', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def emitItemEntered(*__, **_) -> Never:
    """
    Qt's 'void QListWidgetPrivate::emitItemEntered(const QModelIndex
    &index)': leans on 'QListModel::staticMetaObject', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QListWidgetPrivate.emitItemEntered' has no cute function yet. "
        "Qt's 'void QListWidgetPrivate::emitItemEntered(const QModelIndex "
        "&index)': leans on 'QListModel::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def emitItemPressed(*__, **_) -> Never:
    """
    Qt's 'void QListWidgetPrivate::emitItemPressed(const QModelIndex
    &index)': leans on 'QListModel::staticMetaObject', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QListWidgetPrivate.emitItemPressed' has no cute function yet. "
        "Qt's 'void QListWidgetPrivate::emitItemPressed(const QModelIndex "
        "&index)': leans on 'QListModel::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def listModel(*__, **_) -> Never:
    """
    Qt's 'QListModel *QListWidgetPrivate::listModel() const': leans on
    'QListModel::staticMetaObject', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QListWidgetPrivate.listModel' has no cute function yet. Qt's "
        "'QListModel *QListWidgetPrivate::listModel() const': leans on "
        "'QListModel::staticMetaObject', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def setup(*__, **_) -> Never:
    """
    Qt's 'void QListWidgetPrivate::setup()': leans on
    'QListModel::staticMetaObject', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QListWidgetPrivate.setup' has no cute function yet. Qt's 'void "
        "QListWidgetPrivate::setup()': leans on "
        "'QListModel::staticMetaObject', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")
