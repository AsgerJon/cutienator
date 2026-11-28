"""
FileInfoThread binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsFolderListModel/6.12.0/QtLabsFolderListModel/private/fileinfothread_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means FileInfoThread to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class FileInfoThread(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's FileInfoThread: a plain Python object standing in
  front of one C++ FileInfoThread.

  What exists
  -----------

  Every function of Qt's FileInfoThread that has a ritual and that Python can
  call so far, 6 names in all: 'metaObject', 'clear', 'removePath',
  'dirChanged', 'updateFile', 'run'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *FileInfoThread::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int FileInfoThread::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'FileInfoThread::~FileInfoThread()': the destructor: Python never
    removes a C++ FileInfoThread.
  - Qt's 'void FileInfoThread::findChangeRange(const QList<FileProperty>
    &list, int &fromIndex, int &toIndex)': takes a number to change where it
    is.

  What has no ritual
  ------------------

  26 of the 36 functions Qt declares: 15 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 4 the
  compiler refuses its ritual as it would be written here; 3 leans on
  'FileInfoThread; 2 not a gap; 2 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ FileInfoThread is created at the first use, not by
    'FileInfoThread(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ FileInfoThread.
  - Qt tells when it has removed the C++ FileInfoThread. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's FileInfoThread that has no cute function yet,
    '__init__', 'directoryChanged', 'directoryUpdated', 'findChangeRange',
    'getFileInfos', 'initiateScan', 'runOnce', 'setCaseSensitive',
    'setNameFilters', 'setPath', 'setRootPath', 'setShowDirs',
    'setShowDirsFirst', 'setShowDot', 'setShowDotAndDotDot', 'setShowDotDot',
    'setShowFiles', 'setShowHidden', 'setShowOnlyReadable', 'setSortFlags',
    'sortFinished', 'statusChanged', holds a function that raises
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
  __qt_class__ = 'FileInfoThread'

  #  A C++ FileInfoThread Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_FileInfoThread'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *FileInfoThread::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/fileinfothread.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *FileInfoThread::metaObject() const
    address = self.uglySide.call('ritual_ZNK14FileInfoThread10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
    Qt's 'FileInfoThread::FileInfoThread(QObject *parent)': leans on
    'FileInfoThread::qt_metacall(QMetaObject::Call, int, void**)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'FileInfoThread.__init__' has no cute function yet. Qt's "
        "'FileInfoThread::FileInfoThread(QObject *parent)': leans on "
        "'FileInfoThread::qt_metacall(QMetaObject::Call, int, void**)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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
    Calls Qt's 'void FileInfoThread::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/fileinfothread.html#clear
    """
    #  void FileInfoThread::clear()
    self.uglySide.call('ritual_ZN14FileInfoThread5clearEv')

  @overload(str)
  def removePath(self, path: str) -> None:
    """
    Calls Qt's 'void FileInfoThread::removePath(const QString &path)'.

    Qt's own words: https://doc.qt.io/qt-6/fileinfothread.html#removePath

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void FileInfoThread::removePath(const QString &path)
    self.uglySide.call(
        'ritual_ZN14FileInfoThread10removePathERK7QString', path,
    )

  @overload(str)
  def dirChanged(self, directoryPath: str) -> None:
    """
    Calls Qt's 'void FileInfoThread::dirChanged(const QString
    &directoryPath)'.

    Qt's own words: https://doc.qt.io/qt-6/fileinfothread.html#dirChanged

    Parameters
    ----------

    directoryPath : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void FileInfoThread::dirChanged(const QString &directoryPath)
    self.uglySide.call(
        'ritual_ZN14FileInfoThread10dirChangedERK7QString', directoryPath,
    )

  @overload(str)
  def updateFile(self, path: str) -> None:
    """
    Calls Qt's 'void FileInfoThread::updateFile(const QString &path)'.

    Qt's own words: https://doc.qt.io/qt-6/fileinfothread.html#updateFile

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void FileInfoThread::updateFile(const QString &path)
    self.uglySide.call(
        'ritual_ZN14FileInfoThread10updateFileERK7QString', path,
    )

  def run(self) -> None:
    """
    Calls Qt's 'void FileInfoThread::run()'.

    Qt's own words: https://doc.qt.io/qt-6/fileinfothread.html#run
    """
    #  void FileInfoThread::run()
    self.uglySide.call('ritual_ZN14FileInfoThread3runEv')

  @staticmethod
  def directoryChanged(*__, **_) -> Never:
    """
    Qt's 'void FileInfoThread::directoryChanged(const QString &directory,
    const QList<FileProperty> &list) const': the compiler refuses its ritual
    as it would be written here: static_cast from 'const FileInfoThread *' to
    'QObject *', which are not related by inheritance, is not allowed.
    """
    raise NotImplementedError(
        "'FileInfoThread.directoryChanged' has no cute function yet. Qt's "
        "'void FileInfoThread::directoryChanged(const QString &directory, "
        "const QList<FileProperty> &list) const': the compiler refuses its "
        "ritual as it would be written here: static_cast from 'const "
        "FileInfoThread *' to 'QObject *', which are not related by "
        "inheritance, is not allowed.")

  @staticmethod
  def directoryUpdated(*__, **_) -> Never:
    """
    Qt's 'void FileInfoThread::directoryUpdated(const QString &directory,
    const QList<FileProperty> &list, int fromIndex, int toIndex) const': the
    compiler refuses its ritual as it would be written here: static_cast from
    'const FileInfoThread *' to 'QObject *', which are not related by
    inheritance, is not allowed.
    """
    raise NotImplementedError(
        "'FileInfoThread.directoryUpdated' has no cute function yet. Qt's "
        "'void FileInfoThread::directoryUpdated(const QString &directory, "
        "const QList<FileProperty> &list, int fromIndex, int toIndex) "
        "const': the compiler refuses its ritual as it would be written "
        "here: static_cast from 'const FileInfoThread *' to 'QObject *', "
        "which are not related by inheritance, is not allowed.")

  @staticmethod
  def findChangeRange(*__, **_) -> Never:
    """
    Qt's 'void FileInfoThread::findChangeRange(const QList<FileProperty>
    &list, int &fromIndex, int &toIndex)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'FileInfoThread.findChangeRange' has no cute function yet. Qt's "
        "'void FileInfoThread::findChangeRange(const QList<FileProperty> "
        "&list, int &fromIndex, int &toIndex)': takes a number to change "
        "where it is.")

  @staticmethod
  def getFileInfos(*__, **_) -> Never:
    """
    Qt's 'void FileInfoThread::getFileInfos(const QString &path)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: unknown type name 'lcFileInfoThread'; did you mean
    'FileInfoThread'?.
    """
    raise NotImplementedError(
        "'FileInfoThread.getFileInfos' has no cute function yet. Qt's 'void "
        "FileInfoThread::getFileInfos(const QString &path)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: unknown type name 'lcFileInfoThread'; did you "
        "mean 'FileInfoThread'?.")

  @staticmethod
  def initiateScan(*__, **_) -> Never:
    """
    Qt's 'void FileInfoThread::initiateScan()': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file:
    unknown type name 'lcFileInfoThread'; did you mean 'FileInfoThread'?.
    """
    raise NotImplementedError(
        "'FileInfoThread.initiateScan' has no cute function yet. Qt's 'void "
        "FileInfoThread::initiateScan()': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "unknown type name 'lcFileInfoThread'; did you mean "
        "'FileInfoThread'?.")

  @staticmethod
  def runOnce(*__, **_) -> Never:
    """
    Qt's 'void FileInfoThread::runOnce()': leans on
    'FileInfoThread::statusChanged(QQuickFolderListModel::Status) const',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'FileInfoThread.runOnce' has no cute function yet. Qt's 'void "
        "FileInfoThread::runOnce()': leans on "
        "'FileInfoThread::statusChanged(QQuickFolderListModel::Status) "
        "const', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def setCaseSensitive(*__, **_) -> Never:
    """
    Qt's 'void FileInfoThread::setCaseSensitive(bool on)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: unknown type name 'lcFileInfoThread'; did you mean
    'FileInfoThread'?.
    """
    raise NotImplementedError(
        "'FileInfoThread.setCaseSensitive' has no cute function yet. Qt's "
        "'void FileInfoThread::setCaseSensitive(bool on)': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: unknown type name 'lcFileInfoThread'; did you mean "
        "'FileInfoThread'?.")

  @staticmethod
  def setNameFilters(*__, **_) -> Never:
    """
    Qt's 'void FileInfoThread::setNameFilters(const QStringList
    &nameFilters)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: unknown type name
    'lcFileInfoThread'; did you mean 'FileInfoThread'?.
    """
    raise NotImplementedError(
        "'FileInfoThread.setNameFilters' has no cute function yet. Qt's "
        "'void FileInfoThread::setNameFilters(const QStringList "
        "&nameFilters)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: unknown type "
        "name 'lcFileInfoThread'; did you mean 'FileInfoThread'?.")

  @staticmethod
  def setPath(*__, **_) -> Never:
    """
    Qt's 'void FileInfoThread::setPath(const QString &path)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: unknown type name 'lcFileInfoThread'; did you mean
    'FileInfoThread'?.
    """
    raise NotImplementedError(
        "'FileInfoThread.setPath' has no cute function yet. Qt's 'void "
        "FileInfoThread::setPath(const QString &path)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: unknown type name 'lcFileInfoThread'; did you mean "
        "'FileInfoThread'?.")

  @staticmethod
  def setRootPath(*__, **_) -> Never:
    """
    Qt's 'void FileInfoThread::setRootPath(const QString &path)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: unknown type name 'lcFileInfoThread'; did you mean
    'FileInfoThread'?.
    """
    raise NotImplementedError(
        "'FileInfoThread.setRootPath' has no cute function yet. Qt's 'void "
        "FileInfoThread::setRootPath(const QString &path)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: unknown type name 'lcFileInfoThread'; did you "
        "mean 'FileInfoThread'?.")

  @staticmethod
  def setShowDirs(*__, **_) -> Never:
    """
    Qt's 'void FileInfoThread::setShowDirs(bool showFolders)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: unknown type name 'lcFileInfoThread'; did you mean
    'FileInfoThread'?.
    """
    raise NotImplementedError(
        "'FileInfoThread.setShowDirs' has no cute function yet. Qt's 'void "
        "FileInfoThread::setShowDirs(bool showFolders)': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: unknown type name 'lcFileInfoThread'; did you mean "
        "'FileInfoThread'?.")

  @staticmethod
  def setShowDirsFirst(*__, **_) -> Never:
    """
    Qt's 'void FileInfoThread::setShowDirsFirst(bool show)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: unknown type name 'lcFileInfoThread'; did you mean
    'FileInfoThread'?.
    """
    raise NotImplementedError(
        "'FileInfoThread.setShowDirsFirst' has no cute function yet. Qt's "
        "'void FileInfoThread::setShowDirsFirst(bool show)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: unknown type name 'lcFileInfoThread'; did you "
        "mean 'FileInfoThread'?.")

  @staticmethod
  def setShowDot(*__, **_) -> Never:
    """
    Qt's 'void FileInfoThread::setShowDot(bool on)': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    unknown type name 'lcFileInfoThread'; did you mean 'FileInfoThread'?.
    """
    raise NotImplementedError(
        "'FileInfoThread.setShowDot' has no cute function yet. Qt's 'void "
        "FileInfoThread::setShowDot(bool on)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: unknown type name 'lcFileInfoThread'; did you mean "
        "'FileInfoThread'?.")

  @staticmethod
  def setShowDotAndDotDot(*__, **_) -> Never:
    """
    Qt's 'void FileInfoThread::setShowDotAndDotDot(bool on)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: unknown type name 'lcFileInfoThread'; did you mean
    'FileInfoThread'?.
    """
    raise NotImplementedError(
        "'FileInfoThread.setShowDotAndDotDot' has no cute function yet. "
        "Qt's 'void FileInfoThread::setShowDotAndDotDot(bool on)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: unknown type name 'lcFileInfoThread'; "
        "did you mean 'FileInfoThread'?.")

  @staticmethod
  def setShowDotDot(*__, **_) -> Never:
    """
    Qt's 'void FileInfoThread::setShowDotDot(bool on)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: unknown type name 'lcFileInfoThread'; did you mean
    'FileInfoThread'?.
    """
    raise NotImplementedError(
        "'FileInfoThread.setShowDotDot' has no cute function yet. Qt's "
        "'void FileInfoThread::setShowDotDot(bool on)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: unknown type name 'lcFileInfoThread'; did you mean "
        "'FileInfoThread'?.")

  @staticmethod
  def setShowFiles(*__, **_) -> Never:
    """
    Qt's 'void FileInfoThread::setShowFiles(bool show)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: unknown type name 'lcFileInfoThread'; did you mean
    'FileInfoThread'?.
    """
    raise NotImplementedError(
        "'FileInfoThread.setShowFiles' has no cute function yet. Qt's 'void "
        "FileInfoThread::setShowFiles(bool show)': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: unknown type name 'lcFileInfoThread'; did you mean "
        "'FileInfoThread'?.")

  @staticmethod
  def setShowHidden(*__, **_) -> Never:
    """
    Qt's 'void FileInfoThread::setShowHidden(bool on)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: unknown type name 'lcFileInfoThread'; did you mean
    'FileInfoThread'?.
    """
    raise NotImplementedError(
        "'FileInfoThread.setShowHidden' has no cute function yet. Qt's "
        "'void FileInfoThread::setShowHidden(bool on)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: unknown type name 'lcFileInfoThread'; did you mean "
        "'FileInfoThread'?.")

  @staticmethod
  def setShowOnlyReadable(*__, **_) -> Never:
    """
    Qt's 'void FileInfoThread::setShowOnlyReadable(bool on)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: unknown type name 'lcFileInfoThread'; did you mean
    'FileInfoThread'?.
    """
    raise NotImplementedError(
        "'FileInfoThread.setShowOnlyReadable' has no cute function yet. "
        "Qt's 'void FileInfoThread::setShowOnlyReadable(bool on)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: unknown type name 'lcFileInfoThread'; "
        "did you mean 'FileInfoThread'?.")

  @staticmethod
  def setSortFlags(*__, **_) -> Never:
    """
    Qt's 'void FileInfoThread::setSortFlags(QDir::SortFlags flags)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: unknown type name 'lcFileInfoThread'; did you mean
    'FileInfoThread'?.
    """
    raise NotImplementedError(
        "'FileInfoThread.setSortFlags' has no cute function yet. Qt's 'void "
        "FileInfoThread::setSortFlags(QDir::SortFlags flags)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: unknown type name 'lcFileInfoThread'; did you "
        "mean 'FileInfoThread'?.")

  @staticmethod
  def sortFinished(*__, **_) -> Never:
    """
    Qt's 'void FileInfoThread::sortFinished(const QList<FileProperty> &list)
    const': the compiler refuses its ritual as it would be written here:
    static_cast from 'const FileInfoThread *' to 'QObject *', which are not
    related by inheritance, is not allowed.
    """
    raise NotImplementedError(
        "'FileInfoThread.sortFinished' has no cute function yet. Qt's 'void "
        "FileInfoThread::sortFinished(const QList<FileProperty> &list) "
        "const': the compiler refuses its ritual as it would be written "
        "here: static_cast from 'const FileInfoThread *' to 'QObject *', "
        "which are not related by inheritance, is not allowed.")

  @staticmethod
  def statusChanged(*__, **_) -> Never:
    """
    Qt's 'void FileInfoThread::statusChanged(QQuickFolderListModel::Status
    status) const': the compiler refuses its ritual as it would be written
    here: static_cast from 'const FileInfoThread *' to 'QObject *', which are
    not related by inheritance, is not allowed.
    """
    raise NotImplementedError(
        "'FileInfoThread.statusChanged' has no cute function yet. Qt's "
        "'void FileInfoThread::statusChanged(QQuickFolderListModel::Status "
        "status) const': the compiler refuses its ritual as it would be "
        "written here: static_cast from 'const FileInfoThread *' to "
        "'QObject *', which are not related by inheritance, is not allowed.")
