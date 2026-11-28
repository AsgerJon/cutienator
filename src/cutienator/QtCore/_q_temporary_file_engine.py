"""
QTemporaryFileEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qtemporaryfile_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QTemporaryFileEngine to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum
from . import QAbstractFileEngine, QFSFileEngine, QIODeviceBase

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QFSFileEnginePrivate


class QTemporaryFileEngine(QFSFileEngine):
  """
  The cute side of Qt's QTemporaryFileEngine: a plain Python object standing
  in front of one C++ QTemporaryFileEngine.

  It is built on the cute 'QFSFileEngine', as Qt's QTemporaryFileEngine is
  built on Qt's QFSFileEngine, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTemporaryFileEngine that has a ritual and that
  Python can call so far, 9 names in all: 'd_func', 'isReallyOpen',
  'setFileName', 'remove', 'rename', 'renameOverwrite', 'close', 'fileName',
  'isUnnamedFile'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QFSFileEnginePrivate *QTemporaryFileEngine::d_func() const':
    takes in Python what 'QFSFileEnginePrivate
    *QTemporaryFileEngine::d_func()' takes.
  - Qt's 'QTemporaryFileEngine::~QTemporaryFileEngine()': the destructor:
    Python never removes a C++ QTemporaryFileEngine.
  - Qt's 'bool QTemporaryFileEngine::open(QIODevice::OpenMode flags,
    std::optional<QFile::Permissions> permissions)': takes a type Python has
    no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 15 functions Qt declares: 2 leans on 'QFileSystemEntry; 1 leans on
  'QFSFileEnginePrivate.

  What to expect
  --------------

  - The C++ QTemporaryFileEngine is created at the first use, not by
    'QTemporaryFileEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTemporaryFileEngine.
  - Each name of Qt's QTemporaryFileEngine that has no cute function yet,
    '__init__', 'initialize', 'materializeUnnamedFile', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QTemporaryFileEngine, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Flags(CuteNum):
    """
    The enum 'QTemporaryFileEngine::Flags' of Qt, with the 1 names Qt gives
    in it.
    """

    Win32NonShared = Kee[int](1)

  class MaterializationMode(CuteNum):
    """
    The enum 'QTemporaryFileEngine::MaterializationMode' of Qt, with the 3
    names Qt gives in it.
    """

    Overwrite = Kee[int](0)
    DontOverwrite = Kee[int](1)
    NameIsTemplate = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTemporaryFileEngine'

  #  A C++ QTemporaryFileEngine Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTemporaryFileEngine'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isReallyOpen(self) -> bool:
    """
    Calls Qt's 'bool QTemporaryFileEngine::isReallyOpen() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtemporaryfileengine.html#isReallyOpen
    """
    #  bool QTemporaryFileEngine::isReallyOpen() const
    return self.uglySide.call(
        'ritual_ZNK20QTemporaryFileEngine12isReallyOpenEv',
    )

  @overload(QAbstractFileEngine.FileName)
  def fileName(self, file: QAbstractFileEngine.FileName) -> str:
    """
    Calls Qt's 'QString QTemporaryFileEngine::fileName(FileName file) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtemporaryfileengine.html#fileName

    Parameters
    ----------

    file : QAbstractFileEngine.FileName
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTemporaryFileEngine::fileName(FileName file) const
    return self.uglySide.call(
        'ritual_ZNK20QTemporaryFileEngine8fileNameEN19QAbstractFileEngine8F'
        'ileNameE',
        file.value,
    )

  def isUnnamedFile(self) -> bool:
    """
    Calls Qt's 'bool QTemporaryFileEngine::isUnnamedFile() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtemporaryfileengine.html#isUnnamedFile
    """
    #  bool QTemporaryFileEngine::isUnnamedFile() const
    return self.uglySide.call(
        'ritual_ZNK20QTemporaryFileEngine13isUnnamedFileEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setFileName(self, file: str) -> None:
    """
    Calls Qt's 'void QTemporaryFileEngine::setFileName(const QString &file)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtemporaryfileengine.html#setFileName

    Parameters
    ----------

    file : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTemporaryFileEngine::setFileName(const QString &file)
    ritual = 'ritual_ZN20QTemporaryFileEngine11setFileNameERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QTemporaryFileEngine11setFileNameERK7QString'
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QTemporaryFileEngine::QTemporaryFileEngine(const QString
    *_templateName, int _flags)': leans on
    'QFSFileEnginePrivate::unmap(unsigned char*)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QTemporaryFileEngine.__init__' has no cute function yet. Qt's "
        "'QTemporaryFileEngine::QTemporaryFileEngine(const QString "
        "*_templateName, int _flags)': leans on "
        "'QFSFileEnginePrivate::unmap(unsigned char*)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

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
    Calls Qt's 'QFSFileEnginePrivate *QTemporaryFileEngine::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qtemporaryfileengine.html#d_func

    Returns
    -------

    Optional[QFSFileEnginePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFSFileEnginePrivate *QTemporaryFileEngine::d_func()
    address = self.uglySide.call('ritual_ZN20QTemporaryFileEngine6d_funcEv')
    from . import QFSFileEnginePrivate
    return QFSFileEnginePrivate._cuteAt(address)

  def remove(self) -> bool:
    """
    Calls Qt's 'bool QTemporaryFileEngine::remove()'.

    Qt's own words: https://doc.qt.io/qt-6/qtemporaryfileengine.html#remove
    """
    #  bool QTemporaryFileEngine::remove()
    return self.uglySide.call('ritual_ZN20QTemporaryFileEngine6removeEv')

  @overload(str)
  def rename(self, newName: str) -> bool:
    """
    Calls Qt's 'bool QTemporaryFileEngine::rename(const QString &newName)'.

    Qt's own words: https://doc.qt.io/qt-6/qtemporaryfileengine.html#rename

    Parameters
    ----------

    newName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QTemporaryFileEngine::rename(const QString &newName)
    return self.uglySide.call(
        'ritual_ZN20QTemporaryFileEngine6renameERK7QString', newName,
    )

  @overload(str)
  def renameOverwrite(self, newName: str) -> bool:
    """
    Calls Qt's 'bool QTemporaryFileEngine::renameOverwrite(const QString
    &newName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtemporaryfileengine.html#renameOverwrite

    Parameters
    ----------

    newName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QTemporaryFileEngine::renameOverwrite(const QString &newName)
    return self.uglySide.call(
        'ritual_ZN20QTemporaryFileEngine15renameOverwriteERK7QString',
        newName,
    )

  def close(self) -> bool:
    """
    Calls Qt's 'bool QTemporaryFileEngine::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qtemporaryfileengine.html#close
    """
    #  bool QTemporaryFileEngine::close()
    ritual = 'ritual_ZN20QTemporaryFileEngine5closeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QTemporaryFileEngine5closeEv'
    return self.uglySide.call(ritual)

  @staticmethod
  def initialize(*__, **_) -> Never:
    """
    Qt's 'void QTemporaryFileEngine::initialize(const QString &file, quint32
    mode, bool nameIsTemplate)': leans on
    'QFileSystemEntry::QFileSystemEntry(QString const&)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QTemporaryFileEngine.initialize' has no cute function yet. Qt's "
        "'void QTemporaryFileEngine::initialize(const QString &file, "
        "quint32 mode, bool nameIsTemplate)': leans on "
        "'QFileSystemEntry::QFileSystemEntry(QString const&)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def materializeUnnamedFile(*__, **_) -> Never:
    """
    Qt's 'bool QTemporaryFileEngine::materializeUnnamedFile(const QString
    &newName, MaterializationMode mode)': leans on
    'QFileSystemEntry::QFileSystemEntry(QByteArray const&,
    QFileSystemEntry::FromNativePath)', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QTemporaryFileEngine.materializeUnnamedFile' has no cute function "
        "yet. Qt's 'bool QTemporaryFileEngine::materializeUnnamedFile(const "
        "QString &newName, MaterializationMode mode)': leans on "
        "'QFileSystemEntry::QFileSystemEntry(QByteArray const&, "
        "QFileSystemEntry::FromNativePath)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")
