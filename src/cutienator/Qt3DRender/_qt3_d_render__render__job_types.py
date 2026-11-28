"""
JobTypes stands for the namespace 'Qt3DRender::Render::JobTypes' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class JobTypes:
  """
  The namespace 'Qt3DRender::Render::JobTypes' of Qt, which holds no objects.
  It holds the 1 enums Qt writes in it, each under its name, and the 0 names
  Qt has for the combinations of a flags enum, each holding the class of that
  enum. It is never made into an object.
  """

  class JobType(CuteNum):
    """
    The enum 'Qt3DRender::Render::JobTypes::JobType' of Qt, with the 50 names
    Qt gives in it.
    """

    LoadBuffer = Kee[int](1)
    FrameCleanup = Kee[int](2)
    UpdateShaderDataTransform = Kee[int](3)
    CalcBoundingVolume = Kee[int](4)
    CalcTriangleVolume = Kee[int](5)
    LoadGeometry = Kee[int](6)
    LoadScene = Kee[int](7)
    LoadTextureData = Kee[int](8)
    PickBoundingVolume = Kee[int](9)
    RayCasting = Kee[int](10)
    RenderView = Kee[int](11)
    UpdateTransform = Kee[int](12)
    UpdateTreeEnabled = Kee[int](13)
    ExpandBoundingVolume = Kee[int](14)
    FrameSubmissionPart1 = Kee[int](15)
    LayerFiltering = Kee[int](16)
    EntityComponentTypeFiltering = Kee[int](17)
    MaterialParameterGathering = Kee[int](18)
    RenderCommandUpdater = Kee[int](19)
    GenericLambda = Kee[int](20)
    FrustumCulling = Kee[int](21)
    LightGathering = Kee[int](22)
    UpdateWorldBoundingVolume = Kee[int](23)
    FrameSubmissionPart2 = Kee[int](24)
    DirtyBufferGathering = Kee[int](25)
    DirtyVaoGathering = Kee[int](26)
    DirtyTextureGathering = Kee[int](27)
    DirtyShaderGathering = Kee[int](28)
    SendRenderCapture = Kee[int](29)
    SendBufferCapture = Kee[int](30)
    SyncRenderViewPreCommandUpdate = Kee[int](31)
    SyncRenderViewInitialization = Kee[int](32)
    SyncRenderViewPostCommandUpdate = Kee[int](33)
    SyncFrustumCulling = Kee[int](34)
    ClearBufferDrawIndex = Kee[int](35)
    UpdateMeshTriangleList = Kee[int](36)
    FilterCompatibleTechniques = Kee[int](37)
    UpdateLevelOfDetail = Kee[int](38)
    SyncLoadingJobs = Kee[int](39)
    LoadSkeleton = Kee[int](40)
    UpdateSkinningPalette = Kee[int](41)
    ProximityFiltering = Kee[int](42)
    SyncFilterEntityByLayer = Kee[int](43)
    SyncMaterialGatherer = Kee[int](44)
    UpdateLayerEntity = Kee[int](45)
    SendTextureChangesToFrontend = Kee[int](46)
    SendSetFenceHandlesToFrontend = Kee[int](47)
    SendDisablesToFrontend = Kee[int](48)
    RenderViewCommandBuilder = Kee[int](49)
    SyncRenderViewPreCommandBuilding = Kee[int](50)
