"""
QWindowsFileSystemWatcherEngineThread binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qfilesystemwatcher_win_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QWindowsFileSystemWatcherEngineThread to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from . import QThread

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWindowsFileSystemWatcherEngineThread(QThread):
  """
  The cute side of Qt's QWindowsFileSystemWatcherEngineThread: a plain Python
  object standing in front of one C++ QWindowsFileSystemWatcherEngineThread.

  It is built on the cute 'QThread', as Qt's
  QWindowsFileSystemWatcherEngineThread is built on Qt's QThread, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QWindowsFileSystemWatcherEngineThread that has a
  ritual and that Python can call so far, 7 names in all: 'metaObject', 'tr',
  'run', 'stop', 'wakeup', 'fileChanged', 'directoryChanged'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWindowsFileSystemWatcherEngineThread::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QWindowsFileSystemWatcherEngineThread::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QWindowsFileSystemWatcherEngineThread::
    ~QWindowsFileSystemWatcherEngineThread()': the destructor: Python never
    removes a C++ QWindowsFileSystemWatcherEngineThread.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWindowsFileSystemWatcherEngineThread is created at the first
    use, not by 'QWindowsFileSystemWatcherEngineThread(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWindowsFileSystemWatcherEngineThread.
  - Qt tells when it has removed the C++
    QWindowsFileSystemWatcherEngineThread. Every call on the cute object, and
    every use of it as an argument, then raises 'RuntimeError', and nothing
    reaches C++.
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
    Calls Qt's 'QString QWindowsFileSystemWatcherEngineThread::tr(const char
    *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsfilesystemwatcherenginethread.html#tr

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
    #  QString QWindowsFileSystemWatcherEngineThread::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN37QWindowsFileSystemWatcherEngineThread2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWindowsFileSystemWatcherEngineThread'

  #  A C++ QWindowsFileSystemWatcherEngineThread Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWindowsFileSystemWatcherEngineThread'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QWindowsFileSystemWatcherEngineThread::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsfilesystemwatcherenginethread.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWindowsFileSystemWatcherEngineThread::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK37QWindowsFileSystemWatcherEngineThread10metaObjectEv',
    )
    from . import QMetaObject
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QWindowsFileSystemWatcherEngineThread::
    QWindowsFileSystemWatcherEngineThread()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsfilesystemwatcherenginethread.html
    """
    #  QWindowsFileSystemWatcherEngineThread::
    #      QWindowsFileSystemWatcherEngineThread()
    self._noteCreation(
        QWindowsFileSystemWatcherEngineThread, lambda: Rituals.call(
            'ritual_ZN37QWindowsFileSystemWatcherEngineThreadC1Ev',
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

  def run(self) -> None:
    """
    Calls Qt's 'void QWindowsFileSystemWatcherEngineThread::run()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsfilesystemwatcherenginethread.html#run
    """
    #  void QWindowsFileSystemWatcherEngineThread::run()
    ritual = 'ritual_ZN37QWindowsFileSystemWatcherEngineThread3runEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN37QWindowsFileSystemWatcherEngineThread3runEv'
    self.uglySide.call(ritual)

  def stop(self) -> None:
    """
    Calls Qt's 'void QWindowsFileSystemWatcherEngineThread::stop()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsfilesystemwatcherenginethread.html#stop
    """
    #  void QWindowsFileSystemWatcherEngineThread::stop()
    self.uglySide.call(
        'ritual_ZN37QWindowsFileSystemWatcherEngineThread4stopEv',
    )

  def wakeup(self) -> None:
    """
    Calls Qt's 'void QWindowsFileSystemWatcherEngineThread::wakeup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsfilesystemwatcherenginethread.html#wakeup
    """
    #  void QWindowsFileSystemWatcherEngineThread::wakeup()
    self.uglySide.call(
        'ritual_ZN37QWindowsFileSystemWatcherEngineThread6wakeupEv',
    )

  @overload(str, bool)
  def fileChanged(self, path: str, removed: bool) -> None:
    """
    Calls Qt's 'void QWindowsFileSystemWatcherEngineThread::fileChanged(const
    QString &path, bool removed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsfilesystemwatcherenginethread.html

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    removed : bool
      Passed on as it is.
    """
    #  void QWindowsFileSystemWatcherEngineThread::fileChanged(const QString
    #      &path, bool removed)
    self.uglySide.call(
        'ritual_ZN37QWindowsFileSystemWatcherEngineThread11fileChangedERK7Q'
        'Stringb',
        path, removed,
    )

  @overload(str, bool)
  def directoryChanged(self, path: str, removed: bool) -> None:
    """
    Calls Qt's 'void
    QWindowsFileSystemWatcherEngineThread::directoryChanged(const QString
    &path, bool removed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsfilesystemwatcherenginethread.html

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    removed : bool
      Passed on as it is.
    """
    #  void QWindowsFileSystemWatcherEngineThread::directoryChanged(const
    #      QString &path, bool removed)
    self.uglySide.call(
        'ritual_ZN37QWindowsFileSystemWatcherEngineThread16directoryChanged'
        'ERK7QStringb',
        path, removed,
    )
