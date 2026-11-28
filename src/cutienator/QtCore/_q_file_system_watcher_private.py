"""
QFileSystemWatcherPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qfilesystemwatcher_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QFileSystemWatcherPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QFileSystemWatcher, QFileSystemWatcherEngine, QObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFileSystemWatcherPrivate(QObjectPrivate):
  """
  The cute side of Qt's QFileSystemWatcherPrivate: a plain Python object
  standing in front of one C++ QFileSystemWatcherPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QFileSystemWatcherPrivate
  is built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QFileSystemWatcherPrivate that has a ritual and that
  Python can call so far, 2 names in all: 'q_func', 'createNativeEngine'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QFileSystemWatcher *QFileSystemWatcherPrivate::q_func()
    const': takes in Python what 'QFileSystemWatcher
    *QFileSystemWatcherPrivate::q_func()' takes.

  What has no ritual
  ------------------

  5 of the 9 functions Qt declares: 3 leans on 'QFileSystemWatcherEngine; 2
  Qt's library has no name for it, and its code in Qt's source does not
  compile apart from its file.

  What to expect
  --------------

  - The C++ QFileSystemWatcherPrivate is created at the first use, not by
    'QFileSystemWatcherPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QFileSystemWatcherPrivate.
  - Each name of Qt's QFileSystemWatcherPrivate that has no cute function
    yet, 'connectEngine', 'directoryChanged', 'fileChanged', 'init',
    'initPollerEngine', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def createNativeEngine(
      parent: Optional[QObject],
  ) -> Optional[QFileSystemWatcherEngine]:
    """
    Calls Qt's 'QFileSystemWatcherEngine
    *QFileSystemWatcherPrivate::createNativeEngine(QObject *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemwatcherprivate.html#createNativeEngine

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QFileSystemWatcherEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFileSystemWatcherEngine
    #      *QFileSystemWatcherPrivate::createNativeEngine(QObject *parent)
    address = Rituals.call(
        'ritual_ZN25QFileSystemWatcherPrivate18createNativeEngineEP7QObject',
        CuteMixin._addressOf(parent, 'QObject'),
    )
    from . import QFileSystemWatcherEngine
    return QFileSystemWatcherEngine._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFileSystemWatcherPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    'QFileSystemWatcherPrivate::QFileSystemWatcherPrivate()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemwatcherprivate.html
    """
    #  QFileSystemWatcherPrivate::QFileSystemWatcherPrivate()
    self._noteCreation(QFileSystemWatcherPrivate, lambda: Rituals.call(
        'ritual_ZN25QFileSystemWatcherPrivateC1Ev',
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

  def q_func(self) -> Optional[QFileSystemWatcher]:
    """
    Calls Qt's 'QFileSystemWatcher *QFileSystemWatcherPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemwatcherprivate.html#q_func

    Returns
    -------

    Optional[QFileSystemWatcher]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFileSystemWatcher *QFileSystemWatcherPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN25QFileSystemWatcherPrivate6q_funcEv',
    )
    from . import QFileSystemWatcher
    return QFileSystemWatcher._cuteAt(address)

  @staticmethod
  def connectEngine(*__, **_) -> Never:
    """
    Qt's 'void
    QFileSystemWatcherPrivate::connectEngine(QFileSystemWatcherEngine *e)':
    leans on 'QFileSystemWatcherEngine::fileChanged(QString const&, bool)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QFileSystemWatcherPrivate.connectEngine' has no cute function "
        "yet. Qt's 'void "
        "QFileSystemWatcherPrivate::connectEngine(QFileSystemWatcherEngine "
        "*e)': leans on 'QFileSystemWatcherEngine::fileChanged(QString "
        "const&, bool)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def directoryChanged(*__, **_) -> Never:
    """
    Qt's 'void QFileSystemWatcherPrivate::directoryChanged(const QString
    &path, bool removed)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: use of undeclared
    identifier 'lcWatcher'.
    """
    raise NotImplementedError(
        "'QFileSystemWatcherPrivate.directoryChanged' has no cute function "
        "yet. Qt's 'void QFileSystemWatcherPrivate::directoryChanged(const "
        "QString &path, bool removed)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "use of undeclared identifier 'lcWatcher'.")

  @staticmethod
  def fileChanged(*__, **_) -> Never:
    """
    Qt's 'void QFileSystemWatcherPrivate::fileChanged(const QString &path,
    bool removed)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'lcWatcher'.
    """
    raise NotImplementedError(
        "'QFileSystemWatcherPrivate.fileChanged' has no cute function yet. "
        "Qt's 'void QFileSystemWatcherPrivate::fileChanged(const QString "
        "&path, bool removed)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'lcWatcher'.")

  @staticmethod
  def init(*__, **_) -> Never:
    """
    Qt's 'void QFileSystemWatcherPrivate::init()': leans on
    'QFileSystemWatcherEngine::fileChanged(QString const&, bool)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QFileSystemWatcherPrivate.init' has no cute function yet. Qt's "
        "'void QFileSystemWatcherPrivate::init()': leans on "
        "'QFileSystemWatcherEngine::fileChanged(QString const&, bool)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def initPollerEngine(*__, **_) -> Never:
    """
    Qt's 'void QFileSystemWatcherPrivate::initPollerEngine()': leans on
    'QFileSystemWatcherEngine::fileChanged(QString const&, bool)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QFileSystemWatcherPrivate.initPollerEngine' has no cute function "
        "yet. Qt's 'void QFileSystemWatcherPrivate::initPollerEngine()': "
        "leans on 'QFileSystemWatcherEngine::fileChanged(QString const&, "
        "bool)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")
