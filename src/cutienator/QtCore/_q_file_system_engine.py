"""
QFileSystemEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qfilesystemengine_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QFileSystemEngine to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QAbstractFileEngine, QFileDevice

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QByteArray, QFileSystemEntry, QFileSystemMetaData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFileSystemEntry = WAIT['QFileSystemEntry']
  QFileSystemMetaData = WAIT['QFileSystemMetaData']


class QFileSystemEngine(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QFileSystemEngine: a plain Python object standing in
  front of one C++ QFileSystemEngine.

  C++ hands a QFileSystemEngine around as a copy, so every C++
  QFileSystemEngine behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QFileSystemEngine that has a ritual and that Python
  can call so far, 6 names in all: 'resolveUserName', 'resolveGroupName',
  'bundleName', 'cloneFile', 'id', 'slowCanonicalized'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFileSystemEntry QFileSystemEngine::getJunctionTarget(const
    QFileSystemEntry &link, QFileSystemMetaData &data)': takes a type Python
    has no way to hand over yet.
  - Qt's 'bool QFileSystemEngine::setFileTime(int fd, const QDateTime
    &newDate, QFile::FileTime whatTime, QSystemError &error)': takes a type
    Python has no way to hand over yet.
  - Qt's 'bool QFileSystemEngine::setPermissions(int fd, QFile::Permissions
    permissions, QSystemError &error)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QFileSystemEngine::~QFileSystemEngine()': the destructor: Python
    removes its C++ QFileSystemEngine by it, and has no other use for it.

  What has no ritual
  ------------------

  32 of the 42 functions Qt declares: 25 cannot be called and cannot be
  called through the meta-object and cannot be copied; 4 leans on
  'QFileSystemEngine; 1 Qt's library has no name for it, and its code in Qt's
  source does not compile apart from its file; 1 leans on
  'QFileSystemMetaData; 1 leans on 'QFileSystemEntry.

  What to expect
  --------------

  - The C++ QFileSystemEngine is created at the first use, not by
    'QFileSystemEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QFileSystemEngine back gives a copy the ritual made
    for Python, in a new cute QFileSystemEngine.
  - Each name of Qt's QFileSystemEngine that has no cute function yet,
    'absoluteName', 'canonicalName', 'copyFile', 'createDirectory',
    'createLegacyEngine', 'createLink', 'currentPath', 'fillMetaData',
    'getJunctionTarget', 'getLinkTarget', 'getRawLinkPath', 'homePath',
    'isCaseSensitive', 'mkdir', 'mkpath', 'moveFileToTrash',
    'removeDirectory', 'removeFile', 'renameFile', 'renameOverwriteFile',
    'rmdir', 'rmpath', 'rootPath', 'setCurrentPath', 'setFileTime',
    'setPermissions', 'supportsMoveFileToTrash', 'tempPath', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(int)
  def resolveUserName(userId: int) -> str:
    """
    Calls Qt's 'QString QFileSystemEngine::resolveUserName(uint userId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemengine.html#resolveUserName

    Parameters
    ----------

    userId : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileSystemEngine::resolveUserName(uint userId)
    return Rituals.call(
        'ritual_ZN17QFileSystemEngine15resolveUserNameEj', userId,
    )

  @staticmethod
  @overload(int)
  def resolveGroupName(groupId: int) -> str:
    """
    Calls Qt's 'QString QFileSystemEngine::resolveGroupName(uint groupId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemengine.html#resolveGroupName

    Parameters
    ----------

    groupId : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileSystemEngine::resolveGroupName(uint groupId)
    return Rituals.call(
        'ritual_ZN17QFileSystemEngine16resolveGroupNameEj', groupId,
    )

  @staticmethod
  @overload(QFileSystemEntry)
  def bundleName(a0: QFileSystemEntry) -> str:
    """
    Calls Qt's 'QString QFileSystemEngine::bundleName(const QFileSystemEntry
    &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemengine.html#bundleName

    Parameters
    ----------

    a0 : QFileSystemEntry
      Passed on as a value: Qt reads the C++ QFileSystemEntry, which stays
      Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileSystemEngine::bundleName(const QFileSystemEntry &a0)
    return Rituals.call(
        'ritual_ZN17QFileSystemEngine10bundleNameERK16QFileSystemEntry',
        CuteMixin._valueOf(a0),
    )

  @staticmethod
  @overload(int, int, QFileSystemMetaData)
  def cloneFile(
      srcfd: int,
      dstfd: int,
      knownData: QFileSystemMetaData,
  ) -> QAbstractFileEngine.TriStateResult:
    """
    Calls Qt's 'TriStateResult QFileSystemEngine::cloneFile(int srcfd, int
    dstfd, const QFileSystemMetaData &knownData)'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemengine.html#cloneFile

    Parameters
    ----------

    srcfd : int
      Passed on as it is.

    dstfd : int
      Passed on as it is.

    knownData : QFileSystemMetaData
      Passed on as a value: Qt reads the C++ QFileSystemMetaData, which stays
      Python's own.

    Returns
    -------

    QAbstractFileEngine.TriStateResult
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstractFileEngine.TriStateResult(number)' gives.
    """
    #  TriStateResult QFileSystemEngine::cloneFile(int srcfd, int dstfd,
    #      const QFileSystemMetaData &knownData)
    return QAbstractFileEngine.TriStateResult(Rituals.call(
        'ritual_ZN17QFileSystemEngine9cloneFileEiiRK19QFileSystemMetaData',
        srcfd, dstfd, CuteMixin._valueOf(knownData),
    ))

  @staticmethod
  @overload(int)
  def id(fd: int) -> QByteArray:
    """
    Calls Qt's 'QByteArray QFileSystemEngine::id(int fd)'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemengine.html#id

    Parameters
    ----------

    fd : int
      Passed on as it is.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QFileSystemEngine::id(int fd)
    address = Rituals.call('ritual_ZN17QFileSystemEngine2idEi', fd)
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  @staticmethod
  @overload(str)
  def slowCanonicalized(path: str) -> str:
    """
    Calls Qt's 'QString QFileSystemEngine::slowCanonicalized(const QString
    &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemengine.html#slowCanonicalized

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileSystemEngine::slowCanonicalized(const QString &path)
    return Rituals.call(
        'ritual_ZN17QFileSystemEngine17slowCanonicalizedERK7QString', path,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFileSystemEngine'

  #  Qt's '~QFileSystemEngine()'. Naming it makes this a value class: Python
  #  owns every C++ QFileSystemEngine behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QFileSystemEngineD1Ev'

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

  @staticmethod
  def absoluteName(*__, **_) -> Never:
    """
    Qt's 'QFileSystemEntry QFileSystemEngine::absoluteName(const
    QFileSystemEntry &entry)': cannot be called and cannot be called through
    the meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QFileSystemEngine.absoluteName' has no cute function yet. Qt's "
        "'QFileSystemEntry QFileSystemEngine::absoluteName(const "
        "QFileSystemEntry &entry)': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def canonicalName(*__, **_) -> Never:
    """
    Qt's 'QFileSystemEntry QFileSystemEngine::canonicalName(const
    QFileSystemEntry &entry, QFileSystemMetaData &data)': cannot be called
    and cannot be called through the meta-object and cannot be copied: no
    header file has its code, Qt's source does not mark it or its class for
    use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QFileSystemEngine.canonicalName' has no cute function yet. Qt's "
        "'QFileSystemEntry QFileSystemEngine::canonicalName(const "
        "QFileSystemEntry &entry, QFileSystemMetaData &data)': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def copyFile(*__, **_) -> Never:
    """
    Qt's 'bool QFileSystemEngine::copyFile(const QFileSystemEntry &source,
    const QFileSystemEntry &target, QSystemError &error)': cannot be called
    and cannot be called through the meta-object and cannot be copied: no
    header file has its code, Qt's source does not mark it or its class for
    use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QFileSystemEngine.copyFile' has no cute function yet. Qt's 'bool "
        "QFileSystemEngine::copyFile(const QFileSystemEntry &source, const "
        "QFileSystemEntry &target, QSystemError &error)': cannot be called "
        "and cannot be called through the meta-object and cannot be copied: "
        "no header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def createDirectory(*__, **_) -> Never:
    """
    Qt's 'bool QFileSystemEngine::createDirectory(const QFileSystemEntry
    &entry, bool createParents, std::optional<QFile::Permissions>
    permissions)': leans on 'QFileSystemEngine::mkdir(QFileSystemEntry
    const&, std::optional<QFlags<QFileDevice::Permission> >)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QFileSystemEngine.createDirectory' has no cute function yet. Qt's "
        "'bool QFileSystemEngine::createDirectory(const QFileSystemEntry "
        "&entry, bool createParents, std::optional<QFile::Permissions> "
        "permissions)': leans on 'QFileSystemEngine::mkdir(QFileSystemEntry "
        "const&, std::optional<QFlags<QFileDevice::Permission> >)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def createLegacyEngine(*__, **_) -> Never:
    """
    - Qt's 'std::unique_ptr<QAbstractFileEngine>
      QFileSystemEngine::createLegacyEngine(QFileSystemEntry &entry,
      QFileSystemMetaData &data)': Qt's library has no name for it, and its
      code in Qt's source does not compile apart from its file: use of
      undeclared identifier '_q_createLegacyEngine_recursive'.
    - Qt's 'std::unique_ptr<QAbstractFileEngine>
      QFileSystemEngine::createLegacyEngine(const QString &fileName)': leans
      on 'QFileSystemEntry::QFileSystemEntry(QString const&)', which Qt's
      source does not mark for use from outside Qt and has no code for that
      could be taken.
    """
    raise NotImplementedError(
        "'QFileSystemEngine.createLegacyEngine' has no cute function yet. "
        "Qt's 'std::unique_ptr<QAbstractFileEngine> "
        "QFileSystemEngine::createLegacyEngine(QFileSystemEntry &entry, "
        "QFileSystemMetaData &data)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier '_q_createLegacyEngine_recursive'. Qt's "
        "'std::unique_ptr<QAbstractFileEngine> "
        "QFileSystemEngine::createLegacyEngine(const QString &fileName)': "
        "leans on 'QFileSystemEntry::QFileSystemEntry(QString const&)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def createLink(*__, **_) -> Never:
    """
    Qt's 'bool QFileSystemEngine::createLink(const QFileSystemEntry &source,
    const QFileSystemEntry &target, QSystemError &error)': cannot be called
    and cannot be called through the meta-object and cannot be copied: no
    header file has its code, Qt's source does not mark it or its class for
    use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QFileSystemEngine.createLink' has no cute function yet. Qt's "
        "'bool QFileSystemEngine::createLink(const QFileSystemEntry "
        "&source, const QFileSystemEntry &target, QSystemError &error)': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def currentPath(*__, **_) -> Never:
    """
    Qt's 'QFileSystemEntry QFileSystemEngine::currentPath()': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QFileSystemEngine.currentPath' has no cute function yet. Qt's "
        "'QFileSystemEntry QFileSystemEngine::currentPath()': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def fillMetaData(*__, **_) -> Never:
    """
    - Qt's 'bool QFileSystemEngine::fillMetaData(const QFileSystemEntry
      &entry, QFileSystemMetaData &data, QFileSystemMetaData::MetaDataFlags
      what)': cannot be called and cannot be called through the meta-object
      and cannot be copied: no header file has its code, Qt's source does not
      mark it or its class for use from outside Qt or writes it 'inline' or
      nowhere, and it is no signal, slot or invokable function giving back
      nothing, of a class built on QObject, and Qt's source has no code for
      it that could be told from the rest.
    - Qt's 'bool QFileSystemEngine::fillMetaData(int fd, QFileSystemMetaData
      &data)': leans on 'QFileSystemMetaData::fillFromStatxBuf(statx
      const&)', which Qt's source does not mark for use from outside Qt and
      has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QFileSystemEngine.fillMetaData' has no cute function yet. Qt's "
        "'bool QFileSystemEngine::fillMetaData(const QFileSystemEntry "
        "&entry, QFileSystemMetaData &data, "
        "QFileSystemMetaData::MetaDataFlags what)': cannot be called and "
        "cannot be called through the meta-object and cannot be copied: no "
        "header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest. Qt's 'bool "
        "QFileSystemEngine::fillMetaData(int fd, QFileSystemMetaData "
        "&data)': leans on 'QFileSystemMetaData::fillFromStatxBuf(statx "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def getJunctionTarget(*__, **_) -> Never:
    """
    Qt's 'QFileSystemEntry QFileSystemEngine::getJunctionTarget(const
    QFileSystemEntry &link, QFileSystemMetaData &data)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QFileSystemEngine.getJunctionTarget' has no cute function yet. "
        "Qt's 'QFileSystemEntry QFileSystemEngine::getJunctionTarget(const "
        "QFileSystemEntry &link, QFileSystemMetaData &data)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def getLinkTarget(*__, **_) -> Never:
    """
    Qt's 'QFileSystemEntry QFileSystemEngine::getLinkTarget(const
    QFileSystemEntry &link, QFileSystemMetaData &data)': cannot be called and
    cannot be called through the meta-object and cannot be copied: no header
    file has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QFileSystemEngine.getLinkTarget' has no cute function yet. Qt's "
        "'QFileSystemEntry QFileSystemEngine::getLinkTarget(const "
        "QFileSystemEntry &link, QFileSystemMetaData &data)': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def getRawLinkPath(*__, **_) -> Never:
    """
    Qt's 'QFileSystemEntry QFileSystemEngine::getRawLinkPath(const
    QFileSystemEntry &link, QFileSystemMetaData &data)': cannot be called and
    cannot be called through the meta-object and cannot be copied: no header
    file has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QFileSystemEngine.getRawLinkPath' has no cute function yet. Qt's "
        "'QFileSystemEntry QFileSystemEngine::getRawLinkPath(const "
        "QFileSystemEntry &link, QFileSystemMetaData &data)': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def homePath(*__, **_) -> Never:
    """
    Qt's 'QString QFileSystemEngine::homePath()': cannot be called and cannot
    be called through the meta-object and cannot be copied: no header file
    has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QFileSystemEngine.homePath' has no cute function yet. Qt's "
        "'QString QFileSystemEngine::homePath()': cannot be called and "
        "cannot be called through the meta-object and cannot be copied: no "
        "header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def isCaseSensitive(*__, **_) -> Never:
    """
    Qt's 'bool QFileSystemEngine::isCaseSensitive(const QFileSystemEntry
    &entry, QFileSystemMetaData &data)': cannot be called and cannot be
    called through the meta-object and cannot be copied: no header file has
    its code, Qt's source does not mark it or its class for use from outside
    Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QFileSystemEngine.isCaseSensitive' has no cute function yet. Qt's "
        "'bool QFileSystemEngine::isCaseSensitive(const QFileSystemEntry "
        "&entry, QFileSystemMetaData &data)': cannot be called and cannot "
        "be called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")

  @staticmethod
  def mkdir(*__, **_) -> Never:
    """
    Qt's 'bool QFileSystemEngine::mkdir(const QFileSystemEntry &entry,
    std::optional<QFile::Permissions> permissions)': cannot be called and
    cannot be called through the meta-object and cannot be copied: no header
    file has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QFileSystemEngine.mkdir' has no cute function yet. Qt's 'bool "
        "QFileSystemEngine::mkdir(const QFileSystemEntry &entry, "
        "std::optional<QFile::Permissions> permissions)': cannot be called "
        "and cannot be called through the meta-object and cannot be copied: "
        "no header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def mkpath(*__, **_) -> Never:
    """
    Qt's 'bool QFileSystemEngine::mkpath(const QFileSystemEntry &entry,
    std::optional<QFile::Permissions> permissions)': cannot be called and
    cannot be called through the meta-object and cannot be copied: no header
    file has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QFileSystemEngine.mkpath' has no cute function yet. Qt's 'bool "
        "QFileSystemEngine::mkpath(const QFileSystemEntry &entry, "
        "std::optional<QFile::Permissions> permissions)': cannot be called "
        "and cannot be called through the meta-object and cannot be copied: "
        "no header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def moveFileToTrash(*__, **_) -> Never:
    """
    Qt's 'bool QFileSystemEngine::moveFileToTrash(const QFileSystemEntry
    &source, QFileSystemEntry &newLocation, QSystemError &error)': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QFileSystemEngine.moveFileToTrash' has no cute function yet. Qt's "
        "'bool QFileSystemEngine::moveFileToTrash(const QFileSystemEntry "
        "&source, QFileSystemEntry &newLocation, QSystemError &error)': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def removeDirectory(*__, **_) -> Never:
    """
    Qt's 'bool QFileSystemEngine::removeDirectory(const QFileSystemEntry
    &entry, bool removeEmptyParents)': leans on
    'QFileSystemEngine::rmdir(QFileSystemEntry const&)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QFileSystemEngine.removeDirectory' has no cute function yet. Qt's "
        "'bool QFileSystemEngine::removeDirectory(const QFileSystemEntry "
        "&entry, bool removeEmptyParents)': leans on "
        "'QFileSystemEngine::rmdir(QFileSystemEntry const&)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def removeFile(*__, **_) -> Never:
    """
    Qt's 'bool QFileSystemEngine::removeFile(const QFileSystemEntry &entry,
    QSystemError &error)': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QFileSystemEngine.removeFile' has no cute function yet. Qt's "
        "'bool QFileSystemEngine::removeFile(const QFileSystemEntry &entry, "
        "QSystemError &error)': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def renameFile(*__, **_) -> Never:
    """
    Qt's 'bool QFileSystemEngine::renameFile(const QFileSystemEntry &source,
    const QFileSystemEntry &target, QSystemError &error)': cannot be called
    and cannot be called through the meta-object and cannot be copied: no
    header file has its code, Qt's source does not mark it or its class for
    use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QFileSystemEngine.renameFile' has no cute function yet. Qt's "
        "'bool QFileSystemEngine::renameFile(const QFileSystemEntry "
        "&source, const QFileSystemEntry &target, QSystemError &error)': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def renameOverwriteFile(*__, **_) -> Never:
    """
    Qt's 'bool QFileSystemEngine::renameOverwriteFile(const QFileSystemEntry
    &source, const QFileSystemEntry &target, QSystemError &error)': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QFileSystemEngine.renameOverwriteFile' has no cute function yet. "
        "Qt's 'bool QFileSystemEngine::renameOverwriteFile(const "
        "QFileSystemEntry &source, const QFileSystemEntry &target, "
        "QSystemError &error)': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def rmdir(*__, **_) -> Never:
    """
    Qt's 'bool QFileSystemEngine::rmdir(const QFileSystemEntry &entry)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QFileSystemEngine.rmdir' has no cute function yet. Qt's 'bool "
        "QFileSystemEngine::rmdir(const QFileSystemEntry &entry)': cannot "
        "be called and cannot be called through the meta-object and cannot "
        "be copied: no header file has its code, Qt's source does not mark "
        "it or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def rmpath(*__, **_) -> Never:
    """
    Qt's 'bool QFileSystemEngine::rmpath(const QFileSystemEntry &entry)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QFileSystemEngine.rmpath' has no cute function yet. Qt's 'bool "
        "QFileSystemEngine::rmpath(const QFileSystemEntry &entry)': cannot "
        "be called and cannot be called through the meta-object and cannot "
        "be copied: no header file has its code, Qt's source does not mark "
        "it or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def rootPath(*__, **_) -> Never:
    """
    Qt's 'QString QFileSystemEngine::rootPath()': cannot be called and cannot
    be called through the meta-object and cannot be copied: no header file
    has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QFileSystemEngine.rootPath' has no cute function yet. Qt's "
        "'QString QFileSystemEngine::rootPath()': cannot be called and "
        "cannot be called through the meta-object and cannot be copied: no "
        "header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def setCurrentPath(*__, **_) -> Never:
    """
    Qt's 'bool QFileSystemEngine::setCurrentPath(const QFileSystemEntry
    &entry)': cannot be called and cannot be called through the meta-object
    and cannot be copied: no header file has its code, Qt's source does not
    mark it or its class for use from outside Qt or writes it 'inline' or
    nowhere, and it is no signal, slot or invokable function giving back
    nothing, of a class built on QObject, and Qt's source has no code for it
    that could be told from the rest.
    """
    raise NotImplementedError(
        "'QFileSystemEngine.setCurrentPath' has no cute function yet. Qt's "
        "'bool QFileSystemEngine::setCurrentPath(const QFileSystemEntry "
        "&entry)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def setFileTime(*__, **_) -> Never:
    """
    - Qt's 'bool QFileSystemEngine::setFileTime(int fd, const QDateTime
      &newDate, QFile::FileTime whatTime, QSystemError &error)': takes a type
      Python has no way to hand over yet.
    - Qt's 'bool QFileSystemEngine::setFileTime(const QFileSystemEntry
      &entry, const QDateTime &newDate, QFile::FileTime whatTime,
      QSystemError &error)': cannot be called and cannot be called through
      the meta-object and cannot be copied: no header file has its code, Qt's
      source does not mark it or its class for use from outside Qt or writes
      it 'inline' or nowhere, and it is no signal, slot or invokable function
      giving back nothing, of a class built on QObject, and Qt's source has
      no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QFileSystemEngine.setFileTime' has no cute function yet. Qt's "
        "'bool QFileSystemEngine::setFileTime(int fd, const QDateTime "
        "&newDate, QFile::FileTime whatTime, QSystemError &error)': takes a "
        "type Python has no way to hand over yet. Qt's 'bool "
        "QFileSystemEngine::setFileTime(const QFileSystemEntry &entry, "
        "const QDateTime &newDate, QFile::FileTime whatTime, QSystemError "
        "&error)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def setPermissions(*__, **_) -> Never:
    """
    - Qt's 'bool QFileSystemEngine::setPermissions(int fd, QFile::Permissions
      permissions, QSystemError &error)': takes a type Python has no way to
      hand over yet.
    - Qt's 'bool QFileSystemEngine::setPermissions(const QFileSystemEntry
      &entry, QFile::Permissions permissions, QSystemError &error)': cannot
      be called and cannot be called through the meta-object and cannot be
      copied: no header file has its code, Qt's source does not mark it or
      its class for use from outside Qt or writes it 'inline' or nowhere, and
      it is no signal, slot or invokable function giving back nothing, of a
      class built on QObject, and Qt's source has no code for it that could
      be told from the rest.
    """
    raise NotImplementedError(
        "'QFileSystemEngine.setPermissions' has no cute function yet. Qt's "
        "'bool QFileSystemEngine::setPermissions(int fd, QFile::Permissions "
        "permissions, QSystemError &error)': takes a type Python has no way "
        "to hand over yet. Qt's 'bool "
        "QFileSystemEngine::setPermissions(const QFileSystemEntry &entry, "
        "QFile::Permissions permissions, QSystemError &error)': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def supportsMoveFileToTrash(*__, **_) -> Never:
    """
    Qt's 'bool QFileSystemEngine::supportsMoveFileToTrash()': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QFileSystemEngine.supportsMoveFileToTrash' has no cute function "
        "yet. Qt's 'bool QFileSystemEngine::supportsMoveFileToTrash()': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def tempPath(*__, **_) -> Never:
    """
    Qt's 'QString QFileSystemEngine::tempPath()': cannot be called and cannot
    be called through the meta-object and cannot be copied: no header file
    has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QFileSystemEngine.tempPath' has no cute function yet. Qt's "
        "'QString QFileSystemEngine::tempPath()': cannot be called and "
        "cannot be called through the meta-object and cannot be copied: no "
        "header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")
