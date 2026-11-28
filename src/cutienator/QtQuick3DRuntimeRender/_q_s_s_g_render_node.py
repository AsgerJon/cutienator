"""
QSSGRenderNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendernode_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRenderNode to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QSSGRenderGraphObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtGui import QMatrix4x4, QQuaternion, QVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMatrix4x4 = WAIT['QMatrix4x4']
  QQuaternion = WAIT['QQuaternion']
  QVector3D = WAIT['QVector3D']


class QSSGRenderNode(QSSGRenderGraphObject):
  """
  The cute side of Qt's QSSGRenderNode: a plain Python object standing in
  front of one C++ QSSGRenderNode.

  It is built on the cute 'QSSGRenderGraphObject', as Qt's QSSGRenderNode is
  built on Qt's QSSGRenderGraphObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSSGRenderNode that has a ritual and that Python can
  call so far, 12 names in all: 'markDirty', 'clearDirty', 'isDirty',
  'setState', 'getLocalState', 'getGlobalState', 'removeFromGraph',
  'calculateTransformMatrix', 'getGlobalPos', 'getDirection',
  'getScalingCorrectDirection', 'signedSquared'. It can be made from Python,
  in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGRenderNode::~QSSGRenderNode()': the destructor: Python never
    removes a C++ QSSGRenderNode.
  - Qt's 'void QSSGRenderNode::addChild(QSSGRenderNode &inChild)': takes a
    type Python has no way to hand over yet.
  - Qt's 'void QSSGRenderNode::removeChild(QSSGRenderNode &inChild)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QSSGBounds3 QSSGRenderNode::getBounds(QSSGBufferManager &inManager,
    bool inIncludeChildren) const': takes a type Python has no way to hand
    over yet.
  - Qt's 'QSSGBounds3 QSSGRenderNode::getChildBounds(QSSGBufferManager
    &inManager) const': takes a type Python has no way to hand over yet.
  - Qt's 'void QSSGRenderNode::calculateMVP(const QMatrix4x4
    &globalTransform, const QMatrix4x4 &inViewProjection, QMatrix4x4
    &outMVP)': takes a type Python has no way to hand over yet.
  - Qt's 'void QSSGRenderNode::calculateNormalMatrix(const QMatrix4x4
    &globalTransform, QMatrix3x3 &outNormalMatrix)': takes a type Python has
    no way to hand over yet.
  - Qt's 'void QSSGRenderNode::calculateMVPAndNormalMatrix(const QMatrix4x4
    &globalTransfor, const QMatrix4x4 &inViewProjection, QMatrix4x4 &outMVP,
    QMatrix3x3 &outNormalMatrix)': takes a type Python has no way to hand
    over yet.

  What to expect
  --------------

  - The C++ QSSGRenderNode is created at the first use, not by
    'QSSGRenderNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGRenderNode.
  - Each name of Qt's QSSGRenderNode that has no cute function yet,
    'addChild', 'calculateMVP', 'calculateMVPAndNormalMatrix',
    'calculateNormalMatrix', 'getBounds', 'getChildBounds', 'removeChild',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QSSGRenderNode, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class DirtyFlag(CuteNum, scoped=True):
    """
    The enum 'QSSGRenderNode::DirtyFlag' of Qt, with the 11 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    TransformDirty = Kee[int](64)
    OpacityDirty = Kee[int](128)
    ActiveDirty = Kee[int](256)
    PickableDirty = Kee[int](512)
    TagDirty = Kee[int](1024)
    ImportDirty = Kee[int](2048)
    SubNodeDirty = Kee[int](4096)
    StickyDirty = Kee[int](8192)
    GlobalValuesDirty = Kee[int](3008)
    SubtreeUpdateMask = Kee[int](11200)
    DirtyMask = Kee[int](7104)

  class GlobalState(CuteNum, scoped=True):
    """
    The enum 'QSSGRenderNode::GlobalState' of Qt, with the 3 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Active = Kee[int](8)
    Pickable = Kee[int](16)
    Imported = Kee[int](32)

  class LocalState(CuteNum, scoped=True):
    """
    The enum 'QSSGRenderNode::LocalState' of Qt, with the 3 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Active = Kee[int](1)
    Pickable = Kee[int](2)
    Imported = Kee[int](4)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QVector3D, QVector3D, QVector3D, QQuaternion)
  def calculateTransformMatrix(
      position: QVector3D,
      scale: QVector3D,
      pivot: QVector3D,
      rotation: QQuaternion,
  ) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4 QSSGRenderNode::calculateTransformMatrix(QVector3D
    position, QVector3D scale, QVector3D pivot, QQuaternion rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendernode.html#calculateTransformMatrix

    Parameters
    ----------

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    scale : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    pivot : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    rotation : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 QSSGRenderNode::calculateTransformMatrix(QVector3D
    #      position, QVector3D scale, QVector3D pivot, QQuaternion rotation)
    address = Rituals.call(
        'ritual_ZN14QSSGRenderNode24calculateTransformMatrixE9QVector3DS0_S'
        '0_11QQuaternion',
        CuteMixin._valueOf(position), CuteMixin._valueOf(scale),
        CuteMixin._valueOf(pivot), CuteMixin._valueOf(rotation),
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  @staticmethod
  @overload(QMatrix4x4)
  def getGlobalPos(globalTransform: QMatrix4x4) -> QVector3D:
    """
    Calls Qt's 'QVector3D QSSGRenderNode::getGlobalPos(const QMatrix4x4
    &globalTransform)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrendernode.html#getGlobalPos

    Parameters
    ----------

    globalTransform : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QSSGRenderNode::getGlobalPos(const QMatrix4x4
    #      &globalTransform)
    address = Rituals.call(
        'ritual_ZN14QSSGRenderNode12getGlobalPosERK10QMatrix4x4',
        CuteMixin._valueOf(globalTransform),
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @staticmethod
  @overload(QMatrix4x4)
  def getDirection(globalTransform: QMatrix4x4) -> QVector3D:
    """
    Calls Qt's 'QVector3D QSSGRenderNode::getDirection(const QMatrix4x4
    &globalTransform)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrendernode.html#getDirection

    Parameters
    ----------

    globalTransform : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QSSGRenderNode::getDirection(const QMatrix4x4
    #      &globalTransform)
    address = Rituals.call(
        'ritual_ZN14QSSGRenderNode12getDirectionERK10QMatrix4x4',
        CuteMixin._valueOf(globalTransform),
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @staticmethod
  @overload(QMatrix4x4)
  def getScalingCorrectDirection(globalTransform: QMatrix4x4) -> QVector3D:
    """
    Calls Qt's 'QVector3D QSSGRenderNode::getScalingCorrectDirection(const
    QMatrix4x4 &globalTransform)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendernode.html#getScalingCorrectDirection

    Parameters
    ----------

    globalTransform : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QSSGRenderNode::getScalingCorrectDirection(const QMatrix4x4
    #      &globalTransform)
    address = Rituals.call(
        'ritual_ZN14QSSGRenderNode26getScalingCorrectDirectionERK10QMatrix4'
        'x4',
        CuteMixin._valueOf(globalTransform),
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @staticmethod
  @overload(float)
  def signedSquared(val: float) -> float:
    """
    Calls Qt's 'float QSSGRenderNode::signedSquared(float val)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrendernode.html#signedSquared

    Parameters
    ----------

    val : float
      Passed on as it is.
    """
    #  float QSSGRenderNode::signedSquared(float val)
    return Rituals.call('ritual_ZN14QSSGRenderNode13signedSquaredEf', val)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRenderNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(DirtyFlag)
  def isDirty(self, dirtyFlag: DirtyFlag = DirtyFlag.DirtyMask) -> bool:
    """
    Calls Qt's 'bool QSSGRenderNode::isDirty(DirtyFlag dirtyFlag) const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrendernode.html#isDirty

    Parameters
    ----------

    dirtyFlag : DirtyFlag
      Passed on as its number. May be left out, as in Qt: it is then
      DirtyFlag.DirtyMask.
    """
    #  bool QSSGRenderNode::isDirty(DirtyFlag dirtyFlag) const
    return self.uglySide.call(
        'ritual_ZNK14QSSGRenderNode7isDirtyENS_9DirtyFlagE', dirtyFlag.value,
    )

  @overload(LocalState)
  def getLocalState(self, stateFlag: LocalState) -> bool:
    """
    Calls Qt's 'bool QSSGRenderNode::getLocalState(LocalState stateFlag)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrendernode.html#getLocalState

    Parameters
    ----------

    stateFlag : LocalState
      Passed on as its number.
    """
    #  bool QSSGRenderNode::getLocalState(LocalState stateFlag) const
    return self.uglySide.call(
        'ritual_ZNK14QSSGRenderNode13getLocalStateENS_10LocalStateE',
        stateFlag.value,
    )

  @overload(GlobalState)
  def getGlobalState(self, stateFlag: GlobalState) -> bool:
    """
    Calls Qt's 'bool QSSGRenderNode::getGlobalState(GlobalState stateFlag)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrendernode.html#getGlobalState

    Parameters
    ----------

    stateFlag : GlobalState
      Passed on as its number.
    """
    #  bool QSSGRenderNode::getGlobalState(GlobalState stateFlag) const
    return self.uglySide.call(
        'ritual_ZNK14QSSGRenderNode14getGlobalStateENS_11GlobalStateE',
        stateFlag.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(LocalState)
  @overload(LocalState, bool)
  def setState(self, state: LocalState, on: bool = True) -> None:
    """
    Calls Qt's 'void QSSGRenderNode::setState(LocalState state, bool on)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrendernode.html#setState

    Parameters
    ----------

    state : LocalState
      Passed on as its number.

    on : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QSSGRenderNode::setState(LocalState state, bool on)
    self.uglySide.call(
        'ritual_ZN14QSSGRenderNode8setStateENS_10LocalStateEb',
        state.value, on,
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QSSGRenderNode::QSSGRenderNode()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qssgrendernode.html#QSSGRenderNode
    """
    #  QSSGRenderNode::QSSGRenderNode()
    self._noteCreation(QSSGRenderNode, lambda: Rituals.call(
        'ritual_ZN14QSSGRenderNodeC1Ev',
    ))

  @overload(QSSGRenderGraphObject.Type)
  @overload(QSSGRenderGraphObject.Type, int)
  def __init__(
      self,
      type: QSSGRenderGraphObject.Type,
      flags: int = 0,
  ) -> None:
    """
    Notes what was given, for Qt's 'QSSGRenderNode::QSSGRenderNode(Type type,
    FlagT flags)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qssgrendernode.html#QSSGRenderNode

    Parameters
    ----------

    type : QSSGRenderGraphObject.Type
      Passed on as its number.

    flags : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  QSSGRenderNode::QSSGRenderNode(Type type, FlagT flags)
    self._noteCreation(QSSGRenderNode, lambda: Rituals.call(
        'ritual_ZN14QSSGRenderNodeC1EN21QSSGRenderGraphObject4TypeEj',
        type.value, flags,
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

  @overload(DirtyFlag)
  def markDirty(self, dirtyFlag: DirtyFlag) -> None:
    """
    Calls Qt's 'void QSSGRenderNode::markDirty(DirtyFlag dirtyFlag)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrendernode.html#markDirty

    Parameters
    ----------

    dirtyFlag : DirtyFlag
      Passed on as its number.
    """
    #  void QSSGRenderNode::markDirty(DirtyFlag dirtyFlag)
    self.uglySide.call(
        'ritual_ZN14QSSGRenderNode9markDirtyENS_9DirtyFlagE',
        dirtyFlag.value,
    )

  @overload(DirtyFlag)
  def clearDirty(self, dirtyFlag: DirtyFlag) -> None:
    """
    Calls Qt's 'void QSSGRenderNode::clearDirty(DirtyFlag dirtyFlag)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrendernode.html#clearDirty

    Parameters
    ----------

    dirtyFlag : DirtyFlag
      Passed on as its number.
    """
    #  void QSSGRenderNode::clearDirty(DirtyFlag dirtyFlag)
    self.uglySide.call(
        'ritual_ZN14QSSGRenderNode10clearDirtyENS_9DirtyFlagE',
        dirtyFlag.value,
    )

  def removeFromGraph(self) -> None:
    """
    Calls Qt's 'void QSSGRenderNode::removeFromGraph()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendernode.html#removeFromGraph
    """
    #  void QSSGRenderNode::removeFromGraph()
    self.uglySide.call('ritual_ZN14QSSGRenderNode15removeFromGraphEv')

  @staticmethod
  def addChild(*__, **_) -> Never:
    """
    Qt's 'void QSSGRenderNode::addChild(QSSGRenderNode &inChild)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderNode.addChild' has no cute function yet. Qt's 'void "
        "QSSGRenderNode::addChild(QSSGRenderNode &inChild)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def calculateMVP(*__, **_) -> Never:
    """
    Qt's 'void QSSGRenderNode::calculateMVP(const QMatrix4x4
    &globalTransform, const QMatrix4x4 &inViewProjection, QMatrix4x4
    &outMVP)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderNode.calculateMVP' has no cute function yet. Qt's 'void "
        "QSSGRenderNode::calculateMVP(const QMatrix4x4 &globalTransform, "
        "const QMatrix4x4 &inViewProjection, QMatrix4x4 &outMVP)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def calculateMVPAndNormalMatrix(*__, **_) -> Never:
    """
    Qt's 'void QSSGRenderNode::calculateMVPAndNormalMatrix(const QMatrix4x4
    &globalTransfor, const QMatrix4x4 &inViewProjection, QMatrix4x4 &outMVP,
    QMatrix3x3 &outNormalMatrix)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderNode.calculateMVPAndNormalMatrix' has no cute function "
        "yet. Qt's 'void QSSGRenderNode::calculateMVPAndNormalMatrix(const "
        "QMatrix4x4 &globalTransfor, const QMatrix4x4 &inViewProjection, "
        "QMatrix4x4 &outMVP, QMatrix3x3 &outNormalMatrix)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def calculateNormalMatrix(*__, **_) -> Never:
    """
    Qt's 'void QSSGRenderNode::calculateNormalMatrix(const QMatrix4x4
    &globalTransform, QMatrix3x3 &outNormalMatrix)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderNode.calculateNormalMatrix' has no cute function yet. "
        "Qt's 'void QSSGRenderNode::calculateNormalMatrix(const QMatrix4x4 "
        "&globalTransform, QMatrix3x3 &outNormalMatrix)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def getBounds(*__, **_) -> Never:
    """
    Qt's 'QSSGBounds3 QSSGRenderNode::getBounds(QSSGBufferManager &inManager,
    bool inIncludeChildren) const': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderNode.getBounds' has no cute function yet. Qt's "
        "'QSSGBounds3 QSSGRenderNode::getBounds(QSSGBufferManager "
        "&inManager, bool inIncludeChildren) const': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def getChildBounds(*__, **_) -> Never:
    """
    Qt's 'QSSGBounds3 QSSGRenderNode::getChildBounds(QSSGBufferManager
    &inManager) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderNode.getChildBounds' has no cute function yet. Qt's "
        "'QSSGBounds3 QSSGRenderNode::getChildBounds(QSSGBufferManager "
        "&inManager) const': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def removeChild(*__, **_) -> Never:
    """
    Qt's 'void QSSGRenderNode::removeChild(QSSGRenderNode &inChild)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderNode.removeChild' has no cute function yet. Qt's 'void "
        "QSSGRenderNode::removeChild(QSSGRenderNode &inChild)': takes a "
        "type Python has no way to hand over yet.")
