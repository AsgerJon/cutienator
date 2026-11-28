"""
Qt3DCore::Quick::QQmlAspectEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DQuick/qqmlaspectengine.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..Qt3DCore import Qt3DCore
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QUrl
  from ..QtQml import QQmlEngine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlAspectEngine(QObject):
  """
  The cute side of Qt's Qt3DCore::Quick::QQmlAspectEngine: a plain Python
  object standing in front of one C++ Qt3DCore::Quick::QQmlAspectEngine.

  It is built on the cute 'QObject', as Qt's
  Qt3DCore::Quick::QQmlAspectEngine is built on Qt's QObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::Quick::QQmlAspectEngine that has a ritual
  and that Python can call so far, 9 names in all: 'metaObject', 'tr',
  'status', 'setSource', 'qmlEngine', 'aspectEngine', 'statusChanged',
  'sceneCreated', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DCore::Quick::QQmlAspectEngine::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DCore::Quick::QQmlAspectEngine::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DCore::Quick::QQmlAspectEngine::~QQmlAspectEngine()': the
    destructor: Python never removes a C++ Qt3DCore::Quick::QQmlAspectEngine.
  - Qt's 'const QQmlAspectEnginePrivate
    *Qt3DCore::Quick::QQmlAspectEngine::d_func() const': takes in Python what
    'QQmlAspectEnginePrivate *Qt3DCore::Quick::QQmlAspectEngine::d_func()'
    takes.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DCore::Quick::QQmlAspectEngine is created at the first use,
    not by 'Qt3DCore::Quick::QQmlAspectEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::Quick::QQmlAspectEngine.
  - Qt tells when it has removed the C++ Qt3DCore::Quick::QQmlAspectEngine.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside Qt3DCore::Quick::QQmlAspectEngine, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class Status(CuteNum):
    """
    The enum 'Qt3DCore::Quick::QQmlAspectEngine::Status' of Qt, with the 4
    names Qt gives in it.
    """

    Null = Kee[int](0)
    Ready = Kee[int](1)
    Loading = Kee[int](2)
    Error = Kee[int](3)

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
    Calls Qt's 'QString Qt3DCore::Quick::QQmlAspectEngine::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qqmlaspectengine.html#tr

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
    #  QString Qt3DCore::Quick::QQmlAspectEngine::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN8Qt3DCore5Quick16QQmlAspectEngine2trEPKcS3_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::Quick::QQmlAspectEngine'

  #  A C++ Qt3DCore::Quick::QQmlAspectEngine Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_Quick_QQmlAspectEngine'

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
    *Qt3DCore::Quick::QQmlAspectEngine::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qqmlaspectengine.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DCore::Quick::QQmlAspectEngine::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick16QQmlAspectEngine10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def status(self) -> Status:
    """
    Calls Qt's 'Status Qt3DCore::Quick::QQmlAspectEngine::status() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qqmlaspectengine.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status Qt3DCore::Quick::QQmlAspectEngine::status() const
    return QQmlAspectEngine.Status(self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick16QQmlAspectEngine6statusEv',
    ))

  def qmlEngine(self) -> Optional[QQmlEngine]:
    """
    Calls Qt's 'QQmlEngine *Qt3DCore::Quick::QQmlAspectEngine::qmlEngine()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qqmlaspectengine.html#qmlEngine

    Returns
    -------

    Optional[QQmlEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlEngine *Qt3DCore::Quick::QQmlAspectEngine::qmlEngine() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick16QQmlAspectEngine9qmlEngineEv',
    )
    from ..QtQml import QQmlEngine
    return QQmlEngine._cuteAt(address)

  def aspectEngine(self) -> Optional[Qt3DCore.QAspectEngine]:
    """
    Calls Qt's 'QAspectEngine
    *Qt3DCore::Quick::QQmlAspectEngine::aspectEngine() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qqmlaspectengine.html#aspectEngine

    Returns
    -------

    Optional[Qt3DCore.QAspectEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAspectEngine *Qt3DCore::Quick::QQmlAspectEngine::aspectEngine() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick16QQmlAspectEngine12aspectEngineEv',
    )
    return Qt3DCore.QAspectEngine._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setSource(self, source: QUrl) -> None:
    """
    Calls Qt's 'void Qt3DCore::Quick::QQmlAspectEngine::setSource(const QUrl
    &source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qqmlaspectengine.html#setSource

    Parameters
    ----------

    source : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void Qt3DCore::Quick::QQmlAspectEngine::setSource(const QUrl &source)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick16QQmlAspectEngine9setSourceERK4QUrl',
        self._valueOf(source),
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
    'Qt3DCore::Quick::QQmlAspectEngine::QQmlAspectEngine(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qqmlaspectengine.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DCore::Quick::QQmlAspectEngine::QQmlAspectEngine(QObject *parent)
    self._noteCreation(QQmlAspectEngine, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore5Quick16QQmlAspectEngineC1EP7QObject',
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

  @overload(Status)
  def statusChanged(self, a0: Status) -> None:
    """
    Calls Qt's 'void Qt3DCore::Quick::QQmlAspectEngine::statusChanged(Status
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qqmlaspectengine.html#statusChanged

    Parameters
    ----------

    a0 : Status
      Passed on as its number.
    """
    #  void Qt3DCore::Quick::QQmlAspectEngine::statusChanged(Status a0)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick16QQmlAspectEngine13statusChangedENS1_6Sta'
        'tusE',
        a0.value,
    )

  @overload(QObject)
  @overload(NoneType)
  def sceneCreated(self, rootObject: Optional[QObject]) -> None:
    """
    Calls Qt's 'void Qt3DCore::Quick::QQmlAspectEngine::sceneCreated(QObject
    *rootObject)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qqmlaspectengine.html#sceneCreated

    Parameters
    ----------

    rootObject : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::Quick::QQmlAspectEngine::sceneCreated(QObject
    #      *rootObject)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick16QQmlAspectEngine12sceneCreatedEP7QObject',
        self._addressOf(rootObject, 'QObject'),
    )

  def d_func(self) -> Optional[Qt3DCore.Quick.QQmlAspectEnginePrivate]:
    """
    Calls Qt's 'QQmlAspectEnginePrivate
    *Qt3DCore::Quick::QQmlAspectEngine::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qqmlaspectengine.html#d_func

    Returns
    -------

    Optional[Qt3DCore.Quick.QQmlAspectEnginePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlAspectEnginePrivate *Qt3DCore::Quick::QQmlAspectEngine::d_func()
    address = self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick16QQmlAspectEngine6d_funcEv',
    )
    return Qt3DCore.Quick.QQmlAspectEnginePrivate._cuteAt(address)
