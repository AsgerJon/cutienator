"""
QMimeBinaryProvider binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qmimeprovider_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QMimeBinaryProvider to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from . import QMimeProviderBase, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QMimeBinaryProvider(QMimeProviderBase):
  """
  The cute side of Qt's QMimeBinaryProvider: a plain Python object standing
  in front of one C++ QMimeBinaryProvider.

  It is built on the cute 'QMimeProviderBase', as Qt's QMimeBinaryProvider is
  built on Qt's QMimeProviderBase, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QMimeBinaryProvider that has a ritual and that
  Python can call so far, 6 names in all: 'isValid', 'isInternalDatabase',
  'knowsMimeType', 'hasGlobDeleteAll', 'globPatterns', 'loadMimeTypeList'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QMimeBinaryProvider::addAllMimeTypes(QList<QMimeType>
    &result)': takes a type Python has no way to hand over yet.
  - Qt's 'QMimeTypePrivate::LocaleHash
    QMimeBinaryProvider::localeComments(const QString &name)': gives a type
    Python has no way to take yet.

  What has no ritual
  ------------------

  16 of the 24 functions Qt declares: 10 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 5 the
  compiler refuses its ritual as it would be written here; 1 leans on
  'QMimeBinaryProvider.

  What to expect
  --------------

  - The C++ QMimeBinaryProvider is created at the first use, not by
    'QMimeBinaryProvider(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMimeBinaryProvider.
  - Each name of Qt's QMimeBinaryProvider that has no cute function yet,
    '__init__', 'checkCacheChanged', 'iconForMime', 'loadMimeTypeExtra',
    'matchGlobList', 'matchMagicRule', 'matchSuffixTree', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMimeBinaryProvider'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isInternalDatabase(self) -> bool:
    """
    Calls Qt's 'bool QMimeBinaryProvider::isInternalDatabase() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmimebinaryprovider.html#isInternalDatabase
    """
    #  bool QMimeBinaryProvider::isInternalDatabase() const
    return self.uglySide.call(
        'ritual_ZNK19QMimeBinaryProvider18isInternalDatabaseEv',
    )

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
    Qt's 'QMimeBinaryProvider::QMimeBinaryProvider(QMimeDatabasePrivate *db,
    const QString &directory)': Qt's library has no name for it, and its code
    in Qt's source does not compile apart from its file: invalid application
    of 'sizeof' to an incomplete type 'QMimeBinaryProvider::CacheFile'.
    """
    raise NotImplementedError(
        "'QMimeBinaryProvider.__init__' has no cute function yet. Qt's "
        "'QMimeBinaryProvider::QMimeBinaryProvider(QMimeDatabasePrivate "
        "*db, const QString &directory)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "invalid application of 'sizeof' to an incomplete type "
        "'QMimeBinaryProvider::CacheFile'.")

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

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QMimeBinaryProvider::isValid()'.

    Qt's own words: https://doc.qt.io/qt-6/qmimebinaryprovider.html#isValid
    """
    #  bool QMimeBinaryProvider::isValid()
    return self.uglySide.call('ritual_ZN19QMimeBinaryProvider7isValidEv')

  @overload(str)
  def knowsMimeType(self, name: str) -> bool:
    """
    Calls Qt's 'bool QMimeBinaryProvider::knowsMimeType(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmimebinaryprovider.html#knowsMimeType

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QMimeBinaryProvider::knowsMimeType(const QString &name)
    return self.uglySide.call(
        'ritual_ZN19QMimeBinaryProvider13knowsMimeTypeERK7QString', name,
    )

  @overload(str)
  def hasGlobDeleteAll(self, name: str) -> bool:
    """
    Calls Qt's 'bool QMimeBinaryProvider::hasGlobDeleteAll(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmimebinaryprovider.html#hasGlobDeleteAll

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QMimeBinaryProvider::hasGlobDeleteAll(const QString &name)
    return self.uglySide.call(
        'ritual_ZN19QMimeBinaryProvider16hasGlobDeleteAllERK7QString', name,
    )

  @overload(str)
  def globPatterns(self, name: str) -> QStringList:
    """
    Calls Qt's 'QStringList QMimeBinaryProvider::globPatterns(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmimebinaryprovider.html#globPatterns

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QMimeBinaryProvider::globPatterns(const QString &name)
    address = self.uglySide.call(
        'ritual_ZN19QMimeBinaryProvider12globPatternsERK7QString', name,
    )
    return QStringList._cuteOwning(address)

  def loadMimeTypeList(self) -> None:
    """
    Calls Qt's 'void QMimeBinaryProvider::loadMimeTypeList()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmimebinaryprovider.html#loadMimeTypeList
    """
    #  void QMimeBinaryProvider::loadMimeTypeList()
    self.uglySide.call('ritual_ZN19QMimeBinaryProvider16loadMimeTypeListEv')

  @staticmethod
  def checkCacheChanged(*__, **_) -> Never:
    """
    Qt's 'bool QMimeBinaryProvider::checkCacheChanged()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type
    'QMimeBinaryProvider::CacheFile'.
    """
    raise NotImplementedError(
        "'QMimeBinaryProvider.checkCacheChanged' has no cute function yet. "
        "Qt's 'bool QMimeBinaryProvider::checkCacheChanged()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: member access into incomplete type "
        "'QMimeBinaryProvider::CacheFile'.")

  @staticmethod
  def iconForMime(*__, **_) -> Never:
    """
    Qt's 'QLatin1StringView QMimeBinaryProvider::iconForMime(CacheFile
    *cacheFile, const RecordList &icons, QStringView inputMime)': the
    compiler refuses its ritual as it would be written here: unknown type
    name 'CacheFile'.
    """
    raise NotImplementedError(
        "'QMimeBinaryProvider.iconForMime' has no cute function yet. Qt's "
        "'QLatin1StringView QMimeBinaryProvider::iconForMime(CacheFile "
        "*cacheFile, const RecordList &icons, QStringView inputMime)': the "
        "compiler refuses its ritual as it would be written here: unknown "
        "type name 'CacheFile'.")

  @staticmethod
  def loadMimeTypeExtra(*__, **_) -> Never:
    """
    Qt's 'MimeTypeExtraMap::const_iterator
    QMimeBinaryProvider::loadMimeTypeExtra(const QString &mimeName)': the
    compiler refuses its ritual as it would be written here: use of
    undeclared identifier 'MimeTypeExtraMap'.
    """
    raise NotImplementedError(
        "'QMimeBinaryProvider.loadMimeTypeExtra' has no cute function yet. "
        "Qt's 'MimeTypeExtraMap::const_iterator "
        "QMimeBinaryProvider::loadMimeTypeExtra(const QString &mimeName)': "
        "the compiler refuses its ritual as it would be written here: use "
        "of undeclared identifier 'MimeTypeExtraMap'.")

  @staticmethod
  def matchGlobList(*__, **_) -> Never:
    """
    Qt's 'quint32 QMimeBinaryProvider::matchGlobList(QMimeGlobMatchResult
    &result, CacheFile *cacheFile, const RecordList &globs, const QString
    &fileName)': the compiler refuses its ritual as it would be written here:
    unknown type name 'CacheFile'.
    """
    raise NotImplementedError(
        "'QMimeBinaryProvider.matchGlobList' has no cute function yet. Qt's "
        "'quint32 QMimeBinaryProvider::matchGlobList(QMimeGlobMatchResult "
        "&result, CacheFile *cacheFile, const RecordList &globs, const "
        "QString &fileName)': the compiler refuses its ritual as it would "
        "be written here: unknown type name 'CacheFile'.")

  @staticmethod
  def matchMagicRule(*__, **_) -> Never:
    """
    Qt's 'bool QMimeBinaryProvider::matchMagicRule(CacheFile *cacheFile,
    quint32 numMatchlets, quint64 firstOffset, const QByteArray &data)': the
    compiler refuses its ritual as it would be written here: unknown type
    name 'CacheFile'.
    """
    raise NotImplementedError(
        "'QMimeBinaryProvider.matchMagicRule' has no cute function yet. "
        "Qt's 'bool QMimeBinaryProvider::matchMagicRule(CacheFile "
        "*cacheFile, quint32 numMatchlets, quint64 firstOffset, const "
        "QByteArray &data)': the compiler refuses its ritual as it would be "
        "written here: unknown type name 'CacheFile'.")

  @staticmethod
  def matchSuffixTree(*__, **_) -> Never:
    """
    Qt's 'bool QMimeBinaryProvider::matchSuffixTree(QMimeGlobMatchResult
    &result, CacheFile *cacheFile, quint32 numEntries, quint64 firstOffset,
    const QString &fileName, qsizetype charPos, bool caseSensitiveCheck)':
    the compiler refuses its ritual as it would be written here: unknown type
    name 'CacheFile'.
    """
    raise NotImplementedError(
        "'QMimeBinaryProvider.matchSuffixTree' has no cute function yet. "
        "Qt's 'bool "
        "QMimeBinaryProvider::matchSuffixTree(QMimeGlobMatchResult &result, "
        "CacheFile *cacheFile, quint32 numEntries, quint64 firstOffset, "
        "const QString &fileName, qsizetype charPos, bool "
        "caseSensitiveCheck)': the compiler refuses its ritual as it would "
        "be written here: unknown type name 'CacheFile'.")
