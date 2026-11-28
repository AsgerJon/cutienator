"""
QSSGBufferManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderbuffermanager_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGBufferManager to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtGui import QRhiTexture
from ..QtQuick3DUtils import QSSGMesh

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMutex
  from ..QtGui import QRhiResourceUpdateBatch
  from ..QtQuick3DUtils import QSSGBounds3, QSSGRenderTextureFormat
  from . import QSSGLoadedTexture, QSSGMeshProcessingOptions
  from . import QSSGRenderContextInterface, QSSGRenderGeometry
  from . import QSSGRenderImage, QSSGRenderImageTexture, QSSGRenderLayer
  from . import QSSGRenderMesh, QSSGRenderModel, QSSGRenderPath
  from . import QSSGRenderResourceLoader, QSSGRenderTextureData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSSGLoadedTexture = WAIT['QSSGLoadedTexture']
  QSSGMeshProcessingOptions = WAIT['QSSGMeshProcessingOptions']
  QSSGRenderContextInterface = WAIT['QSSGRenderContextInterface']
  QSSGRenderGeometry = WAIT['QSSGRenderGeometry']
  QSSGRenderImage = WAIT['QSSGRenderImage']
  QSSGRenderImageTexture = WAIT['QSSGRenderImageTexture']
  QSSGRenderLayer = WAIT['QSSGRenderLayer']
  QSSGRenderMesh = WAIT['QSSGRenderMesh']
  QSSGRenderModel = WAIT['QSSGRenderModel']
  QSSGRenderPath = WAIT['QSSGRenderPath']
  QSSGRenderResourceLoader = WAIT['QSSGRenderResourceLoader']
  QSSGRenderTextureData = WAIT['QSSGRenderTextureData']
  QSSGRenderTextureFormat = WAIT['QSSGRenderTextureFormat']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSSGBufferManager(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGBufferManager: a plain Python object standing in
  front of one C++ QSSGBufferManager.

  What exists
  -----------

  Every function of Qt's QSSGBufferManager that has a ritual and that Python
  can call so far, 32 names in all: 'setRenderContextInterface',
  'releaseCachedResources', 'releaseResourcesForLayer', 'loadRenderImage',
  'loadTextureData', 'loadSkinmap', 'getModelBounds',
  'cleanupUnreferencedBuffers', 'resetUsageCounters', 'releaseGeometry',
  'releaseTextureData', 'commitBufferResourceUpdates',
  'processResourceLoader', 'loadMeshData', 'toRhiFormat',
  'unregisterMeshData', 'runtimeMeshSourceName', 'primitivePath',
  'meshUpdateMutex', 'increaseMemoryStat', 'decreaseMemoryStat',
  'setLightmapSource', 'setCurrentlyLightmapBaking', 'clear',
  'meshBufferUpdateBatch', 'loadPrimitive', 'loadRenderMesh',
  'createRenderMesh', 'createEnvironmentMap', 'releaseMesh', 'releaseImage',
  'validateLightmap'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGBufferManager::~QSSGBufferManager()': the destructor: Python
    never removes a C++ QSSGBufferManager.
  - Qt's 'QSSGRenderImageTexture QSSGBufferManager::loadLightmap(const
    QSSGRenderModel &model)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QSSGRenderMesh *QSSGBufferManager::getMeshForPicking(const
    QSSGRenderModel &model, const QString &lightmap) const': takes a type
    Python has no way to hand over yet.
  - Qt's 'QSSGRenderMesh *QSSGBufferManager::loadMesh(const QSSGRenderModel
    &model)': takes a type Python has no way to hand over yet.
  - Qt's 'QSSGMesh::Mesh QSSGBufferManager::loadLightmapMesh(const
    QSSGRenderModel &model)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QSSGBufferManager::releaseExtensionResult(const
    QSSGRenderExtension &rext)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QSSGBufferManager::releaseUserRenderPass(const
    QSSGRenderUserPass &upass)': takes a type Python has no way to hand over
    yet.
  - Qt's 'std::unique_ptr<QSSGMeshBVH> QSSGBufferManager::loadMeshBVH(const
    QSSGRenderPath &inSourcePath)': gives a type Python has no way to take
    yet.
  - Qt's 'std::unique_ptr<QSSGMeshBVH>
    QSSGBufferManager::loadMeshBVH(QSSGRenderGeometry *geometry)': gives a
    type Python has no way to take yet.
  - Qt's 'std::unique_ptr<QSSGMeshBVH> QSSGBufferManager::loadMeshBVH(const
    QSSGMesh::Mesh &mesh)': gives a type Python has no way to take yet.
  - Qt's 'void QSSGBufferManager::registerExtensionResult(const
    QSSGRenderExtension &extensions, QRhiTexture *texture)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void QSSGBufferManager::registerMeshData(const QString &assetId,
    const QVector<QSSGMesh::Mesh> &meshData)': takes a type Python has no way
    to hand over yet.
  - Qt's 'const QHash<ImageCacheKey, ImageData>
    &QSSGBufferManager::getImageMap() const': gives a type Python has no way
    to take yet.
  - Qt's 'const QHash<CustomImageCacheKey, ImageData>
    &QSSGBufferManager::getCustomTextureMap() const': gives a type Python has
    no way to take yet.
  - Qt's 'const QHash<QSGTexture *, ImageData>
    &QSSGBufferManager::getSGImageMap() const': gives a type Python has no
    way to take yet.
  - Qt's 'const QHash<std::pair<QSSGRenderPath, QString>, MeshData>
    &QSSGBufferManager::getMeshMap() const': gives a type Python has no way
    to take yet.
  - Qt's 'const QHash<std::pair<QSSGRenderGeometry *, QString>, MeshData>
    &QSSGBufferManager::getCustomMeshMap() const': gives a type Python has no
    way to take yet.
  - Qt's 'void QSSGBufferManager::registerUserRenderPassManager(const
    QSSGUserRenderPassManagerPtr &userPassManager)': takes a type Python has
    no way to hand over yet.
  - Qt's 'bool QSSGBufferManager::setRhiTexture(QSSGRenderImageTexture
    &texture, const QSSGLoadedTexture *inTexture, MipMode inMipMode,
    CreateRhiTextureFlags inFlags, const QString &debugObjectName, bool
    *wasTextureCreated)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 59 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QSSGBufferManager is created at the first use, not by
    'QSSGBufferManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGBufferManager.
  - Each name of Qt's QSSGBufferManager that has no cute function yet,
    'getCustomMeshMap', 'getCustomTextureMap', 'getImageMap',
    'getMeshForPicking', 'getMeshMap', 'getSGImageMap', 'loadLightmap',
    'loadLightmapMesh', 'loadMesh', 'loadMeshBVH', 'registerExtensionResult',
    'registerMeshData', 'registerUserRenderPassManager',
    'releaseExtensionResult', 'releaseUserRenderPass', 'setRhiTexture', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QSSGBufferManager, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class LoadRenderImageFlag(CuteFlags):
    """
    The flags enum 'QSSGBufferManager::LoadRenderImageFlag' of Qt, with the 1
    names Qt gives in it. Qt names the type of its combinations
    'QSSGBufferManager::LoadRenderImageFlags'.
    """

    LoadWithFlippedY = 0x1

  LoadRenderImageFlags = LoadRenderImageFlag

  class MipMode(CuteNum):
    """
    The enum 'QSSGBufferManager::MipMode' of Qt, with the 4 names Qt gives in
    it.
    """

    MipModeFollowRenderImage = Kee[int](0)
    MipModeEnable = Kee[int](1)
    MipModeDisable = Kee[int](2)
    MipModeBsdf = Kee[int](3)

  #  The classes Qt writes inside QSSGBufferManager, each a class in here as
  #  in C++.

  class CustomImageCacheKey(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGBufferManager::CustomImageCacheKey: a plain
    Python object standing in front of one C++
    QSSGBufferManager::CustomImageCacheKey.

    C++ hands a QSSGBufferManager::CustomImageCacheKey around as a copy, so
    every C++ QSSGBufferManager::CustomImageCacheKey behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QSSGBufferManager::CustomImageCacheKey yet. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGBufferManager::CustomImageCacheKey::~CustomImageCacheKey()':
      the destructor: Python removes its C++
      QSSGBufferManager::CustomImageCacheKey by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QSSGBufferManager::CustomImageCacheKey is created at the first
      use, not by 'QSSGBufferManager::CustomImageCacheKey(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGBufferManager::CustomImageCacheKey back gives a
      copy the ritual made for Python, in a new cute
      QSSGBufferManager::CustomImageCacheKey.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGBufferManager::CustomImageCacheKey'

    #  Qt's '~QSSGBufferManager::CustomImageCacheKey()'. Naming it makes this
    #  a value class: Python owns every C++
    #  QSSGBufferManager::CustomImageCacheKey behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN17QSSGBufferManager19CustomImageCacheKeyD1Ev')

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

  class ImageCacheKey(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGBufferManager::ImageCacheKey: a plain Python
    object standing in front of one C++ QSSGBufferManager::ImageCacheKey.

    C++ hands a QSSGBufferManager::ImageCacheKey around as a copy, so every
    C++ QSSGBufferManager::ImageCacheKey behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QSSGBufferManager::ImageCacheKey yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGBufferManager::ImageCacheKey::~ImageCacheKey()': the
      destructor: Python removes its C++ QSSGBufferManager::ImageCacheKey by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QSSGBufferManager::ImageCacheKey is created at the first use,
      not by 'QSSGBufferManager::ImageCacheKey(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGBufferManager::ImageCacheKey back gives a copy
      the ritual made for Python, in a new cute
      QSSGBufferManager::ImageCacheKey.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGBufferManager::ImageCacheKey'

    #  Qt's '~QSSGBufferManager::ImageCacheKey()'. Naming it makes this a
    #  value class: Python owns every C++ QSSGBufferManager::ImageCacheKey
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN17QSSGBufferManager13ImageCacheKeyD1Ev'

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

  class ImageData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGBufferManager::ImageData: a plain Python object
    standing in front of one C++ QSSGBufferManager::ImageData.

    C++ hands a QSSGBufferManager::ImageData around as a copy, so every C++
    QSSGBufferManager::ImageData behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QSSGBufferManager::ImageData yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGBufferManager::ImageData::~ImageData()': the destructor:
      Python removes its C++ QSSGBufferManager::ImageData by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QSSGBufferManager::ImageData is created at the first use, not
      by 'QSSGBufferManager::ImageData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGBufferManager::ImageData back gives a copy the
      ritual made for Python, in a new cute QSSGBufferManager::ImageData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGBufferManager::ImageData'

    #  Qt's '~QSSGBufferManager::ImageData()'. Naming it makes this a value
    #  class: Python owns every C++ QSSGBufferManager::ImageData behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN17QSSGBufferManager9ImageDataD1Ev'

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

  class MemoryStats(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGBufferManager::MemoryStats: a plain Python
    object standing in front of one C++ QSSGBufferManager::MemoryStats.

    C++ hands a QSSGBufferManager::MemoryStats around as a copy, so every C++
    QSSGBufferManager::MemoryStats behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QSSGBufferManager::MemoryStats yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGBufferManager::MemoryStats::~MemoryStats()': the destructor:
      Python removes its C++ QSSGBufferManager::MemoryStats by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QSSGBufferManager::MemoryStats is created at the first use, not
      by 'QSSGBufferManager::MemoryStats(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGBufferManager::MemoryStats back gives a copy
      the ritual made for Python, in a new cute
      QSSGBufferManager::MemoryStats.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGBufferManager::MemoryStats'

    #  Qt's '~QSSGBufferManager::MemoryStats()'. Naming it makes this a value
    #  class: Python owns every C++ QSSGBufferManager::MemoryStats behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN17QSSGBufferManager11MemoryStatsD1Ev'

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

  class MeshData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGBufferManager::MeshData: a plain Python object
    standing in front of one C++ QSSGBufferManager::MeshData.

    C++ hands a QSSGBufferManager::MeshData around as a copy, so every C++
    QSSGBufferManager::MeshData behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QSSGBufferManager::MeshData yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGBufferManager::MeshData::~MeshData()': the destructor: Python
      removes its C++ QSSGBufferManager::MeshData by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QSSGBufferManager::MeshData is created at the first use, not by
      'QSSGBufferManager::MeshData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGBufferManager::MeshData back gives a copy the
      ritual made for Python, in a new cute QSSGBufferManager::MeshData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGBufferManager::MeshData'

    #  Qt's '~QSSGBufferManager::MeshData()'. Naming it makes this a value
    #  class: Python owns every C++ QSSGBufferManager::MeshData behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN17QSSGBufferManager8MeshDataD1Ev'

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
  @overload(QSSGRenderPath)
  def loadMeshData(inSourcePath: QSSGRenderPath) -> QSSGMesh.Mesh:
    """
    Calls Qt's 'QSSGMesh::Mesh QSSGBufferManager::loadMeshData(const
    QSSGRenderPath &inSourcePath)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgbuffermanager.html#loadMeshData

    Parameters
    ----------

    inSourcePath : QSSGRenderPath
      Passed on as a value: Qt reads the C++ QSSGRenderPath, which stays
      Python's own.

    Returns
    -------

    QSSGMesh.Mesh
      A new cute QSSGMesh::Mesh around the copy Qt gave back. Python owns it.
    """
    #  QSSGMesh::Mesh QSSGBufferManager::loadMeshData(const QSSGRenderPath
    #      &inSourcePath)
    address = Rituals.call(
        'ritual_ZN17QSSGBufferManager12loadMeshDataERK14QSSGRenderPath',
        CuteMixin._valueOf(inSourcePath),
    )
    return QSSGMesh.Mesh._cuteOwning(address)

  @overload(QSSGRenderGeometry)
  @overload(NoneType)
  def loadMeshData(
      self,
      geometry: Optional[QSSGRenderGeometry],
  ) -> QSSGMesh.Mesh:
    """
    Calls Qt's 'QSSGMesh::Mesh QSSGBufferManager::loadMeshData(const
    QSSGRenderGeometry *geometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgbuffermanager.html#loadMeshData

    Parameters
    ----------

    geometry : Optional[QSSGRenderGeometry]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QSSGMesh.Mesh
      A new cute QSSGMesh::Mesh around the copy Qt gave back. Python owns it.
    """
    #  QSSGMesh::Mesh QSSGBufferManager::loadMeshData(const
    #      QSSGRenderGeometry *geometry)
    address = self.uglySide.call(
        'ritual_ZN17QSSGBufferManager12loadMeshDataEPK18QSSGRenderGeometry',
        self._addressOf(geometry),
    )
    return QSSGMesh.Mesh._cuteOwning(address)

  @staticmethod
  @overload(QSSGRenderTextureFormat)
  def toRhiFormat(format: QSSGRenderTextureFormat) -> QRhiTexture.Format:
    """
    Calls Qt's 'QRhiTexture::Format QSSGBufferManager::toRhiFormat(const
    QSSGRenderTextureFormat format)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgbuffermanager.html#toRhiFormat

    Parameters
    ----------

    format : QSSGRenderTextureFormat
      Passed on as a value: Qt reads the C++ QSSGRenderTextureFormat, which
      stays Python's own.

    Returns
    -------

    QRhiTexture.Format
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QRhiTexture.Format(number)' gives.
    """
    #  QRhiTexture::Format QSSGBufferManager::toRhiFormat(const
    #      QSSGRenderTextureFormat format)
    return QRhiTexture.Format(Rituals.call(
        'ritual_ZN17QSSGBufferManager11toRhiFormatE23QSSGRenderTextureForma'
        't',
        CuteMixin._valueOf(format),
    ))

  @staticmethod
  @overload(str)
  def unregisterMeshData(assetId: str) -> None:
    """
    Calls Qt's 'void QSSGBufferManager::unregisterMeshData(const QString
    &assetId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgbuffermanager.html#unregisterMeshData

    Parameters
    ----------

    assetId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSSGBufferManager::unregisterMeshData(const QString &assetId)
    Rituals.call(
        'ritual_ZN17QSSGBufferManager18unregisterMeshDataERK7QString',
        assetId,
    )

  @staticmethod
  @overload(str, int)
  def runtimeMeshSourceName(assetId: str, meshId: int) -> str:
    """
    Calls Qt's 'QString QSSGBufferManager::runtimeMeshSourceName(const
    QString &assetId, qsizetype meshId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgbuffermanager.html#runtimeMeshSourceName

    Parameters
    ----------

    assetId : str
      Passed on as it is: a QString is made of it for the call.

    meshId : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSSGBufferManager::runtimeMeshSourceName(const QString
    #      &assetId, qsizetype meshId)
    return Rituals.call(
        'ritual_ZN17QSSGBufferManager21runtimeMeshSourceNameERK7QStringx',
        assetId, meshId,
    )

  @staticmethod
  @overload(str)
  def primitivePath(primitive: str) -> str:
    """
    Calls Qt's 'QString QSSGBufferManager::primitivePath(const QString
    &primitive)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgbuffermanager.html#primitivePath

    Parameters
    ----------

    primitive : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSSGBufferManager::primitivePath(const QString &primitive)
    return Rituals.call(
        'ritual_ZN17QSSGBufferManager13primitivePathERK7QString', primitive,
    )

  @staticmethod
  @overload(str)
  def loadPrimitive(inRelativePath: str) -> QSSGMesh.Mesh:
    """
    Calls Qt's 'QSSGMesh::Mesh QSSGBufferManager::loadPrimitive(const QString
    &inRelativePath)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgbuffermanager.html#loadPrimitive

    Parameters
    ----------

    inRelativePath : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QSSGMesh.Mesh
      A new cute QSSGMesh::Mesh around the copy Qt gave back. Python owns it.
    """
    #  QSSGMesh::Mesh QSSGBufferManager::loadPrimitive(const QString
    #      &inRelativePath)
    address = Rituals.call(
        'ritual_ZN17QSSGBufferManager13loadPrimitiveERK7QString',
        inRelativePath,
    )
    return QSSGMesh.Mesh._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGBufferManager'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSSGRenderContextInterface)
  @overload(NoneType)
  def setRenderContextInterface(
      self,
      ctx: Optional[QSSGRenderContextInterface],
  ) -> None:
    """
    Calls Qt's 'void
    QSSGBufferManager::setRenderContextInterface(QSSGRenderContextInterface
    *ctx)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgbuffermanager.html#setRenderContextInterface

    Parameters
    ----------

    ctx : Optional[QSSGRenderContextInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGBufferManager::setRenderContextInterface(
    #      QSSGRenderContextInterface *ctx)
    self.uglySide.call(
        'ritual_ZN17QSSGBufferManager25setRenderContextInterfaceEP26QSSGRen'
        'derContextInterface',
        self._addressOf(ctx),
    )

  @overload(str)
  def setLightmapSource(self, source: str) -> None:
    """
    Calls Qt's 'void QSSGBufferManager::setLightmapSource(const QString
    &source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgbuffermanager.html#setLightmapSource

    Parameters
    ----------

    source : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSSGBufferManager::setLightmapSource(const QString &source)
    self.uglySide.call(
        'ritual_ZN17QSSGBufferManager17setLightmapSourceERK7QString', source,
    )

  @overload(bool)
  def setCurrentlyLightmapBaking(self, value: bool) -> None:
    """
    Calls Qt's 'void QSSGBufferManager::setCurrentlyLightmapBaking(bool
    value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgbuffermanager.html#setCurrentlyLightmapBaking

    Parameters
    ----------

    value : bool
      Passed on as it is.
    """
    #  void QSSGBufferManager::setCurrentlyLightmapBaking(bool value)
    self.uglySide.call(
        'ritual_ZN17QSSGBufferManager26setCurrentlyLightmapBakingEb', value,
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
    Notes what was given, for Qt's 'QSSGBufferManager::QSSGBufferManager()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgbuffermanager.html#QSSGBufferManager
    """
    #  QSSGBufferManager::QSSGBufferManager()
    self._noteCreation(QSSGBufferManager, lambda: Rituals.call(
        'ritual_ZN17QSSGBufferManagerC1Ev',
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

  def releaseCachedResources(self) -> None:
    """
    Calls Qt's 'void QSSGBufferManager::releaseCachedResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgbuffermanager.html#releaseCachedResources
    """
    #  void QSSGBufferManager::releaseCachedResources()
    self.uglySide.call(
        'ritual_ZN17QSSGBufferManager22releaseCachedResourcesEv',
    )

  @overload(QSSGRenderLayer)
  @overload(NoneType)
  def releaseResourcesForLayer(
      self,
      layer: Optional[QSSGRenderLayer],
  ) -> None:
    """
    Calls Qt's 'void
    QSSGBufferManager::releaseResourcesForLayer(QSSGRenderLayer *layer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgbuffermanager.html#releaseResourcesForLayer

    Parameters
    ----------

    layer : Optional[QSSGRenderLayer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGBufferManager::releaseResourcesForLayer(QSSGRenderLayer
    #      *layer)
    self.uglySide.call(
        'ritual_ZN17QSSGBufferManager24releaseResourcesForLayerEP15QSSGRend'
        'erLayer',
        self._addressOf(layer),
    )

  @overload(QSSGRenderImage)
  @overload(NoneType)
  @overload(QSSGRenderImage, MipMode)
  @overload(NoneType, MipMode)
  @overload(QSSGRenderImage, MipMode, LoadRenderImageFlags)
  @overload(NoneType, MipMode, LoadRenderImageFlags)
  def loadRenderImage(
      self,
      image: Optional[QSSGRenderImage],
      inMipMode: MipMode = MipMode.MipModeFollowRenderImage,
      flags: LoadRenderImageFlags = LoadRenderImageFlags.LoadWithFlippedY,
  ) -> QSSGRenderImageTexture:
    """
    Calls Qt's 'QSSGRenderImageTexture
    QSSGBufferManager::loadRenderImage(const QSSGRenderImage *image, MipMode
    inMipMode, LoadRenderImageFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgbuffermanager.html#loadRenderImage

    Parameters
    ----------

    image : Optional[QSSGRenderImage]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    inMipMode : MipMode
      Passed on as its number. May be left out, as in Qt: it is then
      MipMode.MipModeFollowRenderImage.

    flags : LoadRenderImageFlags
      Passed on as its number. May be left out, as in Qt: it is then
      LoadRenderImageFlags.LoadWithFlippedY.

    Returns
    -------

    QSSGRenderImageTexture
      A new cute QSSGRenderImageTexture around the copy Qt gave back. Python
      owns it.
    """
    #  QSSGRenderImageTexture QSSGBufferManager::loadRenderImage(const
    #      QSSGRenderImage *image, MipMode inMipMode, LoadRenderImageFlags
    #      flags)
    address = self.uglySide.call(
        'ritual_ZN17QSSGBufferManager15loadRenderImageEPK15QSSGRenderImageN'
        'S_7MipModeE6QFlagsINS_19LoadRenderImageFlagEE',
        self._addressOf(image), inMipMode.value, flags.value,
    )
    from . import QSSGRenderImageTexture
    return QSSGRenderImageTexture._cuteOwning(address)

  @overload(QSSGRenderTextureData, MipMode)
  @overload(NoneType, MipMode)
  def loadTextureData(
      self,
      data: Optional[QSSGRenderTextureData],
      inMipMode: MipMode,
  ) -> QSSGRenderImageTexture:
    """
    Calls Qt's 'QSSGRenderImageTexture
    QSSGBufferManager::loadTextureData(QSSGRenderTextureData *data, MipMode
    inMipMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgbuffermanager.html#loadTextureData

    Parameters
    ----------

    data : Optional[QSSGRenderTextureData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    inMipMode : MipMode
      Passed on as its number.

    Returns
    -------

    QSSGRenderImageTexture
      A new cute QSSGRenderImageTexture around the copy Qt gave back. Python
      owns it.
    """
    #  QSSGRenderImageTexture
    #      QSSGBufferManager::loadTextureData(QSSGRenderTextureData *data,
    #      MipMode inMipMode)
    address = self.uglySide.call(
        'ritual_ZN17QSSGBufferManager15loadTextureDataEP21QSSGRenderTexture'
        'DataNS_7MipModeE',
        self._addressOf(data), inMipMode.value,
    )
    from . import QSSGRenderImageTexture
    return QSSGRenderImageTexture._cuteOwning(address)

  @overload(QSSGRenderTextureData)
  @overload(NoneType)
  def loadSkinmap(
      self,
      skin: Optional[QSSGRenderTextureData],
  ) -> QSSGRenderImageTexture:
    """
    Calls Qt's 'QSSGRenderImageTexture
    QSSGBufferManager::loadSkinmap(QSSGRenderTextureData *skin)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgbuffermanager.html#loadSkinmap

    Parameters
    ----------

    skin : Optional[QSSGRenderTextureData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QSSGRenderImageTexture
      A new cute QSSGRenderImageTexture around the copy Qt gave back. Python
      owns it.
    """
    #  QSSGRenderImageTexture
    #      QSSGBufferManager::loadSkinmap(QSSGRenderTextureData *skin)
    address = self.uglySide.call(
        'ritual_ZN17QSSGBufferManager11loadSkinmapEP21QSSGRenderTextureData',
        self._addressOf(skin),
    )
    from . import QSSGRenderImageTexture
    return QSSGRenderImageTexture._cuteOwning(address)

  @overload(QSSGRenderModel)
  @overload(NoneType)
  def getModelBounds(self, model: Optional[QSSGRenderModel]) -> QSSGBounds3:
    """
    Calls Qt's 'QSSGBounds3 QSSGBufferManager::getModelBounds(const
    QSSGRenderModel *model)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgbuffermanager.html#getModelBounds

    Parameters
    ----------

    model : Optional[QSSGRenderModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QSSGBounds3
      A new cute QSSGBounds3 around the copy Qt gave back. Python owns it.
    """
    #  QSSGBounds3 QSSGBufferManager::getModelBounds(const QSSGRenderModel
    #      *model)
    address = self.uglySide.call(
        'ritual_ZN17QSSGBufferManager14getModelBoundsEPK15QSSGRenderModel',
        self._addressOf(model),
    )
    from ..QtQuick3DUtils import QSSGBounds3
    return QSSGBounds3._cuteOwning(address)

  @overload(int, QSSGRenderLayer)
  @overload(int, NoneType)
  def cleanupUnreferencedBuffers(
      self,
      frameId: int,
      layer: Optional[QSSGRenderLayer],
  ) -> None:
    """
    Calls Qt's 'void QSSGBufferManager::cleanupUnreferencedBuffers(quint32
    frameId, QSSGRenderLayer *layer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgbuffermanager.html#cleanupUnreferencedBuffers

    Parameters
    ----------

    frameId : int
      Passed on as it is.

    layer : Optional[QSSGRenderLayer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGBufferManager::cleanupUnreferencedBuffers(quint32 frameId,
    #      QSSGRenderLayer *layer)
    self.uglySide.call(
        'ritual_ZN17QSSGBufferManager26cleanupUnreferencedBuffersEjP15QSSGR'
        'enderLayer',
        frameId, self._addressOf(layer),
    )

  @overload(int, QSSGRenderLayer)
  @overload(int, NoneType)
  def resetUsageCounters(
      self,
      frameId: int,
      layer: Optional[QSSGRenderLayer],
  ) -> None:
    """
    Calls Qt's 'void QSSGBufferManager::resetUsageCounters(quint32 frameId,
    QSSGRenderLayer *layer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgbuffermanager.html#resetUsageCounters

    Parameters
    ----------

    frameId : int
      Passed on as it is.

    layer : Optional[QSSGRenderLayer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGBufferManager::resetUsageCounters(quint32 frameId,
    #      QSSGRenderLayer *layer)
    self.uglySide.call(
        'ritual_ZN17QSSGBufferManager18resetUsageCountersEjP15QSSGRenderLay'
        'er',
        frameId, self._addressOf(layer),
    )

  @overload(QSSGRenderGeometry)
  @overload(NoneType)
  @overload(QSSGRenderGeometry, str)
  @overload(NoneType, str)
  def releaseGeometry(
      self,
      geometry: Optional[QSSGRenderGeometry],
      lightmapSource: str = '',
  ) -> None:
    """
    Calls Qt's 'void QSSGBufferManager::releaseGeometry(QSSGRenderGeometry
    *geometry, const QString &lightmapSource)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgbuffermanager.html#releaseGeometry

    Parameters
    ----------

    geometry : Optional[QSSGRenderGeometry]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    lightmapSource : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QSSGBufferManager::releaseGeometry(QSSGRenderGeometry *geometry,
    #      const QString &lightmapSource)
    self.uglySide.call(
        'ritual_ZN17QSSGBufferManager15releaseGeometryEP18QSSGRenderGeometr'
        'yRK7QString',
        self._addressOf(geometry), lightmapSource,
    )

  @overload(QSSGRenderTextureData)
  @overload(NoneType)
  def releaseTextureData(
      self,
      data: Optional[QSSGRenderTextureData],
  ) -> None:
    """
    Calls Qt's 'void QSSGBufferManager::releaseTextureData(const
    QSSGRenderTextureData *data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgbuffermanager.html#releaseTextureData

    Parameters
    ----------

    data : Optional[QSSGRenderTextureData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGBufferManager::releaseTextureData(const QSSGRenderTextureData
    #      *data)
    self.uglySide.call(
        'ritual_ZN17QSSGBufferManager18releaseTextureDataEPK21QSSGRenderTex'
        'tureData',
        self._addressOf(data),
    )

  @overload(CustomImageCacheKey)
  def releaseTextureData(self, key: CustomImageCacheKey) -> None:
    """
    Calls Qt's 'void QSSGBufferManager::releaseTextureData(const
    CustomImageCacheKey &key)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgbuffermanager.html#releaseTextureData

    Parameters
    ----------

    key : CustomImageCacheKey
      Passed on as a value: Qt reads the C++
      QSSGBufferManager::CustomImageCacheKey, which stays Python's own.
    """
    #  void QSSGBufferManager::releaseTextureData(const CustomImageCacheKey
    #      &key)
    self.uglySide.call(
        'ritual_ZN17QSSGBufferManager18releaseTextureDataERKNS_19CustomImag'
        'eCacheKeyE',
        self._valueOf(key),
    )

  def commitBufferResourceUpdates(self) -> None:
    """
    Calls Qt's 'void QSSGBufferManager::commitBufferResourceUpdates()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgbuffermanager.html#commitBufferResourceUpdates
    """
    #  void QSSGBufferManager::commitBufferResourceUpdates()
    self.uglySide.call(
        'ritual_ZN17QSSGBufferManager27commitBufferResourceUpdatesEv',
    )

  @overload(QSSGRenderResourceLoader)
  @overload(NoneType)
  def processResourceLoader(
      self,
      loader: Optional[QSSGRenderResourceLoader],
  ) -> None:
    """
    Calls Qt's 'void QSSGBufferManager::processResourceLoader(const
    QSSGRenderResourceLoader *loader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgbuffermanager.html#processResourceLoader

    Parameters
    ----------

    loader : Optional[QSSGRenderResourceLoader]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGBufferManager::processResourceLoader(const
    #      QSSGRenderResourceLoader *loader)
    self.uglySide.call(
        'ritual_ZN17QSSGBufferManager21processResourceLoaderEPK24QSSGRender'
        'ResourceLoader',
        self._addressOf(loader),
    )

  def meshUpdateMutex(self) -> Optional[QMutex]:
    """
    Calls Qt's 'QMutex *QSSGBufferManager::meshUpdateMutex()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgbuffermanager.html#meshUpdateMutex

    Returns
    -------

    Optional[QMutex]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMutex *QSSGBufferManager::meshUpdateMutex()
    address = self.uglySide.call(
        'ritual_ZN17QSSGBufferManager15meshUpdateMutexEv',
    )
    from ..QtCore import QMutex
    return QMutex._cuteAt(address)

  @overload(QRhiTexture)
  @overload(NoneType)
  def increaseMemoryStat(self, texture: Optional[QRhiTexture]) -> None:
    """
    Calls Qt's 'void QSSGBufferManager::increaseMemoryStat(QRhiTexture
    *texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgbuffermanager.html#increaseMemoryStat

    Parameters
    ----------

    texture : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGBufferManager::increaseMemoryStat(QRhiTexture *texture)
    self.uglySide.call(
        'ritual_ZN17QSSGBufferManager18increaseMemoryStatEP11QRhiTexture',
        self._addressOf(texture),
    )

  @overload(QSSGRenderMesh)
  def increaseMemoryStat(self, mesh: Optional[QSSGRenderMesh]) -> None:
    """
    Calls Qt's 'void QSSGBufferManager::increaseMemoryStat(QSSGRenderMesh
    *mesh)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgbuffermanager.html#increaseMemoryStat

    Parameters
    ----------

    mesh : Optional[QSSGRenderMesh]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGBufferManager::increaseMemoryStat(QSSGRenderMesh *mesh)
    self.uglySide.call(
        'ritual_ZN17QSSGBufferManager18increaseMemoryStatEP14QSSGRenderMesh',
        self._addressOf(mesh),
    )

  @overload(QRhiTexture)
  @overload(NoneType)
  def decreaseMemoryStat(self, texture: Optional[QRhiTexture]) -> None:
    """
    Calls Qt's 'void QSSGBufferManager::decreaseMemoryStat(QRhiTexture
    *texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgbuffermanager.html#decreaseMemoryStat

    Parameters
    ----------

    texture : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGBufferManager::decreaseMemoryStat(QRhiTexture *texture)
    self.uglySide.call(
        'ritual_ZN17QSSGBufferManager18decreaseMemoryStatEP11QRhiTexture',
        self._addressOf(texture),
    )

  @overload(QSSGRenderMesh)
  def decreaseMemoryStat(self, mesh: Optional[QSSGRenderMesh]) -> None:
    """
    Calls Qt's 'void QSSGBufferManager::decreaseMemoryStat(QSSGRenderMesh
    *mesh)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgbuffermanager.html#decreaseMemoryStat

    Parameters
    ----------

    mesh : Optional[QSSGRenderMesh]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGBufferManager::decreaseMemoryStat(QSSGRenderMesh *mesh)
    self.uglySide.call(
        'ritual_ZN17QSSGBufferManager18decreaseMemoryStatEP14QSSGRenderMesh',
        self._addressOf(mesh),
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QSSGBufferManager::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qssgbuffermanager.html#clear
    """
    #  void QSSGBufferManager::clear()
    self.uglySide.call('ritual_ZN17QSSGBufferManager5clearEv')

  def meshBufferUpdateBatch(self) -> Optional[QRhiResourceUpdateBatch]:
    """
    Calls Qt's 'QRhiResourceUpdateBatch
    *QSSGBufferManager::meshBufferUpdateBatch()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgbuffermanager.html#meshBufferUpdateBatch

    Returns
    -------

    Optional[QRhiResourceUpdateBatch]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiResourceUpdateBatch *QSSGBufferManager::meshBufferUpdateBatch()
    address = self.uglySide.call(
        'ritual_ZN17QSSGBufferManager21meshBufferUpdateBatchEv',
    )
    from ..QtGui import QRhiResourceUpdateBatch
    return QRhiResourceUpdateBatch._cuteAt(address)

  @overload(QSSGRenderPath, QSSGMeshProcessingOptions)
  def loadRenderMesh(
      self,
      inSourcePath: QSSGRenderPath,
      options: QSSGMeshProcessingOptions,
  ) -> Optional[QSSGRenderMesh]:
    """
    Calls Qt's 'QSSGRenderMesh *QSSGBufferManager::loadRenderMesh(const
    QSSGRenderPath &inSourcePath, QSSGMeshProcessingOptions options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgbuffermanager.html#loadRenderMesh

    Parameters
    ----------

    inSourcePath : QSSGRenderPath
      Passed on as a value: Qt reads the C++ QSSGRenderPath, which stays
      Python's own.

    options : QSSGMeshProcessingOptions
      Passed on as a value: Qt reads the C++ QSSGMeshProcessingOptions, which
      stays Python's own.

    Returns
    -------

    Optional[QSSGRenderMesh]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGRenderMesh *QSSGBufferManager::loadRenderMesh(const QSSGRenderPath
    #      &inSourcePath, QSSGMeshProcessingOptions options)
    address = self.uglySide.call(
        'ritual_ZN17QSSGBufferManager14loadRenderMeshERK14QSSGRenderPath25Q'
        'SSGMeshProcessingOptions',
        self._valueOf(inSourcePath), self._valueOf(options),
    )
    from . import QSSGRenderMesh
    return QSSGRenderMesh._cuteAt(address)

  @overload(QSSGRenderGeometry, QSSGMeshProcessingOptions)
  @overload(NoneType, QSSGMeshProcessingOptions)
  def loadRenderMesh(
      self,
      geometry: Optional[QSSGRenderGeometry],
      options: QSSGMeshProcessingOptions,
  ) -> Optional[QSSGRenderMesh]:
    """
    Calls Qt's 'QSSGRenderMesh
    *QSSGBufferManager::loadRenderMesh(QSSGRenderGeometry *geometry,
    QSSGMeshProcessingOptions options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgbuffermanager.html#loadRenderMesh

    Parameters
    ----------

    geometry : Optional[QSSGRenderGeometry]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    options : QSSGMeshProcessingOptions
      Passed on as a value: Qt reads the C++ QSSGMeshProcessingOptions, which
      stays Python's own.

    Returns
    -------

    Optional[QSSGRenderMesh]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGRenderMesh *QSSGBufferManager::loadRenderMesh(QSSGRenderGeometry
    #      *geometry, QSSGMeshProcessingOptions options)
    address = self.uglySide.call(
        'ritual_ZN17QSSGBufferManager14loadRenderMeshEP18QSSGRenderGeometry'
        '25QSSGMeshProcessingOptions',
        self._addressOf(geometry), self._valueOf(options),
    )
    from . import QSSGRenderMesh
    return QSSGRenderMesh._cuteAt(address)

  @overload(WAIT['QSSGMesh.Mesh'])
  @overload(WAIT['QSSGMesh.Mesh'], str)
  def createRenderMesh(
      self,
      mesh: QSSGMesh.Mesh,
      debugObjectName: str = '',
  ) -> Optional[QSSGRenderMesh]:
    """
    Calls Qt's 'QSSGRenderMesh *QSSGBufferManager::createRenderMesh(const
    QSSGMesh::Mesh &mesh, const QString &debugObjectName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgbuffermanager.html#createRenderMesh

    Parameters
    ----------

    mesh : QSSGMesh.Mesh
      Passed on as a value: Qt reads the C++ QSSGMesh::Mesh, which stays
      Python's own.

    debugObjectName : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    Optional[QSSGRenderMesh]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGRenderMesh *QSSGBufferManager::createRenderMesh(const
    #      QSSGMesh::Mesh &mesh, const QString &debugObjectName)
    address = self.uglySide.call(
        'ritual_ZN17QSSGBufferManager16createRenderMeshERKN8QSSGMesh4MeshER'
        'K7QString',
        self._valueOf(mesh), debugObjectName,
    )
    from . import QSSGRenderMesh
    return QSSGRenderMesh._cuteAt(address)

  @overload(QSSGLoadedTexture, QSSGRenderImageTexture, str)
  @overload(QSSGLoadedTexture, NoneType, str)
  @overload(NoneType, QSSGRenderImageTexture, str)
  @overload(NoneType, NoneType, str)
  def createEnvironmentMap(
      self,
      inImage: Optional[QSSGLoadedTexture],
      outTexture: Optional[QSSGRenderImageTexture],
      debugObjectName: str,
  ) -> bool:
    """
    Calls Qt's 'bool QSSGBufferManager::createEnvironmentMap(const
    QSSGLoadedTexture *inImage, QSSGRenderImageTexture *outTexture, const
    QString &debugObjectName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgbuffermanager.html#createEnvironmentMap

    Parameters
    ----------

    inImage : Optional[QSSGLoadedTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    outTexture : Optional[QSSGRenderImageTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    debugObjectName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QSSGBufferManager::createEnvironmentMap(const QSSGLoadedTexture
    #      *inImage, QSSGRenderImageTexture *outTexture, const QString
    #      &debugObjectName)
    return self.uglySide.call(
        'ritual_ZN17QSSGBufferManager20createEnvironmentMapEPK17QSSGLoadedT'
        'extureP22QSSGRenderImageTextureRK7QString',
        self._addressOf(inImage), self._addressOf(outTexture),
        debugObjectName,
    )

  @overload(QSSGRenderPath)
  def releaseMesh(self, inSourcePath: QSSGRenderPath) -> None:
    """
    Calls Qt's 'void QSSGBufferManager::releaseMesh(const QSSGRenderPath
    &inSourcePath)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgbuffermanager.html#releaseMesh

    Parameters
    ----------

    inSourcePath : QSSGRenderPath
      Passed on as a value: Qt reads the C++ QSSGRenderPath, which stays
      Python's own.
    """
    #  void QSSGBufferManager::releaseMesh(const QSSGRenderPath
    #      &inSourcePath)
    self.uglySide.call(
        'ritual_ZN17QSSGBufferManager11releaseMeshERK14QSSGRenderPath',
        self._valueOf(inSourcePath),
    )

  @overload(ImageCacheKey)
  def releaseImage(self, key: ImageCacheKey) -> None:
    """
    Calls Qt's 'void QSSGBufferManager::releaseImage(const ImageCacheKey
    &key)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgbuffermanager.html#releaseImage

    Parameters
    ----------

    key : ImageCacheKey
      Passed on as a value: Qt reads the C++
      QSSGBufferManager::ImageCacheKey, which stays Python's own.
    """
    #  void QSSGBufferManager::releaseImage(const ImageCacheKey &key)
    self.uglySide.call(
        'ritual_ZN17QSSGBufferManager12releaseImageERKNS_13ImageCacheKeyE',
        self._valueOf(key),
    )

  def validateLightmap(self) -> bool:
    """
    Calls Qt's 'bool QSSGBufferManager::validateLightmap()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgbuffermanager.html#validateLightmap
    """
    #  bool QSSGBufferManager::validateLightmap()
    return self.uglySide.call(
        'ritual_ZN17QSSGBufferManager16validateLightmapEv',
    )

  @staticmethod
  def getCustomMeshMap(*__, **_) -> Never:
    """
    Qt's 'const QHash<std::pair<QSSGRenderGeometry *, QString>, MeshData>
    &QSSGBufferManager::getCustomMeshMap() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QSSGBufferManager.getCustomMeshMap' has no cute function yet. "
        "Qt's 'const QHash<std::pair<QSSGRenderGeometry *, QString>, "
        "MeshData> &QSSGBufferManager::getCustomMeshMap() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def getCustomTextureMap(*__, **_) -> Never:
    """
    Qt's 'const QHash<CustomImageCacheKey, ImageData>
    &QSSGBufferManager::getCustomTextureMap() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGBufferManager.getCustomTextureMap' has no cute function yet. "
        "Qt's 'const QHash<CustomImageCacheKey, ImageData> "
        "&QSSGBufferManager::getCustomTextureMap() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def getImageMap(*__, **_) -> Never:
    """
    Qt's 'const QHash<ImageCacheKey, ImageData>
    &QSSGBufferManager::getImageMap() const': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'QSSGBufferManager.getImageMap' has no cute function yet. Qt's "
        "'const QHash<ImageCacheKey, ImageData> "
        "&QSSGBufferManager::getImageMap() const': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def getMeshForPicking(*__, **_) -> Never:
    """
    Qt's 'QSSGRenderMesh *QSSGBufferManager::getMeshForPicking(const
    QSSGRenderModel &model, const QString &lightmap) const': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGBufferManager.getMeshForPicking' has no cute function yet. "
        "Qt's 'QSSGRenderMesh *QSSGBufferManager::getMeshForPicking(const "
        "QSSGRenderModel &model, const QString &lightmap) const': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def getMeshMap(*__, **_) -> Never:
    """
    Qt's 'const QHash<std::pair<QSSGRenderPath, QString>, MeshData>
    &QSSGBufferManager::getMeshMap() const': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'QSSGBufferManager.getMeshMap' has no cute function yet. Qt's "
        "'const QHash<std::pair<QSSGRenderPath, QString>, MeshData> "
        "&QSSGBufferManager::getMeshMap() const': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def getSGImageMap(*__, **_) -> Never:
    """
    Qt's 'const QHash<QSGTexture *, ImageData>
    &QSSGBufferManager::getSGImageMap() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QSSGBufferManager.getSGImageMap' has no cute function yet. Qt's "
        "'const QHash<QSGTexture *, ImageData> "
        "&QSSGBufferManager::getSGImageMap() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def loadLightmap(*__, **_) -> Never:
    """
    Qt's 'QSSGRenderImageTexture QSSGBufferManager::loadLightmap(const
    QSSGRenderModel &model)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QSSGBufferManager.loadLightmap' has no cute function yet. Qt's "
        "'QSSGRenderImageTexture QSSGBufferManager::loadLightmap(const "
        "QSSGRenderModel &model)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def loadLightmapMesh(*__, **_) -> Never:
    """
    Qt's 'QSSGMesh::Mesh QSSGBufferManager::loadLightmapMesh(const
    QSSGRenderModel &model)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QSSGBufferManager.loadLightmapMesh' has no cute function yet. "
        "Qt's 'QSSGMesh::Mesh QSSGBufferManager::loadLightmapMesh(const "
        "QSSGRenderModel &model)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def loadMesh(*__, **_) -> Never:
    """
    Qt's 'QSSGRenderMesh *QSSGBufferManager::loadMesh(const QSSGRenderModel
    &model)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGBufferManager.loadMesh' has no cute function yet. Qt's "
        "'QSSGRenderMesh *QSSGBufferManager::loadMesh(const QSSGRenderModel "
        "&model)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def loadMeshBVH(*__, **_) -> Never:
    """
    - Qt's 'std::unique_ptr<QSSGMeshBVH> QSSGBufferManager::loadMeshBVH(const
      QSSGRenderPath &inSourcePath)': gives a type Python has no way to take
      yet.
    - Qt's 'std::unique_ptr<QSSGMeshBVH>
      QSSGBufferManager::loadMeshBVH(QSSGRenderGeometry *geometry)': gives a
      type Python has no way to take yet.
    - Qt's 'std::unique_ptr<QSSGMeshBVH> QSSGBufferManager::loadMeshBVH(const
      QSSGMesh::Mesh &mesh)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGBufferManager.loadMeshBVH' has no cute function yet. Qt's "
        "'std::unique_ptr<QSSGMeshBVH> QSSGBufferManager::loadMeshBVH(const "
        "QSSGRenderPath &inSourcePath)': gives a type Python has no way to "
        "take yet. Qt's 'std::unique_ptr<QSSGMeshBVH> "
        "QSSGBufferManager::loadMeshBVH(QSSGRenderGeometry *geometry)': "
        "gives a type Python has no way to take yet. Qt's "
        "'std::unique_ptr<QSSGMeshBVH> QSSGBufferManager::loadMeshBVH(const "
        "QSSGMesh::Mesh &mesh)': gives a type Python has no way to take yet."
    )

  @staticmethod
  def registerExtensionResult(*__, **_) -> Never:
    """
    Qt's 'void QSSGBufferManager::registerExtensionResult(const
    QSSGRenderExtension &extensions, QRhiTexture *texture)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGBufferManager.registerExtensionResult' has no cute function "
        "yet. Qt's 'void QSSGBufferManager::registerExtensionResult(const "
        "QSSGRenderExtension &extensions, QRhiTexture *texture)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def registerMeshData(*__, **_) -> Never:
    """
    Qt's 'void QSSGBufferManager::registerMeshData(const QString &assetId,
    const QVector<QSSGMesh::Mesh> &meshData)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGBufferManager.registerMeshData' has no cute function yet. "
        "Qt's 'void QSSGBufferManager::registerMeshData(const QString "
        "&assetId, const QVector<QSSGMesh::Mesh> &meshData)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def registerUserRenderPassManager(*__, **_) -> Never:
    """
    Qt's 'void QSSGBufferManager::registerUserRenderPassManager(const
    QSSGUserRenderPassManagerPtr &userPassManager)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGBufferManager.registerUserRenderPassManager' has no cute "
        "function yet. Qt's 'void "
        "QSSGBufferManager::registerUserRenderPassManager(const "
        "QSSGUserRenderPassManagerPtr &userPassManager)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def releaseExtensionResult(*__, **_) -> Never:
    """
    Qt's 'void QSSGBufferManager::releaseExtensionResult(const
    QSSGRenderExtension &rext)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QSSGBufferManager.releaseExtensionResult' has no cute function "
        "yet. Qt's 'void QSSGBufferManager::releaseExtensionResult(const "
        "QSSGRenderExtension &rext)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def releaseUserRenderPass(*__, **_) -> Never:
    """
    Qt's 'void QSSGBufferManager::releaseUserRenderPass(const
    QSSGRenderUserPass &upass)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QSSGBufferManager.releaseUserRenderPass' has no cute function "
        "yet. Qt's 'void QSSGBufferManager::releaseUserRenderPass(const "
        "QSSGRenderUserPass &upass)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def setRhiTexture(*__, **_) -> Never:
    """
    Qt's 'bool QSSGBufferManager::setRhiTexture(QSSGRenderImageTexture
    &texture, const QSSGLoadedTexture *inTexture, MipMode inMipMode,
    CreateRhiTextureFlags inFlags, const QString &debugObjectName, bool
    *wasTextureCreated)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGBufferManager.setRhiTexture' has no cute function yet. Qt's "
        "'bool QSSGBufferManager::setRhiTexture(QSSGRenderImageTexture "
        "&texture, const QSSGLoadedTexture *inTexture, MipMode inMipMode, "
        "CreateRhiTextureFlags inFlags, const QString &debugObjectName, "
        "bool *wasTextureCreated)': takes a type Python has no way to hand "
        "over yet.")
