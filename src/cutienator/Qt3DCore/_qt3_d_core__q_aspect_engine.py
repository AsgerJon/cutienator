"""
Qt3DCore::QAspectEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/qaspectengine.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVariant

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAspectEngine(QObject):
  """
  The cute side of Qt's Qt3DCore::QAspectEngine: a plain Python object
  standing in front of one C++ Qt3DCore::QAspectEngine.

  It is built on the cute 'QObject', as Qt's Qt3DCore::QAspectEngine is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QAspectEngine that has a ritual and that
  Python can call so far, 11 names in all: 'metaObject', 'tr', 'setRunMode',
  'runMode', 'registerAspect', 'unregisterAspect', 'aspect',
  'executeCommand', 'processFrame', 'lookupNode', 'd_func'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DCore::QAspectEngine::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Qt3DCore::QAspectEngine::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DCore::QAspectEngine::~QAspectEngine()': the destructor: Python
    never removes a C++ Qt3DCore::QAspectEngine.
  - Qt's 'void Qt3DCore::QAspectEngine::setRootEntity(QEntityPtr root)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QEntityPtr Qt3DCore::QAspectEngine::rootEntity() const': gives a
    type Python has no way to take yet.
  - Qt's 'QList<QAbstractAspect *> Qt3DCore::QAspectEngine::aspects() const':
    gives a type Python has no way to take yet.
  - Qt's 'QList<QNode *> Qt3DCore::QAspectEngine::lookupNodes(const
    QList<QNodeId> &ids) const': takes a type Python has no way to hand over
    yet.
  - Qt's 'const QAspectEnginePrivate *Qt3DCore::QAspectEngine::d_func()
    const': takes in Python what 'QAspectEnginePrivate
    *Qt3DCore::QAspectEngine::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 24 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DCore::QAspectEngine is created at the first use, not by
    'Qt3DCore::QAspectEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QAspectEngine.
  - Qt tells when it has removed the C++ Qt3DCore::QAspectEngine. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DCore::QAspectEngine that has no cute function yet,
    'aspects', 'lookupNodes', 'rootEntity', 'setRootEntity', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside Qt3DCore::QAspectEngine, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class RunMode(CuteNum):
    """
    The enum 'Qt3DCore::QAspectEngine::RunMode' of Qt, with the 2 names Qt
    gives in it.
    """

    Manual = Kee[int](0)
    Automatic = Kee[int](1)

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
    Calls Qt's 'QString Qt3DCore::QAspectEngine::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qaspectengine.html#tr

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
    #  QString Qt3DCore::QAspectEngine::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN8Qt3DCore13QAspectEngine2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QAspectEngine'

  #  A C++ Qt3DCore::QAspectEngine Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_QAspectEngine'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DCore::QAspectEngine::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectengine.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DCore::QAspectEngine::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore13QAspectEngine10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def runMode(self) -> RunMode:
    """
    Calls Qt's 'RunMode Qt3DCore::QAspectEngine::runMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectengine.html#runMode

    Returns
    -------

    RunMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'RunMode(number)' gives.
    """
    #  RunMode Qt3DCore::QAspectEngine::runMode() const
    return QAspectEngine.RunMode(self.uglySide.call(
        'ritual_ZNK8Qt3DCore13QAspectEngine7runModeEv',
    ))

  @overload(str)
  def aspect(self, name: str) -> Optional[Qt3DCore.QAbstractAspect]:
    """
    Calls Qt's 'QAbstractAspect *Qt3DCore::QAspectEngine::aspect(const
    QString &name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qaspectengine.html#aspect

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[Qt3DCore.QAbstractAspect]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAspect *Qt3DCore::QAspectEngine::aspect(const QString &name)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore13QAspectEngine6aspectERK7QString', name,
    )
    return Qt3DCore.QAbstractAspect._cuteAt(address)

  @overload(WAIT['Qt3DCore.QNodeId'])
  def lookupNode(self, id: Qt3DCore.QNodeId) -> Optional[Qt3DCore.QNode]:
    """
    Calls Qt's 'QNode *Qt3DCore::QAspectEngine::lookupNode(QNodeId id)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectengine.html#lookupNode

    Parameters
    ----------

    id : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.

    Returns
    -------

    Optional[Qt3DCore.QNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNode *Qt3DCore::QAspectEngine::lookupNode(QNodeId id) const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore13QAspectEngine10lookupNodeENS_7QNodeIdE',
        self._valueOf(id),
    )
    return Qt3DCore.QNode._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(RunMode)
  def setRunMode(self, mode: RunMode) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAspectEngine::setRunMode(RunMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectengine.html#setRunMode

    Parameters
    ----------

    mode : RunMode
      Passed on as its number.
    """
    #  void Qt3DCore::QAspectEngine::setRunMode(RunMode mode)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore13QAspectEngine10setRunModeENS0_7RunModeE',
        mode.value,
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
    'Qt3DCore::QAspectEngine::QAspectEngine(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectengine.html#QAspectEngine

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DCore::QAspectEngine::QAspectEngine(QObject *parent)
    self._noteCreation(QAspectEngine, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore13QAspectEngineC1EP7QObject',
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

  @overload(WAIT['Qt3DCore.QAbstractAspect'])
  @overload(NoneType)
  def registerAspect(
      self,
      aspect: Optional[Qt3DCore.QAbstractAspect],
  ) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAspectEngine::registerAspect(QAbstractAspect
    *aspect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectengine.html#registerAspect

    Parameters
    ----------

    aspect : Optional[Qt3DCore.QAbstractAspect]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QAspectEngine::registerAspect(QAbstractAspect *aspect)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore13QAspectEngine14registerAspectEPNS_15QAbstractA'
        'spectE',
        self._addressOf(aspect),
    )

  @overload(str)
  def registerAspect(self, name: str) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAspectEngine::registerAspect(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectengine.html#registerAspect

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DCore::QAspectEngine::registerAspect(const QString &name)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore13QAspectEngine14registerAspectERK7QString', name,
    )

  @overload(WAIT['Qt3DCore.QAbstractAspect'])
  @overload(NoneType)
  def unregisterAspect(
      self,
      aspect: Optional[Qt3DCore.QAbstractAspect],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::QAspectEngine::unregisterAspect(QAbstractAspect *aspect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectengine.html#unregisterAspect

    Parameters
    ----------

    aspect : Optional[Qt3DCore.QAbstractAspect]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QAspectEngine::unregisterAspect(QAbstractAspect
    #      *aspect)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore13QAspectEngine16unregisterAspectEPNS_15QAbstrac'
        'tAspectE',
        self._addressOf(aspect),
    )

  @overload(str)
  def unregisterAspect(self, name: str) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAspectEngine::unregisterAspect(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectengine.html#unregisterAspect

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DCore::QAspectEngine::unregisterAspect(const QString &name)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore13QAspectEngine16unregisterAspectERK7QString',
        name,
    )

  @overload(str)
  def executeCommand(self, command: str) -> QVariant:
    """
    Calls Qt's 'QVariant Qt3DCore::QAspectEngine::executeCommand(const
    QString &command)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectengine.html#executeCommand

    Parameters
    ----------

    command : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant Qt3DCore::QAspectEngine::executeCommand(const QString
    #      &command)
    address = self.uglySide.call(
        'ritual_ZN8Qt3DCore13QAspectEngine14executeCommandERK7QString',
        command,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def processFrame(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAspectEngine::processFrame()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectengine.html#processFrame
    """
    #  void Qt3DCore::QAspectEngine::processFrame()
    self.uglySide.call('ritual_ZN8Qt3DCore13QAspectEngine12processFrameEv')

  def d_func(self) -> Optional[Qt3DCore.QAspectEnginePrivate]:
    """
    Calls Qt's 'QAspectEnginePrivate *Qt3DCore::QAspectEngine::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qaspectengine.html#d_func

    Returns
    -------

    Optional[Qt3DCore.QAspectEnginePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAspectEnginePrivate *Qt3DCore::QAspectEngine::d_func()
    address = self.uglySide.call(
        'ritual_ZN8Qt3DCore13QAspectEngine6d_funcEv',
    )
    return Qt3DCore.QAspectEnginePrivate._cuteAt(address)

  @staticmethod
  def aspects(*__, **_) -> Never:
    """
    Qt's 'QList<QAbstractAspect *> Qt3DCore::QAspectEngine::aspects() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QAspectEngine.aspects' has no cute function yet. Qt's "
        "'QList<QAbstractAspect *> Qt3DCore::QAspectEngine::aspects() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def lookupNodes(*__, **_) -> Never:
    """
    Qt's 'QList<QNode *> Qt3DCore::QAspectEngine::lookupNodes(const
    QList<QNodeId> &ids) const': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QAspectEngine.lookupNodes' has no cute function yet. "
        "Qt's 'QList<QNode *> Qt3DCore::QAspectEngine::lookupNodes(const "
        "QList<QNodeId> &ids) const': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def rootEntity(*__, **_) -> Never:
    """
    Qt's 'QEntityPtr Qt3DCore::QAspectEngine::rootEntity() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QAspectEngine.rootEntity' has no cute function yet. Qt's "
        "'QEntityPtr Qt3DCore::QAspectEngine::rootEntity() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def setRootEntity(*__, **_) -> Never:
    """
    Qt's 'void Qt3DCore::QAspectEngine::setRootEntity(QEntityPtr root)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QAspectEngine.setRootEntity' has no cute function yet. "
        "Qt's 'void Qt3DCore::QAspectEngine::setRootEntity(QEntityPtr "
        "root)': takes a type Python has no way to hand over yet.")
