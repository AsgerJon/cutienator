"""
QTreeWidgetPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qtreewidget_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QTreeWidgetPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QTreeViewPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QTreeWidget


class QTreeWidgetPrivate(QTreeViewPrivate):
  """
  The cute side of Qt's QTreeWidgetPrivate: a plain Python object standing in
  front of one C++ QTreeWidgetPrivate.

  It is built on the cute 'QTreeViewPrivate', as Qt's QTreeWidgetPrivate is
  built on Qt's QTreeViewPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTreeWidgetPrivate that has a ritual and that Python
  can call so far, 2 names in all: 'q_func', 'clearConnections'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QTreeWidget *QTreeWidgetPrivate::q_func() const': takes in
    Python what 'QTreeWidget *QTreeWidgetPrivate::q_func()' takes.

  What has no ritual
  ------------------

  16 of the 19 functions Qt declares: 15 leans on 'QTreeModel; 1 leans on
  'QAbstractItemViewPrivate.

  What to expect
  --------------

  - The C++ QTreeWidgetPrivate is created at the first use, not by
    'QTreeWidgetPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTreeWidgetPrivate.
  - Each name of Qt's QTreeWidgetPrivate that has no cute function yet,
    '__init__', 'dataChanged', 'emitCurrentItemChanged', 'emitItemActivated',
    'emitItemChanged', 'emitItemClicked', 'emitItemCollapsed',
    'emitItemDoubleClicked', 'emitItemEntered', 'emitItemExpanded',
    'emitItemPressed', 'index', 'item', 'selectionChanged', 'sort',
    'treeModel', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTreeWidgetPrivate'

  #  A C++ QTreeWidgetPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTreeWidgetPrivate'

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
    Qt's 'QTreeWidgetPrivate::QTreeWidgetPrivate()': leans on
    'QAbstractItemViewPrivate::columnsAboutToBeRemoved(QModelIndex const&,
    int, int)', which Qt's source does not mark for use from outside Qt and
    has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QTreeWidgetPrivate.__init__' has no cute function yet. Qt's "
        "'QTreeWidgetPrivate::QTreeWidgetPrivate()': leans on "
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

  def q_func(self) -> Optional[QTreeWidget]:
    """
    Calls Qt's 'QTreeWidget *QTreeWidgetPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetprivate.html#q_func

    Returns
    -------

    Optional[QTreeWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTreeWidget *QTreeWidgetPrivate::q_func()
    address = self.uglySide.call('ritual_ZN18QTreeWidgetPrivate6q_funcEv')
    from . import QTreeWidget
    return QTreeWidget._cuteAt(address)

  def clearConnections(self) -> None:
    """
    Calls Qt's 'void QTreeWidgetPrivate::clearConnections()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidgetprivate.html#clearConnections
    """
    #  void QTreeWidgetPrivate::clearConnections()
    self.uglySide.call('ritual_ZN18QTreeWidgetPrivate16clearConnectionsEv')

  @staticmethod
  def dataChanged(*__, **_) -> Never:
    """
    Qt's 'void QTreeWidgetPrivate::dataChanged(const QModelIndex &topLeft,
    const QModelIndex &bottomRight)': leans on
    'QTreeModel::staticMetaObject', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QTreeWidgetPrivate.dataChanged' has no cute function yet. Qt's "
        "'void QTreeWidgetPrivate::dataChanged(const QModelIndex &topLeft, "
        "const QModelIndex &bottomRight)': leans on "
        "'QTreeModel::staticMetaObject', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def emitCurrentItemChanged(*__, **_) -> Never:
    """
    Qt's 'void QTreeWidgetPrivate::emitCurrentItemChanged(const QModelIndex
    &previous, const QModelIndex &index)': leans on
    'QTreeModel::staticMetaObject', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QTreeWidgetPrivate.emitCurrentItemChanged' has no cute function "
        "yet. Qt's 'void QTreeWidgetPrivate::emitCurrentItemChanged(const "
        "QModelIndex &previous, const QModelIndex &index)': leans on "
        "'QTreeModel::staticMetaObject', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def emitItemActivated(*__, **_) -> Never:
    """
    Qt's 'void QTreeWidgetPrivate::emitItemActivated(const QModelIndex
    &index)': leans on 'QTreeModel::staticMetaObject', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QTreeWidgetPrivate.emitItemActivated' has no cute function yet. "
        "Qt's 'void QTreeWidgetPrivate::emitItemActivated(const QModelIndex "
        "&index)': leans on 'QTreeModel::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def emitItemChanged(*__, **_) -> Never:
    """
    Qt's 'void QTreeWidgetPrivate::emitItemChanged(const QModelIndex
    &index)': leans on 'QTreeModel::staticMetaObject', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QTreeWidgetPrivate.emitItemChanged' has no cute function yet. "
        "Qt's 'void QTreeWidgetPrivate::emitItemChanged(const QModelIndex "
        "&index)': leans on 'QTreeModel::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def emitItemClicked(*__, **_) -> Never:
    """
    Qt's 'void QTreeWidgetPrivate::emitItemClicked(const QModelIndex
    &index)': leans on 'QTreeModel::staticMetaObject', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QTreeWidgetPrivate.emitItemClicked' has no cute function yet. "
        "Qt's 'void QTreeWidgetPrivate::emitItemClicked(const QModelIndex "
        "&index)': leans on 'QTreeModel::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def emitItemCollapsed(*__, **_) -> Never:
    """
    Qt's 'void QTreeWidgetPrivate::emitItemCollapsed(const QModelIndex
    &index)': leans on 'QTreeModel::staticMetaObject', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QTreeWidgetPrivate.emitItemCollapsed' has no cute function yet. "
        "Qt's 'void QTreeWidgetPrivate::emitItemCollapsed(const QModelIndex "
        "&index)': leans on 'QTreeModel::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def emitItemDoubleClicked(*__, **_) -> Never:
    """
    Qt's 'void QTreeWidgetPrivate::emitItemDoubleClicked(const QModelIndex
    &index)': leans on 'QTreeModel::staticMetaObject', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QTreeWidgetPrivate.emitItemDoubleClicked' has no cute function "
        "yet. Qt's 'void QTreeWidgetPrivate::emitItemDoubleClicked(const "
        "QModelIndex &index)': leans on 'QTreeModel::staticMetaObject', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def emitItemEntered(*__, **_) -> Never:
    """
    Qt's 'void QTreeWidgetPrivate::emitItemEntered(const QModelIndex
    &index)': leans on 'QTreeModel::staticMetaObject', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QTreeWidgetPrivate.emitItemEntered' has no cute function yet. "
        "Qt's 'void QTreeWidgetPrivate::emitItemEntered(const QModelIndex "
        "&index)': leans on 'QTreeModel::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def emitItemExpanded(*__, **_) -> Never:
    """
    Qt's 'void QTreeWidgetPrivate::emitItemExpanded(const QModelIndex
    &index)': leans on 'QTreeModel::staticMetaObject', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QTreeWidgetPrivate.emitItemExpanded' has no cute function yet. "
        "Qt's 'void QTreeWidgetPrivate::emitItemExpanded(const QModelIndex "
        "&index)': leans on 'QTreeModel::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def emitItemPressed(*__, **_) -> Never:
    """
    Qt's 'void QTreeWidgetPrivate::emitItemPressed(const QModelIndex
    &index)': leans on 'QTreeModel::staticMetaObject', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QTreeWidgetPrivate.emitItemPressed' has no cute function yet. "
        "Qt's 'void QTreeWidgetPrivate::emitItemPressed(const QModelIndex "
        "&index)': leans on 'QTreeModel::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def index(*__, **_) -> Never:
    """
    Qt's 'QModelIndex QTreeWidgetPrivate::index(const QTreeWidgetItem *item,
    int column) const': leans on 'QTreeModel::staticMetaObject', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QTreeWidgetPrivate.index' has no cute function yet. Qt's "
        "'QModelIndex QTreeWidgetPrivate::index(const QTreeWidgetItem "
        "*item, int column) const': leans on "
        "'QTreeModel::staticMetaObject', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def item(*__, **_) -> Never:
    """
    Qt's 'QTreeWidgetItem *QTreeWidgetPrivate::item(const QModelIndex &index)
    const': leans on 'QTreeModel::staticMetaObject', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QTreeWidgetPrivate.item' has no cute function yet. Qt's "
        "'QTreeWidgetItem *QTreeWidgetPrivate::item(const QModelIndex "
        "&index) const': leans on 'QTreeModel::staticMetaObject', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def selectionChanged(*__, **_) -> Never:
    """
    Qt's 'void QTreeWidgetPrivate::selectionChanged(const QItemSelection
    &selected, const QItemSelection &deselected)': leans on
    'QTreeModel::staticMetaObject', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QTreeWidgetPrivate.selectionChanged' has no cute function yet. "
        "Qt's 'void QTreeWidgetPrivate::selectionChanged(const "
        "QItemSelection &selected, const QItemSelection &deselected)': "
        "leans on 'QTreeModel::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def sort(*__, **_) -> Never:
    """
    Qt's 'void QTreeWidgetPrivate::sort()': leans on
    'QTreeModel::staticMetaObject', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QTreeWidgetPrivate.sort' has no cute function yet. Qt's 'void "
        "QTreeWidgetPrivate::sort()': leans on "
        "'QTreeModel::staticMetaObject', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def treeModel(*__, **_) -> Never:
    """
    Qt's 'QTreeModel *QTreeWidgetPrivate::treeModel() const': leans on
    'QTreeModel::staticMetaObject', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QTreeWidgetPrivate.treeModel' has no cute function yet. Qt's "
        "'QTreeModel *QTreeWidgetPrivate::treeModel() const': leans on "
        "'QTreeModel::staticMetaObject', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")
