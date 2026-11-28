"""
QQuick3DModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dmodel_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuick3DModel to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QQuick3DNode, QQuick3DObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QUrl
  from ..QtGui import QMatrix4x4, QVector3D
  from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
  from . import QQuick3DBakedLightmap, QQuick3DBounds3, QQuick3DGeometry
  from . import QQuick3DInstancing, QQuick3DSceneManager, QQuick3DSkeleton
  from . import QQuick3DSkin
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMatrix4x4 = WAIT['QMatrix4x4']
  QQuick3DBakedLightmap = WAIT['QQuick3DBakedLightmap']
  QQuick3DGeometry = WAIT['QQuick3DGeometry']
  QQuick3DInstancing = WAIT['QQuick3DInstancing']
  QQuick3DSceneManager = WAIT['QQuick3DSceneManager']
  QQuick3DSkeleton = WAIT['QQuick3DSkeleton']
  QQuick3DSkin = WAIT['QQuick3DSkin']
  QSSGRenderGraphObject = WAIT['QSSGRenderGraphObject']
  QUrl = WAIT['QUrl']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DModel(QQuick3DNode):
  """
  The cute side of Qt's QQuick3DModel: a plain Python object standing in
  front of one C++ QQuick3DModel.

  It is built on the cute 'QQuick3DNode', as Qt's QQuick3DModel is built on
  Qt's QQuick3DNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DModel that has a ritual and that Python can
  call so far, 82 names in all: 'metaObject', 'tr', 'source', 'castsShadows',
  'receivesShadows', 'pickable', 'geometry', 'skeleton', 'inverseBindPoses',
  'bounds', 'depthBias', 'instancing', 'instanceRoot', 'receivesReflections',
  'castsReflections', 'skin', 'translateMeshSource', 'isUsedInBakedLighting',
  'lightmapBaseResolution', 'bakedLightmap', 'instancingLodMin',
  'instancingLodMax', 'levelOfDetailBias', 'instancingLodFactor',
  'texelsPerUnit', 'setTexelsPerUnit', 'motionVectorEnabled',
  'motionVectorScale', 'setSource', 'setCastsShadows', 'setReceivesShadows',
  'setPickable', 'setGeometry', 'setSkeleton', 'setInverseBindPoses',
  'setBounds', 'setInstancing', 'setInstanceRoot', 'setDepthBias',
  'setReceivesReflections', 'setCastsReflections', 'setSkin',
  'setUsedInBakedLighting', 'setLightmapBaseResolution', 'setBakedLightmap',
  'setInstancingLodMin', 'setInstancingLodMax', 'setLevelOfDetailBias',
  'setInstancingLodFactor', 'setMotionVectorScale', 'setMotionVectorEnabled',
  'sourceChanged', 'castsShadowsChanged', 'receivesShadowsChanged',
  'pickableChanged', 'geometryChanged', 'skeletonChanged',
  'inverseBindPosesChanged', 'boundsChanged', 'instancingChanged',
  'instanceRootChanged', 'morphTargetsChanged', 'depthBiasChanged',
  'receivesReflectionsChanged', 'castsReflectionsChanged', 'skinChanged',
  'usedInBakedLightingChanged', 'lightmapBaseResolutionChanged',
  'bakedLightmapChanged', 'instancingLodMinChanged',
  'instancingLodMaxChanged', 'instancingLodFactorChanged',
  'levelOfDetailBiasChanged', 'texelsPerUnitChanged',
  'motionVectorEnabledChanged', 'motionVectorScaleChanged',
  'updateSpatialNode', 'markAllDirty', 'itemChange', 'onMaterialDestroyed',
  'onMorphTargetDestroyed', 'updateSceneManager'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DModel::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuick3DModel::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DModel::~QQuick3DModel()': the destructor: Python never
    removes a C++ QQuick3DModel.
  - Qt's 'QQmlListProperty<QQuick3DMaterial> QQuick3DModel::materials()':
    gives a type Python has no way to take yet.
  - Qt's 'QQmlListProperty<QQuick3DMorphTarget>
    QQuick3DModel::morphTargets()': gives a type Python has no way to take
    yet.
  - Qt's 'void QQuick3DModel::markDirty(QSSGModelDirtyType type)': names the
    enum 'QQuick3DModel::QSSGModelDirtyType', whose class cannot be named
    here.
  - Qt's 'void
    QQuick3DModel::qmlAppendMaterial(QQmlListProperty<QQuick3DMaterial>
    *list, QQuick3DMaterial *material)': names
    'QQmlListProperty<QQuick3DMaterial>', which has no cute class yet.
  - Qt's 'QQuick3DMaterial
    *QQuick3DModel::qmlMaterialAt(QQmlListProperty<QQuick3DMaterial> *list,
    qsizetype index)': names 'QQmlListProperty<QQuick3DMaterial>', which has
    no cute class yet.
  - Qt's 'qsizetype
    QQuick3DModel::qmlMaterialsCount(QQmlListProperty<QQuick3DMaterial>
    *list)': names 'QQmlListProperty<QQuick3DMaterial>', which has no cute
    class yet.
  - Qt's 'void
    QQuick3DModel::qmlClearMaterials(QQmlListProperty<QQuick3DMaterial>
    *list)': names 'QQmlListProperty<QQuick3DMaterial>', which has no cute
    class yet.
  - Qt's 'void
    QQuick3DModel::qmlAppendMorphTarget(QQmlListProperty<QQuick3DMorphTarget>
    *list, QQuick3DMorphTarget *morphTarget)': names
    'QQmlListProperty<QQuick3DMorphTarget>', which has no cute class yet.
  - Qt's 'QQuick3DMorphTarget
    *QQuick3DModel::qmlMorphTargetAt(QQmlListProperty<QQuick3DMorphTarget>
    *list, qsizetype index)': names 'QQmlListProperty<QQuick3DMorphTarget>',
    which has no cute class yet.
  - Qt's 'qsizetype
    QQuick3DModel::qmlMorphTargetsCount(QQmlListProperty<QQuick3DMorphTarget>
    *list)': names 'QQmlListProperty<QQuick3DMorphTarget>', which has no cute
    class yet.
  - Qt's 'void
    QQuick3DModel::qmlClearMorphTargets(QQmlListProperty<QQuick3DMorphTarget>
    *list)': names 'QQmlListProperty<QQuick3DMorphTarget>', which has no cute
    class yet.

  What has no ritual
  ------------------

  2 of the 99 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DModel is created at the first use, not by
    'QQuick3DModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DModel.
  - Qt tells when it has removed the C++ QQuick3DModel. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DModel that has no cute function yet,
    'markDirty', 'materials', 'morphTargets', 'qmlAppendMaterial',
    'qmlAppendMorphTarget', 'qmlClearMaterials', 'qmlClearMorphTargets',
    'qmlMaterialAt', 'qmlMaterialsCount', 'qmlMorphTargetAt',
    'qmlMorphTargetsCount', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QQuick3DModel::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dmodel.html#tr

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
    #  QString QQuick3DModel::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QQuick3DModel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QUrl, QObject)
  @overload(QUrl, NoneType)
  def translateMeshSource(
      source: QUrl,
      contextObject: Optional[QObject],
  ) -> str:
    """
    Calls Qt's 'QString QQuick3DModel::translateMeshSource(const QUrl
    &source, QObject *contextObject)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#translateMeshSource

    Parameters
    ----------

    source : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    contextObject : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuick3DModel::translateMeshSource(const QUrl &source, QObject
    #      *contextObject)
    return Rituals.call(
        'ritual_ZN13QQuick3DModel19translateMeshSourceERK4QUrlP7QObject',
        CuteMixin._valueOf(source), CuteMixin._addressOf(contextObject,
        'QObject'),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DModel'

  #  A C++ QQuick3DModel Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DModel::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dmodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DModel::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QQuick3DModel10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def source(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuick3DModel::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dmodel.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuick3DModel::source() const
    address = self.uglySide.call('ritual_ZNK13QQuick3DModel6sourceEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def castsShadows(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DModel::castsShadows() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dmodel.html#castsShadows
    """
    #  bool QQuick3DModel::castsShadows() const
    return self.uglySide.call('ritual_ZNK13QQuick3DModel12castsShadowsEv')

  def receivesShadows(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DModel::receivesShadows() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dmodel.html#receivesShadows
    """
    #  bool QQuick3DModel::receivesShadows() const
    return self.uglySide.call('ritual_ZNK13QQuick3DModel15receivesShadowsEv')

  def pickable(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DModel::pickable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dmodel.html#pickable
    """
    #  bool QQuick3DModel::pickable() const
    return self.uglySide.call('ritual_ZNK13QQuick3DModel8pickableEv')

  def geometry(self) -> Optional[QQuick3DGeometry]:
    """
    Calls Qt's 'QQuick3DGeometry *QQuick3DModel::geometry() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dmodel.html#geometry

    Returns
    -------

    Optional[QQuick3DGeometry]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DGeometry *QQuick3DModel::geometry() const
    address = self.uglySide.call('ritual_ZNK13QQuick3DModel8geometryEv')
    from . import QQuick3DGeometry
    return QQuick3DGeometry._cuteAt(address)

  def skeleton(self) -> Optional[QQuick3DSkeleton]:
    """
    Calls Qt's 'QQuick3DSkeleton *QQuick3DModel::skeleton() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dmodel.html#skeleton

    Returns
    -------

    Optional[QQuick3DSkeleton]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DSkeleton *QQuick3DModel::skeleton() const
    address = self.uglySide.call('ritual_ZNK13QQuick3DModel8skeletonEv')
    from . import QQuick3DSkeleton
    return QQuick3DSkeleton._cuteAt(address)

  def inverseBindPoses(self) -> QList[QMatrix4x4]:
    """
    Calls Qt's 'QList<QMatrix4x4> QQuick3DModel::inverseBindPoses() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#inverseBindPoses

    Returns
    -------

    QList[QMatrix4x4]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QMatrix4x4> QQuick3DModel::inverseBindPoses() const
    address = self.uglySide.call(
        'ritual_ZNK13QQuick3DModel16inverseBindPosesEv',
    )
    from ..QtGui import QMatrix4x4
    return QList[QMatrix4x4]._cuteOwning(address)

  def bounds(self) -> QQuick3DBounds3:
    """
    Calls Qt's 'QQuick3DBounds3 QQuick3DModel::bounds() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dmodel.html#bounds

    Returns
    -------

    QQuick3DBounds3
      A new cute QQuick3DBounds3 around the copy Qt gave back. Python owns
      it.
    """
    #  QQuick3DBounds3 QQuick3DModel::bounds() const
    address = self.uglySide.call('ritual_ZNK13QQuick3DModel6boundsEv')
    from . import QQuick3DBounds3
    return QQuick3DBounds3._cuteOwning(address)

  def depthBias(self) -> float:
    """
    Calls Qt's 'float QQuick3DModel::depthBias() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dmodel.html#depthBias
    """
    #  float QQuick3DModel::depthBias() const
    return self.uglySide.call('ritual_ZNK13QQuick3DModel9depthBiasEv')

  def instancing(self) -> Optional[QQuick3DInstancing]:
    """
    Calls Qt's 'QQuick3DInstancing *QQuick3DModel::instancing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dmodel.html#instancing

    Returns
    -------

    Optional[QQuick3DInstancing]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DInstancing *QQuick3DModel::instancing() const
    address = self.uglySide.call('ritual_ZNK13QQuick3DModel10instancingEv')
    from . import QQuick3DInstancing
    return QQuick3DInstancing._cuteAt(address)

  def instanceRoot(self) -> Optional[QQuick3DNode]:
    """
    Calls Qt's 'QQuick3DNode *QQuick3DModel::instanceRoot() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dmodel.html#instanceRoot

    Returns
    -------

    Optional[QQuick3DNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DNode *QQuick3DModel::instanceRoot() const
    address = self.uglySide.call('ritual_ZNK13QQuick3DModel12instanceRootEv')
    return QQuick3DNode._cuteAt(address)

  def receivesReflections(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DModel::receivesReflections() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#receivesReflections
    """
    #  bool QQuick3DModel::receivesReflections() const
    return self.uglySide.call(
        'ritual_ZNK13QQuick3DModel19receivesReflectionsEv',
    )

  def castsReflections(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DModel::castsReflections() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#castsReflections
    """
    #  bool QQuick3DModel::castsReflections() const
    return self.uglySide.call(
        'ritual_ZNK13QQuick3DModel16castsReflectionsEv',
    )

  def skin(self) -> Optional[QQuick3DSkin]:
    """
    Calls Qt's 'QQuick3DSkin *QQuick3DModel::skin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dmodel.html#skin

    Returns
    -------

    Optional[QQuick3DSkin]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DSkin *QQuick3DModel::skin() const
    address = self.uglySide.call('ritual_ZNK13QQuick3DModel4skinEv')
    from . import QQuick3DSkin
    return QQuick3DSkin._cuteAt(address)

  def isUsedInBakedLighting(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DModel::isUsedInBakedLighting() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#isUsedInBakedLighting
    """
    #  bool QQuick3DModel::isUsedInBakedLighting() const
    return self.uglySide.call(
        'ritual_ZNK13QQuick3DModel21isUsedInBakedLightingEv',
    )

  def lightmapBaseResolution(self) -> int:
    """
    Calls Qt's 'int QQuick3DModel::lightmapBaseResolution() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#lightmapBaseResolution
    """
    #  int QQuick3DModel::lightmapBaseResolution() const
    return self.uglySide.call(
        'ritual_ZNK13QQuick3DModel22lightmapBaseResolutionEv',
    )

  def bakedLightmap(self) -> Optional[QQuick3DBakedLightmap]:
    """
    Calls Qt's 'QQuick3DBakedLightmap *QQuick3DModel::bakedLightmap() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dmodel.html#bakedLightmap

    Returns
    -------

    Optional[QQuick3DBakedLightmap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DBakedLightmap *QQuick3DModel::bakedLightmap() const
    address = self.uglySide.call(
        'ritual_ZNK13QQuick3DModel13bakedLightmapEv',
    )
    from . import QQuick3DBakedLightmap
    return QQuick3DBakedLightmap._cuteAt(address)

  def instancingLodMin(self) -> float:
    """
    Calls Qt's 'float QQuick3DModel::instancingLodMin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#instancingLodMin
    """
    #  float QQuick3DModel::instancingLodMin() const
    return self.uglySide.call(
        'ritual_ZNK13QQuick3DModel16instancingLodMinEv',
    )

  def instancingLodMax(self) -> float:
    """
    Calls Qt's 'float QQuick3DModel::instancingLodMax() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#instancingLodMax
    """
    #  float QQuick3DModel::instancingLodMax() const
    return self.uglySide.call(
        'ritual_ZNK13QQuick3DModel16instancingLodMaxEv',
    )

  def levelOfDetailBias(self) -> float:
    """
    Calls Qt's 'float QQuick3DModel::levelOfDetailBias() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#levelOfDetailBias
    """
    #  float QQuick3DModel::levelOfDetailBias() const
    return self.uglySide.call(
        'ritual_ZNK13QQuick3DModel17levelOfDetailBiasEv',
    )

  def instancingLodFactor(self) -> float:
    """
    Calls Qt's 'float QQuick3DModel::instancingLodFactor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#instancingLodFactor
    """
    #  float QQuick3DModel::instancingLodFactor() const
    return self.uglySide.call(
        'ritual_ZNK13QQuick3DModel19instancingLodFactorEv',
    )

  def texelsPerUnit(self) -> float:
    """
    Calls Qt's 'float QQuick3DModel::texelsPerUnit() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dmodel.html#texelsPerUnit
    """
    #  float QQuick3DModel::texelsPerUnit() const
    return self.uglySide.call('ritual_ZNK13QQuick3DModel13texelsPerUnitEv')

  def motionVectorEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DModel::motionVectorEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#motionVectorEnabled
    """
    #  bool QQuick3DModel::motionVectorEnabled() const
    return self.uglySide.call(
        'ritual_ZNK13QQuick3DModel19motionVectorEnabledEv',
    )

  def motionVectorScale(self) -> float:
    """
    Calls Qt's 'float QQuick3DModel::motionVectorScale() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#motionVectorScale
    """
    #  float QQuick3DModel::motionVectorScale() const
    return self.uglySide.call(
        'ritual_ZNK13QQuick3DModel17motionVectorScaleEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setTexelsPerUnit(self, newTexelsPerUnit: float) -> None:
    """
    Calls Qt's 'void QQuick3DModel::setTexelsPerUnit(float
    newTexelsPerUnit)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#setTexelsPerUnit

    Parameters
    ----------

    newTexelsPerUnit : float
      Passed on as it is.
    """
    #  void QQuick3DModel::setTexelsPerUnit(float newTexelsPerUnit)
    self.uglySide.call(
        'ritual_ZN13QQuick3DModel16setTexelsPerUnitEf', newTexelsPerUnit,
    )

  @overload(QUrl)
  def setSource(self, source: QUrl) -> None:
    """
    Calls Qt's 'void QQuick3DModel::setSource(const QUrl &source)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dmodel.html#setSource

    Parameters
    ----------

    source : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuick3DModel::setSource(const QUrl &source)
    self.uglySide.call(
        'ritual_ZN13QQuick3DModel9setSourceERK4QUrl', self._valueOf(source),
    )

  @overload(bool)
  def setCastsShadows(self, castsShadows: bool) -> None:
    """
    Calls Qt's 'void QQuick3DModel::setCastsShadows(bool castsShadows)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dmodel.html#setCastsShadows

    Parameters
    ----------

    castsShadows : bool
      Passed on as it is.
    """
    #  void QQuick3DModel::setCastsShadows(bool castsShadows)
    self.uglySide.call(
        'ritual_ZN13QQuick3DModel15setCastsShadowsEb', castsShadows,
    )

  @overload(bool)
  def setReceivesShadows(self, receivesShadows: bool) -> None:
    """
    Calls Qt's 'void QQuick3DModel::setReceivesShadows(bool
    receivesShadows)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#setReceivesShadows

    Parameters
    ----------

    receivesShadows : bool
      Passed on as it is.
    """
    #  void QQuick3DModel::setReceivesShadows(bool receivesShadows)
    self.uglySide.call(
        'ritual_ZN13QQuick3DModel18setReceivesShadowsEb', receivesShadows,
    )

  @overload(bool)
  def setPickable(self, pickable: bool) -> None:
    """
    Calls Qt's 'void QQuick3DModel::setPickable(bool pickable)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dmodel.html#setPickable

    Parameters
    ----------

    pickable : bool
      Passed on as it is.
    """
    #  void QQuick3DModel::setPickable(bool pickable)
    self.uglySide.call('ritual_ZN13QQuick3DModel11setPickableEb', pickable)

  @overload(QQuick3DGeometry)
  @overload(NoneType)
  def setGeometry(self, geometry: Optional[QQuick3DGeometry]) -> None:
    """
    Calls Qt's 'void QQuick3DModel::setGeometry(QQuick3DGeometry *geometry)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dmodel.html#setGeometry

    Parameters
    ----------

    geometry : Optional[QQuick3DGeometry]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DModel::setGeometry(QQuick3DGeometry *geometry)
    self.uglySide.call(
        'ritual_ZN13QQuick3DModel11setGeometryEP16QQuick3DGeometry',
        self._addressOf(geometry),
    )

  @overload(QQuick3DSkeleton)
  @overload(NoneType)
  def setSkeleton(self, skeleton: Optional[QQuick3DSkeleton]) -> None:
    """
    Calls Qt's 'void QQuick3DModel::setSkeleton(QQuick3DSkeleton *skeleton)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dmodel.html#setSkeleton

    Parameters
    ----------

    skeleton : Optional[QQuick3DSkeleton]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DModel::setSkeleton(QQuick3DSkeleton *skeleton)
    self.uglySide.call(
        'ritual_ZN13QQuick3DModel11setSkeletonEP16QQuick3DSkeleton',
        self._addressOf(skeleton),
    )

  @overload(QList[QMatrix4x4])
  def setInverseBindPoses(self, poses: QList[QMatrix4x4]) -> None:
    """
    Calls Qt's 'void QQuick3DModel::setInverseBindPoses(const
    QList<QMatrix4x4> &poses)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#setInverseBindPoses

    Parameters
    ----------

    poses : QList[QMatrix4x4]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQuick3DModel::setInverseBindPoses(const QList<QMatrix4x4>
    #      &poses)
    self.uglySide.call(
        'ritual_ZN13QQuick3DModel19setInverseBindPosesERK5QListI10QMatrix4x'
        '4E',
        self._valueOf(poses),
    )

  @overload(QVector3D, QVector3D)
  def setBounds(self, min: QVector3D, max: QVector3D) -> None:
    """
    Calls Qt's 'void QQuick3DModel::setBounds(const QVector3D &min, const
    QVector3D &max)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dmodel.html#setBounds

    Parameters
    ----------

    min : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    max : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuick3DModel::setBounds(const QVector3D &min, const QVector3D
    #      &max)
    self.uglySide.call(
        'ritual_ZN13QQuick3DModel9setBoundsERK9QVector3DS2_',
        self._valueOf(min), self._valueOf(max),
    )

  @overload(QQuick3DInstancing)
  @overload(NoneType)
  def setInstancing(self, instancing: Optional[QQuick3DInstancing]) -> None:
    """
    Calls Qt's 'void QQuick3DModel::setInstancing(QQuick3DInstancing
    *instancing)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dmodel.html#setInstancing

    Parameters
    ----------

    instancing : Optional[QQuick3DInstancing]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DModel::setInstancing(QQuick3DInstancing *instancing)
    self.uglySide.call(
        'ritual_ZN13QQuick3DModel13setInstancingEP18QQuick3DInstancing',
        self._addressOf(instancing),
    )

  @overload(QQuick3DNode)
  @overload(NoneType)
  def setInstanceRoot(self, instanceRoot: Optional[QQuick3DNode]) -> None:
    """
    Calls Qt's 'void QQuick3DModel::setInstanceRoot(QQuick3DNode
    *instanceRoot)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dmodel.html#setInstanceRoot

    Parameters
    ----------

    instanceRoot : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DModel::setInstanceRoot(QQuick3DNode *instanceRoot)
    self.uglySide.call(
        'ritual_ZN13QQuick3DModel15setInstanceRootEP12QQuick3DNode',
        self._addressOf(instanceRoot),
    )

  @overload(float)
  def setDepthBias(self, bias: float) -> None:
    """
    Calls Qt's 'void QQuick3DModel::setDepthBias(float bias)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dmodel.html#setDepthBias

    Parameters
    ----------

    bias : float
      Passed on as it is.
    """
    #  void QQuick3DModel::setDepthBias(float bias)
    self.uglySide.call('ritual_ZN13QQuick3DModel12setDepthBiasEf', bias)

  @overload(bool)
  def setReceivesReflections(self, receivesReflections: bool) -> None:
    """
    Calls Qt's 'void QQuick3DModel::setReceivesReflections(bool
    receivesReflections)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#setReceivesReflections

    Parameters
    ----------

    receivesReflections : bool
      Passed on as it is.
    """
    #  void QQuick3DModel::setReceivesReflections(bool receivesReflections)
    self.uglySide.call(
        'ritual_ZN13QQuick3DModel22setReceivesReflectionsEb',
        receivesReflections,
    )

  @overload(bool)
  def setCastsReflections(self, castsReflections: bool) -> None:
    """
    Calls Qt's 'void QQuick3DModel::setCastsReflections(bool
    castsReflections)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#setCastsReflections

    Parameters
    ----------

    castsReflections : bool
      Passed on as it is.
    """
    #  void QQuick3DModel::setCastsReflections(bool castsReflections)
    self.uglySide.call(
        'ritual_ZN13QQuick3DModel19setCastsReflectionsEb', castsReflections,
    )

  @overload(QQuick3DSkin)
  @overload(NoneType)
  def setSkin(self, skin: Optional[QQuick3DSkin]) -> None:
    """
    Calls Qt's 'void QQuick3DModel::setSkin(QQuick3DSkin *skin)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dmodel.html#setSkin

    Parameters
    ----------

    skin : Optional[QQuick3DSkin]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DModel::setSkin(QQuick3DSkin *skin)
    self.uglySide.call(
        'ritual_ZN13QQuick3DModel7setSkinEP12QQuick3DSkin',
        self._addressOf(skin),
    )

  @overload(bool)
  def setUsedInBakedLighting(self, enable: bool) -> None:
    """
    Calls Qt's 'void QQuick3DModel::setUsedInBakedLighting(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#setUsedInBakedLighting

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QQuick3DModel::setUsedInBakedLighting(bool enable)
    self.uglySide.call(
        'ritual_ZN13QQuick3DModel22setUsedInBakedLightingEb', enable,
    )

  @overload(int)
  def setLightmapBaseResolution(self, resolution: int) -> None:
    """
    Calls Qt's 'void QQuick3DModel::setLightmapBaseResolution(int
    resolution)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#setLightmapBaseResolution

    Parameters
    ----------

    resolution : int
      Passed on as it is.
    """
    #  void QQuick3DModel::setLightmapBaseResolution(int resolution)
    self.uglySide.call(
        'ritual_ZN13QQuick3DModel25setLightmapBaseResolutionEi', resolution,
    )

  @overload(QQuick3DBakedLightmap)
  @overload(NoneType)
  def setBakedLightmap(
      self,
      bakedLightmap: Optional[QQuick3DBakedLightmap],
  ) -> None:
    """
    Calls Qt's 'void QQuick3DModel::setBakedLightmap(QQuick3DBakedLightmap
    *bakedLightmap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#setBakedLightmap

    Parameters
    ----------

    bakedLightmap : Optional[QQuick3DBakedLightmap]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DModel::setBakedLightmap(QQuick3DBakedLightmap
    #      *bakedLightmap)
    self.uglySide.call(
        'ritual_ZN13QQuick3DModel16setBakedLightmapEP21QQuick3DBakedLightma'
        'p',
        self._addressOf(bakedLightmap),
    )

  @overload(float)
  def setInstancingLodMin(self, minDistance: float) -> None:
    """
    Calls Qt's 'void QQuick3DModel::setInstancingLodMin(float minDistance)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#setInstancingLodMin

    Parameters
    ----------

    minDistance : float
      Passed on as it is.
    """
    #  void QQuick3DModel::setInstancingLodMin(float minDistance)
    self.uglySide.call(
        'ritual_ZN13QQuick3DModel19setInstancingLodMinEf', minDistance,
    )

  @overload(float)
  def setInstancingLodMax(self, maxDistance: float) -> None:
    """
    Calls Qt's 'void QQuick3DModel::setInstancingLodMax(float maxDistance)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#setInstancingLodMax

    Parameters
    ----------

    maxDistance : float
      Passed on as it is.
    """
    #  void QQuick3DModel::setInstancingLodMax(float maxDistance)
    self.uglySide.call(
        'ritual_ZN13QQuick3DModel19setInstancingLodMaxEf', maxDistance,
    )

  @overload(float)
  def setLevelOfDetailBias(self, newLevelOfDetailBias: float) -> None:
    """
    Calls Qt's 'void QQuick3DModel::setLevelOfDetailBias(float
    newLevelOfDetailBias)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#setLevelOfDetailBias

    Parameters
    ----------

    newLevelOfDetailBias : float
      Passed on as it is.
    """
    #  void QQuick3DModel::setLevelOfDetailBias(float newLevelOfDetailBias)
    self.uglySide.call(
        'ritual_ZN13QQuick3DModel20setLevelOfDetailBiasEf',
        newLevelOfDetailBias,
    )

  @overload(float)
  def setInstancingLodFactor(self, newInstancingLodFactor: float) -> None:
    """
    Calls Qt's 'void QQuick3DModel::setInstancingLodFactor(float
    newInstancingLodFactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#setInstancingLodFactor

    Parameters
    ----------

    newInstancingLodFactor : float
      Passed on as it is.
    """
    #  void QQuick3DModel::setInstancingLodFactor(float
    #      newInstancingLodFactor)
    self.uglySide.call(
        'ritual_ZN13QQuick3DModel22setInstancingLodFactorEf',
        newInstancingLodFactor,
    )

  @overload(float)
  def setMotionVectorScale(self, newMotionVectorScale: float) -> None:
    """
    Calls Qt's 'void QQuick3DModel::setMotionVectorScale(float
    newMotionVectorScale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#setMotionVectorScale

    Parameters
    ----------

    newMotionVectorScale : float
      Passed on as it is.
    """
    #  void QQuick3DModel::setMotionVectorScale(float newMotionVectorScale)
    self.uglySide.call(
        'ritual_ZN13QQuick3DModel20setMotionVectorScaleEf',
        newMotionVectorScale,
    )

  @overload(bool)
  def setMotionVectorEnabled(self, newMotionVectorEnabled: bool) -> None:
    """
    Calls Qt's 'void QQuick3DModel::setMotionVectorEnabled(bool
    newMotionVectorEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#setMotionVectorEnabled

    Parameters
    ----------

    newMotionVectorEnabled : bool
      Passed on as it is.
    """
    #  void QQuick3DModel::setMotionVectorEnabled(bool
    #      newMotionVectorEnabled)
    self.uglySide.call(
        'ritual_ZN13QQuick3DModel22setMotionVectorEnabledEb',
        newMotionVectorEnabled,
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
    Notes what was given, for Qt's 'QQuick3DModel::QQuick3DModel(QQuick3DNode
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dmodel.html#QQuick3DModel

    Parameters
    ----------

    parent : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DModel::QQuick3DModel(QQuick3DNode *parent)
    self._noteCreation(QQuick3DModel, lambda: Rituals.call(
        'ritual_ZN13QQuick3DModelC1EP12QQuick3DNode',
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

  def sourceChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DModel::sourceChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dmodel.html#sourceChanged
    """
    #  void QQuick3DModel::sourceChanged()
    self.uglySide.call('ritual_ZN13QQuick3DModel13sourceChangedEv')

  def castsShadowsChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DModel::castsShadowsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#castsShadowsChanged
    """
    #  void QQuick3DModel::castsShadowsChanged()
    self.uglySide.call('ritual_ZN13QQuick3DModel19castsShadowsChangedEv')

  def receivesShadowsChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DModel::receivesShadowsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#receivesShadowsChanged
    """
    #  void QQuick3DModel::receivesShadowsChanged()
    self.uglySide.call('ritual_ZN13QQuick3DModel22receivesShadowsChangedEv')

  def pickableChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DModel::pickableChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dmodel.html#pickableChanged
    """
    #  void QQuick3DModel::pickableChanged()
    self.uglySide.call('ritual_ZN13QQuick3DModel15pickableChangedEv')

  def geometryChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DModel::geometryChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dmodel.html#geometryChanged
    """
    #  void QQuick3DModel::geometryChanged()
    self.uglySide.call('ritual_ZN13QQuick3DModel15geometryChangedEv')

  def skeletonChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DModel::skeletonChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dmodel.html#skeletonChanged
    """
    #  void QQuick3DModel::skeletonChanged()
    self.uglySide.call('ritual_ZN13QQuick3DModel15skeletonChangedEv')

  def inverseBindPosesChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DModel::inverseBindPosesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#inverseBindPosesChanged
    """
    #  void QQuick3DModel::inverseBindPosesChanged()
    self.uglySide.call('ritual_ZN13QQuick3DModel23inverseBindPosesChangedEv')

  def boundsChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DModel::boundsChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dmodel.html#boundsChanged
    """
    #  void QQuick3DModel::boundsChanged()
    self.uglySide.call('ritual_ZN13QQuick3DModel13boundsChangedEv')

  def instancingChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DModel::instancingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#instancingChanged
    """
    #  void QQuick3DModel::instancingChanged()
    self.uglySide.call('ritual_ZN13QQuick3DModel17instancingChangedEv')

  def instanceRootChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DModel::instanceRootChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#instanceRootChanged
    """
    #  void QQuick3DModel::instanceRootChanged()
    self.uglySide.call('ritual_ZN13QQuick3DModel19instanceRootChangedEv')

  def morphTargetsChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DModel::morphTargetsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#morphTargetsChanged
    """
    #  void QQuick3DModel::morphTargetsChanged()
    self.uglySide.call('ritual_ZN13QQuick3DModel19morphTargetsChangedEv')

  def depthBiasChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DModel::depthBiasChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#depthBiasChanged
    """
    #  void QQuick3DModel::depthBiasChanged()
    self.uglySide.call('ritual_ZN13QQuick3DModel16depthBiasChangedEv')

  def receivesReflectionsChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DModel::receivesReflectionsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#receivesReflectionsChanged
    """
    #  void QQuick3DModel::receivesReflectionsChanged()
    self.uglySide.call(
        'ritual_ZN13QQuick3DModel26receivesReflectionsChangedEv',
    )

  def castsReflectionsChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DModel::castsReflectionsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#castsReflectionsChanged
    """
    #  void QQuick3DModel::castsReflectionsChanged()
    self.uglySide.call('ritual_ZN13QQuick3DModel23castsReflectionsChangedEv')

  def skinChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DModel::skinChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dmodel.html#skinChanged
    """
    #  void QQuick3DModel::skinChanged()
    self.uglySide.call('ritual_ZN13QQuick3DModel11skinChangedEv')

  def usedInBakedLightingChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DModel::usedInBakedLightingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#usedInBakedLightingChanged
    """
    #  void QQuick3DModel::usedInBakedLightingChanged()
    self.uglySide.call(
        'ritual_ZN13QQuick3DModel26usedInBakedLightingChangedEv',
    )

  def lightmapBaseResolutionChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DModel::lightmapBaseResolutionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#lightmapBaseResolutionChanged
    """
    #  void QQuick3DModel::lightmapBaseResolutionChanged()
    self.uglySide.call(
        'ritual_ZN13QQuick3DModel29lightmapBaseResolutionChangedEv',
    )

  def bakedLightmapChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DModel::bakedLightmapChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#bakedLightmapChanged
    """
    #  void QQuick3DModel::bakedLightmapChanged()
    self.uglySide.call('ritual_ZN13QQuick3DModel20bakedLightmapChangedEv')

  def instancingLodMinChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DModel::instancingLodMinChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#instancingLodMinChanged
    """
    #  void QQuick3DModel::instancingLodMinChanged()
    self.uglySide.call('ritual_ZN13QQuick3DModel23instancingLodMinChangedEv')

  def instancingLodMaxChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DModel::instancingLodMaxChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#instancingLodMaxChanged
    """
    #  void QQuick3DModel::instancingLodMaxChanged()
    self.uglySide.call('ritual_ZN13QQuick3DModel23instancingLodMaxChangedEv')

  def instancingLodFactorChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DModel::instancingLodFactorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#instancingLodFactorChanged
    """
    #  void QQuick3DModel::instancingLodFactorChanged()
    self.uglySide.call(
        'ritual_ZN13QQuick3DModel26instancingLodFactorChangedEv',
    )

  def levelOfDetailBiasChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DModel::levelOfDetailBiasChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#levelOfDetailBiasChanged
    """
    #  void QQuick3DModel::levelOfDetailBiasChanged()
    self.uglySide.call(
        'ritual_ZN13QQuick3DModel24levelOfDetailBiasChangedEv',
    )

  def texelsPerUnitChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DModel::texelsPerUnitChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#texelsPerUnitChanged
    """
    #  void QQuick3DModel::texelsPerUnitChanged()
    self.uglySide.call('ritual_ZN13QQuick3DModel20texelsPerUnitChangedEv')

  def motionVectorEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DModel::motionVectorEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#motionVectorEnabledChanged
    """
    #  void QQuick3DModel::motionVectorEnabledChanged()
    self.uglySide.call(
        'ritual_ZN13QQuick3DModel26motionVectorEnabledChangedEv',
    )

  def motionVectorScaleChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DModel::motionVectorScaleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#motionVectorScaleChanged
    """
    #  void QQuick3DModel::motionVectorScaleChanged()
    self.uglySide.call(
        'ritual_ZN13QQuick3DModel24motionVectorScaleChangedEv',
    )

  @overload(QSSGRenderGraphObject)
  @overload(NoneType)
  def updateSpatialNode(
      self,
      node: Optional[QSSGRenderGraphObject],
  ) -> Optional[QSSGRenderGraphObject]:
    """
    Calls Qt's 'QSSGRenderGraphObject
    *QQuick3DModel::updateSpatialNode(QSSGRenderGraphObject *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#updateSpatialNode

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
    #      *QQuick3DModel::updateSpatialNode(QSSGRenderGraphObject *node)
    ritual = (
        'ritual_ZN13QQuick3DModel17updateSpatialNodeEP21QSSGRenderGraphObje'
        'ct')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13QQuick3DModel17updateSpatialNodeEP21QSSGRenderGra'
          'phObject')
    address = self.uglySide.call(ritual, self._addressOf(node))
    from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
    return QSSGRenderGraphObject._cuteAt(address)

  def markAllDirty(self) -> None:
    """
    Calls Qt's 'void QQuick3DModel::markAllDirty()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dmodel.html#markAllDirty
    """
    #  void QQuick3DModel::markAllDirty()
    ritual = 'ritual_ZN13QQuick3DModel12markAllDirtyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuick3DModel12markAllDirtyEv'
    self.uglySide.call(ritual)

  @overload(QQuick3DObject.ItemChange, QQuick3DObject.ItemChangeData)
  def itemChange(
      self,
      a0: QQuick3DObject.ItemChange,
      a1: QQuick3DObject.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DModel::itemChange(ItemChange a0, const
    ItemChangeData &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dmodel.html#itemChange

    Parameters
    ----------

    a0 : QQuick3DObject.ItemChange
      Passed on as its number.

    a1 : QQuick3DObject.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuick3DObject::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuick3DModel::itemChange(ItemChange a0, const ItemChangeData
    #      &a1)
    ritual = (
        'ritual_ZN13QQuick3DModel10itemChangeEN14QQuick3DObject10ItemChange'
        'ERKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13QQuick3DModel10itemChangeEN14QQuick3DObject10Item'
          'ChangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, a0.value, self._valueOf(a1))

  @overload(QObject)
  @overload(NoneType)
  def onMaterialDestroyed(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuick3DModel::onMaterialDestroyed(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#onMaterialDestroyed

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DModel::onMaterialDestroyed(QObject *object)
    self.uglySide.call(
        'ritual_ZN13QQuick3DModel19onMaterialDestroyedEP7QObject',
        self._addressOf(object, 'QObject'),
    )

  @overload(QObject)
  @overload(NoneType)
  def onMorphTargetDestroyed(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuick3DModel::onMorphTargetDestroyed(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#onMorphTargetDestroyed

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DModel::onMorphTargetDestroyed(QObject *object)
    self.uglySide.call(
        'ritual_ZN13QQuick3DModel22onMorphTargetDestroyedEP7QObject',
        self._addressOf(object, 'QObject'),
    )

  @overload(QQuick3DSceneManager)
  @overload(NoneType)
  def updateSceneManager(
      self,
      sceneManager: Optional[QQuick3DSceneManager],
  ) -> None:
    """
    Calls Qt's 'void QQuick3DModel::updateSceneManager(QQuick3DSceneManager
    *sceneManager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmodel.html#updateSceneManager

    Parameters
    ----------

    sceneManager : Optional[QQuick3DSceneManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DModel::updateSceneManager(QQuick3DSceneManager
    #      *sceneManager)
    self.uglySide.call(
        'ritual_ZN13QQuick3DModel18updateSceneManagerEP20QQuick3DSceneManag'
        'er',
        self._addressOf(sceneManager),
    )

  @staticmethod
  def markDirty(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DModel::markDirty(QSSGModelDirtyType type)': names the
    enum 'QQuick3DModel::QSSGModelDirtyType', whose class cannot be named
    here.
    """
    raise NotImplementedError(
        "'QQuick3DModel.markDirty' has no cute function yet. Qt's 'void "
        "QQuick3DModel::markDirty(QSSGModelDirtyType type)': names the enum "
        "'QQuick3DModel::QSSGModelDirtyType', whose class cannot be named "
        "here.")

  @staticmethod
  def materials(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuick3DMaterial> QQuick3DModel::materials()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuick3DModel.materials' has no cute function yet. Qt's "
        "'QQmlListProperty<QQuick3DMaterial> QQuick3DModel::materials()': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def morphTargets(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuick3DMorphTarget>
    QQuick3DModel::morphTargets()': gives a type Python has no way to take
    yet.
    """
    raise NotImplementedError(
        "'QQuick3DModel.morphTargets' has no cute function yet. Qt's "
        "'QQmlListProperty<QQuick3DMorphTarget> "
        "QQuick3DModel::morphTargets()': gives a type Python has no way to "
        "take yet.")

  @staticmethod
  def qmlAppendMaterial(*__, **_) -> Never:
    """
    Qt's 'void
    QQuick3DModel::qmlAppendMaterial(QQmlListProperty<QQuick3DMaterial>
    *list, QQuick3DMaterial *material)': names
    'QQmlListProperty<QQuick3DMaterial>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuick3DModel.qmlAppendMaterial' has no cute function yet. Qt's "
        "'void "
        "QQuick3DModel::qmlAppendMaterial(QQmlListProperty<QQuick3DMaterial>"
        " *list, QQuick3DMaterial *material)': names "
        "'QQmlListProperty<QQuick3DMaterial>', which has no cute class yet.")

  @staticmethod
  def qmlAppendMorphTarget(*__, **_) -> Never:
    """
    Qt's 'void
    QQuick3DModel::qmlAppendMorphTarget(QQmlListProperty<QQuick3DMorphTarget>
    *list, QQuick3DMorphTarget *morphTarget)': names
    'QQmlListProperty<QQuick3DMorphTarget>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuick3DModel.qmlAppendMorphTarget' has no cute function yet. "
        "Qt's 'void "
        "QQuick3DModel::qmlAppendMorphTarget(QQmlListProperty<QQuick3DMorphT"
        "arget> *list, QQuick3DMorphTarget *morphTarget)': names "
        "'QQmlListProperty<QQuick3DMorphTarget>', which has no cute class "
        "yet.")

  @staticmethod
  def qmlClearMaterials(*__, **_) -> Never:
    """
    Qt's 'void
    QQuick3DModel::qmlClearMaterials(QQmlListProperty<QQuick3DMaterial>
    *list)': names 'QQmlListProperty<QQuick3DMaterial>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuick3DModel.qmlClearMaterials' has no cute function yet. Qt's "
        "'void "
        "QQuick3DModel::qmlClearMaterials(QQmlListProperty<QQuick3DMaterial>"
        " *list)': names 'QQmlListProperty<QQuick3DMaterial>', which has no "
        "cute class yet.")

  @staticmethod
  def qmlClearMorphTargets(*__, **_) -> Never:
    """
    Qt's 'void
    QQuick3DModel::qmlClearMorphTargets(QQmlListProperty<QQuick3DMorphTarget>
    *list)': names 'QQmlListProperty<QQuick3DMorphTarget>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuick3DModel.qmlClearMorphTargets' has no cute function yet. "
        "Qt's 'void "
        "QQuick3DModel::qmlClearMorphTargets(QQmlListProperty<QQuick3DMorphT"
        "arget> *list)': names 'QQmlListProperty<QQuick3DMorphTarget>', "
        "which has no cute class yet.")

  @staticmethod
  def qmlMaterialAt(*__, **_) -> Never:
    """
    Qt's 'QQuick3DMaterial
    *QQuick3DModel::qmlMaterialAt(QQmlListProperty<QQuick3DMaterial> *list,
    qsizetype index)': names 'QQmlListProperty<QQuick3DMaterial>', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QQuick3DModel.qmlMaterialAt' has no cute function yet. Qt's "
        "'QQuick3DMaterial "
        "*QQuick3DModel::qmlMaterialAt(QQmlListProperty<QQuick3DMaterial> "
        "*list, qsizetype index)': names "
        "'QQmlListProperty<QQuick3DMaterial>', which has no cute class yet.")

  @staticmethod
  def qmlMaterialsCount(*__, **_) -> Never:
    """
    Qt's 'qsizetype
    QQuick3DModel::qmlMaterialsCount(QQmlListProperty<QQuick3DMaterial>
    *list)': names 'QQmlListProperty<QQuick3DMaterial>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuick3DModel.qmlMaterialsCount' has no cute function yet. Qt's "
        "'qsizetype "
        "QQuick3DModel::qmlMaterialsCount(QQmlListProperty<QQuick3DMaterial>"
        " *list)': names 'QQmlListProperty<QQuick3DMaterial>', which has no "
        "cute class yet.")

  @staticmethod
  def qmlMorphTargetAt(*__, **_) -> Never:
    """
    Qt's 'QQuick3DMorphTarget
    *QQuick3DModel::qmlMorphTargetAt(QQmlListProperty<QQuick3DMorphTarget>
    *list, qsizetype index)': names 'QQmlListProperty<QQuick3DMorphTarget>',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuick3DModel.qmlMorphTargetAt' has no cute function yet. Qt's "
        "'QQuick3DMorphTarget "
        "*QQuick3DModel::qmlMorphTargetAt(QQmlListProperty<QQuick3DMorphTarg"
        "et> *list, qsizetype index)': names "
        "'QQmlListProperty<QQuick3DMorphTarget>', which has no cute class "
        "yet.")

  @staticmethod
  def qmlMorphTargetsCount(*__, **_) -> Never:
    """
    Qt's 'qsizetype
    QQuick3DModel::qmlMorphTargetsCount(QQmlListProperty<QQuick3DMorphTarget>
    *list)': names 'QQmlListProperty<QQuick3DMorphTarget>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuick3DModel.qmlMorphTargetsCount' has no cute function yet. "
        "Qt's 'qsizetype "
        "QQuick3DModel::qmlMorphTargetsCount(QQmlListProperty<QQuick3DMorphT"
        "arget> *list)': names 'QQmlListProperty<QQuick3DMorphTarget>', "
        "which has no cute class yet.")
