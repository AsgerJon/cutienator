"""
QDirEntryInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qdirentryinfo_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QDirEntryInfo to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QAbstractFileEngineIterator
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractFileEngineIterator = WAIT['QAbstractFileEngineIterator']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDirEntryInfo(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDirEntryInfo: a plain Python object standing in
  front of one C++ QDirEntryInfo.

  C++ hands a QDirEntryInfo around as a copy, so every C++ QDirEntryInfo
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDirEntryInfo that has a ritual and that Python can
  call so far, 2 names in all: 'fileName', 'filePath'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDirEntryInfo::QDirEntryInfo(QFileSystemEntry &&e,
    QFileSystemMetaData &&md)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QDirEntryInfo::QDirEntryInfo(QFileInfo &&info)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QDirEntryInfo::~QDirEntryInfo()': the destructor: Python removes
    its C++ QDirEntryInfo by it, and has no other use for it.

  What has no ritual
  ------------------

  23 of the 30 functions Qt declares: 16 leans on 'QFileSystemEngine; 4 leans
  on 'QFileSystemEntry; 3 a template.

  What to expect
  --------------

  - The C++ QDirEntryInfo is created at the first use, not by
    'QDirEntryInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDirEntryInfo back gives a copy the ritual made for
    Python, in a new cute QDirEntryInfo.
  - Each name of Qt's QDirEntryInfo that has no cute function yet,
    'absoluteFilePath', 'absolutePath', 'baseName', 'bundleName',
    'canonicalFilePath', 'completeBaseName', 'completeSuffix', 'exists',
    'fileInfo', 'fileTime', 'isDir', 'isExecutable', 'isFile', 'isHidden',
    'isReadable', 'isSymLink', 'isSymbolicLink', 'isWritable', 'query',
    'size', 'suffix', 'visit', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDirEntryInfo'

  #  Qt's '~QDirEntryInfo()'. Naming it makes this a value class: Python owns
  #  every C++ QDirEntryInfo behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QDirEntryInfoD1Ev'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QDirEntryInfo::QDirEntryInfo()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdirentryinfo.html#QDirEntryInfo
    """
    #  QDirEntryInfo::QDirEntryInfo()
    self._noteCreation(QDirEntryInfo, lambda: Rituals.call(
        'ritual_ZN13QDirEntryInfoC1Ev',
    ))

  @overload(QAbstractFileEngineIterator)
  @overload(NoneType)
  def __init__(
      self,
      iterator: Optional[QAbstractFileEngineIterator],
  ) -> None:
    """
    Notes what was given, for Qt's 'QDirEntryInfo::QDirEntryInfo(const
    QAbstractFileEngineIterator *iterator)', which is called at the first
    use.

    Qt's own words: https://doc.qt.io/qt-6/qdirentryinfo.html#QDirEntryInfo

    Parameters
    ----------

    iterator : Optional[QAbstractFileEngineIterator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QDirEntryInfo::QDirEntryInfo(const QAbstractFileEngineIterator
    #      *iterator)
    self._noteCreation(QDirEntryInfo, lambda: Rituals.call(
        'ritual_ZN13QDirEntryInfoC1EPK27QAbstractFileEngineIterator',
        self._addressOf(iterator),
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

  def fileName(self) -> str:
    """
    Calls Qt's 'QString QDirEntryInfo::fileName()'.

    Qt's own words: https://doc.qt.io/qt-6/qdirentryinfo.html#fileName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDirEntryInfo::fileName()
    return self.uglySide.call('ritual_ZN13QDirEntryInfo8fileNameEv')

  def filePath(self) -> str:
    """
    Calls Qt's 'QString QDirEntryInfo::filePath()'.

    Qt's own words: https://doc.qt.io/qt-6/qdirentryinfo.html#filePath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDirEntryInfo::filePath()
    return self.uglySide.call('ritual_ZN13QDirEntryInfo8filePathEv')

  @staticmethod
  def absoluteFilePath(*__, **_) -> Never:
    """
    Qt's 'QString QDirEntryInfo::absoluteFilePath()': leans on
    'QFileSystemEngine::createLegacyEngine(QFileSystemEntry&,
    QFileSystemMetaData&)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDirEntryInfo.absoluteFilePath' has no cute function yet. Qt's "
        "'QString QDirEntryInfo::absoluteFilePath()': leans on "
        "'QFileSystemEngine::createLegacyEngine(QFileSystemEntry&, "
        "QFileSystemMetaData&)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def absolutePath(*__, **_) -> Never:
    """
    Qt's 'QString QDirEntryInfo::absolutePath()': leans on
    'QFileSystemEngine::createLegacyEngine(QFileSystemEntry&,
    QFileSystemMetaData&)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDirEntryInfo.absolutePath' has no cute function yet. Qt's "
        "'QString QDirEntryInfo::absolutePath()': leans on "
        "'QFileSystemEngine::createLegacyEngine(QFileSystemEntry&, "
        "QFileSystemMetaData&)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def baseName(*__, **_) -> Never:
    """
    Qt's 'QString QDirEntryInfo::baseName()': leans on
    'QFileSystemEntry::findFileNameSeparators() const', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QDirEntryInfo.baseName' has no cute function yet. Qt's 'QString "
        "QDirEntryInfo::baseName()': leans on "
        "'QFileSystemEntry::findFileNameSeparators() const', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def bundleName(*__, **_) -> Never:
    """
    Qt's 'QString QDirEntryInfo::bundleName()': leans on
    'QFileSystemEngine::createLegacyEngine(QFileSystemEntry&,
    QFileSystemMetaData&)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDirEntryInfo.bundleName' has no cute function yet. Qt's 'QString "
        "QDirEntryInfo::bundleName()': leans on "
        "'QFileSystemEngine::createLegacyEngine(QFileSystemEntry&, "
        "QFileSystemMetaData&)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def canonicalFilePath(*__, **_) -> Never:
    """
    Qt's 'QString QDirEntryInfo::canonicalFilePath()': leans on
    'QFileSystemEngine::createLegacyEngine(QFileSystemEntry&,
    QFileSystemMetaData&)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDirEntryInfo.canonicalFilePath' has no cute function yet. Qt's "
        "'QString QDirEntryInfo::canonicalFilePath()': leans on "
        "'QFileSystemEngine::createLegacyEngine(QFileSystemEntry&, "
        "QFileSystemMetaData&)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def completeBaseName(*__, **_) -> Never:
    """
    Qt's 'QString QDirEntryInfo::completeBaseName()': leans on
    'QFileSystemEntry::findFileNameSeparators() const', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QDirEntryInfo.completeBaseName' has no cute function yet. Qt's "
        "'QString QDirEntryInfo::completeBaseName()': leans on "
        "'QFileSystemEntry::findFileNameSeparators() const', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def completeSuffix(*__, **_) -> Never:
    """
    Qt's 'QString QDirEntryInfo::completeSuffix()': leans on
    'QFileSystemEntry::findFileNameSeparators() const', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QDirEntryInfo.completeSuffix' has no cute function yet. Qt's "
        "'QString QDirEntryInfo::completeSuffix()': leans on "
        "'QFileSystemEntry::findFileNameSeparators() const', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def exists(*__, **_) -> Never:
    """
    Qt's 'bool QDirEntryInfo::exists()': leans on
    'QFileSystemEngine::fillMetaData(QFileSystemEntry const&,
    QFileSystemMetaData&, QFlags<QFileSystemMetaData::MetaDataFlag>)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QDirEntryInfo.exists' has no cute function yet. Qt's 'bool "
        "QDirEntryInfo::exists()': leans on "
        "'QFileSystemEngine::fillMetaData(QFileSystemEntry const&, "
        "QFileSystemMetaData&, QFlags<QFileSystemMetaData::MetaDataFlag>)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def fileInfo(*__, **_) -> Never:
    """
    Qt's 'const QFileInfo &QDirEntryInfo::fileInfo()': leans on
    'QFileSystemEngine::createLegacyEngine(QFileSystemEntry&,
    QFileSystemMetaData&)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDirEntryInfo.fileInfo' has no cute function yet. Qt's 'const "
        "QFileInfo &QDirEntryInfo::fileInfo()': leans on "
        "'QFileSystemEngine::createLegacyEngine(QFileSystemEntry&, "
        "QFileSystemMetaData&)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def fileTime(*__, **_) -> Never:
    """
    Qt's 'QDateTime QDirEntryInfo::fileTime(QFile::FileTime type, const
    QTimeZone &tz)': leans on
    'QFileSystemEngine::createLegacyEngine(QFileSystemEntry&,
    QFileSystemMetaData&)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDirEntryInfo.fileTime' has no cute function yet. Qt's 'QDateTime "
        "QDirEntryInfo::fileTime(QFile::FileTime type, const QTimeZone "
        "&tz)': leans on "
        "'QFileSystemEngine::createLegacyEngine(QFileSystemEntry&, "
        "QFileSystemMetaData&)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def isDir(*__, **_) -> Never:
    """
    Qt's 'bool QDirEntryInfo::isDir()': leans on
    'QFileSystemEngine::fillMetaData(QFileSystemEntry const&,
    QFileSystemMetaData&, QFlags<QFileSystemMetaData::MetaDataFlag>)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QDirEntryInfo.isDir' has no cute function yet. Qt's 'bool "
        "QDirEntryInfo::isDir()': leans on "
        "'QFileSystemEngine::fillMetaData(QFileSystemEntry const&, "
        "QFileSystemMetaData&, QFlags<QFileSystemMetaData::MetaDataFlag>)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def isExecutable(*__, **_) -> Never:
    """
    Qt's 'bool QDirEntryInfo::isExecutable()': leans on
    'QFileSystemEngine::fillMetaData(QFileSystemEntry const&,
    QFileSystemMetaData&, QFlags<QFileSystemMetaData::MetaDataFlag>)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QDirEntryInfo.isExecutable' has no cute function yet. Qt's 'bool "
        "QDirEntryInfo::isExecutable()': leans on "
        "'QFileSystemEngine::fillMetaData(QFileSystemEntry const&, "
        "QFileSystemMetaData&, QFlags<QFileSystemMetaData::MetaDataFlag>)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def isFile(*__, **_) -> Never:
    """
    Qt's 'bool QDirEntryInfo::isFile()': leans on
    'QFileSystemEngine::fillMetaData(QFileSystemEntry const&,
    QFileSystemMetaData&, QFlags<QFileSystemMetaData::MetaDataFlag>)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QDirEntryInfo.isFile' has no cute function yet. Qt's 'bool "
        "QDirEntryInfo::isFile()': leans on "
        "'QFileSystemEngine::fillMetaData(QFileSystemEntry const&, "
        "QFileSystemMetaData&, QFlags<QFileSystemMetaData::MetaDataFlag>)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def isHidden(*__, **_) -> Never:
    """
    Qt's 'bool QDirEntryInfo::isHidden()': leans on
    'QFileSystemEngine::fillMetaData(QFileSystemEntry const&,
    QFileSystemMetaData&, QFlags<QFileSystemMetaData::MetaDataFlag>)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QDirEntryInfo.isHidden' has no cute function yet. Qt's 'bool "
        "QDirEntryInfo::isHidden()': leans on "
        "'QFileSystemEngine::fillMetaData(QFileSystemEntry const&, "
        "QFileSystemMetaData&, QFlags<QFileSystemMetaData::MetaDataFlag>)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def isReadable(*__, **_) -> Never:
    """
    Qt's 'bool QDirEntryInfo::isReadable()': leans on
    'QFileSystemEngine::fillMetaData(QFileSystemEntry const&,
    QFileSystemMetaData&, QFlags<QFileSystemMetaData::MetaDataFlag>)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QDirEntryInfo.isReadable' has no cute function yet. Qt's 'bool "
        "QDirEntryInfo::isReadable()': leans on "
        "'QFileSystemEngine::fillMetaData(QFileSystemEntry const&, "
        "QFileSystemMetaData&, QFlags<QFileSystemMetaData::MetaDataFlag>)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def isSymLink(*__, **_) -> Never:
    """
    Qt's 'bool QDirEntryInfo::isSymLink()': leans on
    'QFileSystemEngine::fillMetaData(QFileSystemEntry const&,
    QFileSystemMetaData&, QFlags<QFileSystemMetaData::MetaDataFlag>)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QDirEntryInfo.isSymLink' has no cute function yet. Qt's 'bool "
        "QDirEntryInfo::isSymLink()': leans on "
        "'QFileSystemEngine::fillMetaData(QFileSystemEntry const&, "
        "QFileSystemMetaData&, QFlags<QFileSystemMetaData::MetaDataFlag>)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def isSymbolicLink(*__, **_) -> Never:
    """
    Qt's 'bool QDirEntryInfo::isSymbolicLink()': leans on
    'QFileSystemEngine::fillMetaData(QFileSystemEntry const&,
    QFileSystemMetaData&, QFlags<QFileSystemMetaData::MetaDataFlag>)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QDirEntryInfo.isSymbolicLink' has no cute function yet. Qt's "
        "'bool QDirEntryInfo::isSymbolicLink()': leans on "
        "'QFileSystemEngine::fillMetaData(QFileSystemEntry const&, "
        "QFileSystemMetaData&, QFlags<QFileSystemMetaData::MetaDataFlag>)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def isWritable(*__, **_) -> Never:
    """
    Qt's 'bool QDirEntryInfo::isWritable()': leans on
    'QFileSystemEngine::fillMetaData(QFileSystemEntry const&,
    QFileSystemMetaData&, QFlags<QFileSystemMetaData::MetaDataFlag>)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QDirEntryInfo.isWritable' has no cute function yet. Qt's 'bool "
        "QDirEntryInfo::isWritable()': leans on "
        "'QFileSystemEngine::fillMetaData(QFileSystemEntry const&, "
        "QFileSystemMetaData&, QFlags<QFileSystemMetaData::MetaDataFlag>)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def query(*__, **_) -> Never:
    """
    Qt's 'QDirEntryInfo::query': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QDirEntryInfo.query' has no cute function yet. Qt's "
        "'QDirEntryInfo::query': a template: a pattern and no single "
        "function.")

  @staticmethod
  def size(*__, **_) -> Never:
    """
    Qt's 'qint64 QDirEntryInfo::size()': leans on
    'QFileSystemEngine::createLegacyEngine(QFileSystemEntry&,
    QFileSystemMetaData&)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDirEntryInfo.size' has no cute function yet. Qt's 'qint64 "
        "QDirEntryInfo::size()': leans on "
        "'QFileSystemEngine::createLegacyEngine(QFileSystemEntry&, "
        "QFileSystemMetaData&)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def suffix(*__, **_) -> Never:
    """
    Qt's 'QString QDirEntryInfo::suffix()': leans on
    'QFileSystemEntry::findFileNameSeparators() const', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QDirEntryInfo.suffix' has no cute function yet. Qt's 'QString "
        "QDirEntryInfo::suffix()': leans on "
        "'QFileSystemEntry::findFileNameSeparators() const', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def visit(*__, **_) -> Never:
    """
    Qt's 'QDirEntryInfo::visit': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QDirEntryInfo.visit' has no cute function yet. Qt's "
        "'QDirEntryInfo::visit': a template: a pattern and no single "
        "function.")
