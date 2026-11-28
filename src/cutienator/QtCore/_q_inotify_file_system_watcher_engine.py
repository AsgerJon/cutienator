"""
QInotifyFileSystemWatcherEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qfilesystemwatcher_inotify_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QInotifyFileSystemWatcherEngine to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from . import QFileSystemWatcherEngine, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QMetaObject


class QInotifyFileSystemWatcherEngine(QFileSystemWatcherEngine):
  """
  The cute side of Qt's QInotifyFileSystemWatcherEngine: a plain Python
  object standing in front of one C++ QInotifyFileSystemWatcherEngine.

  It is built on the cute 'QFileSystemWatcherEngine', as Qt's
  QInotifyFileSystemWatcherEngine is built on Qt's QFileSystemWatcherEngine,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QInotifyFileSystemWatcherEngine that has a ritual
  and that Python can call so far, 3 names in all: 'metaObject',
  'readFromInotify', 'getPathFromID'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QInotifyFileSystemWatcherEngine::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QInotifyFileSystemWatcherEngine::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's
    'QInotifyFileSystemWatcherEngine::~QInotifyFileSystemWatcherEngine()':
    the destructor: Python never removes a C++
    QInotifyFileSystemWatcherEngine.
  - Qt's 'QStringList QInotifyFileSystemWatcherEngine::addPaths(const
    QStringList &paths, QStringList *files, QStringList *directories)': names
    'QStringList', which has no cute class yet.
  - Qt's 'QStringList QInotifyFileSystemWatcherEngine::removePaths(const
    QStringList &paths, QStringList *files, QStringList *directories)': names
    'QStringList', which has no cute class yet.

  What has no ritual
  ------------------

  5 of the 13 functions Qt declares: 3 leans on
  'QInotifyFileSystemWatcherEngine; 2 not a gap.

  What to expect
  --------------

  - The C++ QInotifyFileSystemWatcherEngine is created at the first use, not
    by 'QInotifyFileSystemWatcherEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QInotifyFileSystemWatcherEngine.
  - Qt tells when it has removed the C++ QInotifyFileSystemWatcherEngine.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QInotifyFileSystemWatcherEngine that has no cute
    function yet, '__init__', 'create', holds a function that raises
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
  __qt_class__ = 'QInotifyFileSystemWatcherEngine'

  #  A C++ QInotifyFileSystemWatcherEngine Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QInotifyFileSystemWatcherEngine'

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
    *QInotifyFileSystemWatcherEngine::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinotifyfilesystemwatcherengine.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QInotifyFileSystemWatcherEngine::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK31QInotifyFileSystemWatcherEngine10metaObjectEv',
    )
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(int)
  def getPathFromID(self, id: int) -> str:
    """
    Calls Qt's 'QString QInotifyFileSystemWatcherEngine::getPathFromID(int
    id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinotifyfilesystemwatcherengine.html#getPathFromID

    Parameters
    ----------

    id : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QInotifyFileSystemWatcherEngine::getPathFromID(int id) const
    return self.uglySide.call(
        'ritual_ZNK31QInotifyFileSystemWatcherEngine13getPathFromIDEi', id,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's
    'QInotifyFileSystemWatcherEngine::QInotifyFileSystemWatcherEngine(int fd,
    QObject *parent)': leans on
    'QInotifyFileSystemWatcherEngine::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QInotifyFileSystemWatcherEngine.__init__' has no cute function "
        "yet. Qt's "
        "'QInotifyFileSystemWatcherEngine::QInotifyFileSystemWatcherEngine(i"
        "nt fd, QObject *parent)': leans on "
        "'QInotifyFileSystemWatcherEngine::qt_metacall(QMetaObject::Call, "
        "int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

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

  def readFromInotify(self) -> None:
    """
    Calls Qt's 'void QInotifyFileSystemWatcherEngine::readFromInotify()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinotifyfilesystemwatcherengine.html
    """
    #  void QInotifyFileSystemWatcherEngine::readFromInotify()
    self.uglySide.call(
        'ritual_ZN31QInotifyFileSystemWatcherEngine15readFromInotifyEv',
    )

  @staticmethod
  def create(*__, **_) -> Never:
    """
    Qt's 'QInotifyFileSystemWatcherEngine
    *QInotifyFileSystemWatcherEngine::create(QObject *parent)': leans on
    'QInotifyFileSystemWatcherEngine::staticMetaObject', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QInotifyFileSystemWatcherEngine.create' has no cute function yet. "
        "Qt's 'QInotifyFileSystemWatcherEngine "
        "*QInotifyFileSystemWatcherEngine::create(QObject *parent)': leans "
        "on 'QInotifyFileSystemWatcherEngine::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
