"""
QAbstractItemModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qabstractitemmodel.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ._qt import Qt
from ._q_meta_object import QMetaObject
from ._q_mime_data import QMimeData
from ._q_model_index import QModelIndex
from ._q_object import QObject
from ._q_size import QSize
from ._q_variant import QVariant
from ._q_abstract_item_model_check_index_option import CheckIndexOption
from ._q_abstract_item_model_layout_change_hint import LayoutChangeHint

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractItemModel(QObject):
  """
  The cute side of Qt's QAbstractItemModel: a plain Python object standing in
  front of one C++ QAbstractItemModel.

  It is built on the cute 'QObject', as Qt's QAbstractItemModel is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractItemModel that has a ritual and that Python
  can call so far, 39 names in all: 'metaObject', 'tr', 'hasIndex', 'index',
  'parent', 'sibling', 'rowCount', 'columnCount', 'hasChildren', 'data',
  'setData', 'headerData', 'setHeaderData', 'clearItemData',
  'canDropMimeData', 'dropMimeData', 'supportedDropActions',
  'supportedDragActions', 'insertRows', 'insertColumns', 'removeRows',
  'removeColumns', 'moveRows', 'moveColumns', 'insertRow', 'insertColumn',
  'removeRow', 'removeColumn', 'moveRow', 'moveColumn', 'fetchMore',
  'canFetchMore', 'flags', 'sort', 'buddy', 'span', 'checkIndex', 'submit',
  'revert'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAbstractItemModel::~QAbstractItemModel()': the destructor: Python
    never removes a C++ QAbstractItemModel.
  - Qt's 'void QAbstractItemModel::multiData(const QModelIndex &index,
    QModelRoleDataSpan roleDataSpan) const': names 'QModelRoleDataSpan',
    which has no cute class yet.

  What has no ritual
  ------------------

  59 of the 100 functions Qt declares: 25 protected; 18 a signal; 8 takes or
  gives a type that cannot be passed yet; 4 private; 2 forbidden; 1 a
  template; 1 the class is abstract, so C++ cannot make one.

  What to expect
  --------------

  - The C++ QAbstractItemModel is created at the first use, not by
    'QAbstractItemModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractItemModel.
  - Qt tells when it has removed the C++ QAbstractItemModel. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QAbstractItemModel, and the names Qt has for
  #  the combinations of its flags enums.
  CheckIndexOption = CheckIndexOption
  CheckIndexOptions = CheckIndexOption
  LayoutChangeHint = LayoutChangeHint

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
    Calls Qt's 'QString QAbstractItemModel::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemmodel.html#tr

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
    #  QString QAbstractItemModel::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QAbstractItemModel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractItemModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAbstractItemModel::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemmodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstractItemModel::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QAbstractItemModel10metaObjectEv',
    )
    return QMetaObject._cuteAt(address)

  @overload(int, int)
  @overload(int, int, QModelIndex)
  def hasIndex(
      self,
      row: int,
      column: int,
      parent: Optional[QModelIndex] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QAbstractItemModel::hasIndex(int row, int column, const
    QModelIndex &parent) const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemmodel.html#hasIndex

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  bool QAbstractItemModel::hasIndex(int row, int column, const
    #      QModelIndex &parent) const
    if parent is None:
      parent = QModelIndex()
    return self.uglySide.call(
        'ritual_ZNK18QAbstractItemModel8hasIndexEiiRK11QModelIndex',
        row, column, self._valueOf(parent),
    )

  @overload(int, int)
  @overload(int, int, QModelIndex)
  def index(
      self,
      row: int,
      column: int,
      parent: Optional[QModelIndex] = None,
  ) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QAbstractItemModel::index(int row, int column,
    const QModelIndex &parent) const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemmodel.html#index

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QAbstractItemModel::index(int row, int column, const
    #      QModelIndex &parent) const
    if parent is None:
      parent = QModelIndex()
    address = self.uglySide.call(
        'ritual_ZNK18QAbstractItemModel5indexEiiRK11QModelIndex',
        row, column, self._valueOf(parent),
    )
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  def parent(self, child: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QAbstractItemModel::parent(const QModelIndex
    &child) const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemmodel.html#parent

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
    #  QModelIndex QAbstractItemModel::parent(const QModelIndex &child) const
    address = self.uglySide.call(
        'ritual_ZNK18QAbstractItemModel6parentERK11QModelIndex',
        self._valueOf(child),
    )
    return QModelIndex._cuteOwning(address)

  @overload(int, int, QModelIndex)
  def sibling(self, row: int, column: int, idx: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QAbstractItemModel::sibling(int row, int column,
    const QModelIndex &idx) const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemmodel.html#sibling

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
    #  QModelIndex QAbstractItemModel::sibling(int row, int column, const
    #      QModelIndex &idx) const
    address = self.uglySide.call(
        'ritual_ZNK18QAbstractItemModel7siblingEiiRK11QModelIndex',
        row, column, self._valueOf(idx),
    )
    return QModelIndex._cuteOwning(address)

  @overload()
  @overload(QModelIndex)
  def rowCount(self, parent: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QAbstractItemModel::rowCount(const QModelIndex &parent)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemmodel.html#rowCount

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QAbstractItemModel::rowCount(const QModelIndex &parent) const
    if parent is None:
      parent = QModelIndex()
    return self.uglySide.call(
        'ritual_ZNK18QAbstractItemModel8rowCountERK11QModelIndex',
        self._valueOf(parent),
    )

  @overload()
  @overload(QModelIndex)
  def columnCount(self, parent: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QAbstractItemModel::columnCount(const QModelIndex
    &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodel.html#columnCount

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QAbstractItemModel::columnCount(const QModelIndex &parent) const
    if parent is None:
      parent = QModelIndex()
    return self.uglySide.call(
        'ritual_ZNK18QAbstractItemModel11columnCountERK11QModelIndex',
        self._valueOf(parent),
    )

  @overload()
  @overload(QModelIndex)
  def hasChildren(self, parent: Optional[QModelIndex] = None) -> bool:
    """
    Calls Qt's 'bool QAbstractItemModel::hasChildren(const QModelIndex
    &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodel.html#hasChildren

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  bool QAbstractItemModel::hasChildren(const QModelIndex &parent) const
    if parent is None:
      parent = QModelIndex()
    return self.uglySide.call(
        'ritual_ZNK18QAbstractItemModel11hasChildrenERK11QModelIndex',
        self._valueOf(parent),
    )

  @overload(QModelIndex)
  @overload(QModelIndex, int)
  def data(self, index: QModelIndex, role: int = 0) -> QVariant:
    """
    Calls Qt's 'QVariant QAbstractItemModel::data(const QModelIndex &index,
    int role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemmodel.html#data

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    role : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAbstractItemModel::data(const QModelIndex &index, int role)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18QAbstractItemModel4dataERK11QModelIndexi',
        self._valueOf(index), role,
    )
    return QVariant._cuteOwning(address)

  @overload(int, Qt.Orientation)
  @overload(int, Qt.Orientation, int)
  def headerData(
      self,
      section: int,
      orientation: Qt.Orientation,
      role: int = 0,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant QAbstractItemModel::headerData(int section,
    Qt::Orientation orientation, int role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemmodel.html#headerData

    Parameters
    ----------

    section : int
      Passed on as it is.

    orientation : Qt.Orientation
      Passed on as its number.

    role : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAbstractItemModel::headerData(int section, Qt::Orientation
    #      orientation, int role) const
    address = self.uglySide.call(
        'ritual_ZNK18QAbstractItemModel10headerDataEiN2Qt11OrientationEi',
        section, orientation.value, role,
    )
    return QVariant._cuteOwning(address)

  @overload(QMimeData, Qt.DropAction, int, int, QModelIndex)
  @overload(NoneType, Qt.DropAction, int, int, QModelIndex)
  def canDropMimeData(
      self,
      data: Optional[QMimeData],
      action: Qt.DropAction,
      row: int,
      column: int,
      parent: QModelIndex,
  ) -> bool:
    """
    Calls Qt's 'bool QAbstractItemModel::canDropMimeData(const QMimeData
    *data, Qt::DropAction action, int row, int column, const QModelIndex
    &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodel.html#canDropMimeData

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
    #  bool QAbstractItemModel::canDropMimeData(const QMimeData *data,
    #      Qt::DropAction action, int row, int column, const QModelIndex
    #      &parent) const
    return self.uglySide.call(
        'ritual_ZNK18QAbstractItemModel15canDropMimeDataEPK9QMimeDataN2Qt10'
        'DropActionEiiRK11QModelIndex',
        self._addressOf(data), action.value, row, column,
        self._valueOf(parent),
    )

  def supportedDropActions(self) -> Qt.DropActions:
    """
    Calls Qt's 'Qt::DropActions QAbstractItemModel::supportedDropActions()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodel.html#supportedDropActions

    Returns
    -------

    Qt.DropActions
      The value standing for the combination Qt gave back.
    """
    #  Qt::DropActions QAbstractItemModel::supportedDropActions() const
    return Qt.DropActions(self.uglySide.call(
        'ritual_ZNK18QAbstractItemModel20supportedDropActionsEv',
    ))

  def supportedDragActions(self) -> Qt.DropActions:
    """
    Calls Qt's 'Qt::DropActions QAbstractItemModel::supportedDragActions()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodel.html#supportedDragActions

    Returns
    -------

    Qt.DropActions
      The value standing for the combination Qt gave back.
    """
    #  Qt::DropActions QAbstractItemModel::supportedDragActions() const
    return Qt.DropActions(self.uglySide.call(
        'ritual_ZNK18QAbstractItemModel20supportedDragActionsEv',
    ))

  @overload(QModelIndex)
  def canFetchMore(self, parent: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QAbstractItemModel::canFetchMore(const QModelIndex
    &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodel.html#canFetchMore

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QAbstractItemModel::canFetchMore(const QModelIndex &parent) const
    return self.uglySide.call(
        'ritual_ZNK18QAbstractItemModel12canFetchMoreERK11QModelIndex',
        self._valueOf(parent),
    )

  @overload(QModelIndex)
  def flags(self, index: QModelIndex) -> Qt.ItemFlags:
    """
    Calls Qt's 'Qt::ItemFlags QAbstractItemModel::flags(const QModelIndex
    &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemmodel.html#flags

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
    #  Qt::ItemFlags QAbstractItemModel::flags(const QModelIndex &index)
    #      const
    return Qt.ItemFlags(self.uglySide.call(
        'ritual_ZNK18QAbstractItemModel5flagsERK11QModelIndex',
        self._valueOf(index),
    ))

  @overload(QModelIndex)
  def buddy(self, index: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QAbstractItemModel::buddy(const QModelIndex
    &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemmodel.html#buddy

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QAbstractItemModel::buddy(const QModelIndex &index) const
    address = self.uglySide.call(
        'ritual_ZNK18QAbstractItemModel5buddyERK11QModelIndex',
        self._valueOf(index),
    )
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  def span(self, index: QModelIndex) -> QSize:
    """
    Calls Qt's 'QSize QAbstractItemModel::span(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemmodel.html#span

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QAbstractItemModel::span(const QModelIndex &index) const
    address = self.uglySide.call(
        'ritual_ZNK18QAbstractItemModel4spanERK11QModelIndex',
        self._valueOf(index),
    )
    return QSize._cuteOwning(address)

  @overload(QModelIndex)
  @overload(QModelIndex, CheckIndexOptions)
  def checkIndex(
      self,
      index: QModelIndex,
      options: CheckIndexOptions = CheckIndexOptions.NoOption,
  ) -> bool:
    """
    Calls Qt's 'bool QAbstractItemModel::checkIndex(const QModelIndex &index,
    CheckIndexOptions options) const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemmodel.html#checkIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    options : CheckIndexOptions
      Passed on as its number. May be left out, as in Qt: it is then
      CheckIndexOptions.NoOption.
    """
    #  bool QAbstractItemModel::checkIndex(const QModelIndex &index,
    #      CheckIndexOptions options) const
    return self.uglySide.call(
        'ritual_ZNK18QAbstractItemModel10checkIndexERK11QModelIndex6QFlagsI'
        'NS_16CheckIndexOptionEE',
        self._valueOf(index), options.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QModelIndex, QVariant)
  @overload(QModelIndex, QVariant, int)
  def setData(
      self,
      index: QModelIndex,
      value: QVariant,
      role: int = 2,
  ) -> bool:
    """
    Calls Qt's 'bool QAbstractItemModel::setData(const QModelIndex &index,
    const QVariant &value, int role)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemmodel.html#setData

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    role : int
      Passed on as it is. May be left out, as in Qt: it is then 2.
    """
    #  bool QAbstractItemModel::setData(const QModelIndex &index, const
    #      QVariant &value, int role)
    return self.uglySide.call(
        'ritual_ZN18QAbstractItemModel7setDataERK11QModelIndexRK8QVarianti',
        self._valueOf(index), self._valueOf(value), role,
    )

  @overload(int, Qt.Orientation, QVariant)
  @overload(int, Qt.Orientation, QVariant, int)
  def setHeaderData(
      self,
      section: int,
      orientation: Qt.Orientation,
      value: QVariant,
      role: int = 2,
  ) -> bool:
    """
    Calls Qt's 'bool QAbstractItemModel::setHeaderData(int section,
    Qt::Orientation orientation, const QVariant &value, int role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodel.html#setHeaderData

    Parameters
    ----------

    section : int
      Passed on as it is.

    orientation : Qt.Orientation
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    role : int
      Passed on as it is. May be left out, as in Qt: it is then 2.
    """
    #  bool QAbstractItemModel::setHeaderData(int section, Qt::Orientation
    #      orientation, const QVariant &value, int role)
    return self.uglySide.call(
        'ritual_ZN18QAbstractItemModel13setHeaderDataEiN2Qt11OrientationERK'
        '8QVarianti',
        section, orientation.value, self._valueOf(value), role,
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

  @overload(QModelIndex)
  def clearItemData(self, index: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QAbstractItemModel::clearItemData(const QModelIndex
    &index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodel.html#clearItemData

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QAbstractItemModel::clearItemData(const QModelIndex &index)
    return self.uglySide.call(
        'ritual_ZN18QAbstractItemModel13clearItemDataERK11QModelIndex',
        self._valueOf(index),
    )

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
    Calls Qt's 'bool QAbstractItemModel::dropMimeData(const QMimeData *data,
    Qt::DropAction action, int row, int column, const QModelIndex &parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodel.html#dropMimeData

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
    #  bool QAbstractItemModel::dropMimeData(const QMimeData *data,
    #      Qt::DropAction action, int row, int column, const QModelIndex
    #      &parent)
    return self.uglySide.call(
        'ritual_ZN18QAbstractItemModel12dropMimeDataEPK9QMimeDataN2Qt10Drop'
        'ActionEiiRK11QModelIndex',
        self._addressOf(data), action.value, row, column,
        self._valueOf(parent),
    )

  @overload(int, int)
  @overload(int, int, QModelIndex)
  def insertRows(
      self,
      row: int,
      count: int,
      parent: Optional[QModelIndex] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QAbstractItemModel::insertRows(int row, int count, const
    QModelIndex &parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemmodel.html#insertRows

    Parameters
    ----------

    row : int
      Passed on as it is.

    count : int
      Passed on as it is.

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  bool QAbstractItemModel::insertRows(int row, int count, const
    #      QModelIndex &parent)
    if parent is None:
      parent = QModelIndex()
    return self.uglySide.call(
        'ritual_ZN18QAbstractItemModel10insertRowsEiiRK11QModelIndex',
        row, count, self._valueOf(parent),
    )

  @overload(int, int)
  @overload(int, int, QModelIndex)
  def insertColumns(
      self,
      column: int,
      count: int,
      parent: Optional[QModelIndex] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QAbstractItemModel::insertColumns(int column, int count,
    const QModelIndex &parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodel.html#insertColumns

    Parameters
    ----------

    column : int
      Passed on as it is.

    count : int
      Passed on as it is.

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  bool QAbstractItemModel::insertColumns(int column, int count, const
    #      QModelIndex &parent)
    if parent is None:
      parent = QModelIndex()
    return self.uglySide.call(
        'ritual_ZN18QAbstractItemModel13insertColumnsEiiRK11QModelIndex',
        column, count, self._valueOf(parent),
    )

  @overload(int, int)
  @overload(int, int, QModelIndex)
  def removeRows(
      self,
      row: int,
      count: int,
      parent: Optional[QModelIndex] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QAbstractItemModel::removeRows(int row, int count, const
    QModelIndex &parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemmodel.html#removeRows

    Parameters
    ----------

    row : int
      Passed on as it is.

    count : int
      Passed on as it is.

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  bool QAbstractItemModel::removeRows(int row, int count, const
    #      QModelIndex &parent)
    if parent is None:
      parent = QModelIndex()
    return self.uglySide.call(
        'ritual_ZN18QAbstractItemModel10removeRowsEiiRK11QModelIndex',
        row, count, self._valueOf(parent),
    )

  @overload(int, int)
  @overload(int, int, QModelIndex)
  def removeColumns(
      self,
      column: int,
      count: int,
      parent: Optional[QModelIndex] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QAbstractItemModel::removeColumns(int column, int count,
    const QModelIndex &parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodel.html#removeColumns

    Parameters
    ----------

    column : int
      Passed on as it is.

    count : int
      Passed on as it is.

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  bool QAbstractItemModel::removeColumns(int column, int count, const
    #      QModelIndex &parent)
    if parent is None:
      parent = QModelIndex()
    return self.uglySide.call(
        'ritual_ZN18QAbstractItemModel13removeColumnsEiiRK11QModelIndex',
        column, count, self._valueOf(parent),
    )

  @overload(QModelIndex, int, int, QModelIndex, int)
  def moveRows(
      self,
      sourceParent: QModelIndex,
      sourceRow: int,
      count: int,
      destinationParent: QModelIndex,
      destinationChild: int,
  ) -> bool:
    """
    Calls Qt's 'bool QAbstractItemModel::moveRows(const QModelIndex
    &sourceParent, int sourceRow, int count, const QModelIndex
    &destinationParent, int destinationChild)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemmodel.html#moveRows

    Parameters
    ----------

    sourceParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    sourceRow : int
      Passed on as it is.

    count : int
      Passed on as it is.

    destinationParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    destinationChild : int
      Passed on as it is.
    """
    #  bool QAbstractItemModel::moveRows(const QModelIndex &sourceParent, int
    #      sourceRow, int count, const QModelIndex &destinationParent, int
    #      destinationChild)
    return self.uglySide.call(
        'ritual_ZN18QAbstractItemModel8moveRowsERK11QModelIndexiiS2_i',
        self._valueOf(sourceParent), sourceRow, count,
        self._valueOf(destinationParent), destinationChild,
    )

  @overload(QModelIndex, int, int, QModelIndex, int)
  def moveColumns(
      self,
      sourceParent: QModelIndex,
      sourceColumn: int,
      count: int,
      destinationParent: QModelIndex,
      destinationChild: int,
  ) -> bool:
    """
    Calls Qt's 'bool QAbstractItemModel::moveColumns(const QModelIndex
    &sourceParent, int sourceColumn, int count, const QModelIndex
    &destinationParent, int destinationChild)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodel.html#moveColumns

    Parameters
    ----------

    sourceParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    sourceColumn : int
      Passed on as it is.

    count : int
      Passed on as it is.

    destinationParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    destinationChild : int
      Passed on as it is.
    """
    #  bool QAbstractItemModel::moveColumns(const QModelIndex &sourceParent,
    #      int sourceColumn, int count, const QModelIndex &destinationParent,
    #      int destinationChild)
    return self.uglySide.call(
        'ritual_ZN18QAbstractItemModel11moveColumnsERK11QModelIndexiiS2_i',
        self._valueOf(sourceParent), sourceColumn, count,
        self._valueOf(destinationParent), destinationChild,
    )

  @overload(int)
  @overload(int, QModelIndex)
  def insertRow(
      self,
      row: int,
      parent: Optional[QModelIndex] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QAbstractItemModel::insertRow(int row, const QModelIndex
    &parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemmodel.html#insertRow

    Parameters
    ----------

    row : int
      Passed on as it is.

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  bool QAbstractItemModel::insertRow(int row, const QModelIndex &parent)
    if parent is None:
      parent = QModelIndex()
    return self.uglySide.call(
        'ritual_ZN18QAbstractItemModel9insertRowEiRK11QModelIndex',
        row, self._valueOf(parent),
    )

  @overload(int)
  @overload(int, QModelIndex)
  def insertColumn(
      self,
      column: int,
      parent: Optional[QModelIndex] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QAbstractItemModel::insertColumn(int column, const
    QModelIndex &parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodel.html#insertColumn

    Parameters
    ----------

    column : int
      Passed on as it is.

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  bool QAbstractItemModel::insertColumn(int column, const QModelIndex
    #      &parent)
    if parent is None:
      parent = QModelIndex()
    return self.uglySide.call(
        'ritual_ZN18QAbstractItemModel12insertColumnEiRK11QModelIndex',
        column, self._valueOf(parent),
    )

  @overload(int)
  @overload(int, QModelIndex)
  def removeRow(
      self,
      row: int,
      parent: Optional[QModelIndex] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QAbstractItemModel::removeRow(int row, const QModelIndex
    &parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemmodel.html#removeRow

    Parameters
    ----------

    row : int
      Passed on as it is.

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  bool QAbstractItemModel::removeRow(int row, const QModelIndex &parent)
    if parent is None:
      parent = QModelIndex()
    return self.uglySide.call(
        'ritual_ZN18QAbstractItemModel9removeRowEiRK11QModelIndex',
        row, self._valueOf(parent),
    )

  @overload(int)
  @overload(int, QModelIndex)
  def removeColumn(
      self,
      column: int,
      parent: Optional[QModelIndex] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QAbstractItemModel::removeColumn(int column, const
    QModelIndex &parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodel.html#removeColumn

    Parameters
    ----------

    column : int
      Passed on as it is.

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  bool QAbstractItemModel::removeColumn(int column, const QModelIndex
    #      &parent)
    if parent is None:
      parent = QModelIndex()
    return self.uglySide.call(
        'ritual_ZN18QAbstractItemModel12removeColumnEiRK11QModelIndex',
        column, self._valueOf(parent),
    )

  @overload(QModelIndex, int, QModelIndex, int)
  def moveRow(
      self,
      sourceParent: QModelIndex,
      sourceRow: int,
      destinationParent: QModelIndex,
      destinationChild: int,
  ) -> bool:
    """
    Calls Qt's 'bool QAbstractItemModel::moveRow(const QModelIndex
    &sourceParent, int sourceRow, const QModelIndex &destinationParent, int
    destinationChild)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemmodel.html#moveRow

    Parameters
    ----------

    sourceParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    sourceRow : int
      Passed on as it is.

    destinationParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    destinationChild : int
      Passed on as it is.
    """
    #  bool QAbstractItemModel::moveRow(const QModelIndex &sourceParent, int
    #      sourceRow, const QModelIndex &destinationParent, int
    #      destinationChild)
    return self.uglySide.call(
        'ritual_ZN18QAbstractItemModel7moveRowERK11QModelIndexiS2_i',
        self._valueOf(sourceParent), sourceRow,
        self._valueOf(destinationParent), destinationChild,
    )

  @overload(QModelIndex, int, QModelIndex, int)
  def moveColumn(
      self,
      sourceParent: QModelIndex,
      sourceColumn: int,
      destinationParent: QModelIndex,
      destinationChild: int,
  ) -> bool:
    """
    Calls Qt's 'bool QAbstractItemModel::moveColumn(const QModelIndex
    &sourceParent, int sourceColumn, const QModelIndex &destinationParent,
    int destinationChild)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemmodel.html#moveColumn

    Parameters
    ----------

    sourceParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    sourceColumn : int
      Passed on as it is.

    destinationParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    destinationChild : int
      Passed on as it is.
    """
    #  bool QAbstractItemModel::moveColumn(const QModelIndex &sourceParent,
    #      int sourceColumn, const QModelIndex &destinationParent, int
    #      destinationChild)
    return self.uglySide.call(
        'ritual_ZN18QAbstractItemModel10moveColumnERK11QModelIndexiS2_i',
        self._valueOf(sourceParent), sourceColumn,
        self._valueOf(destinationParent), destinationChild,
    )

  @overload(QModelIndex)
  def fetchMore(self, parent: QModelIndex) -> None:
    """
    Calls Qt's 'void QAbstractItemModel::fetchMore(const QModelIndex
    &parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemmodel.html#fetchMore

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QAbstractItemModel::fetchMore(const QModelIndex &parent)
    self.uglySide.call(
        'ritual_ZN18QAbstractItemModel9fetchMoreERK11QModelIndex',
        self._valueOf(parent),
    )

  @overload(int)
  @overload(int, Qt.SortOrder)
  def sort(
      self,
      column: int,
      order: Qt.SortOrder = Qt.SortOrder.AscendingOrder,
  ) -> None:
    """
    Calls Qt's 'void QAbstractItemModel::sort(int column, Qt::SortOrder
    order)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemmodel.html#sort

    Parameters
    ----------

    column : int
      Passed on as it is.

    order : Qt.SortOrder
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.SortOrder.AscendingOrder.
    """
    #  void QAbstractItemModel::sort(int column, Qt::SortOrder order)
    self.uglySide.call(
        'ritual_ZN18QAbstractItemModel4sortEiN2Qt9SortOrderE',
        column, order.value,
    )

  def submit(self) -> bool:
    """
    Calls Qt's 'bool QAbstractItemModel::submit()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemmodel.html#submit
    """
    #  bool QAbstractItemModel::submit()
    return self.uglySide.call('ritual_ZN18QAbstractItemModel6submitEv')

  def revert(self) -> None:
    """
    Calls Qt's 'void QAbstractItemModel::revert()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemmodel.html#revert
    """
    #  void QAbstractItemModel::revert()
    self.uglySide.call('ritual_ZN18QAbstractItemModel6revertEv')
