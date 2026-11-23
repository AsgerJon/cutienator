"""
QDir binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtCore/qdir.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute
from ..occult import Rituals
from . import QList, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QChar, QFileInfo


class QDir(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDir: a plain Python object standing in front of one
  C++ QDir.

  C++ hands a QDir around as a copy, so every C++ QDir behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDir that has a ritual and that Python can call so
  far, 56 names in all: 'setPath', 'path', 'absolutePath', 'canonicalPath',
  'setSearchPaths', 'addSearchPath', 'searchPaths', 'dirName', 'filePath',
  'absoluteFilePath', 'relativeFilePath', 'toNativeSeparators',
  'fromNativeSeparators', 'cd', 'cdUp', 'nameFilters', 'setNameFilters',
  'filter', 'setFilter', 'sorting', 'setSorting', 'isEmpty', '__getitem__',
  'nameFiltersFromString', 'entryList', 'entryInfoList', 'rmdir', 'rmpath',
  'removeRecursively', 'isReadable', 'exists', 'isRoot', 'isRelativePath',
  'isAbsolutePath', 'isRelative', 'isAbsolute', 'makeAbsolute', 'remove',
  'rename', 'drives', 'listSeparator', 'separator', 'setCurrent', 'current',
  'currentPath', 'home', 'homePath', 'root', 'rootPath', 'temp', 'tempPath',
  'match', 'cleanPath', 'refresh', '__eq__', '__ne__'. It can be made from
  Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDir::~QDir()': the destructor: Python removes its C++ QDir by it,
    and has no other use for it.
  - Qt's 'qsizetype QDir::count(Qt::Disambiguated_t a0) const': names
    'Qt::Disambiguated_t', which has no cute class yet.

  What has no ritual
  ------------------

  15 of the 80 functions Qt declares: 11 takes or gives a type that cannot be
  passed yet; 4 a template.

  What to expect
  --------------

  - The C++ QDir is created at the first use, not by 'QDir(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDir back gives a copy the ritual made for Python, in
    a new cute QDir.
  """

  #  The enums Qt writes inside QDir, each a class in here as in C++, and the
  #  names Qt has for the combinations of its flags enums.

  class Filter(CuteFlags):
    """
    The flags enum 'QDir::Filter' of Qt, with the 20 names Qt gives in it. Qt
    names the type of its combinations 'QDir::Filters'.
    """

    Dirs = 0x1
    Files = 0x2
    Drives = 0x4
    NoSymLinks = 0x8
    AllEntries = 0x7
    TypeMask = 0xf
    Readable = 0x10
    Writable = 0x20
    Executable = 0x40
    PermissionMask = 0x70
    Modified = 0x80
    Hidden = 0x100
    System = 0x200
    AccessMask = 0x3f0
    AllDirs = 0x400
    CaseSensitive = 0x800
    NoDot = 0x2000
    NoDotDot = 0x4000
    NoDotAndDotDot = 0x6000
    NoFilter = -1

  Filters = Filter

  class SortFlag(CuteFlags):
    """
    The flags enum 'QDir::SortFlag' of Qt, with the 12 names Qt gives in it.
    Qt names the type of its combinations 'QDir::SortFlags'.
    """

    Name = 0x0
    Time = 0x1
    Size = 0x2
    Unsorted = 0x3
    SortByMask = 0x3
    DirsFirst = 0x4
    Reversed = 0x8
    IgnoreCase = 0x10
    DirsLast = 0x20
    LocaleAware = 0x40
    Type = 0x80
    NoSort = -1

  SortFlags = SortFlag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str, QStringList)
  def setSearchPaths(prefix: str, searchPaths: QStringList) -> None:
    """
    Calls Qt's 'void QDir::setSearchPaths(const QString &prefix, const
    QStringList &searchPaths)'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#setSearchPaths

    Parameters
    ----------

    prefix : str
      Passed on as it is: a QString is made of it for the call.

    searchPaths : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QDir::setSearchPaths(const QString &prefix, const QStringList
    #      &searchPaths)
    Rituals.call(
        'ritual_ZN4QDir14setSearchPathsERK7QStringRK5QListIS0_E',
        prefix, CuteMixin._valueOf(searchPaths),
    )

  @staticmethod
  @overload(str, str)
  def addSearchPath(prefix: str, path: str) -> None:
    """
    Calls Qt's 'void QDir::addSearchPath(const QString &prefix, const QString
    &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#addSearchPath

    Parameters
    ----------

    prefix : str
      Passed on as it is: a QString is made of it for the call.

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDir::addSearchPath(const QString &prefix, const QString &path)
    Rituals.call('ritual_ZN4QDir13addSearchPathERK7QStringS2_', prefix, path)

  @staticmethod
  @overload(str)
  def searchPaths(prefix: str) -> QStringList:
    """
    Calls Qt's 'QStringList QDir::searchPaths(const QString &prefix)'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#searchPaths

    Parameters
    ----------

    prefix : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QDir::searchPaths(const QString &prefix)
    address = Rituals.call('ritual_ZN4QDir11searchPathsERK7QString', prefix)
    return QStringList._cuteOwning(address)

  @staticmethod
  @overload(str)
  def toNativeSeparators(pathName: str) -> str:
    """
    Calls Qt's 'QString QDir::toNativeSeparators(const QString &pathName)'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#toNativeSeparators

    Parameters
    ----------

    pathName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDir::toNativeSeparators(const QString &pathName)
    return Rituals.call(
        'ritual_ZN4QDir18toNativeSeparatorsERK7QString', pathName,
    )

  @staticmethod
  @overload(str)
  def fromNativeSeparators(pathName: str) -> str:
    """
    Calls Qt's 'QString QDir::fromNativeSeparators(const QString &pathName)'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#fromNativeSeparators

    Parameters
    ----------

    pathName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDir::fromNativeSeparators(const QString &pathName)
    return Rituals.call(
        'ritual_ZN4QDir20fromNativeSeparatorsERK7QString', pathName,
    )

  @staticmethod
  @overload(str)
  def nameFiltersFromString(nameFilter: str) -> QStringList:
    """
    Calls Qt's 'QStringList QDir::nameFiltersFromString(const QString
    &nameFilter)'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#nameFiltersFromString

    Parameters
    ----------

    nameFilter : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QDir::nameFiltersFromString(const QString &nameFilter)
    address = Rituals.call(
        'ritual_ZN4QDir21nameFiltersFromStringERK7QString', nameFilter,
    )
    return QStringList._cuteOwning(address)

  @staticmethod
  @overload(str)
  def isRelativePath(path: str) -> bool:
    """
    Calls Qt's 'bool QDir::isRelativePath(const QString &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#isRelativePath

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QDir::isRelativePath(const QString &path)
    return Rituals.call('ritual_ZN4QDir14isRelativePathERK7QString', path)

  @staticmethod
  @overload(str)
  def isAbsolutePath(path: str) -> bool:
    """
    Calls Qt's 'bool QDir::isAbsolutePath(const QString &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#isAbsolutePath

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QDir::isAbsolutePath(const QString &path)
    return Rituals.call('ritual_ZN4QDir14isAbsolutePathERK7QString', path)

  @staticmethod
  def drives() -> QList[QFileInfo]:
    """
    Calls Qt's 'QFileInfoList QDir::drives()'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#drives

    Returns
    -------

    QList[QFileInfo]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QFileInfoList QDir::drives()
    address = Rituals.call('ritual_ZN4QDir6drivesEv')
    from . import QFileInfo
    return QList[QFileInfo]._cuteOwning(address)

  @staticmethod
  def listSeparator() -> QChar:
    """
    Calls Qt's 'QChar QDir::listSeparator()'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#listSeparator

    Returns
    -------

    QChar
      A new cute QChar around the copy Qt gave back. Python owns it.
    """
    #  QChar QDir::listSeparator()
    address = Rituals.call('ritual_ZN4QDir13listSeparatorEv')
    from . import QChar
    return QChar._cuteOwning(address)

  @staticmethod
  def separator() -> QChar:
    """
    Calls Qt's 'QChar QDir::separator()'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#separator

    Returns
    -------

    QChar
      A new cute QChar around the copy Qt gave back. Python owns it.
    """
    #  QChar QDir::separator()
    address = Rituals.call('ritual_ZN4QDir9separatorEv')
    from . import QChar
    return QChar._cuteOwning(address)

  @staticmethod
  @overload(str)
  def setCurrent(path: str) -> bool:
    """
    Calls Qt's 'bool QDir::setCurrent(const QString &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#setCurrent

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QDir::setCurrent(const QString &path)
    return Rituals.call('ritual_ZN4QDir10setCurrentERK7QString', path)

  @staticmethod
  def current() -> QDir:
    """
    Calls Qt's 'QDir QDir::current()'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#current

    Returns
    -------

    QDir
      A new cute QDir around the copy Qt gave back. Python owns it.
    """
    #  QDir QDir::current()
    address = Rituals.call('ritual_ZN4QDir7currentEv')
    return QDir._cuteOwning(address)

  @staticmethod
  def currentPath() -> str:
    """
    Calls Qt's 'QString QDir::currentPath()'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#currentPath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDir::currentPath()
    return Rituals.call('ritual_ZN4QDir11currentPathEv')

  @staticmethod
  def home() -> QDir:
    """
    Calls Qt's 'QDir QDir::home()'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#home

    Returns
    -------

    QDir
      A new cute QDir around the copy Qt gave back. Python owns it.
    """
    #  QDir QDir::home()
    address = Rituals.call('ritual_ZN4QDir4homeEv')
    return QDir._cuteOwning(address)

  @staticmethod
  def homePath() -> str:
    """
    Calls Qt's 'QString QDir::homePath()'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#homePath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDir::homePath()
    return Rituals.call('ritual_ZN4QDir8homePathEv')

  @staticmethod
  def root() -> QDir:
    """
    Calls Qt's 'QDir QDir::root()'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#root

    Returns
    -------

    QDir
      A new cute QDir around the copy Qt gave back. Python owns it.
    """
    #  QDir QDir::root()
    address = Rituals.call('ritual_ZN4QDir4rootEv')
    return QDir._cuteOwning(address)

  @staticmethod
  def rootPath() -> str:
    """
    Calls Qt's 'QString QDir::rootPath()'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#rootPath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDir::rootPath()
    return Rituals.call('ritual_ZN4QDir8rootPathEv')

  @staticmethod
  def temp() -> QDir:
    """
    Calls Qt's 'QDir QDir::temp()'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#temp

    Returns
    -------

    QDir
      A new cute QDir around the copy Qt gave back. Python owns it.
    """
    #  QDir QDir::temp()
    address = Rituals.call('ritual_ZN4QDir4tempEv')
    return QDir._cuteOwning(address)

  @staticmethod
  def tempPath() -> str:
    """
    Calls Qt's 'QString QDir::tempPath()'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#tempPath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDir::tempPath()
    return Rituals.call('ritual_ZN4QDir8tempPathEv')

  @staticmethod
  @overload(QStringList, str)
  def match(filters: QStringList, fileName: str) -> bool:
    """
    Calls Qt's 'bool QDir::match(const QStringList &filters, const QString
    &fileName)'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#match

    Parameters
    ----------

    filters : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QDir::match(const QStringList &filters, const QString &fileName)
    return Rituals.call(
        'ritual_ZN4QDir5matchERK5QListI7QStringERKS1_',
        CuteMixin._valueOf(filters), fileName,
    )

  @staticmethod
  @overload(str, str)
  def match(filter: str, fileName: str) -> bool:
    """
    Calls Qt's 'bool QDir::match(const QString &filter, const QString
    &fileName)'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#match

    Parameters
    ----------

    filter : str
      Passed on as it is: a QString is made of it for the call.

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QDir::match(const QString &filter, const QString &fileName)
    return Rituals.call(
        'ritual_ZN4QDir5matchERK7QStringS2_', filter, fileName,
    )

  @staticmethod
  @overload(str)
  def cleanPath(path: str) -> str:
    """
    Calls Qt's 'QString QDir::cleanPath(const QString &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#cleanPath

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDir::cleanPath(const QString &path)
    return Rituals.call('ritual_ZN4QDir9cleanPathERK7QString', path)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDir'

  #  Qt's '~QDir()'. Naming it makes this a value class: Python owns every
  #  C++ QDir behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN4QDirD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def path(self) -> str:
    """
    Calls Qt's 'QString QDir::path() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#path

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDir::path() const
    return self.uglySide.call('ritual_ZNK4QDir4pathEv')

  def absolutePath(self) -> str:
    """
    Calls Qt's 'QString QDir::absolutePath() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#absolutePath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDir::absolutePath() const
    return self.uglySide.call('ritual_ZNK4QDir12absolutePathEv')

  def canonicalPath(self) -> str:
    """
    Calls Qt's 'QString QDir::canonicalPath() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#canonicalPath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDir::canonicalPath() const
    return self.uglySide.call('ritual_ZNK4QDir13canonicalPathEv')

  def dirName(self) -> str:
    """
    Calls Qt's 'QString QDir::dirName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#dirName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDir::dirName() const
    return self.uglySide.call('ritual_ZNK4QDir7dirNameEv')

  @overload(str)
  def filePath(self, fileName: str) -> str:
    """
    Calls Qt's 'QString QDir::filePath(const QString &fileName) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#filePath

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDir::filePath(const QString &fileName) const
    return self.uglySide.call(
        'ritual_ZNK4QDir8filePathERK7QString', fileName,
    )

  @overload(str)
  def absoluteFilePath(self, fileName: str) -> str:
    """
    Calls Qt's 'QString QDir::absoluteFilePath(const QString &fileName)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#absoluteFilePath

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDir::absoluteFilePath(const QString &fileName) const
    return self.uglySide.call(
        'ritual_ZNK4QDir16absoluteFilePathERK7QString', fileName,
    )

  @overload(str)
  def relativeFilePath(self, fileName: str) -> str:
    """
    Calls Qt's 'QString QDir::relativeFilePath(const QString &fileName)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#relativeFilePath

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDir::relativeFilePath(const QString &fileName) const
    return self.uglySide.call(
        'ritual_ZNK4QDir16relativeFilePathERK7QString', fileName,
    )

  def nameFilters(self) -> QStringList:
    """
    Calls Qt's 'QStringList QDir::nameFilters() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#nameFilters

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QDir::nameFilters() const
    address = self.uglySide.call('ritual_ZNK4QDir11nameFiltersEv')
    return QStringList._cuteOwning(address)

  def filter(self) -> Filters:
    """
    Calls Qt's 'Filters QDir::filter() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#filter

    Returns
    -------

    Filters
      The value standing for the combination Qt gave back.
    """
    #  Filters QDir::filter() const
    return QDir.Filters(self.uglySide.call('ritual_ZNK4QDir6filterEv'))

  def sorting(self) -> SortFlags:
    """
    Calls Qt's 'SortFlags QDir::sorting() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#sorting

    Returns
    -------

    SortFlags
      The value standing for the combination Qt gave back.
    """
    #  SortFlags QDir::sorting() const
    return QDir.SortFlags(self.uglySide.call('ritual_ZNK4QDir7sortingEv'))

  @overload()
  @overload(Filters)
  def isEmpty(
      self,
      filters: Filters = Filters.AllEntries | Filters.NoDotAndDotDot,
  ) -> bool:
    """
    Calls Qt's 'bool QDir::isEmpty(Filters filters) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#isEmpty

    Parameters
    ----------

    filters : Filters
      Passed on as its number. May be left out, as in Qt: it is then
      Filters.AllEntries | Filters.NoDotAndDotDot.
    """
    #  bool QDir::isEmpty(Filters filters) const
    return self.uglySide.call(
        'ritual_ZNK4QDir7isEmptyE6QFlagsINS_6FilterEE', filters.value,
    )

  @overload()
  @overload(Filters)
  @overload(Filters, SortFlags)
  def entryList(
      self,
      filters: Filters = Filters.NoFilter,
      sort: SortFlags = SortFlags.NoSort,
  ) -> QStringList:
    """
    Calls Qt's 'QStringList QDir::entryList(Filters filters, SortFlags sort)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#entryList

    Parameters
    ----------

    filters : Filters
      Passed on as its number. May be left out, as in Qt: it is then
      Filters.NoFilter.

    sort : SortFlags
      Passed on as its number. May be left out, as in Qt: it is then
      SortFlags.NoSort.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QDir::entryList(Filters filters, SortFlags sort) const
    address = self.uglySide.call(
        'ritual_ZNK4QDir9entryListE6QFlagsINS_6FilterEES0_INS_8SortFlagEE',
        filters.value, sort.value,
    )
    return QStringList._cuteOwning(address)

  @overload(QStringList)
  @overload(QStringList, Filters)
  @overload(QStringList, Filters, SortFlags)
  def entryList(
      self,
      nameFilters: QStringList,
      filters: Filters = Filters.NoFilter,
      sort: SortFlags = SortFlags.NoSort,
  ) -> QStringList:
    """
    Calls Qt's 'QStringList QDir::entryList(const QStringList &nameFilters,
    Filters filters, SortFlags sort) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#entryList

    Parameters
    ----------

    nameFilters : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    filters : Filters
      Passed on as its number. May be left out, as in Qt: it is then
      Filters.NoFilter.

    sort : SortFlags
      Passed on as its number. May be left out, as in Qt: it is then
      SortFlags.NoSort.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QDir::entryList(const QStringList &nameFilters, Filters
    #      filters, SortFlags sort) const
    address = self.uglySide.call(
        'ritual_ZNK4QDir9entryListERK5QListI7QStringE6QFlagsINS_6FilterEES5'
        '_INS_8SortFlagEE',
        self._valueOf(nameFilters), filters.value, sort.value,
    )
    return QStringList._cuteOwning(address)

  @overload()
  @overload(Filters)
  @overload(Filters, SortFlags)
  def entryInfoList(
      self,
      filters: Filters = Filters.NoFilter,
      sort: SortFlags = SortFlags.NoSort,
  ) -> QList[QFileInfo]:
    """
    Calls Qt's 'QFileInfoList QDir::entryInfoList(Filters filters, SortFlags
    sort) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#entryInfoList

    Parameters
    ----------

    filters : Filters
      Passed on as its number. May be left out, as in Qt: it is then
      Filters.NoFilter.

    sort : SortFlags
      Passed on as its number. May be left out, as in Qt: it is then
      SortFlags.NoSort.

    Returns
    -------

    QList[QFileInfo]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QFileInfoList QDir::entryInfoList(Filters filters, SortFlags sort)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK4QDir13entryInfoListE6QFlagsINS_6FilterEES0_INS_8SortFla'
        'gEE',
        filters.value, sort.value,
    )
    from . import QFileInfo
    return QList[QFileInfo]._cuteOwning(address)

  @overload(QStringList)
  @overload(QStringList, Filters)
  @overload(QStringList, Filters, SortFlags)
  def entryInfoList(
      self,
      nameFilters: QStringList,
      filters: Filters = Filters.NoFilter,
      sort: SortFlags = SortFlags.NoSort,
  ) -> QList[QFileInfo]:
    """
    Calls Qt's 'QFileInfoList QDir::entryInfoList(const QStringList
    &nameFilters, Filters filters, SortFlags sort) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#entryInfoList

    Parameters
    ----------

    nameFilters : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    filters : Filters
      Passed on as its number. May be left out, as in Qt: it is then
      Filters.NoFilter.

    sort : SortFlags
      Passed on as its number. May be left out, as in Qt: it is then
      SortFlags.NoSort.

    Returns
    -------

    QList[QFileInfo]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QFileInfoList QDir::entryInfoList(const QStringList &nameFilters,
    #      Filters filters, SortFlags sort) const
    address = self.uglySide.call(
        'ritual_ZNK4QDir13entryInfoListERK5QListI7QStringE6QFlagsINS_6Filte'
        'rEES5_INS_8SortFlagEE',
        self._valueOf(nameFilters), filters.value, sort.value,
    )
    from . import QFileInfo
    return QList[QFileInfo]._cuteOwning(address)

  @overload(str)
  def rmdir(self, dirName: str) -> bool:
    """
    Calls Qt's 'bool QDir::rmdir(const QString &dirName) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#rmdir

    Parameters
    ----------

    dirName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QDir::rmdir(const QString &dirName) const
    return self.uglySide.call('ritual_ZNK4QDir5rmdirERK7QString', dirName)

  @overload(str)
  def rmpath(self, dirPath: str) -> bool:
    """
    Calls Qt's 'bool QDir::rmpath(const QString &dirPath) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#rmpath

    Parameters
    ----------

    dirPath : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QDir::rmpath(const QString &dirPath) const
    return self.uglySide.call('ritual_ZNK4QDir6rmpathERK7QString', dirPath)

  def isReadable(self) -> bool:
    """
    Calls Qt's 'bool QDir::isReadable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#isReadable
    """
    #  bool QDir::isReadable() const
    return self.uglySide.call('ritual_ZNK4QDir10isReadableEv')

  @overload()
  def exists(self) -> bool:
    """
    Calls Qt's 'bool QDir::exists() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#exists
    """
    #  bool QDir::exists() const
    return self.uglySide.call('ritual_ZNK4QDir6existsEv')

  @overload(str)
  def exists(self, name: str) -> bool:
    """
    Calls Qt's 'bool QDir::exists(const QString &name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#exists

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QDir::exists(const QString &name) const
    return self.uglySide.call('ritual_ZNK4QDir6existsERK7QString', name)

  def isRoot(self) -> bool:
    """
    Calls Qt's 'bool QDir::isRoot() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#isRoot
    """
    #  bool QDir::isRoot() const
    return self.uglySide.call('ritual_ZNK4QDir6isRootEv')

  def isRelative(self) -> bool:
    """
    Calls Qt's 'bool QDir::isRelative() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#isRelative
    """
    #  bool QDir::isRelative() const
    return self.uglySide.call('ritual_ZNK4QDir10isRelativeEv')

  def isAbsolute(self) -> bool:
    """
    Calls Qt's 'bool QDir::isAbsolute() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#isAbsolute
    """
    #  bool QDir::isAbsolute() const
    return self.uglySide.call('ritual_ZNK4QDir10isAbsoluteEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setPath(self, path: str) -> None:
    """
    Calls Qt's 'void QDir::setPath(const QString &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#setPath

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDir::setPath(const QString &path)
    self.uglySide.call('ritual_ZN4QDir7setPathERK7QString', path)

  @overload(QStringList)
  def setNameFilters(self, nameFilters: QStringList) -> None:
    """
    Calls Qt's 'void QDir::setNameFilters(const QStringList &nameFilters)'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#setNameFilters

    Parameters
    ----------

    nameFilters : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QDir::setNameFilters(const QStringList &nameFilters)
    self.uglySide.call(
        'ritual_ZN4QDir14setNameFiltersERK5QListI7QStringE',
        self._valueOf(nameFilters),
    )

  @overload(Filters)
  def setFilter(self, filter: Filters) -> None:
    """
    Calls Qt's 'void QDir::setFilter(Filters filter)'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#setFilter

    Parameters
    ----------

    filter : Filters
      Passed on as its number.
    """
    #  void QDir::setFilter(Filters filter)
    self.uglySide.call(
        'ritual_ZN4QDir9setFilterE6QFlagsINS_6FilterEE', filter.value,
    )

  @overload(SortFlags)
  def setSorting(self, sort: SortFlags) -> None:
    """
    Calls Qt's 'void QDir::setSorting(SortFlags sort)'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#setSorting

    Parameters
    ----------

    sort : SortFlags
      Passed on as its number.
    """
    #  void QDir::setSorting(SortFlags sort)
    self.uglySide.call(
        'ritual_ZN4QDir10setSortingE6QFlagsINS_8SortFlagEE', sort.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def __getitem__(self, a0: int) -> str:
    """
    Calls Qt's 'QString QDir::operator[](qsizetype a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#operator[]

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDir::operator[](qsizetype a0) const
    return self.uglySide.call('ritual_ZNK4QDirixEx', a0)

  @overload(THIS)
  def __eq__(self, rhs: QDir) -> bool:
    """
    Calls Qt's 'bool operator==(const QDir &lhs, const QDir &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#operator==

    Parameters
    ----------

    rhs : QDir
      Passed on as a value: Qt reads the C++ QDir, which stays Python's own.
    """
    #  bool operator==(const QDir &lhs, const QDir &rhs)
    return Rituals.call(
        'ritual_ZeqRK4QDirS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: QDir) -> bool:
    """
    Calls Qt's 'bool operator!=(const QDir &lhs, const QDir &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#operator!=

    Parameters
    ----------

    rhs : QDir
      Passed on as a value: Qt reads the C++ QDir, which stays Python's own.
    """
    #  bool operator!=(const QDir &lhs, const QDir &rhs)
    return Rituals.call(
        'ritual_ZneRK4QDirS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __init__(self, a0: QDir) -> None:
    """
    Notes what was given, for Qt's 'QDir::QDir(const QDir &a0)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#QDir

    Parameters
    ----------

    a0 : QDir
      Passed on as a value: Qt reads the C++ QDir, which stays Python's own.
    """
    #  QDir::QDir(const QDir &a0)
    self._noteCreation(QDir, lambda: Rituals.call(
        'ritual_ZN4QDirC1ERKS_', self._valueOf(a0),
    ))

  @overload()
  @overload(str)
  def __init__(self, path: str = '') -> None:
    """
    Notes what was given, for Qt's 'QDir::QDir(const QString &path)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#QDir

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  QDir::QDir(const QString &path)
    self._noteCreation(QDir, lambda: Rituals.call(
        'ritual_ZN4QDirC1ERK7QString', path,
    ))

  @overload(str, str)
  @overload(str, str, SortFlags)
  @overload(str, str, SortFlags, Filters)
  def __init__(
      self,
      path: str,
      nameFilter: str,
      sort: SortFlags = SortFlags.Name | SortFlags.IgnoreCase,
      filter: Filters = Filters.AllEntries,
  ) -> None:
    """
    Notes what was given, for Qt's 'QDir::QDir(const QString &path, const
    QString &nameFilter, SortFlags sort, Filters filter)', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#QDir

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    nameFilter : str
      Passed on as it is: a QString is made of it for the call.

    sort : SortFlags
      Passed on as its number. May be left out, as in Qt: it is then
      SortFlags.Name | SortFlags.IgnoreCase.

    filter : Filters
      Passed on as its number. May be left out, as in Qt: it is then
      Filters.AllEntries.
    """
    #  QDir::QDir(const QString &path, const QString &nameFilter, SortFlags
    #      sort, Filters filter)
    self._noteCreation(QDir, lambda: Rituals.call(
        'ritual_ZN4QDirC1ERK7QStringS2_6QFlagsINS_8SortFlagEES3_INS_6Filter'
        'EE',
        path, nameFilter, sort.value, filter.value,
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

  @overload(str)
  def cd(self, dirName: str) -> bool:
    """
    Calls Qt's 'bool QDir::cd(const QString &dirName)'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#cd

    Parameters
    ----------

    dirName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QDir::cd(const QString &dirName)
    return self.uglySide.call('ritual_ZN4QDir2cdERK7QString', dirName)

  def cdUp(self) -> bool:
    """
    Calls Qt's 'bool QDir::cdUp()'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#cdUp
    """
    #  bool QDir::cdUp()
    return self.uglySide.call('ritual_ZN4QDir4cdUpEv')

  def removeRecursively(self) -> bool:
    """
    Calls Qt's 'bool QDir::removeRecursively()'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#removeRecursively
    """
    #  bool QDir::removeRecursively()
    return self.uglySide.call('ritual_ZN4QDir17removeRecursivelyEv')

  def makeAbsolute(self) -> bool:
    """
    Calls Qt's 'bool QDir::makeAbsolute()'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#makeAbsolute
    """
    #  bool QDir::makeAbsolute()
    return self.uglySide.call('ritual_ZN4QDir12makeAbsoluteEv')

  @overload(str)
  def remove(self, fileName: str) -> bool:
    """
    Calls Qt's 'bool QDir::remove(const QString &fileName)'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#remove

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QDir::remove(const QString &fileName)
    return self.uglySide.call('ritual_ZN4QDir6removeERK7QString', fileName)

  @overload(str, str)
  def rename(self, oldName: str, newName: str) -> bool:
    """
    Calls Qt's 'bool QDir::rename(const QString &oldName, const QString
    &newName)'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#rename

    Parameters
    ----------

    oldName : str
      Passed on as it is: a QString is made of it for the call.

    newName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QDir::rename(const QString &oldName, const QString &newName)
    return self.uglySide.call(
        'ritual_ZN4QDir6renameERK7QStringS2_', oldName, newName,
    )

  def refresh(self) -> None:
    """
    Calls Qt's 'void QDir::refresh() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdir.html#refresh
    """
    #  void QDir::refresh() const
    self.uglySide.call('ritual_ZNK4QDir7refreshEv')
