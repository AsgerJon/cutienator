"""
QQuickFolderListModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsFolderListModel/6.12.0/QtLabsFolderListModel/private/qquickfolderlistmodel_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickFolderListModel to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QHash, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QMetaObject, QModelIndex, QObject, QUrl
  from ..QtCore import QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']
  QObject = WAIT['QObject']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickFolderListModel(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickFolderListModel: a plain Python object standing
  in front of one C++ QQuickFolderListModel.

  What exists
  -----------

  Every function of Qt's QQuickFolderListModel that has a ritual and that
  Python can call so far, 63 names in all: 'metaObject', 'tr', 'rowCount',
  'index', 'data', 'roleNames', 'count', 'folder', 'setFolder', 'rootFolder',
  'setRootFolder', 'parentFolder', 'nameFilters', 'setNameFilters',
  'sortField', 'setSortField', 'sortReversed', 'setSortReversed',
  'showFiles', 'setShowFiles', 'showDirs', 'setShowDirs', 'showDirsFirst',
  'setShowDirsFirst', 'showDotAndDotDot', 'setShowDotAndDotDot', 'showDot',
  'setShowDot', 'showDotDot', 'setShowDotDot', 'showHidden', 'setShowHidden',
  'showOnlyReadable', 'setShowOnlyReadable', 'caseSensitive',
  'setCaseSensitive', 'status', 'sortCaseSensitive', 'setSortCaseSensitive',
  'isFolder', 'get', 'indexOf', 'classBegin', 'componentComplete',
  'roleFromString', 'folderChanged', 'rowCountChanged', 'rootFolderChanged',
  'nameFilterChanged', 'sortFieldChanged', 'sortReversedChanged',
  'showFilesChanged', 'showDirsChanged', 'showDirsFirstChanged',
  'showDotAndDotDotChanged', 'showDotChanged', 'showDotDotChanged',
  'showHiddenChanged', 'showOnlyReadableChanged', 'caseSensitiveChanged',
  'sortCaseSensitiveChanged', 'countChanged', 'statusChanged'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickFolderListModel::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickFolderListModel::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickFolderListModel::~QQuickFolderListModel()': the destructor:
    Python never removes a C++ QQuickFolderListModel.
  - Qt's 'QQuickFolderListModelPrivate *QQuickFolderListModel::d_func()':
    gives 'QQuickFolderListModelPrivate', which has no cute class yet.
  - Qt's 'const QQuickFolderListModelPrivate *QQuickFolderListModel::d_func()
    const': gives 'QQuickFolderListModelPrivate', which has no cute class
    yet.

  What has no ritual
  ------------------

  4 of the 73 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickFolderListModel is created at the first use, not by
    'QQuickFolderListModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickFolderListModel.
  - Qt tells when it has removed the C++ QQuickFolderListModel. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickFolderListModel, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class Roles(CuteNum):
    """
    The enum 'QQuickFolderListModel::Roles' of Qt, with the 9 names Qt gives
    in it.
    """

    FileNameRole = Kee[int](257)
    FilePathRole = Kee[int](258)
    FileBaseNameRole = Kee[int](259)
    FileSuffixRole = Kee[int](260)
    FileSizeRole = Kee[int](261)
    FileLastModifiedRole = Kee[int](262)
    FileLastReadRole = Kee[int](263)
    FileIsDirRole = Kee[int](264)
    FileUrlRole = Kee[int](265)

  class SortField(CuteNum):
    """
    The enum 'QQuickFolderListModel::SortField' of Qt, with the 5 names Qt
    gives in it.
    """

    Unsorted = Kee[int](0)
    Name = Kee[int](1)
    Time = Kee[int](2)
    Size = Kee[int](3)
    Type = Kee[int](4)

  class Status(CuteNum):
    """
    The enum 'QQuickFolderListModel::Status' of Qt, with the 3 names Qt gives
    in it.
    """

    Null = Kee[int](0)
    Ready = Kee[int](1)
    Loading = Kee[int](2)

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
    Calls Qt's 'QString QQuickFolderListModel::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfolderlistmodel.html#tr

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
    #  QString QQuickFolderListModel::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QQuickFolderListModel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickFolderListModel'

  #  A C++ QQuickFolderListModel Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickFolderListModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickFolderListModel::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickFolderListModel::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickFolderListModel10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload()
  @overload(QModelIndex)
  def rowCount(self, parent: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QQuickFolderListModel::rowCount(const QModelIndex
    &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#rowCount

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QQuickFolderListModel::rowCount(const QModelIndex &parent) const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK21QQuickFolderListModel8rowCountERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QQuickFolderListModel8rowCountERK11QModelIndex')
    return self.uglySide.call(ritual, self._valueOf(parent))

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
    Calls Qt's 'QModelIndex QQuickFolderListModel::index(int row, int column,
    const QModelIndex &parent) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfolderlistmodel.html#index

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
    #  QModelIndex QQuickFolderListModel::index(int row, int column, const
    #      QModelIndex &parent) const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK21QQuickFolderListModel5indexEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QQuickFolderListModel5indexEiiRK11QModelIndex')
    address = self.uglySide.call(ritual, row, column, self._valueOf(parent))
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  @overload(QModelIndex, int)
  def data(self, index: QModelIndex, role: int = 0) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickFolderListModel::data(const QModelIndex
    &index, int role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfolderlistmodel.html#data

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
    #  QVariant QQuickFolderListModel::data(const QModelIndex &index, int
    #      role) const
    ritual = 'ritual_ZNK21QQuickFolderListModel4dataERK11QModelIndexi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QQuickFolderListModel4dataERK11QModelIndexi'
    address = self.uglySide.call(ritual, self._valueOf(index), role)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def roleNames(self) -> QHash[int, QByteArray]:
    """
    Calls Qt's 'QHash<int, QByteArray> QQuickFolderListModel::roleNames()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#roleNames

    Returns
    -------

    QHash[int, QByteArray]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QHash<int, QByteArray> QQuickFolderListModel::roleNames() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickFolderListModel9roleNamesEv',
    )
    from ..QtCore import QByteArray
    return QHash[int, QByteArray]._cuteOwning(address)

  def count(self) -> int:
    """
    Calls Qt's 'int QQuickFolderListModel::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfolderlistmodel.html#count
    """
    #  int QQuickFolderListModel::count() const
    return self.uglySide.call('ritual_ZNK21QQuickFolderListModel5countEv')

  def folder(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickFolderListModel::folder() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfolderlistmodel.html#folder

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickFolderListModel::folder() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickFolderListModel6folderEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def rootFolder(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickFolderListModel::rootFolder() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#rootFolder

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickFolderListModel::rootFolder() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickFolderListModel10rootFolderEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def parentFolder(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickFolderListModel::parentFolder() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#parentFolder

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickFolderListModel::parentFolder() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickFolderListModel12parentFolderEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def nameFilters(self) -> QStringList:
    """
    Calls Qt's 'QStringList QQuickFolderListModel::nameFilters() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#nameFilters

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQuickFolderListModel::nameFilters() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickFolderListModel11nameFiltersEv',
    )
    return QStringList._cuteOwning(address)

  def sortField(self) -> SortField:
    """
    Calls Qt's 'SortField QQuickFolderListModel::sortField() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#sortField

    Returns
    -------

    SortField
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SortField(number)' gives.
    """
    #  SortField QQuickFolderListModel::sortField() const
    return QQuickFolderListModel.SortField(self.uglySide.call(
        'ritual_ZNK21QQuickFolderListModel9sortFieldEv',
    ))

  def sortReversed(self) -> bool:
    """
    Calls Qt's 'bool QQuickFolderListModel::sortReversed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#sortReversed
    """
    #  bool QQuickFolderListModel::sortReversed() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickFolderListModel12sortReversedEv',
    )

  def showFiles(self) -> bool:
    """
    Calls Qt's 'bool QQuickFolderListModel::showFiles() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#showFiles
    """
    #  bool QQuickFolderListModel::showFiles() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickFolderListModel9showFilesEv',
    )

  def showDirs(self) -> bool:
    """
    Calls Qt's 'bool QQuickFolderListModel::showDirs() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#showDirs
    """
    #  bool QQuickFolderListModel::showDirs() const
    return self.uglySide.call('ritual_ZNK21QQuickFolderListModel8showDirsEv')

  def showDirsFirst(self) -> bool:
    """
    Calls Qt's 'bool QQuickFolderListModel::showDirsFirst() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#showDirsFirst
    """
    #  bool QQuickFolderListModel::showDirsFirst() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickFolderListModel13showDirsFirstEv',
    )

  def showDotAndDotDot(self) -> bool:
    """
    Calls Qt's 'bool QQuickFolderListModel::showDotAndDotDot() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#showDotAndDotDot
    """
    #  bool QQuickFolderListModel::showDotAndDotDot() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickFolderListModel16showDotAndDotDotEv',
    )

  def showDot(self) -> bool:
    """
    Calls Qt's 'bool QQuickFolderListModel::showDot() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfolderlistmodel.html#showDot
    """
    #  bool QQuickFolderListModel::showDot() const
    return self.uglySide.call('ritual_ZNK21QQuickFolderListModel7showDotEv')

  def showDotDot(self) -> bool:
    """
    Calls Qt's 'bool QQuickFolderListModel::showDotDot() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#showDotDot
    """
    #  bool QQuickFolderListModel::showDotDot() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickFolderListModel10showDotDotEv',
    )

  def showHidden(self) -> bool:
    """
    Calls Qt's 'bool QQuickFolderListModel::showHidden() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#showHidden
    """
    #  bool QQuickFolderListModel::showHidden() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickFolderListModel10showHiddenEv',
    )

  def showOnlyReadable(self) -> bool:
    """
    Calls Qt's 'bool QQuickFolderListModel::showOnlyReadable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#showOnlyReadable
    """
    #  bool QQuickFolderListModel::showOnlyReadable() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickFolderListModel16showOnlyReadableEv',
    )

  def caseSensitive(self) -> bool:
    """
    Calls Qt's 'bool QQuickFolderListModel::caseSensitive() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#caseSensitive
    """
    #  bool QQuickFolderListModel::caseSensitive() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickFolderListModel13caseSensitiveEv',
    )

  def status(self) -> Status:
    """
    Calls Qt's 'Status QQuickFolderListModel::status() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfolderlistmodel.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status QQuickFolderListModel::status() const
    return QQuickFolderListModel.Status(self.uglySide.call(
        'ritual_ZNK21QQuickFolderListModel6statusEv',
    ))

  def sortCaseSensitive(self) -> bool:
    """
    Calls Qt's 'bool QQuickFolderListModel::sortCaseSensitive() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#sortCaseSensitive
    """
    #  bool QQuickFolderListModel::sortCaseSensitive() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickFolderListModel17sortCaseSensitiveEv',
    )

  @overload(int)
  def isFolder(self, index: int) -> bool:
    """
    Calls Qt's 'bool QQuickFolderListModel::isFolder(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#isFolder

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QQuickFolderListModel::isFolder(int index) const
    return self.uglySide.call(
        'ritual_ZNK21QQuickFolderListModel8isFolderEi', index,
    )

  @overload(int, str)
  def get(self, idx: int, property: str) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickFolderListModel::get(int idx, const QString
    &property) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfolderlistmodel.html#get

    Parameters
    ----------

    idx : int
      Passed on as it is.

    property : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickFolderListModel::get(int idx, const QString &property)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickFolderListModel3getEiRK7QString', idx, property,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QUrl)
  def indexOf(self, file: QUrl) -> int:
    """
    Calls Qt's 'int QQuickFolderListModel::indexOf(const QUrl &file) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfolderlistmodel.html#indexOf

    Parameters
    ----------

    file : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  int QQuickFolderListModel::indexOf(const QUrl &file) const
    return self.uglySide.call(
        'ritual_ZNK21QQuickFolderListModel7indexOfERK4QUrl',
        self._valueOf(file),
    )

  @overload(str)
  def roleFromString(self, roleName: str) -> int:
    """
    Calls Qt's 'int QQuickFolderListModel::roleFromString(const QString
    &roleName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#roleFromString

    Parameters
    ----------

    roleName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QQuickFolderListModel::roleFromString(const QString &roleName)
    #      const
    return self.uglySide.call(
        'ritual_ZNK21QQuickFolderListModel14roleFromStringERK7QString',
        roleName,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setFolder(self, folder: QUrl) -> None:
    """
    Calls Qt's 'void QQuickFolderListModel::setFolder(const QUrl &folder)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#setFolder

    Parameters
    ----------

    folder : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickFolderListModel::setFolder(const QUrl &folder)
    self.uglySide.call(
        'ritual_ZN21QQuickFolderListModel9setFolderERK4QUrl',
        self._valueOf(folder),
    )

  @overload(QUrl)
  def setRootFolder(self, path: QUrl) -> None:
    """
    Calls Qt's 'void QQuickFolderListModel::setRootFolder(const QUrl &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#setRootFolder

    Parameters
    ----------

    path : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickFolderListModel::setRootFolder(const QUrl &path)
    self.uglySide.call(
        'ritual_ZN21QQuickFolderListModel13setRootFolderERK4QUrl',
        self._valueOf(path),
    )

  @overload(QStringList)
  def setNameFilters(self, filters: QStringList) -> None:
    """
    Calls Qt's 'void QQuickFolderListModel::setNameFilters(const QStringList
    &filters)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#setNameFilters

    Parameters
    ----------

    filters : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQuickFolderListModel::setNameFilters(const QStringList &filters)
    self.uglySide.call(
        'ritual_ZN21QQuickFolderListModel14setNameFiltersERK5QListI7QString'
        'E',
        self._valueOf(filters),
    )

  @overload(SortField)
  def setSortField(self, field: SortField) -> None:
    """
    Calls Qt's 'void QQuickFolderListModel::setSortField(SortField field)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#setSortField

    Parameters
    ----------

    field : SortField
      Passed on as its number.
    """
    #  void QQuickFolderListModel::setSortField(SortField field)
    self.uglySide.call(
        'ritual_ZN21QQuickFolderListModel12setSortFieldENS_9SortFieldE',
        field.value,
    )

  @overload(bool)
  def setSortReversed(self, rev: bool) -> None:
    """
    Calls Qt's 'void QQuickFolderListModel::setSortReversed(bool rev)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#setSortReversed

    Parameters
    ----------

    rev : bool
      Passed on as it is.
    """
    #  void QQuickFolderListModel::setSortReversed(bool rev)
    self.uglySide.call(
        'ritual_ZN21QQuickFolderListModel15setSortReversedEb', rev,
    )

  @overload(bool)
  def setShowFiles(self, showFiles: bool) -> None:
    """
    Calls Qt's 'void QQuickFolderListModel::setShowFiles(bool showFiles)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#setShowFiles

    Parameters
    ----------

    showFiles : bool
      Passed on as it is.
    """
    #  void QQuickFolderListModel::setShowFiles(bool showFiles)
    self.uglySide.call(
        'ritual_ZN21QQuickFolderListModel12setShowFilesEb', showFiles,
    )

  @overload(bool)
  def setShowDirs(self, showDirs: bool) -> None:
    """
    Calls Qt's 'void QQuickFolderListModel::setShowDirs(bool showDirs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#setShowDirs

    Parameters
    ----------

    showDirs : bool
      Passed on as it is.
    """
    #  void QQuickFolderListModel::setShowDirs(bool showDirs)
    self.uglySide.call(
        'ritual_ZN21QQuickFolderListModel11setShowDirsEb', showDirs,
    )

  @overload(bool)
  def setShowDirsFirst(self, showDirsFirst: bool) -> None:
    """
    Calls Qt's 'void QQuickFolderListModel::setShowDirsFirst(bool
    showDirsFirst)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#setShowDirsFirst

    Parameters
    ----------

    showDirsFirst : bool
      Passed on as it is.
    """
    #  void QQuickFolderListModel::setShowDirsFirst(bool showDirsFirst)
    self.uglySide.call(
        'ritual_ZN21QQuickFolderListModel16setShowDirsFirstEb',
        showDirsFirst,
    )

  @overload(bool)
  def setShowDotAndDotDot(self, on: bool) -> None:
    """
    Calls Qt's 'void QQuickFolderListModel::setShowDotAndDotDot(bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#setShowDotAndDotDot

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickFolderListModel::setShowDotAndDotDot(bool on)
    self.uglySide.call(
        'ritual_ZN21QQuickFolderListModel19setShowDotAndDotDotEb', on,
    )

  @overload(bool)
  def setShowDot(self, on: bool) -> None:
    """
    Calls Qt's 'void QQuickFolderListModel::setShowDot(bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#setShowDot

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickFolderListModel::setShowDot(bool on)
    self.uglySide.call('ritual_ZN21QQuickFolderListModel10setShowDotEb', on)

  @overload(bool)
  def setShowDotDot(self, on: bool) -> None:
    """
    Calls Qt's 'void QQuickFolderListModel::setShowDotDot(bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#setShowDotDot

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickFolderListModel::setShowDotDot(bool on)
    self.uglySide.call(
        'ritual_ZN21QQuickFolderListModel13setShowDotDotEb', on,
    )

  @overload(bool)
  def setShowHidden(self, on: bool) -> None:
    """
    Calls Qt's 'void QQuickFolderListModel::setShowHidden(bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#setShowHidden

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickFolderListModel::setShowHidden(bool on)
    self.uglySide.call(
        'ritual_ZN21QQuickFolderListModel13setShowHiddenEb', on,
    )

  @overload(bool)
  def setShowOnlyReadable(self, on: bool) -> None:
    """
    Calls Qt's 'void QQuickFolderListModel::setShowOnlyReadable(bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#setShowOnlyReadable

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickFolderListModel::setShowOnlyReadable(bool on)
    self.uglySide.call(
        'ritual_ZN21QQuickFolderListModel19setShowOnlyReadableEb', on,
    )

  @overload(bool)
  def setCaseSensitive(self, on: bool) -> None:
    """
    Calls Qt's 'void QQuickFolderListModel::setCaseSensitive(bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#setCaseSensitive

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickFolderListModel::setCaseSensitive(bool on)
    self.uglySide.call(
        'ritual_ZN21QQuickFolderListModel16setCaseSensitiveEb', on,
    )

  @overload(bool)
  def setSortCaseSensitive(self, on: bool) -> None:
    """
    Calls Qt's 'void QQuickFolderListModel::setSortCaseSensitive(bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#setSortCaseSensitive

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QQuickFolderListModel::setSortCaseSensitive(bool on)
    self.uglySide.call(
        'ritual_ZN21QQuickFolderListModel20setSortCaseSensitiveEb', on,
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
    Notes what was given, for Qt's
    'QQuickFolderListModel::QQuickFolderListModel(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#QQuickFolderListModel

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickFolderListModel::QQuickFolderListModel(QObject *parent)
    self._noteCreation(QQuickFolderListModel, lambda: Rituals.call(
        'ritual_ZN21QQuickFolderListModelC1EP7QObject',
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

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuickFolderListModel::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#classBegin
    """
    #  void QQuickFolderListModel::classBegin()
    ritual = 'ritual_ZN21QQuickFolderListModel10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QQuickFolderListModel10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickFolderListModel::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#componentComplete
    """
    #  void QQuickFolderListModel::componentComplete()
    ritual = 'ritual_ZN21QQuickFolderListModel17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QQuickFolderListModel17componentCompleteEv'
    self.uglySide.call(ritual)

  def folderChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFolderListModel::folderChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#folderChanged
    """
    #  void QQuickFolderListModel::folderChanged()
    self.uglySide.call('ritual_ZN21QQuickFolderListModel13folderChangedEv')

  def rowCountChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFolderListModel::rowCountChanged() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#rowCountChanged
    """
    #  void QQuickFolderListModel::rowCountChanged() const
    self.uglySide.call(
        'ritual_ZNK21QQuickFolderListModel15rowCountChangedEv',
    )

  def rootFolderChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFolderListModel::rootFolderChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#rootFolderChanged
    """
    #  void QQuickFolderListModel::rootFolderChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickFolderListModel17rootFolderChangedEv',
    )

  def nameFilterChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFolderListModel::nameFilterChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#nameFilterChanged
    """
    #  void QQuickFolderListModel::nameFilterChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickFolderListModel17nameFilterChangedEv',
    )

  def sortFieldChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFolderListModel::sortFieldChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#sortFieldChanged
    """
    #  void QQuickFolderListModel::sortFieldChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickFolderListModel16sortFieldChangedEv',
    )

  def sortReversedChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFolderListModel::sortReversedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#sortReversedChanged
    """
    #  void QQuickFolderListModel::sortReversedChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickFolderListModel19sortReversedChangedEv',
    )

  def showFilesChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFolderListModel::showFilesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#showFilesChanged
    """
    #  void QQuickFolderListModel::showFilesChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickFolderListModel16showFilesChangedEv',
    )

  def showDirsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFolderListModel::showDirsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#showDirsChanged
    """
    #  void QQuickFolderListModel::showDirsChanged()
    self.uglySide.call('ritual_ZN21QQuickFolderListModel15showDirsChangedEv')

  def showDirsFirstChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFolderListModel::showDirsFirstChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#showDirsFirstChanged
    """
    #  void QQuickFolderListModel::showDirsFirstChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickFolderListModel20showDirsFirstChangedEv',
    )

  def showDotAndDotDotChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFolderListModel::showDotAndDotDotChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#showDotAndDotDotChanged
    """
    #  void QQuickFolderListModel::showDotAndDotDotChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickFolderListModel23showDotAndDotDotChangedEv',
    )

  def showDotChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFolderListModel::showDotChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#showDotChanged
    """
    #  void QQuickFolderListModel::showDotChanged()
    self.uglySide.call('ritual_ZN21QQuickFolderListModel14showDotChangedEv')

  def showDotDotChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFolderListModel::showDotDotChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#showDotDotChanged
    """
    #  void QQuickFolderListModel::showDotDotChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickFolderListModel17showDotDotChangedEv',
    )

  def showHiddenChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFolderListModel::showHiddenChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#showHiddenChanged
    """
    #  void QQuickFolderListModel::showHiddenChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickFolderListModel17showHiddenChangedEv',
    )

  def showOnlyReadableChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFolderListModel::showOnlyReadableChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#showOnlyReadableChanged
    """
    #  void QQuickFolderListModel::showOnlyReadableChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickFolderListModel23showOnlyReadableChangedEv',
    )

  def caseSensitiveChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFolderListModel::caseSensitiveChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#caseSensitiveChanged
    """
    #  void QQuickFolderListModel::caseSensitiveChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickFolderListModel20caseSensitiveChangedEv',
    )

  def sortCaseSensitiveChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFolderListModel::sortCaseSensitiveChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html
    """
    #  void QQuickFolderListModel::sortCaseSensitiveChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickFolderListModel24sortCaseSensitiveChangedEv',
    )

  def countChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFolderListModel::countChanged() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#countChanged
    """
    #  void QQuickFolderListModel::countChanged() const
    self.uglySide.call('ritual_ZNK21QQuickFolderListModel12countChangedEv')

  def statusChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFolderListModel::statusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderlistmodel.html#statusChanged
    """
    #  void QQuickFolderListModel::statusChanged()
    self.uglySide.call('ritual_ZN21QQuickFolderListModel13statusChangedEv')
