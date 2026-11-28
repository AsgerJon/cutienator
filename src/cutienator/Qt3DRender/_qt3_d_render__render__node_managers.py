"""
Qt3DRender::Render::NodeManagers binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/nodemanagers_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DRender::Render::NodeManagers to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional


class NodeManagers(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DRender::Render::NodeManagers: a plain Python
  object standing in front of one C++ Qt3DRender::Render::NodeManagers.

  C++ hands a Qt3DRender::Render::NodeManagers around as a copy, so every C++
  Qt3DRender::Render::NodeManagers behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::NodeManagers that has a ritual
  and that Python can call so far, 36 names in all: 'cameraManager',
  'renderNodesManager', 'materialManager', 'worldMatrixManager',
  'shaderManager', 'shaderBuilderManager', 'techniqueManager',
  'effectManager', 'renderPassManager', 'textureManager', 'layerManager',
  'levelOfDetailManager', 'filterKeyManager', 'frameGraphManager',
  'transformManager', 'renderTargetManager', 'sceneManager',
  'attachmentManager', 'parameterManager', 'shaderDataManager',
  'textureImageManager', 'bufferManager', 'attributeManager',
  'geometryManager', 'geometryRendererManager', 'objectPickerManager',
  'rayCasterManager', 'lightManager', 'environmentLightManager',
  'computeJobManager', 'renderStateManager', 'armatureManager',
  'skeletonManager', 'jointManager', 'shaderImageManager',
  'pickingProxyManager'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::NodeManagers::~NodeManagers()': the destructor:
    Python removes its C++ Qt3DRender::Render::NodeManagers by it, and has no
    other use for it.

  What has no ritual
  ------------------

  4 of the 42 functions Qt declares: 4 a template.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::NodeManagers is created at the first use, not
    by 'Qt3DRender::Render::NodeManagers(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DRender::Render::NodeManagers back gives a copy
    the ritual made for Python, in a new cute
    Qt3DRender::Render::NodeManagers.
  - Each name of Qt's Qt3DRender::Render::NodeManagers that has no cute
    function yet, 'data', 'lookupHandle', 'lookupResource', 'manager', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::NodeManagers'

  #  Qt's '~Qt3DRender::Render::NodeManagers()'. Naming it makes this a value
  #  class: Python owns every C++ Qt3DRender::Render::NodeManagers behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10Qt3DRender6Render12NodeManagersD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def cameraManager(self) -> Optional[Qt3DRender.Render.CameraManager]:
    """
    Calls Qt's 'CameraManager
    *Qt3DRender::Render::NodeManagers::cameraManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-nodemanagers.html#cameraManager

    Returns
    -------

    Optional[Qt3DRender.Render.CameraManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  CameraManager *Qt3DRender::Render::NodeManagers::cameraManager() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12NodeManagers13cameraManagerEv',
    )
    return Qt3DRender.Render.CameraManager._cuteAt(address)

  def renderNodesManager(self) -> Optional[Qt3DRender.Render.EntityManager]:
    """
    Calls Qt's 'EntityManager
    *Qt3DRender::Render::NodeManagers::renderNodesManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-nodemanagers.html

    Returns
    -------

    Optional[Qt3DRender.Render.EntityManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  EntityManager *Qt3DRender::Render::NodeManagers::renderNodesManager()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12NodeManagers18renderNodesManagerEv',
    )
    return Qt3DRender.Render.EntityManager._cuteAt(address)

  def materialManager(self) -> Optional[Qt3DRender.Render.MaterialManager]:
    """
    Calls Qt's 'MaterialManager
    *Qt3DRender::Render::NodeManagers::materialManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-nodemanagers.html

    Returns
    -------

    Optional[Qt3DRender.Render.MaterialManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  MaterialManager *Qt3DRender::Render::NodeManagers::materialManager()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12NodeManagers15materialManagerEv',
    )
    return Qt3DRender.Render.MaterialManager._cuteAt(address)

  def worldMatrixManager(self) -> Optional[Qt3DRender.Render.MatrixManager]:
    """
    Calls Qt's 'MatrixManager
    *Qt3DRender::Render::NodeManagers::worldMatrixManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-nodemanagers.html

    Returns
    -------

    Optional[Qt3DRender.Render.MatrixManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  MatrixManager *Qt3DRender::Render::NodeManagers::worldMatrixManager()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12NodeManagers18worldMatrixManagerEv',
    )
    return Qt3DRender.Render.MatrixManager._cuteAt(address)

  def shaderManager(self) -> Optional[Qt3DRender.Render.ShaderManager]:
    """
    Calls Qt's 'ShaderManager
    *Qt3DRender::Render::NodeManagers::shaderManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-nodemanagers.html#shaderManager

    Returns
    -------

    Optional[Qt3DRender.Render.ShaderManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ShaderManager *Qt3DRender::Render::NodeManagers::shaderManager() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12NodeManagers13shaderManagerEv',
    )
    return Qt3DRender.Render.ShaderManager._cuteAt(address)

  def shaderBuilderManager(
      self,
  ) -> Optional[Qt3DRender.Render.ShaderBuilderManager]:
    """
    Calls Qt's 'ShaderBuilderManager
    *Qt3DRender::Render::NodeManagers::shaderBuilderManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-nodemanagers.html

    Returns
    -------

    Optional[Qt3DRender.Render.ShaderBuilderManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ShaderBuilderManager
    #      *Qt3DRender::Render::NodeManagers::shaderBuilderManager() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12NodeManagers20shaderBuilderManagerE'
        'v',
    )
    return Qt3DRender.Render.ShaderBuilderManager._cuteAt(address)

  def techniqueManager(self) -> Optional[Qt3DRender.Render.TechniqueManager]:
    """
    Calls Qt's 'TechniqueManager
    *Qt3DRender::Render::NodeManagers::techniqueManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-nodemanagers.html

    Returns
    -------

    Optional[Qt3DRender.Render.TechniqueManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  TechniqueManager *Qt3DRender::Render::NodeManagers::techniqueManager()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12NodeManagers16techniqueManagerEv',
    )
    return Qt3DRender.Render.TechniqueManager._cuteAt(address)

  def effectManager(self) -> Optional[Qt3DRender.Render.EffectManager]:
    """
    Calls Qt's 'EffectManager
    *Qt3DRender::Render::NodeManagers::effectManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-nodemanagers.html#effectManager

    Returns
    -------

    Optional[Qt3DRender.Render.EffectManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  EffectManager *Qt3DRender::Render::NodeManagers::effectManager() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12NodeManagers13effectManagerEv',
    )
    return Qt3DRender.Render.EffectManager._cuteAt(address)

  def renderPassManager(
      self,
  ) -> Optional[Qt3DRender.Render.RenderPassManager]:
    """
    Calls Qt's 'RenderPassManager
    *Qt3DRender::Render::NodeManagers::renderPassManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-nodemanagers.html

    Returns
    -------

    Optional[Qt3DRender.Render.RenderPassManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  RenderPassManager
    #      *Qt3DRender::Render::NodeManagers::renderPassManager() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12NodeManagers17renderPassManagerEv',
    )
    return Qt3DRender.Render.RenderPassManager._cuteAt(address)

  def textureManager(self) -> Optional[Qt3DRender.Render.TextureManager]:
    """
    Calls Qt's 'TextureManager
    *Qt3DRender::Render::NodeManagers::textureManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-nodemanagers.html#textureManager

    Returns
    -------

    Optional[Qt3DRender.Render.TextureManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  TextureManager *Qt3DRender::Render::NodeManagers::textureManager()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12NodeManagers14textureManagerEv',
    )
    return Qt3DRender.Render.TextureManager._cuteAt(address)

  def layerManager(self) -> Optional[Qt3DRender.Render.LayerManager]:
    """
    Calls Qt's 'LayerManager
    *Qt3DRender::Render::NodeManagers::layerManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-nodemanagers.html#layerManager

    Returns
    -------

    Optional[Qt3DRender.Render.LayerManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  LayerManager *Qt3DRender::Render::NodeManagers::layerManager() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12NodeManagers12layerManagerEv',
    )
    return Qt3DRender.Render.LayerManager._cuteAt(address)

  def levelOfDetailManager(
      self,
  ) -> Optional[Qt3DRender.Render.LevelOfDetailManager]:
    """
    Calls Qt's 'LevelOfDetailManager
    *Qt3DRender::Render::NodeManagers::levelOfDetailManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-nodemanagers.html

    Returns
    -------

    Optional[Qt3DRender.Render.LevelOfDetailManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  LevelOfDetailManager
    #      *Qt3DRender::Render::NodeManagers::levelOfDetailManager() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12NodeManagers20levelOfDetailManagerE'
        'v',
    )
    return Qt3DRender.Render.LevelOfDetailManager._cuteAt(address)

  def filterKeyManager(self) -> Optional[Qt3DRender.Render.FilterKeyManager]:
    """
    Calls Qt's 'FilterKeyManager
    *Qt3DRender::Render::NodeManagers::filterKeyManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-nodemanagers.html

    Returns
    -------

    Optional[Qt3DRender.Render.FilterKeyManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FilterKeyManager *Qt3DRender::Render::NodeManagers::filterKeyManager()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12NodeManagers16filterKeyManagerEv',
    )
    return Qt3DRender.Render.FilterKeyManager._cuteAt(address)

  def frameGraphManager(
      self,
  ) -> Optional[Qt3DRender.Render.FrameGraphManager]:
    """
    Calls Qt's 'FrameGraphManager
    *Qt3DRender::Render::NodeManagers::frameGraphManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-nodemanagers.html

    Returns
    -------

    Optional[Qt3DRender.Render.FrameGraphManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FrameGraphManager
    #      *Qt3DRender::Render::NodeManagers::frameGraphManager() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12NodeManagers17frameGraphManagerEv',
    )
    return Qt3DRender.Render.FrameGraphManager._cuteAt(address)

  def transformManager(self) -> Optional[Qt3DRender.Render.TransformManager]:
    """
    Calls Qt's 'TransformManager
    *Qt3DRender::Render::NodeManagers::transformManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-nodemanagers.html

    Returns
    -------

    Optional[Qt3DRender.Render.TransformManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  TransformManager *Qt3DRender::Render::NodeManagers::transformManager()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12NodeManagers16transformManagerEv',
    )
    return Qt3DRender.Render.TransformManager._cuteAt(address)

  def renderTargetManager(
      self,
  ) -> Optional[Qt3DRender.Render.RenderTargetManager]:
    """
    Calls Qt's 'RenderTargetManager
    *Qt3DRender::Render::NodeManagers::renderTargetManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-nodemanagers.html

    Returns
    -------

    Optional[Qt3DRender.Render.RenderTargetManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  RenderTargetManager
    #      *Qt3DRender::Render::NodeManagers::renderTargetManager() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12NodeManagers19renderTargetManagerEv',
    )
    return Qt3DRender.Render.RenderTargetManager._cuteAt(address)

  def sceneManager(self) -> Optional[Qt3DRender.Render.SceneManager]:
    """
    Calls Qt's 'SceneManager
    *Qt3DRender::Render::NodeManagers::sceneManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-nodemanagers.html#sceneManager

    Returns
    -------

    Optional[Qt3DRender.Render.SceneManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  SceneManager *Qt3DRender::Render::NodeManagers::sceneManager() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12NodeManagers12sceneManagerEv',
    )
    return Qt3DRender.Render.SceneManager._cuteAt(address)

  def attachmentManager(
      self,
  ) -> Optional[Qt3DRender.Render.AttachmentManager]:
    """
    Calls Qt's 'AttachmentManager
    *Qt3DRender::Render::NodeManagers::attachmentManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-nodemanagers.html

    Returns
    -------

    Optional[Qt3DRender.Render.AttachmentManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  AttachmentManager
    #      *Qt3DRender::Render::NodeManagers::attachmentManager() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12NodeManagers17attachmentManagerEv',
    )
    return Qt3DRender.Render.AttachmentManager._cuteAt(address)

  def parameterManager(self) -> Optional[Qt3DRender.Render.ParameterManager]:
    """
    Calls Qt's 'ParameterManager
    *Qt3DRender::Render::NodeManagers::parameterManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-nodemanagers.html

    Returns
    -------

    Optional[Qt3DRender.Render.ParameterManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ParameterManager *Qt3DRender::Render::NodeManagers::parameterManager()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12NodeManagers16parameterManagerEv',
    )
    return Qt3DRender.Render.ParameterManager._cuteAt(address)

  def shaderDataManager(
      self,
  ) -> Optional[Qt3DRender.Render.ShaderDataManager]:
    """
    Calls Qt's 'ShaderDataManager
    *Qt3DRender::Render::NodeManagers::shaderDataManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-nodemanagers.html

    Returns
    -------

    Optional[Qt3DRender.Render.ShaderDataManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ShaderDataManager
    #      *Qt3DRender::Render::NodeManagers::shaderDataManager() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12NodeManagers17shaderDataManagerEv',
    )
    return Qt3DRender.Render.ShaderDataManager._cuteAt(address)

  def textureImageManager(
      self,
  ) -> Optional[Qt3DRender.Render.TextureImageManager]:
    """
    Calls Qt's 'TextureImageManager
    *Qt3DRender::Render::NodeManagers::textureImageManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-nodemanagers.html

    Returns
    -------

    Optional[Qt3DRender.Render.TextureImageManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  TextureImageManager
    #      *Qt3DRender::Render::NodeManagers::textureImageManager() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12NodeManagers19textureImageManagerEv',
    )
    return Qt3DRender.Render.TextureImageManager._cuteAt(address)

  def bufferManager(self) -> Optional[Qt3DRender.Render.BufferManager]:
    """
    Calls Qt's 'BufferManager
    *Qt3DRender::Render::NodeManagers::bufferManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-nodemanagers.html#bufferManager

    Returns
    -------

    Optional[Qt3DRender.Render.BufferManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  BufferManager *Qt3DRender::Render::NodeManagers::bufferManager() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12NodeManagers13bufferManagerEv',
    )
    return Qt3DRender.Render.BufferManager._cuteAt(address)

  def attributeManager(self) -> Optional[Qt3DRender.Render.AttributeManager]:
    """
    Calls Qt's 'AttributeManager
    *Qt3DRender::Render::NodeManagers::attributeManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-nodemanagers.html

    Returns
    -------

    Optional[Qt3DRender.Render.AttributeManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  AttributeManager *Qt3DRender::Render::NodeManagers::attributeManager()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12NodeManagers16attributeManagerEv',
    )
    return Qt3DRender.Render.AttributeManager._cuteAt(address)

  def geometryManager(self) -> Optional[Qt3DRender.Render.GeometryManager]:
    """
    Calls Qt's 'GeometryManager
    *Qt3DRender::Render::NodeManagers::geometryManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-nodemanagers.html

    Returns
    -------

    Optional[Qt3DRender.Render.GeometryManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  GeometryManager *Qt3DRender::Render::NodeManagers::geometryManager()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12NodeManagers15geometryManagerEv',
    )
    return Qt3DRender.Render.GeometryManager._cuteAt(address)

  def geometryRendererManager(
      self,
  ) -> Optional[Qt3DRender.Render.GeometryRendererManager]:
    """
    Calls Qt's 'GeometryRendererManager
    *Qt3DRender::Render::NodeManagers::geometryRendererManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-nodemanagers.html

    Returns
    -------

    Optional[Qt3DRender.Render.GeometryRendererManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  GeometryRendererManager
    #      *Qt3DRender::Render::NodeManagers::geometryRendererManager() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12NodeManagers23geometryRendererManag'
        'erEv',
    )
    return Qt3DRender.Render.GeometryRendererManager._cuteAt(address)

  def objectPickerManager(
      self,
  ) -> Optional[Qt3DRender.Render.ObjectPickerManager]:
    """
    Calls Qt's 'ObjectPickerManager
    *Qt3DRender::Render::NodeManagers::objectPickerManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-nodemanagers.html

    Returns
    -------

    Optional[Qt3DRender.Render.ObjectPickerManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ObjectPickerManager
    #      *Qt3DRender::Render::NodeManagers::objectPickerManager() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12NodeManagers19objectPickerManagerEv',
    )
    return Qt3DRender.Render.ObjectPickerManager._cuteAt(address)

  def rayCasterManager(self) -> Optional[Qt3DRender.Render.RayCasterManager]:
    """
    Calls Qt's 'RayCasterManager
    *Qt3DRender::Render::NodeManagers::rayCasterManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-nodemanagers.html

    Returns
    -------

    Optional[Qt3DRender.Render.RayCasterManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  RayCasterManager *Qt3DRender::Render::NodeManagers::rayCasterManager()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12NodeManagers16rayCasterManagerEv',
    )
    return Qt3DRender.Render.RayCasterManager._cuteAt(address)

  def lightManager(self) -> Optional[Qt3DRender.Render.LightManager]:
    """
    Calls Qt's 'LightManager
    *Qt3DRender::Render::NodeManagers::lightManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-nodemanagers.html#lightManager

    Returns
    -------

    Optional[Qt3DRender.Render.LightManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  LightManager *Qt3DRender::Render::NodeManagers::lightManager() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12NodeManagers12lightManagerEv',
    )
    return Qt3DRender.Render.LightManager._cuteAt(address)

  def environmentLightManager(
      self,
  ) -> Optional[Qt3DRender.Render.EnvironmentLightManager]:
    """
    Calls Qt's 'EnvironmentLightManager
    *Qt3DRender::Render::NodeManagers::environmentLightManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-nodemanagers.html

    Returns
    -------

    Optional[Qt3DRender.Render.EnvironmentLightManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  EnvironmentLightManager
    #      *Qt3DRender::Render::NodeManagers::environmentLightManager() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12NodeManagers23environmentLightManag'
        'erEv',
    )
    return Qt3DRender.Render.EnvironmentLightManager._cuteAt(address)

  def computeJobManager(
      self,
  ) -> Optional[Qt3DRender.Render.ComputeCommandManager]:
    """
    Calls Qt's 'ComputeCommandManager
    *Qt3DRender::Render::NodeManagers::computeJobManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-nodemanagers.html

    Returns
    -------

    Optional[Qt3DRender.Render.ComputeCommandManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ComputeCommandManager
    #      *Qt3DRender::Render::NodeManagers::computeJobManager() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12NodeManagers17computeJobManagerEv',
    )
    return Qt3DRender.Render.ComputeCommandManager._cuteAt(address)

  def renderStateManager(
      self,
  ) -> Optional[Qt3DRender.Render.RenderStateManager]:
    """
    Calls Qt's 'RenderStateManager
    *Qt3DRender::Render::NodeManagers::renderStateManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-nodemanagers.html

    Returns
    -------

    Optional[Qt3DRender.Render.RenderStateManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  RenderStateManager
    #      *Qt3DRender::Render::NodeManagers::renderStateManager() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12NodeManagers18renderStateManagerEv',
    )
    return Qt3DRender.Render.RenderStateManager._cuteAt(address)

  def armatureManager(self) -> Optional[Qt3DRender.Render.ArmatureManager]:
    """
    Calls Qt's 'ArmatureManager
    *Qt3DRender::Render::NodeManagers::armatureManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-nodemanagers.html

    Returns
    -------

    Optional[Qt3DRender.Render.ArmatureManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ArmatureManager *Qt3DRender::Render::NodeManagers::armatureManager()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12NodeManagers15armatureManagerEv',
    )
    return Qt3DRender.Render.ArmatureManager._cuteAt(address)

  def skeletonManager(self) -> Optional[Qt3DRender.Render.SkeletonManager]:
    """
    Calls Qt's 'SkeletonManager
    *Qt3DRender::Render::NodeManagers::skeletonManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-nodemanagers.html

    Returns
    -------

    Optional[Qt3DRender.Render.SkeletonManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  SkeletonManager *Qt3DRender::Render::NodeManagers::skeletonManager()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12NodeManagers15skeletonManagerEv',
    )
    return Qt3DRender.Render.SkeletonManager._cuteAt(address)

  def jointManager(self) -> Optional[Qt3DRender.Render.JointManager]:
    """
    Calls Qt's 'JointManager
    *Qt3DRender::Render::NodeManagers::jointManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-nodemanagers.html#jointManager

    Returns
    -------

    Optional[Qt3DRender.Render.JointManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  JointManager *Qt3DRender::Render::NodeManagers::jointManager() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12NodeManagers12jointManagerEv',
    )
    return Qt3DRender.Render.JointManager._cuteAt(address)

  def shaderImageManager(
      self,
  ) -> Optional[Qt3DRender.Render.ShaderImageManager]:
    """
    Calls Qt's 'ShaderImageManager
    *Qt3DRender::Render::NodeManagers::shaderImageManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-nodemanagers.html

    Returns
    -------

    Optional[Qt3DRender.Render.ShaderImageManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ShaderImageManager
    #      *Qt3DRender::Render::NodeManagers::shaderImageManager() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12NodeManagers18shaderImageManagerEv',
    )
    return Qt3DRender.Render.ShaderImageManager._cuteAt(address)

  def pickingProxyManager(
      self,
  ) -> Optional[Qt3DRender.Render.PickingProxyManager]:
    """
    Calls Qt's 'PickingProxyManager
    *Qt3DRender::Render::NodeManagers::pickingProxyManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-nodemanagers.html

    Returns
    -------

    Optional[Qt3DRender.Render.PickingProxyManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  PickingProxyManager
    #      *Qt3DRender::Render::NodeManagers::pickingProxyManager() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12NodeManagers19pickingProxyManagerEv',
    )
    return Qt3DRender.Render.PickingProxyManager._cuteAt(address)

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::Render::NodeManagers::NodeManagers()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-nodemanagers.html#NodeManagers
    """
    #  Qt3DRender::Render::NodeManagers::NodeManagers()
    self._noteCreation(NodeManagers, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render12NodeManagersC1Ev',
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

  @staticmethod
  def data(*__, **_) -> Never:
    """
    Qt's 'Qt3DRender::Render::NodeManagers::data': a template: a pattern and
    no single function.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.NodeManagers.data' has no cute function yet. "
        "Qt's 'Qt3DRender::Render::NodeManagers::data': a template: a "
        "pattern and no single function.")

  @staticmethod
  def lookupHandle(*__, **_) -> Never:
    """
    Qt's 'Qt3DRender::Render::NodeManagers::lookupHandle': a template: a
    pattern and no single function.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.NodeManagers.lookupHandle' has no cute function "
        "yet. Qt's 'Qt3DRender::Render::NodeManagers::lookupHandle': a "
        "template: a pattern and no single function.")

  @staticmethod
  def lookupResource(*__, **_) -> Never:
    """
    Qt's 'Qt3DRender::Render::NodeManagers::lookupResource': a template: a
    pattern and no single function.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.NodeManagers.lookupResource' has no cute "
        "function yet. Qt's "
        "'Qt3DRender::Render::NodeManagers::lookupResource': a template: a "
        "pattern and no single function.")

  @staticmethod
  def manager(*__, **_) -> Never:
    """
    Qt's 'Qt3DRender::Render::NodeManagers::manager': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.NodeManagers.manager' has no cute function yet. "
        "Qt's 'Qt3DRender::Render::NodeManagers::manager': a template: a "
        "pattern and no single function.")
