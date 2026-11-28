"""
QSSGRenderSkyMaterialManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderskymaterialmanager_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRenderSkyMaterialManager to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QSSGRenderImageTexture, QSSGRenderSkyMaterial
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSSGRenderSkyMaterial = WAIT['QSSGRenderSkyMaterial']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSSGRenderSkyMaterialManager(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGRenderSkyMaterialManager: a plain Python object
  standing in front of one C++ QSSGRenderSkyMaterialManager.

  What exists
  -----------

  Every function of Qt's QSSGRenderSkyMaterialManager that has a ritual and
  that Python can call so far, 4 names in all: 'releaseCachedResources',
  'resolve', 'ensureEnvironmentMap', 'clearPrefilterCache'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGRenderSkyMaterialManager::QSSGRenderSkyMaterialManager(const
    QSSGRenderContextInterface &inContext)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QSSGRenderSkyMaterialManager::~QSSGRenderSkyMaterialManager()': the
    destructor: Python never removes a C++ QSSGRenderSkyMaterialManager.

  What has no ritual
  ------------------

  11 of the 17 functions Qt declares: 8 the compiler refuses its ritual as it
  would be written here; 2 forbidden; 1 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QSSGRenderSkyMaterialManager is created at the first use, not by
    'QSSGRenderSkyMaterialManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGRenderSkyMaterialManager.
  - Each name of Qt's QSSGRenderSkyMaterialManager that has no cute function
    yet, '__init__', 'computeFrameState', 'deriveCycleState',
    'ensureSharedResources', 'ensureTextures', 'initializeTailMips',
    'renderEnvironmentCube', 'runEnvironmentMipChain', 'runPrefilterCycle',
    'validateAndUpdateCacheKey', holds a function that raises
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
  __qt_class__ = 'QSSGRenderSkyMaterialManager'

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
    Qt's 'QSSGRenderSkyMaterialManager::QSSGRenderSkyMaterialManager(const
    QSSGRenderContextInterface &inContext)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderSkyMaterialManager.__init__' has no cute function yet. "
        "Qt's "
        "'QSSGRenderSkyMaterialManager::QSSGRenderSkyMaterialManager(const "
        "QSSGRenderContextInterface &inContext)': takes a type Python has "
        "no way to hand over yet.")

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
    Calls Qt's 'void QSSGRenderSkyMaterialManager::releaseCachedResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderskymaterialmanager.html
    """
    #  void QSSGRenderSkyMaterialManager::releaseCachedResources()
    self.uglySide.call(
        'ritual_ZN28QSSGRenderSkyMaterialManager22releaseCachedResourcesEv',
    )

  @overload(QSSGRenderSkyMaterial)
  @overload(NoneType)
  def resolve(
      self,
      settings: Optional[QSSGRenderSkyMaterial],
  ) -> QSSGRenderImageTexture:
    """
    Calls Qt's 'QSSGRenderImageTexture
    QSSGRenderSkyMaterialManager::resolve(QSSGRenderSkyMaterial *settings)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderskymaterialmanager.html#resolve

    Parameters
    ----------

    settings : Optional[QSSGRenderSkyMaterial]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QSSGRenderImageTexture
      A new cute QSSGRenderImageTexture around the copy Qt gave back. Python
      owns it.
    """
    #  QSSGRenderImageTexture
    #      QSSGRenderSkyMaterialManager::resolve(QSSGRenderSkyMaterial
    #      *settings)
    address = self.uglySide.call(
        'ritual_ZN28QSSGRenderSkyMaterialManager7resolveEP21QSSGRenderSkyMa'
        'terial',
        self._addressOf(settings),
    )
    from . import QSSGRenderImageTexture
    return QSSGRenderImageTexture._cuteOwning(address)

  @overload(QSSGRenderSkyMaterial)
  @overload(NoneType)
  def ensureEnvironmentMap(
      self,
      settings: Optional[QSSGRenderSkyMaterial],
  ) -> bool:
    """
    Calls Qt's 'bool
    QSSGRenderSkyMaterialManager::ensureEnvironmentMap(QSSGRenderSkyMaterial
    *settings)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderskymaterialmanager.html

    Parameters
    ----------

    settings : Optional[QSSGRenderSkyMaterial]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSSGRenderSkyMaterialManager::ensureEnvironmentMap(
    #      QSSGRenderSkyMaterial *settings)
    return self.uglySide.call(
        'ritual_ZN28QSSGRenderSkyMaterialManager20ensureEnvironmentMapEP21Q'
        'SSGRenderSkyMaterial',
        self._addressOf(settings),
    )

  def clearPrefilterCache(self) -> None:
    """
    Calls Qt's 'void QSSGRenderSkyMaterialManager::clearPrefilterCache()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderskymaterialmanager.html
    """
    #  void QSSGRenderSkyMaterialManager::clearPrefilterCache()
    self.uglySide.call(
        'ritual_ZN28QSSGRenderSkyMaterialManager19clearPrefilterCacheEv',
    )

  @staticmethod
  def computeFrameState(*__, **_) -> Never:
    """
    Qt's 'bool
    QSSGRenderSkyMaterialManager::computeFrameState(QSSGRenderSkyMaterial
    *inSky, FrameState &fs)': the compiler refuses its ritual as it would be
    written here: unknown type name 'FrameState'; did you mean
    'QSSGRenderSkyMaterialManager::FrameState'?.
    """
    raise NotImplementedError(
        "'QSSGRenderSkyMaterialManager.computeFrameState' has no cute "
        "function yet. Qt's 'bool "
        "QSSGRenderSkyMaterialManager::computeFrameState(QSSGRenderSkyMateri"
        "al *inSky, FrameState &fs)': the compiler refuses its ritual as it "
        "would be written here: unknown type name 'FrameState'; did you "
        "mean 'QSSGRenderSkyMaterialManager::FrameState'?.")

  @staticmethod
  def deriveCycleState(*__, **_) -> Never:
    """
    Qt's 'void
    QSSGRenderSkyMaterialManager::deriveCycleState(QSSGRenderSkyMaterial
    *inSky, FrameState &fs)': the compiler refuses its ritual as it would be
    written here: unknown type name 'FrameState'; did you mean
    'QSSGRenderSkyMaterialManager::FrameState'?.
    """
    raise NotImplementedError(
        "'QSSGRenderSkyMaterialManager.deriveCycleState' has no cute "
        "function yet. Qt's 'void "
        "QSSGRenderSkyMaterialManager::deriveCycleState(QSSGRenderSkyMateria"
        "l *inSky, FrameState &fs)': the compiler refuses its ritual as it "
        "would be written here: unknown type name 'FrameState'; did you "
        "mean 'QSSGRenderSkyMaterialManager::FrameState'?.")

  @staticmethod
  def ensureSharedResources(*__, **_) -> Never:
    """
    Qt's 'bool QSSGRenderSkyMaterialManager::ensureSharedResources(FrameState
    &fs, QRhiCommandBuffer *cb)': the compiler refuses its ritual as it would
    be written here: unknown type name 'FrameState'; did you mean
    'QSSGRenderSkyMaterialManager::FrameState'?.
    """
    raise NotImplementedError(
        "'QSSGRenderSkyMaterialManager.ensureSharedResources' has no cute "
        "function yet. Qt's 'bool "
        "QSSGRenderSkyMaterialManager::ensureSharedResources(FrameState "
        "&fs, QRhiCommandBuffer *cb)': the compiler refuses its ritual as "
        "it would be written here: unknown type name 'FrameState'; did you "
        "mean 'QSSGRenderSkyMaterialManager::FrameState'?.")

  @staticmethod
  def ensureTextures(*__, **_) -> Never:
    """
    Qt's 'bool QSSGRenderSkyMaterialManager::ensureTextures(FrameState &fs)':
    the compiler refuses its ritual as it would be written here: unknown type
    name 'FrameState'; did you mean
    'QSSGRenderSkyMaterialManager::FrameState'?.
    """
    raise NotImplementedError(
        "'QSSGRenderSkyMaterialManager.ensureTextures' has no cute function "
        "yet. Qt's 'bool "
        "QSSGRenderSkyMaterialManager::ensureTextures(FrameState &fs)': the "
        "compiler refuses its ritual as it would be written here: unknown "
        "type name 'FrameState'; did you mean "
        "'QSSGRenderSkyMaterialManager::FrameState'?.")

  @staticmethod
  def initializeTailMips(*__, **_) -> Never:
    """
    Qt's 'void QSSGRenderSkyMaterialManager::initializeTailMips(const
    FrameState &fs, QRhiCommandBuffer *cb)': the compiler refuses its ritual
    as it would be written here: unknown type name 'FrameState'; did you mean
    'QSSGRenderSkyMaterialManager::FrameState'?.
    """
    raise NotImplementedError(
        "'QSSGRenderSkyMaterialManager.initializeTailMips' has no cute "
        "function yet. Qt's 'void "
        "QSSGRenderSkyMaterialManager::initializeTailMips(const FrameState "
        "&fs, QRhiCommandBuffer *cb)': the compiler refuses its ritual as "
        "it would be written here: unknown type name 'FrameState'; did you "
        "mean 'QSSGRenderSkyMaterialManager::FrameState'?.")

  @staticmethod
  def renderEnvironmentCube(*__, **_) -> Never:
    """
    Qt's 'bool
    QSSGRenderSkyMaterialManager::renderEnvironmentCube(QSSGRenderSkyMaterial
    *inSky, const FrameState &fs, const QSSGRhiShaderPipelinePtr
    &shaderPipeline, QRhiCommandBuffer *cb, QRhiResourceUpdateBatch *rub)':
    the compiler refuses its ritual as it would be written here: unknown type
    name 'FrameState'; did you mean
    'QSSGRenderSkyMaterialManager::FrameState'?.
    """
    raise NotImplementedError(
        "'QSSGRenderSkyMaterialManager.renderEnvironmentCube' has no cute "
        "function yet. Qt's 'bool "
        "QSSGRenderSkyMaterialManager::renderEnvironmentCube(QSSGRenderSkyMa"
        "terial *inSky, const FrameState &fs, const "
        "QSSGRhiShaderPipelinePtr &shaderPipeline, QRhiCommandBuffer *cb, "
        "QRhiResourceUpdateBatch *rub)': the compiler refuses its ritual as "
        "it would be written here: unknown type name 'FrameState'; did you "
        "mean 'QSSGRenderSkyMaterialManager::FrameState'?.")

  @staticmethod
  def runEnvironmentMipChain(*__, **_) -> Never:
    """
    Qt's 'void QSSGRenderSkyMaterialManager::runEnvironmentMipChain(const
    FrameState &fs, QRhiCommandBuffer *cb)': the compiler refuses its ritual
    as it would be written here: unknown type name 'FrameState'; did you mean
    'QSSGRenderSkyMaterialManager::FrameState'?.
    """
    raise NotImplementedError(
        "'QSSGRenderSkyMaterialManager.runEnvironmentMipChain' has no cute "
        "function yet. Qt's 'void "
        "QSSGRenderSkyMaterialManager::runEnvironmentMipChain(const "
        "FrameState &fs, QRhiCommandBuffer *cb)': the compiler refuses its "
        "ritual as it would be written here: unknown type name "
        "'FrameState'; did you mean "
        "'QSSGRenderSkyMaterialManager::FrameState'?.")

  @staticmethod
  def runPrefilterCycle(*__, **_) -> Never:
    """
    Qt's 'bool
    QSSGRenderSkyMaterialManager::runPrefilterCycle(QSSGRenderSkyMaterial
    *inSky, const FrameState &fs, QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *&rub)': takes or gives a type that cannot be
    passed yet: QRhiResourceUpdateBatch *&.
    """
    raise NotImplementedError(
        "'QSSGRenderSkyMaterialManager.runPrefilterCycle' has no cute "
        "function yet. Qt's 'bool "
        "QSSGRenderSkyMaterialManager::runPrefilterCycle(QSSGRenderSkyMateri"
        "al *inSky, const FrameState &fs, QRhiCommandBuffer *cb, "
        "QRhiResourceUpdateBatch *&rub)': takes or gives a type that cannot "
        "be passed yet: QRhiResourceUpdateBatch *&.")

  @staticmethod
  def validateAndUpdateCacheKey(*__, **_) -> Never:
    """
    Qt's 'void QSSGRenderSkyMaterialManager::validateAndUpdateCacheKey(const
    FrameState &fs, QSSGRhiShaderPipeline *envShaderPipelineKey)': the
    compiler refuses its ritual as it would be written here: unknown type
    name 'FrameState'; did you mean
    'QSSGRenderSkyMaterialManager::FrameState'?.
    """
    raise NotImplementedError(
        "'QSSGRenderSkyMaterialManager.validateAndUpdateCacheKey' has no "
        "cute function yet. Qt's 'void "
        "QSSGRenderSkyMaterialManager::validateAndUpdateCacheKey(const "
        "FrameState &fs, QSSGRhiShaderPipeline *envShaderPipelineKey)': the "
        "compiler refuses its ritual as it would be written here: unknown "
        "type name 'FrameState'; did you mean "
        "'QSSGRenderSkyMaterialManager::FrameState'?.")
