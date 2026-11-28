"""
QQuick3DViewport binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dviewport_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DViewport to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList
from ..QtQuick import QQuickItem, QQuickShaderEffectSource

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject, QPointF, QRectF, QSize
  from ..QtGui import QPointerEvent, QSinglePointEvent, QVector3D
  from ..QtQml import QJSValue
  from ..QtQuick import QSGNode, QSGTextureProvider
  from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
  from ..QtQuick3DRuntimeRender import QSSGRenderPickResult
  from . import QQuick3DCamera, QQuick3DLightmapBaker, QQuick3DMaterial
  from . import QQuick3DModel, QQuick3DNode, QQuick3DObject
  from . import QQuick3DPickResult, QQuick3DRenderStats
  from . import QQuick3DSceneEnvironment, QQuick3DSceneManager
  from . import QQuick3DSceneRenderer
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QJSValue = WAIT['QJSValue']
  QPointF = WAIT['QPointF']
  QPointerEvent = WAIT['QPointerEvent']
  QQuick3DCamera = WAIT['QQuick3DCamera']
  QQuick3DMaterial = WAIT['QQuick3DMaterial']
  QQuick3DModel = WAIT['QQuick3DModel']
  QQuick3DNode = WAIT['QQuick3DNode']
  QQuick3DObject = WAIT['QQuick3DObject']
  QQuick3DSceneEnvironment = WAIT['QQuick3DSceneEnvironment']
  QQuick3DSceneManager = WAIT['QQuick3DSceneManager']
  QRectF = WAIT['QRectF']
  QSGNode = WAIT['QSGNode']
  QSSGRenderGraphObject = WAIT['QSSGRenderGraphObject']
  QSSGRenderPickResult = WAIT['QSSGRenderPickResult']
  QSinglePointEvent = WAIT['QSinglePointEvent']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DViewport(QQuickItem):
  """
  The cute side of Qt's QQuick3DViewport: a plain Python object standing in
  front of one C++ QQuick3DViewport.

  It is built on the cute 'QQuickItem', as Qt's QQuick3DViewport is built on
  Qt's QQuickItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DViewport that has a ritual and that Python
  can call so far, 78 names in all: 'metaObject', 'tr', 'camera',
  'environment', 'scene', 'importScene', 'renderMode', 'renderFormat',
  'renderStats', 'createRenderer', 'isTextureProvider', 'textureProvider',
  'releaseResources', 'mapFrom3DScene', 'mapTo3DScene', 'pick', 'pickSubset',
  'pickAll', 'rayPick', 'rayPickAll', 'closestPointPick', 'pickInRect',
  'processPointerEventFromRay', 'singlePointPick', 'setTouchpoint',
  'maybeLightmapBaker', 'lightmapBaker', 'bakeLightmap', 'denoiseLightmap',
  'explicitTextureWidth', 'explicitTextureHeight', 'effectiveTextureSize',
  'extensionListDirty', 'extensionList', 'clearExtensionListDirty',
  'rebuildExtensionList', 'isXrViewInstance', 'renderOverrides',
  'setRenderOverrides', 'geometryChange', 'updatePaintNode', 'itemChange',
  'event', 'componentComplete', 'setCamera', 'setEnvironment',
  'setImportScene', 'setRenderMode', 'setRenderFormat',
  'setExplicitTextureWidth', 'setExplicitTextureHeight',
  'cleanupDirectRenderer', 'setGlobalPickingEnabled', 'invalidateSceneGraph',
  'updateInputProcessing', 'onReleaseCachedResources', 'cameraChanged',
  'environmentChanged', 'sceneChanged', 'importSceneChanged',
  'renderModeChanged', 'renderFormatChanged', 'explicitTextureWidthChanged',
  'explicitTextureHeightChanged', 'effectiveTextureSizeChanged',
  'renderOverridesChanged', 'getRenderer', 'updateDynamicTextures',
  'setupOffscreenRenderer', 'setupInlineRenderer', 'setupDirectRenderer',
  'checkIsVisible', 'internalPick', 'getSubSceneRootItem',
  'processPickResult', 'findFrontendNode', 'findChildSceneManager',
  'updateSceneManagerForImportScene'. It can be made from Python, in 2 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DViewport::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuick3DViewport::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DViewport::~QQuick3DViewport()': the destructor: Python
    never removes a C++ QQuick3DViewport.
  - Qt's 'QQmlListProperty<QObject> QQuick3DViewport::data()': gives a type
    Python has no way to take yet.
  - Qt's 'QQmlListProperty<QQuick3DObject> QQuick3DViewport::extensions()':
    gives a type Python has no way to take yet.
  - Qt's 'void QQuick3DViewport::updateCameraForLayer(const QQuick3DViewport
    &view3D, QSSGRenderLayer &layerNode)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QQuick3DViewport::setMultiViewCameras(QQuick3DCamera
    **firstCamera, int count)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QPair<QQuickItem *, QPointF>
    QQuick3DViewport::getItemAndPosition(const QSSGRenderPickResult
    &pickResult) const': gives a type Python has no way to take yet.
  - Qt's 'QVarLengthArray<QSSGRenderPickResult, 20>
    QQuick3DViewport::getPickResults(QQuick3DSceneRenderer *renderer, const
    QVector3D &origin, const QVector3D &direction) const': gives a type
    Python has no way to take yet.
  - Qt's 'QVarLengthArray<QSSGRenderPickResult, 20>
    QQuick3DViewport::getPickResults(QQuick3DSceneRenderer *renderer, const
    QEventPoint &eventPoint) const': gives a type Python has no way to take
    yet.
  - Qt's 'bool QQuick3DViewport::forwardEventToSubscenes(QPointerEvent
    *event, bool useRayPicking, QQuick3DSceneRenderer *renderer, const
    QFlatMap<QQuickItem *, SubsceneInfo> &visitedSubscenes) const': takes a
    type Python has no way to hand over yet.
  - Qt's 'void QQuick3DViewport::processPickedObject(const
    QSSGRenderPickResult &pickResult, int pointIndex, QPointerEvent *event,
    QFlatMap<QQuickItem *, SubsceneInfo> &vistedSubscenes) const': takes a
    type Python has no way to hand over yet.
  - Qt's 'QQuick3DPickResult QQuick3DViewport::getNearestPickResult(const
    QVarLengthArray<QSSGRenderPickResult, 20> &pickResults) const': takes a
    type Python has no way to hand over yet.

  What has no ritual
  ------------------

  5 of the 100 functions Qt declares: 2 not a gap; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QQuick3DViewport is created at the first use, not by
    'QQuick3DViewport(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DViewport.
  - Qt tells when it has removed the C++ QQuick3DViewport. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DViewport that has no cute function yet, 'data',
    'extensions', 'forwardEventToSubscenes', 'getItemAndPosition',
    'getNearestPickResult', 'getPickResults', 'processPickedObject',
    'setMultiViewCameras', 'updateCameraForLayer', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuick3DViewport, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class PrivateInstanceType(CuteNum, scoped=True):
    """
    The enum 'QQuick3DViewport::PrivateInstanceType' of Qt, with the 1 names
    Qt gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    XrViewInstance = Kee[int](1)

  class RenderMode(CuteNum):
    """
    The enum 'QQuick3DViewport::RenderMode' of Qt, with the 4 names Qt gives
    in it.
    """

    Offscreen = Kee[int](0)
    Underlay = Kee[int](1)
    Overlay = Kee[int](2)
    Inline = Kee[int](3)

  class RenderOverride(CuteFlags, scoped=True):
    """
    The flags enum 'QQuick3DViewport::RenderOverride' of Qt, with the 2 names
    Qt gives in it. Qt names the type of its combinations
    'QQuick3DViewport::RenderOverrides'. C++ keeps these names inside the
    enum, so the class that holds the enum does not have them.
    """

    NULL = 0x0
    DisableInternalPasses = 0x1

  RenderOverrides = RenderOverride

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
    Calls Qt's 'QString QQuick3DViewport::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dviewport.html#tr

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
    #  QString QQuick3DViewport::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QQuick3DViewport2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DViewport'

  #  A C++ QQuick3DViewport Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DViewport'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DViewport::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dviewport.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DViewport::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuick3DViewport10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def camera(self) -> Optional[QQuick3DCamera]:
    """
    Calls Qt's 'QQuick3DCamera *QQuick3DViewport::camera() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dviewport.html#camera

    Returns
    -------

    Optional[QQuick3DCamera]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DCamera *QQuick3DViewport::camera() const
    address = self.uglySide.call('ritual_ZNK16QQuick3DViewport6cameraEv')
    from . import QQuick3DCamera
    return QQuick3DCamera._cuteAt(address)

  def environment(self) -> Optional[QQuick3DSceneEnvironment]:
    """
    Calls Qt's 'QQuick3DSceneEnvironment *QQuick3DViewport::environment()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dviewport.html#environment

    Returns
    -------

    Optional[QQuick3DSceneEnvironment]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DSceneEnvironment *QQuick3DViewport::environment() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuick3DViewport11environmentEv',
    )
    from . import QQuick3DSceneEnvironment
    return QQuick3DSceneEnvironment._cuteAt(address)

  def scene(self) -> Optional[QQuick3DNode]:
    """
    Calls Qt's 'QQuick3DNode *QQuick3DViewport::scene() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dviewport.html#scene

    Returns
    -------

    Optional[QQuick3DNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DNode *QQuick3DViewport::scene() const
    address = self.uglySide.call('ritual_ZNK16QQuick3DViewport5sceneEv')
    from . import QQuick3DNode
    return QQuick3DNode._cuteAt(address)

  def importScene(self) -> Optional[QQuick3DNode]:
    """
    Calls Qt's 'QQuick3DNode *QQuick3DViewport::importScene() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dviewport.html#importScene

    Returns
    -------

    Optional[QQuick3DNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DNode *QQuick3DViewport::importScene() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuick3DViewport11importSceneEv',
    )
    from . import QQuick3DNode
    return QQuick3DNode._cuteAt(address)

  def renderMode(self) -> RenderMode:
    """
    Calls Qt's 'RenderMode QQuick3DViewport::renderMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dviewport.html#renderMode

    Returns
    -------

    RenderMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'RenderMode(number)'
      gives.
    """
    #  RenderMode QQuick3DViewport::renderMode() const
    return QQuick3DViewport.RenderMode(self.uglySide.call(
        'ritual_ZNK16QQuick3DViewport10renderModeEv',
    ))

  def renderFormat(self) -> QQuickShaderEffectSource.Format:
    """
    Calls Qt's 'QQuickShaderEffectSource::Format
    QQuick3DViewport::renderFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dviewport.html#renderFormat

    Returns
    -------

    QQuickShaderEffectSource.Format
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickShaderEffectSource.Format(number)' gives.
    """
    #  QQuickShaderEffectSource::Format QQuick3DViewport::renderFormat()
    #      const
    return QQuickShaderEffectSource.Format(self.uglySide.call(
        'ritual_ZNK16QQuick3DViewport12renderFormatEv',
    ))

  def renderStats(self) -> Optional[QQuick3DRenderStats]:
    """
    Calls Qt's 'QQuick3DRenderStats *QQuick3DViewport::renderStats() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dviewport.html#renderStats

    Returns
    -------

    Optional[QQuick3DRenderStats]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DRenderStats *QQuick3DViewport::renderStats() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuick3DViewport11renderStatsEv',
    )
    from . import QQuick3DRenderStats
    return QQuick3DRenderStats._cuteAt(address)

  def createRenderer(self) -> Optional[QQuick3DSceneRenderer]:
    """
    Calls Qt's 'QQuick3DSceneRenderer *QQuick3DViewport::createRenderer()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#createRenderer

    Returns
    -------

    Optional[QQuick3DSceneRenderer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DSceneRenderer *QQuick3DViewport::createRenderer() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuick3DViewport14createRendererEv',
    )
    from . import QQuick3DSceneRenderer
    return QQuick3DSceneRenderer._cuteAt(address)

  def isTextureProvider(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DViewport::isTextureProvider() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#isTextureProvider
    """
    #  bool QQuick3DViewport::isTextureProvider() const
    ritual = 'ritual_ZNK16QQuick3DViewport17isTextureProviderEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QQuick3DViewport17isTextureProviderEv'
    return self.uglySide.call(ritual)

  def textureProvider(self) -> Optional[QSGTextureProvider]:
    """
    Calls Qt's 'QSGTextureProvider *QQuick3DViewport::textureProvider()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#textureProvider

    Returns
    -------

    Optional[QSGTextureProvider]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTextureProvider *QQuick3DViewport::textureProvider() const
    ritual = 'ritual_ZNK16QQuick3DViewport15textureProviderEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QQuick3DViewport15textureProviderEv'
    address = self.uglySide.call(ritual)
    from ..QtQuick import QSGTextureProvider
    return QSGTextureProvider._cuteAt(address)

  @overload(QVector3D)
  def mapFrom3DScene(self, scenePos: QVector3D) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DViewport::mapFrom3DScene(const QVector3D
    &scenePos) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#mapFrom3DScene

    Parameters
    ----------

    scenePos : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DViewport::mapFrom3DScene(const QVector3D &scenePos)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK16QQuick3DViewport14mapFrom3DSceneERK9QVector3D',
        self._valueOf(scenePos),
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(QVector3D)
  def mapTo3DScene(self, viewPos: QVector3D) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DViewport::mapTo3DScene(const QVector3D
    &viewPos) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dviewport.html#mapTo3DScene

    Parameters
    ----------

    viewPos : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DViewport::mapTo3DScene(const QVector3D &viewPos)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK16QQuick3DViewport12mapTo3DSceneERK9QVector3D',
        self._valueOf(viewPos),
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(float, float)
  def pick(self, x: float, y: float) -> QQuick3DPickResult:
    """
    Calls Qt's 'QQuick3DPickResult QQuick3DViewport::pick(float x, float y)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dviewport.html#pick

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    Returns
    -------

    QQuick3DPickResult
      A new cute QQuick3DPickResult around the copy Qt gave back. Python owns
      it.
    """
    #  QQuick3DPickResult QQuick3DViewport::pick(float x, float y) const
    address = self.uglySide.call(
        'ritual_ZNK16QQuick3DViewport4pickEff', x, y,
    )
    from . import QQuick3DPickResult
    return QQuick3DPickResult._cuteOwning(address)

  @overload(float, float, QQuick3DModel)
  @overload(float, float, NoneType)
  def pick(
      self,
      x: float,
      y: float,
      model: Optional[QQuick3DModel],
  ) -> QQuick3DPickResult:
    """
    Calls Qt's 'QQuick3DPickResult QQuick3DViewport::pick(float x, float y,
    QQuick3DModel *model) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dviewport.html#pick

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    model : Optional[QQuick3DModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QQuick3DPickResult
      A new cute QQuick3DPickResult around the copy Qt gave back. Python owns
      it.
    """
    #  QQuick3DPickResult QQuick3DViewport::pick(float x, float y,
    #      QQuick3DModel *model) const
    address = self.uglySide.call(
        'ritual_ZNK16QQuick3DViewport4pickEffP13QQuick3DModel',
        x, y, self._addressOf(model),
    )
    from . import QQuick3DPickResult
    return QQuick3DPickResult._cuteOwning(address)

  @overload(float, float, QJSValue)
  def pickSubset(
      self,
      x: float,
      y: float,
      models: QJSValue,
  ) -> QList[QQuick3DPickResult]:
    """
    Calls Qt's 'QList<QQuick3DPickResult> QQuick3DViewport::pickSubset(float
    x, float y, const QJSValue &models) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dviewport.html#pickSubset

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    models : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.

    Returns
    -------

    QList[QQuick3DPickResult]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQuick3DPickResult> QQuick3DViewport::pickSubset(float x, float
    #      y, const QJSValue &models) const
    address = self.uglySide.call(
        'ritual_ZNK16QQuick3DViewport10pickSubsetEffRK8QJSValue',
        x, y, self._valueOf(models),
    )
    from . import QQuick3DPickResult
    return QList[QQuick3DPickResult]._cuteOwning(address)

  @overload(float, float)
  def pickAll(self, x: float, y: float) -> QList[QQuick3DPickResult]:
    """
    Calls Qt's 'QList<QQuick3DPickResult> QQuick3DViewport::pickAll(float x,
    float y) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dviewport.html#pickAll

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    Returns
    -------

    QList[QQuick3DPickResult]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQuick3DPickResult> QQuick3DViewport::pickAll(float x, float y)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK16QQuick3DViewport7pickAllEff', x, y,
    )
    from . import QQuick3DPickResult
    return QList[QQuick3DPickResult]._cuteOwning(address)

  @overload(QVector3D, QVector3D)
  def rayPick(
      self,
      origin: QVector3D,
      direction: QVector3D,
  ) -> QQuick3DPickResult:
    """
    Calls Qt's 'QQuick3DPickResult QQuick3DViewport::rayPick(const QVector3D
    &origin, const QVector3D &direction) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dviewport.html#rayPick

    Parameters
    ----------

    origin : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    direction : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    Returns
    -------

    QQuick3DPickResult
      A new cute QQuick3DPickResult around the copy Qt gave back. Python owns
      it.
    """
    #  QQuick3DPickResult QQuick3DViewport::rayPick(const QVector3D &origin,
    #      const QVector3D &direction) const
    address = self.uglySide.call(
        'ritual_ZNK16QQuick3DViewport7rayPickERK9QVector3DS2_',
        self._valueOf(origin), self._valueOf(direction),
    )
    from . import QQuick3DPickResult
    return QQuick3DPickResult._cuteOwning(address)

  @overload(QVector3D, QVector3D, QQuick3DModel)
  @overload(QVector3D, QVector3D, NoneType)
  def rayPick(
      self,
      origin: QVector3D,
      direction: QVector3D,
      model: Optional[QQuick3DModel],
  ) -> QQuick3DPickResult:
    """
    Calls Qt's 'QQuick3DPickResult QQuick3DViewport::rayPick(const QVector3D
    &origin, const QVector3D &direction, QQuick3DModel *model) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dviewport.html#rayPick

    Parameters
    ----------

    origin : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    direction : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    model : Optional[QQuick3DModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QQuick3DPickResult
      A new cute QQuick3DPickResult around the copy Qt gave back. Python owns
      it.
    """
    #  QQuick3DPickResult QQuick3DViewport::rayPick(const QVector3D &origin,
    #      const QVector3D &direction, QQuick3DModel *model) const
    address = self.uglySide.call(
        'ritual_ZNK16QQuick3DViewport7rayPickERK9QVector3DS2_P13QQuick3DMod'
        'el',
        self._valueOf(origin), self._valueOf(direction),
        self._addressOf(model),
    )
    from . import QQuick3DPickResult
    return QQuick3DPickResult._cuteOwning(address)

  @overload(QVector3D, QVector3D)
  def rayPickAll(
      self,
      origin: QVector3D,
      direction: QVector3D,
  ) -> QList[QQuick3DPickResult]:
    """
    Calls Qt's 'QList<QQuick3DPickResult> QQuick3DViewport::rayPickAll(const
    QVector3D &origin, const QVector3D &direction) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dviewport.html#rayPickAll

    Parameters
    ----------

    origin : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    direction : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    Returns
    -------

    QList[QQuick3DPickResult]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQuick3DPickResult> QQuick3DViewport::rayPickAll(const QVector3D
    #      &origin, const QVector3D &direction) const
    address = self.uglySide.call(
        'ritual_ZNK16QQuick3DViewport10rayPickAllERK9QVector3DS2_',
        self._valueOf(origin), self._valueOf(direction),
    )
    from . import QQuick3DPickResult
    return QList[QQuick3DPickResult]._cuteOwning(address)

  @overload(QVector3D, float)
  @overload(QVector3D, float, QQuick3DModel)
  @overload(QVector3D, float, NoneType)
  def closestPointPick(
      self,
      origin: QVector3D,
      radius: float,
      model: Optional[QQuick3DModel] = None,
  ) -> QQuick3DPickResult:
    """
    Calls Qt's 'QQuick3DPickResult QQuick3DViewport::closestPointPick(const
    QVector3D &origin, float radius, QQuick3DModel *model) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#closestPointPick

    Parameters
    ----------

    origin : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    radius : float
      Passed on as it is.

    model : Optional[QQuick3DModel]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QQuick3DPickResult
      A new cute QQuick3DPickResult around the copy Qt gave back. Python owns
      it.
    """
    #  QQuick3DPickResult QQuick3DViewport::closestPointPick(const QVector3D
    #      &origin, float radius, QQuick3DModel *model) const
    address = self.uglySide.call(
        'ritual_ZNK16QQuick3DViewport16closestPointPickERK9QVector3DfP13QQu'
        'ick3DModel',
        self._valueOf(origin), radius, self._addressOf(model),
    )
    from . import QQuick3DPickResult
    return QQuick3DPickResult._cuteOwning(address)

  @overload(QPointF, QPointF)
  def pickInRect(
      self,
      start: QPointF,
      end: QPointF,
  ) -> QList[QQuick3DObject]:
    """
    Calls Qt's 'QList<QQuick3DObject *> QQuick3DViewport::pickInRect(const
    QPointF &start, const QPointF &end) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dviewport.html#pickInRect

    Parameters
    ----------

    start : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    end : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QList[QQuick3DObject]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQuick3DObject *> QQuick3DViewport::pickInRect(const QPointF
    #      &start, const QPointF &end) const
    address = self.uglySide.call(
        'ritual_ZNK16QQuick3DViewport10pickInRectERK7QPointFS2_',
        self._valueOf(start, 'QPointF'), self._valueOf(end, 'QPointF'),
    )
    from . import QQuick3DObject
    return QList[QQuick3DObject]._cuteOwning(address)

  def explicitTextureWidth(self) -> int:
    """
    Calls Qt's 'int QQuick3DViewport::explicitTextureWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#explicitTextureWidth
    """
    #  int QQuick3DViewport::explicitTextureWidth() const
    return self.uglySide.call(
        'ritual_ZNK16QQuick3DViewport20explicitTextureWidthEv',
    )

  def explicitTextureHeight(self) -> int:
    """
    Calls Qt's 'int QQuick3DViewport::explicitTextureHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#explicitTextureHeight
    """
    #  int QQuick3DViewport::explicitTextureHeight() const
    return self.uglySide.call(
        'ritual_ZNK16QQuick3DViewport21explicitTextureHeightEv',
    )

  def effectiveTextureSize(self) -> QSize:
    """
    Calls Qt's 'QSize QQuick3DViewport::effectiveTextureSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#effectiveTextureSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QQuick3DViewport::effectiveTextureSize() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuick3DViewport20effectiveTextureSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def extensionListDirty(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DViewport::extensionListDirty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#extensionListDirty
    """
    #  bool QQuick3DViewport::extensionListDirty() const
    return self.uglySide.call(
        'ritual_ZNK16QQuick3DViewport18extensionListDirtyEv',
    )

  def extensionList(self) -> QList[QQuick3DObject]:
    """
    Calls Qt's 'const QList<QQuick3DObject *>
    &QQuick3DViewport::extensionList() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#extensionList

    Returns
    -------

    QList[QQuick3DObject]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QList<QQuick3DObject *> &QQuick3DViewport::extensionList() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuick3DViewport13extensionListEv',
    )
    from . import QQuick3DObject
    return QList[QQuick3DObject]._cuteOwning(address)

  def isXrViewInstance(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DViewport::isXrViewInstance() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#isXrViewInstance
    """
    #  bool QQuick3DViewport::isXrViewInstance() const
    return self.uglySide.call(
        'ritual_ZNK16QQuick3DViewport16isXrViewInstanceEv',
    )

  def renderOverrides(self) -> RenderOverrides:
    """
    Calls Qt's 'RenderOverrides QQuick3DViewport::renderOverrides() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#renderOverrides

    Returns
    -------

    RenderOverrides
      The value standing for the combination Qt gave back.
    """
    #  RenderOverrides QQuick3DViewport::renderOverrides() const
    return QQuick3DViewport.RenderOverrides(self.uglySide.call(
        'ritual_ZNK16QQuick3DViewport15renderOverridesEv',
    ))

  def getRenderer(self) -> Optional[QQuick3DSceneRenderer]:
    """
    Calls Qt's 'QQuick3DSceneRenderer *QQuick3DViewport::getRenderer()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dviewport.html#getRenderer

    Returns
    -------

    Optional[QQuick3DSceneRenderer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DSceneRenderer *QQuick3DViewport::getRenderer() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuick3DViewport11getRendererEv',
    )
    from . import QQuick3DSceneRenderer
    return QQuick3DSceneRenderer._cuteAt(address)

  def checkIsVisible(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DViewport::checkIsVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#checkIsVisible
    """
    #  bool QQuick3DViewport::checkIsVisible() const
    return self.uglySide.call(
        'ritual_ZNK16QQuick3DViewport14checkIsVisibleEv',
    )

  @overload(QPointerEvent)
  @overload(NoneType)
  @overload(QPointerEvent, QVector3D)
  @overload(NoneType, QVector3D)
  @overload(QPointerEvent, QVector3D, QVector3D)
  @overload(NoneType, QVector3D, QVector3D)
  def internalPick(
      self,
      event: Optional[QPointerEvent],
      origin: Optional[QVector3D] = None,
      direction: Optional[QVector3D] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QQuick3DViewport::internalPick(QPointerEvent *event,
    const QVector3D &origin, const QVector3D &direction) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dviewport.html#internalPick

    Parameters
    ----------

    event : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    origin : Optional[QVector3D]
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own. May be left out, as in Qt: a new 'QVector3D()' is then passed on.

    direction : Optional[QVector3D]
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own. May be left out, as in Qt: a new 'QVector3D()' is then passed on.
    """
    #  bool QQuick3DViewport::internalPick(QPointerEvent *event, const
    #      QVector3D &origin, const QVector3D &direction) const
    if origin is None:
      from ..QtGui import QVector3D
      origin = QVector3D()
    if direction is None:
      from ..QtGui import QVector3D
      direction = QVector3D()
    return self.uglySide.call(
        'ritual_ZNK16QQuick3DViewport12internalPickEP13QPointerEventRK9QVec'
        'tor3DS4_',
        self._addressOf(event), self._valueOf(origin),
        self._valueOf(direction),
    )

  @overload(QQuick3DMaterial)
  @overload(NoneType)
  def getSubSceneRootItem(
      self,
      material: Optional[QQuick3DMaterial],
  ) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem
    *QQuick3DViewport::getSubSceneRootItem(QQuick3DMaterial *material)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#getSubSceneRootItem

    Parameters
    ----------

    material : Optional[QQuick3DMaterial]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuick3DViewport::getSubSceneRootItem(QQuick3DMaterial
    #      *material) const
    address = self.uglySide.call(
        'ritual_ZNK16QQuick3DViewport19getSubSceneRootItemEP16QQuick3DMater'
        'ial',
        self._addressOf(material),
    )
    return QQuickItem._cuteAt(address)

  @overload(QSSGRenderPickResult)
  def processPickResult(
      self,
      pickResult: QSSGRenderPickResult,
  ) -> QQuick3DPickResult:
    """
    Calls Qt's 'QQuick3DPickResult QQuick3DViewport::processPickResult(const
    QSSGRenderPickResult &pickResult) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#processPickResult

    Parameters
    ----------

    pickResult : QSSGRenderPickResult
      Passed on as a value: Qt reads the C++ QSSGRenderPickResult, which
      stays Python's own.

    Returns
    -------

    QQuick3DPickResult
      A new cute QQuick3DPickResult around the copy Qt gave back. Python owns
      it.
    """
    #  QQuick3DPickResult QQuick3DViewport::processPickResult(const
    #      QSSGRenderPickResult &pickResult) const
    address = self.uglySide.call(
        'ritual_ZNK16QQuick3DViewport17processPickResultERK20QSSGRenderPick'
        'Result',
        self._valueOf(pickResult),
    )
    from . import QQuick3DPickResult
    return QQuick3DPickResult._cuteOwning(address)

  @overload(QSSGRenderGraphObject)
  @overload(NoneType)
  def findFrontendNode(
      self,
      backendObject: Optional[QSSGRenderGraphObject],
  ) -> Optional[QQuick3DObject]:
    """
    Calls Qt's 'QQuick3DObject *QQuick3DViewport::findFrontendNode(const
    QSSGRenderGraphObject *backendObject) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#findFrontendNode

    Parameters
    ----------

    backendObject : Optional[QSSGRenderGraphObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuick3DObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DObject *QQuick3DViewport::findFrontendNode(const
    #      QSSGRenderGraphObject *backendObject) const
    address = self.uglySide.call(
        'ritual_ZNK16QQuick3DViewport16findFrontendNodeEPK21QSSGRenderGraph'
        'Object',
        self._addressOf(backendObject),
    )
    from . import QQuick3DObject
    return QQuick3DObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickItem, QPointF, int, bool)
  @overload(NoneType, QPointF, int, bool)
  def setTouchpoint(
      self,
      target: Optional[QQuickItem],
      position: QPointF,
      pointId: int,
      active: bool,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DViewport::setTouchpoint(QQuickItem *target,
    const QPointF &position, int pointId, bool active)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#setTouchpoint

    Parameters
    ----------

    target : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    pointId : int
      Passed on as it is.

    active : bool
      Passed on as it is.
    """
    #  void QQuick3DViewport::setTouchpoint(QQuickItem *target, const QPointF
    #      &position, int pointId, bool active)
    self.uglySide.call(
        'ritual_ZN16QQuick3DViewport13setTouchpointEP10QQuickItemRK7QPointF'
        'ib',
        self._addressOf(target), self._valueOf(position, 'QPointF'), pointId,
        active,
    )

  @overload(RenderOverrides)
  def setRenderOverrides(self, newRenderOverrides: RenderOverrides) -> None:
    """
    Calls Qt's 'void QQuick3DViewport::setRenderOverrides(RenderOverrides
    newRenderOverrides)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#setRenderOverrides

    Parameters
    ----------

    newRenderOverrides : RenderOverrides
      Passed on as its number.
    """
    #  void QQuick3DViewport::setRenderOverrides(RenderOverrides
    #      newRenderOverrides)
    self.uglySide.call(
        'ritual_ZN16QQuick3DViewport18setRenderOverridesE6QFlagsINS_14Rende'
        'rOverrideEE',
        newRenderOverrides.value,
    )

  @overload(QQuick3DCamera)
  @overload(NoneType)
  def setCamera(self, camera: Optional[QQuick3DCamera]) -> None:
    """
    Calls Qt's 'void QQuick3DViewport::setCamera(QQuick3DCamera *camera)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dviewport.html#setCamera

    Parameters
    ----------

    camera : Optional[QQuick3DCamera]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DViewport::setCamera(QQuick3DCamera *camera)
    self.uglySide.call(
        'ritual_ZN16QQuick3DViewport9setCameraEP14QQuick3DCamera',
        self._addressOf(camera),
    )

  @overload(QQuick3DSceneEnvironment)
  @overload(NoneType)
  def setEnvironment(
      self,
      environment: Optional[QQuick3DSceneEnvironment],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DViewport::setEnvironment(QQuick3DSceneEnvironment *environment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#setEnvironment

    Parameters
    ----------

    environment : Optional[QQuick3DSceneEnvironment]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DViewport::setEnvironment(QQuick3DSceneEnvironment
    #      *environment)
    self.uglySide.call(
        'ritual_ZN16QQuick3DViewport14setEnvironmentEP24QQuick3DSceneEnviro'
        'nment',
        self._addressOf(environment),
    )

  @overload(QQuick3DNode)
  @overload(NoneType)
  def setImportScene(self, inScene: Optional[QQuick3DNode]) -> None:
    """
    Calls Qt's 'void QQuick3DViewport::setImportScene(QQuick3DNode
    *inScene)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#setImportScene

    Parameters
    ----------

    inScene : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DViewport::setImportScene(QQuick3DNode *inScene)
    self.uglySide.call(
        'ritual_ZN16QQuick3DViewport14setImportSceneEP12QQuick3DNode',
        self._addressOf(inScene),
    )

  @overload(RenderMode)
  def setRenderMode(self, renderMode: RenderMode) -> None:
    """
    Calls Qt's 'void
    QQuick3DViewport::setRenderMode(QQuick3DViewport::RenderMode
    renderMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#setRenderMode

    Parameters
    ----------

    renderMode : RenderMode
      Passed on as its number.
    """
    #  void QQuick3DViewport::setRenderMode(QQuick3DViewport::RenderMode
    #      renderMode)
    self.uglySide.call(
        'ritual_ZN16QQuick3DViewport13setRenderModeENS_10RenderModeE',
        renderMode.value,
    )

  @overload(QQuickShaderEffectSource.Format)
  def setRenderFormat(self, format: QQuickShaderEffectSource.Format) -> None:
    """
    Calls Qt's 'void
    QQuick3DViewport::setRenderFormat(QQuickShaderEffectSource::Format
    format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#setRenderFormat

    Parameters
    ----------

    format : QQuickShaderEffectSource.Format
      Passed on as its number.
    """
    #  void
    #      QQuick3DViewport::setRenderFormat(QQuickShaderEffectSource::Format
    #      format)
    self.uglySide.call(
        'ritual_ZN16QQuick3DViewport15setRenderFormatEN24QQuickShaderEffect'
        'Source6FormatE',
        format.value,
    )

  @overload(int)
  def setExplicitTextureWidth(self, width: int) -> None:
    """
    Calls Qt's 'void QQuick3DViewport::setExplicitTextureWidth(int width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#setExplicitTextureWidth

    Parameters
    ----------

    width : int
      Passed on as it is.
    """
    #  void QQuick3DViewport::setExplicitTextureWidth(int width)
    self.uglySide.call(
        'ritual_ZN16QQuick3DViewport23setExplicitTextureWidthEi', width,
    )

  @overload(int)
  def setExplicitTextureHeight(self, height: int) -> None:
    """
    Calls Qt's 'void QQuick3DViewport::setExplicitTextureHeight(int height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#setExplicitTextureHeight

    Parameters
    ----------

    height : int
      Passed on as it is.
    """
    #  void QQuick3DViewport::setExplicitTextureHeight(int height)
    self.uglySide.call(
        'ritual_ZN16QQuick3DViewport24setExplicitTextureHeightEi', height,
    )

  @overload(bool)
  def setGlobalPickingEnabled(self, isEnabled: bool) -> None:
    """
    Calls Qt's 'void QQuick3DViewport::setGlobalPickingEnabled(bool
    isEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#setGlobalPickingEnabled

    Parameters
    ----------

    isEnabled : bool
      Passed on as it is.
    """
    #  void QQuick3DViewport::setGlobalPickingEnabled(bool isEnabled)
    self.uglySide.call(
        'ritual_ZN16QQuick3DViewport23setGlobalPickingEnabledEb', isEnabled,
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DViewport::QQuick3DViewport(QQuickItem *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#QQuick3DViewport

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DViewport::QQuick3DViewport(QQuickItem *parent)
    self._noteCreation(QQuick3DViewport, lambda: Rituals.call(
        'ritual_ZN16QQuick3DViewportC1EP10QQuickItem',
        self._addressOf(parent),
    ))

  @overload(PrivateInstanceType)
  @overload(PrivateInstanceType, QQuickItem)
  @overload(PrivateInstanceType, NoneType)
  def __init__(
      self,
      type: PrivateInstanceType,
      parent: Optional[QQuickItem] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DViewport::QQuick3DViewport(PrivateInstanceType type, QQuickItem
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#QQuick3DViewport

    Parameters
    ----------

    type : PrivateInstanceType
      Passed on as its number.

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DViewport::QQuick3DViewport(PrivateInstanceType type,
    #      QQuickItem *parent)
    self._noteCreation(QQuick3DViewport, lambda: Rituals.call(
        'ritual_ZN16QQuick3DViewportC1ENS_19PrivateInstanceTypeEP10QQuickIt'
        'em',
        type.value, self._addressOf(parent),
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

  def releaseResources(self) -> None:
    """
    Calls Qt's 'void QQuick3DViewport::releaseResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#releaseResources
    """
    #  void QQuick3DViewport::releaseResources()
    ritual = 'ritual_ZN16QQuick3DViewport16releaseResourcesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuick3DViewport16releaseResourcesEv'
    self.uglySide.call(ritual)

  @overload(QVector3D, QVector3D, QPointerEvent)
  @overload(QVector3D, QVector3D, NoneType)
  def processPointerEventFromRay(
      self,
      origin: QVector3D,
      direction: QVector3D,
      event: Optional[QPointerEvent],
  ) -> None:
    """
    Calls Qt's 'void QQuick3DViewport::processPointerEventFromRay(const
    QVector3D &origin, const QVector3D &direction, QPointerEvent *event)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#processPointerEventFromRay

    Parameters
    ----------

    origin : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    direction : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    event : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DViewport::processPointerEventFromRay(const QVector3D
    #      &origin, const QVector3D &direction, QPointerEvent *event) const
    self.uglySide.call(
        'ritual_ZNK16QQuick3DViewport26processPointerEventFromRayERK9QVecto'
        'r3DS2_P13QPointerEvent',
        self._valueOf(origin), self._valueOf(direction),
        self._addressOf(event),
    )

  @overload(QSinglePointEvent, QVector3D, QVector3D)
  @overload(NoneType, QVector3D, QVector3D)
  def singlePointPick(
      self,
      event: Optional[QSinglePointEvent],
      origin: QVector3D,
      direction: QVector3D,
  ) -> bool:
    """
    Calls Qt's 'bool QQuick3DViewport::singlePointPick(QSinglePointEvent
    *event, const QVector3D &origin, const QVector3D &direction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#singlePointPick

    Parameters
    ----------

    event : Optional[QSinglePointEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    origin : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    direction : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  bool QQuick3DViewport::singlePointPick(QSinglePointEvent *event, const
    #      QVector3D &origin, const QVector3D &direction)
    return self.uglySide.call(
        'ritual_ZN16QQuick3DViewport15singlePointPickEP17QSinglePointEventR'
        'K9QVector3DS4_',
        self._addressOf(event), self._valueOf(origin),
        self._valueOf(direction),
    )

  def maybeLightmapBaker(self) -> Optional[QQuick3DLightmapBaker]:
    """
    Calls Qt's 'QQuick3DLightmapBaker
    *QQuick3DViewport::maybeLightmapBaker()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#maybeLightmapBaker

    Returns
    -------

    Optional[QQuick3DLightmapBaker]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DLightmapBaker *QQuick3DViewport::maybeLightmapBaker()
    address = self.uglySide.call(
        'ritual_ZN16QQuick3DViewport18maybeLightmapBakerEv',
    )
    from . import QQuick3DLightmapBaker
    return QQuick3DLightmapBaker._cuteAt(address)

  def lightmapBaker(self) -> Optional[QQuick3DLightmapBaker]:
    """
    Calls Qt's 'QQuick3DLightmapBaker *QQuick3DViewport::lightmapBaker()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#lightmapBaker

    Returns
    -------

    Optional[QQuick3DLightmapBaker]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DLightmapBaker *QQuick3DViewport::lightmapBaker()
    address = self.uglySide.call(
        'ritual_ZN16QQuick3DViewport13lightmapBakerEv',
    )
    from . import QQuick3DLightmapBaker
    return QQuick3DLightmapBaker._cuteAt(address)

  def bakeLightmap(self) -> None:
    """
    Calls Qt's 'void QQuick3DViewport::bakeLightmap()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dviewport.html#bakeLightmap
    """
    #  void QQuick3DViewport::bakeLightmap()
    self.uglySide.call('ritual_ZN16QQuick3DViewport12bakeLightmapEv')

  def denoiseLightmap(self) -> None:
    """
    Calls Qt's 'void QQuick3DViewport::denoiseLightmap()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#denoiseLightmap
    """
    #  void QQuick3DViewport::denoiseLightmap()
    self.uglySide.call('ritual_ZN16QQuick3DViewport15denoiseLightmapEv')

  def clearExtensionListDirty(self) -> None:
    """
    Calls Qt's 'void QQuick3DViewport::clearExtensionListDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#clearExtensionListDirty
    """
    #  void QQuick3DViewport::clearExtensionListDirty()
    self.uglySide.call(
        'ritual_ZN16QQuick3DViewport23clearExtensionListDirtyEv',
    )

  def rebuildExtensionList(self) -> None:
    """
    Calls Qt's 'void QQuick3DViewport::rebuildExtensionList()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#rebuildExtensionList
    """
    #  void QQuick3DViewport::rebuildExtensionList()
    self.uglySide.call('ritual_ZN16QQuick3DViewport20rebuildExtensionListEv')

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuick3DViewport::geometryChange(const QRectF
    &newGeometry, const QRectF &oldGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuick3DViewport::geometryChange(const QRectF &newGeometry, const
    #      QRectF &oldGeometry)
    ritual = 'ritual_ZN16QQuick3DViewport14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuick3DViewport14geometryChangeERK6QRectFS2_'
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  @overload(QSGNode, QQuickItem.UpdatePaintNodeData)
  @overload(QSGNode, NoneType)
  @overload(NoneType, QQuickItem.UpdatePaintNodeData)
  @overload(NoneType, NoneType)
  def updatePaintNode(
      self,
      a0: Optional[QSGNode],
      a1: Optional[QQuickItem.UpdatePaintNodeData],
  ) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode *QQuick3DViewport::updatePaintNode(QSGNode *a0,
    UpdatePaintNodeData *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#updatePaintNode

    Parameters
    ----------

    a0 : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QQuickItem.UpdatePaintNodeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNode *QQuick3DViewport::updatePaintNode(QSGNode *a0,
    #      UpdatePaintNodeData *a1)
    ritual = (
        'ritual_ZN16QQuick3DViewport15updatePaintNodeEP7QSGNodePN10QQuickIt'
        'em19UpdatePaintNodeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuick3DViewport15updatePaintNodeEP7QSGNodePN10QQ'
          'uickItem19UpdatePaintNodeDataE')
    address = self.uglySide.call(
        ritual, self._addressOf(a0, 'QSGNode'), self._addressOf(a1),
    )
    from ..QtQuick import QSGNode
    return QSGNode._cuteAt(address)

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      value: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DViewport::itemChange(QQuickItem::ItemChange
    change, const QQuickItem::ItemChangeData &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dviewport.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    value : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuick3DViewport::itemChange(QQuickItem::ItemChange change, const
    #      QQuickItem::ItemChangeData &value)
    ritual = (
        'ritual_ZN16QQuick3DViewport10itemChangeEN10QQuickItem10ItemChangeE'
        'RKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuick3DViewport10itemChangeEN10QQuickItem10ItemC'
          'hangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(value))

  @overload(QEvent)
  @overload(NoneType)
  def event(self, a0: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QQuick3DViewport::event(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dviewport.html#event

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuick3DViewport::event(QEvent *a0)
    ritual = 'ritual_ZN16QQuick3DViewport5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuick3DViewport5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(a0))

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuick3DViewport::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#componentComplete
    """
    #  void QQuick3DViewport::componentComplete()
    ritual = 'ritual_ZN16QQuick3DViewport17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuick3DViewport17componentCompleteEv'
    self.uglySide.call(ritual)

  def cleanupDirectRenderer(self) -> None:
    """
    Calls Qt's 'void QQuick3DViewport::cleanupDirectRenderer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#cleanupDirectRenderer
    """
    #  void QQuick3DViewport::cleanupDirectRenderer()
    self.uglySide.call(
        'ritual_ZN16QQuick3DViewport21cleanupDirectRendererEv',
    )

  def invalidateSceneGraph(self) -> None:
    """
    Calls Qt's 'void QQuick3DViewport::invalidateSceneGraph()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#invalidateSceneGraph
    """
    #  void QQuick3DViewport::invalidateSceneGraph()
    self.uglySide.call('ritual_ZN16QQuick3DViewport20invalidateSceneGraphEv')

  def updateInputProcessing(self) -> None:
    """
    Calls Qt's 'void QQuick3DViewport::updateInputProcessing()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#updateInputProcessing
    """
    #  void QQuick3DViewport::updateInputProcessing()
    self.uglySide.call(
        'ritual_ZN16QQuick3DViewport21updateInputProcessingEv',
    )

  def onReleaseCachedResources(self) -> None:
    """
    Calls Qt's 'void QQuick3DViewport::onReleaseCachedResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#onReleaseCachedResources
    """
    #  void QQuick3DViewport::onReleaseCachedResources()
    self.uglySide.call(
        'ritual_ZN16QQuick3DViewport24onReleaseCachedResourcesEv',
    )

  def cameraChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DViewport::cameraChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#cameraChanged
    """
    #  void QQuick3DViewport::cameraChanged()
    self.uglySide.call('ritual_ZN16QQuick3DViewport13cameraChangedEv')

  def environmentChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DViewport::environmentChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#environmentChanged
    """
    #  void QQuick3DViewport::environmentChanged()
    self.uglySide.call('ritual_ZN16QQuick3DViewport18environmentChangedEv')

  def sceneChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DViewport::sceneChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dviewport.html#sceneChanged
    """
    #  void QQuick3DViewport::sceneChanged()
    self.uglySide.call('ritual_ZN16QQuick3DViewport12sceneChangedEv')

  def importSceneChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DViewport::importSceneChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#importSceneChanged
    """
    #  void QQuick3DViewport::importSceneChanged()
    self.uglySide.call('ritual_ZN16QQuick3DViewport18importSceneChangedEv')

  def renderModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DViewport::renderModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#renderModeChanged
    """
    #  void QQuick3DViewport::renderModeChanged()
    self.uglySide.call('ritual_ZN16QQuick3DViewport17renderModeChangedEv')

  def renderFormatChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DViewport::renderFormatChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#renderFormatChanged
    """
    #  void QQuick3DViewport::renderFormatChanged()
    self.uglySide.call('ritual_ZN16QQuick3DViewport19renderFormatChangedEv')

  def explicitTextureWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DViewport::explicitTextureWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#explicitTextureWidthChanged
    """
    #  void QQuick3DViewport::explicitTextureWidthChanged()
    self.uglySide.call(
        'ritual_ZN16QQuick3DViewport27explicitTextureWidthChangedEv',
    )

  def explicitTextureHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DViewport::explicitTextureHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#explicitTextureHeightChanged
    """
    #  void QQuick3DViewport::explicitTextureHeightChanged()
    self.uglySide.call(
        'ritual_ZN16QQuick3DViewport28explicitTextureHeightChangedEv',
    )

  def effectiveTextureSizeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DViewport::effectiveTextureSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#effectiveTextureSizeChanged
    """
    #  void QQuick3DViewport::effectiveTextureSizeChanged()
    self.uglySide.call(
        'ritual_ZN16QQuick3DViewport27effectiveTextureSizeChangedEv',
    )

  def renderOverridesChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DViewport::renderOverridesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#renderOverridesChanged
    """
    #  void QQuick3DViewport::renderOverridesChanged()
    self.uglySide.call(
        'ritual_ZN16QQuick3DViewport22renderOverridesChangedEv',
    )

  def updateDynamicTextures(self) -> None:
    """
    Calls Qt's 'void QQuick3DViewport::updateDynamicTextures()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#updateDynamicTextures
    """
    #  void QQuick3DViewport::updateDynamicTextures()
    self.uglySide.call(
        'ritual_ZN16QQuick3DViewport21updateDynamicTexturesEv',
    )

  @overload(QSGNode)
  @overload(NoneType)
  def setupOffscreenRenderer(
      self,
      node: Optional[QSGNode],
  ) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode *QQuick3DViewport::setupOffscreenRenderer(QSGNode
    *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#setupOffscreenRenderer

    Parameters
    ----------

    node : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNode *QQuick3DViewport::setupOffscreenRenderer(QSGNode *node)
    address = self.uglySide.call(
        'ritual_ZN16QQuick3DViewport22setupOffscreenRendererEP7QSGNode',
        self._addressOf(node, 'QSGNode'),
    )
    from ..QtQuick import QSGNode
    return QSGNode._cuteAt(address)

  @overload(QSGNode)
  @overload(NoneType)
  def setupInlineRenderer(
      self,
      node: Optional[QSGNode],
  ) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode *QQuick3DViewport::setupInlineRenderer(QSGNode
    *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#setupInlineRenderer

    Parameters
    ----------

    node : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNode *QQuick3DViewport::setupInlineRenderer(QSGNode *node)
    address = self.uglySide.call(
        'ritual_ZN16QQuick3DViewport19setupInlineRendererEP7QSGNode',
        self._addressOf(node, 'QSGNode'),
    )
    from ..QtQuick import QSGNode
    return QSGNode._cuteAt(address)

  @overload(RenderMode)
  def setupDirectRenderer(self, mode: RenderMode) -> None:
    """
    Calls Qt's 'void QQuick3DViewport::setupDirectRenderer(RenderMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#setupDirectRenderer

    Parameters
    ----------

    mode : RenderMode
      Passed on as its number.
    """
    #  void QQuick3DViewport::setupDirectRenderer(RenderMode mode)
    self.uglySide.call(
        'ritual_ZN16QQuick3DViewport19setupDirectRendererENS_10RenderModeE',
        mode.value,
    )

  @overload(QQuick3DObject)
  @overload(NoneType)
  @overload(QQuick3DObject, QQuick3DSceneManager)
  @overload(QQuick3DObject, NoneType)
  @overload(NoneType, QQuick3DSceneManager)
  @overload(NoneType, NoneType)
  def findChildSceneManager(
      self,
      inObject: Optional[QQuick3DObject],
      manager: Optional[QQuick3DSceneManager] = None,
  ) -> Optional[QQuick3DSceneManager]:
    """
    Calls Qt's 'QQuick3DSceneManager
    *QQuick3DViewport::findChildSceneManager(QQuick3DObject *inObject,
    QQuick3DSceneManager *manager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html#findChildSceneManager

    Parameters
    ----------

    inObject : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    manager : Optional[QQuick3DSceneManager]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QQuick3DSceneManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DSceneManager
    #      *QQuick3DViewport::findChildSceneManager(QQuick3DObject *inObject,
    #      QQuick3DSceneManager *manager)
    address = self.uglySide.call(
        'ritual_ZN16QQuick3DViewport21findChildSceneManagerEP14QQuick3DObje'
        'ctP20QQuick3DSceneManager',
        self._addressOf(inObject), self._addressOf(manager),
    )
    from . import QQuick3DSceneManager
    return QQuick3DSceneManager._cuteAt(address)

  def updateSceneManagerForImportScene(self) -> None:
    """
    Calls Qt's 'void QQuick3DViewport::updateSceneManagerForImportScene()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dviewport.html
    """
    #  void QQuick3DViewport::updateSceneManagerForImportScene()
    self.uglySide.call(
        'ritual_ZN16QQuick3DViewport32updateSceneManagerForImportSceneEv',
    )

  @staticmethod
  def data(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject> QQuick3DViewport::data()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuick3DViewport.data' has no cute function yet. Qt's "
        "'QQmlListProperty<QObject> QQuick3DViewport::data()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def extensions(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuick3DObject> QQuick3DViewport::extensions()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuick3DViewport.extensions' has no cute function yet. Qt's "
        "'QQmlListProperty<QQuick3DObject> QQuick3DViewport::extensions()': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def forwardEventToSubscenes(*__, **_) -> Never:
    """
    Qt's 'bool QQuick3DViewport::forwardEventToSubscenes(QPointerEvent
    *event, bool useRayPicking, QQuick3DSceneRenderer *renderer, const
    QFlatMap<QQuickItem *, SubsceneInfo> &visitedSubscenes) const': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuick3DViewport.forwardEventToSubscenes' has no cute function "
        "yet. Qt's 'bool "
        "QQuick3DViewport::forwardEventToSubscenes(QPointerEvent *event, "
        "bool useRayPicking, QQuick3DSceneRenderer *renderer, const "
        "QFlatMap<QQuickItem *, SubsceneInfo> &visitedSubscenes) const': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def getItemAndPosition(*__, **_) -> Never:
    """
    Qt's 'QPair<QQuickItem *, QPointF>
    QQuick3DViewport::getItemAndPosition(const QSSGRenderPickResult
    &pickResult) const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuick3DViewport.getItemAndPosition' has no cute function yet. "
        "Qt's 'QPair<QQuickItem *, QPointF> "
        "QQuick3DViewport::getItemAndPosition(const QSSGRenderPickResult "
        "&pickResult) const': gives a type Python has no way to take yet.")

  @staticmethod
  def getNearestPickResult(*__, **_) -> Never:
    """
    Qt's 'QQuick3DPickResult QQuick3DViewport::getNearestPickResult(const
    QVarLengthArray<QSSGRenderPickResult, 20> &pickResults) const': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuick3DViewport.getNearestPickResult' has no cute function yet. "
        "Qt's 'QQuick3DPickResult "
        "QQuick3DViewport::getNearestPickResult(const "
        "QVarLengthArray<QSSGRenderPickResult, 20> &pickResults) const': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def getPickResults(*__, **_) -> Never:
    """
    - Qt's 'QVarLengthArray<QSSGRenderPickResult, 20>
      QQuick3DViewport::getPickResults(QQuick3DSceneRenderer *renderer, const
      QVector3D &origin, const QVector3D &direction) const': gives a type
      Python has no way to take yet.
    - Qt's 'QVarLengthArray<QSSGRenderPickResult, 20>
      QQuick3DViewport::getPickResults(QQuick3DSceneRenderer *renderer, const
      QEventPoint &eventPoint) const': gives a type Python has no way to take
      yet.
    """
    raise NotImplementedError(
        "'QQuick3DViewport.getPickResults' has no cute function yet. Qt's "
        "'QVarLengthArray<QSSGRenderPickResult, 20> "
        "QQuick3DViewport::getPickResults(QQuick3DSceneRenderer *renderer, "
        "const QVector3D &origin, const QVector3D &direction) const': gives "
        "a type Python has no way to take yet. Qt's "
        "'QVarLengthArray<QSSGRenderPickResult, 20> "
        "QQuick3DViewport::getPickResults(QQuick3DSceneRenderer *renderer, "
        "const QEventPoint &eventPoint) const': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def processPickedObject(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DViewport::processPickedObject(const
    QSSGRenderPickResult &pickResult, int pointIndex, QPointerEvent *event,
    QFlatMap<QQuickItem *, SubsceneInfo> &vistedSubscenes) const': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuick3DViewport.processPickedObject' has no cute function yet. "
        "Qt's 'void QQuick3DViewport::processPickedObject(const "
        "QSSGRenderPickResult &pickResult, int pointIndex, QPointerEvent "
        "*event, QFlatMap<QQuickItem *, SubsceneInfo> &vistedSubscenes) "
        "const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setMultiViewCameras(*__, **_) -> Never:
    """
    - Qt's 'void QQuick3DViewport::setMultiViewCameras(QQuick3DCamera
      **firstCamera, int count)': takes a type Python has no way to hand over
      yet.
    - Qt's 'QQuick3DViewport::setMultiViewCameras': a template: a pattern and
      no single function.
    """
    raise NotImplementedError(
        "'QQuick3DViewport.setMultiViewCameras' has no cute function yet. "
        "Qt's 'void QQuick3DViewport::setMultiViewCameras(QQuick3DCamera "
        "**firstCamera, int count)': takes a type Python has no way to hand "
        "over yet. Qt's 'QQuick3DViewport::setMultiViewCameras': a "
        "template: a pattern and no single function.")

  @staticmethod
  def updateCameraForLayer(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DViewport::updateCameraForLayer(const QQuick3DViewport
    &view3D, QSSGRenderLayer &layerNode)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQuick3DViewport.updateCameraForLayer' has no cute function yet. "
        "Qt's 'void QQuick3DViewport::updateCameraForLayer(const "
        "QQuick3DViewport &view3D, QSSGRenderLayer &layerNode)': takes a "
        "type Python has no way to hand over yet.")
