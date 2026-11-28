"""
QWindowsFileSystemWatcherEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qfilesystemwatcher_win_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QWindowsFileSystemWatcherEngine to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QFileSystemWatcherEngine, QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QFileInfo, QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWindowsFileSystemWatcherEngine(QFileSystemWatcherEngine):
  """
  The cute side of Qt's QWindowsFileSystemWatcherEngine: a plain Python
  object standing in front of one C++ QWindowsFileSystemWatcherEngine.

  It is built on the cute 'QFileSystemWatcherEngine', as Qt's
  QWindowsFileSystemWatcherEngine is built on Qt's QFileSystemWatcherEngine,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWindowsFileSystemWatcherEngine that has a ritual
  and that Python can call so far, 5 names in all: 'metaObject', 'tr',
  'driveLockForRemoval', 'driveLockForRemovalFailed', 'driveRemoved'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWindowsFileSystemWatcherEngine::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QWindowsFileSystemWatcherEngine::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's
    'QWindowsFileSystemWatcherEngine::~QWindowsFileSystemWatcherEngine()':
    the destructor: Python never removes a C++
    QWindowsFileSystemWatcherEngine.
  - Qt's 'QStringList QWindowsFileSystemWatcherEngine::addPaths(const
    QStringList &paths, QStringList *files, QStringList *directories)': names
    'QStringList', which has no cute class yet.
  - Qt's 'QStringList QWindowsFileSystemWatcherEngine::removePaths(const
    QStringList &paths, QStringList *files, QStringList *directories)': names
    'QStringList', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWindowsFileSystemWatcherEngine is created at the first use, not
    by 'QWindowsFileSystemWatcherEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWindowsFileSystemWatcherEngine.
  - Qt tells when it has removed the C++ QWindowsFileSystemWatcherEngine.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  """

  #  The classes Qt writes inside QWindowsFileSystemWatcherEngine, each a
  #  class in here as in C++.

  class Handle(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QWindowsFileSystemWatcherEngine::Handle: a plain
    Python object standing in front of one C++
    QWindowsFileSystemWatcherEngine::Handle.

    C++ hands a QWindowsFileSystemWatcherEngine::Handle around as a copy, so
    every C++ QWindowsFileSystemWatcherEngine::Handle behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QWindowsFileSystemWatcherEngine::Handle yet. It can
    be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QWindowsFileSystemWatcherEngine::Handle::~Handle()': the
      destructor: Python removes its C++
      QWindowsFileSystemWatcherEngine::Handle by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QWindowsFileSystemWatcherEngine::Handle is created at the first
      use, not by 'QWindowsFileSystemWatcherEngine::Handle(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QWindowsFileSystemWatcherEngine::Handle back gives
      a copy the ritual made for Python, in a new cute
      QWindowsFileSystemWatcherEngine::Handle.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QWindowsFileSystemWatcherEngine::Handle'

    #  Qt's '~QWindowsFileSystemWatcherEngine::Handle()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QWindowsFileSystemWatcherEngine::Handle behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN31QWindowsFileSystemWatcherEngine6HandleD1Ev')

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
      'QWindowsFileSystemWatcherEngine::Handle::Handle()', which is called at
      the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qwindowsfilesystemwatcherengine-handle.html
      """
      #  QWindowsFileSystemWatcherEngine::Handle::Handle()
      self._noteCreation(
          QWindowsFileSystemWatcherEngine.Handle, lambda: Rituals.call(
              'ritual_ZN31QWindowsFileSystemWatcherEngine6HandleC1Ev',
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

  class PathInfo(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QWindowsFileSystemWatcherEngine::PathInfo: a plain
    Python object standing in front of one C++
    QWindowsFileSystemWatcherEngine::PathInfo.

    C++ hands a QWindowsFileSystemWatcherEngine::PathInfo around as a copy,
    so every C++ QWindowsFileSystemWatcherEngine::PathInfo behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QWindowsFileSystemWatcherEngine::PathInfo that has
    a ritual and that Python can call so far, 1 name in all: '__ne__'. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'PathInfo
      &QWindowsFileSystemWatcherEngine::PathInfo::operator=(const QFileInfo
      &fileInfo)': assignment: Python binds a name and has no operator for
      it.
    - Qt's 'QWindowsFileSystemWatcherEngine::PathInfo::~PathInfo()': the
      destructor: Python removes its C++
      QWindowsFileSystemWatcherEngine::PathInfo by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QWindowsFileSystemWatcherEngine::PathInfo is created at the
      first use, not by 'QWindowsFileSystemWatcherEngine::PathInfo(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QWindowsFileSystemWatcherEngine::PathInfo back
      gives a copy the ritual made for Python, in a new cute
      QWindowsFileSystemWatcherEngine::PathInfo.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QFileInfo = WAIT['QFileInfo']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QWindowsFileSystemWatcherEngine::PathInfo'

    #  Qt's '~QWindowsFileSystemWatcherEngine::PathInfo()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QWindowsFileSystemWatcherEngine::PathInfo behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN31QWindowsFileSystemWatcherEngine8PathInfoD1Ev')

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

    @overload(QFileInfo)
    def __ne__(self, fileInfo: QFileInfo) -> bool:
      """
      Calls Qt's 'bool
      QWindowsFileSystemWatcherEngine::PathInfo::operator!=(const QFileInfo
      &fileInfo) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qwindowsfilesystemwatcherengine-pathinfo.html

      Parameters
      ----------

      fileInfo : QFileInfo
        Passed on as a value: Qt reads the C++ QFileInfo, which stays
        Python's own.
      """
      #  bool QWindowsFileSystemWatcherEngine::PathInfo::operator!=(const
      #      QFileInfo &fileInfo) const
      return self.uglySide.call(
          'ritual_ZNK31QWindowsFileSystemWatcherEngine8PathInfoneERK9QFileI'
          'nfo',
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
    Calls Qt's 'QString QWindowsFileSystemWatcherEngine::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsfilesystemwatcherengine.html#tr

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
    #  QString QWindowsFileSystemWatcherEngine::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN31QWindowsFileSystemWatcherEngine2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWindowsFileSystemWatcherEngine'

  #  A C++ QWindowsFileSystemWatcherEngine Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWindowsFileSystemWatcherEngine'

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
    *QWindowsFileSystemWatcherEngine::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsfilesystemwatcherengine.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWindowsFileSystemWatcherEngine::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK31QWindowsFileSystemWatcherEngine10metaObjectEv',
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

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's
    'QWindowsFileSystemWatcherEngine::QWindowsFileSystemWatcherEngine(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsfilesystemwatcherengine.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QWindowsFileSystemWatcherEngine::QWindowsFileSystemWatcherEngine(
    #      QObject *parent)
    self._noteCreation(QWindowsFileSystemWatcherEngine, lambda: Rituals.call(
        'ritual_ZN31QWindowsFileSystemWatcherEngineC1EP7QObject',
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

  @overload(str)
  def driveLockForRemoval(self, a0: str) -> None:
    """
    Calls Qt's 'void
    QWindowsFileSystemWatcherEngine::driveLockForRemoval(const QString &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsfilesystemwatcherengine.html

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWindowsFileSystemWatcherEngine::driveLockForRemoval(const
    #      QString &a0)
    self.uglySide.call(
        'ritual_ZN31QWindowsFileSystemWatcherEngine19driveLockForRemovalERK'
        '7QString',
        a0,
    )

  @overload(str)
  def driveLockForRemovalFailed(self, a0: str) -> None:
    """
    Calls Qt's 'void
    QWindowsFileSystemWatcherEngine::driveLockForRemovalFailed(const QString
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsfilesystemwatcherengine.html

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWindowsFileSystemWatcherEngine::driveLockForRemovalFailed(const
    #      QString &a0)
    self.uglySide.call(
        'ritual_ZN31QWindowsFileSystemWatcherEngine25driveLockForRemovalFai'
        'ledERK7QString',
        a0,
    )

  @overload(str)
  def driveRemoved(self, a0: str) -> None:
    """
    Calls Qt's 'void QWindowsFileSystemWatcherEngine::driveRemoved(const
    QString &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsfilesystemwatcherengine.html#driveRemoved

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWindowsFileSystemWatcherEngine::driveRemoved(const QString &a0)
    self.uglySide.call(
        'ritual_ZN31QWindowsFileSystemWatcherEngine12driveRemovedERK7QStrin'
        'g',
        a0,
    )
