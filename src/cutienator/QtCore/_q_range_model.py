"""
QRangeModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qrangemodel.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import Qt, QAbstractItemModel

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QCollator, QMetaObject, QMimeData, QModelIndex
  from . import QModelRoleDataSpan, QSize, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCollator = WAIT['QCollator']
  QMimeData = WAIT['QMimeData']
  QModelIndex = WAIT['QModelIndex']
  QModelRoleDataSpan = WAIT['QModelRoleDataSpan']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRangeModel(QAbstractItemModel):
  """
  The cute side of Qt's QRangeModel: a plain Python object standing in front
  of one C++ QRangeModel.

  It is built on the cute 'QAbstractItemModel', as Qt's QRangeModel is built
  on Qt's QAbstractItemModel, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QRangeModel that has a ritual and that Python can
  call so far, 43 names in all: 'metaObject', 'tr', 'index', 'parent',
  'sibling', 'rowCount', 'columnCount', 'flags', 'headerData',
  'setHeaderData', 'data', 'setData', 'clearItemData', 'insertColumns',
  'removeColumns', 'moveColumns', 'insertRows', 'removeRows', 'moveRows',
  'resetRoleNames', 'canFetchMore', 'fetchMore', 'hasChildren', 'buddy',
  'canDropMimeData', 'dropMimeData', 'multiData', 'sort', 'sortCollator',
  'setSortCollator', 'resetSortCollator', 'sortRole', 'setSortRole',
  'resetSortRole', 'span', 'supportedDragActions', 'setSupportedDragActions',
  'resetSupportedDragActions', 'supportedDropActions',
  'setSupportedDropActions', 'resetSupportedDropActions',
  'autoConnectPolicy', 'setAutoConnectPolicy'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRangeModel::~QRangeModel()': the destructor: Python never removes
    a C++ QRangeModel.

  What has no ritual
  ------------------

  30 of the 74 functions Qt declares: 9 takes or gives a type that cannot be
  passed yet; 6 a signal; 4 a template; 4 private; 4 forbidden; 3 protected.

  What to expect
  --------------

  - The C++ QRangeModel is created at the first use, not by
    'QRangeModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRangeModel.
  - Qt tells when it has removed the C++ QRangeModel. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QRangeModel, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class AutoConnectPolicy(CuteNum, scoped=True):
    """
    The enum 'QRangeModel::AutoConnectPolicy' of Qt, with the 3 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    NULL = Kee[int](0)
    Full = Kee[int](1)
    OnRead = Kee[int](2)

  class DropOperation(CuteNum, scoped=True):
    """
    The enum 'QRangeModel::DropOperation' of Qt, with the 6 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    DontDrop = Kee[int](0)
    Automatic = Kee[int](1)
    OverwriteAndIgnore = Kee[int](2)
    OverwriteAndExtend = Kee[int](3)
    InsertAsSiblings = Kee[int](4)
    InsertAsChildren = Kee[int](5)

  class RowCategory(CuteNum, scoped=True):
    """
    The enum 'QRangeModel::RowCategory' of Qt, with the 2 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Default = Kee[int](0)
    MultiRoleItem = Kee[int](1)

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
    Calls Qt's 'QString QRangeModel::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qrangemodel.html#tr

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
    #  QString QRangeModel::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QRangeModel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRangeModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QRangeModel::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrangemodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QRangeModel::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QRangeModel10metaObjectEv')
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(int, int)
  @overload(int, int, QModelIndex)
  def index(
      self,
      row: int,
      column: int,
      parent: Optional[QModelIndex] = None,
  ) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QRangeModel::index(int row, int column, const
    QModelIndex &parent) const'.

    Qt's own words: https://doc.qt.io/qt-6/qrangemodel.html#index

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
    #  QModelIndex QRangeModel::index(int row, int column, const QModelIndex
    #      &parent) const
    if parent is None:
      from . import QModelIndex
      parent = QModelIndex()
    address = self.uglySide.call(
        'ritual_ZNK11QRangeModel5indexEiiRK11QModelIndex',
        row, column, self._valueOf(parent),
    )
    from . import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  def parent(self, child: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QRangeModel::parent(const QModelIndex &child)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qrangemodel.html#parent

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
    #  QModelIndex QRangeModel::parent(const QModelIndex &child) const
    address = self.uglySide.call(
        'ritual_ZNK11QRangeModel6parentERK11QModelIndex',
        self._valueOf(child),
    )
    from . import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(int, int, QModelIndex)
  def sibling(
      self,
      row: int,
      column: int,
      index: QModelIndex,
  ) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QRangeModel::sibling(int row, int column, const
    QModelIndex &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qrangemodel.html#sibling

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QRangeModel::sibling(int row, int column, const
    #      QModelIndex &index) const
    address = self.uglySide.call(
        'ritual_ZNK11QRangeModel7siblingEiiRK11QModelIndex',
        row, column, self._valueOf(index),
    )
    from . import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload()
  @overload(QModelIndex)
  def rowCount(self, parent: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QRangeModel::rowCount(const QModelIndex &parent) const'.

    Qt's own words: https://doc.qt.io/qt-6/qrangemodel.html#rowCount

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QRangeModel::rowCount(const QModelIndex &parent) const
    if parent is None:
      from . import QModelIndex
      parent = QModelIndex()
    return self.uglySide.call(
        'ritual_ZNK11QRangeModel8rowCountERK11QModelIndex',
        self._valueOf(parent),
    )

  @overload()
  @overload(QModelIndex)
  def columnCount(self, parent: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QRangeModel::columnCount(const QModelIndex &parent)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qrangemodel.html#columnCount

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QRangeModel::columnCount(const QModelIndex &parent) const
    if parent is None:
      from . import QModelIndex
      parent = QModelIndex()
    return self.uglySide.call(
        'ritual_ZNK11QRangeModel11columnCountERK11QModelIndex',
        self._valueOf(parent),
    )

  @overload(QModelIndex)
  def flags(self, index: QModelIndex) -> Qt.ItemFlags:
    """
    Calls Qt's 'Qt::ItemFlags QRangeModel::flags(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qrangemodel.html#flags

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
    #  Qt::ItemFlags QRangeModel::flags(const QModelIndex &index) const
    return Qt.ItemFlags(self.uglySide.call(
        'ritual_ZNK11QRangeModel5flagsERK11QModelIndex',
        self._valueOf(index),
    ))

  @overload(int, Qt.Orientation)
  @overload(int, Qt.Orientation, int)
  def headerData(
      self,
      section: int,
      orientation: Qt.Orientation,
      role: int = 0,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant QRangeModel::headerData(int section, Qt::Orientation
    orientation, int role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qrangemodel.html#headerData

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
    #  QVariant QRangeModel::headerData(int section, Qt::Orientation
    #      orientation, int role) const
    address = self.uglySide.call(
        'ritual_ZNK11QRangeModel10headerDataEiN2Qt11OrientationEi',
        section, orientation.value, role,
    )
    from . import QVariant
    return QVariant._cuteOwning(address)

  @overload(QModelIndex)
  @overload(QModelIndex, int)
  def data(self, index: QModelIndex, role: int = 0) -> QVariant:
    """
    Calls Qt's 'QVariant QRangeModel::data(const QModelIndex &index, int
    role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qrangemodel.html#data

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
    #  QVariant QRangeModel::data(const QModelIndex &index, int role) const
    address = self.uglySide.call(
        'ritual_ZNK11QRangeModel4dataERK11QModelIndexi',
        self._valueOf(index), role,
    )
    from . import QVariant
    return QVariant._cuteOwning(address)

  @overload(QModelIndex)
  def canFetchMore(self, parent: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QRangeModel::canFetchMore(const QModelIndex &parent)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qrangemodel.html#canFetchMore

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QRangeModel::canFetchMore(const QModelIndex &parent) const
    return self.uglySide.call(
        'ritual_ZNK11QRangeModel12canFetchMoreERK11QModelIndex',
        self._valueOf(parent),
    )

  @overload()
  @overload(QModelIndex)
  def hasChildren(self, parent: Optional[QModelIndex] = None) -> bool:
    """
    Calls Qt's 'bool QRangeModel::hasChildren(const QModelIndex &parent)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qrangemodel.html#hasChildren

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  bool QRangeModel::hasChildren(const QModelIndex &parent) const
    if parent is None:
      from . import QModelIndex
      parent = QModelIndex()
    return self.uglySide.call(
        'ritual_ZNK11QRangeModel11hasChildrenERK11QModelIndex',
        self._valueOf(parent),
    )

  @overload(QModelIndex)
  def buddy(self, index: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QRangeModel::buddy(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qrangemodel.html#buddy

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
    #  QModelIndex QRangeModel::buddy(const QModelIndex &index) const
    address = self.uglySide.call(
        'ritual_ZNK11QRangeModel5buddyERK11QModelIndex',
        self._valueOf(index),
    )
    from . import QModelIndex
    return QModelIndex._cuteOwning(address)

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
    Calls Qt's 'bool QRangeModel::canDropMimeData(const QMimeData *data,
    Qt::DropAction action, int row, int column, const QModelIndex &parent)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qrangemodel.html#canDropMimeData

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
    #  bool QRangeModel::canDropMimeData(const QMimeData *data,
    #      Qt::DropAction action, int row, int column, const QModelIndex
    #      &parent) const
    return self.uglySide.call(
        'ritual_ZNK11QRangeModel15canDropMimeDataEPK9QMimeDataN2Qt10DropAct'
        'ionEiiRK11QModelIndex',
        self._addressOf(data), action.value, row, column,
        self._valueOf(parent),
    )

  def sortCollator(self) -> QCollator:
    """
    Calls Qt's 'QCollator QRangeModel::sortCollator() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrangemodel.html#sortCollator

    Returns
    -------

    QCollator
      A new cute QCollator around the copy Qt gave back. Python owns it.
    """
    #  QCollator QRangeModel::sortCollator() const
    address = self.uglySide.call('ritual_ZNK11QRangeModel12sortCollatorEv')
    from . import QCollator
    return QCollator._cuteOwning(address)

  def sortRole(self) -> int:
    """
    Calls Qt's 'int QRangeModel::sortRole() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrangemodel.html#sortRole
    """
    #  int QRangeModel::sortRole() const
    return self.uglySide.call('ritual_ZNK11QRangeModel8sortRoleEv')

  @overload(QModelIndex)
  def span(self, index: QModelIndex) -> QSize:
    """
    Calls Qt's 'QSize QRangeModel::span(const QModelIndex &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qrangemodel.html#span

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
    #  QSize QRangeModel::span(const QModelIndex &index) const
    address = self.uglySide.call(
        'ritual_ZNK11QRangeModel4spanERK11QModelIndex', self._valueOf(index),
    )
    from . import QSize
    return QSize._cuteOwning(address)

  def supportedDragActions(self) -> Qt.DropActions:
    """
    Calls Qt's 'Qt::DropActions QRangeModel::supportedDragActions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrangemodel.html#supportedDragActions

    Returns
    -------

    Qt.DropActions
      The value standing for the combination Qt gave back.
    """
    #  Qt::DropActions QRangeModel::supportedDragActions() const
    return Qt.DropActions(self.uglySide.call(
        'ritual_ZNK11QRangeModel20supportedDragActionsEv',
    ))

  def supportedDropActions(self) -> Qt.DropActions:
    """
    Calls Qt's 'Qt::DropActions QRangeModel::supportedDropActions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrangemodel.html#supportedDropActions

    Returns
    -------

    Qt.DropActions
      The value standing for the combination Qt gave back.
    """
    #  Qt::DropActions QRangeModel::supportedDropActions() const
    return Qt.DropActions(self.uglySide.call(
        'ritual_ZNK11QRangeModel20supportedDropActionsEv',
    ))

  def autoConnectPolicy(self) -> AutoConnectPolicy:
    """
    Calls Qt's 'AutoConnectPolicy QRangeModel::autoConnectPolicy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrangemodel.html#autoConnectPolicy

    Returns
    -------

    AutoConnectPolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'AutoConnectPolicy(number)' gives.
    """
    #  AutoConnectPolicy QRangeModel::autoConnectPolicy() const
    return QRangeModel.AutoConnectPolicy(self.uglySide.call(
        'ritual_ZNK11QRangeModel17autoConnectPolicyEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, Qt.Orientation, QVariant)
  @overload(int, Qt.Orientation, QVariant, int)
  def setHeaderData(
      self,
      section: int,
      orientation: Qt.Orientation,
      data: QVariant,
      role: int = 2,
  ) -> bool:
    """
    Calls Qt's 'bool QRangeModel::setHeaderData(int section, Qt::Orientation
    orientation, const QVariant &data, int role)'.

    Qt's own words: https://doc.qt.io/qt-6/qrangemodel.html#setHeaderData

    Parameters
    ----------

    section : int
      Passed on as it is.

    orientation : Qt.Orientation
      Passed on as its number.

    data : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    role : int
      Passed on as it is. May be left out, as in Qt: it is then 2.
    """
    #  bool QRangeModel::setHeaderData(int section, Qt::Orientation
    #      orientation, const QVariant &data, int role)
    return self.uglySide.call(
        'ritual_ZN11QRangeModel13setHeaderDataEiN2Qt11OrientationERK8QVaria'
        'nti',
        section, orientation.value, self._valueOf(data), role,
    )

  @overload(QModelIndex, QVariant)
  @overload(QModelIndex, QVariant, int)
  def setData(
      self,
      index: QModelIndex,
      data: QVariant,
      role: int = 2,
  ) -> bool:
    """
    Calls Qt's 'bool QRangeModel::setData(const QModelIndex &index, const
    QVariant &data, int role)'.

    Qt's own words: https://doc.qt.io/qt-6/qrangemodel.html#setData

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    data : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    role : int
      Passed on as it is. May be left out, as in Qt: it is then 2.
    """
    #  bool QRangeModel::setData(const QModelIndex &index, const QVariant
    #      &data, int role)
    return self.uglySide.call(
        'ritual_ZN11QRangeModel7setDataERK11QModelIndexRK8QVarianti',
        self._valueOf(index), self._valueOf(data), role,
    )

  @overload(QCollator)
  def setSortCollator(self, collator: QCollator) -> None:
    """
    Calls Qt's 'void QRangeModel::setSortCollator(const QCollator
    &collator)'.

    Qt's own words: https://doc.qt.io/qt-6/qrangemodel.html#setSortCollator

    Parameters
    ----------

    collator : QCollator
      Passed on as a value: Qt reads the C++ QCollator, which stays Python's
      own.
    """
    #  void QRangeModel::setSortCollator(const QCollator &collator)
    self.uglySide.call(
        'ritual_ZN11QRangeModel15setSortCollatorERK9QCollator',
        self._valueOf(collator),
    )

  @overload(int)
  def setSortRole(self, role: int) -> None:
    """
    Calls Qt's 'void QRangeModel::setSortRole(int role)'.

    Qt's own words: https://doc.qt.io/qt-6/qrangemodel.html#setSortRole

    Parameters
    ----------

    role : int
      Passed on as it is.
    """
    #  void QRangeModel::setSortRole(int role)
    self.uglySide.call('ritual_ZN11QRangeModel11setSortRoleEi', role)

  @overload(Qt.DropActions)
  def setSupportedDragActions(self, actions: Qt.DropActions) -> None:
    """
    Calls Qt's 'void QRangeModel::setSupportedDragActions(Qt::DropActions
    actions)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrangemodel.html#setSupportedDragActions

    Parameters
    ----------

    actions : Qt.DropActions
      Passed on as its number.
    """
    #  void QRangeModel::setSupportedDragActions(Qt::DropActions actions)
    self.uglySide.call(
        'ritual_ZN11QRangeModel23setSupportedDragActionsE6QFlagsIN2Qt10Drop'
        'ActionEE',
        actions.value,
    )

  @overload(Qt.DropActions)
  def setSupportedDropActions(self, actions: Qt.DropActions) -> None:
    """
    Calls Qt's 'void QRangeModel::setSupportedDropActions(Qt::DropActions
    actions)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrangemodel.html#setSupportedDropActions

    Parameters
    ----------

    actions : Qt.DropActions
      Passed on as its number.
    """
    #  void QRangeModel::setSupportedDropActions(Qt::DropActions actions)
    self.uglySide.call(
        'ritual_ZN11QRangeModel23setSupportedDropActionsE6QFlagsIN2Qt10Drop'
        'ActionEE',
        actions.value,
    )

  @overload(AutoConnectPolicy)
  def setAutoConnectPolicy(self, policy: AutoConnectPolicy) -> None:
    """
    Calls Qt's 'void QRangeModel::setAutoConnectPolicy(AutoConnectPolicy
    policy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrangemodel.html#setAutoConnectPolicy

    Parameters
    ----------

    policy : AutoConnectPolicy
      Passed on as its number.
    """
    #  void QRangeModel::setAutoConnectPolicy(AutoConnectPolicy policy)
    self.uglySide.call(
        'ritual_ZN11QRangeModel20setAutoConnectPolicyENS_17AutoConnectPolic'
        'yE',
        policy.value,
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
    Calls Qt's 'bool QRangeModel::clearItemData(const QModelIndex &index)'.

    Qt's own words: https://doc.qt.io/qt-6/qrangemodel.html#clearItemData

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QRangeModel::clearItemData(const QModelIndex &index)
    return self.uglySide.call(
        'ritual_ZN11QRangeModel13clearItemDataERK11QModelIndex',
        self._valueOf(index),
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
    Calls Qt's 'bool QRangeModel::insertColumns(int column, int count, const
    QModelIndex &parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qrangemodel.html#insertColumns

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
    #  bool QRangeModel::insertColumns(int column, int count, const
    #      QModelIndex &parent)
    if parent is None:
      from . import QModelIndex
      parent = QModelIndex()
    return self.uglySide.call(
        'ritual_ZN11QRangeModel13insertColumnsEiiRK11QModelIndex',
        column, count, self._valueOf(parent),
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
    Calls Qt's 'bool QRangeModel::removeColumns(int column, int count, const
    QModelIndex &parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qrangemodel.html#removeColumns

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
    #  bool QRangeModel::removeColumns(int column, int count, const
    #      QModelIndex &parent)
    if parent is None:
      from . import QModelIndex
      parent = QModelIndex()
    return self.uglySide.call(
        'ritual_ZN11QRangeModel13removeColumnsEiiRK11QModelIndex',
        column, count, self._valueOf(parent),
    )

  @overload(QModelIndex, int, int, QModelIndex, int)
  def moveColumns(
      self,
      sourceParent: QModelIndex,
      sourceColumn: int,
      count: int,
      destParent: QModelIndex,
      destColumn: int,
  ) -> bool:
    """
    Calls Qt's 'bool QRangeModel::moveColumns(const QModelIndex
    &sourceParent, int sourceColumn, int count, const QModelIndex
    &destParent, int destColumn)'.

    Qt's own words: https://doc.qt.io/qt-6/qrangemodel.html#moveColumns

    Parameters
    ----------

    sourceParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    sourceColumn : int
      Passed on as it is.

    count : int
      Passed on as it is.

    destParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    destColumn : int
      Passed on as it is.
    """
    #  bool QRangeModel::moveColumns(const QModelIndex &sourceParent, int
    #      sourceColumn, int count, const QModelIndex &destParent, int
    #      destColumn)
    return self.uglySide.call(
        'ritual_ZN11QRangeModel11moveColumnsERK11QModelIndexiiS2_i',
        self._valueOf(sourceParent), sourceColumn, count,
        self._valueOf(destParent), destColumn,
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
    Calls Qt's 'bool QRangeModel::insertRows(int row, int count, const
    QModelIndex &parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qrangemodel.html#insertRows

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
    #  bool QRangeModel::insertRows(int row, int count, const QModelIndex
    #      &parent)
    if parent is None:
      from . import QModelIndex
      parent = QModelIndex()
    return self.uglySide.call(
        'ritual_ZN11QRangeModel10insertRowsEiiRK11QModelIndex',
        row, count, self._valueOf(parent),
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
    Calls Qt's 'bool QRangeModel::removeRows(int row, int count, const
    QModelIndex &parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qrangemodel.html#removeRows

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
    #  bool QRangeModel::removeRows(int row, int count, const QModelIndex
    #      &parent)
    if parent is None:
      from . import QModelIndex
      parent = QModelIndex()
    return self.uglySide.call(
        'ritual_ZN11QRangeModel10removeRowsEiiRK11QModelIndex',
        row, count, self._valueOf(parent),
    )

  @overload(QModelIndex, int, int, QModelIndex, int)
  def moveRows(
      self,
      sourceParent: QModelIndex,
      sourceRow: int,
      count: int,
      destParent: QModelIndex,
      destRow: int,
  ) -> bool:
    """
    Calls Qt's 'bool QRangeModel::moveRows(const QModelIndex &sourceParent,
    int sourceRow, int count, const QModelIndex &destParent, int destRow)'.

    Qt's own words: https://doc.qt.io/qt-6/qrangemodel.html#moveRows

    Parameters
    ----------

    sourceParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    sourceRow : int
      Passed on as it is.

    count : int
      Passed on as it is.

    destParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    destRow : int
      Passed on as it is.
    """
    #  bool QRangeModel::moveRows(const QModelIndex &sourceParent, int
    #      sourceRow, int count, const QModelIndex &destParent, int destRow)
    return self.uglySide.call(
        'ritual_ZN11QRangeModel8moveRowsERK11QModelIndexiiS2_i',
        self._valueOf(sourceParent), sourceRow, count,
        self._valueOf(destParent), destRow,
    )

  def resetRoleNames(self) -> None:
    """
    Calls Qt's 'void QRangeModel::resetRoleNames()'.

    Qt's own words: https://doc.qt.io/qt-6/qrangemodel.html#resetRoleNames
    """
    #  void QRangeModel::resetRoleNames()
    self.uglySide.call('ritual_ZN11QRangeModel14resetRoleNamesEv')

  @overload(QModelIndex)
  def fetchMore(self, parent: QModelIndex) -> None:
    """
    Calls Qt's 'void QRangeModel::fetchMore(const QModelIndex &parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qrangemodel.html#fetchMore

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QRangeModel::fetchMore(const QModelIndex &parent)
    self.uglySide.call(
        'ritual_ZN11QRangeModel9fetchMoreERK11QModelIndex',
        self._valueOf(parent),
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
    Calls Qt's 'bool QRangeModel::dropMimeData(const QMimeData *data,
    Qt::DropAction action, int row, int column, const QModelIndex &parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qrangemodel.html#dropMimeData

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
    #  bool QRangeModel::dropMimeData(const QMimeData *data, Qt::DropAction
    #      action, int row, int column, const QModelIndex &parent)
    return self.uglySide.call(
        'ritual_ZN11QRangeModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionE'
        'iiRK11QModelIndex',
        self._addressOf(data), action.value, row, column,
        self._valueOf(parent),
    )

  @overload(QModelIndex, QModelRoleDataSpan)
  def multiData(
      self,
      index: QModelIndex,
      roleDataSpan: QModelRoleDataSpan,
  ) -> None:
    """
    Calls Qt's 'void QRangeModel::multiData(const QModelIndex &index,
    QModelRoleDataSpan roleDataSpan) const'.

    Qt's own words: https://doc.qt.io/qt-6/qrangemodel.html#multiData

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    roleDataSpan : QModelRoleDataSpan
      Passed on as a value: Qt reads the C++ QModelRoleDataSpan, which stays
      Python's own.
    """
    #  void QRangeModel::multiData(const QModelIndex &index,
    #      QModelRoleDataSpan roleDataSpan) const
    self.uglySide.call(
        'ritual_ZNK11QRangeModel9multiDataERK11QModelIndex18QModelRoleDataS'
        'pan',
        self._valueOf(index), self._valueOf(roleDataSpan),
    )

  @overload(int)
  @overload(int, Qt.SortOrder)
  def sort(
      self,
      column: int,
      order: Qt.SortOrder = Qt.SortOrder.AscendingOrder,
  ) -> None:
    """
    Calls Qt's 'void QRangeModel::sort(int column, Qt::SortOrder order)'.

    Qt's own words: https://doc.qt.io/qt-6/qrangemodel.html#sort

    Parameters
    ----------

    column : int
      Passed on as it is.

    order : Qt.SortOrder
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.SortOrder.AscendingOrder.
    """
    #  void QRangeModel::sort(int column, Qt::SortOrder order)
    self.uglySide.call(
        'ritual_ZN11QRangeModel4sortEiN2Qt9SortOrderE', column, order.value,
    )

  def resetSortCollator(self) -> None:
    """
    Calls Qt's 'void QRangeModel::resetSortCollator()'.

    Qt's own words: https://doc.qt.io/qt-6/qrangemodel.html#resetSortCollator
    """
    #  void QRangeModel::resetSortCollator()
    self.uglySide.call('ritual_ZN11QRangeModel17resetSortCollatorEv')

  def resetSortRole(self) -> None:
    """
    Calls Qt's 'void QRangeModel::resetSortRole()'.

    Qt's own words: https://doc.qt.io/qt-6/qrangemodel.html#resetSortRole
    """
    #  void QRangeModel::resetSortRole()
    self.uglySide.call('ritual_ZN11QRangeModel13resetSortRoleEv')

  def resetSupportedDragActions(self) -> None:
    """
    Calls Qt's 'void QRangeModel::resetSupportedDragActions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrangemodel.html#resetSupportedDragActions
    """
    #  void QRangeModel::resetSupportedDragActions()
    self.uglySide.call('ritual_ZN11QRangeModel25resetSupportedDragActionsEv')

  def resetSupportedDropActions(self) -> None:
    """
    Calls Qt's 'void QRangeModel::resetSupportedDropActions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrangemodel.html#resetSupportedDropActions
    """
    #  void QRangeModel::resetSupportedDropActions()
    self.uglySide.call('ritual_ZN11QRangeModel25resetSupportedDropActionsEv')
