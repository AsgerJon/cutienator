"""
Qt3DRender::Render::AbstractRenderer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/abstractrenderer_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::Render::AbstractRenderer to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..QtCore import QStringList
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QObject, QVariant
  from ..QtGui import QKeyEvent, QMouseEvent, QOpenGLContext, QRhi
  from ..QtGui import QRhiCommandBuffer, QRhiRenderTarget, QScreen
  from ..QtGui import QSurfaceFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QKeyEvent = WAIT['QKeyEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QObject = WAIT['QObject']
  QOpenGLContext = WAIT['QOpenGLContext']
  QRhi = WAIT['QRhi']
  QRhiCommandBuffer = WAIT['QRhiCommandBuffer']
  QRhiRenderTarget = WAIT['QRhiRenderTarget']
  QScreen = WAIT['QScreen']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class AbstractRenderer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DRender::Render::AbstractRenderer: a plain Python
  object standing in front of one C++ Qt3DRender::Render::AbstractRenderer.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::AbstractRenderer that has a
  ritual and that Python can call so far, 48 names in all: 'dumpInfo', 'api',
  'setRenderDriver', 'renderDriver', 'time', 'setTime', 'setJobsInLastFrame',
  'setAspect', 'setNodeManagers', 'setServices', 'setSurfaceExposed',
  'aspect', 'nodeManagers', 'services', 'initialize', 'shutdown',
  'releaseGraphicsResources', 'render', 'cleanGraphicsResources',
  'isRunning', 'markDirty', 'dirtyBits', 'shouldRender', 'skipNextFrame',
  'jobsDone', 'processMouseEvent', 'processKeyEvent', 'setSceneRoot',
  'sceneRoot', 'frameGraphRoot', 'frameAdvanceService', 'setSettings',
  'settings', 'executeCommand', 'setOpenGLContext', 'setRHIContext',
  'setDefaultRHIRenderTarget', 'setRHICommandBuffer', 'setScreen', 'screen',
  'setOffscreenSurfaceHelper', 'format', 'shareContext', 'contextInfo',
  'containsGeneratedShaderGraph', 'cachedGeneratedShaderGraph',
  'insertGeneratedShaderGraph', 'removeGeneratedShaderGraph'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::AbstractRenderer::~AbstractRenderer()': the
    destructor: Python never removes a C++
    Qt3DRender::Render::AbstractRenderer.
  - Qt's 'std::vector<Qt3DCore::QAspectJobPtr>
    Qt3DRender::Render::AbstractRenderer::preRenderingJobs()': gives a type
    Python has no way to take yet.
  - Qt's 'std::vector<Qt3DCore::QAspectJobPtr>
    Qt3DRender::Render::AbstractRenderer::renderBinJobs()': gives a type
    Python has no way to take yet.
  - Qt's 'bool
    Qt3DRender::Render::AbstractRenderer::accessOpenGLTexture(Qt3DCore::
    QNodeId nodeId, QOpenGLTexture **texture, QMutex **lock, bool readonly)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QSharedPointer<RenderBackendResourceAccessor>
    Qt3DRender::Render::AbstractRenderer::resourceAccessor() const': gives a
    type Python has no way to take yet.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::AbstractRenderer is created at the first use,
    not by 'Qt3DRender::Render::AbstractRenderer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::AbstractRenderer.
  - Each name of Qt's Qt3DRender::Render::AbstractRenderer that has no cute
    function yet, 'accessOpenGLTexture', 'preRenderingJobs', 'renderBinJobs',
    'resourceAccessor', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside Qt3DRender::Render::AbstractRenderer, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class BackendNodeDirtyFlag(CuteFlags):
    """
    The flags enum
    'Qt3DRender::Render::AbstractRenderer::BackendNodeDirtyFlag' of Qt, with
    the 16 names Qt gives in it. Qt names the type of its combinations
    'Qt3DRender::Render::AbstractRenderer::BackendNodeDirtySet'.
    """

    TransformDirty = 0x1
    MaterialDirty = 0x2
    GeometryDirty = 0x4
    ComputeDirty = 0x8
    ParameterDirty = 0x10
    FrameGraphDirty = 0x20
    EntityEnabledDirty = 0x40
    BuffersDirty = 0x80
    TexturesDirty = 0x100
    ShadersDirty = 0x200
    SkeletonDataDirty = 0x400
    JointDirty = 0x800
    LayersDirty = 0x1000
    TechniquesDirty = 0x2000
    LightsDirty = 0x8000
    AllDirty = 0xffffff

  BackendNodeDirtySet = BackendNodeDirtyFlag

  class RenderDriver(CuteNum):
    """
    The enum 'Qt3DRender::Render::AbstractRenderer::RenderDriver' of Qt, with
    the 2 names Qt gives in it.
    """

    Qt3D = Kee[int](0)
    Scene3D = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::AbstractRenderer'

  #  A C++ Qt3DRender::Render::AbstractRenderer Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_Render_AbstractRenderer'

  #  The functions Qt calls itself that Qt3DRender::Render::AbstractRenderer
  #  is the first to declare and that cannot be handed to Python yet, each as
  #  Qt declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'preRenderingJobs': (
          'std::vector<Qt3DCore::QAspectJobPtr> '
          'Qt3DRender::Render::AbstractRenderer::preRenderingJobs()',
      ),
      'renderBinJobs': (
          'std::vector<Qt3DCore::QAspectJobPtr> '
          'Qt3DRender::Render::AbstractRenderer::renderBinJobs()',
      ),
      'executeCommand': (
          'QVariant '
          'Qt3DRender::Render::AbstractRenderer::executeCommand(const '
          'QStringList &)',
      ),
      'accessOpenGLTexture': (
          'bool '
          'Qt3DRender::Render::AbstractRenderer::accessOpenGLTexture(Qt3DCo'
          're::QNodeId, QOpenGLTexture **, QMutex **, bool)',
      ),
      'resourceAccessor': (
          'QSharedPointer<RenderBackendResourceAccessor> '
          'Qt3DRender::Render::AbstractRenderer::resourceAccessor() const',
      ),
  }

  #  The functions Qt calls itself that Qt3DRender::Render::AbstractRenderer
  #  is the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'dumpInfo': (
          ('_ZNK10Qt3DRender6Render16AbstractRenderer8dumpInfoEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'api': (
          ('_ZNK10Qt3DRender6Render16AbstractRenderer3apiEv',
           ('int', 'enum', 'Qt3DRender:Qt3DRender.API'),
           ()),
      ),
      'setRenderDriver': (
          ('_ZN10Qt3DRender6Render16AbstractRenderer15setRenderDriverENS1_1'
           '2RenderDriverE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum',
                'Qt3DRender:Qt3DRender.Render.AbstractRenderer.RenderDriver'),
           )),
      ),
      'renderDriver': (
          ('_ZNK10Qt3DRender6Render16AbstractRenderer12renderDriverEv',
           ('int', 'enum',
            'Qt3DRender:Qt3DRender.Render.AbstractRenderer.RenderDriver'),
           ()),
      ),
      'time': (
          ('_ZNK10Qt3DRender6Render16AbstractRenderer4timeEv',
           ('long long', 'number', ''),
           ()),
      ),
      'setTime': (
          ('_ZN10Qt3DRender6Render16AbstractRenderer7setTimeEx',
           ('nothing', 'nothing', ''),
           (
               ('long long', 'number', ''),
           )),
      ),
      'setJobsInLastFrame': (
          ('_ZN10Qt3DRender6Render16AbstractRenderer18setJobsInLastFrameEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'setAspect': (
          ('_ZN10Qt3DRender6Render16AbstractRenderer9setAspectEPNS_13QRende'
           'rAspectE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'Qt3DRender:Qt3DRender.QRenderAspect'),
           )),
      ),
      'setNodeManagers': (
          ('_ZN10Qt3DRender6Render16AbstractRenderer15setNodeManagersEPNS0_'
           '12NodeManagersE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'Qt3DRender:Qt3DRender.Render.NodeManagers'),
           )),
      ),
      'setServices': (
          ('_ZN10Qt3DRender6Render16AbstractRenderer11setServicesEPN8Qt3DCo'
           're15QServiceLocatorE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'Qt3DCore:Qt3DCore.QServiceLocator'),
           )),
      ),
      'setSurfaceExposed': (
          ('_ZN10Qt3DRender6Render16AbstractRenderer17setSurfaceExposedEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'aspect': (
          ('_ZNK10Qt3DRender6Render16AbstractRenderer6aspectEv',
           ('address', 'address', 'Qt3DRender:Qt3DRender.QRenderAspect'),
           ()),
      ),
      'nodeManagers': (
          ('_ZNK10Qt3DRender6Render16AbstractRenderer12nodeManagersEv',
           ('address', 'address',
            'Qt3DRender:Qt3DRender.Render.NodeManagers'),
           ()),
      ),
      'services': (
          ('_ZNK10Qt3DRender6Render16AbstractRenderer8servicesEv',
           ('address', 'address', 'Qt3DCore:Qt3DCore.QServiceLocator'),
           ()),
      ),
      'initialize': (
          ('_ZN10Qt3DRender6Render16AbstractRenderer10initializeEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'shutdown': (
          ('_ZN10Qt3DRender6Render16AbstractRenderer8shutdownEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'releaseGraphicsResources': (
          ('_ZN10Qt3DRender6Render16AbstractRenderer24releaseGraphicsResour'
           'cesEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'render': (
          ('_ZN10Qt3DRender6Render16AbstractRenderer6renderEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'cleanGraphicsResources': (
          ('_ZN10Qt3DRender6Render16AbstractRenderer22cleanGraphicsResource'
           'sEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'isRunning': (
          ('_ZNK10Qt3DRender6Render16AbstractRenderer9isRunningEv',
           ('bool', 'number', ''),
           ()),
      ),
      'markDirty': (
          ('_ZN10Qt3DRender6Render16AbstractRenderer9markDirtyE6QFlagsINS1_'
           '20BackendNodeDirtyFlagEEPNS0_11BackendNodeE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'flags',
                'Qt3DRender:Qt3DRender.Render.AbstractRenderer.BackendNodeDirtyFlag'),
               ('address', 'address',
                'Qt3DRender:Qt3DRender.Render.BackendNode'),
           )),
      ),
      'dirtyBits': (
          ('_ZN10Qt3DRender6Render16AbstractRenderer9dirtyBitsEv',
           ('int', 'flags',
            'Qt3DRender:Qt3DRender.Render.AbstractRenderer.BackendNodeDirtyFlag'),
           ()),
      ),
      'shouldRender': (
          ('_ZNK10Qt3DRender6Render16AbstractRenderer12shouldRenderEv',
           ('bool', 'number', ''),
           ()),
      ),
      'skipNextFrame': (
          ('_ZN10Qt3DRender6Render16AbstractRenderer13skipNextFrameEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'jobsDone': (
          ('_ZN10Qt3DRender6Render16AbstractRenderer8jobsDoneEPN8Qt3DCore14'
           'QAspectManagerE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'Qt3DCore:Qt3DCore.QAspectManager'),
           )),
      ),
      'processMouseEvent': (
          ('_ZN10Qt3DRender6Render16AbstractRenderer17processMouseEventEP7Q'
           'ObjectP11QMouseEvent',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
               ('address', 'address', 'QtGui:QMouseEvent'),
           )),
      ),
      'processKeyEvent': (
          ('_ZN10Qt3DRender6Render16AbstractRenderer15processKeyEventEP7QOb'
           'jectP9QKeyEvent',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
               ('address', 'address', 'QtGui:QKeyEvent'),
           )),
      ),
      'setSceneRoot': (
          ('_ZN10Qt3DRender6Render16AbstractRenderer12setSceneRootEPNS0_6En'
           'tityE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'Qt3DRender:Qt3DRender.Render.Entity'),
           )),
      ),
      'sceneRoot': (
          ('_ZNK10Qt3DRender6Render16AbstractRenderer9sceneRootEv',
           ('address', 'address', 'Qt3DRender:Qt3DRender.Render.Entity'),
           ()),
      ),
      'frameGraphRoot': (
          ('_ZNK10Qt3DRender6Render16AbstractRenderer14frameGraphRootEv',
           ('address', 'address',
            'Qt3DRender:Qt3DRender.Render.FrameGraphNode'),
           ()),
      ),
      'frameAdvanceService': (
          ('_ZNK10Qt3DRender6Render16AbstractRenderer19frameAdvanceServiceE'
           'v',
           ('address', 'address',
            'Qt3DCore:Qt3DCore.QAbstractFrameAdvanceService'),
           ()),
      ),
      'setSettings': (
          ('_ZN10Qt3DRender6Render16AbstractRenderer11setSettingsEPNS0_14Re'
           'nderSettingsE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'Qt3DRender:Qt3DRender.Render.RenderSettings'),
           )),
      ),
      'settings': (
          ('_ZNK10Qt3DRender6Render16AbstractRenderer8settingsEv',
           ('address', 'address',
            'Qt3DRender:Qt3DRender.Render.RenderSettings'),
           ()),
      ),
      'setOpenGLContext': (
          ('_ZN10Qt3DRender6Render16AbstractRenderer16setOpenGLContextEP14Q'
           'OpenGLContext',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QOpenGLContext'),
           )),
      ),
      'setRHIContext': (
          ('_ZN10Qt3DRender6Render16AbstractRenderer13setRHIContextEP4QRhi',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QRhi'),
           )),
      ),
      'setDefaultRHIRenderTarget': (
          ('_ZN10Qt3DRender6Render16AbstractRenderer25setDefaultRHIRenderTa'
           'rgetEP16QRhiRenderTarget',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QRhiRenderTarget'),
           )),
      ),
      'setRHICommandBuffer': (
          ('_ZN10Qt3DRender6Render16AbstractRenderer19setRHICommandBufferEP'
           '17QRhiCommandBuffer',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QRhiCommandBuffer'),
           )),
      ),
      'setScreen': (
          ('_ZN10Qt3DRender6Render16AbstractRenderer9setScreenEP7QScreen',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QScreen'),
           )),
      ),
      'screen': (
          ('_ZNK10Qt3DRender6Render16AbstractRenderer6screenEv',
           ('address', 'address', 'QtGui:QScreen'),
           ()),
      ),
      'setOffscreenSurfaceHelper': (
          ('_ZN10Qt3DRender6Render16AbstractRenderer25setOffscreenSurfaceHe'
           'lperEPNS0_22OffscreenSurfaceHelperE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'Qt3DRender:Qt3DRender.Render.OffscreenSurfaceHelper'),
           )),
      ),
      'format': (
          ('_ZN10Qt3DRender6Render16AbstractRenderer6formatEv',
           ('address', 'value', 'QtGui:QSurfaceFormat'),
           ()),
      ),
      'shareContext': (
          ('_ZNK10Qt3DRender6Render16AbstractRenderer12shareContextEv',
           ('address', 'address', 'QtGui:QOpenGLContext'),
           ()),
      ),
      'contextInfo': (
          ('_ZNK10Qt3DRender6Render16AbstractRenderer11contextInfoEv',
           ('address', 'address',
            'Qt3DRender:Qt3DRender.GraphicsApiFilterData'),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def api(self) -> Qt3DRender.API:
    """
    Calls Qt's 'API Qt3DRender::Render::AbstractRenderer::api() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html#api

    Returns
    -------

    Qt3DRender.API
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt3DRender.API(number)'
      gives.
    """
    #  API Qt3DRender::Render::AbstractRenderer::api() const
    return Qt3DRender.API(self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render16AbstractRenderer3apiEv',
    ))

  def renderDriver(self) -> RenderDriver:
    """
    Calls Qt's 'RenderDriver
    Qt3DRender::Render::AbstractRenderer::renderDriver() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html

    Returns
    -------

    RenderDriver
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'RenderDriver(number)'
      gives.
    """
    #  RenderDriver Qt3DRender::Render::AbstractRenderer::renderDriver()
    #      const
    return AbstractRenderer.RenderDriver(self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render16AbstractRenderer12renderDriverEv',
    ))

  def time(self) -> int:
    """
    Calls Qt's 'qint64 Qt3DRender::Render::AbstractRenderer::time() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html#time
    """
    #  qint64 Qt3DRender::Render::AbstractRenderer::time() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render16AbstractRenderer4timeEv',
    )

  def aspect(self) -> Optional[Qt3DRender.QRenderAspect]:
    """
    Calls Qt's 'QRenderAspect *Qt3DRender::Render::AbstractRenderer::aspect()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html#aspect

    Returns
    -------

    Optional[Qt3DRender.QRenderAspect]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRenderAspect *Qt3DRender::Render::AbstractRenderer::aspect() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render16AbstractRenderer6aspectEv',
    )
    return Qt3DRender.QRenderAspect._cuteAt(address)

  def nodeManagers(self) -> Optional[Qt3DRender.Render.NodeManagers]:
    """
    Calls Qt's 'NodeManagers
    *Qt3DRender::Render::AbstractRenderer::nodeManagers() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html

    Returns
    -------

    Optional[Qt3DRender.Render.NodeManagers]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  NodeManagers *Qt3DRender::Render::AbstractRenderer::nodeManagers()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render16AbstractRenderer12nodeManagersEv',
    )
    return Qt3DRender.Render.NodeManagers._cuteAt(address)

  def services(self) -> Optional[Qt3DCore.QServiceLocator]:
    """
    Calls Qt's 'Qt3DCore::QServiceLocator
    *Qt3DRender::Render::AbstractRenderer::services() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html#services

    Returns
    -------

    Optional[Qt3DCore.QServiceLocator]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QServiceLocator
    #      *Qt3DRender::Render::AbstractRenderer::services() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render16AbstractRenderer8servicesEv',
    )
    return Qt3DCore.QServiceLocator._cuteAt(address)

  def isRunning(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Render::AbstractRenderer::isRunning()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html#isRunning
    """
    #  bool Qt3DRender::Render::AbstractRenderer::isRunning() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render16AbstractRenderer9isRunningEv',
    )

  def shouldRender(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Render::AbstractRenderer::shouldRender()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html
    """
    #  bool Qt3DRender::Render::AbstractRenderer::shouldRender() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render16AbstractRenderer12shouldRenderEv',
    )

  def sceneRoot(self) -> Optional[Qt3DRender.Render.Entity]:
    """
    Calls Qt's 'Entity *Qt3DRender::Render::AbstractRenderer::sceneRoot()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html#sceneRoot

    Returns
    -------

    Optional[Qt3DRender.Render.Entity]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Entity *Qt3DRender::Render::AbstractRenderer::sceneRoot() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render16AbstractRenderer9sceneRootEv',
    )
    return Qt3DRender.Render.Entity._cuteAt(address)

  def frameGraphRoot(self) -> Optional[Qt3DRender.Render.FrameGraphNode]:
    """
    Calls Qt's 'FrameGraphNode
    *Qt3DRender::Render::AbstractRenderer::frameGraphRoot() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html

    Returns
    -------

    Optional[Qt3DRender.Render.FrameGraphNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FrameGraphNode *Qt3DRender::Render::AbstractRenderer::frameGraphRoot()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render16AbstractRenderer14frameGraphRootEv',
    )
    return Qt3DRender.Render.FrameGraphNode._cuteAt(address)

  def frameAdvanceService(
      self,
  ) -> Optional[Qt3DCore.QAbstractFrameAdvanceService]:
    """
    Calls Qt's 'Qt3DCore::QAbstractFrameAdvanceService
    *Qt3DRender::Render::AbstractRenderer::frameAdvanceService() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html

    Returns
    -------

    Optional[Qt3DCore.QAbstractFrameAdvanceService]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QAbstractFrameAdvanceService
    #      *Qt3DRender::Render::AbstractRenderer::frameAdvanceService() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render16AbstractRenderer19frameAdvanceServi'
        'ceEv',
    )
    return Qt3DCore.QAbstractFrameAdvanceService._cuteAt(address)

  def settings(self) -> Optional[Qt3DRender.Render.RenderSettings]:
    """
    Calls Qt's 'RenderSettings
    *Qt3DRender::Render::AbstractRenderer::settings() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html#settings

    Returns
    -------

    Optional[Qt3DRender.Render.RenderSettings]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  RenderSettings *Qt3DRender::Render::AbstractRenderer::settings() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render16AbstractRenderer8settingsEv',
    )
    return Qt3DRender.Render.RenderSettings._cuteAt(address)

  def screen(self) -> Optional[QScreen]:
    """
    Calls Qt's 'QScreen *Qt3DRender::Render::AbstractRenderer::screen()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html#screen

    Returns
    -------

    Optional[QScreen]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScreen *Qt3DRender::Render::AbstractRenderer::screen() const
    ritual = 'ritual_ZNK10Qt3DRender6Render16AbstractRenderer6screenEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10Qt3DRender6Render16AbstractRenderer6screenEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QScreen
    return QScreen._cuteAt(address)

  def shareContext(self) -> Optional[QOpenGLContext]:
    """
    Calls Qt's 'QOpenGLContext
    *Qt3DRender::Render::AbstractRenderer::shareContext() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html

    Returns
    -------

    Optional[QOpenGLContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLContext *Qt3DRender::Render::AbstractRenderer::shareContext()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render16AbstractRenderer12shareContextEv',
    )
    from ..QtGui import QOpenGLContext
    return QOpenGLContext._cuteAt(address)

  def contextInfo(self) -> Optional[Qt3DRender.GraphicsApiFilterData]:
    """
    Calls Qt's 'const GraphicsApiFilterData
    *Qt3DRender::Render::AbstractRenderer::contextInfo() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html

    Returns
    -------

    Optional[Qt3DRender.GraphicsApiFilterData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const GraphicsApiFilterData
    #      *Qt3DRender::Render::AbstractRenderer::contextInfo() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render16AbstractRenderer11contextInfoEv',
    )
    return Qt3DRender.GraphicsApiFilterData._cuteAt(address)

  @overload(QByteArray)
  def containsGeneratedShaderGraph(self, key: QByteArray) -> bool:
    """
    Calls Qt's 'bool
    Qt3DRender::Render::AbstractRenderer::containsGeneratedShaderGraph(const
    QByteArray &key) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html

    Parameters
    ----------

    key : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool Qt3DRender::Render::AbstractRenderer::
    #      containsGeneratedShaderGraph(const QByteArray &key) const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render16AbstractRenderer28containsGenerated'
        'ShaderGraphERK10QByteArray',
        self._valueOf(key),
    )

  @overload(QByteArray)
  def cachedGeneratedShaderGraph(self, key: QByteArray) -> QByteArray:
    """
    Calls Qt's 'QByteArray
    Qt3DRender::Render::AbstractRenderer::cachedGeneratedShaderGraph(const
    QByteArray &key) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html

    Parameters
    ----------

    key : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray
    #      Qt3DRender::Render::AbstractRenderer::cachedGeneratedShaderGraph(
    #      const QByteArray &key) const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render16AbstractRenderer26cachedGeneratedSh'
        'aderGraphERK10QByteArray',
        self._valueOf(key),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(RenderDriver)
  def setRenderDriver(self, driver: RenderDriver) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::AbstractRenderer::setRenderDriver(RenderDriver
    driver)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html

    Parameters
    ----------

    driver : RenderDriver
      Passed on as its number.
    """
    #  void
    #      Qt3DRender::Render::AbstractRenderer::setRenderDriver(RenderDriver
    #      driver)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render16AbstractRenderer15setRenderDriverENS'
        '1_12RenderDriverE',
        driver.value,
    )

  @overload(int)
  def setTime(self, time: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::AbstractRenderer::setTime(qint64
    time)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html#setTime

    Parameters
    ----------

    time : int
      Passed on as it is.
    """
    #  void Qt3DRender::Render::AbstractRenderer::setTime(qint64 time)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render16AbstractRenderer7setTimeEx', time,
    )

  @overload(int)
  def setJobsInLastFrame(self, jobsInLastFrame: int) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::AbstractRenderer::setJobsInLastFrame(int
    jobsInLastFrame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html

    Parameters
    ----------

    jobsInLastFrame : int
      Passed on as it is.
    """
    #  void Qt3DRender::Render::AbstractRenderer::setJobsInLastFrame(int
    #      jobsInLastFrame)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render16AbstractRenderer18setJobsInLastFrame'
        'Ei',
        jobsInLastFrame,
    )

  @overload(WAIT['Qt3DRender.QRenderAspect'])
  @overload(NoneType)
  def setAspect(self, aspect: Optional[Qt3DRender.QRenderAspect]) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::AbstractRenderer::setAspect(QRenderAspect *aspect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html#setAspect

    Parameters
    ----------

    aspect : Optional[Qt3DRender.QRenderAspect]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::AbstractRenderer::setAspect(QRenderAspect
    #      *aspect)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render16AbstractRenderer9setAspectEPNS_13QRe'
        'nderAspectE',
        self._addressOf(aspect),
    )

  @overload(WAIT['Qt3DRender.Render.NodeManagers'])
  @overload(NoneType)
  def setNodeManagers(
      self,
      managers: Optional[Qt3DRender.Render.NodeManagers],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::AbstractRenderer::setNodeManagers(NodeManagers
    *managers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html

    Parameters
    ----------

    managers : Optional[Qt3DRender.Render.NodeManagers]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      Qt3DRender::Render::AbstractRenderer::setNodeManagers(NodeManagers
    #      *managers)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render16AbstractRenderer15setNodeManagersEPN'
        'S0_12NodeManagersE',
        self._addressOf(managers),
    )

  @overload(WAIT['Qt3DCore.QServiceLocator'])
  @overload(NoneType)
  def setServices(
      self,
      services: Optional[Qt3DCore.QServiceLocator],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::AbstractRenderer::setServices(Qt3DCore::
    QServiceLocator *services)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html

    Parameters
    ----------

    services : Optional[Qt3DCore.QServiceLocator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::AbstractRenderer::setServices(Qt3DCore::
    #      QServiceLocator *services)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render16AbstractRenderer11setServicesEPN8Qt3'
        'DCore15QServiceLocatorE',
        self._addressOf(services),
    )

  @overload(bool)
  def setSurfaceExposed(self, exposed: bool) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::AbstractRenderer::setSurfaceExposed(bool exposed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html

    Parameters
    ----------

    exposed : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Render::AbstractRenderer::setSurfaceExposed(bool
    #      exposed)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render16AbstractRenderer17setSurfaceExposedE'
        'b',
        exposed,
    )

  @overload(WAIT['Qt3DRender.Render.Entity'])
  @overload(NoneType)
  def setSceneRoot(self, root: Optional[Qt3DRender.Render.Entity]) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::AbstractRenderer::setSceneRoot(Entity *root)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html

    Parameters
    ----------

    root : Optional[Qt3DRender.Render.Entity]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::AbstractRenderer::setSceneRoot(Entity *root)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render16AbstractRenderer12setSceneRootEPNS0_'
        '6EntityE',
        self._addressOf(root),
    )

  @overload(WAIT['Qt3DRender.Render.RenderSettings'])
  @overload(NoneType)
  def setSettings(
      self,
      settings: Optional[Qt3DRender.Render.RenderSettings],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::AbstractRenderer::setSettings(RenderSettings
    *settings)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html

    Parameters
    ----------

    settings : Optional[Qt3DRender.Render.RenderSettings]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::AbstractRenderer::setSettings(RenderSettings
    #      *settings)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render16AbstractRenderer11setSettingsEPNS0_1'
        '4RenderSettingsE',
        self._addressOf(settings),
    )

  @overload(QOpenGLContext)
  @overload(NoneType)
  def setOpenGLContext(self, ctx: Optional[QOpenGLContext]) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::AbstractRenderer::setOpenGLContext(QOpenGLContext
    *ctx)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html

    Parameters
    ----------

    ctx : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::AbstractRenderer::setOpenGLContext(
    #      QOpenGLContext *ctx)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render16AbstractRenderer16setOpenGLContextEP'
        '14QOpenGLContext',
        self._addressOf(ctx),
    )

  @overload(QRhi)
  @overload(NoneType)
  def setRHIContext(self, ctx: Optional[QRhi]) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::AbstractRenderer::setRHIContext(QRhi
    *ctx)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html

    Parameters
    ----------

    ctx : Optional[QRhi]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::AbstractRenderer::setRHIContext(QRhi *ctx)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render16AbstractRenderer13setRHIContextEP4QR'
        'hi',
        self._addressOf(ctx),
    )

  @overload(QRhiRenderTarget)
  @overload(NoneType)
  def setDefaultRHIRenderTarget(
      self,
      defaultTarget: Optional[QRhiRenderTarget],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::AbstractRenderer::setDefaultRHIRenderTarget(
    QRhiRenderTarget *defaultTarget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html

    Parameters
    ----------

    defaultTarget : Optional[QRhiRenderTarget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::AbstractRenderer::setDefaultRHIRenderTarget(
    #      QRhiRenderTarget *defaultTarget)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render16AbstractRenderer25setDefaultRHIRende'
        'rTargetEP16QRhiRenderTarget',
        self._addressOf(defaultTarget),
    )

  @overload(QRhiCommandBuffer)
  @overload(NoneType)
  def setRHICommandBuffer(
      self,
      commandBuffer: Optional[QRhiCommandBuffer],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::AbstractRenderer::setRHICommandBuffer(
    QRhiCommandBuffer *commandBuffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html

    Parameters
    ----------

    commandBuffer : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::AbstractRenderer::setRHICommandBuffer(
    #      QRhiCommandBuffer *commandBuffer)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render16AbstractRenderer19setRHICommandBuffe'
        'rEP17QRhiCommandBuffer',
        self._addressOf(commandBuffer),
    )

  @overload(QScreen)
  @overload(NoneType)
  def setScreen(self, a0: Optional[QScreen]) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::AbstractRenderer::setScreen(QScreen
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html#setScreen

    Parameters
    ----------

    a0 : Optional[QScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::AbstractRenderer::setScreen(QScreen *a0)
    ritual = (
        'ritual_ZN10Qt3DRender6Render16AbstractRenderer9setScreenEP7QScreen')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render16AbstractRenderer9setScreenEP7Q'
          'Screen')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['Qt3DRender.Render.OffscreenSurfaceHelper'])
  @overload(NoneType)
  def setOffscreenSurfaceHelper(
      self,
      helper: Optional[Qt3DRender.Render.OffscreenSurfaceHelper],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::AbstractRenderer::setOffscreenSurfaceHelper(
    OffscreenSurfaceHelper *helper)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html

    Parameters
    ----------

    helper : Optional[Qt3DRender.Render.OffscreenSurfaceHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::AbstractRenderer::setOffscreenSurfaceHelper(
    #      OffscreenSurfaceHelper *helper)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render16AbstractRenderer25setOffscreenSurfac'
        'eHelperEPNS0_22OffscreenSurfaceHelperE',
        self._addressOf(helper),
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

  def dumpInfo(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::AbstractRenderer::dumpInfo() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html#dumpInfo
    """
    #  void Qt3DRender::Render::AbstractRenderer::dumpInfo() const
    self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render16AbstractRenderer8dumpInfoEv',
    )

  def initialize(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::AbstractRenderer::initialize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html#initialize
    """
    #  void Qt3DRender::Render::AbstractRenderer::initialize()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render16AbstractRenderer10initializeEv',
    )

  def shutdown(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::AbstractRenderer::shutdown()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html#shutdown
    """
    #  void Qt3DRender::Render::AbstractRenderer::shutdown()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render16AbstractRenderer8shutdownEv',
    )

  def releaseGraphicsResources(self) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::AbstractRenderer::releaseGraphicsResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html
    """
    #  void Qt3DRender::Render::AbstractRenderer::releaseGraphicsResources()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render16AbstractRenderer24releaseGraphicsRes'
        'ourcesEv',
    )

  @overload(bool)
  def render(self, swapBuffers: bool) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::AbstractRenderer::render(bool
    swapBuffers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html#render

    Parameters
    ----------

    swapBuffers : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Render::AbstractRenderer::render(bool swapBuffers)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render16AbstractRenderer6renderEb',
        swapBuffers,
    )

  def cleanGraphicsResources(self) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::AbstractRenderer::cleanGraphicsResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html
    """
    #  void Qt3DRender::Render::AbstractRenderer::cleanGraphicsResources()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render16AbstractRenderer22cleanGraphicsResou'
        'rcesEv',
    )

  @overload(BackendNodeDirtySet, WAIT['Qt3DRender.Render.BackendNode'])
  @overload(BackendNodeDirtySet, NoneType)
  def markDirty(
      self,
      changes: BackendNodeDirtySet,
      node: Optional[Qt3DRender.Render.BackendNode],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::AbstractRenderer::markDirty(BackendNodeDirtySet
    changes, BackendNode *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html#markDirty

    Parameters
    ----------

    changes : BackendNodeDirtySet
      Passed on as its number.

    node : Optional[Qt3DRender.Render.BackendNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::AbstractRenderer::markDirty(
    #      BackendNodeDirtySet changes, BackendNode *node)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render16AbstractRenderer9markDirtyE6QFlagsIN'
        'S1_20BackendNodeDirtyFlagEEPNS0_11BackendNodeE',
        changes.value, self._addressOf(node),
    )

  def dirtyBits(self) -> BackendNodeDirtySet:
    """
    Calls Qt's 'BackendNodeDirtySet
    Qt3DRender::Render::AbstractRenderer::dirtyBits()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html#dirtyBits

    Returns
    -------

    BackendNodeDirtySet
      The value standing for the combination Qt gave back.
    """
    #  BackendNodeDirtySet Qt3DRender::Render::AbstractRenderer::dirtyBits()
    return AbstractRenderer.BackendNodeDirtySet(self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render16AbstractRenderer9dirtyBitsEv',
    ))

  def skipNextFrame(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::AbstractRenderer::skipNextFrame()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html
    """
    #  void Qt3DRender::Render::AbstractRenderer::skipNextFrame()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render16AbstractRenderer13skipNextFrameEv',
    )

  @overload(WAIT['Qt3DCore.QAspectManager'])
  @overload(NoneType)
  def jobsDone(self, manager: Optional[Qt3DCore.QAspectManager]) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::AbstractRenderer::jobsDone(Qt3DCore::QAspectManager
    *manager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html#jobsDone

    Parameters
    ----------

    manager : Optional[Qt3DCore.QAspectManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::AbstractRenderer::jobsDone(Qt3DCore::
    #      QAspectManager *manager)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render16AbstractRenderer8jobsDoneEPN8Qt3DCor'
        'e14QAspectManagerE',
        self._addressOf(manager),
    )

  @overload(QObject, QMouseEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QMouseEvent)
  @overload(NoneType, NoneType)
  def processMouseEvent(
      self,
      object: Optional[QObject],
      event: Optional[QMouseEvent],
  ) -> bool:
    """
    Calls Qt's 'bool
    Qt3DRender::Render::AbstractRenderer::processMouseEvent(QObject *object,
    QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool Qt3DRender::Render::AbstractRenderer::processMouseEvent(QObject
    #      *object, QMouseEvent *event)
    return self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render16AbstractRenderer17processMouseEventE'
        'P7QObjectP11QMouseEvent',
        self._addressOf(object, 'QObject'), self._addressOf(event),
    )

  @overload(QObject, QKeyEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QKeyEvent)
  @overload(NoneType, NoneType)
  def processKeyEvent(
      self,
      object: Optional[QObject],
      event: Optional[QKeyEvent],
  ) -> bool:
    """
    Calls Qt's 'bool
    Qt3DRender::Render::AbstractRenderer::processKeyEvent(QObject *object,
    QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool Qt3DRender::Render::AbstractRenderer::processKeyEvent(QObject
    #      *object, QKeyEvent *event)
    return self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render16AbstractRenderer15processKeyEventEP7'
        'QObjectP9QKeyEvent',
        self._addressOf(object, 'QObject'), self._addressOf(event),
    )

  @overload(QStringList)
  def executeCommand(self, args: QStringList) -> QVariant:
    """
    Calls Qt's 'QVariant
    Qt3DRender::Render::AbstractRenderer::executeCommand(const QStringList
    &args)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html

    Parameters
    ----------

    args : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant Qt3DRender::Render::AbstractRenderer::executeCommand(const
    #      QStringList &args)
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render16AbstractRenderer14executeCommandERK5'
        'QListI7QStringE',
        self._valueOf(args),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def format(self) -> QSurfaceFormat:
    """
    Calls Qt's 'QSurfaceFormat
    Qt3DRender::Render::AbstractRenderer::format()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html#format

    Returns
    -------

    QSurfaceFormat
      A new cute QSurfaceFormat around the copy Qt gave back. Python owns it.
    """
    #  QSurfaceFormat Qt3DRender::Render::AbstractRenderer::format()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render16AbstractRenderer6formatEv',
    )
    from ..QtGui import QSurfaceFormat
    return QSurfaceFormat._cuteOwning(address)

  @overload(QByteArray, QByteArray)
  def insertGeneratedShaderGraph(
      self,
      key: QByteArray,
      shaderCode: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::AbstractRenderer::insertGeneratedShaderGraph(const
    QByteArray &key, const QByteArray shaderCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html

    Parameters
    ----------

    key : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    shaderCode : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void Qt3DRender::Render::AbstractRenderer::insertGeneratedShaderGraph(
    #      const QByteArray &key, const QByteArray shaderCode)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render16AbstractRenderer26insertGeneratedSha'
        'derGraphERK10QByteArrayS2_',
        self._valueOf(key), self._valueOf(shaderCode),
    )

  @overload(QByteArray)
  def removeGeneratedShaderGraph(self, key: QByteArray) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::AbstractRenderer::removeGeneratedShaderGraph(const
    QByteArray &key)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractrenderer.html

    Parameters
    ----------

    key : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void Qt3DRender::Render::AbstractRenderer::removeGeneratedShaderGraph(
    #      const QByteArray &key)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render16AbstractRenderer26removeGeneratedSha'
        'derGraphERK10QByteArray',
        self._valueOf(key),
    )

  @staticmethod
  def accessOpenGLTexture(*__, **_) -> Never:
    """
    Qt's 'bool
    Qt3DRender::Render::AbstractRenderer::accessOpenGLTexture(Qt3DCore::
    QNodeId nodeId, QOpenGLTexture **texture, QMutex **lock, bool readonly)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.AbstractRenderer.accessOpenGLTexture' has no "
        "cute function yet. Qt's 'bool "
        "Qt3DRender::Render::AbstractRenderer::accessOpenGLTexture(Qt3DCore:"
        ":QNodeId nodeId, QOpenGLTexture **texture, QMutex **lock, bool "
        "readonly)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def preRenderingJobs(*__, **_) -> Never:
    """
    Qt's 'std::vector<Qt3DCore::QAspectJobPtr>
    Qt3DRender::Render::AbstractRenderer::preRenderingJobs()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.AbstractRenderer.preRenderingJobs' has no cute "
        "function yet. Qt's 'std::vector<Qt3DCore::QAspectJobPtr> "
        "Qt3DRender::Render::AbstractRenderer::preRenderingJobs()': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def renderBinJobs(*__, **_) -> Never:
    """
    Qt's 'std::vector<Qt3DCore::QAspectJobPtr>
    Qt3DRender::Render::AbstractRenderer::renderBinJobs()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.AbstractRenderer.renderBinJobs' has no cute "
        "function yet. Qt's 'std::vector<Qt3DCore::QAspectJobPtr> "
        "Qt3DRender::Render::AbstractRenderer::renderBinJobs()': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def resourceAccessor(*__, **_) -> Never:
    """
    Qt's 'QSharedPointer<RenderBackendResourceAccessor>
    Qt3DRender::Render::AbstractRenderer::resourceAccessor() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.AbstractRenderer.resourceAccessor' has no cute "
        "function yet. Qt's 'QSharedPointer<RenderBackendResourceAccessor> "
        "Qt3DRender::Render::AbstractRenderer::resourceAccessor() const': "
        "gives a type Python has no way to take yet.")
