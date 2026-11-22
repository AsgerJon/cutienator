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
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from . import Qt, QHash, QList, QMap, QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QByteArray, QMetaObject, QMimeData, QModelIndex
  from . import QModelRoleDataSpan, QSize, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMimeData = WAIT['QMimeData']
  QModelIndex = WAIT['QModelIndex']
  QModelRoleDataSpan = WAIT['QModelRoleDataSpan']
  QVariant = WAIT['QVariant']

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
  can call so far, 47 names in all: 'metaObject', 'tr', 'hasIndex', 'index',
  'parent', 'sibling', 'rowCount', 'columnCount', 'hasChildren', 'data',
  'setData', 'headerData', 'setHeaderData', 'itemData', 'setItemData',
  'clearItemData', 'mimeTypes', 'mimeData', 'canDropMimeData',
  'dropMimeData', 'supportedDropActions', 'supportedDragActions',
  'insertRows', 'insertColumns', 'removeRows', 'removeColumns', 'moveRows',
  'moveColumns', 'insertRow', 'insertColumn', 'removeRow', 'removeColumn',
  'moveRow', 'moveColumn', 'fetchMore', 'canFetchMore', 'flags', 'sort',
  'buddy', 'match', 'span', 'roleNames', 'checkIndex', 'multiData', 'submit',
  'revert', 'resetInternalData'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAbstractItemModel::~QAbstractItemModel()': the destructor: Python
    never removes a C++ QAbstractItemModel.

  What has no ritual
  ------------------

  52 of the 100 functions Qt declares: 24 protected; 18 a signal; 4 private;
  2 takes or gives a type that cannot be passed yet; 2 forbidden; 1 a
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

  #  The enums Qt writes inside QAbstractItemModel, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class CheckIndexOption(CuteFlags, scoped=True):
    """
    The flags enum 'QAbstractItemModel::CheckIndexOption' of Qt, with the 4
    names Qt gives in it. Qt names the type of its combinations
    'QAbstractItemModel::CheckIndexOptions'. C++ keeps these names inside the
    enum, so the class that holds the enum does not have them.
    """

    NoOption = 0x0
    IndexIsValid = 0x1
    DoNotUseParent = 0x2
    ParentIsInvalid = 0x4

  CheckIndexOptions = CheckIndexOption

  class LayoutChangeHint(CuteNum):
    """
    The enum 'QAbstractItemModel::LayoutChangeHint' of Qt, with the 3 names
    Qt gives in it.
    """

    NoLayoutChangeHint = Kee[int](0)
    VerticalSortHint = Kee[int](1)
    HorizontalSortHint = Kee[int](2)

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

  #  A C++ QAbstractItemModel Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractItemModel'

  #  The functions Qt calls itself that QAbstractItemModel is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'itemData': (
          'QMap<int, QVariant> QAbstractItemModel::itemData(const '
          'QModelIndex &) const',
      ),
      'setItemData': (
          'bool QAbstractItemModel::setItemData(const QModelIndex &, const '
          'QMap<int, QVariant> &)',
      ),
      'mimeTypes': (
          'QStringList QAbstractItemModel::mimeTypes() const',
      ),
      'mimeData': (
          'QMimeData *QAbstractItemModel::mimeData(const QModelIndexList '
          '&) const',
      ),
      'match': (
          'QModelIndexList QAbstractItemModel::match(const QModelIndex &, '
          'int, const QVariant &, int, Qt::MatchFlags) const',
      ),
      'roleNames': (
          'QHash<int, QByteArray> QAbstractItemModel::roleNames() const',
      ),
  }

  #  The functions Qt calls itself that QAbstractItemModel is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'index': (
          ('_ZNK18QAbstractItemModel5indexEiiRK11QModelIndex',
           ('address', 'value', 'QtCore:QModelIndex'),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('address', 'value', 'QtCore:QModelIndex'),
           )),
      ),
      'parent': (
          ('_ZNK18QAbstractItemModel6parentERK11QModelIndex',
           ('address', 'value', 'QtCore:QModelIndex'),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
           )),
      ),
      'sibling': (
          ('_ZNK18QAbstractItemModel7siblingEiiRK11QModelIndex',
           ('address', 'value', 'QtCore:QModelIndex'),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('address', 'value', 'QtCore:QModelIndex'),
           )),
      ),
      'rowCount': (
          ('_ZNK18QAbstractItemModel8rowCountERK11QModelIndex',
           ('int', 'number', ''),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
           )),
      ),
      'columnCount': (
          ('_ZNK18QAbstractItemModel11columnCountERK11QModelIndex',
           ('int', 'number', ''),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
           )),
      ),
      'hasChildren': (
          ('_ZNK18QAbstractItemModel11hasChildrenERK11QModelIndex',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
           )),
      ),
      'data': (
          ('_ZNK18QAbstractItemModel4dataERK11QModelIndexi',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
               ('int', 'number', ''),
           )),
      ),
      'setData': (
          ('_ZN18QAbstractItemModel7setDataERK11QModelIndexRK8QVarianti',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
               ('address', 'value', 'QtCore:QVariant'),
               ('int', 'number', ''),
           )),
      ),
      'headerData': (
          ('_ZNK18QAbstractItemModel10headerDataEiN2Qt11OrientationEi',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('int', 'number', ''),
               ('int', 'enum', 'QtCore:Qt.Orientation'),
               ('int', 'number', ''),
           )),
      ),
      'setHeaderData': (
          ('_ZN18QAbstractItemModel13setHeaderDataEiN2Qt11OrientationERK8QV'
           'arianti',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
               ('int', 'enum', 'QtCore:Qt.Orientation'),
               ('address', 'value', 'QtCore:QVariant'),
               ('int', 'number', ''),
           )),
      ),
      'clearItemData': (
          ('_ZN18QAbstractItemModel13clearItemDataERK11QModelIndex',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
           )),
      ),
      'canDropMimeData': (
          ('_ZNK18QAbstractItemModel15canDropMimeDataEPK9QMimeDataN2Qt10Dro'
           'pActionEiiRK11QModelIndex',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtCore:QMimeData'),
               ('int', 'enum', 'QtCore:Qt.DropAction'),
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('address', 'value', 'QtCore:QModelIndex'),
           )),
      ),
      'dropMimeData': (
          ('_ZN18QAbstractItemModel12dropMimeDataEPK9QMimeDataN2Qt10DropAct'
           'ionEiiRK11QModelIndex',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtCore:QMimeData'),
               ('int', 'enum', 'QtCore:Qt.DropAction'),
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('address', 'value', 'QtCore:QModelIndex'),
           )),
      ),
      'supportedDropActions': (
          ('_ZNK18QAbstractItemModel20supportedDropActionsEv',
           ('int', 'flags', 'QtCore:Qt.DropAction'),
           ()),
      ),
      'supportedDragActions': (
          ('_ZNK18QAbstractItemModel20supportedDragActionsEv',
           ('int', 'flags', 'QtCore:Qt.DropAction'),
           ()),
      ),
      'insertRows': (
          ('_ZN18QAbstractItemModel10insertRowsEiiRK11QModelIndex',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('address', 'value', 'QtCore:QModelIndex'),
           )),
      ),
      'insertColumns': (
          ('_ZN18QAbstractItemModel13insertColumnsEiiRK11QModelIndex',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('address', 'value', 'QtCore:QModelIndex'),
           )),
      ),
      'removeRows': (
          ('_ZN18QAbstractItemModel10removeRowsEiiRK11QModelIndex',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('address', 'value', 'QtCore:QModelIndex'),
           )),
      ),
      'removeColumns': (
          ('_ZN18QAbstractItemModel13removeColumnsEiiRK11QModelIndex',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('address', 'value', 'QtCore:QModelIndex'),
           )),
      ),
      'moveRows': (
          ('_ZN18QAbstractItemModel8moveRowsERK11QModelIndexiiS2_i',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('address', 'value', 'QtCore:QModelIndex'),
               ('int', 'number', ''),
           )),
      ),
      'moveColumns': (
          ('_ZN18QAbstractItemModel11moveColumnsERK11QModelIndexiiS2_i',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('address', 'value', 'QtCore:QModelIndex'),
               ('int', 'number', ''),
           )),
      ),
      'fetchMore': (
          ('_ZN18QAbstractItemModel9fetchMoreERK11QModelIndex',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
           )),
      ),
      'canFetchMore': (
          ('_ZNK18QAbstractItemModel12canFetchMoreERK11QModelIndex',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
           )),
      ),
      'flags': (
          ('_ZNK18QAbstractItemModel5flagsERK11QModelIndex',
           ('int', 'flags', 'QtCore:Qt.ItemFlag'),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
           )),
      ),
      'sort': (
          ('_ZN18QAbstractItemModel4sortEiN2Qt9SortOrderE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'enum', 'QtCore:Qt.SortOrder'),
           )),
      ),
      'buddy': (
          ('_ZNK18QAbstractItemModel5buddyERK11QModelIndex',
           ('address', 'value', 'QtCore:QModelIndex'),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
           )),
      ),
      'span': (
          ('_ZNK18QAbstractItemModel4spanERK11QModelIndex',
           ('address', 'value', 'QtCore:QSize'),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
           )),
      ),
      'multiData': (
          ('_ZNK18QAbstractItemModel9multiDataERK11QModelIndex18QModelRoleD'
           'ataSpan',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
               ('address', 'value', 'QtCore:QModelRoleDataSpan'),
           )),
      ),
      'submit': (
          ('_ZN18QAbstractItemModel6submitEv',
           ('bool', 'number', ''),
           ()),
      ),
      'revert': (
          ('_ZN18QAbstractItemModel6revertEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'resetInternalData': (
          ('_ZN18QAbstractItemModel17resetInternalDataEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

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
    from . import QMetaObject
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
      from . import QModelIndex
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
      from . import QModelIndex
      parent = QModelIndex()
    address = self.uglySide.call(
        'ritual_ZNK18QAbstractItemModel5indexEiiRK11QModelIndex',
        row, column, self._valueOf(parent),
    )
    from . import QModelIndex
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
    from . import QModelIndex
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
    ritual = 'ritual_ZNK18QAbstractItemModel7siblingEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QAbstractItemModel7siblingEiiRK11QModelIndex'
    address = self.uglySide.call(ritual, row, column, self._valueOf(idx))
    from . import QModelIndex
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
      from . import QModelIndex
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
      from . import QModelIndex
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
      from . import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK18QAbstractItemModel11hasChildrenERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18QAbstractItemModel11hasChildrenERK11QModelIndex')
    return self.uglySide.call(ritual, self._valueOf(parent))

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
    from . import QVariant
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
    ritual = (
        'ritual_ZNK18QAbstractItemModel10headerDataEiN2Qt11OrientationEi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18QAbstractItemModel10headerDataEiN2Qt11Orientatio'
          'nEi')
    address = self.uglySide.call(ritual, section, orientation.value, role)
    from . import QVariant
    return QVariant._cuteOwning(address)

  @overload(QModelIndex)
  def itemData(self, index: QModelIndex) -> QMap[int, QVariant]:
    """
    Calls Qt's 'QMap<int, QVariant> QAbstractItemModel::itemData(const
    QModelIndex &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemmodel.html#itemData

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QMap[int, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QMap<int, QVariant> QAbstractItemModel::itemData(const QModelIndex
    #      &index) const
    address = self.uglySide.call(
        'ritual_ZNK18QAbstractItemModel8itemDataERK11QModelIndex',
        self._valueOf(index),
    )
    from . import QVariant
    return QMap[int, QVariant]._cuteOwning(address)

  def mimeTypes(self) -> QStringList:
    """
    Calls Qt's 'QStringList QAbstractItemModel::mimeTypes() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemmodel.html#mimeTypes

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QAbstractItemModel::mimeTypes() const
    address = self.uglySide.call(
        'ritual_ZNK18QAbstractItemModel9mimeTypesEv',
    )
    return QStringList._cuteOwning(address)

  @overload(QList[QModelIndex])
  def mimeData(self, indexes: QList[QModelIndex]) -> Optional[QMimeData]:
    """
    Calls Qt's 'QMimeData *QAbstractItemModel::mimeData(const QModelIndexList
    &indexes) const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemmodel.html#mimeData

    Parameters
    ----------

    indexes : QList[QModelIndex]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    Optional[QMimeData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMimeData *QAbstractItemModel::mimeData(const QModelIndexList
    #      &indexes) const
    address = self.uglySide.call(
        'ritual_ZNK18QAbstractItemModel8mimeDataERK5QListI11QModelIndexE',
        self._valueOf(indexes),
    )
    from . import QMimeData
    return QMimeData._cuteAt(address)

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
    ritual = (
        'ritual_ZNK18QAbstractItemModel15canDropMimeDataEPK9QMimeDataN2Qt10'
        'DropActionEiiRK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18QAbstractItemModel15canDropMimeDataEPK9QMimeData'
          'N2Qt10DropActionEiiRK11QModelIndex')
    return self.uglySide.call(
        ritual,
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
    ritual = 'ritual_ZNK18QAbstractItemModel20supportedDropActionsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QAbstractItemModel20supportedDropActionsEv'
    return Qt.DropActions(self.uglySide.call(ritual))

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
    ritual = 'ritual_ZNK18QAbstractItemModel20supportedDragActionsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QAbstractItemModel20supportedDragActionsEv'
    return Qt.DropActions(self.uglySide.call(ritual))

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
    ritual = 'ritual_ZNK18QAbstractItemModel12canFetchMoreERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18QAbstractItemModel12canFetchMoreERK11QModelIndex')
    return self.uglySide.call(ritual, self._valueOf(parent))

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
    ritual = 'ritual_ZNK18QAbstractItemModel5flagsERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QAbstractItemModel5flagsERK11QModelIndex'
    return Qt.ItemFlags(self.uglySide.call(ritual, self._valueOf(index)))

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
    ritual = 'ritual_ZNK18QAbstractItemModel5buddyERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QAbstractItemModel5buddyERK11QModelIndex'
    address = self.uglySide.call(ritual, self._valueOf(index))
    from . import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex, int, QVariant)
  @overload(QModelIndex, int, QVariant, int)
  @overload(QModelIndex, int, QVariant, int, Qt.MatchFlags)
  def match(
      self,
      start: QModelIndex,
      role: int,
      value: QVariant,
      hits: int = 1,
      flags: Qt.MatchFlags = (
          Qt.MatchFlags.MatchStartsWith | Qt.MatchFlags.MatchWrap),
  ) -> QList[QModelIndex]:
    """
    Calls Qt's 'QModelIndexList QAbstractItemModel::match(const QModelIndex
    &start, int role, const QVariant &value, int hits, Qt::MatchFlags flags)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemmodel.html#match

    Parameters
    ----------

    start : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    role : int
      Passed on as it is.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    hits : int
      Passed on as it is. May be left out, as in Qt: it is then 1.

    flags : Qt.MatchFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.MatchFlags.MatchStartsWith | Qt.MatchFlags.MatchWrap.

    Returns
    -------

    QList[QModelIndex]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QModelIndexList QAbstractItemModel::match(const QModelIndex &start,
    #      int role, const QVariant &value, int hits, Qt::MatchFlags flags)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18QAbstractItemModel5matchERK11QModelIndexiRK8QVarianti6'
        'QFlagsIN2Qt9MatchFlagEE',
        self._valueOf(start), role, self._valueOf(value), hits, flags.value,
    )
    from . import QModelIndex
    return QList[QModelIndex]._cuteOwning(address)

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
    ritual = 'ritual_ZNK18QAbstractItemModel4spanERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QAbstractItemModel4spanERK11QModelIndex'
    address = self.uglySide.call(ritual, self._valueOf(index))
    from . import QSize
    return QSize._cuteOwning(address)

  def roleNames(self) -> QHash[int, QByteArray]:
    """
    Calls Qt's 'QHash<int, QByteArray> QAbstractItemModel::roleNames()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemmodel.html#roleNames

    Returns
    -------

    QHash[int, QByteArray]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QHash<int, QByteArray> QAbstractItemModel::roleNames() const
    address = self.uglySide.call(
        'ritual_ZNK18QAbstractItemModel9roleNamesEv',
    )
    from . import QByteArray
    return QHash[int, QByteArray]._cuteOwning(address)

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
    ritual = (
        'ritual_ZN18QAbstractItemModel7setDataERK11QModelIndexRK8QVarianti')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QAbstractItemModel7setDataERK11QModelIndexRK8QVar'
          'ianti')
    return self.uglySide.call(
        ritual, self._valueOf(index), self._valueOf(value), role,
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
    ritual = (
        'ritual_ZN18QAbstractItemModel13setHeaderDataEiN2Qt11OrientationERK'
        '8QVarianti')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QAbstractItemModel13setHeaderDataEiN2Qt11Orientat'
          'ionERK8QVarianti')
    return self.uglySide.call(
        ritual, section, orientation.value, self._valueOf(value), role,
    )

  @overload(QModelIndex, QMap[int, QVariant])
  def setItemData(
      self,
      index: QModelIndex,
      roles: QMap[int, QVariant],
  ) -> bool:
    """
    Calls Qt's 'bool QAbstractItemModel::setItemData(const QModelIndex
    &index, const QMap<int, QVariant> &roles)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodel.html#setItemData

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    roles : QMap[int, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  bool QAbstractItemModel::setItemData(const QModelIndex &index, const
    #      QMap<int, QVariant> &roles)
    return self.uglySide.call(
        'ritual_ZN18QAbstractItemModel11setItemDataERK11QModelIndexRK4QMapI'
        'i8QVariantE',
        self._valueOf(index), self._valueOf(roles),
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
    ritual = 'ritual_ZN18QAbstractItemModel13clearItemDataERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QAbstractItemModel13clearItemDataERK11QModelIndex')
    return self.uglySide.call(ritual, self._valueOf(index))

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
    ritual = (
        'ritual_ZN18QAbstractItemModel12dropMimeDataEPK9QMimeDataN2Qt10Drop'
        'ActionEiiRK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QAbstractItemModel12dropMimeDataEPK9QMimeDataN2Qt'
          '10DropActionEiiRK11QModelIndex')
    return self.uglySide.call(
        ritual,
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
      from . import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZN18QAbstractItemModel10insertRowsEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QAbstractItemModel10insertRowsEiiRK11QModelIndex')
    return self.uglySide.call(ritual, row, count, self._valueOf(parent))

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
      from . import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZN18QAbstractItemModel13insertColumnsEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QAbstractItemModel13insertColumnsEiiRK11QModelInd'
          'ex')
    return self.uglySide.call(ritual, column, count, self._valueOf(parent))

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
      from . import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZN18QAbstractItemModel10removeRowsEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QAbstractItemModel10removeRowsEiiRK11QModelIndex')
    return self.uglySide.call(ritual, row, count, self._valueOf(parent))

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
      from . import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZN18QAbstractItemModel13removeColumnsEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QAbstractItemModel13removeColumnsEiiRK11QModelInd'
          'ex')
    return self.uglySide.call(ritual, column, count, self._valueOf(parent))

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
    ritual = 'ritual_ZN18QAbstractItemModel8moveRowsERK11QModelIndexiiS2_i'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QAbstractItemModel8moveRowsERK11QModelIndexiiS2_i')
    return self.uglySide.call(
        ritual,
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
    ritual = (
        'ritual_ZN18QAbstractItemModel11moveColumnsERK11QModelIndexiiS2_i')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QAbstractItemModel11moveColumnsERK11QModelIndexii'
          'S2_i')
    return self.uglySide.call(
        ritual,
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
      from . import QModelIndex
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
      from . import QModelIndex
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
      from . import QModelIndex
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
      from . import QModelIndex
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
    ritual = 'ritual_ZN18QAbstractItemModel9fetchMoreERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QAbstractItemModel9fetchMoreERK11QModelIndex'
    self.uglySide.call(ritual, self._valueOf(parent))

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
    ritual = 'ritual_ZN18QAbstractItemModel4sortEiN2Qt9SortOrderE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QAbstractItemModel4sortEiN2Qt9SortOrderE'
    self.uglySide.call(ritual, column, order.value)

  @overload(QModelIndex, QModelRoleDataSpan)
  def multiData(
      self,
      index: QModelIndex,
      roleDataSpan: QModelRoleDataSpan,
  ) -> None:
    """
    Calls Qt's 'void QAbstractItemModel::multiData(const QModelIndex &index,
    QModelRoleDataSpan roleDataSpan) const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemmodel.html#multiData

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    roleDataSpan : QModelRoleDataSpan
      Passed on as a value: Qt reads the C++ QModelRoleDataSpan, which stays
      Python's own.
    """
    #  void QAbstractItemModel::multiData(const QModelIndex &index,
    #      QModelRoleDataSpan roleDataSpan) const
    ritual = (
        'ritual_ZNK18QAbstractItemModel9multiDataERK11QModelIndex18QModelRo'
        'leDataSpan')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18QAbstractItemModel9multiDataERK11QModelIndex18QM'
          'odelRoleDataSpan')
    self.uglySide.call(
        ritual, self._valueOf(index), self._valueOf(roleDataSpan),
    )

  def submit(self) -> bool:
    """
    Calls Qt's 'bool QAbstractItemModel::submit()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemmodel.html#submit
    """
    #  bool QAbstractItemModel::submit()
    ritual = 'ritual_ZN18QAbstractItemModel6submitEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QAbstractItemModel6submitEv'
    return self.uglySide.call(ritual)

  def revert(self) -> None:
    """
    Calls Qt's 'void QAbstractItemModel::revert()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemmodel.html#revert
    """
    #  void QAbstractItemModel::revert()
    ritual = 'ritual_ZN18QAbstractItemModel6revertEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QAbstractItemModel6revertEv'
    self.uglySide.call(ritual)

  def resetInternalData(self) -> None:
    """
    Calls Qt's 'void QAbstractItemModel::resetInternalData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemmodel.html#resetInternalData
    """
    #  void QAbstractItemModel::resetInternalData()
    self.uglySide.call(
        'ritual_own_ZN18QAbstractItemModel17resetInternalDataEv',
    )


#  Qt's 'QList<QAbstractItemModel *>': the list of QAbstractItemModel, which
#  'QList[QAbstractItemModel]' gives. It is made here, so that there is one
#  as soon as there can be a QAbstractItemModel.
QList.createKind(
    QAbstractItemModel, 'address',
    make='ritual_list_make_QAbstractItemModel_ptr',
    add='ritual_list_add_QAbstractItemModel_ptr',
    size='ritual_list_size_QAbstractItemModel_ptr',
    at='ritual_list_at_QAbstractItemModel_ptr',
    drop='ritual_list_drop_QAbstractItemModel_ptr',
)
