"""
QDirPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qdir_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QDirPrivate to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QDir, QDirListing, QSharedData, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QChar
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QChar = WAIT['QChar']


class QDirPrivate(QSharedData):
  """
  The cute side of Qt's QDirPrivate: a plain Python object standing in front
  of one C++ QDirPrivate.

  It is built on the cute 'QSharedData', as Qt's QDirPrivate is built on Qt's
  QSharedData, and has everything that class has.

  C++ hands a QDirPrivate around as a copy, so every C++ QDirPrivate behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDirPrivate that has a ritual and that Python can
  call so far, 5 names in all: 'toDirListingFlags',
  'checkNonDirListingFlags', 'initFileLists', 'getFilterSepChar',
  'splitFilters'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDirPrivate::~QDirPrivate()': the destructor: Python removes its
    C++ QDirPrivate by it, and has no other use for it.

  What has no ritual
  ------------------

  6 of the 13 functions Qt declares: 3 leans on 'QFileSystemEntry; 2 leans on
  'QFileSystemEngine; 1 Qt's library has no name for it, and its code in Qt's
  source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QDirPrivate is created at the first use, not by
    'QDirPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDirPrivate back gives a copy the ritual made for
    Python, in a new cute QDirPrivate.
  - Each name of Qt's QDirPrivate that has no cute function yet,
    'clearCache', 'exists', 'resolveAbsoluteEntry', 'setPath',
    'sortFileList', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QDirPrivate, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class MetaDataClearing(CuteNum):
    """
    The enum 'QDirPrivate::MetaDataClearing' of Qt, with the 2 names Qt gives
    in it.
    """

    KeepMetaData = Kee[int](0)
    IncludingMetaData = Kee[int](1)

  class PathNormalization(CuteFlags):
    """
    The flags enum 'QDirPrivate::PathNormalization' of Qt, with the 3 names
    Qt gives in it. Qt names the type of its combinations
    'QDirPrivate::PathNormalizations'.
    """

    DefaultNormalization = 0x0
    UrlNormalizationMode = 0x1
    RemotePath = 0x2

  PathNormalizations = PathNormalization

  #  The classes Qt writes inside QDirPrivate, each a class in here as in
  #  C++.

  class FileCache(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QDirPrivate::FileCache: a plain Python object
    standing in front of one C++ QDirPrivate::FileCache.

    What exists
    -----------

    No function of Qt's QDirPrivate::FileCache yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What to expect
    --------------

    - The C++ QDirPrivate::FileCache is created at the first use, not by
      'QDirPrivate::FileCache(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++ QDirPrivate::FileCache.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QDirPrivate::FileCache'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QDir.Filters)
  def toDirListingFlags(filters: QDir.Filters) -> QDirListing.IteratorFlags:
    """
    Calls Qt's 'QDirListing::IteratorFlags
    QDirPrivate::toDirListingFlags(QDir::Filters filters)'.

    Qt's own words: https://doc.qt.io/qt-6/qdirprivate.html#toDirListingFlags

    Parameters
    ----------

    filters : QDir.Filters
      Passed on as its number.

    Returns
    -------

    QDirListing.IteratorFlags
      The value standing for the combination Qt gave back.
    """
    #  QDirListing::IteratorFlags
    #      QDirPrivate::toDirListingFlags(QDir::Filters filters)
    return QDirListing.IteratorFlags(Rituals.call(
        'ritual_ZN11QDirPrivate17toDirListingFlagsE6QFlagsIN4QDir6FilterEE',
        filters.value,
    ))

  @staticmethod
  @overload(QDirListing.DirEntry, QDir.Filters)
  def checkNonDirListingFlags(
      dirEntry: QDirListing.DirEntry,
      filters: QDir.Filters,
  ) -> bool:
    """
    Calls Qt's 'bool QDirPrivate::checkNonDirListingFlags(const
    QDirListing::DirEntry &dirEntry, QDir::Filters filters)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdirprivate.html#checkNonDirListingFlags

    Parameters
    ----------

    dirEntry : QDirListing.DirEntry
      Passed on as a value: Qt reads the C++ QDirListing::DirEntry, which
      stays Python's own.

    filters : QDir.Filters
      Passed on as its number.
    """
    #  bool QDirPrivate::checkNonDirListingFlags(const QDirListing::DirEntry
    #      &dirEntry, QDir::Filters filters)
    return Rituals.call(
        'ritual_ZN11QDirPrivate23checkNonDirListingFlagsERKN11QDirListing8D'
        'irEntryE6QFlagsIN4QDir6FilterEE',
        CuteMixin._valueOf(dirEntry), filters.value,
    )

  @staticmethod
  @overload(str)
  def getFilterSepChar(nameFilter: str) -> QChar:
    """
    Calls Qt's 'QChar QDirPrivate::getFilterSepChar(const QString
    &nameFilter)'.

    Qt's own words: https://doc.qt.io/qt-6/qdirprivate.html#getFilterSepChar

    Parameters
    ----------

    nameFilter : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QChar
      A new cute QChar around the copy Qt gave back. Python owns it.
    """
    #  QChar QDirPrivate::getFilterSepChar(const QString &nameFilter)
    address = Rituals.call(
        'ritual_ZN11QDirPrivate16getFilterSepCharERK7QString', nameFilter,
    )
    from . import QChar
    return QChar._cuteOwning(address)

  @staticmethod
  @overload(str)
  @overload(str, QChar)
  def splitFilters(
      nameFilter: str,
      sep: Optional[QChar] = None,
  ) -> QStringList:
    """
    Calls Qt's 'QStringList QDirPrivate::splitFilters(const QString
    &nameFilter, QChar sep)'.

    Qt's own words: https://doc.qt.io/qt-6/qdirprivate.html#splitFilters

    Parameters
    ----------

    nameFilter : str
      Passed on as it is: a QString is made of it for the call.

    sep : Optional[QChar]
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
      May be left out, as in Qt: a new 'QChar()' is then passed on.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QDirPrivate::splitFilters(const QString &nameFilter, QChar
    #      sep)
    if sep is None:
      from . import QChar
      sep = QChar()
    address = Rituals.call(
        'ritual_ZN11QDirPrivate12splitFiltersERK7QString5QChar',
        nameFilter, CuteMixin._valueOf(sep),
    )
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDirPrivate'

  #  Qt's '~QDirPrivate()'. Naming it makes this a value class: Python owns
  #  every C++ QDirPrivate behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QDirPrivateD1Ev'

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

  @overload(THIS)
  def __init__(self, copy: QDirPrivate) -> None:
    """
    Notes what was given, for Qt's 'QDirPrivate::QDirPrivate(const
    QDirPrivate &copy)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdirprivate.html#QDirPrivate

    Parameters
    ----------

    copy : QDirPrivate
      Passed on as a value: Qt reads the C++ QDirPrivate, which stays
      Python's own.
    """
    #  QDirPrivate::QDirPrivate(const QDirPrivate &copy)
    self._noteCreation(QDirPrivate, lambda: Rituals.call(
        'ritual_ZN11QDirPrivateC1ERKS_', self._valueOf(copy),
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

  @overload(QDir)
  def initFileLists(self, dir: QDir) -> None:
    """
    Calls Qt's 'void QDirPrivate::initFileLists(const QDir &dir) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdirprivate.html#initFileLists

    Parameters
    ----------

    dir : QDir
      Passed on as a value: Qt reads the C++ QDir, which stays Python's own.
    """
    #  void QDirPrivate::initFileLists(const QDir &dir) const
    self.uglySide.call(
        'ritual_ZNK11QDirPrivate13initFileListsERK4QDir', self._valueOf(dir),
    )

  @staticmethod
  def clearCache(*__, **_) -> Never:
    """
    Qt's 'void QDirPrivate::clearCache(MetaDataClearing mode)': leans on
    'QFileSystemEngine::createLegacyEngine(QFileSystemEntry&,
    QFileSystemMetaData&)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDirPrivate.clearCache' has no cute function yet. Qt's 'void "
        "QDirPrivate::clearCache(MetaDataClearing mode)': leans on "
        "'QFileSystemEngine::createLegacyEngine(QFileSystemEntry&, "
        "QFileSystemMetaData&)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def exists(*__, **_) -> Never:
    """
    Qt's 'bool QDirPrivate::exists() const': leans on
    'QFileSystemEngine::fillMetaData(QFileSystemEntry const&,
    QFileSystemMetaData&, QFlags<QFileSystemMetaData::MetaDataFlag>)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QDirPrivate.exists' has no cute function yet. Qt's 'bool "
        "QDirPrivate::exists() const': leans on "
        "'QFileSystemEngine::fillMetaData(QFileSystemEntry const&, "
        "QFileSystemMetaData&, QFlags<QFileSystemMetaData::MetaDataFlag>)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def resolveAbsoluteEntry(*__, **_) -> Never:
    """
    Qt's 'QString QDirPrivate::resolveAbsoluteEntry() const': leans on
    'QFileSystemEntry::QFileSystemEntry(QString const&,
    QFileSystemEntry::FromInternalPath)', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDirPrivate.resolveAbsoluteEntry' has no cute function yet. Qt's "
        "'QString QDirPrivate::resolveAbsoluteEntry() const': leans on "
        "'QFileSystemEntry::QFileSystemEntry(QString const&, "
        "QFileSystemEntry::FromInternalPath)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setPath(*__, **_) -> Never:
    """
    Qt's 'void QDirPrivate::setPath(const QString &path)': leans on
    'QFileSystemEntry::QFileSystemEntry(QString const&,
    QFileSystemEntry::FromInternalPath)', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDirPrivate.setPath' has no cute function yet. Qt's 'void "
        "QDirPrivate::setPath(const QString &path)': leans on "
        "'QFileSystemEntry::QFileSystemEntry(QString const&, "
        "QFileSystemEntry::FromInternalPath)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def sortFileList(*__, **_) -> Never:
    """
    Qt's 'void QDirPrivate::sortFileList(QDir::SortFlags a0, const
    QFileInfoList &a1, QStringList *a2, QFileInfoList *a3)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'QDirSortItemComparator'.
    """
    raise NotImplementedError(
        "'QDirPrivate.sortFileList' has no cute function yet. Qt's 'void "
        "QDirPrivate::sortFileList(QDir::SortFlags a0, const QFileInfoList "
        "&a1, QStringList *a2, QFileInfoList *a3)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier "
        "'QDirSortItemComparator'.")
