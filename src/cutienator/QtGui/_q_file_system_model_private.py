"""
QFileSystemModelPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qfilesystemmodel_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QFileSystemModelPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QAbstractItemModelPrivate, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QDateTime, QFileInfo, QModelIndex, QTimeZone
  from . import QAbstractFileIconProvider, QExtendedInformation
  from . import QFileSystemModel, QIcon
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFileInfo = WAIT['QFileInfo']
  QModelIndex = WAIT['QModelIndex']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFileSystemModelPrivate(QAbstractItemModelPrivate):
  """
  The cute side of Qt's QFileSystemModelPrivate: a plain Python object
  standing in front of one C++ QFileSystemModelPrivate.

  It is built on the cute 'QAbstractItemModelPrivate', as Qt's
  QFileSystemModelPrivate is built on Qt's QAbstractItemModelPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QFileSystemModelPrivate that has a ritual and that
  Python can call so far, 26 names in all: 'q_func', 'init',
  'isHiddenByFilter', 'node', 'index', 'filtersAcceptsNode',
  'passNameFilters', 'removeNode', 'addNode', 'addVisibleFiles',
  'removeVisibleFile', 'sortChildren', 'translateVisibleLocation',
  'myComputer', 'delayedSort', 'icon', 'name', 'displayName', 'filePath',
  'size', 'type', 'time', 'directoryChanged', 'performDelayedSort',
  'resolvedName', 'rebuildNameFilterRegexps'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QFileSystemModel *QFileSystemModelPrivate::q_func() const':
    takes in Python what 'QFileSystemModel
    *QFileSystemModelPrivate::q_func()' takes.
  - Qt's 'QFileSystemModelPrivate::~QFileSystemModelPrivate()': the
    destructor: Python never removes a C++ QFileSystemModelPrivate.
  - Qt's 'void QFileSystemModelPrivate::fileSystemChanged(const QString
    &path, const QList<std::pair<QString, QFileInfo>> &a1)': takes a type
    Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QFileSystemModelPrivate is created at the first use, not by
    'QFileSystemModelPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QFileSystemModelPrivate.
  - Each name of Qt's QFileSystemModelPrivate that has no cute function yet,
    'fileSystemChanged', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The classes Qt writes inside QFileSystemModelPrivate, each a class in
  #  here as in C++.

  class Fetching(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QFileSystemModelPrivate::Fetching: a plain Python
    object standing in front of one C++ QFileSystemModelPrivate::Fetching.

    C++ hands a QFileSystemModelPrivate::Fetching around as a copy, so every
    C++ QFileSystemModelPrivate::Fetching behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QFileSystemModelPrivate::Fetching yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QFileSystemModelPrivate::Fetching::~Fetching()': the destructor:
      Python removes its C++ QFileSystemModelPrivate::Fetching by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ QFileSystemModelPrivate::Fetching is created at the first use,
      not by 'QFileSystemModelPrivate::Fetching(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QFileSystemModelPrivate::Fetching back gives a copy
      the ritual made for Python, in a new cute
      QFileSystemModelPrivate::Fetching.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QFileSystemModelPrivate::Fetching'

    #  Qt's '~QFileSystemModelPrivate::Fetching()'. Naming it makes this a
    #  value class: Python owns every C++ QFileSystemModelPrivate::Fetching
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN23QFileSystemModelPrivate8FetchingD1Ev'

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

  class QFileSystemNode(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QFileSystemModelPrivate::QFileSystemNode: a plain
    Python object standing in front of one C++
    QFileSystemModelPrivate::QFileSystemNode.

    What exists
    -----------

    Every function of Qt's QFileSystemModelPrivate::QFileSystemNode that has
    a ritual and that Python can call so far, 23 names in all: 'size',
    'type', 'lastModified', 'isReadable', 'isWritable', 'isExecutable',
    'isDir', 'fileInfo', 'isFile', 'isSystem', 'isHidden', 'isSymLink',
    'caseSensitive', 'icon', '__gt__', '__lt__', '__ne__', '__eq__',
    'hasInformation', 'populate', 'visibleLocation', 'updateIcon',
    'retranslateStrings'. It can be made from Python, in 1 way; see
    '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QFileSystemModelPrivate::QFileSystemNode::~QFileSystemNode()':
      the destructor: Python never removes a C++
      QFileSystemModelPrivate::QFileSystemNode.
    - Qt's 'QFile::Permissions
      QFileSystemModelPrivate::QFileSystemNode::permissions() const': gives a
      type Python has no way to take yet.
    - Qt's 'bool QFileSystemModelPrivate::QFileSystemNode::operator<(const
      QFileSystemNode &node) const': takes a type Python has no way to hand
      over yet.

    What has no ritual
    ------------------

    4 of the 32 functions Qt declares: 4 forbidden.

    What to expect
    --------------

    - The C++ QFileSystemModelPrivate::QFileSystemNode is created at the
      first use, not by 'QFileSystemModelPrivate::QFileSystemNode(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++ QFileSystemModelPrivate::QFileSystemNode.
    - Each name of Qt's QFileSystemModelPrivate::QFileSystemNode that has no
      cute function yet, 'permissions', holds a function that raises
      'NotImplementedError', and its docstring says why.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QAbstractFileIconProvider = WAIT['QAbstractFileIconProvider']
      QExtendedInformation = WAIT['QExtendedInformation']
      QTimeZone = WAIT['QTimeZone']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QFileSystemModelPrivate::QFileSystemNode'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def size(self) -> int:
      """
      Calls Qt's 'qint64 QFileSystemModelPrivate::QFileSystemNode::size()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qfilesystemmodelprivate-qfilesystemnode.html
      """
      #  qint64 QFileSystemModelPrivate::QFileSystemNode::size() const
      return self.uglySide.call(
          'ritual_ZNK23QFileSystemModelPrivate15QFileSystemNode4sizeEv',
      )

    def type(self) -> str:
      """
      Calls Qt's 'QString QFileSystemModelPrivate::QFileSystemNode::type()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qfilesystemmodelprivate-qfilesystemnode.html

      Returns
      -------

      str
        The text Qt gave back.
      """
      #  QString QFileSystemModelPrivate::QFileSystemNode::type() const
      return self.uglySide.call(
          'ritual_ZNK23QFileSystemModelPrivate15QFileSystemNode4typeEv',
      )

    @overload(QTimeZone)
    def lastModified(self, tz: QTimeZone) -> QDateTime:
      """
      Calls Qt's 'QDateTime
      QFileSystemModelPrivate::QFileSystemNode::lastModified(const QTimeZone
      &tz) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qfilesystemmodelprivate-qfilesystemnode.html

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
      #  QDateTime
      #      QFileSystemModelPrivate::QFileSystemNode::lastModified(const
      #      QTimeZone &tz) const
      address = self.uglySide.call(
          'ritual_ZNK23QFileSystemModelPrivate15QFileSystemNode12lastModifi'
          'edERK9QTimeZone',
          self._valueOf(tz),
      )
      from ..QtCore import QDateTime
      return QDateTime._cuteOwning(address)

    def isReadable(self) -> bool:
      """
      Calls Qt's 'bool QFileSystemModelPrivate::QFileSystemNode::isReadable()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qfilesystemmodelprivate-qfilesystemnode.html
      """
      #  bool QFileSystemModelPrivate::QFileSystemNode::isReadable() const
      return self.uglySide.call(
          'ritual_ZNK23QFileSystemModelPrivate15QFileSystemNode10isReadable'
          'Ev',
      )

    def isWritable(self) -> bool:
      """
      Calls Qt's 'bool QFileSystemModelPrivate::QFileSystemNode::isWritable()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qfilesystemmodelprivate-qfilesystemnode.html
      """
      #  bool QFileSystemModelPrivate::QFileSystemNode::isWritable() const
      return self.uglySide.call(
          'ritual_ZNK23QFileSystemModelPrivate15QFileSystemNode10isWritable'
          'Ev',
      )

    def isExecutable(self) -> bool:
      """
      Calls Qt's 'bool
      QFileSystemModelPrivate::QFileSystemNode::isExecutable() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qfilesystemmodelprivate-qfilesystemnode.html
      """
      #  bool QFileSystemModelPrivate::QFileSystemNode::isExecutable() const
      return self.uglySide.call(
          'ritual_ZNK23QFileSystemModelPrivate15QFileSystemNode12isExecutab'
          'leEv',
      )

    def isDir(self) -> bool:
      """
      Calls Qt's 'bool QFileSystemModelPrivate::QFileSystemNode::isDir()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qfilesystemmodelprivate-qfilesystemnode.html
      """
      #  bool QFileSystemModelPrivate::QFileSystemNode::isDir() const
      return self.uglySide.call(
          'ritual_ZNK23QFileSystemModelPrivate15QFileSystemNode5isDirEv',
      )

    def fileInfo(self) -> QFileInfo:
      """
      Calls Qt's 'QFileInfo
      QFileSystemModelPrivate::QFileSystemNode::fileInfo() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qfilesystemmodelprivate-qfilesystemnode.html

      Returns
      -------

      QFileInfo
        A new cute QFileInfo around the copy Qt gave back. Python owns it.
      """
      #  QFileInfo QFileSystemModelPrivate::QFileSystemNode::fileInfo() const
      address = self.uglySide.call(
          'ritual_ZNK23QFileSystemModelPrivate15QFileSystemNode8fileInfoEv',
      )
      from ..QtCore import QFileInfo
      return QFileInfo._cuteOwning(address)

    def isFile(self) -> bool:
      """
      Calls Qt's 'bool QFileSystemModelPrivate::QFileSystemNode::isFile()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qfilesystemmodelprivate-qfilesystemnode.html
      """
      #  bool QFileSystemModelPrivate::QFileSystemNode::isFile() const
      return self.uglySide.call(
          'ritual_ZNK23QFileSystemModelPrivate15QFileSystemNode6isFileEv',
      )

    def isSystem(self) -> bool:
      """
      Calls Qt's 'bool QFileSystemModelPrivate::QFileSystemNode::isSystem()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qfilesystemmodelprivate-qfilesystemnode.html
      """
      #  bool QFileSystemModelPrivate::QFileSystemNode::isSystem() const
      return self.uglySide.call(
          'ritual_ZNK23QFileSystemModelPrivate15QFileSystemNode8isSystemEv',
      )

    def isHidden(self) -> bool:
      """
      Calls Qt's 'bool QFileSystemModelPrivate::QFileSystemNode::isHidden()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qfilesystemmodelprivate-qfilesystemnode.html
      """
      #  bool QFileSystemModelPrivate::QFileSystemNode::isHidden() const
      return self.uglySide.call(
          'ritual_ZNK23QFileSystemModelPrivate15QFileSystemNode8isHiddenEv',
      )

    @overload()
    @overload(bool)
    def isSymLink(self, ignoreNtfsSymLinks: bool = False) -> bool:
      """
      Calls Qt's 'bool
      QFileSystemModelPrivate::QFileSystemNode::isSymLink(bool
      ignoreNtfsSymLinks) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qfilesystemmodelprivate-qfilesystemnode.html

      Parameters
      ----------

      ignoreNtfsSymLinks : bool
        Passed on as it is. May be left out, as in Qt: it is then False.
      """
      #  bool QFileSystemModelPrivate::QFileSystemNode::isSymLink(bool
      #      ignoreNtfsSymLinks) const
      return self.uglySide.call(
          'ritual_ZNK23QFileSystemModelPrivate15QFileSystemNode9isSymLinkEb',
          ignoreNtfsSymLinks,
      )

    def caseSensitive(self) -> bool:
      """
      Calls Qt's 'bool
      QFileSystemModelPrivate::QFileSystemNode::caseSensitive() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qfilesystemmodelprivate-qfilesystemnode.html
      """
      #  bool QFileSystemModelPrivate::QFileSystemNode::caseSensitive() const
      return self.uglySide.call(
          'ritual_ZNK23QFileSystemModelPrivate15QFileSystemNode13caseSensit'
          'iveEv',
      )

    def icon(self) -> QIcon:
      """
      Calls Qt's 'QIcon QFileSystemModelPrivate::QFileSystemNode::icon()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qfilesystemmodelprivate-qfilesystemnode.html

      Returns
      -------

      QIcon
        A new cute QIcon around the copy Qt gave back. Python owns it.
      """
      #  QIcon QFileSystemModelPrivate::QFileSystemNode::icon() const
      address = self.uglySide.call(
          'ritual_ZNK23QFileSystemModelPrivate15QFileSystemNode4iconEv',
      )
      from . import QIcon
      return QIcon._cuteOwning(address)

    def hasInformation(self) -> bool:
      """
      Calls Qt's 'bool
      QFileSystemModelPrivate::QFileSystemNode::hasInformation() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qfilesystemmodelprivate-qfilesystemnode.html
      """
      #  bool QFileSystemModelPrivate::QFileSystemNode::hasInformation()
      #      const
      return self.uglySide.call(
          'ritual_ZNK23QFileSystemModelPrivate15QFileSystemNode14hasInforma'
          'tionEv',
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(str)
    def __gt__(self, name: str) -> bool:
      """
      Calls Qt's 'bool
      QFileSystemModelPrivate::QFileSystemNode::operator>(const QString
      &name) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qfilesystemmodelprivate-qfilesystemnode.html

      Parameters
      ----------

      name : str
        Passed on as it is: a QString is made of it for the call.
      """
      #  bool QFileSystemModelPrivate::QFileSystemNode::operator>(const
      #      QString &name) const
      return self.uglySide.call(
          'ritual_ZNK23QFileSystemModelPrivate15QFileSystemNodegtERK7QStrin'
          'g',
          name,
      )

    @overload.fallback
    def __gt__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    @overload(str)
    def __lt__(self, name: str) -> bool:
      """
      Calls Qt's 'bool
      QFileSystemModelPrivate::QFileSystemNode::operator<(const QString
      &name) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qfilesystemmodelprivate-qfilesystemnode.html

      Parameters
      ----------

      name : str
        Passed on as it is: a QString is made of it for the call.
      """
      #  bool QFileSystemModelPrivate::QFileSystemNode::operator<(const
      #      QString &name) const
      return self.uglySide.call(
          'ritual_ZNK23QFileSystemModelPrivate15QFileSystemNodeltERK7QStrin'
          'g',
          name,
      )

    @overload.fallback
    def __lt__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    @overload(QExtendedInformation)
    def __ne__(self, fileInfo: QExtendedInformation) -> bool:
      """
      Calls Qt's 'bool
      QFileSystemModelPrivate::QFileSystemNode::operator!=(const
      QExtendedInformation &fileInfo) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qfilesystemmodelprivate-qfilesystemnode.html

      Parameters
      ----------

      fileInfo : QExtendedInformation
        Passed on as a value: Qt reads the C++ QExtendedInformation, which
        stays Python's own.
      """
      #  bool QFileSystemModelPrivate::QFileSystemNode::operator!=(const
      #      QExtendedInformation &fileInfo) const
      return self.uglySide.call(
          'ritual_ZNK23QFileSystemModelPrivate15QFileSystemNodeneERK20QExte'
          'ndedInformation',
          self._valueOf(fileInfo),
      )

    @overload.fallback
    def __ne__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    @overload(str)
    def __eq__(self, name: str) -> bool:
      """
      Calls Qt's 'bool
      QFileSystemModelPrivate::QFileSystemNode::operator==(const QString
      &name) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qfilesystemmodelprivate-qfilesystemnode.html

      Parameters
      ----------

      name : str
        Passed on as it is: a QString is made of it for the call.
      """
      #  bool QFileSystemModelPrivate::QFileSystemNode::operator==(const
      #      QString &name) const
      return self.uglySide.call(
          'ritual_ZNK23QFileSystemModelPrivate15QFileSystemNodeeqERK7QStrin'
          'g',
          name,
      )

    @overload(QExtendedInformation)
    def __eq__(self, fileInfo: QExtendedInformation) -> bool:
      """
      Calls Qt's 'bool
      QFileSystemModelPrivate::QFileSystemNode::operator==(const
      QExtendedInformation &fileInfo) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qfilesystemmodelprivate-qfilesystemnode.html

      Parameters
      ----------

      fileInfo : QExtendedInformation
        Passed on as a value: Qt reads the C++ QExtendedInformation, which
        stays Python's own.
      """
      #  bool QFileSystemModelPrivate::QFileSystemNode::operator==(const
      #      QExtendedInformation &fileInfo) const
      return self.uglySide.call(
          'ritual_ZNK23QFileSystemModelPrivate15QFileSystemNodeeqERK20QExte'
          'ndedInformation',
          self._valueOf(fileInfo),
      )

    @overload.fallback
    def __eq__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    @overload(str)
    @overload(str, THIS)
    @overload(str, NoneType)
    def __init__(
        self,
        filename: str = '',
        p: Optional[QFileSystemModelPrivate.QFileSystemNode] = None,
    ) -> None:
      """
      Notes what was given, for Qt's
      'QFileSystemModelPrivate::QFileSystemNode::QFileSystemNode(const
      QString &filename, QFileSystemNode *p)', which is called at the first
      use.

      Qt's own words:
      https://doc.qt.io/qt-6/qfilesystemmodelprivate-qfilesystemnode.html

      Parameters
      ----------

      filename : str
        Passed on as it is: a QString is made of it for the call. May be left
        out, as in Qt: it is then ''.

      p : Optional[QFileSystemModelPrivate.QFileSystemNode]
        Passed on as the address of its C++ object. None is passed on as no
        object. May be left out, as in Qt: it is then None.
      """
      #  QFileSystemModelPrivate::QFileSystemNode::QFileSystemNode(const
      #      QString &filename, QFileSystemNode *p)
      self._noteCreation(
          QFileSystemModelPrivate.QFileSystemNode, lambda: Rituals.call(
              'ritual_ZN23QFileSystemModelPrivate15QFileSystemNodeC1ERK7QSt'
              'ringPS0_',
              filename, self._addressOf(p),
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

    @overload(QExtendedInformation)
    def populate(self, fileInfo: QExtendedInformation) -> None:
      """
      Calls Qt's 'void
      QFileSystemModelPrivate::QFileSystemNode::populate(const
      QExtendedInformation &fileInfo)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qfilesystemmodelprivate-qfilesystemnode.html

      Parameters
      ----------

      fileInfo : QExtendedInformation
        Passed on as a value: Qt reads the C++ QExtendedInformation, which
        stays Python's own.
      """
      #  void QFileSystemModelPrivate::QFileSystemNode::populate(const
      #      QExtendedInformation &fileInfo)
      self.uglySide.call(
          'ritual_ZN23QFileSystemModelPrivate15QFileSystemNode8populateERK2'
          '0QExtendedInformation',
          self._valueOf(fileInfo),
      )

    @overload(str)
    def visibleLocation(self, childName: str) -> int:
      """
      Calls Qt's 'int
      QFileSystemModelPrivate::QFileSystemNode::visibleLocation(const QString
      &childName)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qfilesystemmodelprivate-qfilesystemnode.html

      Parameters
      ----------

      childName : str
        Passed on as it is: a QString is made of it for the call.
      """
      #  int QFileSystemModelPrivate::QFileSystemNode::visibleLocation(const
      #      QString &childName)
      return self.uglySide.call(
          'ritual_ZN23QFileSystemModelPrivate15QFileSystemNode15visibleLoca'
          'tionERK7QString',
          childName,
      )

    @overload(QAbstractFileIconProvider, str)
    @overload(NoneType, str)
    def updateIcon(
        self,
        iconProvider: Optional[QAbstractFileIconProvider],
        path: str,
    ) -> None:
      """
      Calls Qt's 'void QFileSystemModelPrivate::QFileSystemNode::updateIcon(
      QAbstractFileIconProvider *iconProvider, const QString &path)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qfilesystemmodelprivate-qfilesystemnode.html

      Parameters
      ----------

      iconProvider : Optional[QAbstractFileIconProvider]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      path : str
        Passed on as it is: a QString is made of it for the call.
      """
      #  void QFileSystemModelPrivate::QFileSystemNode::updateIcon(
      #      QAbstractFileIconProvider *iconProvider, const QString &path)
      self.uglySide.call(
          'ritual_ZN23QFileSystemModelPrivate15QFileSystemNode10updateIconE'
          'P25QAbstractFileIconProviderRK7QString',
          self._addressOf(iconProvider), path,
      )

    @overload(QAbstractFileIconProvider, str)
    @overload(NoneType, str)
    def retranslateStrings(
        self,
        iconProvider: Optional[QAbstractFileIconProvider],
        path: str,
    ) -> None:
      """
      Calls Qt's 'void
      QFileSystemModelPrivate::QFileSystemNode::retranslateStrings(
      QAbstractFileIconProvider *iconProvider, const QString &path)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qfilesystemmodelprivate-qfilesystemnode.html

      Parameters
      ----------

      iconProvider : Optional[QAbstractFileIconProvider]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      path : str
        Passed on as it is: a QString is made of it for the call.
      """
      #  void QFileSystemModelPrivate::QFileSystemNode::retranslateStrings(
      #      QAbstractFileIconProvider *iconProvider, const QString &path)
      self.uglySide.call(
          'ritual_ZN23QFileSystemModelPrivate15QFileSystemNode18retranslate'
          'StringsEP25QAbstractFileIconProviderRK7QString',
          self._addressOf(iconProvider), path,
      )

    @staticmethod
    def permissions(*__, **_) -> Never:
      """
      Qt's 'QFile::Permissions
      QFileSystemModelPrivate::QFileSystemNode::permissions() const': gives a
      type Python has no way to take yet.
      """
      raise NotImplementedError(
          "'QFileSystemModelPrivate.QFileSystemNode.permissions' has no "
          "cute function yet. Qt's 'QFile::Permissions "
          "QFileSystemModelPrivate::QFileSystemNode::permissions() const': "
          "gives a type Python has no way to take yet.")

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def myComputer() -> str:
    """
    Calls Qt's 'QString QFileSystemModelPrivate::myComputer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemmodelprivate.html#myComputer

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileSystemModelPrivate::myComputer()
    return Rituals.call('ritual_ZN23QFileSystemModelPrivate10myComputerEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFileSystemModelPrivate'

  #  A C++ QFileSystemModelPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QFileSystemModelPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QFileSystemNode, QModelIndex)
  @overload(NoneType, QModelIndex)
  def isHiddenByFilter(
      self,
      indexNode: Optional[QFileSystemNode],
      index: QModelIndex,
  ) -> bool:
    """
    Calls Qt's 'bool
    QFileSystemModelPrivate::isHiddenByFilter(QFileSystemNode *indexNode,
    const QModelIndex &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemmodelprivate.html#isHiddenByFilter

    Parameters
    ----------

    indexNode : Optional[QFileSystemNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QFileSystemModelPrivate::isHiddenByFilter(QFileSystemNode
    #      *indexNode, const QModelIndex &index) const
    return self.uglySide.call(
        'ritual_ZNK23QFileSystemModelPrivate16isHiddenByFilterEPNS_15QFileS'
        'ystemNodeERK11QModelIndex',
        self._addressOf(indexNode), self._valueOf(index),
    )

  @overload(QModelIndex)
  def node(self, index: QModelIndex) -> Optional[QFileSystemNode]:
    """
    Calls Qt's 'QFileSystemNode *QFileSystemModelPrivate::node(const
    QModelIndex &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodelprivate.html#node

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    Optional[QFileSystemNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFileSystemNode *QFileSystemModelPrivate::node(const QModelIndex
    #      &index) const
    address = self.uglySide.call(
        'ritual_ZNK23QFileSystemModelPrivate4nodeERK11QModelIndex',
        self._valueOf(index),
    )
    return QFileSystemModelPrivate.QFileSystemNode._cuteAt(address)

  @overload(str)
  @overload(str, bool)
  def node(self, path: str, fetch: bool = True) -> Optional[QFileSystemNode]:
    """
    Calls Qt's 'QFileSystemNode *QFileSystemModelPrivate::node(const QString
    &path, bool fetch) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodelprivate.html#node

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    fetch : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    Returns
    -------

    Optional[QFileSystemNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFileSystemNode *QFileSystemModelPrivate::node(const QString &path,
    #      bool fetch) const
    address = self.uglySide.call(
        'ritual_ZNK23QFileSystemModelPrivate4nodeERK7QStringb', path, fetch,
    )
    return QFileSystemModelPrivate.QFileSystemNode._cuteAt(address)

  @overload(QFileSystemNode)
  @overload(NoneType)
  def filtersAcceptsNode(self, node: Optional[QFileSystemNode]) -> bool:
    """
    Calls Qt's 'bool QFileSystemModelPrivate::filtersAcceptsNode(const
    QFileSystemNode *node) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemmodelprivate.html#filtersAcceptsNode

    Parameters
    ----------

    node : Optional[QFileSystemNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QFileSystemModelPrivate::filtersAcceptsNode(const QFileSystemNode
    #      *node) const
    return self.uglySide.call(
        'ritual_ZNK23QFileSystemModelPrivate18filtersAcceptsNodeEPKNS_15QFi'
        'leSystemNodeE',
        self._addressOf(node),
    )

  @overload(QFileSystemNode)
  @overload(NoneType)
  def passNameFilters(self, node: Optional[QFileSystemNode]) -> bool:
    """
    Calls Qt's 'bool QFileSystemModelPrivate::passNameFilters(const
    QFileSystemNode *node) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemmodelprivate.html#passNameFilters

    Parameters
    ----------

    node : Optional[QFileSystemNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QFileSystemModelPrivate::passNameFilters(const QFileSystemNode
    #      *node) const
    return self.uglySide.call(
        'ritual_ZNK23QFileSystemModelPrivate15passNameFiltersEPKNS_15QFileS'
        'ystemNodeE',
        self._addressOf(node),
    )

  @overload(QFileSystemNode, int)
  @overload(NoneType, int)
  def translateVisibleLocation(
      self,
      parent: Optional[QFileSystemNode],
      row: int,
  ) -> int:
    """
    Calls Qt's 'int
    QFileSystemModelPrivate::translateVisibleLocation(QFileSystemNode
    *parent, int row) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemmodelprivate.html

    Parameters
    ----------

    parent : Optional[QFileSystemNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    row : int
      Passed on as it is.
    """
    #  int QFileSystemModelPrivate::translateVisibleLocation(QFileSystemNode
    #      *parent, int row) const
    return self.uglySide.call(
        'ritual_ZNK23QFileSystemModelPrivate24translateVisibleLocationEPNS_'
        '15QFileSystemNodeEi',
        self._addressOf(parent), row,
    )

  @overload(QModelIndex)
  def icon(self, index: QModelIndex) -> QIcon:
    """
    Calls Qt's 'QIcon QFileSystemModelPrivate::icon(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodelprivate.html#icon

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QFileSystemModelPrivate::icon(const QModelIndex &index) const
    address = self.uglySide.call(
        'ritual_ZNK23QFileSystemModelPrivate4iconERK11QModelIndex',
        self._valueOf(index),
    )
    from . import QIcon
    return QIcon._cuteOwning(address)

  @overload(QModelIndex)
  def name(self, index: QModelIndex) -> str:
    """
    Calls Qt's 'QString QFileSystemModelPrivate::name(const QModelIndex
    &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodelprivate.html#name

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileSystemModelPrivate::name(const QModelIndex &index) const
    return self.uglySide.call(
        'ritual_ZNK23QFileSystemModelPrivate4nameERK11QModelIndex',
        self._valueOf(index),
    )

  @overload(QModelIndex)
  def displayName(self, index: QModelIndex) -> str:
    """
    Calls Qt's 'QString QFileSystemModelPrivate::displayName(const
    QModelIndex &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemmodelprivate.html#displayName

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileSystemModelPrivate::displayName(const QModelIndex &index)
    #      const
    return self.uglySide.call(
        'ritual_ZNK23QFileSystemModelPrivate11displayNameERK11QModelIndex',
        self._valueOf(index),
    )

  @overload(QModelIndex)
  def filePath(self, index: QModelIndex) -> str:
    """
    Calls Qt's 'QString QFileSystemModelPrivate::filePath(const QModelIndex
    &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemmodelprivate.html#filePath

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileSystemModelPrivate::filePath(const QModelIndex &index)
    #      const
    return self.uglySide.call(
        'ritual_ZNK23QFileSystemModelPrivate8filePathERK11QModelIndex',
        self._valueOf(index),
    )

  @overload(QModelIndex)
  def size(self, index: QModelIndex) -> str:
    """
    Calls Qt's 'QString QFileSystemModelPrivate::size(const QModelIndex
    &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodelprivate.html#size

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileSystemModelPrivate::size(const QModelIndex &index) const
    return self.uglySide.call(
        'ritual_ZNK23QFileSystemModelPrivate4sizeERK11QModelIndex',
        self._valueOf(index),
    )

  @staticmethod
  @overload(int)
  def size(bytes: int) -> str:
    """
    Calls Qt's 'QString QFileSystemModelPrivate::size(qint64 bytes)'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodelprivate.html#size

    Parameters
    ----------

    bytes : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileSystemModelPrivate::size(qint64 bytes)
    return Rituals.call('ritual_ZN23QFileSystemModelPrivate4sizeEx', bytes)

  @overload(QModelIndex)
  def type(self, index: QModelIndex) -> str:
    """
    Calls Qt's 'QString QFileSystemModelPrivate::type(const QModelIndex
    &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodelprivate.html#type

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileSystemModelPrivate::type(const QModelIndex &index) const
    return self.uglySide.call(
        'ritual_ZNK23QFileSystemModelPrivate4typeERK11QModelIndex',
        self._valueOf(index),
    )

  @overload(QModelIndex)
  def time(self, index: QModelIndex) -> str:
    """
    Calls Qt's 'QString QFileSystemModelPrivate::time(const QModelIndex
    &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodelprivate.html#time

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileSystemModelPrivate::time(const QModelIndex &index) const
    return self.uglySide.call(
        'ritual_ZNK23QFileSystemModelPrivate4timeERK11QModelIndex',
        self._valueOf(index),
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QFileSystemModelPrivate::QFileSystemModelPrivate()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemmodelprivate.html
    """
    #  QFileSystemModelPrivate::QFileSystemModelPrivate()
    self._noteCreation(QFileSystemModelPrivate, lambda: Rituals.call(
        'ritual_ZN23QFileSystemModelPrivateC1Ev',
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

  def q_func(self) -> Optional[QFileSystemModel]:
    """
    Calls Qt's 'QFileSystemModel *QFileSystemModelPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemmodelprivate.html#q_func

    Returns
    -------

    Optional[QFileSystemModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFileSystemModel *QFileSystemModelPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN23QFileSystemModelPrivate6q_funcEv',
    )
    from . import QFileSystemModel
    return QFileSystemModel._cuteAt(address)

  def init(self) -> None:
    """
    Calls Qt's 'void QFileSystemModelPrivate::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodelprivate.html#init
    """
    #  void QFileSystemModelPrivate::init()
    self.uglySide.call('ritual_ZN23QFileSystemModelPrivate4initEv')

  @overload(str)
  @overload(str, int)
  def index(self, path: str, column: int = 0) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QFileSystemModelPrivate::index(const QString
    &path, int column)'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodelprivate.html#index

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    column : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QFileSystemModelPrivate::index(const QString &path, int
    #      column)
    address = self.uglySide.call(
        'ritual_ZN23QFileSystemModelPrivate5indexERK7QStringi', path, column,
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QFileSystemNode)
  @overload(NoneType)
  @overload(QFileSystemNode, int)
  @overload(NoneType, int)
  def index(
      self,
      node: Optional[QFileSystemNode],
      column: int = 0,
  ) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QFileSystemModelPrivate::index(const
    QFileSystemNode *node, int column) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmodelprivate.html#index

    Parameters
    ----------

    node : Optional[QFileSystemNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    column : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QFileSystemModelPrivate::index(const QFileSystemNode
    #      *node, int column) const
    address = self.uglySide.call(
        'ritual_ZNK23QFileSystemModelPrivate5indexEPKNS_15QFileSystemNodeEi',
        self._addressOf(node), column,
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QFileSystemNode, str)
  @overload(NoneType, str)
  def removeNode(
      self,
      parentNode: Optional[QFileSystemNode],
      name: str,
  ) -> None:
    """
    Calls Qt's 'void QFileSystemModelPrivate::removeNode(QFileSystemNode
    *parentNode, const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemmodelprivate.html#removeNode

    Parameters
    ----------

    parentNode : Optional[QFileSystemNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QFileSystemModelPrivate::removeNode(QFileSystemNode *parentNode,
    #      const QString &name)
    self.uglySide.call(
        'ritual_ZN23QFileSystemModelPrivate10removeNodeEPNS_15QFileSystemNo'
        'deERK7QString',
        self._addressOf(parentNode), name,
    )

  @overload(QFileSystemNode, str, QFileInfo)
  @overload(NoneType, str, QFileInfo)
  def addNode(
      self,
      parentNode: Optional[QFileSystemNode],
      fileName: str,
      info: QFileInfo,
  ) -> Optional[QFileSystemNode]:
    """
    Calls Qt's 'QFileSystemNode
    *QFileSystemModelPrivate::addNode(QFileSystemNode *parentNode, const
    QString &fileName, const QFileInfo &info)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemmodelprivate.html#addNode

    Parameters
    ----------

    parentNode : Optional[QFileSystemNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    info : QFileInfo
      Passed on as a value: Qt reads the C++ QFileInfo, which stays Python's
      own.

    Returns
    -------

    Optional[QFileSystemNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFileSystemNode *QFileSystemModelPrivate::addNode(QFileSystemNode
    #      *parentNode, const QString &fileName, const QFileInfo &info)
    address = self.uglySide.call(
        'ritual_ZN23QFileSystemModelPrivate7addNodeEPNS_15QFileSystemNodeER'
        'K7QStringRK9QFileInfo',
        self._addressOf(parentNode), fileName, self._valueOf(info),
    )
    return QFileSystemModelPrivate.QFileSystemNode._cuteAt(address)

  @overload(QFileSystemNode, QStringList)
  @overload(NoneType, QStringList)
  def addVisibleFiles(
      self,
      parentNode: Optional[QFileSystemNode],
      newFiles: QStringList,
  ) -> None:
    """
    Calls Qt's 'void QFileSystemModelPrivate::addVisibleFiles(QFileSystemNode
    *parentNode, const QStringList &newFiles)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemmodelprivate.html#addVisibleFiles

    Parameters
    ----------

    parentNode : Optional[QFileSystemNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    newFiles : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QFileSystemModelPrivate::addVisibleFiles(QFileSystemNode
    #      *parentNode, const QStringList &newFiles)
    self.uglySide.call(
        'ritual_ZN23QFileSystemModelPrivate15addVisibleFilesEPNS_15QFileSys'
        'temNodeERK5QListI7QStringE',
        self._addressOf(parentNode), self._valueOf(newFiles),
    )

  @overload(QFileSystemNode, int)
  @overload(NoneType, int)
  def removeVisibleFile(
      self,
      parentNode: Optional[QFileSystemNode],
      visibleLocation: int,
  ) -> None:
    """
    Calls Qt's 'void
    QFileSystemModelPrivate::removeVisibleFile(QFileSystemNode *parentNode,
    int visibleLocation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemmodelprivate.html#removeVisibleFile

    Parameters
    ----------

    parentNode : Optional[QFileSystemNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    visibleLocation : int
      Passed on as it is.
    """
    #  void QFileSystemModelPrivate::removeVisibleFile(QFileSystemNode
    #      *parentNode, int visibleLocation)
    self.uglySide.call(
        'ritual_ZN23QFileSystemModelPrivate17removeVisibleFileEPNS_15QFileS'
        'ystemNodeEi',
        self._addressOf(parentNode), visibleLocation,
    )

  @overload(int, QModelIndex)
  def sortChildren(self, column: int, parent: QModelIndex) -> None:
    """
    Calls Qt's 'void QFileSystemModelPrivate::sortChildren(int column, const
    QModelIndex &parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemmodelprivate.html#sortChildren

    Parameters
    ----------

    column : int
      Passed on as it is.

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QFileSystemModelPrivate::sortChildren(int column, const
    #      QModelIndex &parent)
    self.uglySide.call(
        'ritual_ZN23QFileSystemModelPrivate12sortChildrenEiRK11QModelIndex',
        column, self._valueOf(parent),
    )

  def delayedSort(self) -> None:
    """
    Calls Qt's 'void QFileSystemModelPrivate::delayedSort()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemmodelprivate.html#delayedSort
    """
    #  void QFileSystemModelPrivate::delayedSort()
    self.uglySide.call('ritual_ZN23QFileSystemModelPrivate11delayedSortEv')

  @overload(str, QStringList)
  def directoryChanged(self, directory: str, list: QStringList) -> None:
    """
    Calls Qt's 'void QFileSystemModelPrivate::directoryChanged(const QString
    &directory, const QStringList &list)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemmodelprivate.html#directoryChanged

    Parameters
    ----------

    directory : str
      Passed on as it is: a QString is made of it for the call.

    list : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QFileSystemModelPrivate::directoryChanged(const QString
    #      &directory, const QStringList &list)
    self.uglySide.call(
        'ritual_ZN23QFileSystemModelPrivate16directoryChangedERK7QStringRK5'
        'QListIS0_E',
        directory, self._valueOf(list),
    )

  def performDelayedSort(self) -> None:
    """
    Calls Qt's 'void QFileSystemModelPrivate::performDelayedSort()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemmodelprivate.html#performDelayedSort
    """
    #  void QFileSystemModelPrivate::performDelayedSort()
    self.uglySide.call(
        'ritual_ZN23QFileSystemModelPrivate18performDelayedSortEv',
    )

  @overload(str, str)
  def resolvedName(self, fileName: str, resolvedName: str) -> None:
    """
    Calls Qt's 'void QFileSystemModelPrivate::resolvedName(const QString
    &fileName, const QString &resolvedName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemmodelprivate.html#resolvedName

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    resolvedName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QFileSystemModelPrivate::resolvedName(const QString &fileName,
    #      const QString &resolvedName)
    self.uglySide.call(
        'ritual_ZN23QFileSystemModelPrivate12resolvedNameERK7QStringS2_',
        fileName, resolvedName,
    )

  def rebuildNameFilterRegexps(self) -> None:
    """
    Calls Qt's 'void QFileSystemModelPrivate::rebuildNameFilterRegexps()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemmodelprivate.html
    """
    #  void QFileSystemModelPrivate::rebuildNameFilterRegexps()
    self.uglySide.call(
        'ritual_ZN23QFileSystemModelPrivate24rebuildNameFilterRegexpsEv',
    )

  @staticmethod
  def fileSystemChanged(*__, **_) -> Never:
    """
    Qt's 'void QFileSystemModelPrivate::fileSystemChanged(const QString
    &path, const QList<std::pair<QString, QFileInfo>> &a1)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QFileSystemModelPrivate.fileSystemChanged' has no cute function "
        "yet. Qt's 'void QFileSystemModelPrivate::fileSystemChanged(const "
        "QString &path, const QList<std::pair<QString, QFileInfo>> &a1)': "
        "takes a type Python has no way to hand over yet.")
