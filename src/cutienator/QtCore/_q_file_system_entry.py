"""
QFileSystemEntry binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qfilesystementry_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QFileSystemEntry to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QByteArray


class QFileSystemEntry(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QFileSystemEntry: a plain Python object standing in
  front of one C++ QFileSystemEntry.

  C++ hands a QFileSystemEntry around as a copy, so every C++
  QFileSystemEntry behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QFileSystemEntry that has a ritual and that Python
  can call so far, 14 names in all: 'filePath', 'fileName', 'path',
  'nativeFilePath', 'baseName', 'completeBaseName', 'suffix',
  'completeSuffix', 'isRoot', 'isEmpty', 'clear', 'isRootPath',
  'resolveFilePath', 'resolveNativeFilePath'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFileSystemEntry::~QFileSystemEntry()': the destructor: Python
    removes its C++ QFileSystemEntry by it, and has no other use for it.

  What has no ritual
  ------------------

  9 of the 25 functions Qt declares: 6 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 cannot be
  called and cannot be called through the meta-object and cannot be copied; 1
  leans on 'qt_isPathNormalized(QString const&, QFlags<QDirPrivate.

  What to expect
  --------------

  - The C++ QFileSystemEntry is created at the first use, not by
    'QFileSystemEntry(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QFileSystemEntry back gives a copy the ritual made
    for Python, in a new cute QFileSystemEntry.
  - Each name of Qt's QFileSystemEntry that has no cute function yet,
    'findFileNameSeparators', 'findLastSeparator', 'isAbsolute', 'isClean',
    'isRelative', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The classes Qt writes inside QFileSystemEntry, each a class in here as
  #  in C++.

  class FromInternalPath(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QFileSystemEntry::FromInternalPath: a plain Python
    object standing in front of one C++ QFileSystemEntry::FromInternalPath.

    C++ hands a QFileSystemEntry::FromInternalPath around as a copy, so every
    C++ QFileSystemEntry::FromInternalPath behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QFileSystemEntry::FromInternalPath yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QFileSystemEntry::FromInternalPath::~FromInternalPath()': the
      destructor: Python removes its C++ QFileSystemEntry::FromInternalPath
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QFileSystemEntry::FromInternalPath is created at the first use,
      not by 'QFileSystemEntry::FromInternalPath(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QFileSystemEntry::FromInternalPath back gives a
      copy the ritual made for Python, in a new cute
      QFileSystemEntry::FromInternalPath.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QFileSystemEntry::FromInternalPath'

    #  Qt's '~QFileSystemEntry::FromInternalPath()'. Naming it makes this a
    #  value class: Python owns every C++ QFileSystemEntry::FromInternalPath
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN16QFileSystemEntry16FromInternalPathD1Ev'

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

  class FromNativePath(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QFileSystemEntry::FromNativePath: a plain Python
    object standing in front of one C++ QFileSystemEntry::FromNativePath.

    C++ hands a QFileSystemEntry::FromNativePath around as a copy, so every
    C++ QFileSystemEntry::FromNativePath behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QFileSystemEntry::FromNativePath yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QFileSystemEntry::FromNativePath::~FromNativePath()': the
      destructor: Python removes its C++ QFileSystemEntry::FromNativePath by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QFileSystemEntry::FromNativePath is created at the first use,
      not by 'QFileSystemEntry::FromNativePath(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QFileSystemEntry::FromNativePath back gives a copy
      the ritual made for Python, in a new cute
      QFileSystemEntry::FromNativePath.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QFileSystemEntry::FromNativePath'

    #  Qt's '~QFileSystemEntry::FromNativePath()'. Naming it makes this a
    #  value class: Python owns every C++ QFileSystemEntry::FromNativePath
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN16QFileSystemEntry14FromNativePathD1Ev'

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
  @overload(str)
  def isRootPath(path: str) -> bool:
    """
    Calls Qt's 'bool QFileSystemEntry::isRootPath(const QString &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystementry.html#isRootPath

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QFileSystemEntry::isRootPath(const QString &path)
    return Rituals.call(
        'ritual_ZN16QFileSystemEntry10isRootPathERK7QString', path,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFileSystemEntry'

  #  Qt's '~QFileSystemEntry()'. Naming it makes this a value class: Python
  #  owns every C++ QFileSystemEntry behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QFileSystemEntryD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def filePath(self) -> str:
    """
    Calls Qt's 'QString QFileSystemEntry::filePath() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystementry.html#filePath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileSystemEntry::filePath() const
    return self.uglySide.call('ritual_ZNK16QFileSystemEntry8filePathEv')

  def fileName(self) -> str:
    """
    Calls Qt's 'QString QFileSystemEntry::fileName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystementry.html#fileName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileSystemEntry::fileName() const
    return self.uglySide.call('ritual_ZNK16QFileSystemEntry8fileNameEv')

  def path(self) -> str:
    """
    Calls Qt's 'QString QFileSystemEntry::path() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystementry.html#path

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileSystemEntry::path() const
    return self.uglySide.call('ritual_ZNK16QFileSystemEntry4pathEv')

  def nativeFilePath(self) -> QByteArray:
    """
    Calls Qt's 'NativePath QFileSystemEntry::nativeFilePath() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystementry.html#nativeFilePath

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  NativePath QFileSystemEntry::nativeFilePath() const
    address = self.uglySide.call(
        'ritual_ZNK16QFileSystemEntry14nativeFilePathEv',
    )
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  def baseName(self) -> str:
    """
    Calls Qt's 'QString QFileSystemEntry::baseName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystementry.html#baseName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileSystemEntry::baseName() const
    return self.uglySide.call('ritual_ZNK16QFileSystemEntry8baseNameEv')

  def completeBaseName(self) -> str:
    """
    Calls Qt's 'QString QFileSystemEntry::completeBaseName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystementry.html#completeBaseName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileSystemEntry::completeBaseName() const
    return self.uglySide.call(
        'ritual_ZNK16QFileSystemEntry16completeBaseNameEv',
    )

  def suffix(self) -> str:
    """
    Calls Qt's 'QString QFileSystemEntry::suffix() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystementry.html#suffix

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileSystemEntry::suffix() const
    return self.uglySide.call('ritual_ZNK16QFileSystemEntry6suffixEv')

  def completeSuffix(self) -> str:
    """
    Calls Qt's 'QString QFileSystemEntry::completeSuffix() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystementry.html#completeSuffix

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileSystemEntry::completeSuffix() const
    return self.uglySide.call(
        'ritual_ZNK16QFileSystemEntry14completeSuffixEv',
    )

  def isRoot(self) -> bool:
    """
    Calls Qt's 'bool QFileSystemEntry::isRoot() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystementry.html#isRoot
    """
    #  bool QFileSystemEntry::isRoot() const
    return self.uglySide.call('ritual_ZNK16QFileSystemEntry6isRootEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QFileSystemEntry::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystementry.html#isEmpty
    """
    #  bool QFileSystemEntry::isEmpty() const
    return self.uglySide.call('ritual_ZNK16QFileSystemEntry7isEmptyEv')

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
    Notes what was given, for Qt's 'QFileSystemEntry::QFileSystemEntry()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystementry.html#QFileSystemEntry
    """
    #  QFileSystemEntry::QFileSystemEntry()
    self._noteCreation(QFileSystemEntry, lambda: Rituals.call(
        'ritual_ZN16QFileSystemEntryC1Ev',
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

  def clear(self) -> None:
    """
    Calls Qt's 'void QFileSystemEntry::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystementry.html#clear
    """
    #  void QFileSystemEntry::clear()
    self.uglySide.call('ritual_ZN16QFileSystemEntry5clearEv')

  def resolveFilePath(self) -> None:
    """
    Calls Qt's 'void QFileSystemEntry::resolveFilePath() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystementry.html#resolveFilePath
    """
    #  void QFileSystemEntry::resolveFilePath() const
    self.uglySide.call('ritual_ZNK16QFileSystemEntry15resolveFilePathEv')

  def resolveNativeFilePath(self) -> None:
    """
    Calls Qt's 'void QFileSystemEntry::resolveNativeFilePath() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystementry.html#resolveNativeFilePath
    """
    #  void QFileSystemEntry::resolveNativeFilePath() const
    self.uglySide.call(
        'ritual_ZNK16QFileSystemEntry21resolveNativeFilePathEv',
    )

  @staticmethod
  def findFileNameSeparators(*__, **_) -> Never:
    """
    Qt's 'void QFileSystemEntry::findFileNameSeparators() const': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'Uninitialized'.
    """
    raise NotImplementedError(
        "'QFileSystemEntry.findFileNameSeparators' has no cute function "
        "yet. Qt's 'void QFileSystemEntry::findFileNameSeparators() const': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'Uninitialized'.")

  @staticmethod
  def findLastSeparator(*__, **_) -> Never:
    """
    Qt's 'void QFileSystemEntry::findLastSeparator() const': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'Uninitialized'.
    """
    raise NotImplementedError(
        "'QFileSystemEntry.findLastSeparator' has no cute function yet. "
        "Qt's 'void QFileSystemEntry::findLastSeparator() const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'Uninitialized'.")

  @staticmethod
  def isAbsolute(*__, **_) -> Never:
    """
    Qt's 'bool QFileSystemEntry::isAbsolute() const': cannot be called and
    cannot be called through the meta-object and cannot be copied: no header
    file has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QFileSystemEntry.isAbsolute' has no cute function yet. Qt's 'bool "
        "QFileSystemEntry::isAbsolute() const': cannot be called and cannot "
        "be called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")

  @staticmethod
  def isClean(*__, **_) -> Never:
    """
    Qt's 'bool QFileSystemEntry::isClean() const': leans on
    'qt_isPathNormalized(QString const&,
    QFlags<QDirPrivate::PathNormalization>)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QFileSystemEntry.isClean' has no cute function yet. Qt's 'bool "
        "QFileSystemEntry::isClean() const': leans on "
        "'qt_isPathNormalized(QString const&, "
        "QFlags<QDirPrivate::PathNormalization>)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def isRelative(*__, **_) -> Never:
    """
    Qt's 'bool QFileSystemEntry::isRelative() const': cannot be called and
    cannot be called through the meta-object and cannot be copied: no header
    file has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QFileSystemEntry.isRelative' has no cute function yet. Qt's 'bool "
        "QFileSystemEntry::isRelative() const': cannot be called and cannot "
        "be called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")
