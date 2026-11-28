"""
QResourceFileEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qresource_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QResourceFileEngine to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from . import QAbstractFileEngine, QDirListing, QIODeviceBase, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QResourceFileEngine(QAbstractFileEngine):
  """
  The cute side of Qt's QResourceFileEngine: a plain Python object standing
  in front of one C++ QResourceFileEngine.

  It is built on the cute 'QAbstractFileEngine', as Qt's QResourceFileEngine
  is built on Qt's QAbstractFileEngine, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QResourceFileEngine that has a ritual and that
  Python can call so far, 13 names in all: 'setFileName', 'close', 'flush',
  'size', 'pos', 'atEnd', 'seek', 'caseSensitive', 'fileFlags', 'fileName',
  'ownerId', 'extension', 'supportsExtension'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QResourceFileEnginePrivate *QResourceFileEngine::d_func()': gives
    'QResourceFileEnginePrivate', which has no cute class yet.
  - Qt's 'const QResourceFileEnginePrivate *QResourceFileEngine::d_func()
    const': gives 'QResourceFileEnginePrivate', which has no cute class yet.
  - Qt's 'QResourceFileEngine::~QResourceFileEngine()': the destructor:
    Python never removes a C++ QResourceFileEngine.
  - Qt's 'bool QResourceFileEngine::open(QIODevice::OpenMode flags,
    std::optional<QFile::Permissions> permissions)': takes a type Python has
    no way to hand over yet.
  - Qt's 'qint64 QResourceFileEngine::read(char *data, qint64 maxlen)': names
    'char', which has no cute class yet.
  - Qt's 'QDateTime QResourceFileEngine::fileTime(QFile::FileTime time)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'IteratorUniquePtr QResourceFileEngine::beginEntryList(const QString
    &path, QDirListing::IteratorFlags filters, const QStringList
    &filterNames)': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  1 of the 21 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QResourceFileEngine is created at the first use, not by
    'QResourceFileEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QResourceFileEngine.
  - Each name of Qt's QResourceFileEngine that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QResourceFileEngine'

  #  A C++ QResourceFileEngine Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QResourceFileEngine'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def size(self) -> int:
    """
    Calls Qt's 'qint64 QResourceFileEngine::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qresourcefileengine.html#size
    """
    #  qint64 QResourceFileEngine::size() const
    ritual = 'ritual_ZNK19QResourceFileEngine4sizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QResourceFileEngine4sizeEv'
    return self.uglySide.call(ritual)

  def pos(self) -> int:
    """
    Calls Qt's 'qint64 QResourceFileEngine::pos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qresourcefileengine.html#pos
    """
    #  qint64 QResourceFileEngine::pos() const
    ritual = 'ritual_ZNK19QResourceFileEngine3posEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QResourceFileEngine3posEv'
    return self.uglySide.call(ritual)

  def atEnd(self) -> bool:
    """
    Calls Qt's 'bool QResourceFileEngine::atEnd() const'.

    Qt's own words: https://doc.qt.io/qt-6/qresourcefileengine.html#atEnd
    """
    #  bool QResourceFileEngine::atEnd() const
    ritual = 'ritual_ZNK19QResourceFileEngine5atEndEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QResourceFileEngine5atEndEv'
    return self.uglySide.call(ritual)

  def caseSensitive(self) -> bool:
    """
    Calls Qt's 'bool QResourceFileEngine::caseSensitive() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qresourcefileengine.html#caseSensitive
    """
    #  bool QResourceFileEngine::caseSensitive() const
    ritual = 'ritual_ZNK19QResourceFileEngine13caseSensitiveEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QResourceFileEngine13caseSensitiveEv'
    return self.uglySide.call(ritual)

  @overload(QAbstractFileEngine.FileFlags)
  def fileFlags(
      self,
      type: QAbstractFileEngine.FileFlags,
  ) -> QAbstractFileEngine.FileFlags:
    """
    Calls Qt's 'FileFlags QResourceFileEngine::fileFlags(FileFlags type)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qresourcefileengine.html#fileFlags

    Parameters
    ----------

    type : QAbstractFileEngine.FileFlags
      Passed on as its number.

    Returns
    -------

    QAbstractFileEngine.FileFlags
      The value standing for the combination Qt gave back.
    """
    #  FileFlags QResourceFileEngine::fileFlags(FileFlags type) const
    ritual = (
        'ritual_ZNK19QResourceFileEngine9fileFlagsE6QFlagsIN19QAbstractFile'
        'Engine8FileFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QResourceFileEngine9fileFlagsE6QFlagsIN19QAbstra'
          'ctFileEngine8FileFlagEE')
    return QAbstractFileEngine.FileFlags(self.uglySide.call(
        ritual, type.value,
    ))

  @overload(QAbstractFileEngine.FileName)
  def fileName(self, file: QAbstractFileEngine.FileName) -> str:
    """
    Calls Qt's 'QString
    QResourceFileEngine::fileName(QAbstractFileEngine::FileName file) const'.

    Qt's own words: https://doc.qt.io/qt-6/qresourcefileengine.html#fileName

    Parameters
    ----------

    file : QAbstractFileEngine.FileName
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QResourceFileEngine::fileName(QAbstractFileEngine::FileName
    #      file) const
    ritual = (
        'ritual_ZNK19QResourceFileEngine8fileNameEN19QAbstractFileEngine8Fi'
        'leNameE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QResourceFileEngine8fileNameEN19QAbstractFileEng'
          'ine8FileNameE')
    return self.uglySide.call(ritual, file.value)

  @overload(QAbstractFileEngine.FileOwner)
  def ownerId(self, a0: QAbstractFileEngine.FileOwner) -> int:
    """
    Calls Qt's 'uint QResourceFileEngine::ownerId(FileOwner a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qresourcefileengine.html#ownerId

    Parameters
    ----------

    a0 : QAbstractFileEngine.FileOwner
      Passed on as its number.
    """
    #  uint QResourceFileEngine::ownerId(FileOwner a0) const
    ritual = (
        'ritual_ZNK19QResourceFileEngine7ownerIdEN19QAbstractFileEngine9Fil'
        'eOwnerE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QResourceFileEngine7ownerIdEN19QAbstractFileEngi'
          'ne9FileOwnerE')
    return self.uglySide.call(ritual, a0.value)

  @overload(QAbstractFileEngine.Extension)
  def supportsExtension(
      self,
      extension: QAbstractFileEngine.Extension,
  ) -> bool:
    """
    Calls Qt's 'bool QResourceFileEngine::supportsExtension(Extension
    extension) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qresourcefileengine.html#supportsExtension

    Parameters
    ----------

    extension : QAbstractFileEngine.Extension
      Passed on as its number.
    """
    #  bool QResourceFileEngine::supportsExtension(Extension extension) const
    ritual = (
        'ritual_ZNK19QResourceFileEngine17supportsExtensionEN19QAbstractFil'
        'eEngine9ExtensionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QResourceFileEngine17supportsExtensionEN19QAbstr'
          'actFileEngine9ExtensionE')
    return self.uglySide.call(ritual, extension.value)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setFileName(self, file: str) -> None:
    """
    Calls Qt's 'void QResourceFileEngine::setFileName(const QString &file)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qresourcefileengine.html#setFileName

    Parameters
    ----------

    file : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QResourceFileEngine::setFileName(const QString &file)
    ritual = 'ritual_ZN19QResourceFileEngine11setFileNameERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QResourceFileEngine11setFileNameERK7QString'
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
    Qt's 'QResourceFileEngine::QResourceFileEngine(const QString &path)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: member access into incomplete type
    'QResourceFileEnginePrivate'.
    """
    raise NotImplementedError(
        "'QResourceFileEngine.__init__' has no cute function yet. Qt's "
        "'QResourceFileEngine::QResourceFileEngine(const QString &path)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: member access into incomplete "
        "type 'QResourceFileEnginePrivate'.")

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

  def close(self) -> bool:
    """
    Calls Qt's 'bool QResourceFileEngine::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qresourcefileengine.html#close
    """
    #  bool QResourceFileEngine::close()
    ritual = 'ritual_ZN19QResourceFileEngine5closeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QResourceFileEngine5closeEv'
    return self.uglySide.call(ritual)

  def flush(self) -> bool:
    """
    Calls Qt's 'bool QResourceFileEngine::flush()'.

    Qt's own words: https://doc.qt.io/qt-6/qresourcefileengine.html#flush
    """
    #  bool QResourceFileEngine::flush()
    ritual = 'ritual_ZN19QResourceFileEngine5flushEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QResourceFileEngine5flushEv'
    return self.uglySide.call(ritual)

  @overload(int)
  def seek(self, a0: int) -> bool:
    """
    Calls Qt's 'bool QResourceFileEngine::seek(qint64 a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qresourcefileengine.html#seek

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  bool QResourceFileEngine::seek(qint64 a0)
    ritual = 'ritual_ZN19QResourceFileEngine4seekEx'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QResourceFileEngine4seekEx'
    return self.uglySide.call(ritual, a0)

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
    Calls Qt's 'bool QResourceFileEngine::extension(Extension extension,
    const ExtensionOption *option, ExtensionReturn *output)'.

    Qt's own words: https://doc.qt.io/qt-6/qresourcefileengine.html#extension

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
    #  bool QResourceFileEngine::extension(Extension extension, const
    #      ExtensionOption *option, ExtensionReturn *output)
    return self.uglySide.call(
        'ritual_ZN19QResourceFileEngine9extensionEN19QAbstractFileEngine9Ex'
        'tensionEPKNS0_15ExtensionOptionEPNS0_15ExtensionReturnE',
        extension.value, self._addressOf(option), self._addressOf(output),
    )
