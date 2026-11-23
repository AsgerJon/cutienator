"""
QFileInfoGatherer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qfileinfogatherer_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QFileInfoGatherer to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject, QStringList, QThread

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject
  from . import QAbstractFileIconProvider
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractFileIconProvider = WAIT['QAbstractFileIconProvider']
  QEvent = WAIT['QEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFileInfoGatherer(QThread):
  """
  The cute side of Qt's QFileInfoGatherer: a plain Python object standing in
  front of one C++ QFileInfoGatherer.

  It is built on the cute 'QThread', as Qt's QFileInfoGatherer is built on
  Qt's QThread, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QFileInfoGatherer that has a ritual and that Python
  can call so far, 24 names in all: 'metaObject', 'tr', 'watchedFiles',
  'watchedDirectories', 'watchPaths', 'unwatchPaths', 'isWatching',
  'setWatching', 'clear', 'removePath', 'iconProvider', 'resolveSymlinks',
  'requestAbort', 'list', 'fetchExtendedInformation', 'updateFile',
  'setResolveSymlinks', 'setIconProvider', 'driveAdded', 'driveRemoved',
  'event', 'run', 'getFileInfos', 'createWatcher'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFileInfoGatherer::~QFileInfoGatherer()': the destructor: Python
    never removes a C++ QFileInfoGatherer.

  What has no ritual
  ------------------

  10 of the 36 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet; 4 a signal; 1 a template; 1 declared and nowhere to be found.

  What to expect
  --------------

  - The C++ QFileInfoGatherer is created at the first use, not by
    'QFileInfoGatherer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QFileInfoGatherer.
  - Qt tells when it has removed the C++ QFileInfoGatherer. Every call on the
    cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QFileInfoGatherer::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfogatherer.html#tr

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
    #  QString QFileInfoGatherer::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QFileInfoGatherer2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFileInfoGatherer'

  #  A C++ QFileInfoGatherer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QFileInfoGatherer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QFileInfoGatherer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfogatherer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QFileInfoGatherer::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QFileInfoGatherer10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def watchedFiles(self) -> QStringList:
    """
    Calls Qt's 'QStringList QFileInfoGatherer::watchedFiles() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfileinfogatherer.html#watchedFiles

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QFileInfoGatherer::watchedFiles() const
    address = self.uglySide.call(
        'ritual_ZNK17QFileInfoGatherer12watchedFilesEv',
    )
    return QStringList._cuteOwning(address)

  def watchedDirectories(self) -> QStringList:
    """
    Calls Qt's 'QStringList QFileInfoGatherer::watchedDirectories() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfileinfogatherer.html#watchedDirectories

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QFileInfoGatherer::watchedDirectories() const
    address = self.uglySide.call(
        'ritual_ZNK17QFileInfoGatherer18watchedDirectoriesEv',
    )
    return QStringList._cuteOwning(address)

  def isWatching(self) -> bool:
    """
    Calls Qt's 'bool QFileInfoGatherer::isWatching() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfogatherer.html#isWatching
    """
    #  bool QFileInfoGatherer::isWatching() const
    return self.uglySide.call('ritual_ZNK17QFileInfoGatherer10isWatchingEv')

  def iconProvider(self) -> Optional[QAbstractFileIconProvider]:
    """
    Calls Qt's 'QAbstractFileIconProvider *QFileInfoGatherer::iconProvider()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfileinfogatherer.html#iconProvider

    Returns
    -------

    Optional[QAbstractFileIconProvider]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractFileIconProvider *QFileInfoGatherer::iconProvider() const
    address = self.uglySide.call(
        'ritual_ZNK17QFileInfoGatherer12iconProviderEv',
    )
    from . import QAbstractFileIconProvider
    return QAbstractFileIconProvider._cuteAt(address)

  def resolveSymlinks(self) -> bool:
    """
    Calls Qt's 'bool QFileInfoGatherer::resolveSymlinks() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfileinfogatherer.html#resolveSymlinks
    """
    #  bool QFileInfoGatherer::resolveSymlinks() const
    return self.uglySide.call(
        'ritual_ZNK17QFileInfoGatherer15resolveSymlinksEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setWatching(self, v: bool) -> None:
    """
    Calls Qt's 'void QFileInfoGatherer::setWatching(bool v)'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfogatherer.html#setWatching

    Parameters
    ----------

    v : bool
      Passed on as it is.
    """
    #  void QFileInfoGatherer::setWatching(bool v)
    self.uglySide.call('ritual_ZN17QFileInfoGatherer11setWatchingEb', v)

  @overload(bool)
  def setResolveSymlinks(self, enable: bool) -> None:
    """
    Calls Qt's 'void QFileInfoGatherer::setResolveSymlinks(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfileinfogatherer.html#setResolveSymlinks

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QFileInfoGatherer::setResolveSymlinks(bool enable)
    self.uglySide.call(
        'ritual_ZN17QFileInfoGatherer18setResolveSymlinksEb', enable,
    )

  @overload(QAbstractFileIconProvider)
  @overload(NoneType)
  def setIconProvider(
      self,
      provider: Optional[QAbstractFileIconProvider],
  ) -> None:
    """
    Calls Qt's 'void
    QFileInfoGatherer::setIconProvider(QAbstractFileIconProvider *provider)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfileinfogatherer.html#setIconProvider

    Parameters
    ----------

    provider : Optional[QAbstractFileIconProvider]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFileInfoGatherer::setIconProvider(QAbstractFileIconProvider
    #      *provider)
    self.uglySide.call(
        'ritual_ZN17QFileInfoGatherer15setIconProviderEP25QAbstractFileIcon'
        'Provider',
        self._addressOf(provider),
    )

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
    'QFileInfoGatherer::QFileInfoGatherer(QObject *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qfileinfogatherer.html#QFileInfoGatherer

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QFileInfoGatherer::QFileInfoGatherer(QObject *parent)
    self._noteCreation(QFileInfoGatherer, lambda: Rituals.call(
        'ritual_ZN17QFileInfoGathererC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  @overload(QStringList)
  def watchPaths(self, paths: QStringList) -> None:
    """
    Calls Qt's 'void QFileInfoGatherer::watchPaths(const QStringList
    &paths)'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfogatherer.html#watchPaths

    Parameters
    ----------

    paths : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QFileInfoGatherer::watchPaths(const QStringList &paths)
    self.uglySide.call(
        'ritual_ZN17QFileInfoGatherer10watchPathsERK5QListI7QStringE',
        self._valueOf(paths),
    )

  @overload(QStringList)
  def unwatchPaths(self, paths: QStringList) -> None:
    """
    Calls Qt's 'void QFileInfoGatherer::unwatchPaths(const QStringList
    &paths)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfileinfogatherer.html#unwatchPaths

    Parameters
    ----------

    paths : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QFileInfoGatherer::unwatchPaths(const QStringList &paths)
    self.uglySide.call(
        'ritual_ZN17QFileInfoGatherer12unwatchPathsERK5QListI7QStringE',
        self._valueOf(paths),
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QFileInfoGatherer::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfogatherer.html#clear
    """
    #  void QFileInfoGatherer::clear()
    self.uglySide.call('ritual_ZN17QFileInfoGatherer5clearEv')

  @overload(str)
  def removePath(self, path: str) -> None:
    """
    Calls Qt's 'void QFileInfoGatherer::removePath(const QString &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfogatherer.html#removePath

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QFileInfoGatherer::removePath(const QString &path)
    self.uglySide.call(
        'ritual_ZN17QFileInfoGatherer10removePathERK7QString', path,
    )

  def requestAbort(self) -> None:
    """
    Calls Qt's 'void QFileInfoGatherer::requestAbort()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfileinfogatherer.html#requestAbort
    """
    #  void QFileInfoGatherer::requestAbort()
    self.uglySide.call('ritual_ZN17QFileInfoGatherer12requestAbortEv')

  @overload(str)
  def list(self, directoryPath: str) -> None:
    """
    Calls Qt's 'void QFileInfoGatherer::list(const QString &directoryPath)'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfogatherer.html#list

    Parameters
    ----------

    directoryPath : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QFileInfoGatherer::list(const QString &directoryPath)
    self.uglySide.call(
        'ritual_ZN17QFileInfoGatherer4listERK7QString', directoryPath,
    )

  @overload(str, QStringList)
  def fetchExtendedInformation(self, path: str, files: QStringList) -> None:
    """
    Calls Qt's 'void QFileInfoGatherer::fetchExtendedInformation(const
    QString &path, const QStringList &files)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfileinfogatherer.html#fetchExtendedInformation

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    files : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QFileInfoGatherer::fetchExtendedInformation(const QString &path,
    #      const QStringList &files)
    self.uglySide.call(
        'ritual_ZN17QFileInfoGatherer24fetchExtendedInformationERK7QStringR'
        'K5QListIS0_E',
        path, self._valueOf(files),
    )

  @overload(str)
  def updateFile(self, path: str) -> None:
    """
    Calls Qt's 'void QFileInfoGatherer::updateFile(const QString &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfogatherer.html#updateFile

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QFileInfoGatherer::updateFile(const QString &path)
    self.uglySide.call(
        'ritual_ZN17QFileInfoGatherer10updateFileERK7QString', path,
    )

  def driveAdded(self) -> None:
    """
    Calls Qt's 'void QFileInfoGatherer::driveAdded()'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfogatherer.html#driveAdded
    """
    #  void QFileInfoGatherer::driveAdded()
    self.uglySide.call('ritual_ZN17QFileInfoGatherer10driveAddedEv')

  def driveRemoved(self) -> None:
    """
    Calls Qt's 'void QFileInfoGatherer::driveRemoved()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfileinfogatherer.html#driveRemoved
    """
    #  void QFileInfoGatherer::driveRemoved()
    self.uglySide.call('ritual_ZN17QFileInfoGatherer12driveRemovedEv')

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QFileInfoGatherer::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfogatherer.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QFileInfoGatherer::event(QEvent *event)
    ritual = 'ritual_ZN17QFileInfoGatherer5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QFileInfoGatherer5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  def run(self) -> None:
    """
    Calls Qt's 'void QFileInfoGatherer::run()'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfogatherer.html#run
    """
    #  void QFileInfoGatherer::run()
    ritual = 'ritual_ZN17QFileInfoGatherer3runEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QFileInfoGatherer3runEv'
    self.uglySide.call(ritual)

  @overload(str, QStringList)
  def getFileInfos(self, path: str, files: QStringList) -> None:
    """
    Calls Qt's 'void QFileInfoGatherer::getFileInfos(const QString &path,
    const QStringList &files)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfileinfogatherer.html#getFileInfos

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    files : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QFileInfoGatherer::getFileInfos(const QString &path, const
    #      QStringList &files)
    self.uglySide.call(
        'ritual_ZN17QFileInfoGatherer12getFileInfosERK7QStringRK5QListIS0_E',
        path, self._valueOf(files),
    )

  def createWatcher(self) -> None:
    """
    Calls Qt's 'void QFileInfoGatherer::createWatcher()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfileinfogatherer.html#createWatcher
    """
    #  void QFileInfoGatherer::createWatcher()
    self.uglySide.call('ritual_ZN17QFileInfoGatherer13createWatcherEv')
