"""
QQmlProfilerDefinitions binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlprofilerdefinitions_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQmlProfilerDefinitions to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute


class QQmlProfilerDefinitions(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlProfilerDefinitions: a plain Python object
  standing in front of one C++ QQmlProfilerDefinitions.

  C++ hands a QQmlProfilerDefinitions around as a copy, so every C++
  QQmlProfilerDefinitions behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QQmlProfilerDefinitions yet. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlProfilerDefinitions::~QQmlProfilerDefinitions()': the
    destructor: Python removes its C++ QQmlProfilerDefinitions by it, and has
    no other use for it.

  What to expect
  --------------

  - The C++ QQmlProfilerDefinitions is created at the first use, not by
    'QQmlProfilerDefinitions(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlProfilerDefinitions back gives a copy the ritual
    made for Python, in a new cute QQmlProfilerDefinitions.
  """

  #  The enums Qt writes inside QQmlProfilerDefinitions, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class EventType(CuteNum):
    """
    The enum 'QQmlProfilerDefinitions::EventType' of Qt, with the 7 names Qt
    gives in it.
    """

    FramePaint = Kee[int](0)
    Mouse = Kee[int](1)
    Key = Kee[int](2)
    AnimationFrame = Kee[int](3)
    EndTrace = Kee[int](4)
    StartTrace = Kee[int](5)
    MaximumEventType = Kee[int](6)

  class InputEventType(CuteNum):
    """
    The enum 'QQmlProfilerDefinitions::InputEventType' of Qt, with the 10
    names Qt gives in it.
    """

    InputKeyPress = Kee[int](0)
    InputKeyRelease = Kee[int](1)
    InputKeyUnknown = Kee[int](2)
    InputMousePress = Kee[int](3)
    InputMouseRelease = Kee[int](4)
    InputMouseMove = Kee[int](5)
    InputMouseDoubleClick = Kee[int](6)
    InputMouseWheel = Kee[int](7)
    InputMouseUnknown = Kee[int](8)
    MaximumInputEventType = Kee[int](9)

  class Message(CuteNum):
    """
    The enum 'QQmlProfilerDefinitions::Message' of Qt, with the 12 names Qt
    gives in it.
    """

    Event = Kee[int](0)
    RangeStart = Kee[int](1)
    RangeData = Kee[int](2)
    RangeLocation = Kee[int](3)
    RangeEnd = Kee[int](4)
    Complete = Kee[int](5)
    PixmapCacheEvent = Kee[int](6)
    SceneGraphFrame = Kee[int](7)
    MemoryAllocation = Kee[int](8)
    DebugMessage = Kee[int](9)
    Quick3DFrame = Kee[int](10)
    MaximumMessage = Kee[int](11)

  class PixmapEventType(CuteNum):
    """
    The enum 'QQmlProfilerDefinitions::PixmapEventType' of Qt, with the 7
    names Qt gives in it.
    """

    PixmapSizeKnown = Kee[int](0)
    PixmapReferenceCountChanged = Kee[int](1)
    PixmapCacheCountChanged = Kee[int](2)
    PixmapLoadingStarted = Kee[int](3)
    PixmapLoadingFinished = Kee[int](4)
    PixmapLoadingError = Kee[int](5)
    MaximumPixmapEventType = Kee[int](6)

  class ProfileFeature(CuteNum):
    """
    The enum 'QQmlProfilerDefinitions::ProfileFeature' of Qt, with the 14
    names Qt gives in it.
    """

    ProfileJavaScript = Kee[int](0)
    ProfileMemory = Kee[int](1)
    ProfilePixmapCache = Kee[int](2)
    ProfileSceneGraph = Kee[int](3)
    ProfileAnimations = Kee[int](4)
    ProfilePainting = Kee[int](5)
    ProfileCompiling = Kee[int](6)
    ProfileCreating = Kee[int](7)
    ProfileBinding = Kee[int](8)
    ProfileHandlingSignal = Kee[int](9)
    ProfileInputEvents = Kee[int](10)
    ProfileDebugMessages = Kee[int](11)
    ProfileQuick3D = Kee[int](12)
    MaximumProfileFeature = Kee[int](13)

  class Quick3DFrameType(CuteNum):
    """
    The enum 'QQmlProfilerDefinitions::Quick3DFrameType' of Qt, with the 13
    names Qt gives in it.
    """

    Quick3DRenderFrame = Kee[int](0)
    Quick3DSynchronizeFrame = Kee[int](1)
    Quick3DPrepareFrame = Kee[int](2)
    Quick3DMeshLoad = Kee[int](3)
    Quick3DCustomMeshLoad = Kee[int](4)
    Quick3DTextureLoad = Kee[int](5)
    Quick3DGenerateShader = Kee[int](6)
    Quick3DLoadShader = Kee[int](7)
    Quick3DParticleUpdate = Kee[int](8)
    Quick3DRenderCall = Kee[int](9)
    Quick3DRenderPass = Kee[int](10)
    Quick3DEventData = Kee[int](11)
    MaximumQuick3DFrameType = Kee[int](12)

  class RangeType(CuteNum):
    """
    The enum 'QQmlProfilerDefinitions::RangeType' of Qt, with the 7 names Qt
    gives in it.
    """

    Painting = Kee[int](0)
    Compiling = Kee[int](1)
    Creating = Kee[int](2)
    Binding = Kee[int](3)
    HandlingSignal = Kee[int](4)
    Javascript = Kee[int](5)
    MaximumRangeType = Kee[int](6)

  class SceneGraphFrameType(CuteNum):
    """
    The enum 'QQmlProfilerDefinitions::SceneGraphFrameType' of Qt, with the
    13 names Qt gives in it.
    """

    SceneGraphRendererFrame = Kee[int](0)
    SceneGraphAdaptationLayerFrame = Kee[int](1)
    SceneGraphContextFrame = Kee[int](2)
    SceneGraphRenderLoopFrame = Kee[int](3)
    SceneGraphTexturePrepare = Kee[int](4)
    SceneGraphTextureDeletion = Kee[int](5)
    SceneGraphPolishAndSync = Kee[int](6)
    SceneGraphWindowsRenderShow = Kee[int](7)
    SceneGraphWindowsAnimations = Kee[int](8)
    SceneGraphPolishFrame = Kee[int](9)
    MaximumSceneGraphFrameType = Kee[int](10)
    NumRenderThreadFrameTypes = Kee[int](6)
    NumGUIThreadFrameTypes = Kee[int](4)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlProfilerDefinitions'

  #  Qt's '~QQmlProfilerDefinitions()'. Naming it makes this a value class:
  #  Python owns every C++ QQmlProfilerDefinitions behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QQmlProfilerDefinitionsD1Ev'

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
