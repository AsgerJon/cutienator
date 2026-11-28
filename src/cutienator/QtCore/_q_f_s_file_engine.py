"""
QFSFileEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qfsfileengine_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QFSFileEngine to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QAbstractFileEngine, QDirListing, QFileDevice, QIODeviceBase
from . import QList, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QByteArray, QFSFileEnginePrivate, QFileInfo

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFSFileEngine(QAbstractFileEngine):
  """
  The cute side of Qt's QFSFileEngine: a plain Python object standing in
  front of one C++ QFSFileEngine.

  It is built on the cute 'QAbstractFileEngine', as Qt's QFSFileEngine is
  built on Qt's QAbstractFileEngine, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QFSFileEngine that has a ritual and that Python can
  call so far, 34 names in all: 'd_func', 'close', 'flush', 'syncToDisk',
  'size', 'pos', 'seek', 'isSequential', 'remove', 'copy', 'rename',
  'renameOverwrite', 'link', 'rmdir', 'setSize', 'caseSensitive',
  'isRelativePath', 'fileFlags', 'setPermissions', 'id', 'fileName',
  'ownerId', 'owner', 'setFileName', 'handle', 'write', 'cloneTo',
  'isUnnamedFile', 'extension', 'supportsExtension', 'open',
  'setCurrentPath', 'currentPath', 'drives'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QFSFileEnginePrivate *QFSFileEngine::d_func() const': takes
    in Python what 'QFSFileEnginePrivate *QFSFileEngine::d_func()' takes.
  - Qt's 'QFSFileEngine::~QFSFileEngine()': the destructor: Python never
    removes a C++ QFSFileEngine.
  - Qt's 'bool QFSFileEngine::open(QIODevice::OpenMode openMode,
    std::optional<QFile::Permissions> permissions)': takes a type Python has
    no way to hand over yet.
  - Qt's 'bool QFSFileEngine::mkdir(const QString &dirName, bool
    createParentDirectories, std::optional<QFile::Permissions> permissions)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'bool QFSFileEngine::setFileTime(const QDateTime &newDate,
    QFile::FileTime time)': takes a type Python has no way to hand over yet.
  - Qt's 'QDateTime QFSFileEngine::fileTime(QFile::FileTime time) const':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QFSFileEngine::setFileEntry(QFileSystemEntry &&entry)': takes
    a type Python has no way to hand over yet.
  - Qt's 'IteratorUniquePtr QFSFileEngine::beginEntryList(const QString
    &path, QDirListing::IteratorFlags filters, const QStringList
    &filterNames)': gives a type Python has no way to take yet.
  - Qt's 'qint64 QFSFileEngine::read(char *data, qint64 maxlen)': names
    'char', which has no cute class yet.
  - Qt's 'qint64 QFSFileEngine::readLine(char *data, qint64 maxlen)': names
    'char', which has no cute class yet.
  - Qt's 'bool QFSFileEngine::open(QIODevice::OpenMode flags, FILE *fh,
    QFile::FileHandleFlags handleFlags)': names 'FILE', which has no cute
    class yet.
  - Qt's 'QFSFileEngine::QFSFileEngine(QFSFileEnginePrivate &dd)': takes a
    type Python has no way to hand over yet.
  - Qt's 'bool QFSFileEngine::rename_helper(const QString &newName,
    RenameMode mode)': names the enum 'QFSFileEngine::RenameMode', whose
    class cannot be named here.

  What to expect
  --------------

  - The C++ QFSFileEngine is created at the first use, not by
    'QFSFileEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QFSFileEngine.
  - Each name of Qt's QFSFileEngine that has no cute function yet,
    'rename_helper', 'setFileEntry', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  def setCurrentPath(path: str) -> bool:
    """
    Calls Qt's 'bool QFSFileEngine::setCurrentPath(const QString &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qfsfileengine.html#setCurrentPath

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QFSFileEngine::setCurrentPath(const QString &path)
    return Rituals.call(
        'ritual_ZN13QFSFileEngine14setCurrentPathERK7QString', path,
    )

  @staticmethod
  @overload()
  @overload(str)
  def currentPath(path: str = '') -> str:
    """
    Calls Qt's 'QString QFSFileEngine::currentPath(const QString &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qfsfileengine.html#currentPath

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFSFileEngine::currentPath(const QString &path)
    return Rituals.call(
        'ritual_ZN13QFSFileEngine11currentPathERK7QString', path,
    )

  @staticmethod
  def drives() -> QList[QFileInfo]:
    """
    Calls Qt's 'QFileInfoList QFSFileEngine::drives()'.

    Qt's own words: https://doc.qt.io/qt-6/qfsfileengine.html#drives

    Returns
    -------

    QList[QFileInfo]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QFileInfoList QFSFileEngine::drives()
    address = Rituals.call('ritual_ZN13QFSFileEngine6drivesEv')
    from . import QFileInfo
    return QList[QFileInfo]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFSFileEngine'

  #  A C++ QFSFileEngine Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QFSFileEngine'

  #  The functions Qt calls itself that QFSFileEngine is the first to declare
  #  and that cannot be handed to Python yet, each as Qt declares it. A class
  #  of a program that writes one of them anew is refused, since Qt would
  #  never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'setFileEntry': (
          'void QFSFileEngine::setFileEntry(QFileSystemEntry &&)',
      ),
  }

  #  The functions Qt calls itself that QFSFileEngine is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'isUnnamedFile': (
          ('_ZNK13QFSFileEngine13isUnnamedFileEv',
           ('bool', 'number', ''),
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

  def size(self) -> int:
    """
    Calls Qt's 'qint64 QFSFileEngine::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfsfileengine.html#size
    """
    #  qint64 QFSFileEngine::size() const
    ritual = 'ritual_ZNK13QFSFileEngine4sizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QFSFileEngine4sizeEv'
    return self.uglySide.call(ritual)

  def pos(self) -> int:
    """
    Calls Qt's 'qint64 QFSFileEngine::pos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfsfileengine.html#pos
    """
    #  qint64 QFSFileEngine::pos() const
    ritual = 'ritual_ZNK13QFSFileEngine3posEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QFSFileEngine3posEv'
    return self.uglySide.call(ritual)

  def isSequential(self) -> bool:
    """
    Calls Qt's 'bool QFSFileEngine::isSequential() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfsfileengine.html#isSequential
    """
    #  bool QFSFileEngine::isSequential() const
    ritual = 'ritual_ZNK13QFSFileEngine12isSequentialEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QFSFileEngine12isSequentialEv'
    return self.uglySide.call(ritual)

  @overload(str, bool)
  def rmdir(self, dirName: str, recurseParentDirectories: bool) -> bool:
    """
    Calls Qt's 'bool QFSFileEngine::rmdir(const QString &dirName, bool
    recurseParentDirectories) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfsfileengine.html#rmdir

    Parameters
    ----------

    dirName : str
      Passed on as it is: a QString is made of it for the call.

    recurseParentDirectories : bool
      Passed on as it is.
    """
    #  bool QFSFileEngine::rmdir(const QString &dirName, bool
    #      recurseParentDirectories) const
    ritual = 'ritual_ZNK13QFSFileEngine5rmdirERK7QStringb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QFSFileEngine5rmdirERK7QStringb'
    return self.uglySide.call(ritual, dirName, recurseParentDirectories)

  def caseSensitive(self) -> bool:
    """
    Calls Qt's 'bool QFSFileEngine::caseSensitive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfsfileengine.html#caseSensitive
    """
    #  bool QFSFileEngine::caseSensitive() const
    ritual = 'ritual_ZNK13QFSFileEngine13caseSensitiveEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QFSFileEngine13caseSensitiveEv'
    return self.uglySide.call(ritual)

  def isRelativePath(self) -> bool:
    """
    Calls Qt's 'bool QFSFileEngine::isRelativePath() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfsfileengine.html#isRelativePath
    """
    #  bool QFSFileEngine::isRelativePath() const
    ritual = 'ritual_ZNK13QFSFileEngine14isRelativePathEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QFSFileEngine14isRelativePathEv'
    return self.uglySide.call(ritual)

  @overload(QAbstractFileEngine.FileFlags)
  def fileFlags(
      self,
      type: QAbstractFileEngine.FileFlags,
  ) -> QAbstractFileEngine.FileFlags:
    """
    Calls Qt's 'FileFlags QFSFileEngine::fileFlags(FileFlags type) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfsfileengine.html#fileFlags

    Parameters
    ----------

    type : QAbstractFileEngine.FileFlags
      Passed on as its number.

    Returns
    -------

    QAbstractFileEngine.FileFlags
      The value standing for the combination Qt gave back.
    """
    #  FileFlags QFSFileEngine::fileFlags(FileFlags type) const
    ritual = (
        'ritual_ZNK13QFSFileEngine9fileFlagsE6QFlagsIN19QAbstractFileEngine'
        '8FileFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK13QFSFileEngine9fileFlagsE6QFlagsIN19QAbstractFile'
          'Engine8FileFlagEE')
    return QAbstractFileEngine.FileFlags(self.uglySide.call(
        ritual, type.value,
    ))

  def id(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QFSFileEngine::id() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfsfileengine.html#id

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QFSFileEngine::id() const
    ritual = 'ritual_ZNK13QFSFileEngine2idEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QFSFileEngine2idEv'
    address = self.uglySide.call(ritual)
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(QAbstractFileEngine.FileName)
  def fileName(self, file: QAbstractFileEngine.FileName) -> str:
    """
    Calls Qt's 'QString QFSFileEngine::fileName(FileName file) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfsfileengine.html#fileName

    Parameters
    ----------

    file : QAbstractFileEngine.FileName
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFSFileEngine::fileName(FileName file) const
    ritual = (
        'ritual_ZNK13QFSFileEngine8fileNameEN19QAbstractFileEngine8FileName'
        'E')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK13QFSFileEngine8fileNameEN19QAbstractFileEngine8Fi'
          'leNameE')
    return self.uglySide.call(ritual, file.value)

  @overload(QAbstractFileEngine.FileOwner)
  def ownerId(self, a0: QAbstractFileEngine.FileOwner) -> int:
    """
    Calls Qt's 'uint QFSFileEngine::ownerId(FileOwner a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfsfileengine.html#ownerId

    Parameters
    ----------

    a0 : QAbstractFileEngine.FileOwner
      Passed on as its number.
    """
    #  uint QFSFileEngine::ownerId(FileOwner a0) const
    ritual = (
        'ritual_ZNK13QFSFileEngine7ownerIdEN19QAbstractFileEngine9FileOwner'
        'E')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK13QFSFileEngine7ownerIdEN19QAbstractFileEngine9Fil'
          'eOwnerE')
    return self.uglySide.call(ritual, a0.value)

  @overload(QAbstractFileEngine.FileOwner)
  def owner(self, a0: QAbstractFileEngine.FileOwner) -> str:
    """
    Calls Qt's 'QString QFSFileEngine::owner(FileOwner a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfsfileengine.html#owner

    Parameters
    ----------

    a0 : QAbstractFileEngine.FileOwner
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFSFileEngine::owner(FileOwner a0) const
    ritual = (
        'ritual_ZNK13QFSFileEngine5ownerEN19QAbstractFileEngine9FileOwnerE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK13QFSFileEngine5ownerEN19QAbstractFileEngine9FileO'
          'wnerE')
    return self.uglySide.call(ritual, a0.value)

  def handle(self) -> int:
    """
    Calls Qt's 'int QFSFileEngine::handle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfsfileengine.html#handle
    """
    #  int QFSFileEngine::handle() const
    ritual = 'ritual_ZNK13QFSFileEngine6handleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QFSFileEngine6handleEv'
    return self.uglySide.call(ritual)

  def isUnnamedFile(self) -> bool:
    """
    Calls Qt's 'bool QFSFileEngine::isUnnamedFile() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfsfileengine.html#isUnnamedFile
    """
    #  bool QFSFileEngine::isUnnamedFile() const
    ritual = 'ritual_ZNK13QFSFileEngine13isUnnamedFileEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QFSFileEngine13isUnnamedFileEv'
    return self.uglySide.call(ritual)

  @overload(QAbstractFileEngine.Extension)
  def supportsExtension(
      self,
      extension: QAbstractFileEngine.Extension,
  ) -> bool:
    """
    Calls Qt's 'bool QFSFileEngine::supportsExtension(Extension extension)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfsfileengine.html#supportsExtension

    Parameters
    ----------

    extension : QAbstractFileEngine.Extension
      Passed on as its number.
    """
    #  bool QFSFileEngine::supportsExtension(Extension extension) const
    ritual = (
        'ritual_ZNK13QFSFileEngine17supportsExtensionEN19QAbstractFileEngin'
        'e9ExtensionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK13QFSFileEngine17supportsExtensionEN19QAbstractFil'
          'eEngine9ExtensionE')
    return self.uglySide.call(ritual, extension.value)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setSize(self, size: int) -> bool:
    """
    Calls Qt's 'bool QFSFileEngine::setSize(qint64 size)'.

    Qt's own words: https://doc.qt.io/qt-6/qfsfileengine.html#setSize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  bool QFSFileEngine::setSize(qint64 size)
    ritual = 'ritual_ZN13QFSFileEngine7setSizeEx'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QFSFileEngine7setSizeEx'
    return self.uglySide.call(ritual, size)

  @overload(int)
  def setPermissions(self, perms: int) -> bool:
    """
    Calls Qt's 'bool QFSFileEngine::setPermissions(uint perms)'.

    Qt's own words: https://doc.qt.io/qt-6/qfsfileengine.html#setPermissions

    Parameters
    ----------

    perms : int
      Passed on as it is.
    """
    #  bool QFSFileEngine::setPermissions(uint perms)
    ritual = 'ritual_ZN13QFSFileEngine14setPermissionsEj'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QFSFileEngine14setPermissionsEj'
    return self.uglySide.call(ritual, perms)

  @overload(str)
  def setFileName(self, file: str) -> None:
    """
    Calls Qt's 'void QFSFileEngine::setFileName(const QString &file)'.

    Qt's own words: https://doc.qt.io/qt-6/qfsfileengine.html#setFileName

    Parameters
    ----------

    file : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QFSFileEngine::setFileName(const QString &file)
    ritual = 'ritual_ZN13QFSFileEngine11setFileNameERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QFSFileEngine11setFileNameERK7QString'
    self.uglySide.call(ritual, file)

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
    Notes what was given, for Qt's 'QFSFileEngine::QFSFileEngine()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfsfileengine.html#QFSFileEngine
    """
    #  QFSFileEngine::QFSFileEngine()
    self._noteCreation(QFSFileEngine, lambda: Rituals.call(
        'ritual_ZN13QFSFileEngineC1Ev',
    ))

  @overload(str)
  def __init__(self, file: str) -> None:
    """
    Notes what was given, for Qt's 'QFSFileEngine::QFSFileEngine(const
    QString &file)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfsfileengine.html#QFSFileEngine

    Parameters
    ----------

    file : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QFSFileEngine::QFSFileEngine(const QString &file)
    self._noteCreation(QFSFileEngine, lambda: Rituals.call(
        'ritual_ZN13QFSFileEngineC1ERK7QString', file,
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

  def d_func(self) -> Optional[QFSFileEnginePrivate]:
    """
    Calls Qt's 'QFSFileEnginePrivate *QFSFileEngine::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qfsfileengine.html#d_func

    Returns
    -------

    Optional[QFSFileEnginePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFSFileEnginePrivate *QFSFileEngine::d_func()
    address = self.uglySide.call('ritual_ZN13QFSFileEngine6d_funcEv')
    from . import QFSFileEnginePrivate
    return QFSFileEnginePrivate._cuteAt(address)

  def close(self) -> bool:
    """
    Calls Qt's 'bool QFSFileEngine::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qfsfileengine.html#close
    """
    #  bool QFSFileEngine::close()
    ritual = 'ritual_ZN13QFSFileEngine5closeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QFSFileEngine5closeEv'
    return self.uglySide.call(ritual)

  def flush(self) -> bool:
    """
    Calls Qt's 'bool QFSFileEngine::flush()'.

    Qt's own words: https://doc.qt.io/qt-6/qfsfileengine.html#flush
    """
    #  bool QFSFileEngine::flush()
    ritual = 'ritual_ZN13QFSFileEngine5flushEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QFSFileEngine5flushEv'
    return self.uglySide.call(ritual)

  def syncToDisk(self) -> bool:
    """
    Calls Qt's 'bool QFSFileEngine::syncToDisk()'.

    Qt's own words: https://doc.qt.io/qt-6/qfsfileengine.html#syncToDisk
    """
    #  bool QFSFileEngine::syncToDisk()
    ritual = 'ritual_ZN13QFSFileEngine10syncToDiskEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QFSFileEngine10syncToDiskEv'
    return self.uglySide.call(ritual)

  @overload(int)
  def seek(self, a0: int) -> bool:
    """
    Calls Qt's 'bool QFSFileEngine::seek(qint64 a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qfsfileengine.html#seek

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  bool QFSFileEngine::seek(qint64 a0)
    ritual = 'ritual_ZN13QFSFileEngine4seekEx'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QFSFileEngine4seekEx'
    return self.uglySide.call(ritual, a0)

  def remove(self) -> bool:
    """
    Calls Qt's 'bool QFSFileEngine::remove()'.

    Qt's own words: https://doc.qt.io/qt-6/qfsfileengine.html#remove
    """
    #  bool QFSFileEngine::remove()
    ritual = 'ritual_ZN13QFSFileEngine6removeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QFSFileEngine6removeEv'
    return self.uglySide.call(ritual)

  @overload(str)
  def copy(self, newName: str) -> bool:
    """
    Calls Qt's 'bool QFSFileEngine::copy(const QString &newName)'.

    Qt's own words: https://doc.qt.io/qt-6/qfsfileengine.html#copy

    Parameters
    ----------

    newName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QFSFileEngine::copy(const QString &newName)
    ritual = 'ritual_ZN13QFSFileEngine4copyERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QFSFileEngine4copyERK7QString'
    return self.uglySide.call(ritual, newName)

  @overload(str)
  def rename(self, newName: str) -> bool:
    """
    Calls Qt's 'bool QFSFileEngine::rename(const QString &newName)'.

    Qt's own words: https://doc.qt.io/qt-6/qfsfileengine.html#rename

    Parameters
    ----------

    newName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QFSFileEngine::rename(const QString &newName)
    ritual = 'ritual_ZN13QFSFileEngine6renameERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QFSFileEngine6renameERK7QString'
    return self.uglySide.call(ritual, newName)

  @overload(str)
  def renameOverwrite(self, newName: str) -> bool:
    """
    Calls Qt's 'bool QFSFileEngine::renameOverwrite(const QString &newName)'.

    Qt's own words: https://doc.qt.io/qt-6/qfsfileengine.html#renameOverwrite

    Parameters
    ----------

    newName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QFSFileEngine::renameOverwrite(const QString &newName)
    ritual = 'ritual_ZN13QFSFileEngine15renameOverwriteERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QFSFileEngine15renameOverwriteERK7QString'
    return self.uglySide.call(ritual, newName)

  @overload(str)
  def link(self, newName: str) -> bool:
    """
    Calls Qt's 'bool QFSFileEngine::link(const QString &newName)'.

    Qt's own words: https://doc.qt.io/qt-6/qfsfileengine.html#link

    Parameters
    ----------

    newName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QFSFileEngine::link(const QString &newName)
    ritual = 'ritual_ZN13QFSFileEngine4linkERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QFSFileEngine4linkERK7QString'
    return self.uglySide.call(ritual, newName)

  @overload(str, int)
  @overload(NoneType, int)
  def write(self, data: Optional[str], len: int) -> int:
    """
    Calls Qt's 'qint64 QFSFileEngine::write(const char *data, qint64 len)'.

    Qt's own words: https://doc.qt.io/qt-6/qfsfileengine.html#write

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    len : int
      Passed on as it is.
    """
    #  qint64 QFSFileEngine::write(const char *data, qint64 len)
    return self.uglySide.call(
        'ritual_ZN13QFSFileEngine5writeEPKcx', self._bytesOf(data), len,
    )

  @overload(QAbstractFileEngine)
  @overload(NoneType)
  def cloneTo(
      self,
      target: Optional[QAbstractFileEngine],
  ) -> QAbstractFileEngine.TriStateResult:
    """
    Calls Qt's 'TriStateResult QFSFileEngine::cloneTo(QAbstractFileEngine
    *target)'.

    Qt's own words: https://doc.qt.io/qt-6/qfsfileengine.html#cloneTo

    Parameters
    ----------

    target : Optional[QAbstractFileEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QAbstractFileEngine.TriStateResult
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstractFileEngine.TriStateResult(number)' gives.
    """
    #  TriStateResult QFSFileEngine::cloneTo(QAbstractFileEngine *target)
    ritual = 'ritual_ZN13QFSFileEngine7cloneToEP19QAbstractFileEngine'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QFSFileEngine7cloneToEP19QAbstractFileEngine'
    return QAbstractFileEngine.TriStateResult(self.uglySide.call(
        ritual, self._addressOf(target),
    ))

  @overload(QAbstractFileEngine.Extension)
  @overload(
      QAbstractFileEngine.Extension, QAbstractFileEngine.ExtensionOption,
  )
  @overload(QAbstractFileEngine.Extension, NoneType)
  @overload(
      QAbstractFileEngine.Extension, QAbstractFileEngine.ExtensionOption,
      QAbstractFileEngine.ExtensionReturn,
  )
  @overload(
      QAbstractFileEngine.Extension, QAbstractFileEngine.ExtensionOption,
      NoneType,
  )
  @overload(
      QAbstractFileEngine.Extension, NoneType,
      QAbstractFileEngine.ExtensionReturn,
  )
  @overload(QAbstractFileEngine.Extension, NoneType, NoneType)
  def extension(
      self,
      extension: QAbstractFileEngine.Extension,
      option: Optional[QAbstractFileEngine.ExtensionOption] = None,
      output: Optional[QAbstractFileEngine.ExtensionReturn] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QFSFileEngine::extension(Extension extension, const
    ExtensionOption *option, ExtensionReturn *output)'.

    Qt's own words: https://doc.qt.io/qt-6/qfsfileengine.html#extension

    Parameters
    ----------

    extension : QAbstractFileEngine.Extension
      Passed on as its number.

    option : Optional[QAbstractFileEngine.ExtensionOption]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    output : Optional[QAbstractFileEngine.ExtensionReturn]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  bool QFSFileEngine::extension(Extension extension, const
    #      ExtensionOption *option, ExtensionReturn *output)
    ritual = (
        'ritual_ZN13QFSFileEngine9extensionEN19QAbstractFileEngine9Extensio'
        'nEPKNS0_15ExtensionOptionEPNS0_15ExtensionReturnE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13QFSFileEngine9extensionEN19QAbstractFileEngine9Ex'
          'tensionEPKNS0_15ExtensionOptionEPNS0_15ExtensionReturnE')
    return self.uglySide.call(
        ritual,
        extension.value, self._addressOf(option), self._addressOf(output),
    )

  @overload(QIODeviceBase.OpenMode, int, QFileDevice.FileHandleFlags)
  def open(
      self,
      flags: QIODeviceBase.OpenMode,
      fd: int,
      handleFlags: QFileDevice.FileHandleFlags,
  ) -> bool:
    """
    Calls Qt's 'bool QFSFileEngine::open(QIODevice::OpenMode flags, int fd,
    QFile::FileHandleFlags handleFlags)'.

    Qt's own words: https://doc.qt.io/qt-6/qfsfileengine.html#open

    Parameters
    ----------

    flags : QIODeviceBase.OpenMode
      Passed on as its number.

    fd : int
      Passed on as it is.

    handleFlags : QFileDevice.FileHandleFlags
      Passed on as its number.
    """
    #  bool QFSFileEngine::open(QIODevice::OpenMode flags, int fd,
    #      QFile::FileHandleFlags handleFlags)
    return self.uglySide.call(
        'ritual_ZN13QFSFileEngine4openE6QFlagsIN13QIODeviceBase12OpenModeFl'
        'agEEiS0_IN11QFileDevice14FileHandleFlagEE',
        flags.value, fd, handleFlags.value,
    )

  @staticmethod
  def rename_helper(*__, **_) -> Never:
    """
    Qt's 'bool QFSFileEngine::rename_helper(const QString &newName,
    RenameMode mode)': names the enum 'QFSFileEngine::RenameMode', whose
    class cannot be named here.
    """
    raise NotImplementedError(
        "'QFSFileEngine.rename_helper' has no cute function yet. Qt's 'bool "
        "QFSFileEngine::rename_helper(const QString &newName, RenameMode "
        "mode)': names the enum 'QFSFileEngine::RenameMode', whose class "
        "cannot be named here.")

  @staticmethod
  def setFileEntry(*__, **_) -> Never:
    """
    Qt's 'void QFSFileEngine::setFileEntry(QFileSystemEntry &&entry)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QFSFileEngine.setFileEntry' has no cute function yet. Qt's 'void "
        "QFSFileEngine::setFileEntry(QFileSystemEntry &&entry)': takes a "
        "type Python has no way to hand over yet.")
