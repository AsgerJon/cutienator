"""
QQuick3DParticleSpriteParticle binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticlespriteparticle_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DParticleSpriteParticle to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtQuick3DRuntimeRender import QSSGRenderParticles
from ..QtQuick3D import QQuick3DNode, QQuick3DObject
from . import QQuick3DParticle

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QVector3D, QVector4D
  from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
  from ..QtQuick3D import QQuick3DSceneManager, QQuick3DTexture
  from . import QQuick3DParticleEmitter, QQuick3DParticleSpriteSequence
  from . import QQuick3DParticleSystem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuick3DNode = WAIT['QQuick3DNode']
  QQuick3DParticleEmitter = WAIT['QQuick3DParticleEmitter']
  QQuick3DParticleSpriteSequence = WAIT['QQuick3DParticleSpriteSequence']
  QQuick3DParticleSystem = WAIT['QQuick3DParticleSystem']
  QQuick3DSceneManager = WAIT['QQuick3DSceneManager']
  QQuick3DTexture = WAIT['QQuick3DTexture']
  QSSGRenderGraphObject = WAIT['QSSGRenderGraphObject']
  QVector3D = WAIT['QVector3D']
  QVector4D = WAIT['QVector4D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DParticleSpriteParticle(QQuick3DParticle):
  """
  The cute side of Qt's QQuick3DParticleSpriteParticle: a plain Python object
  standing in front of one C++ QQuick3DParticleSpriteParticle.

  It is built on the cute 'QQuick3DParticle', as Qt's
  QQuick3DParticleSpriteParticle is built on Qt's QQuick3DParticle, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DParticleSpriteParticle that has a ritual and
  that Python can call so far, 51 names in all: 'metaObject', 'tr',
  'blendMode', 'sprite', 'spriteSequence', 'billboard', 'particleScale',
  'colorTable', 'offsetX', 'offsetY', 'castsReflections', 'setBlendMode',
  'setSprite', 'setSpriteSequence', 'setBillboard', 'setParticleScale',
  'setColorTable', 'setOffsetX', 'setOffsetY', 'setCastsReflections',
  'blendModeChanged', 'spriteChanged', 'spriteSequenceChanged',
  'billboardChanged', 'particleScaleChanged', 'colorTableChanged',
  'lightsChanged', 'offsetXChanged', 'offsetYChanged',
  'castsReflectionsChanged', 'itemChange', 'reset', 'componentComplete',
  'nextCurrentIndex', 'setParticleData', 'resetParticleData',
  'commitParticles', 'setDepthBias', 'onLightDestroyed',
  'updateParticleNode', 'handleMaxAmountChanged', 'handleSystemChanged',
  'updateNodes', 'deleteNodes', 'markNodesDirty', 'updateNodeLayers',
  'mapFeatureLevel', 'updateParticleBuffer', 'updateAnimatedParticleBuffer',
  'updateSceneManager', 'updateFeatureLevel'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DParticleSpriteParticle::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQuick3DParticleSpriteParticle::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DParticleSpriteParticle::~QQuick3DParticleSpriteParticle()':
    the destructor: Python never removes a C++
    QQuick3DParticleSpriteParticle.
  - Qt's 'QQmlListProperty<QQuick3DAbstractLight>
    QQuick3DParticleSpriteParticle::lights()': gives a type Python has no way
    to take yet.
  - Qt's 'PerEmitterData
    &QQuick3DParticleSpriteParticle::perEmitterData(const QQuick3DNode
    *updateNode)': gives a type Python has no way to take yet.
  - Qt's 'PerEmitterData &QQuick3DParticleSpriteParticle::perEmitterData(int
    emitterIndex)': gives a type Python has no way to take yet.
  - Qt's 'void QQuick3DParticleSpriteParticle::qmlAppendLight(
    QQmlListProperty<QQuick3DAbstractLight> *list, QQuick3DAbstractLight
    *light)': names 'QQmlListProperty<QQuick3DAbstractLight>', which has no
    cute class yet.
  - Qt's 'QQuick3DAbstractLight *QQuick3DParticleSpriteParticle::qmlLightAt(
    QQmlListProperty<QQuick3DAbstractLight> *list, qsizetype index)': names
    'QQmlListProperty<QQuick3DAbstractLight>', which has no cute class yet.
  - Qt's 'qsizetype QQuick3DParticleSpriteParticle::qmlLightsCount(
    QQmlListProperty<QQuick3DAbstractLight> *list)': names
    'QQmlListProperty<QQuick3DAbstractLight>', which has no cute class yet.
  - Qt's 'void QQuick3DParticleSpriteParticle::qmlClearLights(
    QQmlListProperty<QQuick3DAbstractLight> *list)': names
    'QQmlListProperty<QQuick3DAbstractLight>', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 64 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DParticleSpriteParticle is created at the first use, not
    by 'QQuick3DParticleSpriteParticle(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DParticleSpriteParticle.
  - Qt tells when it has removed the C++ QQuick3DParticleSpriteParticle.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DParticleSpriteParticle that has no cute
    function yet, 'lights', 'perEmitterData', 'qmlAppendLight',
    'qmlClearLights', 'qmlLightAt', 'qmlLightsCount', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuick3DParticleSpriteParticle, each a class
  #  in here as in C++, and the names Qt has for the combinations of its
  #  flags enums.

  class BlendMode(CuteNum):
    """
    The enum 'QQuick3DParticleSpriteParticle::BlendMode' of Qt, with the 3
    names Qt gives in it.
    """

    SourceOver = Kee[int](0)
    Screen = Kee[int](1)
    Multiply = Kee[int](2)

  class FeatureLevel(CuteNum):
    """
    The enum 'QQuick3DParticleSpriteParticle::FeatureLevel' of Qt, with the 6
    names Qt gives in it.
    """

    Simple = Kee[int](0)
    Mapped = Kee[int](1)
    Animated = Kee[int](2)
    SimpleVLight = Kee[int](3)
    MappedVLight = Kee[int](4)
    AnimatedVLight = Kee[int](5)

  #  The classes Qt writes inside QQuick3DParticleSpriteParticle, each a
  #  class in here as in C++.

  class ParticleUpdateNode(QQuick3DNode):
    """
    The cute side of Qt's QQuick3DParticleSpriteParticle::ParticleUpdateNode:
    a plain Python object standing in front of one C++
    QQuick3DParticleSpriteParticle::ParticleUpdateNode.

    It is built on the cute 'QQuick3DNode', as Qt's
    QQuick3DParticleSpriteParticle::ParticleUpdateNode is built on Qt's
    QQuick3DNode, and has everything that class has.

    What exists
    -----------

    Every function of Qt's QQuick3DParticleSpriteParticle::ParticleUpdateNode
    that has a ritual and that Python can call so far, 1 name in all:
    'updateSpatialNode'. It can be made from Python, in 1 way; see
    '__init__'.

    What to expect
    --------------

    - The C++ QQuick3DParticleSpriteParticle::ParticleUpdateNode is created
      at the first use, not by
      'QQuick3DParticleSpriteParticle::ParticleUpdateNode(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++
      QQuick3DParticleSpriteParticle::ParticleUpdateNode.
    - Qt tells when it has removed the C++
      QQuick3DParticleSpriteParticle::ParticleUpdateNode. Every call on the
      cute object, and every use of it as an argument, then raises
      'RuntimeError', and nothing reaches C++.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QSSGRenderGraphObject = WAIT['QSSGRenderGraphObject']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuick3DParticleSpriteParticle::ParticleUpdateNode'

    #  A C++ QQuick3DParticleSpriteParticle::ParticleUpdateNode Python makes
    #  is of a C++ class of ours, in which Python can take functions over.
    #  This ritual hands one over; see 'CuteMixin._takeOver'.
    __take_ritual__ = 'ritual_take_QQuick3DParticleSpriteParticle_ParticleUpdateNode'

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
    @overload(QQuick3DNode)
    @overload(NoneType)
    def __init__(self, parent: Optional[QQuick3DNode] = None) -> None:
      """
      Notes what was given, for Qt's
      'QQuick3DParticleSpriteParticle::ParticleUpdateNode::
      ParticleUpdateNode(QQuick3DNode *parent)', which is called at the first
      use.

      Qt's own words:
      https://doc.qt.io/qt-6/qquick3dparticlespriteparticle-particleupdatenode.html

      Parameters
      ----------

      parent : Optional[QQuick3DNode]
        Passed on as the address of its C++ object. None is passed on as no
        object. May be left out, as in Qt: it is then None.
      """
      #  QQuick3DParticleSpriteParticle::ParticleUpdateNode::
      #      ParticleUpdateNode(QQuick3DNode *parent)
      self._noteCreation(
          QQuick3DParticleSpriteParticle.ParticleUpdateNode, lambda: Rituals.call(
              'ritual_ZN30QQuick3DParticleSpriteParticle18ParticleUpdateNod'
              'eC1EP12QQuick3DNode',
              self._addressOf(parent),
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

    @overload(QSSGRenderGraphObject)
    @overload(NoneType)
    def updateSpatialNode(
        self,
        node: Optional[QSSGRenderGraphObject],
    ) -> Optional[QSSGRenderGraphObject]:
      """
      Calls Qt's 'QSSGRenderGraphObject
      *QQuick3DParticleSpriteParticle::ParticleUpdateNode::updateSpatialNode(
      QSSGRenderGraphObject *node)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquick3dparticlespriteparticle-particleupdatenode.html

      Parameters
      ----------

      node : Optional[QSSGRenderGraphObject]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      Returns
      -------

      Optional[QSSGRenderGraphObject]
        The cute object standing for what Qt gave back. None when Qt gave
        back no object.
      """
      #  QSSGRenderGraphObject
      #      *QQuick3DParticleSpriteParticle::ParticleUpdateNode::
      #      updateSpatialNode(QSSGRenderGraphObject *node)
      ritual = (
          'ritual_ZN30QQuick3DParticleSpriteParticle18ParticleUpdateNode17u'
          'pdateSpatialNodeEP21QSSGRenderGraphObject')
      if self.uglySide.isOurs():
        ritual = (
            'ritual_own_ZN30QQuick3DParticleSpriteParticle18ParticleUpdateN'
            'ode17updateSpatialNodeEP21QSSGRenderGraphObject')
      address = self.uglySide.call(ritual, self._addressOf(node))
      from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
      return QSSGRenderGraphObject._cuteAt(address)

  class PerEmitterData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuick3DParticleSpriteParticle::PerEmitterData: a
    plain Python object standing in front of one C++
    QQuick3DParticleSpriteParticle::PerEmitterData.

    C++ hands a QQuick3DParticleSpriteParticle::PerEmitterData around as a
    copy, so every C++ QQuick3DParticleSpriteParticle::PerEmitterData behind
    a cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QQuick3DParticleSpriteParticle::PerEmitterData yet.
    None can be made from Python: one comes out of a function of another
    class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QQuick3DParticleSpriteParticle::PerEmitterData::~PerEmitterData()':
      the destructor: Python removes its C++
      QQuick3DParticleSpriteParticle::PerEmitterData by it, and has no other
      use for it.

    What to expect
    --------------

    - The C++ QQuick3DParticleSpriteParticle::PerEmitterData is created at
      the first use, not by
      'QQuick3DParticleSpriteParticle::PerEmitterData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuick3DParticleSpriteParticle::PerEmitterData back
      gives a copy the ritual made for Python, in a new cute
      QQuick3DParticleSpriteParticle::PerEmitterData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuick3DParticleSpriteParticle::PerEmitterData'

    #  Qt's '~QQuick3DParticleSpriteParticle::PerEmitterData()'. Naming it
    #  makes this a value class: Python owns every C++
    #  QQuick3DParticleSpriteParticle::PerEmitterData behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN30QQuick3DParticleSpriteParticle14PerEmitterDataD1Ev')

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

  class SpriteParticleData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuick3DParticleSpriteParticle::SpriteParticleData:
    a plain Python object standing in front of one C++
    QQuick3DParticleSpriteParticle::SpriteParticleData.

    C++ hands a QQuick3DParticleSpriteParticle::SpriteParticleData around as
    a copy, so every C++ QQuick3DParticleSpriteParticle::SpriteParticleData
    behind a cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QQuick3DParticleSpriteParticle::SpriteParticleData
    yet. None can be made from Python: one comes out of a function of another
    class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuick3DParticleSpriteParticle::SpriteParticleData::
      ~SpriteParticleData()': the destructor: Python removes its C++
      QQuick3DParticleSpriteParticle::SpriteParticleData by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QQuick3DParticleSpriteParticle::SpriteParticleData is created
      at the first use, not by
      'QQuick3DParticleSpriteParticle::SpriteParticleData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuick3DParticleSpriteParticle::SpriteParticleData
      back gives a copy the ritual made for Python, in a new cute
      QQuick3DParticleSpriteParticle::SpriteParticleData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuick3DParticleSpriteParticle::SpriteParticleData'

    #  Qt's '~QQuick3DParticleSpriteParticle::SpriteParticleData()'. Naming
    #  it makes this a value class: Python owns every C++
    #  QQuick3DParticleSpriteParticle::SpriteParticleData behind a cute one,
    #  and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN30QQuick3DParticleSpriteParticle18SpriteParticleDataD1Ev')

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
    Calls Qt's 'QString QQuick3DParticleSpriteParticle::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html#tr

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
    #  QString QQuick3DParticleSpriteParticle::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN30QQuick3DParticleSpriteParticle2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(FeatureLevel)
  def mapFeatureLevel(
      level: FeatureLevel,
  ) -> QSSGRenderParticles.FeatureLevel:
    """
    Calls Qt's 'QSSGRenderParticles::FeatureLevel
    QQuick3DParticleSpriteParticle::mapFeatureLevel(
    QQuick3DParticleSpriteParticle::FeatureLevel level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html

    Parameters
    ----------

    level : FeatureLevel
      Passed on as its number.

    Returns
    -------

    QSSGRenderParticles.FeatureLevel
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSSGRenderParticles.FeatureLevel(number)' gives.
    """
    #  QSSGRenderParticles::FeatureLevel
    #      QQuick3DParticleSpriteParticle::mapFeatureLevel(
    #      QQuick3DParticleSpriteParticle::FeatureLevel level)
    return QSSGRenderParticles.FeatureLevel(Rituals.call(
        'ritual_ZN30QQuick3DParticleSpriteParticle15mapFeatureLevelENS_12Fe'
        'atureLevelE',
        level.value,
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DParticleSpriteParticle'

  #  A C++ QQuick3DParticleSpriteParticle Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DParticleSpriteParticle'

  #  The functions Qt calls itself that QQuick3DParticleSpriteParticle is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'setParticleData': (
          ('_ZN30QQuick3DParticleSpriteParticle15setParticleDataEiRK9QVecto'
           'r3DS2_RK9QVector4Dfff',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('address', 'value', 'QtGui:QVector3D'),
               ('address', 'value', 'QtGui:QVector3D'),
               ('address', 'value', 'QtGui:QVector4D'),
               ('float', 'number', ''),
               ('float', 'number', ''),
               ('float', 'number', ''),
           )),
      ),
      'resetParticleData': (
          ('_ZN30QQuick3DParticleSpriteParticle17resetParticleDataEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'commitParticles': (
          ('_ZN30QQuick3DParticleSpriteParticle15commitParticlesEf',
           ('nothing', 'nothing', ''),
           (
               ('float', 'number', ''),
           )),
      ),
      'handleMaxAmountChanged': (
          ('_ZN30QQuick3DParticleSpriteParticle22handleMaxAmountChangedEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'handleSystemChanged': (
          ('_ZN30QQuick3DParticleSpriteParticle19handleSystemChangedEP22QQu'
           'ick3DParticleSystem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtQuick3DParticles:QQuick3DParticleSystem'),
           )),
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
    Calls Qt's 'const QMetaObject
    *QQuick3DParticleSpriteParticle::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DParticleSpriteParticle::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK30QQuick3DParticleSpriteParticle10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def blendMode(self) -> BlendMode:
    """
    Calls Qt's 'BlendMode QQuick3DParticleSpriteParticle::blendMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html#blendMode

    Returns
    -------

    BlendMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'BlendMode(number)' gives.
    """
    #  BlendMode QQuick3DParticleSpriteParticle::blendMode() const
    return QQuick3DParticleSpriteParticle.BlendMode(self.uglySide.call(
        'ritual_ZNK30QQuick3DParticleSpriteParticle9blendModeEv',
    ))

  def sprite(self) -> Optional[QQuick3DTexture]:
    """
    Calls Qt's 'QQuick3DTexture *QQuick3DParticleSpriteParticle::sprite()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html#sprite

    Returns
    -------

    Optional[QQuick3DTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DTexture *QQuick3DParticleSpriteParticle::sprite() const
    address = self.uglySide.call(
        'ritual_ZNK30QQuick3DParticleSpriteParticle6spriteEv',
    )
    from ..QtQuick3D import QQuick3DTexture
    return QQuick3DTexture._cuteAt(address)

  def spriteSequence(self) -> Optional[QQuick3DParticleSpriteSequence]:
    """
    Calls Qt's 'QQuick3DParticleSpriteSequence
    *QQuick3DParticleSpriteParticle::spriteSequence() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html#spriteSequence

    Returns
    -------

    Optional[QQuick3DParticleSpriteSequence]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DParticleSpriteSequence
    #      *QQuick3DParticleSpriteParticle::spriteSequence() const
    address = self.uglySide.call(
        'ritual_ZNK30QQuick3DParticleSpriteParticle14spriteSequenceEv',
    )
    from . import QQuick3DParticleSpriteSequence
    return QQuick3DParticleSpriteSequence._cuteAt(address)

  def billboard(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DParticleSpriteParticle::billboard() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html#billboard
    """
    #  bool QQuick3DParticleSpriteParticle::billboard() const
    return self.uglySide.call(
        'ritual_ZNK30QQuick3DParticleSpriteParticle9billboardEv',
    )

  def particleScale(self) -> float:
    """
    Calls Qt's 'float QQuick3DParticleSpriteParticle::particleScale() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html#particleScale
    """
    #  float QQuick3DParticleSpriteParticle::particleScale() const
    return self.uglySide.call(
        'ritual_ZNK30QQuick3DParticleSpriteParticle13particleScaleEv',
    )

  def colorTable(self) -> Optional[QQuick3DTexture]:
    """
    Calls Qt's 'QQuick3DTexture *QQuick3DParticleSpriteParticle::colorTable()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html#colorTable

    Returns
    -------

    Optional[QQuick3DTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DTexture *QQuick3DParticleSpriteParticle::colorTable() const
    address = self.uglySide.call(
        'ritual_ZNK30QQuick3DParticleSpriteParticle10colorTableEv',
    )
    from ..QtQuick3D import QQuick3DTexture
    return QQuick3DTexture._cuteAt(address)

  def offsetX(self) -> float:
    """
    Calls Qt's 'float QQuick3DParticleSpriteParticle::offsetX() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html#offsetX
    """
    #  float QQuick3DParticleSpriteParticle::offsetX() const
    return self.uglySide.call(
        'ritual_ZNK30QQuick3DParticleSpriteParticle7offsetXEv',
    )

  def offsetY(self) -> float:
    """
    Calls Qt's 'float QQuick3DParticleSpriteParticle::offsetY() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html#offsetY
    """
    #  float QQuick3DParticleSpriteParticle::offsetY() const
    return self.uglySide.call(
        'ritual_ZNK30QQuick3DParticleSpriteParticle7offsetYEv',
    )

  def castsReflections(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DParticleSpriteParticle::castsReflections()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html
    """
    #  bool QQuick3DParticleSpriteParticle::castsReflections() const
    return self.uglySide.call(
        'ritual_ZNK30QQuick3DParticleSpriteParticle16castsReflectionsEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(BlendMode)
  def setBlendMode(self, blendMode: BlendMode) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSpriteParticle::setBlendMode(
    QQuick3DParticleSpriteParticle::BlendMode blendMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html#setBlendMode

    Parameters
    ----------

    blendMode : BlendMode
      Passed on as its number.
    """
    #  void QQuick3DParticleSpriteParticle::setBlendMode(
    #      QQuick3DParticleSpriteParticle::BlendMode blendMode)
    self.uglySide.call(
        'ritual_ZN30QQuick3DParticleSpriteParticle12setBlendModeENS_9BlendM'
        'odeE',
        blendMode.value,
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def setSprite(self, sprite: Optional[QQuick3DTexture]) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleSpriteParticle::setSprite(QQuick3DTexture *sprite)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html#setSprite

    Parameters
    ----------

    sprite : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DParticleSpriteParticle::setSprite(QQuick3DTexture
    #      *sprite)
    self.uglySide.call(
        'ritual_ZN30QQuick3DParticleSpriteParticle9setSpriteEP15QQuick3DTex'
        'ture',
        self._addressOf(sprite),
    )

  @overload(QQuick3DParticleSpriteSequence)
  @overload(NoneType)
  def setSpriteSequence(
      self,
      spriteSequence: Optional[QQuick3DParticleSpriteSequence],
  ) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSpriteParticle::setSpriteSequence(
    QQuick3DParticleSpriteSequence *spriteSequence)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html

    Parameters
    ----------

    spriteSequence : Optional[QQuick3DParticleSpriteSequence]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DParticleSpriteParticle::setSpriteSequence(
    #      QQuick3DParticleSpriteSequence *spriteSequence)
    self.uglySide.call(
        'ritual_ZN30QQuick3DParticleSpriteParticle17setSpriteSequenceEP30QQ'
        'uick3DParticleSpriteSequence',
        self._addressOf(spriteSequence),
    )

  @overload(bool)
  def setBillboard(self, billboard: bool) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSpriteParticle::setBillboard(bool
    billboard)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html#setBillboard

    Parameters
    ----------

    billboard : bool
      Passed on as it is.
    """
    #  void QQuick3DParticleSpriteParticle::setBillboard(bool billboard)
    self.uglySide.call(
        'ritual_ZN30QQuick3DParticleSpriteParticle12setBillboardEb',
        billboard,
    )

  @overload(float)
  def setParticleScale(self, scale: float) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSpriteParticle::setParticleScale(float
    scale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html

    Parameters
    ----------

    scale : float
      Passed on as it is.
    """
    #  void QQuick3DParticleSpriteParticle::setParticleScale(float scale)
    self.uglySide.call(
        'ritual_ZN30QQuick3DParticleSpriteParticle16setParticleScaleEf',
        scale,
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def setColorTable(self, colorTable: Optional[QQuick3DTexture]) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleSpriteParticle::setColorTable(QQuick3DTexture
    *colorTable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html#setColorTable

    Parameters
    ----------

    colorTable : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DParticleSpriteParticle::setColorTable(QQuick3DTexture
    #      *colorTable)
    self.uglySide.call(
        'ritual_ZN30QQuick3DParticleSpriteParticle13setColorTableEP15QQuick'
        '3DTexture',
        self._addressOf(colorTable),
    )

  @overload(float)
  def setOffsetX(self, value: float) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSpriteParticle::setOffsetX(float
    value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html#setOffsetX

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QQuick3DParticleSpriteParticle::setOffsetX(float value)
    self.uglySide.call(
        'ritual_ZN30QQuick3DParticleSpriteParticle10setOffsetXEf', value,
    )

  @overload(float)
  def setOffsetY(self, value: float) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSpriteParticle::setOffsetY(float
    value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html#setOffsetY

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QQuick3DParticleSpriteParticle::setOffsetY(float value)
    self.uglySide.call(
        'ritual_ZN30QQuick3DParticleSpriteParticle10setOffsetYEf', value,
    )

  @overload(bool)
  def setCastsReflections(self, castsReflections: bool) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSpriteParticle::setCastsReflections(bool
    castsReflections)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html

    Parameters
    ----------

    castsReflections : bool
      Passed on as it is.
    """
    #  void QQuick3DParticleSpriteParticle::setCastsReflections(bool
    #      castsReflections)
    self.uglySide.call(
        'ritual_ZN30QQuick3DParticleSpriteParticle19setCastsReflectionsEb',
        castsReflections,
    )

  @overload(int, QVector3D, QVector3D, QVector4D, float, float, float)
  def setParticleData(
      self,
      particleIndex: int,
      position: QVector3D,
      rotation: QVector3D,
      color: QVector4D,
      size: float,
      age: float,
      animationFrame: float,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSpriteParticle::setParticleData(int
    particleIndex, const QVector3D &position, const QVector3D &rotation,
    const QVector4D &color, float size, float age, float animationFrame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html

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

    animationFrame : float
      Passed on as it is.
    """
    #  void QQuick3DParticleSpriteParticle::setParticleData(int
    #      particleIndex, const QVector3D &position, const QVector3D
    #      &rotation, const QVector4D &color, float size, float age, float
    #      animationFrame)
    ritual = (
        'ritual_ZN30QQuick3DParticleSpriteParticle15setParticleDataEiRK9QVe'
        'ctor3DS2_RK9QVector4Dfff')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30QQuick3DParticleSpriteParticle15setParticleDataEi'
          'RK9QVector3DS2_RK9QVector4Dfff')
    self.uglySide.call(
        ritual,
        particleIndex, self._valueOf(position), self._valueOf(rotation),
        self._valueOf(color), size, age, animationFrame,
    )

  @overload(float)
  def setDepthBias(self, bias: float) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSpriteParticle::setDepthBias(float
    bias)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html#setDepthBias

    Parameters
    ----------

    bias : float
      Passed on as it is.
    """
    #  void QQuick3DParticleSpriteParticle::setDepthBias(float bias)
    ritual = 'ritual_ZN30QQuick3DParticleSpriteParticle12setDepthBiasEf'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30QQuick3DParticleSpriteParticle12setDepthBiasEf')
    self.uglySide.call(ritual, bias)

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
    'QQuick3DParticleSpriteParticle::QQuick3DParticleSpriteParticle(
    QQuick3DNode *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html

    Parameters
    ----------

    parent : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DParticleSpriteParticle::QQuick3DParticleSpriteParticle(
    #      QQuick3DNode *parent)
    self._noteCreation(QQuick3DParticleSpriteParticle, lambda: Rituals.call(
        'ritual_ZN30QQuick3DParticleSpriteParticleC1EP12QQuick3DNode',
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

  def blendModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSpriteParticle::blendModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html
    """
    #  void QQuick3DParticleSpriteParticle::blendModeChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DParticleSpriteParticle16blendModeChangedEv',
    )

  def spriteChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSpriteParticle::spriteChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html#spriteChanged
    """
    #  void QQuick3DParticleSpriteParticle::spriteChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DParticleSpriteParticle13spriteChangedEv',
    )

  def spriteSequenceChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleSpriteParticle::spriteSequenceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html
    """
    #  void QQuick3DParticleSpriteParticle::spriteSequenceChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DParticleSpriteParticle21spriteSequenceChangedEv',
    )

  def billboardChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSpriteParticle::billboardChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html
    """
    #  void QQuick3DParticleSpriteParticle::billboardChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DParticleSpriteParticle16billboardChangedEv',
    )

  def particleScaleChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSpriteParticle::particleScaleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html
    """
    #  void QQuick3DParticleSpriteParticle::particleScaleChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DParticleSpriteParticle20particleScaleChangedEv',
    )

  def colorTableChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSpriteParticle::colorTableChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html
    """
    #  void QQuick3DParticleSpriteParticle::colorTableChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DParticleSpriteParticle17colorTableChangedEv',
    )

  def lightsChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSpriteParticle::lightsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html#lightsChanged
    """
    #  void QQuick3DParticleSpriteParticle::lightsChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DParticleSpriteParticle13lightsChangedEv',
    )

  def offsetXChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSpriteParticle::offsetXChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html#offsetXChanged
    """
    #  void QQuick3DParticleSpriteParticle::offsetXChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DParticleSpriteParticle14offsetXChangedEv',
    )

  def offsetYChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSpriteParticle::offsetYChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html#offsetYChanged
    """
    #  void QQuick3DParticleSpriteParticle::offsetYChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DParticleSpriteParticle14offsetYChangedEv',
    )

  def castsReflectionsChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleSpriteParticle::castsReflectionsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html
    """
    #  void QQuick3DParticleSpriteParticle::castsReflectionsChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DParticleSpriteParticle23castsReflectionsChanged'
        'Ev',
    )

  @overload(QQuick3DObject.ItemChange, QQuick3DObject.ItemChangeData)
  def itemChange(
      self,
      a0: QQuick3DObject.ItemChange,
      a1: QQuick3DObject.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSpriteParticle::itemChange(ItemChange
    a0, const ItemChangeData &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html#itemChange

    Parameters
    ----------

    a0 : QQuick3DObject.ItemChange
      Passed on as its number.

    a1 : QQuick3DObject.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuick3DObject::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuick3DParticleSpriteParticle::itemChange(ItemChange a0, const
    #      ItemChangeData &a1)
    ritual = (
        'ritual_ZN30QQuick3DParticleSpriteParticle10itemChangeEN14QQuick3DO'
        'bject10ItemChangeERKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30QQuick3DParticleSpriteParticle10itemChangeEN14QQu'
          'ick3DObject10ItemChangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, a0.value, self._valueOf(a1))

  def reset(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSpriteParticle::reset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html#reset
    """
    #  void QQuick3DParticleSpriteParticle::reset()
    ritual = 'ritual_ZN30QQuick3DParticleSpriteParticle5resetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN30QQuick3DParticleSpriteParticle5resetEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSpriteParticle::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html
    """
    #  void QQuick3DParticleSpriteParticle::componentComplete()
    ritual = 'ritual_ZN30QQuick3DParticleSpriteParticle17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30QQuick3DParticleSpriteParticle17componentComplete'
          'Ev')
    self.uglySide.call(ritual)

  @overload(QQuick3DParticleEmitter)
  @overload(NoneType)
  def nextCurrentIndex(
      self,
      emitter: Optional[QQuick3DParticleEmitter],
  ) -> int:
    """
    Calls Qt's 'int QQuick3DParticleSpriteParticle::nextCurrentIndex(const
    QQuick3DParticleEmitter *emitter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html

    Parameters
    ----------

    emitter : Optional[QQuick3DParticleEmitter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QQuick3DParticleSpriteParticle::nextCurrentIndex(const
    #      QQuick3DParticleEmitter *emitter)
    ritual = (
        'ritual_ZN30QQuick3DParticleSpriteParticle16nextCurrentIndexEPK23QQ'
        'uick3DParticleEmitter')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30QQuick3DParticleSpriteParticle16nextCurrentIndexE'
          'PK23QQuick3DParticleEmitter')
    return self.uglySide.call(ritual, self._addressOf(emitter))

  @overload(int)
  def resetParticleData(self, particleIndex: int) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSpriteParticle::resetParticleData(int
    particleIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html

    Parameters
    ----------

    particleIndex : int
      Passed on as it is.
    """
    #  void QQuick3DParticleSpriteParticle::resetParticleData(int
    #      particleIndex)
    ritual = 'ritual_ZN30QQuick3DParticleSpriteParticle17resetParticleDataEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30QQuick3DParticleSpriteParticle17resetParticleData'
          'Ei')
    self.uglySide.call(ritual, particleIndex)

  @overload(float)
  def commitParticles(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSpriteParticle::commitParticles(float
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuick3DParticleSpriteParticle::commitParticles(float a0)
    ritual = 'ritual_ZN30QQuick3DParticleSpriteParticle15commitParticlesEf'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30QQuick3DParticleSpriteParticle15commitParticlesEf')
    self.uglySide.call(ritual, a0)

  @overload(QObject)
  @overload(NoneType)
  def onLightDestroyed(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSpriteParticle::onLightDestroyed(QObject
    *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DParticleSpriteParticle::onLightDestroyed(QObject *object)
    self.uglySide.call(
        'ritual_ZN30QQuick3DParticleSpriteParticle16onLightDestroyedEP7QObj'
        'ect',
        self._addressOf(object, 'QObject'),
    )

  @overload(ParticleUpdateNode, QSSGRenderGraphObject)
  @overload(ParticleUpdateNode, NoneType)
  @overload(NoneType, QSSGRenderGraphObject)
  @overload(NoneType, NoneType)
  def updateParticleNode(
      self,
      updateNode: Optional[ParticleUpdateNode],
      node: Optional[QSSGRenderGraphObject],
  ) -> Optional[QSSGRenderGraphObject]:
    """
    Calls Qt's 'QSSGRenderGraphObject
    *QQuick3DParticleSpriteParticle::updateParticleNode(const
    ParticleUpdateNode *updateNode, QSSGRenderGraphObject *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html

    Parameters
    ----------

    updateNode : Optional[ParticleUpdateNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

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
    #      *QQuick3DParticleSpriteParticle::updateParticleNode(const
    #      ParticleUpdateNode *updateNode, QSSGRenderGraphObject *node)
    address = self.uglySide.call(
        'ritual_ZN30QQuick3DParticleSpriteParticle18updateParticleNodeEPKNS'
        '_18ParticleUpdateNodeEP21QSSGRenderGraphObject',
        self._addressOf(updateNode), self._addressOf(node),
    )
    from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
    return QSSGRenderGraphObject._cuteAt(address)

  @overload(int)
  def handleMaxAmountChanged(self, amount: int) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleSpriteParticle::handleMaxAmountChanged(int amount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html

    Parameters
    ----------

    amount : int
      Passed on as it is.
    """
    #  void QQuick3DParticleSpriteParticle::handleMaxAmountChanged(int
    #      amount)
    ritual = (
        'ritual_ZN30QQuick3DParticleSpriteParticle22handleMaxAmountChangedE'
        'i')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30QQuick3DParticleSpriteParticle22handleMaxAmountCh'
          'angedEi')
    self.uglySide.call(ritual, amount)

  @overload(QQuick3DParticleSystem)
  @overload(NoneType)
  def handleSystemChanged(
      self,
      system: Optional[QQuick3DParticleSystem],
  ) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSpriteParticle::handleSystemChanged(
    QQuick3DParticleSystem *system)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html

    Parameters
    ----------

    system : Optional[QQuick3DParticleSystem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DParticleSpriteParticle::handleSystemChanged(
    #      QQuick3DParticleSystem *system)
    ritual = (
        'ritual_ZN30QQuick3DParticleSpriteParticle19handleSystemChangedEP22'
        'QQuick3DParticleSystem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30QQuick3DParticleSpriteParticle19handleSystemChang'
          'edEP22QQuick3DParticleSystem')
    self.uglySide.call(ritual, self._addressOf(system))

  def updateNodes(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSpriteParticle::updateNodes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html#updateNodes
    """
    #  void QQuick3DParticleSpriteParticle::updateNodes()
    self.uglySide.call(
        'ritual_ZN30QQuick3DParticleSpriteParticle11updateNodesEv',
    )

  def deleteNodes(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSpriteParticle::deleteNodes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html#deleteNodes
    """
    #  void QQuick3DParticleSpriteParticle::deleteNodes()
    self.uglySide.call(
        'ritual_ZN30QQuick3DParticleSpriteParticle11deleteNodesEv',
    )

  def markNodesDirty(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSpriteParticle::markNodesDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html#markNodesDirty
    """
    #  void QQuick3DParticleSpriteParticle::markNodesDirty()
    self.uglySide.call(
        'ritual_ZN30QQuick3DParticleSpriteParticle14markNodesDirtyEv',
    )

  def updateNodeLayers(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSpriteParticle::updateNodeLayers()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html
    """
    #  void QQuick3DParticleSpriteParticle::updateNodeLayers()
    ritual = 'ritual_ZN30QQuick3DParticleSpriteParticle16updateNodeLayersEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30QQuick3DParticleSpriteParticle16updateNodeLayersE'
          'v')
    self.uglySide.call(ritual)

  @overload(ParticleUpdateNode, QSSGRenderGraphObject)
  @overload(ParticleUpdateNode, NoneType)
  @overload(NoneType, QSSGRenderGraphObject)
  @overload(NoneType, NoneType)
  def updateParticleBuffer(
      self,
      updateNode: Optional[ParticleUpdateNode],
      node: Optional[QSSGRenderGraphObject],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleSpriteParticle::updateParticleBuffer(ParticleUpdateNode
    *updateNode, QSSGRenderGraphObject *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html

    Parameters
    ----------

    updateNode : Optional[ParticleUpdateNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    node : Optional[QSSGRenderGraphObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DParticleSpriteParticle::updateParticleBuffer(
    #      ParticleUpdateNode *updateNode, QSSGRenderGraphObject *node)
    self.uglySide.call(
        'ritual_ZN30QQuick3DParticleSpriteParticle20updateParticleBufferEPN'
        'S_18ParticleUpdateNodeEP21QSSGRenderGraphObject',
        self._addressOf(updateNode), self._addressOf(node),
    )

  @overload(ParticleUpdateNode, QSSGRenderGraphObject)
  @overload(ParticleUpdateNode, NoneType)
  @overload(NoneType, QSSGRenderGraphObject)
  @overload(NoneType, NoneType)
  def updateAnimatedParticleBuffer(
      self,
      updateNode: Optional[ParticleUpdateNode],
      node: Optional[QSSGRenderGraphObject],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleSpriteParticle::updateAnimatedParticleBuffer(
    ParticleUpdateNode *updateNode, QSSGRenderGraphObject *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html

    Parameters
    ----------

    updateNode : Optional[ParticleUpdateNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    node : Optional[QSSGRenderGraphObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DParticleSpriteParticle::updateAnimatedParticleBuffer(
    #      ParticleUpdateNode *updateNode, QSSGRenderGraphObject *node)
    self.uglySide.call(
        'ritual_ZN30QQuick3DParticleSpriteParticle28updateAnimatedParticleB'
        'ufferEPNS_18ParticleUpdateNodeEP21QSSGRenderGraphObject',
        self._addressOf(updateNode), self._addressOf(node),
    )

  @overload(QQuick3DSceneManager)
  @overload(NoneType)
  def updateSceneManager(
      self,
      window: Optional[QQuick3DSceneManager],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleSpriteParticle::updateSceneManager(QQuick3DSceneManager
    *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html

    Parameters
    ----------

    window : Optional[QQuick3DSceneManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DParticleSpriteParticle::updateSceneManager(
    #      QQuick3DSceneManager *window)
    self.uglySide.call(
        'ritual_ZN30QQuick3DParticleSpriteParticle18updateSceneManagerEP20Q'
        'Quick3DSceneManager',
        self._addressOf(window),
    )

  def updateFeatureLevel(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSpriteParticle::updateFeatureLevel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespriteparticle.html
    """
    #  void QQuick3DParticleSpriteParticle::updateFeatureLevel()
    self.uglySide.call(
        'ritual_ZN30QQuick3DParticleSpriteParticle18updateFeatureLevelEv',
    )

  @staticmethod
  def lights(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuick3DAbstractLight>
    QQuick3DParticleSpriteParticle::lights()': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'QQuick3DParticleSpriteParticle.lights' has no cute function yet. "
        "Qt's 'QQmlListProperty<QQuick3DAbstractLight> "
        "QQuick3DParticleSpriteParticle::lights()': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def perEmitterData(*__, **_) -> Never:
    """
    - Qt's 'PerEmitterData
      &QQuick3DParticleSpriteParticle::perEmitterData(const QQuick3DNode
      *updateNode)': gives a type Python has no way to take yet.
    - Qt's 'PerEmitterData
      &QQuick3DParticleSpriteParticle::perEmitterData(int emitterIndex)':
      gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuick3DParticleSpriteParticle.perEmitterData' has no cute "
        "function yet. Qt's 'PerEmitterData "
        "&QQuick3DParticleSpriteParticle::perEmitterData(const QQuick3DNode "
        "*updateNode)': gives a type Python has no way to take yet. Qt's "
        "'PerEmitterData "
        "&QQuick3DParticleSpriteParticle::perEmitterData(int "
        "emitterIndex)': gives a type Python has no way to take yet.")

  @staticmethod
  def qmlAppendLight(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DParticleSpriteParticle::qmlAppendLight(
    QQmlListProperty<QQuick3DAbstractLight> *list, QQuick3DAbstractLight
    *light)': names 'QQmlListProperty<QQuick3DAbstractLight>', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QQuick3DParticleSpriteParticle.qmlAppendLight' has no cute "
        "function yet. Qt's 'void "
        "QQuick3DParticleSpriteParticle::qmlAppendLight(QQmlListProperty<QQu"
        "ick3DAbstractLight> *list, QQuick3DAbstractLight *light)': names "
        "'QQmlListProperty<QQuick3DAbstractLight>', which has no cute class "
        "yet.")

  @staticmethod
  def qmlClearLights(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DParticleSpriteParticle::qmlClearLights(
    QQmlListProperty<QQuick3DAbstractLight> *list)': names
    'QQmlListProperty<QQuick3DAbstractLight>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuick3DParticleSpriteParticle.qmlClearLights' has no cute "
        "function yet. Qt's 'void "
        "QQuick3DParticleSpriteParticle::qmlClearLights(QQmlListProperty<QQu"
        "ick3DAbstractLight> *list)': names "
        "'QQmlListProperty<QQuick3DAbstractLight>', which has no cute class "
        "yet.")

  @staticmethod
  def qmlLightAt(*__, **_) -> Never:
    """
    Qt's 'QQuick3DAbstractLight *QQuick3DParticleSpriteParticle::qmlLightAt(
    QQmlListProperty<QQuick3DAbstractLight> *list, qsizetype index)': names
    'QQmlListProperty<QQuick3DAbstractLight>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuick3DParticleSpriteParticle.qmlLightAt' has no cute function "
        "yet. Qt's 'QQuick3DAbstractLight "
        "*QQuick3DParticleSpriteParticle::qmlLightAt(QQmlListProperty<QQuick"
        "3DAbstractLight> *list, qsizetype index)': names "
        "'QQmlListProperty<QQuick3DAbstractLight>', which has no cute class "
        "yet.")

  @staticmethod
  def qmlLightsCount(*__, **_) -> Never:
    """
    Qt's 'qsizetype QQuick3DParticleSpriteParticle::qmlLightsCount(
    QQmlListProperty<QQuick3DAbstractLight> *list)': names
    'QQmlListProperty<QQuick3DAbstractLight>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuick3DParticleSpriteParticle.qmlLightsCount' has no cute "
        "function yet. Qt's 'qsizetype "
        "QQuick3DParticleSpriteParticle::qmlLightsCount(QQmlListProperty<QQu"
        "ick3DAbstractLight> *list)': names "
        "'QQmlListProperty<QQuick3DAbstractLight>', which has no cute class "
        "yet.")
