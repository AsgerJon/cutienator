"""
QFileSystemModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qfilesystemmodel.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QAbstractItemModel, QDir, QHash, QList, QObject
from ..QtCore import QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QDateTime, QEvent, QFileInfo, QMetaObject
  from ..QtCore import QMimeData, QModelIndex, QTimeZone, QTimerEvent
  from ..QtCore import QVariant
  from . import QAbstractFileIconProvider, QIcon
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractFileIconProvider = WAIT['QAbstractFileIconProvider']
  QEvent = WAIT['QEvent']
  QMimeData = WAIT['QMimeData']
  QModelIndex = WAIT['QModelIndex']
  QTimeZone = WAIT['QTimeZone']
  QTimerEvent = WAIT['QTimerEvent']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFileSystemModel(QAbstractItemModel):
  """
  The cute side of Qt's QFileSystemModel: a plain Python object standing in
  front of one C++ QFileSystemModel.

  It is built on the cute 'QAbstractItemModel', as Qt's QFileSystemModel is
  built on Qt's QAbstractItemModel, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QFileSystemModel that has a ritual and that Python
  can call so far, 53 names in all: 'metaObject', 'tr', 'index', 'parent',
  'sibling', 'hasChildren', 'canFetchMore', 'fetchMore', 'rowCount',
  'columnCount', 'myComputer', 'data', 'setData', 'headerData', 'flags',
  'sort', 'mimeTypes', 'mimeData', 'dropMimeData', 'supportedDropActions',
  'roleNames', 'setRootPath', 'rootPath', 'rootDirectory', 'setIconProvider',
  'iconProvider', 'setFilter', 'filter', 'setResolveSymlinks',
  'resolveSymlinks', 'setReadOnly', 'isReadOnly', 'setNameFilterDisables',
  'nameFilterDisables', 'setNameFilters', 'nameFilters', 'setOption',
  'testOption', 'setOptions', 'options', 'filePath', 'isDir', 'size', 'type',
  'lastModified', 'mkdir', 'rmdir', 'fileName', 'fileIcon', 'fileInfo',
  'remove', 'timerEvent', 'event'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFileSystemModel::~QFileSystemModel()': the destructor: Python
    never removes a C++ QFileSystemModel.

  What has no ritual
  ------------------

  13 of the 70 functions Qt declares: 6 takes or gives a type that cannot be
  passed yet; 3 a signal; 2 forbidden; 1 a template; 1 declared and nowhere
  to be found.

  What to expect
  --------------

  - The C++ QFileSystemModel is created at the first use, not by
    'QFileSystemModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QFileSystemModel.
  - Qt tells when it has removed the C++ QFileSystemModel. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QFileSystemModel, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Option(CuteFlags):
    """
    The flags enum 'QFileSystemModel::Option' of Qt, with the 3 names Qt
    gives in it. Qt names the type of its combinations
    'QFileSystemModel::Options'.
    """

    DontWatchForChanges = 0x1
    DontResolveSymlinks = 0x2
    DontUseCustomDirectoryIcons = 0x4

  Options = Option

  class Roles(CuteNum):
    """
    The enum 'QFileSystemModel::Roles' of Qt, with the 5 names Qt gives in
    it.
    """

    FileIconRole = Kee[int](1)
    FileInfoRole = Kee[int](252)
    FilePathRole = Kee[int](257)
    FileNameRole = Kee[int](258)
    FilePermissions = Kee[int](259)

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
    Calls Qt's 'QString QFileSystemModel::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodel.html#tr

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
    #  QString QFileSystemModel::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QFileSystemModel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFileSystemModel'

  #  A C++ QFileSystemModel Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QFileSystemModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QFileSystemModel::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QFileSystemModel::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QFileSystemModel10metaObjectEv',
    )
    from ..QtCore import QMetaObject
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
    Calls Qt's 'QModelIndex QFileSystemModel::index(int row, int column,
    const QModelIndex &parent) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodel.html#index

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
    #  QModelIndex QFileSystemModel::index(int row, int column, const
    #      QModelIndex &parent) const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK16QFileSystemModel5indexEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QFileSystemModel5indexEiiRK11QModelIndex'
    address = self.uglySide.call(ritual, row, column, self._valueOf(parent))
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(str)
  @overload(str, int)
  def index(self, path: str, column: int = 0) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QFileSystemModel::index(const QString &path, int
    column) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodel.html#index

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    column : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QFileSystemModel::index(const QString &path, int column)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK16QFileSystemModel5indexERK7QStringi', path, column,
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  def parent(self, child: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QFileSystemModel::parent(const QModelIndex
    &child) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodel.html#parent

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
    #  QModelIndex QFileSystemModel::parent(const QModelIndex &child) const
    ritual = 'ritual_ZNK16QFileSystemModel6parentERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QFileSystemModel6parentERK11QModelIndex'
    address = self.uglySide.call(ritual, self._valueOf(child))
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(int, int, QModelIndex)
  def sibling(self, row: int, column: int, idx: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QFileSystemModel::sibling(int row, int column,
    const QModelIndex &idx) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodel.html#sibling

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
    #  QModelIndex QFileSystemModel::sibling(int row, int column, const
    #      QModelIndex &idx) const
    ritual = 'ritual_ZNK16QFileSystemModel7siblingEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QFileSystemModel7siblingEiiRK11QModelIndex'
    address = self.uglySide.call(ritual, row, column, self._valueOf(idx))
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload()
  @overload(QModelIndex)
  def hasChildren(self, parent: Optional[QModelIndex] = None) -> bool:
    """
    Calls Qt's 'bool QFileSystemModel::hasChildren(const QModelIndex &parent)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodel.html#hasChildren

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  bool QFileSystemModel::hasChildren(const QModelIndex &parent) const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK16QFileSystemModel11hasChildrenERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK16QFileSystemModel11hasChildrenERK11QModelIndex')
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload(QModelIndex)
  def canFetchMore(self, parent: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QFileSystemModel::canFetchMore(const QModelIndex
    &parent) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodel.html#canFetchMore

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QFileSystemModel::canFetchMore(const QModelIndex &parent) const
    ritual = 'ritual_ZNK16QFileSystemModel12canFetchMoreERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK16QFileSystemModel12canFetchMoreERK11QModelIndex')
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload()
  @overload(QModelIndex)
  def rowCount(self, parent: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QFileSystemModel::rowCount(const QModelIndex &parent)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodel.html#rowCount

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QFileSystemModel::rowCount(const QModelIndex &parent) const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK16QFileSystemModel8rowCountERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QFileSystemModel8rowCountERK11QModelIndex'
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload()
  @overload(QModelIndex)
  def columnCount(self, parent: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QFileSystemModel::columnCount(const QModelIndex &parent)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodel.html#columnCount

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QFileSystemModel::columnCount(const QModelIndex &parent) const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK16QFileSystemModel11columnCountERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK16QFileSystemModel11columnCountERK11QModelIndex')
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload()
  @overload(int)
  def myComputer(self, role: int = 0) -> QVariant:
    """
    Calls Qt's 'QVariant QFileSystemModel::myComputer(int role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodel.html#myComputer

    Parameters
    ----------

    role : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QFileSystemModel::myComputer(int role) const
    address = self.uglySide.call(
        'ritual_ZNK16QFileSystemModel10myComputerEi', role,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QModelIndex)
  @overload(QModelIndex, int)
  def data(self, index: QModelIndex, role: int = 0) -> QVariant:
    """
    Calls Qt's 'QVariant QFileSystemModel::data(const QModelIndex &index, int
    role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodel.html#data

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
    #  QVariant QFileSystemModel::data(const QModelIndex &index, int role)
    #      const
    ritual = 'ritual_ZNK16QFileSystemModel4dataERK11QModelIndexi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QFileSystemModel4dataERK11QModelIndexi'
    address = self.uglySide.call(ritual, self._valueOf(index), role)
    from ..QtCore import QVariant
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
    Calls Qt's 'QVariant QFileSystemModel::headerData(int section,
    Qt::Orientation orientation, int role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodel.html#headerData

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
    #  QVariant QFileSystemModel::headerData(int section, Qt::Orientation
    #      orientation, int role) const
    ritual = 'ritual_ZNK16QFileSystemModel10headerDataEiN2Qt11OrientationEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK16QFileSystemModel10headerDataEiN2Qt11OrientationE'
          'i')
    address = self.uglySide.call(ritual, section, orientation.value, role)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QModelIndex)
  def flags(self, index: QModelIndex) -> Qt.ItemFlags:
    """
    Calls Qt's 'Qt::ItemFlags QFileSystemModel::flags(const QModelIndex
    &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodel.html#flags

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
    #  Qt::ItemFlags QFileSystemModel::flags(const QModelIndex &index) const
    ritual = 'ritual_ZNK16QFileSystemModel5flagsERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QFileSystemModel5flagsERK11QModelIndex'
    return Qt.ItemFlags(self.uglySide.call(ritual, self._valueOf(index)))

  def mimeTypes(self) -> QStringList:
    """
    Calls Qt's 'QStringList QFileSystemModel::mimeTypes() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodel.html#mimeTypes

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QFileSystemModel::mimeTypes() const
    address = self.uglySide.call('ritual_ZNK16QFileSystemModel9mimeTypesEv')
    return QStringList._cuteOwning(address)

  @overload(QList[QModelIndex])
  def mimeData(self, indexes: QList[QModelIndex]) -> Optional[QMimeData]:
    """
    Calls Qt's 'QMimeData *QFileSystemModel::mimeData(const QModelIndexList
    &indexes) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodel.html#mimeData

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
    #  QMimeData *QFileSystemModel::mimeData(const QModelIndexList &indexes)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK16QFileSystemModel8mimeDataERK5QListI11QModelIndexE',
        self._valueOf(indexes),
    )
    from ..QtCore import QMimeData
    return QMimeData._cuteAt(address)

  def supportedDropActions(self) -> Qt.DropActions:
    """
    Calls Qt's 'Qt::DropActions QFileSystemModel::supportedDropActions()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemmodel.html#supportedDropActions

    Returns
    -------

    Qt.DropActions
      The value standing for the combination Qt gave back.
    """
    #  Qt::DropActions QFileSystemModel::supportedDropActions() const
    ritual = 'ritual_ZNK16QFileSystemModel20supportedDropActionsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QFileSystemModel20supportedDropActionsEv'
    return Qt.DropActions(self.uglySide.call(ritual))

  def roleNames(self) -> QHash[int, QByteArray]:
    """
    Calls Qt's 'QHash<int, QByteArray> QFileSystemModel::roleNames() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodel.html#roleNames

    Returns
    -------

    QHash[int, QByteArray]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QHash<int, QByteArray> QFileSystemModel::roleNames() const
    address = self.uglySide.call('ritual_ZNK16QFileSystemModel9roleNamesEv')
    from ..QtCore import QByteArray
    return QHash[int, QByteArray]._cuteOwning(address)

  def rootPath(self) -> str:
    """
    Calls Qt's 'QString QFileSystemModel::rootPath() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodel.html#rootPath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileSystemModel::rootPath() const
    return self.uglySide.call('ritual_ZNK16QFileSystemModel8rootPathEv')

  def rootDirectory(self) -> QDir:
    """
    Calls Qt's 'QDir QFileSystemModel::rootDirectory() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemmodel.html#rootDirectory

    Returns
    -------

    QDir
      A new cute QDir around the copy Qt gave back. Python owns it.
    """
    #  QDir QFileSystemModel::rootDirectory() const
    address = self.uglySide.call(
        'ritual_ZNK16QFileSystemModel13rootDirectoryEv',
    )
    return QDir._cuteOwning(address)

  def iconProvider(self) -> Optional[QAbstractFileIconProvider]:
    """
    Calls Qt's 'QAbstractFileIconProvider *QFileSystemModel::iconProvider()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodel.html#iconProvider

    Returns
    -------

    Optional[QAbstractFileIconProvider]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractFileIconProvider *QFileSystemModel::iconProvider() const
    address = self.uglySide.call(
        'ritual_ZNK16QFileSystemModel12iconProviderEv',
    )
    from . import QAbstractFileIconProvider
    return QAbstractFileIconProvider._cuteAt(address)

  def filter(self) -> QDir.Filters:
    """
    Calls Qt's 'QDir::Filters QFileSystemModel::filter() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodel.html#filter

    Returns
    -------

    QDir.Filters
      The value standing for the combination Qt gave back.
    """
    #  QDir::Filters QFileSystemModel::filter() const
    return QDir.Filters(self.uglySide.call(
        'ritual_ZNK16QFileSystemModel6filterEv',
    ))

  def resolveSymlinks(self) -> bool:
    """
    Calls Qt's 'bool QFileSystemModel::resolveSymlinks() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemmodel.html#resolveSymlinks
    """
    #  bool QFileSystemModel::resolveSymlinks() const
    return self.uglySide.call(
        'ritual_ZNK16QFileSystemModel15resolveSymlinksEv',
    )

  def isReadOnly(self) -> bool:
    """
    Calls Qt's 'bool QFileSystemModel::isReadOnly() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodel.html#isReadOnly
    """
    #  bool QFileSystemModel::isReadOnly() const
    return self.uglySide.call('ritual_ZNK16QFileSystemModel10isReadOnlyEv')

  def nameFilterDisables(self) -> bool:
    """
    Calls Qt's 'bool QFileSystemModel::nameFilterDisables() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemmodel.html#nameFilterDisables
    """
    #  bool QFileSystemModel::nameFilterDisables() const
    return self.uglySide.call(
        'ritual_ZNK16QFileSystemModel18nameFilterDisablesEv',
    )

  def nameFilters(self) -> QStringList:
    """
    Calls Qt's 'QStringList QFileSystemModel::nameFilters() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodel.html#nameFilters

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QFileSystemModel::nameFilters() const
    address = self.uglySide.call(
        'ritual_ZNK16QFileSystemModel11nameFiltersEv',
    )
    return QStringList._cuteOwning(address)

  @overload(Option)
  def testOption(self, option: Option) -> bool:
    """
    Calls Qt's 'bool QFileSystemModel::testOption(Option option) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodel.html#testOption

    Parameters
    ----------

    option : Option
      Passed on as its number.
    """
    #  bool QFileSystemModel::testOption(Option option) const
    return self.uglySide.call(
        'ritual_ZNK16QFileSystemModel10testOptionENS_6OptionE', option.value,
    )

  def options(self) -> Options:
    """
    Calls Qt's 'Options QFileSystemModel::options() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodel.html#options

    Returns
    -------

    Options
      The value standing for the combination Qt gave back.
    """
    #  Options QFileSystemModel::options() const
    return QFileSystemModel.Options(self.uglySide.call(
        'ritual_ZNK16QFileSystemModel7optionsEv',
    ))

  @overload(QModelIndex)
  def filePath(self, index: QModelIndex) -> str:
    """
    Calls Qt's 'QString QFileSystemModel::filePath(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodel.html#filePath

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileSystemModel::filePath(const QModelIndex &index) const
    return self.uglySide.call(
        'ritual_ZNK16QFileSystemModel8filePathERK11QModelIndex',
        self._valueOf(index),
    )

  @overload(QModelIndex)
  def isDir(self, index: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QFileSystemModel::isDir(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodel.html#isDir

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QFileSystemModel::isDir(const QModelIndex &index) const
    return self.uglySide.call(
        'ritual_ZNK16QFileSystemModel5isDirERK11QModelIndex',
        self._valueOf(index),
    )

  @overload(QModelIndex)
  def size(self, index: QModelIndex) -> int:
    """
    Calls Qt's 'qint64 QFileSystemModel::size(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodel.html#size

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  qint64 QFileSystemModel::size(const QModelIndex &index) const
    return self.uglySide.call(
        'ritual_ZNK16QFileSystemModel4sizeERK11QModelIndex',
        self._valueOf(index),
    )

  @overload(QModelIndex)
  def type(self, index: QModelIndex) -> str:
    """
    Calls Qt's 'QString QFileSystemModel::type(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodel.html#type

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileSystemModel::type(const QModelIndex &index) const
    return self.uglySide.call(
        'ritual_ZNK16QFileSystemModel4typeERK11QModelIndex',
        self._valueOf(index),
    )

  @overload(QModelIndex)
  def lastModified(self, index: QModelIndex) -> QDateTime:
    """
    Calls Qt's 'QDateTime QFileSystemModel::lastModified(const QModelIndex
    &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodel.html#lastModified

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QFileSystemModel::lastModified(const QModelIndex &index)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK16QFileSystemModel12lastModifiedERK11QModelIndex',
        self._valueOf(index),
    )
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  @overload(QModelIndex, QTimeZone)
  def lastModified(self, index: QModelIndex, tz: QTimeZone) -> QDateTime:
    """
    Calls Qt's 'QDateTime QFileSystemModel::lastModified(const QModelIndex
    &index, const QTimeZone &tz) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodel.html#lastModified

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    tz : QTimeZone
      Passed on as a value: Qt reads the C++ QTimeZone, which stays Python's
      own.

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QFileSystemModel::lastModified(const QModelIndex &index,
    #      const QTimeZone &tz) const
    address = self.uglySide.call(
        'ritual_ZNK16QFileSystemModel12lastModifiedERK11QModelIndexRK9QTime'
        'Zone',
        self._valueOf(index), self._valueOf(tz),
    )
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  @overload(QModelIndex)
  def fileName(self, index: QModelIndex) -> str:
    """
    Calls Qt's 'QString QFileSystemModel::fileName(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodel.html#fileName

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileSystemModel::fileName(const QModelIndex &index) const
    return self.uglySide.call(
        'ritual_ZNK16QFileSystemModel8fileNameERK11QModelIndex',
        self._valueOf(index),
    )

  @overload(QModelIndex)
  def fileIcon(self, index: QModelIndex) -> QIcon:
    """
    Calls Qt's 'QIcon QFileSystemModel::fileIcon(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodel.html#fileIcon

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QFileSystemModel::fileIcon(const QModelIndex &index) const
    address = self.uglySide.call(
        'ritual_ZNK16QFileSystemModel8fileIconERK11QModelIndex',
        self._valueOf(index),
    )
    from . import QIcon
    return QIcon._cuteOwning(address)

  @overload(QModelIndex)
  def fileInfo(self, index: QModelIndex) -> QFileInfo:
    """
    Calls Qt's 'QFileInfo QFileSystemModel::fileInfo(const QModelIndex
    &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodel.html#fileInfo

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QFileInfo
      A new cute QFileInfo around the copy Qt gave back. Python owns it.
    """
    #  QFileInfo QFileSystemModel::fileInfo(const QModelIndex &index) const
    address = self.uglySide.call(
        'ritual_ZNK16QFileSystemModel8fileInfoERK11QModelIndex',
        self._valueOf(index),
    )
    from ..QtCore import QFileInfo
    return QFileInfo._cuteOwning(address)

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
    Calls Qt's 'bool QFileSystemModel::setData(const QModelIndex &index,
    const QVariant &value, int role)'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodel.html#setData

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
    #  bool QFileSystemModel::setData(const QModelIndex &index, const
    #      QVariant &value, int role)
    ritual = (
        'ritual_ZN16QFileSystemModel7setDataERK11QModelIndexRK8QVarianti')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QFileSystemModel7setDataERK11QModelIndexRK8QVaria'
          'nti')
    return self.uglySide.call(
        ritual, self._valueOf(index), self._valueOf(value), role,
    )

  @overload(str)
  def setRootPath(self, path: str) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QFileSystemModel::setRootPath(const QString
    &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodel.html#setRootPath

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QFileSystemModel::setRootPath(const QString &path)
    address = self.uglySide.call(
        'ritual_ZN16QFileSystemModel11setRootPathERK7QString', path,
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QAbstractFileIconProvider)
  @overload(NoneType)
  def setIconProvider(
      self,
      provider: Optional[QAbstractFileIconProvider],
  ) -> None:
    """
    Calls Qt's 'void
    QFileSystemModel::setIconProvider(QAbstractFileIconProvider *provider)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemmodel.html#setIconProvider

    Parameters
    ----------

    provider : Optional[QAbstractFileIconProvider]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFileSystemModel::setIconProvider(QAbstractFileIconProvider
    #      *provider)
    self.uglySide.call(
        'ritual_ZN16QFileSystemModel15setIconProviderEP25QAbstractFileIconP'
        'rovider',
        self._addressOf(provider),
    )

  @overload(QDir.Filters)
  def setFilter(self, filters: QDir.Filters) -> None:
    """
    Calls Qt's 'void QFileSystemModel::setFilter(QDir::Filters filters)'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodel.html#setFilter

    Parameters
    ----------

    filters : QDir.Filters
      Passed on as its number.
    """
    #  void QFileSystemModel::setFilter(QDir::Filters filters)
    self.uglySide.call(
        'ritual_ZN16QFileSystemModel9setFilterE6QFlagsIN4QDir6FilterEE',
        filters.value,
    )

  @overload(bool)
  def setResolveSymlinks(self, enable: bool) -> None:
    """
    Calls Qt's 'void QFileSystemModel::setResolveSymlinks(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemmodel.html#setResolveSymlinks

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QFileSystemModel::setResolveSymlinks(bool enable)
    self.uglySide.call(
        'ritual_ZN16QFileSystemModel18setResolveSymlinksEb', enable,
    )

  @overload(bool)
  def setReadOnly(self, enable: bool) -> None:
    """
    Calls Qt's 'void QFileSystemModel::setReadOnly(bool enable)'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodel.html#setReadOnly

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QFileSystemModel::setReadOnly(bool enable)
    self.uglySide.call('ritual_ZN16QFileSystemModel11setReadOnlyEb', enable)

  @overload(bool)
  def setNameFilterDisables(self, enable: bool) -> None:
    """
    Calls Qt's 'void QFileSystemModel::setNameFilterDisables(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemmodel.html#setNameFilterDisables

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QFileSystemModel::setNameFilterDisables(bool enable)
    self.uglySide.call(
        'ritual_ZN16QFileSystemModel21setNameFilterDisablesEb', enable,
    )

  @overload(QStringList)
  def setNameFilters(self, filters: QStringList) -> None:
    """
    Calls Qt's 'void QFileSystemModel::setNameFilters(const QStringList
    &filters)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemmodel.html#setNameFilters

    Parameters
    ----------

    filters : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QFileSystemModel::setNameFilters(const QStringList &filters)
    self.uglySide.call(
        'ritual_ZN16QFileSystemModel14setNameFiltersERK5QListI7QStringE',
        self._valueOf(filters),
    )

  @overload(Option)
  @overload(Option, bool)
  def setOption(self, option: Option, on: bool = True) -> None:
    """
    Calls Qt's 'void QFileSystemModel::setOption(Option option, bool on)'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodel.html#setOption

    Parameters
    ----------

    option : Option
      Passed on as its number.

    on : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QFileSystemModel::setOption(Option option, bool on)
    self.uglySide.call(
        'ritual_ZN16QFileSystemModel9setOptionENS_6OptionEb',
        option.value, on,
    )

  @overload(Options)
  def setOptions(self, options: Options) -> None:
    """
    Calls Qt's 'void QFileSystemModel::setOptions(Options options)'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodel.html#setOptions

    Parameters
    ----------

    options : Options
      Passed on as its number.
    """
    #  void QFileSystemModel::setOptions(Options options)
    self.uglySide.call(
        'ritual_ZN16QFileSystemModel10setOptionsE6QFlagsINS_6OptionEE',
        options.value,
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
    'QFileSystemModel::QFileSystemModel(QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemmodel.html#QFileSystemModel

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QFileSystemModel::QFileSystemModel(QObject *parent)
    self._noteCreation(QFileSystemModel, lambda: Rituals.call(
        'ritual_ZN16QFileSystemModelC1EP7QObject', self._addressOf(parent),
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

  @overload(QModelIndex)
  def fetchMore(self, parent: QModelIndex) -> None:
    """
    Calls Qt's 'void QFileSystemModel::fetchMore(const QModelIndex &parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodel.html#fetchMore

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QFileSystemModel::fetchMore(const QModelIndex &parent)
    ritual = 'ritual_ZN16QFileSystemModel9fetchMoreERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QFileSystemModel9fetchMoreERK11QModelIndex'
    self.uglySide.call(ritual, self._valueOf(parent))

  @overload(int)
  @overload(int, Qt.SortOrder)
  def sort(
      self,
      column: int,
      order: Qt.SortOrder = Qt.SortOrder.AscendingOrder,
  ) -> None:
    """
    Calls Qt's 'void QFileSystemModel::sort(int column, Qt::SortOrder
    order)'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodel.html#sort

    Parameters
    ----------

    column : int
      Passed on as it is.

    order : Qt.SortOrder
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.SortOrder.AscendingOrder.
    """
    #  void QFileSystemModel::sort(int column, Qt::SortOrder order)
    ritual = 'ritual_ZN16QFileSystemModel4sortEiN2Qt9SortOrderE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QFileSystemModel4sortEiN2Qt9SortOrderE'
    self.uglySide.call(ritual, column, order.value)

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
    Calls Qt's 'bool QFileSystemModel::dropMimeData(const QMimeData *data,
    Qt::DropAction action, int row, int column, const QModelIndex &parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodel.html#dropMimeData

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
    #  bool QFileSystemModel::dropMimeData(const QMimeData *data,
    #      Qt::DropAction action, int row, int column, const QModelIndex
    #      &parent)
    ritual = (
        'ritual_ZN16QFileSystemModel12dropMimeDataEPK9QMimeDataN2Qt10DropAc'
        'tionEiiRK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QFileSystemModel12dropMimeDataEPK9QMimeDataN2Qt10'
          'DropActionEiiRK11QModelIndex')
    return self.uglySide.call(
        ritual,
        self._addressOf(data), action.value, row, column,
        self._valueOf(parent),
    )

  @overload(QModelIndex, str)
  def mkdir(self, parent: QModelIndex, name: str) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QFileSystemModel::mkdir(const QModelIndex
    &parent, const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodel.html#mkdir

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QFileSystemModel::mkdir(const QModelIndex &parent, const
    #      QString &name)
    address = self.uglySide.call(
        'ritual_ZN16QFileSystemModel5mkdirERK11QModelIndexRK7QString',
        self._valueOf(parent), name,
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  def rmdir(self, index: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QFileSystemModel::rmdir(const QModelIndex &index)'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodel.html#rmdir

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QFileSystemModel::rmdir(const QModelIndex &index)
    return self.uglySide.call(
        'ritual_ZN16QFileSystemModel5rmdirERK11QModelIndex',
        self._valueOf(index),
    )

  @overload(QModelIndex)
  def remove(self, index: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QFileSystemModel::remove(const QModelIndex &index)'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodel.html#remove

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QFileSystemModel::remove(const QModelIndex &index)
    return self.uglySide.call(
        'ritual_ZN16QFileSystemModel6removeERK11QModelIndex',
        self._valueOf(index),
    )

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, event: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QFileSystemModel::timerEvent(QTimerEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodel.html#timerEvent

    Parameters
    ----------

    event : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFileSystemModel::timerEvent(QTimerEvent *event)
    ritual = 'ritual_ZN16QFileSystemModel10timerEventEP11QTimerEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QFileSystemModel10timerEventEP11QTimerEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QFileSystemModel::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodel.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QFileSystemModel::event(QEvent *event)
    ritual = 'ritual_ZN16QFileSystemModel5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QFileSystemModel5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))
