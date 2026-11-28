"""
QAbstractFileEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qabstractfileengine_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QAbstractFileEngine to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute
from ..occult import Rituals
from . import QDirListing, QFileDevice, QIODeviceBase, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QAbstractFileEnginePrivate, QByteArray

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractFileEngine(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QAbstractFileEngine: a plain Python object standing
  in front of one C++ QAbstractFileEngine.

  What exists
  -----------

  Every function of Qt's QAbstractFileEngine that has a ritual and that
  Python can call so far, 31 names in all: 'close', 'flush', 'syncToDisk',
  'size', 'pos', 'seek', 'isSequential', 'remove', 'copy', 'rename',
  'renameOverwrite', 'link', 'rmdir', 'setSize', 'caseSensitive',
  'isRelativePath', 'fileFlags', 'setPermissions', 'id', 'fileName',
  'ownerId', 'owner', 'setFileName', 'handle', 'cloneTo', 'atEnd', 'write',
  'errorString', 'extension', 'supportsExtension', 'd_func'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAbstractFileEngine::~QAbstractFileEngine()': the destructor:
    Python never removes a C++ QAbstractFileEngine.
  - Qt's 'bool QAbstractFileEngine::open(QIODevice::OpenMode openMode,
    std::optional<QFile::Permissions> permissions)': takes a type Python has
    no way to hand over yet.
  - Qt's 'bool QAbstractFileEngine::mkdir(const QString &dirName, bool
    createParentDirectories, std::optional<QFile::Permissions> permissions)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'bool QAbstractFileEngine::setFileTime(const QDateTime &newDate,
    QFile::FileTime time)': takes a type Python has no way to hand over yet.
  - Qt's 'QDateTime QAbstractFileEngine::fileTime(QFile::FileTime time)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'bool QAbstractFileEngine::unmap(uchar *ptr)': takes a number to
    change where it is.
  - Qt's 'IteratorUniquePtr QAbstractFileEngine::endEntryList()': gives a
    type Python has no way to take yet.
  - Qt's 'IteratorUniquePtr QAbstractFileEngine::beginEntryList(const QString
    &path, QDirListing::IteratorFlags filters, const QStringList
    &filterNames)': gives a type Python has no way to take yet.
  - Qt's 'qint64 QAbstractFileEngine::read(char *data, qint64 maxlen)': names
    'char', which has no cute class yet.
  - Qt's 'qint64 QAbstractFileEngine::readLine(char *data, qint64 maxlen)':
    names 'char', which has no cute class yet.
  - Qt's 'QFile::FileError QAbstractFileEngine::error() const': gives a type
    Python has no way to take yet.
  - Qt's 'std::unique_ptr<QAbstractFileEngine>
    QAbstractFileEngine::create(const QString &fileName)': gives a type
    Python has no way to take yet.
  - Qt's 'void QAbstractFileEngine::setError(QFile::FileError error, const
    QString &str)': takes a type Python has no way to hand over yet.
  - Qt's 'QAbstractFileEngine::QAbstractFileEngine(QAbstractFileEnginePrivate
    &a0)': takes a type Python has no way to hand over yet.
  - Qt's 'const QAbstractFileEnginePrivate *QAbstractFileEngine::d_func()
    const': takes in Python what 'QAbstractFileEnginePrivate
    *QAbstractFileEngine::d_func()' takes.

  What has no ritual
  ------------------

  5 of the 52 functions Qt declares: 4 forbidden; 1 takes or gives a type
  that cannot be passed yet.

  What to expect
  --------------

  - The C++ QAbstractFileEngine is created at the first use, not by
    'QAbstractFileEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractFileEngine.
  - Each name of Qt's QAbstractFileEngine that has no cute function yet,
    'beginEntryList', 'create', 'endEntryList', 'error', 'fileTime', 'map',
    'mkdir', 'open', 'read', 'readLine', 'setError', 'setFileTime', 'unmap',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QAbstractFileEngine, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Extension(CuteNum):
    """
    The enum 'QAbstractFileEngine::Extension' of Qt, with the 4 names Qt
    gives in it.
    """

    AtEndExtension = Kee[int](0)
    FastReadLineExtension = Kee[int](1)
    MapExtension = Kee[int](2)
    UnMapExtension = Kee[int](3)

  class FileFlag(CuteFlags):
    """
    The flags enum 'QAbstractFileEngine::FileFlag' of Qt, with the 25 names
    Qt gives in it. Qt names the type of its combinations
    'QAbstractFileEngine::FileFlags'.
    """

    ReadOwnerPerm = 0x4000
    WriteOwnerPerm = 0x2000
    ExeOwnerPerm = 0x1000
    ReadUserPerm = 0x400
    WriteUserPerm = 0x200
    ExeUserPerm = 0x100
    ReadGroupPerm = 0x40
    WriteGroupPerm = 0x20
    ExeGroupPerm = 0x10
    ReadOtherPerm = 0x4
    WriteOtherPerm = 0x2
    ExeOtherPerm = 0x1
    LinkType = 0x10000
    FileType = 0x20000
    DirectoryType = 0x40000
    BundleType = 0x80000
    HiddenFlag = 0x100000
    LocalDiskFlag = 0x200000
    ExistsFlag = 0x400000
    RootFlag = 0x800000
    Refresh = 0x1000000
    PermsMask = 0xffff
    TypesMask = 0xf0000
    FlagsMask = 0xff00000
    FileInfoAll = 0xfffffff

  FileFlags = FileFlag

  class FileName(CuteNum):
    """
    The enum 'QAbstractFileEngine::FileName' of Qt, with the 12 names Qt
    gives in it.
    """

    DefaultName = Kee[int](0)
    BaseName = Kee[int](1)
    PathName = Kee[int](2)
    AbsoluteName = Kee[int](3)
    AbsolutePathName = Kee[int](4)
    AbsoluteLinkTarget = Kee[int](5)
    CanonicalName = Kee[int](6)
    CanonicalPathName = Kee[int](7)
    BundleName = Kee[int](8)
    JunctionName = Kee[int](9)
    RawLinkPath = Kee[int](10)
    NFileNames = Kee[int](11)

  class FileOwner(CuteNum):
    """
    The enum 'QAbstractFileEngine::FileOwner' of Qt, with the 2 names Qt
    gives in it.
    """

    OwnerUser = Kee[int](0)
    OwnerGroup = Kee[int](1)

  class TriStateResult(CuteNum, scoped=True):
    """
    The enum 'QAbstractFileEngine::TriStateResult' of Qt, with the 3 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    NotSupported = Kee[int](-1)
    Failed = Kee[int](0)
    Success = Kee[int](1)

  #  The classes Qt writes inside QAbstractFileEngine, each a class in here
  #  as in C++.

  class ExtensionOption(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QAbstractFileEngine::ExtensionOption: a plain
    Python object standing in front of one C++
    QAbstractFileEngine::ExtensionOption.

    C++ hands a QAbstractFileEngine::ExtensionOption around as a copy, so
    every C++ QAbstractFileEngine::ExtensionOption behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QAbstractFileEngine::ExtensionOption yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QAbstractFileEngine::ExtensionOption::~ExtensionOption()': the
      destructor: Python removes its C++ QAbstractFileEngine::ExtensionOption
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QAbstractFileEngine::ExtensionOption is created at the first
      use, not by 'QAbstractFileEngine::ExtensionOption(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QAbstractFileEngine::ExtensionOption back gives a
      copy the ritual made for Python, in a new cute
      QAbstractFileEngine::ExtensionOption.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QAbstractFileEngine::ExtensionOption'

    #  Qt's '~QAbstractFileEngine::ExtensionOption()'. Naming it makes this a
    #  value class: Python owns every C++
    #  QAbstractFileEngine::ExtensionOption behind a cute one, and removes it
    #  by this ritual.
    __delete_ritual__ = 'ritual_ZN19QAbstractFileEngine15ExtensionOptionD1Ev'

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

  class ExtensionReturn(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QAbstractFileEngine::ExtensionReturn: a plain
    Python object standing in front of one C++
    QAbstractFileEngine::ExtensionReturn.

    C++ hands a QAbstractFileEngine::ExtensionReturn around as a copy, so
    every C++ QAbstractFileEngine::ExtensionReturn behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QAbstractFileEngine::ExtensionReturn yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QAbstractFileEngine::ExtensionReturn::~ExtensionReturn()': the
      destructor: Python removes its C++ QAbstractFileEngine::ExtensionReturn
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QAbstractFileEngine::ExtensionReturn is created at the first
      use, not by 'QAbstractFileEngine::ExtensionReturn(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QAbstractFileEngine::ExtensionReturn back gives a
      copy the ritual made for Python, in a new cute
      QAbstractFileEngine::ExtensionReturn.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QAbstractFileEngine::ExtensionReturn'

    #  Qt's '~QAbstractFileEngine::ExtensionReturn()'. Naming it makes this a
    #  value class: Python owns every C++
    #  QAbstractFileEngine::ExtensionReturn behind a cute one, and removes it
    #  by this ritual.
    __delete_ritual__ = 'ritual_ZN19QAbstractFileEngine15ExtensionReturnD1Ev'

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

  class MapExtensionOption(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QAbstractFileEngine::MapExtensionOption: a plain
    Python object standing in front of one C++
    QAbstractFileEngine::MapExtensionOption.

    What exists
    -----------

    No function of Qt's QAbstractFileEngine::MapExtensionOption yet. It can
    be made from Python, in 1 way; see '__init__'.

    What has no ritual
    ------------------

    4 of the 5 functions Qt declares: 4 forbidden.

    What to expect
    --------------

    - The C++ QAbstractFileEngine::MapExtensionOption is created at the first
      use, not by 'QAbstractFileEngine::MapExtensionOption(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++ QAbstractFileEngine::MapExtensionOption.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QAbstractFileEngine::MapExtensionOption'

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

    @overload(int, int, QFileDevice.MemoryMapFlags)
    def __init__(
        self,
        off: int,
        sz: int,
        f: QFileDevice.MemoryMapFlags,
    ) -> None:
      """
      Notes what was given, for Qt's
      'QAbstractFileEngine::MapExtensionOption::MapExtensionOption(qint64
      off, qint64 sz, QFile::MemoryMapFlags f)', which is called at the first
      use.

      Qt's own words:
      https://doc.qt.io/qt-6/qabstractfileengine-mapextensionoption.html

      Parameters
      ----------

      off : int
        Passed on as it is.

      sz : int
        Passed on as it is.

      f : QFileDevice.MemoryMapFlags
        Passed on as its number.
      """
      #  QAbstractFileEngine::MapExtensionOption::MapExtensionOption(qint64
      #      off, qint64 sz, QFile::MemoryMapFlags f)
      self._noteCreation(
          QAbstractFileEngine.MapExtensionOption, lambda: Rituals.call(
              'ritual_ZN19QAbstractFileEngine18MapExtensionOptionC1Exx6QFla'
              'gsIN11QFileDevice13MemoryMapFlagEE',
              off, sz, f.value,
          ))

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

  class MapExtensionReturn(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QAbstractFileEngine::MapExtensionReturn: a plain
    Python object standing in front of one C++
    QAbstractFileEngine::MapExtensionReturn.

    What exists
    -----------

    No function of Qt's QAbstractFileEngine::MapExtensionReturn yet. It can
    be made from Python, in 1 way; see '__init__'.

    What has no ritual
    ------------------

    4 of the 5 functions Qt declares: 4 forbidden.

    What to expect
    --------------

    - The C++ QAbstractFileEngine::MapExtensionReturn is created at the first
      use, not by 'QAbstractFileEngine::MapExtensionReturn(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++ QAbstractFileEngine::MapExtensionReturn.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QAbstractFileEngine::MapExtensionReturn'

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

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QAbstractFileEngine::MapExtensionReturn::MapExtensionReturn()', which
      is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qabstractfileengine-mapextensionreturn.html
      """
      #  QAbstractFileEngine::MapExtensionReturn::MapExtensionReturn()
      self._noteCreation(
          QAbstractFileEngine.MapExtensionReturn, lambda: Rituals.call(
              'ritual_ZN19QAbstractFileEngine18MapExtensionReturnC1Ev',
          ))

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

  class UnMapExtensionOption(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QAbstractFileEngine::UnMapExtensionOption: a plain
    Python object standing in front of one C++
    QAbstractFileEngine::UnMapExtensionOption.

    What exists
    -----------

    No function of Qt's QAbstractFileEngine::UnMapExtensionOption yet. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QAbstractFileEngine::UnMapExtensionOption::UnMapExtensionOption(uchar
      *p)': takes a number to change where it is.

    What has no ritual
    ------------------

    4 of the 5 functions Qt declares: 4 forbidden.

    What to expect
    --------------

    - The C++ QAbstractFileEngine::UnMapExtensionOption is created at the
      first use, not by 'QAbstractFileEngine::UnMapExtensionOption(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++ QAbstractFileEngine::UnMapExtensionOption.
    - Each name of Qt's QAbstractFileEngine::UnMapExtensionOption that has no
      cute function yet, '__init__', holds a function that raises
      'NotImplementedError', and its docstring says why.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QAbstractFileEngine::UnMapExtensionOption'

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

    @staticmethod
    def __init__(*__, **_) -> Never:
      """
      Qt's
      'QAbstractFileEngine::UnMapExtensionOption::UnMapExtensionOption(uchar
      *p)': takes a number to change where it is.
      """
      raise NotImplementedError(
          "'QAbstractFileEngine.UnMapExtensionOption.__init__' has no cute "
          "function yet. Qt's "
          "'QAbstractFileEngine::UnMapExtensionOption::UnMapExtensionOption("
          "uchar *p)': takes a number to change where it is.")

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractFileEngine'

  #  A C++ QAbstractFileEngine Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractFileEngine'

  #  The functions Qt calls itself that QAbstractFileEngine is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'open': (
          'bool QAbstractFileEngine::open(QIODevice::OpenMode, '
          'std::optional<QFile::Permissions>)',
      ),
      'mkdir': (
          'bool QAbstractFileEngine::mkdir(const QString &, bool, '
          'std::optional<QFile::Permissions>) const',
      ),
      'setFileTime': (
          'bool QAbstractFileEngine::setFileTime(const QDateTime &, '
          'QFile::FileTime)',
      ),
      'fileTime': (
          'QDateTime QAbstractFileEngine::fileTime(QFile::FileTime) const',
      ),
      'endEntryList': (
          'IteratorUniquePtr QAbstractFileEngine::endEntryList()',
      ),
      'beginEntryList': (
          'IteratorUniquePtr QAbstractFileEngine::beginEntryList(const '
          'QString &, QDirListing::IteratorFlags, const QStringList &)',
      ),
      'read': (
          'qint64 QAbstractFileEngine::read(char *, qint64)',
      ),
      'readLine': (
          'qint64 QAbstractFileEngine::readLine(char *, qint64)',
      ),
      'write': (
          'qint64 QAbstractFileEngine::write(const char *, qint64)',
      ),
  }

  #  The functions Qt calls itself that QAbstractFileEngine is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'close': (
          ('_ZN19QAbstractFileEngine5closeEv',
           ('bool', 'number', ''),
           ()),
      ),
      'flush': (
          ('_ZN19QAbstractFileEngine5flushEv',
           ('bool', 'number', ''),
           ()),
      ),
      'syncToDisk': (
          ('_ZN19QAbstractFileEngine10syncToDiskEv',
           ('bool', 'number', ''),
           ()),
      ),
      'size': (
          ('_ZNK19QAbstractFileEngine4sizeEv',
           ('long long', 'number', ''),
           ()),
      ),
      'pos': (
          ('_ZNK19QAbstractFileEngine3posEv',
           ('long long', 'number', ''),
           ()),
      ),
      'seek': (
          ('_ZN19QAbstractFileEngine4seekEx',
           ('bool', 'number', ''),
           (
               ('long long', 'number', ''),
           )),
      ),
      'isSequential': (
          ('_ZNK19QAbstractFileEngine12isSequentialEv',
           ('bool', 'number', ''),
           ()),
      ),
      'remove': (
          ('_ZN19QAbstractFileEngine6removeEv',
           ('bool', 'number', ''),
           ()),
      ),
      'copy': (
          ('_ZN19QAbstractFileEngine4copyERK7QString',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'rename': (
          ('_ZN19QAbstractFileEngine6renameERK7QString',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'renameOverwrite': (
          ('_ZN19QAbstractFileEngine15renameOverwriteERK7QString',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'link': (
          ('_ZN19QAbstractFileEngine4linkERK7QString',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'rmdir': (
          ('_ZNK19QAbstractFileEngine5rmdirERK7QStringb',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
               ('bool', 'number', ''),
           )),
      ),
      'setSize': (
          ('_ZN19QAbstractFileEngine7setSizeEx',
           ('bool', 'number', ''),
           (
               ('long long', 'number', ''),
           )),
      ),
      'caseSensitive': (
          ('_ZNK19QAbstractFileEngine13caseSensitiveEv',
           ('bool', 'number', ''),
           ()),
      ),
      'isRelativePath': (
          ('_ZNK19QAbstractFileEngine14isRelativePathEv',
           ('bool', 'number', ''),
           ()),
      ),
      'fileFlags': (
          ('_ZNK19QAbstractFileEngine9fileFlagsE6QFlagsINS_8FileFlagEE',
           ('int', 'flags', 'QtCore:QAbstractFileEngine.FileFlag'),
           (
               ('int', 'flags', 'QtCore:QAbstractFileEngine.FileFlag'),
           )),
      ),
      'setPermissions': (
          ('_ZN19QAbstractFileEngine14setPermissionsEj',
           ('bool', 'number', ''),
           (
               ('unsigned int', 'number', ''),
           )),
      ),
      'id': (
          ('_ZNK19QAbstractFileEngine2idEv',
           ('address', 'value', 'QtCore:QByteArray'),
           ()),
      ),
      'fileName': (
          ('_ZNK19QAbstractFileEngine8fileNameENS_8FileNameE',
           ('address', 'text', ''),
           (
               ('int', 'enum', 'QtCore:QAbstractFileEngine.FileName'),
           )),
      ),
      'ownerId': (
          ('_ZNK19QAbstractFileEngine7ownerIdENS_9FileOwnerE',
           ('unsigned int', 'number', ''),
           (
               ('int', 'enum', 'QtCore:QAbstractFileEngine.FileOwner'),
           )),
      ),
      'owner': (
          ('_ZNK19QAbstractFileEngine5ownerENS_9FileOwnerE',
           ('address', 'text', ''),
           (
               ('int', 'enum', 'QtCore:QAbstractFileEngine.FileOwner'),
           )),
      ),
      'setFileName': (
          ('_ZN19QAbstractFileEngine11setFileNameERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'handle': (
          ('_ZNK19QAbstractFileEngine6handleEv',
           ('int', 'number', ''),
           ()),
      ),
      'cloneTo': (
          ('_ZN19QAbstractFileEngine7cloneToEPS_',
           ('int', 'enum', 'QtCore:QAbstractFileEngine.TriStateResult'),
           (
               ('address', 'address', 'QtCore:QAbstractFileEngine'),
           )),
      ),
      'extension': (
          ('_ZN19QAbstractFileEngine9extensionENS_9ExtensionEPKNS_15Extensi'
           'onOptionEPNS_15ExtensionReturnE',
           ('bool', 'number', ''),
           (
               ('int', 'enum', 'QtCore:QAbstractFileEngine.Extension'),
               ('address', 'address',
                'QtCore:QAbstractFileEngine.ExtensionOption'),
               ('address', 'address',
                'QtCore:QAbstractFileEngine.ExtensionReturn'),
           )),
      ),
      'supportsExtension': (
          ('_ZNK19QAbstractFileEngine17supportsExtensionENS_9ExtensionE',
           ('bool', 'number', ''),
           (
               ('int', 'enum', 'QtCore:QAbstractFileEngine.Extension'),
           )),
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
    Calls Qt's 'qint64 QAbstractFileEngine::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractfileengine.html#size
    """
    #  qint64 QAbstractFileEngine::size() const
    ritual = 'ritual_ZNK19QAbstractFileEngine4sizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QAbstractFileEngine4sizeEv'
    return self.uglySide.call(ritual)

  def pos(self) -> int:
    """
    Calls Qt's 'qint64 QAbstractFileEngine::pos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractfileengine.html#pos
    """
    #  qint64 QAbstractFileEngine::pos() const
    ritual = 'ritual_ZNK19QAbstractFileEngine3posEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QAbstractFileEngine3posEv'
    return self.uglySide.call(ritual)

  def isSequential(self) -> bool:
    """
    Calls Qt's 'bool QAbstractFileEngine::isSequential() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractfileengine.html#isSequential
    """
    #  bool QAbstractFileEngine::isSequential() const
    ritual = 'ritual_ZNK19QAbstractFileEngine12isSequentialEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QAbstractFileEngine12isSequentialEv'
    return self.uglySide.call(ritual)

  @overload(str, bool)
  def rmdir(self, dirName: str, recurseParentDirectories: bool) -> bool:
    """
    Calls Qt's 'bool QAbstractFileEngine::rmdir(const QString &dirName, bool
    recurseParentDirectories) const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractfileengine.html#rmdir

    Parameters
    ----------

    dirName : str
      Passed on as it is: a QString is made of it for the call.

    recurseParentDirectories : bool
      Passed on as it is.
    """
    #  bool QAbstractFileEngine::rmdir(const QString &dirName, bool
    #      recurseParentDirectories) const
    ritual = 'ritual_ZNK19QAbstractFileEngine5rmdirERK7QStringb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QAbstractFileEngine5rmdirERK7QStringb'
    return self.uglySide.call(ritual, dirName, recurseParentDirectories)

  def caseSensitive(self) -> bool:
    """
    Calls Qt's 'bool QAbstractFileEngine::caseSensitive() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractfileengine.html#caseSensitive
    """
    #  bool QAbstractFileEngine::caseSensitive() const
    ritual = 'ritual_ZNK19QAbstractFileEngine13caseSensitiveEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QAbstractFileEngine13caseSensitiveEv'
    return self.uglySide.call(ritual)

  def isRelativePath(self) -> bool:
    """
    Calls Qt's 'bool QAbstractFileEngine::isRelativePath() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractfileengine.html#isRelativePath
    """
    #  bool QAbstractFileEngine::isRelativePath() const
    ritual = 'ritual_ZNK19QAbstractFileEngine14isRelativePathEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QAbstractFileEngine14isRelativePathEv'
    return self.uglySide.call(ritual)

  @overload()
  @overload(FileFlags)
  def fileFlags(self, type: FileFlags = FileFlags.FileInfoAll) -> FileFlags:
    """
    Calls Qt's 'FileFlags QAbstractFileEngine::fileFlags(FileFlags type)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractfileengine.html#fileFlags

    Parameters
    ----------

    type : FileFlags
      Passed on as its number. May be left out, as in Qt: it is then
      FileFlags.FileInfoAll.

    Returns
    -------

    FileFlags
      The value standing for the combination Qt gave back.
    """
    #  FileFlags QAbstractFileEngine::fileFlags(FileFlags type) const
    ritual = (
        'ritual_ZNK19QAbstractFileEngine9fileFlagsE6QFlagsINS_8FileFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QAbstractFileEngine9fileFlagsE6QFlagsINS_8FileFl'
          'agEE')
    return QAbstractFileEngine.FileFlags(self.uglySide.call(
        ritual, type.value,
    ))

  def id(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QAbstractFileEngine::id() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractfileengine.html#id

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QAbstractFileEngine::id() const
    ritual = 'ritual_ZNK19QAbstractFileEngine2idEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QAbstractFileEngine2idEv'
    address = self.uglySide.call(ritual)
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  @overload()
  @overload(FileName)
  def fileName(self, file: FileName = FileName.DefaultName) -> str:
    """
    Calls Qt's 'QString QAbstractFileEngine::fileName(FileName file) const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractfileengine.html#fileName

    Parameters
    ----------

    file : FileName
      Passed on as its number. May be left out, as in Qt: it is then
      FileName.DefaultName.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstractFileEngine::fileName(FileName file) const
    ritual = 'ritual_ZNK19QAbstractFileEngine8fileNameENS_8FileNameE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QAbstractFileEngine8fileNameENS_8FileNameE'
    return self.uglySide.call(ritual, file.value)

  @overload(FileOwner)
  def ownerId(self, a0: FileOwner) -> int:
    """
    Calls Qt's 'uint QAbstractFileEngine::ownerId(FileOwner a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractfileengine.html#ownerId

    Parameters
    ----------

    a0 : FileOwner
      Passed on as its number.
    """
    #  uint QAbstractFileEngine::ownerId(FileOwner a0) const
    ritual = 'ritual_ZNK19QAbstractFileEngine7ownerIdENS_9FileOwnerE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QAbstractFileEngine7ownerIdENS_9FileOwnerE'
    return self.uglySide.call(ritual, a0.value)

  @overload(FileOwner)
  def owner(self, a0: FileOwner) -> str:
    """
    Calls Qt's 'QString QAbstractFileEngine::owner(FileOwner a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractfileengine.html#owner

    Parameters
    ----------

    a0 : FileOwner
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstractFileEngine::owner(FileOwner a0) const
    ritual = 'ritual_ZNK19QAbstractFileEngine5ownerENS_9FileOwnerE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QAbstractFileEngine5ownerENS_9FileOwnerE'
    return self.uglySide.call(ritual, a0.value)

  def handle(self) -> int:
    """
    Calls Qt's 'int QAbstractFileEngine::handle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractfileengine.html#handle
    """
    #  int QAbstractFileEngine::handle() const
    ritual = 'ritual_ZNK19QAbstractFileEngine6handleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QAbstractFileEngine6handleEv'
    return self.uglySide.call(ritual)

  def atEnd(self) -> bool:
    """
    Calls Qt's 'bool QAbstractFileEngine::atEnd() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractfileengine.html#atEnd
    """
    #  bool QAbstractFileEngine::atEnd() const
    return self.uglySide.call('ritual_ZNK19QAbstractFileEngine5atEndEv')

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QAbstractFileEngine::errorString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractfileengine.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstractFileEngine::errorString() const
    return self.uglySide.call(
        'ritual_ZNK19QAbstractFileEngine11errorStringEv',
    )

  @overload(Extension)
  def supportsExtension(self, extension: Extension) -> bool:
    """
    Calls Qt's 'bool QAbstractFileEngine::supportsExtension(Extension
    extension) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractfileengine.html#supportsExtension

    Parameters
    ----------

    extension : Extension
      Passed on as its number.
    """
    #  bool QAbstractFileEngine::supportsExtension(Extension extension) const
    ritual = (
        'ritual_ZNK19QAbstractFileEngine17supportsExtensionENS_9ExtensionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QAbstractFileEngine17supportsExtensionENS_9Exten'
          'sionE')
    return self.uglySide.call(ritual, extension.value)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setSize(self, size: int) -> bool:
    """
    Calls Qt's 'bool QAbstractFileEngine::setSize(qint64 size)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractfileengine.html#setSize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  bool QAbstractFileEngine::setSize(qint64 size)
    ritual = 'ritual_ZN19QAbstractFileEngine7setSizeEx'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QAbstractFileEngine7setSizeEx'
    return self.uglySide.call(ritual, size)

  @overload(int)
  def setPermissions(self, perms: int) -> bool:
    """
    Calls Qt's 'bool QAbstractFileEngine::setPermissions(uint perms)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractfileengine.html#setPermissions

    Parameters
    ----------

    perms : int
      Passed on as it is.
    """
    #  bool QAbstractFileEngine::setPermissions(uint perms)
    ritual = 'ritual_ZN19QAbstractFileEngine14setPermissionsEj'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QAbstractFileEngine14setPermissionsEj'
    return self.uglySide.call(ritual, perms)

  @overload(str)
  def setFileName(self, file: str) -> None:
    """
    Calls Qt's 'void QAbstractFileEngine::setFileName(const QString &file)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractfileengine.html#setFileName

    Parameters
    ----------

    file : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstractFileEngine::setFileName(const QString &file)
    ritual = 'ritual_ZN19QAbstractFileEngine11setFileNameERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QAbstractFileEngine11setFileNameERK7QString'
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
    Notes what was given, for Qt's
    'QAbstractFileEngine::QAbstractFileEngine()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractfileengine.html#QAbstractFileEngine
    """
    #  QAbstractFileEngine::QAbstractFileEngine()
    self._noteCreation(QAbstractFileEngine, lambda: Rituals.call(
        'ritual_ZN19QAbstractFileEngineC1Ev',
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

  def close(self) -> bool:
    """
    Calls Qt's 'bool QAbstractFileEngine::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractfileengine.html#close
    """
    #  bool QAbstractFileEngine::close()
    ritual = 'ritual_ZN19QAbstractFileEngine5closeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QAbstractFileEngine5closeEv'
    return self.uglySide.call(ritual)

  def flush(self) -> bool:
    """
    Calls Qt's 'bool QAbstractFileEngine::flush()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractfileengine.html#flush
    """
    #  bool QAbstractFileEngine::flush()
    ritual = 'ritual_ZN19QAbstractFileEngine5flushEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QAbstractFileEngine5flushEv'
    return self.uglySide.call(ritual)

  def syncToDisk(self) -> bool:
    """
    Calls Qt's 'bool QAbstractFileEngine::syncToDisk()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractfileengine.html#syncToDisk
    """
    #  bool QAbstractFileEngine::syncToDisk()
    ritual = 'ritual_ZN19QAbstractFileEngine10syncToDiskEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QAbstractFileEngine10syncToDiskEv'
    return self.uglySide.call(ritual)

  @overload(int)
  def seek(self, pos: int) -> bool:
    """
    Calls Qt's 'bool QAbstractFileEngine::seek(qint64 pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractfileengine.html#seek

    Parameters
    ----------

    pos : int
      Passed on as it is.
    """
    #  bool QAbstractFileEngine::seek(qint64 pos)
    ritual = 'ritual_ZN19QAbstractFileEngine4seekEx'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QAbstractFileEngine4seekEx'
    return self.uglySide.call(ritual, pos)

  def remove(self) -> bool:
    """
    Calls Qt's 'bool QAbstractFileEngine::remove()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractfileengine.html#remove
    """
    #  bool QAbstractFileEngine::remove()
    ritual = 'ritual_ZN19QAbstractFileEngine6removeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QAbstractFileEngine6removeEv'
    return self.uglySide.call(ritual)

  @overload(str)
  def copy(self, newName: str) -> bool:
    """
    Calls Qt's 'bool QAbstractFileEngine::copy(const QString &newName)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractfileengine.html#copy

    Parameters
    ----------

    newName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QAbstractFileEngine::copy(const QString &newName)
    ritual = 'ritual_ZN19QAbstractFileEngine4copyERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QAbstractFileEngine4copyERK7QString'
    return self.uglySide.call(ritual, newName)

  @overload(str)
  def rename(self, newName: str) -> bool:
    """
    Calls Qt's 'bool QAbstractFileEngine::rename(const QString &newName)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractfileengine.html#rename

    Parameters
    ----------

    newName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QAbstractFileEngine::rename(const QString &newName)
    ritual = 'ritual_ZN19QAbstractFileEngine6renameERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QAbstractFileEngine6renameERK7QString'
    return self.uglySide.call(ritual, newName)

  @overload(str)
  def renameOverwrite(self, newName: str) -> bool:
    """
    Calls Qt's 'bool QAbstractFileEngine::renameOverwrite(const QString
    &newName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractfileengine.html#renameOverwrite

    Parameters
    ----------

    newName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QAbstractFileEngine::renameOverwrite(const QString &newName)
    ritual = 'ritual_ZN19QAbstractFileEngine15renameOverwriteERK7QString'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QAbstractFileEngine15renameOverwriteERK7QString')
    return self.uglySide.call(ritual, newName)

  @overload(str)
  def link(self, newName: str) -> bool:
    """
    Calls Qt's 'bool QAbstractFileEngine::link(const QString &newName)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractfileengine.html#link

    Parameters
    ----------

    newName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QAbstractFileEngine::link(const QString &newName)
    ritual = 'ritual_ZN19QAbstractFileEngine4linkERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QAbstractFileEngine4linkERK7QString'
    return self.uglySide.call(ritual, newName)

  @overload(THIS)
  @overload(NoneType)
  def cloneTo(self, target: Optional[QAbstractFileEngine]) -> TriStateResult:
    """
    Calls Qt's 'TriStateResult
    QAbstractFileEngine::cloneTo(QAbstractFileEngine *target)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractfileengine.html#cloneTo

    Parameters
    ----------

    target : Optional[QAbstractFileEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    TriStateResult
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TriStateResult(number)'
      gives.
    """
    #  TriStateResult QAbstractFileEngine::cloneTo(QAbstractFileEngine
    #      *target)
    ritual = 'ritual_ZN19QAbstractFileEngine7cloneToEPS_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QAbstractFileEngine7cloneToEPS_'
    return QAbstractFileEngine.TriStateResult(self.uglySide.call(
        ritual, self._addressOf(target),
    ))

  @overload(str, int)
  @overload(NoneType, int)
  def write(self, data: Optional[str], len: int) -> int:
    """
    Calls Qt's 'qint64 QAbstractFileEngine::write(const char *data, qint64
    len)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractfileengine.html#write

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    len : int
      Passed on as it is.
    """
    #  qint64 QAbstractFileEngine::write(const char *data, qint64 len)
    return self.uglySide.call(
        'ritual_ZN19QAbstractFileEngine5writeEPKcx',
        self._bytesOf(data), len,
    )

  @overload(Extension)
  @overload(Extension, ExtensionOption)
  @overload(Extension, NoneType)
  @overload(Extension, ExtensionOption, ExtensionReturn)
  @overload(Extension, ExtensionOption, NoneType)
  @overload(Extension, NoneType, ExtensionReturn)
  @overload(Extension, NoneType, NoneType)
  def extension(
      self,
      extension: Extension,
      option: Optional[ExtensionOption] = None,
      output: Optional[ExtensionReturn] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QAbstractFileEngine::extension(Extension extension,
    const ExtensionOption *option, ExtensionReturn *output)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractfileengine.html#extension

    Parameters
    ----------

    extension : Extension
      Passed on as its number.

    option : Optional[ExtensionOption]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    output : Optional[ExtensionReturn]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  bool QAbstractFileEngine::extension(Extension extension, const
    #      ExtensionOption *option, ExtensionReturn *output)
    ritual = (
        'ritual_ZN19QAbstractFileEngine9extensionENS_9ExtensionEPKNS_15Exte'
        'nsionOptionEPNS_15ExtensionReturnE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QAbstractFileEngine9extensionENS_9ExtensionEPKNS_'
          '15ExtensionOptionEPNS_15ExtensionReturnE')
    return self.uglySide.call(
        ritual,
        extension.value, self._addressOf(option), self._addressOf(output),
    )

  def d_func(self) -> Optional[QAbstractFileEnginePrivate]:
    """
    Calls Qt's 'QAbstractFileEnginePrivate *QAbstractFileEngine::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractfileengine.html#d_func

    Returns
    -------

    Optional[QAbstractFileEnginePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractFileEnginePrivate *QAbstractFileEngine::d_func()
    address = self.uglySide.call('ritual_ZN19QAbstractFileEngine6d_funcEv')
    from . import QAbstractFileEnginePrivate
    return QAbstractFileEnginePrivate._cuteAt(address)

  @staticmethod
  def beginEntryList(*__, **_) -> Never:
    """
    Qt's 'IteratorUniquePtr QAbstractFileEngine::beginEntryList(const QString
    &path, QDirListing::IteratorFlags filters, const QStringList
    &filterNames)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QAbstractFileEngine.beginEntryList' has no cute function yet. "
        "Qt's 'IteratorUniquePtr QAbstractFileEngine::beginEntryList(const "
        "QString &path, QDirListing::IteratorFlags filters, const "
        "QStringList &filterNames)': gives a type Python has no way to take "
        "yet.")

  @staticmethod
  def create(*__, **_) -> Never:
    """
    Qt's 'std::unique_ptr<QAbstractFileEngine>
    QAbstractFileEngine::create(const QString &fileName)': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QAbstractFileEngine.create' has no cute function yet. Qt's "
        "'std::unique_ptr<QAbstractFileEngine> "
        "QAbstractFileEngine::create(const QString &fileName)': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def endEntryList(*__, **_) -> Never:
    """
    Qt's 'IteratorUniquePtr QAbstractFileEngine::endEntryList()': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QAbstractFileEngine.endEntryList' has no cute function yet. Qt's "
        "'IteratorUniquePtr QAbstractFileEngine::endEntryList()': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def error(*__, **_) -> Never:
    """
    Qt's 'QFile::FileError QAbstractFileEngine::error() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QAbstractFileEngine.error' has no cute function yet. Qt's "
        "'QFile::FileError QAbstractFileEngine::error() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def fileTime(*__, **_) -> Never:
    """
    Qt's 'QDateTime QAbstractFileEngine::fileTime(QFile::FileTime time)
    const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractFileEngine.fileTime' has no cute function yet. Qt's "
        "'QDateTime QAbstractFileEngine::fileTime(QFile::FileTime time) "
        "const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def map(*__, **_) -> Never:
    """
    Qt's 'uchar *QAbstractFileEngine::map(qint64 offset, qint64 size,
    QFile::MemoryMapFlags flags)': takes or gives a type that cannot be
    passed yet: uchar *.
    """
    raise NotImplementedError(
        "'QAbstractFileEngine.map' has no cute function yet. Qt's 'uchar "
        "*QAbstractFileEngine::map(qint64 offset, qint64 size, "
        "QFile::MemoryMapFlags flags)': takes or gives a type that cannot "
        "be passed yet: uchar *.")

  @staticmethod
  def mkdir(*__, **_) -> Never:
    """
    Qt's 'bool QAbstractFileEngine::mkdir(const QString &dirName, bool
    createParentDirectories, std::optional<QFile::Permissions> permissions)
    const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractFileEngine.mkdir' has no cute function yet. Qt's 'bool "
        "QAbstractFileEngine::mkdir(const QString &dirName, bool "
        "createParentDirectories, std::optional<QFile::Permissions> "
        "permissions) const': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def open(*__, **_) -> Never:
    """
    Qt's 'bool QAbstractFileEngine::open(QIODevice::OpenMode openMode,
    std::optional<QFile::Permissions> permissions)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractFileEngine.open' has no cute function yet. Qt's 'bool "
        "QAbstractFileEngine::open(QIODevice::OpenMode openMode, "
        "std::optional<QFile::Permissions> permissions)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'qint64 QAbstractFileEngine::read(char *data, qint64 maxlen)': names
    'char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QAbstractFileEngine.read' has no cute function yet. Qt's 'qint64 "
        "QAbstractFileEngine::read(char *data, qint64 maxlen)': names "
        "'char', which has no cute class yet.")

  @staticmethod
  def readLine(*__, **_) -> Never:
    """
    Qt's 'qint64 QAbstractFileEngine::readLine(char *data, qint64 maxlen)':
    names 'char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QAbstractFileEngine.readLine' has no cute function yet. Qt's "
        "'qint64 QAbstractFileEngine::readLine(char *data, qint64 maxlen)': "
        "names 'char', which has no cute class yet.")

  @staticmethod
  def setError(*__, **_) -> Never:
    """
    Qt's 'void QAbstractFileEngine::setError(QFile::FileError error, const
    QString &str)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractFileEngine.setError' has no cute function yet. Qt's "
        "'void QAbstractFileEngine::setError(QFile::FileError error, const "
        "QString &str)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setFileTime(*__, **_) -> Never:
    """
    Qt's 'bool QAbstractFileEngine::setFileTime(const QDateTime &newDate,
    QFile::FileTime time)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractFileEngine.setFileTime' has no cute function yet. Qt's "
        "'bool QAbstractFileEngine::setFileTime(const QDateTime &newDate, "
        "QFile::FileTime time)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def unmap(*__, **_) -> Never:
    """
    Qt's 'bool QAbstractFileEngine::unmap(uchar *ptr)': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QAbstractFileEngine.unmap' has no cute function yet. Qt's 'bool "
        "QAbstractFileEngine::unmap(uchar *ptr)': takes a number to change "
        "where it is.")
