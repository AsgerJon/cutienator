"""
QFileSystemWatcher binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qfilesystemwatcher.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from . import QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QFileSystemWatcherPrivate, QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFileSystemWatcher(QObject):
  """
  The cute side of Qt's QFileSystemWatcher: a plain Python object standing in
  front of one C++ QFileSystemWatcher.

  It is built on the cute 'QObject', as Qt's QFileSystemWatcher is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QFileSystemWatcher that has a ritual and that Python
  can call so far, 11 names in all: 'metaObject', 'tr', 'd_func', 'addPath',
  'addPaths', 'removePath', 'removePaths', 'files', 'directories',
  'fileChanged', 'directoryChanged'. It can be made from Python, in 2 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QFileSystemWatcher::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QFileSystemWatcher::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QFileSystemWatcherPrivate *QFileSystemWatcher::d_func()
    const': takes in Python what 'QFileSystemWatcherPrivate
    *QFileSystemWatcher::d_func()' takes.
  - Qt's 'QFileSystemWatcher::~QFileSystemWatcher()': the destructor: Python
    never removes a C++ QFileSystemWatcher.

  What has no ritual
  ------------------

  2 of the 19 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QFileSystemWatcher is created at the first use, not by
    'QFileSystemWatcher(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QFileSystemWatcher.
  - Qt tells when it has removed the C++ QFileSystemWatcher. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QFileSystemWatcher::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemwatcher.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileSystemWatcher::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QFileSystemWatcher2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFileSystemWatcher'

  #  A C++ QFileSystemWatcher Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QFileSystemWatcher'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QFileSystemWatcher::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemwatcher.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QFileSystemWatcher::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QFileSystemWatcher10metaObjectEv',
    )
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  def files(self) -> QStringList:
    """
    Calls Qt's 'QStringList QFileSystemWatcher::files() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemwatcher.html#files

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QFileSystemWatcher::files() const
    address = self.uglySide.call('ritual_ZNK18QFileSystemWatcher5filesEv')
    return QStringList._cuteOwning(address)

  def directories(self) -> QStringList:
    """
    Calls Qt's 'QStringList QFileSystemWatcher::directories() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemwatcher.html#directories

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QFileSystemWatcher::directories() const
    address = self.uglySide.call(
        'ritual_ZNK18QFileSystemWatcher11directoriesEv',
    )
    return QStringList._cuteOwning(address)

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QFileSystemWatcher::QFileSystemWatcher(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemwatcher.html#QFileSystemWatcher

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QFileSystemWatcher::QFileSystemWatcher(QObject *parent)
    self._noteCreation(QFileSystemWatcher, lambda: Rituals.call(
        'ritual_ZN18QFileSystemWatcherC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(QStringList)
  @overload(QStringList, QObject)
  @overload(QStringList, NoneType)
  def __init__(
      self,
      paths: QStringList,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QFileSystemWatcher::QFileSystemWatcher(const QStringList &paths, QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemwatcher.html#QFileSystemWatcher

    Parameters
    ----------

    paths : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QFileSystemWatcher::QFileSystemWatcher(const QStringList &paths,
    #      QObject *parent)
    self._noteCreation(QFileSystemWatcher, lambda: Rituals.call(
        'ritual_ZN18QFileSystemWatcherC1ERK5QListI7QStringEP7QObject',
        self._valueOf(paths), self._addressOf(parent, 'QObject'),
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

  def d_func(self) -> Optional[QFileSystemWatcherPrivate]:
    """
    Calls Qt's 'QFileSystemWatcherPrivate *QFileSystemWatcher::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemwatcher.html#d_func

    Returns
    -------

    Optional[QFileSystemWatcherPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFileSystemWatcherPrivate *QFileSystemWatcher::d_func()
    address = self.uglySide.call('ritual_ZN18QFileSystemWatcher6d_funcEv')
    from . import QFileSystemWatcherPrivate
    return QFileSystemWatcherPrivate._cuteAt(address)

  @overload(str)
  def addPath(self, file: str) -> bool:
    """
    Calls Qt's 'bool QFileSystemWatcher::addPath(const QString &file)'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemwatcher.html#addPath

    Parameters
    ----------

    file : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QFileSystemWatcher::addPath(const QString &file)
    return self.uglySide.call(
        'ritual_ZN18QFileSystemWatcher7addPathERK7QString', file,
    )

  @overload(QStringList)
  def addPaths(self, files: QStringList) -> QStringList:
    """
    Calls Qt's 'QStringList QFileSystemWatcher::addPaths(const QStringList
    &files)'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemwatcher.html#addPaths

    Parameters
    ----------

    files : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QFileSystemWatcher::addPaths(const QStringList &files)
    address = self.uglySide.call(
        'ritual_ZN18QFileSystemWatcher8addPathsERK5QListI7QStringE',
        self._valueOf(files),
    )
    return QStringList._cuteOwning(address)

  @overload(str)
  def removePath(self, file: str) -> bool:
    """
    Calls Qt's 'bool QFileSystemWatcher::removePath(const QString &file)'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemwatcher.html#removePath

    Parameters
    ----------

    file : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QFileSystemWatcher::removePath(const QString &file)
    return self.uglySide.call(
        'ritual_ZN18QFileSystemWatcher10removePathERK7QString', file,
    )

  @overload(QStringList)
  def removePaths(self, files: QStringList) -> QStringList:
    """
    Calls Qt's 'QStringList QFileSystemWatcher::removePaths(const QStringList
    &files)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemwatcher.html#removePaths

    Parameters
    ----------

    files : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QFileSystemWatcher::removePaths(const QStringList &files)
    address = self.uglySide.call(
        'ritual_ZN18QFileSystemWatcher11removePathsERK5QListI7QStringE',
        self._valueOf(files),
    )
    return QStringList._cuteOwning(address)

  @overload(str)
  def fileChanged(self, path: str) -> None:
    """
    Calls Qt's 'void QFileSystemWatcher::fileChanged(const QString &path,
    QPrivateSignal a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemwatcher.html#fileChanged

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QFileSystemWatcher::fileChanged(const QString &path,
    #      QPrivateSignal a1)
    self.uglySide.call(
        'ritual_ZN18QFileSystemWatcher11fileChangedERK7QStringNS_14QPrivate'
        'SignalE',
        path,
    )

  @overload(str)
  def directoryChanged(self, path: str) -> None:
    """
    Calls Qt's 'void QFileSystemWatcher::directoryChanged(const QString
    &path, QPrivateSignal a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemwatcher.html#directoryChanged

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QFileSystemWatcher::directoryChanged(const QString &path,
    #      QPrivateSignal a1)
    self.uglySide.call(
        'ritual_ZN18QFileSystemWatcher16directoryChangedERK7QStringNS_14QPr'
        'ivateSignalE',
        path,
    )
