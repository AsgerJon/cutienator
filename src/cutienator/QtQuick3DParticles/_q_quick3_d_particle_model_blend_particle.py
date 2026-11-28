"""
QQuick3DParticleModelBlendParticle binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticlemodelblendparticle_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DParticleModelBlendParticle to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtQuick3D import QQuick3DObject
from . import QQuick3DParticle

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QMatrix4x4, QVector3D, QVector4D
  from ..QtQml import QQmlComponent
  from ..QtQuick3DRuntimeRender import QSSGParticleBuffer
  from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
  from ..QtQuick3D import QQuick3DNode
  from . import QQuick3DParticleEmitter
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMatrix4x4 = WAIT['QMatrix4x4']
  QQmlComponent = WAIT['QQmlComponent']
  QQuick3DNode = WAIT['QQuick3DNode']
  QQuick3DParticleEmitter = WAIT['QQuick3DParticleEmitter']
  QSSGParticleBuffer = WAIT['QSSGParticleBuffer']
  QSSGRenderGraphObject = WAIT['QSSGRenderGraphObject']
  QVector3D = WAIT['QVector3D']
  QVector4D = WAIT['QVector4D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DParticleModelBlendParticle(QQuick3DParticle):
  """
  The cute side of Qt's QQuick3DParticleModelBlendParticle: a plain Python
  object standing in front of one C++ QQuick3DParticleModelBlendParticle.

  It is built on the cute 'QQuick3DParticle', as Qt's
  QQuick3DParticleModelBlendParticle is built on Qt's QQuick3DParticle, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DParticleModelBlendParticle that has a ritual
  and that Python can call so far, 38 names in all: 'metaObject', 'tr',
  'delegate', 'endNode', 'modelBlendMode', 'endTime', 'activationNode',
  'emitMode', 'setDelegate', 'setEndNode', 'setEndTime', 'setModelBlendMode',
  'setActivationNode', 'setEmitMode', 'delegateChanged',
  'blendFactorChanged', 'endNodeChanged', 'modelBlendModeChanged',
  'endTimeChanged', 'activationNodeChanged', 'emitModeChanged', 'itemChange',
  'reset', 'lastParticle', 'doSetMaxAmount', 'componentComplete',
  'nextCurrentIndex', 'setParticleData', 'particleCenter',
  'particleEndPosition', 'particleEndRotation', 'randomIndex',
  'commitParticles', 'updateSpatialNode', 'updateParticleBuffer',
  'regenerate', 'updateParticles', 'handleEndNodeChanged'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DParticleModelBlendParticle::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QQuick3DParticleModelBlendParticle::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's
    'QQuick3DParticleModelBlendParticle::~QQuick3DParticleModelBlendParticle(
    )': the destructor: Python never removes a C++
    QQuick3DParticleModelBlendParticle.
  - Qt's 'PerEmitterData
    &QQuick3DParticleModelBlendParticle::perEmitterData(int emitterIndex)':
    gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 45 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DParticleModelBlendParticle is created at the first use,
    not by 'QQuick3DParticleModelBlendParticle(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DParticleModelBlendParticle.
  - Qt tells when it has removed the C++ QQuick3DParticleModelBlendParticle.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DParticleModelBlendParticle that has no cute
    function yet, 'perEmitterData', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuick3DParticleModelBlendParticle, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class ModelBlendEmitMode(CuteNum):
    """
    The enum 'QQuick3DParticleModelBlendParticle::ModelBlendEmitMode' of Qt,
    with the 3 names Qt gives in it.
    """

    Sequential = Kee[int](0)
    Random = Kee[int](1)
    Activation = Kee[int](2)

  class ModelBlendMode(CuteNum):
    """
    The enum 'QQuick3DParticleModelBlendParticle::ModelBlendMode' of Qt, with
    the 3 names Qt gives in it.
    """

    Explode = Kee[int](0)
    Construct = Kee[int](1)
    Transfer = Kee[int](2)

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
    Calls Qt's 'QString QQuick3DParticleModelBlendParticle::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelblendparticle.html#tr

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
    #  QString QQuick3DParticleModelBlendParticle::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN34QQuick3DParticleModelBlendParticle2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DParticleModelBlendParticle'

  #  A C++ QQuick3DParticleModelBlendParticle Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DParticleModelBlendParticle'

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
    *QQuick3DParticleModelBlendParticle::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelblendparticle.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DParticleModelBlendParticle::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK34QQuick3DParticleModelBlendParticle10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def delegate(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQuick3DParticleModelBlendParticle::delegate()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelblendparticle.html#delegate

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQuick3DParticleModelBlendParticle::delegate() const
    address = self.uglySide.call(
        'ritual_ZNK34QQuick3DParticleModelBlendParticle8delegateEv',
    )
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def endNode(self) -> Optional[QQuick3DNode]:
    """
    Calls Qt's 'QQuick3DNode *QQuick3DParticleModelBlendParticle::endNode()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelblendparticle.html#endNode

    Returns
    -------

    Optional[QQuick3DNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DNode *QQuick3DParticleModelBlendParticle::endNode() const
    address = self.uglySide.call(
        'ritual_ZNK34QQuick3DParticleModelBlendParticle7endNodeEv',
    )
    from ..QtQuick3D import QQuick3DNode
    return QQuick3DNode._cuteAt(address)

  def modelBlendMode(self) -> ModelBlendMode:
    """
    Calls Qt's 'ModelBlendMode
    QQuick3DParticleModelBlendParticle::modelBlendMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelblendparticle.html

    Returns
    -------

    ModelBlendMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ModelBlendMode(number)'
      gives.
    """
    #  ModelBlendMode QQuick3DParticleModelBlendParticle::modelBlendMode()
    #      const
    return QQuick3DParticleModelBlendParticle.ModelBlendMode(
        self.uglySide.call(
            'ritual_ZNK34QQuick3DParticleModelBlendParticle14modelBlendMode'
            'Ev',
        ))

  def endTime(self) -> int:
    """
    Calls Qt's 'int QQuick3DParticleModelBlendParticle::endTime() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelblendparticle.html#endTime
    """
    #  int QQuick3DParticleModelBlendParticle::endTime() const
    return self.uglySide.call(
        'ritual_ZNK34QQuick3DParticleModelBlendParticle7endTimeEv',
    )

  def activationNode(self) -> Optional[QQuick3DNode]:
    """
    Calls Qt's 'QQuick3DNode
    *QQuick3DParticleModelBlendParticle::activationNode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelblendparticle.html

    Returns
    -------

    Optional[QQuick3DNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DNode *QQuick3DParticleModelBlendParticle::activationNode()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK34QQuick3DParticleModelBlendParticle14activationNodeEv',
    )
    from ..QtQuick3D import QQuick3DNode
    return QQuick3DNode._cuteAt(address)

  def emitMode(self) -> ModelBlendEmitMode:
    """
    Calls Qt's 'ModelBlendEmitMode
    QQuick3DParticleModelBlendParticle::emitMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelblendparticle.html#emitMode

    Returns
    -------

    ModelBlendEmitMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'ModelBlendEmitMode(number)' gives.
    """
    #  ModelBlendEmitMode QQuick3DParticleModelBlendParticle::emitMode()
    #      const
    return QQuick3DParticleModelBlendParticle.ModelBlendEmitMode(
        self.uglySide.call(
            'ritual_ZNK34QQuick3DParticleModelBlendParticle8emitModeEv',
        ))

  def lastParticle(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DParticleModelBlendParticle::lastParticle()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelblendparticle.html
    """
    #  bool QQuick3DParticleModelBlendParticle::lastParticle() const
    return self.uglySide.call(
        'ritual_ZNK34QQuick3DParticleModelBlendParticle12lastParticleEv',
    )

  @overload(int)
  def particleCenter(self, particleIndex: int) -> QVector3D:
    """
    Calls Qt's 'QVector3D
    QQuick3DParticleModelBlendParticle::particleCenter(int particleIndex)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelblendparticle.html

    Parameters
    ----------

    particleIndex : int
      Passed on as it is.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DParticleModelBlendParticle::particleCenter(int
    #      particleIndex) const
    address = self.uglySide.call(
        'ritual_ZNK34QQuick3DParticleModelBlendParticle14particleCenterEi',
        particleIndex,
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(int)
  def particleEndPosition(self, particleIndex: int) -> QVector3D:
    """
    Calls Qt's 'QVector3D
    QQuick3DParticleModelBlendParticle::particleEndPosition(int
    particleIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelblendparticle.html

    Parameters
    ----------

    particleIndex : int
      Passed on as it is.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DParticleModelBlendParticle::particleEndPosition(int
    #      particleIndex) const
    address = self.uglySide.call(
        'ritual_ZNK34QQuick3DParticleModelBlendParticle19particleEndPositio'
        'nEi',
        particleIndex,
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(int)
  def particleEndRotation(self, particleIndex: int) -> QVector3D:
    """
    Calls Qt's 'QVector3D
    QQuick3DParticleModelBlendParticle::particleEndRotation(int
    particleIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelblendparticle.html

    Parameters
    ----------

    particleIndex : int
      Passed on as it is.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DParticleModelBlendParticle::particleEndRotation(int
    #      particleIndex) const
    address = self.uglySide.call(
        'ritual_ZNK34QQuick3DParticleModelBlendParticle19particleEndRotatio'
        'nEi',
        particleIndex,
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQmlComponent)
  @overload(NoneType)
  def setDelegate(self, setDelegate: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleModelBlendParticle::setDelegate(QQmlComponent
    *setDelegate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelblendparticle.html

    Parameters
    ----------

    setDelegate : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DParticleModelBlendParticle::setDelegate(QQmlComponent
    #      *setDelegate)
    self.uglySide.call(
        'ritual_ZN34QQuick3DParticleModelBlendParticle11setDelegateEP13QQml'
        'Component',
        self._addressOf(setDelegate),
    )

  @overload(QQuick3DNode)
  @overload(NoneType)
  def setEndNode(self, endNode: Optional[QQuick3DNode]) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleModelBlendParticle::setEndNode(QQuick3DNode *endNode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelblendparticle.html#setEndNode

    Parameters
    ----------

    endNode : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DParticleModelBlendParticle::setEndNode(QQuick3DNode
    #      *endNode)
    self.uglySide.call(
        'ritual_ZN34QQuick3DParticleModelBlendParticle10setEndNodeEP12QQuic'
        'k3DNode',
        self._addressOf(endNode),
    )

  @overload(int)
  def setEndTime(self, endTime: int) -> None:
    """
    Calls Qt's 'void QQuick3DParticleModelBlendParticle::setEndTime(int
    endTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelblendparticle.html#setEndTime

    Parameters
    ----------

    endTime : int
      Passed on as it is.
    """
    #  void QQuick3DParticleModelBlendParticle::setEndTime(int endTime)
    self.uglySide.call(
        'ritual_ZN34QQuick3DParticleModelBlendParticle10setEndTimeEi',
        endTime,
    )

  @overload(ModelBlendMode)
  def setModelBlendMode(self, mode: ModelBlendMode) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleModelBlendParticle::setModelBlendMode(ModelBlendMode
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelblendparticle.html

    Parameters
    ----------

    mode : ModelBlendMode
      Passed on as its number.
    """
    #  void QQuick3DParticleModelBlendParticle::setModelBlendMode(
    #      ModelBlendMode mode)
    self.uglySide.call(
        'ritual_ZN34QQuick3DParticleModelBlendParticle17setModelBlendModeEN'
        'S_14ModelBlendModeE',
        mode.value,
    )

  @overload(QQuick3DNode)
  @overload(NoneType)
  def setActivationNode(
      self,
      activationNode: Optional[QQuick3DNode],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleModelBlendParticle::setActivationNode(QQuick3DNode
    *activationNode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelblendparticle.html

    Parameters
    ----------

    activationNode : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      QQuick3DParticleModelBlendParticle::setActivationNode(QQuick3DNode
    #      *activationNode)
    self.uglySide.call(
        'ritual_ZN34QQuick3DParticleModelBlendParticle17setActivationNodeEP'
        '12QQuick3DNode',
        self._addressOf(activationNode),
    )

  @overload(ModelBlendEmitMode)
  def setEmitMode(self, emitMode: ModelBlendEmitMode) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleModelBlendParticle::setEmitMode(ModelBlendEmitMode
    emitMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelblendparticle.html

    Parameters
    ----------

    emitMode : ModelBlendEmitMode
      Passed on as its number.
    """
    #  void
    #      QQuick3DParticleModelBlendParticle::setEmitMode(ModelBlendEmitMode
    #      emitMode)
    self.uglySide.call(
        'ritual_ZN34QQuick3DParticleModelBlendParticle11setEmitModeENS_18Mo'
        'delBlendEmitModeE',
        emitMode.value,
    )

  @overload(int, QVector3D, QVector3D, QVector4D, float, float)
  def setParticleData(
      self,
      particleIndex: int,
      position: QVector3D,
      rotation: QVector3D,
      color: QVector4D,
      size: float,
      age: float,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DParticleModelBlendParticle::setParticleData(int
    particleIndex, const QVector3D &position, const QVector3D &rotation,
    const QVector4D &color, float size, float age)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelblendparticle.html

    Parameters
    ----------

    particleIndex : int
      Passed on as it is.

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    rotation : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    color : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.

    size : float
      Passed on as it is.

    age : float
      Passed on as it is.
    """
    #  void QQuick3DParticleModelBlendParticle::setParticleData(int
    #      particleIndex, const QVector3D &position, const QVector3D
    #      &rotation, const QVector4D &color, float size, float age)
    self.uglySide.call(
        'ritual_ZN34QQuick3DParticleModelBlendParticle15setParticleDataEiRK'
        '9QVector3DS2_RK9QVector4Dff',
        particleIndex, self._valueOf(position), self._valueOf(rotation),
        self._valueOf(color), size, age,
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
  @overload(QQuick3DNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuick3DNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DParticleModelBlendParticle::QQuick3DParticleModelBlendParticle(
    QQuick3DNode *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelblendparticle.html

    Parameters
    ----------

    parent : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DParticleModelBlendParticle::
    #      QQuick3DParticleModelBlendParticle(QQuick3DNode *parent)
    self._noteCreation(
        QQuick3DParticleModelBlendParticle, lambda: Rituals.call(
            'ritual_ZN34QQuick3DParticleModelBlendParticleC1EP12QQuick3DNod'
            'e',
            self._addressOf(parent),
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

  def delegateChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleModelBlendParticle::delegateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelblendparticle.html
    """
    #  void QQuick3DParticleModelBlendParticle::delegateChanged()
    self.uglySide.call(
        'ritual_ZN34QQuick3DParticleModelBlendParticle15delegateChangedEv',
    )

  def blendFactorChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleModelBlendParticle::blendFactorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelblendparticle.html
    """
    #  void QQuick3DParticleModelBlendParticle::blendFactorChanged()
    self.uglySide.call(
        'ritual_ZN34QQuick3DParticleModelBlendParticle18blendFactorChangedE'
        'v',
    )

  def endNodeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleModelBlendParticle::endNodeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelblendparticle.html
    """
    #  void QQuick3DParticleModelBlendParticle::endNodeChanged()
    self.uglySide.call(
        'ritual_ZN34QQuick3DParticleModelBlendParticle14endNodeChangedEv',
    )

  def modelBlendModeChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleModelBlendParticle::modelBlendModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelblendparticle.html
    """
    #  void QQuick3DParticleModelBlendParticle::modelBlendModeChanged()
    self.uglySide.call(
        'ritual_ZN34QQuick3DParticleModelBlendParticle21modelBlendModeChang'
        'edEv',
    )

  def endTimeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleModelBlendParticle::endTimeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelblendparticle.html
    """
    #  void QQuick3DParticleModelBlendParticle::endTimeChanged()
    self.uglySide.call(
        'ritual_ZN34QQuick3DParticleModelBlendParticle14endTimeChangedEv',
    )

  def activationNodeChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleModelBlendParticle::activationNodeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelblendparticle.html
    """
    #  void QQuick3DParticleModelBlendParticle::activationNodeChanged()
    self.uglySide.call(
        'ritual_ZN34QQuick3DParticleModelBlendParticle21activationNodeChang'
        'edEv',
    )

  def emitModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleModelBlendParticle::emitModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelblendparticle.html
    """
    #  void QQuick3DParticleModelBlendParticle::emitModeChanged()
    self.uglySide.call(
        'ritual_ZN34QQuick3DParticleModelBlendParticle15emitModeChangedEv',
    )

  @overload(QQuick3DObject.ItemChange, QQuick3DObject.ItemChangeData)
  def itemChange(
      self,
      a0: QQuick3DObject.ItemChange,
      a1: QQuick3DObject.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleModelBlendParticle::itemChange(ItemChange a0, const
    ItemChangeData &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelblendparticle.html#itemChange

    Parameters
    ----------

    a0 : QQuick3DObject.ItemChange
      Passed on as its number.

    a1 : QQuick3DObject.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuick3DObject::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuick3DParticleModelBlendParticle::itemChange(ItemChange a0,
    #      const ItemChangeData &a1)
    ritual = (
        'ritual_ZN34QQuick3DParticleModelBlendParticle10itemChangeEN14QQuic'
        'k3DObject10ItemChangeERKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN34QQuick3DParticleModelBlendParticle10itemChangeEN1'
          '4QQuick3DObject10ItemChangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, a0.value, self._valueOf(a1))

  def reset(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleModelBlendParticle::reset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelblendparticle.html#reset
    """
    #  void QQuick3DParticleModelBlendParticle::reset()
    ritual = 'ritual_ZN34QQuick3DParticleModelBlendParticle5resetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN34QQuick3DParticleModelBlendParticle5resetEv'
    self.uglySide.call(ritual)

  @overload(int)
  def doSetMaxAmount(self, amount: int) -> None:
    """
    Calls Qt's 'void QQuick3DParticleModelBlendParticle::doSetMaxAmount(int
    amount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelblendparticle.html

    Parameters
    ----------

    amount : int
      Passed on as it is.
    """
    #  void QQuick3DParticleModelBlendParticle::doSetMaxAmount(int amount)
    ritual = (
        'ritual_ZN34QQuick3DParticleModelBlendParticle14doSetMaxAmountEi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN34QQuick3DParticleModelBlendParticle14doSetMaxAmoun'
          'tEi')
    self.uglySide.call(ritual, amount)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleModelBlendParticle::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelblendparticle.html
    """
    #  void QQuick3DParticleModelBlendParticle::componentComplete()
    ritual = (
        'ritual_ZN34QQuick3DParticleModelBlendParticle17componentCompleteEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN34QQuick3DParticleModelBlendParticle17componentComp'
          'leteEv')
    self.uglySide.call(ritual)

  @overload(QQuick3DParticleEmitter)
  @overload(NoneType)
  def nextCurrentIndex(
      self,
      emitter: Optional[QQuick3DParticleEmitter],
  ) -> int:
    """
    Calls Qt's 'int
    QQuick3DParticleModelBlendParticle::nextCurrentIndex(const
    QQuick3DParticleEmitter *emitter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelblendparticle.html

    Parameters
    ----------

    emitter : Optional[QQuick3DParticleEmitter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QQuick3DParticleModelBlendParticle::nextCurrentIndex(const
    #      QQuick3DParticleEmitter *emitter)
    ritual = (
        'ritual_ZN34QQuick3DParticleModelBlendParticle16nextCurrentIndexEPK'
        '23QQuick3DParticleEmitter')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN34QQuick3DParticleModelBlendParticle16nextCurrentIn'
          'dexEPK23QQuick3DParticleEmitter')
    return self.uglySide.call(ritual, self._addressOf(emitter))

  @overload(int)
  def randomIndex(self, particleIndex: int) -> int:
    """
    Calls Qt's 'int QQuick3DParticleModelBlendParticle::randomIndex(int
    particleIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelblendparticle.html

    Parameters
    ----------

    particleIndex : int
      Passed on as it is.
    """
    #  int QQuick3DParticleModelBlendParticle::randomIndex(int particleIndex)
    return self.uglySide.call(
        'ritual_ZN34QQuick3DParticleModelBlendParticle11randomIndexEi',
        particleIndex,
    )

  def commitParticles(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleModelBlendParticle::commitParticles()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelblendparticle.html
    """
    #  void QQuick3DParticleModelBlendParticle::commitParticles()
    self.uglySide.call(
        'ritual_ZN34QQuick3DParticleModelBlendParticle15commitParticlesEv',
    )

  @overload(QSSGRenderGraphObject)
  @overload(NoneType)
  def updateSpatialNode(
      self,
      node: Optional[QSSGRenderGraphObject],
  ) -> Optional[QSSGRenderGraphObject]:
    """
    Calls Qt's 'QSSGRenderGraphObject
    *QQuick3DParticleModelBlendParticle::updateSpatialNode(
    QSSGRenderGraphObject *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelblendparticle.html

    Parameters
    ----------

    node : Optional[QSSGRenderGraphObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSSGRenderGraphObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGRenderGraphObject
    #      *QQuick3DParticleModelBlendParticle::updateSpatialNode(
    #      QSSGRenderGraphObject *node)
    ritual = (
        'ritual_ZN34QQuick3DParticleModelBlendParticle17updateSpatialNodeEP'
        '21QSSGRenderGraphObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN34QQuick3DParticleModelBlendParticle17updateSpatial'
          'NodeEP21QSSGRenderGraphObject')
    address = self.uglySide.call(ritual, self._addressOf(node))
    from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
    return QSSGRenderGraphObject._cuteAt(address)

  @overload(QSSGParticleBuffer, QMatrix4x4)
  @overload(NoneType, QMatrix4x4)
  def updateParticleBuffer(
      self,
      buffer: Optional[QSSGParticleBuffer],
      sceneTransform: QMatrix4x4,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleModelBlendParticle::updateParticleBuffer(
    QSSGParticleBuffer *buffer, const QMatrix4x4 &sceneTransform)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelblendparticle.html

    Parameters
    ----------

    buffer : Optional[QSSGParticleBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    sceneTransform : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.
    """
    #  void QQuick3DParticleModelBlendParticle::updateParticleBuffer(
    #      QSSGParticleBuffer *buffer, const QMatrix4x4 &sceneTransform)
    self.uglySide.call(
        'ritual_ZN34QQuick3DParticleModelBlendParticle20updateParticleBuffe'
        'rEP18QSSGParticleBufferRK10QMatrix4x4',
        self._addressOf(buffer), self._valueOf(sceneTransform),
    )

  def regenerate(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleModelBlendParticle::regenerate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelblendparticle.html#regenerate
    """
    #  void QQuick3DParticleModelBlendParticle::regenerate()
    self.uglySide.call(
        'ritual_ZN34QQuick3DParticleModelBlendParticle10regenerateEv',
    )

  def updateParticles(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleModelBlendParticle::updateParticles()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelblendparticle.html
    """
    #  void QQuick3DParticleModelBlendParticle::updateParticles()
    self.uglySide.call(
        'ritual_ZN34QQuick3DParticleModelBlendParticle15updateParticlesEv',
    )

  def handleEndNodeChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleModelBlendParticle::handleEndNodeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlemodelblendparticle.html
    """
    #  void QQuick3DParticleModelBlendParticle::handleEndNodeChanged()
    self.uglySide.call(
        'ritual_ZN34QQuick3DParticleModelBlendParticle20handleEndNodeChange'
        'dEv',
    )

  @staticmethod
  def perEmitterData(*__, **_) -> Never:
    """
    Qt's 'PerEmitterData
    &QQuick3DParticleModelBlendParticle::perEmitterData(int emitterIndex)':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuick3DParticleModelBlendParticle.perEmitterData' has no cute "
        "function yet. Qt's 'PerEmitterData "
        "&QQuick3DParticleModelBlendParticle::perEmitterData(int "
        "emitterIndex)': gives a type Python has no way to take yet.")
