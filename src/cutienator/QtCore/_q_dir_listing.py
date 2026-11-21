"""
QDirListing binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qdirlisting.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute, WAIT
from ..occult import Rituals
from . import QFileDevice

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QDateTime, QFileInfo, QTimeZone


class QDirListing(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDirListing: a plain Python object standing in front
  of one C++ QDirListing.

  What exists
  -----------

  Every function of Qt's QDirListing that has a ritual and that Python can
  call so far, 5 names in all: 'iteratorPath', 'iteratorFlags', 'end',
  'cend', 'constEnd'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDirListing::~QDirListing()': the destructor: Python never removes
    a C++ QDirListing.

  What has no ritual
  ------------------

  14 of the 21 functions Qt declares: 8 takes or gives a type that cannot be
  passed yet; 2 private; 2 forbidden; 1 declared and nowhere to be found; 1 a
  template.

  What to expect
  --------------

  - The C++ QDirListing is created at the first use, not by
    'QDirListing(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDirListing.
  """

  #  The enums Qt writes inside QDirListing, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class IteratorFlag(CuteFlags, scoped=True):
    """
    The flags enum 'QDirListing::IteratorFlag' of Qt, with the 15 names Qt
    gives in it. Qt names the type of its combinations
    'QDirListing::IteratorFlags'. C++ keeps these names inside the enum, so
    the class that holds the enum does not have them.
    """

    Default = 0x0
    ExcludeFiles = 0x4
    ExcludeDirs = 0x8
    ExcludeSpecial = 0x10
    ExcludeOther = 0x10
    ResolveSymlinks = 0x20
    FilesOnly = 0x18
    DirsOnly = 0x14
    IncludeHidden = 0x40
    IncludeDotAndDotDot = 0x80
    CaseSensitive = 0x100
    Recursive = 0x400
    FollowDirSymlinks = 0x800
    IncludeBrokenSymlinks = 0x1000
    NoNameFiltersForDirs = 0x40000

  IteratorFlags = IteratorFlag

  #  The classes Qt writes inside QDirListing, each a class in here as in
  #  C++.

  class DirEntry(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QDirListing::DirEntry: a plain Python object
    standing in front of one C++ QDirListing::DirEntry.

    C++ hands a QDirListing::DirEntry around as a copy, so every C++
    QDirListing::DirEntry behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QDirListing::DirEntry that has a ritual and that
    Python can call so far, 25 names in all: 'fileName', 'baseName',
    'completeBaseName', 'suffix', 'bundleName', 'completeSuffix', 'filePath',
    'isDir', 'isFile', 'isSymLink', 'exists', 'isHidden', 'isReadable',
    'isWritable', 'isExecutable', 'fileInfo', 'canonicalFilePath',
    'absoluteFilePath', 'absolutePath', 'size', 'birthTime',
    'metadataChangeTime', 'lastModified', 'lastRead', 'fileTime'. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QDirListing::DirEntry::~DirEntry()': the destructor: Python
      removes its C++ QDirListing::DirEntry by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QDirListing::DirEntry is created at the first use, not by
      'QDirListing::DirEntry(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QDirListing::DirEntry back gives a copy the ritual
      made for Python, in a new cute QDirListing::DirEntry.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QTimeZone = WAIT['QTimeZone']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QDirListing::DirEntry'

    #  Qt's '~QDirListing::DirEntry()'. Naming it makes this a value class:
    #  Python owns every C++ QDirListing::DirEntry behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN11QDirListing8DirEntryD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def fileName(self) -> str:
      """
      Calls Qt's 'QString QDirListing::DirEntry::fileName() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdirlisting-direntry.html#fileName

      Returns
      -------

      str
        The text Qt gave back.
      """
      #  QString QDirListing::DirEntry::fileName() const
      return self.uglySide.call(
          'ritual_ZNK11QDirListing8DirEntry8fileNameEv',
      )

    def baseName(self) -> str:
      """
      Calls Qt's 'QString QDirListing::DirEntry::baseName() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdirlisting-direntry.html#baseName

      Returns
      -------

      str
        The text Qt gave back.
      """
      #  QString QDirListing::DirEntry::baseName() const
      return self.uglySide.call(
          'ritual_ZNK11QDirListing8DirEntry8baseNameEv',
      )

    def completeBaseName(self) -> str:
      """
      Calls Qt's 'QString QDirListing::DirEntry::completeBaseName() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdirlisting-direntry.html#completeBaseName

      Returns
      -------

      str
        The text Qt gave back.
      """
      #  QString QDirListing::DirEntry::completeBaseName() const
      return self.uglySide.call(
          'ritual_ZNK11QDirListing8DirEntry16completeBaseNameEv',
      )

    def suffix(self) -> str:
      """
      Calls Qt's 'QString QDirListing::DirEntry::suffix() const'.

      Qt's own words: https://doc.qt.io/qt-6/qdirlisting-direntry.html#suffix

      Returns
      -------

      str
        The text Qt gave back.
      """
      #  QString QDirListing::DirEntry::suffix() const
      return self.uglySide.call('ritual_ZNK11QDirListing8DirEntry6suffixEv')

    def bundleName(self) -> str:
      """
      Calls Qt's 'QString QDirListing::DirEntry::bundleName() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdirlisting-direntry.html#bundleName

      Returns
      -------

      str
        The text Qt gave back.
      """
      #  QString QDirListing::DirEntry::bundleName() const
      return self.uglySide.call(
          'ritual_ZNK11QDirListing8DirEntry10bundleNameEv',
      )

    def completeSuffix(self) -> str:
      """
      Calls Qt's 'QString QDirListing::DirEntry::completeSuffix() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdirlisting-direntry.html#completeSuffix

      Returns
      -------

      str
        The text Qt gave back.
      """
      #  QString QDirListing::DirEntry::completeSuffix() const
      return self.uglySide.call(
          'ritual_ZNK11QDirListing8DirEntry14completeSuffixEv',
      )

    def filePath(self) -> str:
      """
      Calls Qt's 'QString QDirListing::DirEntry::filePath() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdirlisting-direntry.html#filePath

      Returns
      -------

      str
        The text Qt gave back.
      """
      #  QString QDirListing::DirEntry::filePath() const
      return self.uglySide.call(
          'ritual_ZNK11QDirListing8DirEntry8filePathEv',
      )

    def isDir(self) -> bool:
      """
      Calls Qt's 'bool QDirListing::DirEntry::isDir() const'.

      Qt's own words: https://doc.qt.io/qt-6/qdirlisting-direntry.html#isDir
      """
      #  bool QDirListing::DirEntry::isDir() const
      return self.uglySide.call('ritual_ZNK11QDirListing8DirEntry5isDirEv')

    def isFile(self) -> bool:
      """
      Calls Qt's 'bool QDirListing::DirEntry::isFile() const'.

      Qt's own words: https://doc.qt.io/qt-6/qdirlisting-direntry.html#isFile
      """
      #  bool QDirListing::DirEntry::isFile() const
      return self.uglySide.call('ritual_ZNK11QDirListing8DirEntry6isFileEv')

    def isSymLink(self) -> bool:
      """
      Calls Qt's 'bool QDirListing::DirEntry::isSymLink() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdirlisting-direntry.html#isSymLink
      """
      #  bool QDirListing::DirEntry::isSymLink() const
      return self.uglySide.call(
          'ritual_ZNK11QDirListing8DirEntry9isSymLinkEv',
      )

    def exists(self) -> bool:
      """
      Calls Qt's 'bool QDirListing::DirEntry::exists() const'.

      Qt's own words: https://doc.qt.io/qt-6/qdirlisting-direntry.html#exists
      """
      #  bool QDirListing::DirEntry::exists() const
      return self.uglySide.call('ritual_ZNK11QDirListing8DirEntry6existsEv')

    def isHidden(self) -> bool:
      """
      Calls Qt's 'bool QDirListing::DirEntry::isHidden() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdirlisting-direntry.html#isHidden
      """
      #  bool QDirListing::DirEntry::isHidden() const
      return self.uglySide.call(
          'ritual_ZNK11QDirListing8DirEntry8isHiddenEv',
      )

    def isReadable(self) -> bool:
      """
      Calls Qt's 'bool QDirListing::DirEntry::isReadable() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdirlisting-direntry.html#isReadable
      """
      #  bool QDirListing::DirEntry::isReadable() const
      return self.uglySide.call(
          'ritual_ZNK11QDirListing8DirEntry10isReadableEv',
      )

    def isWritable(self) -> bool:
      """
      Calls Qt's 'bool QDirListing::DirEntry::isWritable() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdirlisting-direntry.html#isWritable
      """
      #  bool QDirListing::DirEntry::isWritable() const
      return self.uglySide.call(
          'ritual_ZNK11QDirListing8DirEntry10isWritableEv',
      )

    def isExecutable(self) -> bool:
      """
      Calls Qt's 'bool QDirListing::DirEntry::isExecutable() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdirlisting-direntry.html#isExecutable
      """
      #  bool QDirListing::DirEntry::isExecutable() const
      return self.uglySide.call(
          'ritual_ZNK11QDirListing8DirEntry12isExecutableEv',
      )

    def fileInfo(self) -> QFileInfo:
      """
      Calls Qt's 'QFileInfo QDirListing::DirEntry::fileInfo() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdirlisting-direntry.html#fileInfo

      Returns
      -------

      QFileInfo
        A new cute QFileInfo around the copy Qt gave back. Python owns it.
      """
      #  QFileInfo QDirListing::DirEntry::fileInfo() const
      address = self.uglySide.call(
          'ritual_ZNK11QDirListing8DirEntry8fileInfoEv',
      )
      from . import QFileInfo
      return QFileInfo._cuteOwning(address)

    def canonicalFilePath(self) -> str:
      """
      Calls Qt's 'QString QDirListing::DirEntry::canonicalFilePath() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdirlisting-direntry.html#canonicalFilePath

      Returns
      -------

      str
        The text Qt gave back.
      """
      #  QString QDirListing::DirEntry::canonicalFilePath() const
      return self.uglySide.call(
          'ritual_ZNK11QDirListing8DirEntry17canonicalFilePathEv',
      )

    def absoluteFilePath(self) -> str:
      """
      Calls Qt's 'QString QDirListing::DirEntry::absoluteFilePath() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdirlisting-direntry.html#absoluteFilePath

      Returns
      -------

      str
        The text Qt gave back.
      """
      #  QString QDirListing::DirEntry::absoluteFilePath() const
      return self.uglySide.call(
          'ritual_ZNK11QDirListing8DirEntry16absoluteFilePathEv',
      )

    def absolutePath(self) -> str:
      """
      Calls Qt's 'QString QDirListing::DirEntry::absolutePath() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdirlisting-direntry.html#absolutePath

      Returns
      -------

      str
        The text Qt gave back.
      """
      #  QString QDirListing::DirEntry::absolutePath() const
      return self.uglySide.call(
          'ritual_ZNK11QDirListing8DirEntry12absolutePathEv',
      )

    def size(self) -> int:
      """
      Calls Qt's 'qint64 QDirListing::DirEntry::size() const'.

      Qt's own words: https://doc.qt.io/qt-6/qdirlisting-direntry.html#size
      """
      #  qint64 QDirListing::DirEntry::size() const
      return self.uglySide.call('ritual_ZNK11QDirListing8DirEntry4sizeEv')

    @overload(QTimeZone)
    def birthTime(self, tz: QTimeZone) -> QDateTime:
      """
      Calls Qt's 'QDateTime QDirListing::DirEntry::birthTime(const QTimeZone
      &tz) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdirlisting-direntry.html#birthTime

      Parameters
      ----------

      tz : QTimeZone
        Passed on as a value: Qt reads the C++ QTimeZone, which stays
        Python's own.

      Returns
      -------

      QDateTime
        A new cute QDateTime around the copy Qt gave back. Python owns it.
      """
      #  QDateTime QDirListing::DirEntry::birthTime(const QTimeZone &tz)
      #      const
      address = self.uglySide.call(
          'ritual_ZNK11QDirListing8DirEntry9birthTimeERK9QTimeZone',
          self._valueOf(tz),
      )
      from . import QDateTime
      return QDateTime._cuteOwning(address)

    @overload(QTimeZone)
    def metadataChangeTime(self, tz: QTimeZone) -> QDateTime:
      """
      Calls Qt's 'QDateTime QDirListing::DirEntry::metadataChangeTime(const
      QTimeZone &tz) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdirlisting-direntry.html#metadataChangeTime

      Parameters
      ----------

      tz : QTimeZone
        Passed on as a value: Qt reads the C++ QTimeZone, which stays
        Python's own.

      Returns
      -------

      QDateTime
        A new cute QDateTime around the copy Qt gave back. Python owns it.
      """
      #  QDateTime QDirListing::DirEntry::metadataChangeTime(const QTimeZone
      #      &tz) const
      address = self.uglySide.call(
          'ritual_ZNK11QDirListing8DirEntry18metadataChangeTimeERK9QTimeZon'
          'e',
          self._valueOf(tz),
      )
      from . import QDateTime
      return QDateTime._cuteOwning(address)

    @overload(QTimeZone)
    def lastModified(self, tz: QTimeZone) -> QDateTime:
      """
      Calls Qt's 'QDateTime QDirListing::DirEntry::lastModified(const
      QTimeZone &tz) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdirlisting-direntry.html#lastModified

      Parameters
      ----------

      tz : QTimeZone
        Passed on as a value: Qt reads the C++ QTimeZone, which stays
        Python's own.

      Returns
      -------

      QDateTime
        A new cute QDateTime around the copy Qt gave back. Python owns it.
      """
      #  QDateTime QDirListing::DirEntry::lastModified(const QTimeZone &tz)
      #      const
      address = self.uglySide.call(
          'ritual_ZNK11QDirListing8DirEntry12lastModifiedERK9QTimeZone',
          self._valueOf(tz),
      )
      from . import QDateTime
      return QDateTime._cuteOwning(address)

    @overload(QTimeZone)
    def lastRead(self, tz: QTimeZone) -> QDateTime:
      """
      Calls Qt's 'QDateTime QDirListing::DirEntry::lastRead(const QTimeZone
      &tz) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdirlisting-direntry.html#lastRead

      Parameters
      ----------

      tz : QTimeZone
        Passed on as a value: Qt reads the C++ QTimeZone, which stays
        Python's own.

      Returns
      -------

      QDateTime
        A new cute QDateTime around the copy Qt gave back. Python owns it.
      """
      #  QDateTime QDirListing::DirEntry::lastRead(const QTimeZone &tz) const
      address = self.uglySide.call(
          'ritual_ZNK11QDirListing8DirEntry8lastReadERK9QTimeZone',
          self._valueOf(tz),
      )
      from . import QDateTime
      return QDateTime._cuteOwning(address)

    @overload(QFileDevice.FileTime, QTimeZone)
    def fileTime(
        self,
        type: QFileDevice.FileTime,
        tz: QTimeZone,
    ) -> QDateTime:
      """
      Calls Qt's 'QDateTime
      QDirListing::DirEntry::fileTime(QFileDevice::FileTime type, const
      QTimeZone &tz) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdirlisting-direntry.html#fileTime

      Parameters
      ----------

      type : QFileDevice.FileTime
        Passed on as its number.

      tz : QTimeZone
        Passed on as a value: Qt reads the C++ QTimeZone, which stays
        Python's own.

      Returns
      -------

      QDateTime
        A new cute QDateTime around the copy Qt gave back. Python owns it.
      """
      #  QDateTime QDirListing::DirEntry::fileTime(QFileDevice::FileTime
      #      type, const QTimeZone &tz) const
      address = self.uglySide.call(
          'ritual_ZNK11QDirListing8DirEntry8fileTimeEN11QFileDevice8FileTim'
          'eERK9QTimeZone',
          type.value, self._valueOf(tz),
      )
      from . import QDateTime
      return QDateTime._cuteOwning(address)

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

  class const_iterator(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QDirListing::const_iterator: a plain Python object
    standing in front of one C++ QDirListing::const_iterator.

    What exists
    -----------

    No function of Qt's QDirListing::const_iterator yet. It can be made from
    Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'void QDirListing::const_iterator::operator++(int a0)': an
      operator, which is not reflected yet.

    What has no ritual
    ------------------

    9 of the 11 functions Qt declares: 5 takes or gives a type that cannot be
    passed yet; 2 forbidden; 2 private.

    What to expect
    --------------

    - The C++ QDirListing::const_iterator is created at the first use, not by
      'QDirListing::const_iterator(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++ QDirListing::const_iterator.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QDirListing::const_iterator'

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
      'QDirListing::const_iterator::const_iterator()', which is called at the
      first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qdirlisting-const_iterator.html#const_iterator
      """
      #  QDirListing::const_iterator::const_iterator()
      self._noteCreation(QDirListing.const_iterator, lambda: Rituals.call(
          'ritual_ZN11QDirListing14const_iteratorC1Ev',
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

  class sentinel(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QDirListing::sentinel: a plain Python object
    standing in front of one C++ QDirListing::sentinel.

    C++ hands a QDirListing::sentinel around as a copy, so every C++
    QDirListing::sentinel behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QDirListing::sentinel yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QDirListing::sentinel::~sentinel()': the destructor: Python
      removes its C++ QDirListing::sentinel by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QDirListing::sentinel is created at the first use, not by
      'QDirListing::sentinel(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QDirListing::sentinel back gives a copy the ritual
      made for Python, in a new cute QDirListing::sentinel.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QDirListing::sentinel'

    #  Qt's '~QDirListing::sentinel()'. Naming it makes this a value class:
    #  Python owns every C++ QDirListing::sentinel behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN11QDirListing8sentinelD1Ev'

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDirListing'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def iteratorPath(self) -> str:
    """
    Calls Qt's 'QString QDirListing::iteratorPath() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdirlisting.html#iteratorPath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDirListing::iteratorPath() const
    return self.uglySide.call('ritual_ZNK11QDirListing12iteratorPathEv')

  def iteratorFlags(self) -> IteratorFlags:
    """
    Calls Qt's 'IteratorFlags QDirListing::iteratorFlags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdirlisting.html#iteratorFlags

    Returns
    -------

    IteratorFlags
      The value standing for the combination Qt gave back.
    """
    #  IteratorFlags QDirListing::iteratorFlags() const
    return QDirListing.IteratorFlags(self.uglySide.call(
        'ritual_ZNK11QDirListing13iteratorFlagsEv',
    ))

  def end(self) -> sentinel:
    """
    Calls Qt's 'sentinel QDirListing::end() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdirlisting.html#end

    Returns
    -------

    sentinel
      A new cute QDirListing::sentinel around the copy Qt gave back. Python
      owns it.
    """
    #  sentinel QDirListing::end() const
    address = self.uglySide.call('ritual_ZNK11QDirListing3endEv')
    return QDirListing.sentinel._cuteOwning(address)

  def cend(self) -> sentinel:
    """
    Calls Qt's 'sentinel QDirListing::cend() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdirlisting.html#cend

    Returns
    -------

    sentinel
      A new cute QDirListing::sentinel around the copy Qt gave back. Python
      owns it.
    """
    #  sentinel QDirListing::cend() const
    address = self.uglySide.call('ritual_ZNK11QDirListing4cendEv')
    return QDirListing.sentinel._cuteOwning(address)

  def constEnd(self) -> sentinel:
    """
    Calls Qt's 'sentinel QDirListing::constEnd() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdirlisting.html#constEnd

    Returns
    -------

    sentinel
      A new cute QDirListing::sentinel around the copy Qt gave back. Python
      owns it.
    """
    #  sentinel QDirListing::constEnd() const
    address = self.uglySide.call('ritual_ZNK11QDirListing8constEndEv')
    return QDirListing.sentinel._cuteOwning(address)

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

  @overload(str)
  @overload(str, IteratorFlags)
  def __init__(
      self,
      path: str,
      flags: IteratorFlags = IteratorFlags.Default,
  ) -> None:
    """
    Notes what was given, for Qt's 'QDirListing::QDirListing(const QString
    &path, IteratorFlags flags)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdirlisting.html#QDirListing

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    flags : IteratorFlags
      Passed on as its number. May be left out, as in Qt: it is then
      IteratorFlags.Default.
    """
    #  QDirListing::QDirListing(const QString &path, IteratorFlags flags)
    self._noteCreation(QDirListing, lambda: Rituals.call(
        'ritual_ZN11QDirListingC1ERK7QString6QFlagsINS_12IteratorFlagEE',
        path, flags.value,
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
