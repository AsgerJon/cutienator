"""
QAbstractListModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qabstractitemmodel.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import Qt, QAbstractItemModel

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QMetaObject, QMimeData, QModelIndex
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMimeData = WAIT['QMimeData']
  QModelIndex = WAIT['QModelIndex']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractListModel(QAbstractItemModel):
  """
  The cute side of Qt's QAbstractListModel: a plain Python object standing in
  front of one C++ QAbstractListModel.

  It is built on the cute 'QAbstractItemModel', as Qt's QAbstractListModel is
  built on Qt's QAbstractItemModel, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractListModel that has a ritual and that Python
  can call so far, 9 names in all: 'metaObject', 'tr', 'index', 'sibling',
  'dropMimeData', 'flags', 'parent', 'columnCount', 'hasChildren'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAbstractListModel::~QAbstractListModel()': the destructor: Python
    never removes a C++ QAbstractListModel.

  What has no ritual
  ------------------

  10 of the 20 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet; 2 the class is abstract, so C++ cannot make one; 2 forbidden; 1
  a template; 1 declared and nowhere to be found.

  What to expect
  --------------

  - The C++ QAbstractListModel is created at the first use, not by
    'QAbstractListModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractListModel.
  - Qt tells when it has removed the C++ QAbstractListModel. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QAbstractListModel::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractlistmodel.html#tr

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
    #  QString QAbstractListModel::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QAbstractListModel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractListModel'

  #  A C++ QAbstractListModel Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractListModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAbstractListModel::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractlistmodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstractListModel::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QAbstractListModel10metaObjectEv',
    )
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(int)
  @overload(int, int)
  @overload(int, int, QModelIndex)
  def index(
      self,
      row: int,
      column: int = 0,
      parent: Optional[QModelIndex] = None,
  ) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QAbstractListModel::index(int row, int column,
    const QModelIndex &parent) const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractlistmodel.html#index

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QAbstractListModel::index(int row, int column, const
    #      QModelIndex &parent) const
    if parent is None:
      from . import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK18QAbstractListModel5indexEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QAbstractListModel5indexEiiRK11QModelIndex'
    address = self.uglySide.call(ritual, row, column, self._valueOf(parent))
    from . import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(int, int, QModelIndex)
  def sibling(self, row: int, column: int, idx: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QAbstractListModel::sibling(int row, int column,
    const QModelIndex &idx) const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractlistmodel.html#sibling

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    idx : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QAbstractListModel::sibling(int row, int column, const
    #      QModelIndex &idx) const
    ritual = 'ritual_ZNK18QAbstractListModel7siblingEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QAbstractListModel7siblingEiiRK11QModelIndex'
    address = self.uglySide.call(ritual, row, column, self._valueOf(idx))
    from . import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  def flags(self, index: QModelIndex) -> Qt.ItemFlags:
    """
    Calls Qt's 'Qt::ItemFlags QAbstractListModel::flags(const QModelIndex
    &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractlistmodel.html#flags

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    Qt.ItemFlags
      The value standing for the combination Qt gave back.
    """
    #  Qt::ItemFlags QAbstractListModel::flags(const QModelIndex &index)
    #      const
    ritual = 'ritual_ZNK18QAbstractListModel5flagsERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QAbstractListModel5flagsERK11QModelIndex'
    return Qt.ItemFlags(self.uglySide.call(ritual, self._valueOf(index)))

  @overload(QModelIndex)
  def parent(self, child: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QAbstractListModel::parent(const QModelIndex
    &child) const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractlistmodel.html#parent

    Parameters
    ----------

    child : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QAbstractListModel::parent(const QModelIndex &child) const
    ritual = 'ritual_ZNK18QAbstractListModel6parentERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QAbstractListModel6parentERK11QModelIndex'
    address = self.uglySide.call(ritual, self._valueOf(child))
    from . import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  def columnCount(self, parent: QModelIndex) -> int:
    """
    Calls Qt's 'int QAbstractListModel::columnCount(const QModelIndex
    &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractlistmodel.html#columnCount

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  int QAbstractListModel::columnCount(const QModelIndex &parent) const
    ritual = 'ritual_ZNK18QAbstractListModel11columnCountERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18QAbstractListModel11columnCountERK11QModelIndex')
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload(QModelIndex)
  def hasChildren(self, parent: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QAbstractListModel::hasChildren(const QModelIndex
    &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractlistmodel.html#hasChildren

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QAbstractListModel::hasChildren(const QModelIndex &parent) const
    ritual = 'ritual_ZNK18QAbstractListModel11hasChildrenERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18QAbstractListModel11hasChildrenERK11QModelIndex')
    return self.uglySide.call(ritual, self._valueOf(parent))

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

  @overload(QMimeData, Qt.DropAction, int, int, QModelIndex)
  @overload(NoneType, Qt.DropAction, int, int, QModelIndex)
  def dropMimeData(
      self,
      data: Optional[QMimeData],
      action: Qt.DropAction,
      row: int,
      column: int,
      parent: QModelIndex,
  ) -> bool:
    """
    Calls Qt's 'bool QAbstractListModel::dropMimeData(const QMimeData *data,
    Qt::DropAction action, int row, int column, const QModelIndex &parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractlistmodel.html#dropMimeData

    Parameters
    ----------

    data : Optional[QMimeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    action : Qt.DropAction
      Passed on as its number.

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QAbstractListModel::dropMimeData(const QMimeData *data,
    #      Qt::DropAction action, int row, int column, const QModelIndex
    #      &parent)
    ritual = (
        'ritual_ZN18QAbstractListModel12dropMimeDataEPK9QMimeDataN2Qt10Drop'
        'ActionEiiRK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QAbstractListModel12dropMimeDataEPK9QMimeDataN2Qt'
          '10DropActionEiiRK11QModelIndex')
    return self.uglySide.call(
        ritual,
        self._addressOf(data), action.value, row, column,
        self._valueOf(parent),
    )
