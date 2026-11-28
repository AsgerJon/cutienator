"""
QSGRendererInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/qsgrendererinterface.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QSGRendererInterface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSGRendererInterface: a plain Python object standing
  in front of one C++ QSGRendererInterface.

  What exists
  -----------

  Every function of Qt's QSGRendererInterface that has a ritual and that
  Python can call so far, 5 names in all: 'graphicsApi', 'shaderType',
  'shaderCompilationType', 'shaderSourceType', 'isApiRhiBased'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGRendererInterface::~QSGRendererInterface()': the destructor:
    Python never removes a C++ QSGRendererInterface.
  - Qt's 'void *QSGRendererInterface::getResource(QQuickWindow *window,
    Resource resource) const': gives 'void', which has no cute class yet.
  - Qt's 'void *QSGRendererInterface::getResource(QQuickWindow *window, const
    char *resource) const': gives 'void', which has no cute class yet.

  What to expect
  --------------

  - The C++ QSGRendererInterface is created at the first use, not by
    'QSGRendererInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGRendererInterface.
  - Each name of Qt's QSGRendererInterface that has no cute function yet,
    'getResource', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QSGRendererInterface, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class GraphicsApi(CuteNum):
    """
    The enum 'QSGRendererInterface::GraphicsApi' of Qt, with the 14 names Qt
    gives in it.
    """

    Unknown = Kee[int](0)
    Software = Kee[int](1)
    OpenVG = Kee[int](2)
    OpenGL = Kee[int](3)
    Direct3D11 = Kee[int](4)
    Vulkan = Kee[int](5)
    Metal = Kee[int](6)
    Null = Kee[int](7)
    Direct3D12 = Kee[int](8)
    OpenGLRhi = Kee[int](3)
    Direct3D11Rhi = Kee[int](4)
    VulkanRhi = Kee[int](5)
    MetalRhi = Kee[int](6)
    NullRhi = Kee[int](7)

  class RenderMode(CuteNum):
    """
    The enum 'QSGRendererInterface::RenderMode' of Qt, with the 3 names Qt
    gives in it.
    """

    RenderMode2D = Kee[int](0)
    RenderMode2DNoDepthBuffer = Kee[int](1)
    RenderMode3D = Kee[int](2)

  class Resource(CuteNum):
    """
    The enum 'QSGRendererInterface::Resource' of Qt, with the 17 names Qt
    gives in it.
    """

    DeviceResource = Kee[int](0)
    CommandQueueResource = Kee[int](1)
    CommandListResource = Kee[int](2)
    PainterResource = Kee[int](3)
    RhiResource = Kee[int](4)
    RhiSwapchainResource = Kee[int](5)
    RhiRedirectCommandBuffer = Kee[int](6)
    RhiRedirectRenderTarget = Kee[int](7)
    PhysicalDeviceResource = Kee[int](8)
    OpenGLContextResource = Kee[int](9)
    DeviceContextResource = Kee[int](10)
    CommandEncoderResource = Kee[int](11)
    VulkanInstanceResource = Kee[int](12)
    RenderPassResource = Kee[int](13)
    RedirectPaintDevice = Kee[int](14)
    GraphicsQueueFamilyIndexResource = Kee[int](15)
    GraphicsQueueIndexResource = Kee[int](16)

  class ShaderCompilationType(CuteFlags):
    """
    The flags enum 'QSGRendererInterface::ShaderCompilationType' of Qt, with
    the 2 names Qt gives in it. Qt names the type of its combinations
    'QSGRendererInterface::ShaderCompilationTypes'.
    """

    RuntimeCompilation = 0x1
    OfflineCompilation = 0x2

  ShaderCompilationTypes = ShaderCompilationType

  class ShaderSourceType(CuteFlags):
    """
    The flags enum 'QSGRendererInterface::ShaderSourceType' of Qt, with the 3
    names Qt gives in it. Qt names the type of its combinations
    'QSGRendererInterface::ShaderSourceTypes'.
    """

    ShaderSourceString = 0x1
    ShaderSourceFile = 0x2
    ShaderByteCode = 0x4

  ShaderSourceTypes = ShaderSourceType

  class ShaderType(CuteNum):
    """
    The enum 'QSGRendererInterface::ShaderType' of Qt, with the 4 names Qt
    gives in it.
    """

    UnknownShadingLanguage = Kee[int](0)
    GLSL = Kee[int](1)
    HLSL = Kee[int](2)
    RhiShader = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(GraphicsApi)
  def isApiRhiBased(api: GraphicsApi) -> bool:
    """
    Calls Qt's 'bool QSGRendererInterface::isApiRhiBased(GraphicsApi api)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrendererinterface.html#isApiRhiBased

    Parameters
    ----------

    api : GraphicsApi
      Passed on as its number.
    """
    #  bool QSGRendererInterface::isApiRhiBased(GraphicsApi api)
    return Rituals.call(
        'ritual_ZN20QSGRendererInterface13isApiRhiBasedENS_11GraphicsApiE',
        api.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGRendererInterface'

  #  A C++ QSGRendererInterface Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGRendererInterface'

  #  The functions Qt calls itself that QSGRendererInterface is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'getResource': (
          'void *QSGRendererInterface::getResource(QQuickWindow *, '
          'Resource) const',
          'void *QSGRendererInterface::getResource(QQuickWindow *, const '
          'char *) const',
      ),
  }

  #  The functions Qt calls itself that QSGRendererInterface is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'graphicsApi': (
          ('_ZNK20QSGRendererInterface11graphicsApiEv',
           ('int', 'enum', 'QtQuick:QSGRendererInterface.GraphicsApi'),
           ()),
      ),
      'shaderType': (
          ('_ZNK20QSGRendererInterface10shaderTypeEv',
           ('int', 'enum', 'QtQuick:QSGRendererInterface.ShaderType'),
           ()),
      ),
      'shaderCompilationType': (
          ('_ZNK20QSGRendererInterface21shaderCompilationTypeEv',
           ('int', 'flags',
            'QtQuick:QSGRendererInterface.ShaderCompilationType'),
           ()),
      ),
      'shaderSourceType': (
          ('_ZNK20QSGRendererInterface16shaderSourceTypeEv',
           ('int', 'flags', 'QtQuick:QSGRendererInterface.ShaderSourceType'),
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

  def graphicsApi(self) -> GraphicsApi:
    """
    Calls Qt's 'GraphicsApi QSGRendererInterface::graphicsApi() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrendererinterface.html#graphicsApi

    Returns
    -------

    GraphicsApi
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'GraphicsApi(number)'
      gives.
    """
    #  GraphicsApi QSGRendererInterface::graphicsApi() const
    return QSGRendererInterface.GraphicsApi(self._callAs(
        'QSGRendererInterface',
        'ritual_ZNK20QSGRendererInterface11graphicsApiEv',
    ))

  def shaderType(self) -> ShaderType:
    """
    Calls Qt's 'ShaderType QSGRendererInterface::shaderType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrendererinterface.html#shaderType

    Returns
    -------

    ShaderType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ShaderType(number)'
      gives.
    """
    #  ShaderType QSGRendererInterface::shaderType() const
    return QSGRendererInterface.ShaderType(self._callAs(
        'QSGRendererInterface',
        'ritual_ZNK20QSGRendererInterface10shaderTypeEv',
    ))

  def shaderCompilationType(self) -> ShaderCompilationTypes:
    """
    Calls Qt's 'ShaderCompilationTypes
    QSGRendererInterface::shaderCompilationType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrendererinterface.html#shaderCompilationType

    Returns
    -------

    ShaderCompilationTypes
      The value standing for the combination Qt gave back.
    """
    #  ShaderCompilationTypes QSGRendererInterface::shaderCompilationType()
    #      const
    return QSGRendererInterface.ShaderCompilationTypes(self._callAs(
        'QSGRendererInterface',
        'ritual_ZNK20QSGRendererInterface21shaderCompilationTypeEv',
    ))

  def shaderSourceType(self) -> ShaderSourceTypes:
    """
    Calls Qt's 'ShaderSourceTypes QSGRendererInterface::shaderSourceType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrendererinterface.html#shaderSourceType

    Returns
    -------

    ShaderSourceTypes
      The value standing for the combination Qt gave back.
    """
    #  ShaderSourceTypes QSGRendererInterface::shaderSourceType() const
    return QSGRendererInterface.ShaderSourceTypes(self._callAs(
        'QSGRendererInterface',
        'ritual_ZNK20QSGRendererInterface16shaderSourceTypeEv',
    ))

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

  @staticmethod
  def getResource(*__, **_) -> Never:
    """
    - Qt's 'void *QSGRendererInterface::getResource(QQuickWindow *window,
      Resource resource) const': gives 'void', which has no cute class yet.
    - Qt's 'void *QSGRendererInterface::getResource(QQuickWindow *window,
      const char *resource) const': gives 'void', which has no cute class
      yet.
    """
    raise NotImplementedError(
        "'QSGRendererInterface.getResource' has no cute function yet. Qt's "
        "'void *QSGRendererInterface::getResource(QQuickWindow *window, "
        "Resource resource) const': gives 'void', which has no cute class "
        "yet. Qt's 'void *QSGRendererInterface::getResource(QQuickWindow "
        "*window, const char *resource) const': gives 'void', which has no "
        "cute class yet.")
