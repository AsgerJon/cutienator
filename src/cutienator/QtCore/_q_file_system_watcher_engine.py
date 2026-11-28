"""
QFileSystemWatcherEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qfilesystemwatcher_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QFileSystemWatcherEngine to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from . import QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QMetaObject


class QFileSystemWatcherEngine(QObject):
  """
  The cute side of Qt's QFileSystemWatcherEngine: a plain Python object
  standing in front of one C++ QFileSystemWatcherEngine.

  It is built on the cute 'QObject', as Qt's QFileSystemWatcherEngine is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QFileSystemWatcherEngine that has a ritual and that
  Python can call so far, 3 names in all: 'metaObject', 'fileChanged',
  'directoryChanged'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QFileSystemWatcherEngine::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QFileSystemWatcherEngine::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QStringList QFileSystemWatcherEngine::addPaths(const QStringList
    &paths, QStringList *files, QStringList *directories)': names
    'QStringList', which has no cute class yet.
  - Qt's 'QStringList QFileSystemWatcherEngine::removePaths(const QStringList
    &paths, QStringList *files, QStringList *directories)': names
    'QStringList', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 11 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open; 1 leans on 'QFileSystemWatcherEngine.

  What to expect
  --------------

  - The C++ QFileSystemWatcherEngine is created at the first use, not by
    'QFileSystemWatcherEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QFileSystemWatcherEngine.
  - Qt tells when it has removed the C++ QFileSystemWatcherEngine. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QFileSystemWatcherEngine that has no cute function yet,
    '__init__', 'addPaths', 'removePaths', holds a function that raises
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
  __qt_class__ = 'QFileSystemWatcherEngine'

  #  A C++ QFileSystemWatcherEngine Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QFileSystemWatcherEngine'

  #  The functions Qt calls itself that QFileSystemWatcherEngine is the first
  #  to declare and that cannot be handed to Python yet, each as Qt declares
  #  it. A class of a program that writes one of them anew is refused, since
  #  Qt would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'addPaths': (
          'QStringList QFileSystemWatcherEngine::addPaths(const '
          'QStringList &, QStringList *, QStringList *)',
      ),
      'removePaths': (
          'QStringList QFileSystemWatcherEngine::removePaths(const '
          'QStringList &, QStringList *, QStringList *)',
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QFileSystemWatcherEngine::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemwatcherengine.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QFileSystemWatcherEngine::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QFileSystemWatcherEngine10metaObjectEv',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QFileSystemWatcherEngine::QFileSystemWatcherEngine(QObject
    *parent)': the class is abstract, so C++ cannot make one, and the C++
    class of ours does not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QFileSystemWatcherEngine.__init__' has no cute function yet. Qt's "
        "'QFileSystemWatcherEngine::QFileSystemWatcherEngine(QObject "
        "*parent)': the class is abstract, so C++ cannot make one, and the "
        "C++ class of ours does not fill in every function it leaves open.")

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

  @overload(str, bool)
  def fileChanged(self, path: str, removed: bool) -> None:
    """
    Calls Qt's 'void QFileSystemWatcherEngine::fileChanged(const QString
    &path, bool removed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemwatcherengine.html#fileChanged

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    removed : bool
      Passed on as it is.
    """
    #  void QFileSystemWatcherEngine::fileChanged(const QString &path, bool
    #      removed)
    self.uglySide.call(
        'ritual_ZN24QFileSystemWatcherEngine11fileChangedERK7QStringb',
        path, removed,
    )

  @overload(str, bool)
  def directoryChanged(self, path: str, removed: bool) -> None:
    """
    Calls Qt's 'void QFileSystemWatcherEngine::directoryChanged(const QString
    &path, bool removed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemwatcherengine.html#directoryChanged

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    removed : bool
      Passed on as it is.
    """
    #  void QFileSystemWatcherEngine::directoryChanged(const QString &path,
    #      bool removed)
    self.uglySide.call(
        'ritual_ZN24QFileSystemWatcherEngine16directoryChangedERK7QStringb',
        path, removed,
    )

  @staticmethod
  def addPaths(*__, **_) -> Never:
    """
    Qt's 'QStringList QFileSystemWatcherEngine::addPaths(const QStringList
    &paths, QStringList *files, QStringList *directories)': names
    'QStringList', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QFileSystemWatcherEngine.addPaths' has no cute function yet. Qt's "
        "'QStringList QFileSystemWatcherEngine::addPaths(const QStringList "
        "&paths, QStringList *files, QStringList *directories)': names "
        "'QStringList', which has no cute class yet.")

  @staticmethod
  def removePaths(*__, **_) -> Never:
    """
    Qt's 'QStringList QFileSystemWatcherEngine::removePaths(const QStringList
    &paths, QStringList *files, QStringList *directories)': names
    'QStringList', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QFileSystemWatcherEngine.removePaths' has no cute function yet. "
        "Qt's 'QStringList QFileSystemWatcherEngine::removePaths(const "
        "QStringList &paths, QStringList *files, QStringList "
        "*directories)': names 'QStringList', which has no cute class yet.")
