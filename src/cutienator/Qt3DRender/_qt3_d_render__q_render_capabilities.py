"""
Qt3DRender::QRenderCapabilities binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qrendercapabilities.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject, QStringList
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRenderCapabilities(QObject):
  """
  The cute side of Qt's Qt3DRender::QRenderCapabilities: a plain Python
  object standing in front of one C++ Qt3DRender::QRenderCapabilities.

  It is built on the cute 'QObject', as Qt's Qt3DRender::QRenderCapabilities
  is built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QRenderCapabilities that has a ritual
  and that Python can call so far, 34 names in all: 'metaObject', 'tr',
  'isValid', 'api', 'profile', 'majorVersion', 'minorVersion', 'extensions',
  'vendor', 'renderer', 'driverVersion', 'glslVersion', 'maxSamples',
  'maxTextureSize', 'maxTextureUnits', 'maxTextureLayers', 'supportsUBO',
  'maxUBOSize', 'maxUBOBindings', 'supportsSSBO', 'maxSSBOSize',
  'maxSSBOBindings', 'supportsImageStore', 'maxImageUnits',
  'supportsCompute', 'maxWorkGroupCountX', 'maxWorkGroupCountY',
  'maxWorkGroupCountZ', 'maxWorkGroupSizeX', 'maxWorkGroupSizeY',
  'maxWorkGroupSizeZ', 'maxComputeInvocations', 'maxComputeSharedMemorySize',
  'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QRenderCapabilities::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int Qt3DRender::QRenderCapabilities::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QRenderCapabilities::~QRenderCapabilities()': the
    destructor: Python never removes a C++ Qt3DRender::QRenderCapabilities.
  - Qt's 'const QRenderCapabilitiesPrivate
    *Qt3DRender::QRenderCapabilities::d_func() const': takes in Python what
    'QRenderCapabilitiesPrivate *Qt3DRender::QRenderCapabilities::d_func()'
    takes.

  What has no ritual
  ------------------

  2 of the 41 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QRenderCapabilities is created at the first use, not
    by 'Qt3DRender::QRenderCapabilities(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QRenderCapabilities.
  - Qt tells when it has removed the C++ Qt3DRender::QRenderCapabilities.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside Qt3DRender::QRenderCapabilities, each a class
  #  in here as in C++, and the names Qt has for the combinations of its
  #  flags enums.

  class API(CuteNum):
    """
    The enum 'Qt3DRender::QRenderCapabilities::API' of Qt, with the 5 names
    Qt gives in it.
    """

    OpenGL = Kee[int](1)
    OpenGLES = Kee[int](2)
    Vulkan = Kee[int](3)
    DirectX = Kee[int](4)
    RHI = Kee[int](5)

  class Profile(CuteNum):
    """
    The enum 'Qt3DRender::QRenderCapabilities::Profile' of Qt, with the 3
    names Qt gives in it.
    """

    NoProfile = Kee[int](0)
    CoreProfile = Kee[int](1)
    CompatibilityProfile = Kee[int](2)

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
    Calls Qt's 'QString Qt3DRender::QRenderCapabilities::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapabilities.html#tr

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
    #  QString Qt3DRender::QRenderCapabilities::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender19QRenderCapabilities2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QRenderCapabilities'

  #  A C++ Qt3DRender::QRenderCapabilities Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QRenderCapabilities'

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
    *Qt3DRender::QRenderCapabilities::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapabilities.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QRenderCapabilities::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender19QRenderCapabilities10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::QRenderCapabilities::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapabilities.html#isValid
    """
    #  bool Qt3DRender::QRenderCapabilities::isValid() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender19QRenderCapabilities7isValidEv',
    )

  def api(self) -> API:
    """
    Calls Qt's 'API Qt3DRender::QRenderCapabilities::api() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapabilities.html#api

    Returns
    -------

    API
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'API(number)' gives.
    """
    #  API Qt3DRender::QRenderCapabilities::api() const
    return QRenderCapabilities.API(self.uglySide.call(
        'ritual_ZNK10Qt3DRender19QRenderCapabilities3apiEv',
    ))

  def profile(self) -> Profile:
    """
    Calls Qt's 'Profile Qt3DRender::QRenderCapabilities::profile() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapabilities.html#profile

    Returns
    -------

    Profile
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Profile(number)' gives.
    """
    #  Profile Qt3DRender::QRenderCapabilities::profile() const
    return QRenderCapabilities.Profile(self.uglySide.call(
        'ritual_ZNK10Qt3DRender19QRenderCapabilities7profileEv',
    ))

  def majorVersion(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QRenderCapabilities::majorVersion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapabilities.html#majorVersion
    """
    #  int Qt3DRender::QRenderCapabilities::majorVersion() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender19QRenderCapabilities12majorVersionEv',
    )

  def minorVersion(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QRenderCapabilities::minorVersion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapabilities.html#minorVersion
    """
    #  int Qt3DRender::QRenderCapabilities::minorVersion() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender19QRenderCapabilities12minorVersionEv',
    )

  def extensions(self) -> QStringList:
    """
    Calls Qt's 'QStringList Qt3DRender::QRenderCapabilities::extensions()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapabilities.html#extensions

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList Qt3DRender::QRenderCapabilities::extensions() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender19QRenderCapabilities10extensionsEv',
    )
    return QStringList._cuteOwning(address)

  def vendor(self) -> str:
    """
    Calls Qt's 'QString Qt3DRender::QRenderCapabilities::vendor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapabilities.html#vendor

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DRender::QRenderCapabilities::vendor() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender19QRenderCapabilities6vendorEv',
    )

  def renderer(self) -> str:
    """
    Calls Qt's 'QString Qt3DRender::QRenderCapabilities::renderer() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapabilities.html#renderer

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DRender::QRenderCapabilities::renderer() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender19QRenderCapabilities8rendererEv',
    )

  def driverVersion(self) -> str:
    """
    Calls Qt's 'QString Qt3DRender::QRenderCapabilities::driverVersion()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapabilities.html#driverVersion

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DRender::QRenderCapabilities::driverVersion() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender19QRenderCapabilities13driverVersionEv',
    )

  def glslVersion(self) -> str:
    """
    Calls Qt's 'QString Qt3DRender::QRenderCapabilities::glslVersion()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapabilities.html#glslVersion

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DRender::QRenderCapabilities::glslVersion() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender19QRenderCapabilities11glslVersionEv',
    )

  def maxSamples(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QRenderCapabilities::maxSamples() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapabilities.html#maxSamples
    """
    #  int Qt3DRender::QRenderCapabilities::maxSamples() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender19QRenderCapabilities10maxSamplesEv',
    )

  def maxTextureSize(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QRenderCapabilities::maxTextureSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapabilities.html#maxTextureSize
    """
    #  int Qt3DRender::QRenderCapabilities::maxTextureSize() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender19QRenderCapabilities14maxTextureSizeEv',
    )

  def maxTextureUnits(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QRenderCapabilities::maxTextureUnits()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapabilities.html
    """
    #  int Qt3DRender::QRenderCapabilities::maxTextureUnits() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender19QRenderCapabilities15maxTextureUnitsEv',
    )

  def maxTextureLayers(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QRenderCapabilities::maxTextureLayers()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapabilities.html
    """
    #  int Qt3DRender::QRenderCapabilities::maxTextureLayers() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender19QRenderCapabilities16maxTextureLayersEv',
    )

  def supportsUBO(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::QRenderCapabilities::supportsUBO() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapabilities.html#supportsUBO
    """
    #  bool Qt3DRender::QRenderCapabilities::supportsUBO() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender19QRenderCapabilities11supportsUBOEv',
    )

  def maxUBOSize(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QRenderCapabilities::maxUBOSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapabilities.html#maxUBOSize
    """
    #  int Qt3DRender::QRenderCapabilities::maxUBOSize() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender19QRenderCapabilities10maxUBOSizeEv',
    )

  def maxUBOBindings(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QRenderCapabilities::maxUBOBindings() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapabilities.html#maxUBOBindings
    """
    #  int Qt3DRender::QRenderCapabilities::maxUBOBindings() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender19QRenderCapabilities14maxUBOBindingsEv',
    )

  def supportsSSBO(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::QRenderCapabilities::supportsSSBO() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapabilities.html#supportsSSBO
    """
    #  bool Qt3DRender::QRenderCapabilities::supportsSSBO() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender19QRenderCapabilities12supportsSSBOEv',
    )

  def maxSSBOSize(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QRenderCapabilities::maxSSBOSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapabilities.html#maxSSBOSize
    """
    #  int Qt3DRender::QRenderCapabilities::maxSSBOSize() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender19QRenderCapabilities11maxSSBOSizeEv',
    )

  def maxSSBOBindings(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QRenderCapabilities::maxSSBOBindings()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapabilities.html
    """
    #  int Qt3DRender::QRenderCapabilities::maxSSBOBindings() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender19QRenderCapabilities15maxSSBOBindingsEv',
    )

  def supportsImageStore(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::QRenderCapabilities::supportsImageStore()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapabilities.html
    """
    #  bool Qt3DRender::QRenderCapabilities::supportsImageStore() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender19QRenderCapabilities18supportsImageStoreEv',
    )

  def maxImageUnits(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QRenderCapabilities::maxImageUnits() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapabilities.html#maxImageUnits
    """
    #  int Qt3DRender::QRenderCapabilities::maxImageUnits() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender19QRenderCapabilities13maxImageUnitsEv',
    )

  def supportsCompute(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::QRenderCapabilities::supportsCompute()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapabilities.html
    """
    #  bool Qt3DRender::QRenderCapabilities::supportsCompute() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender19QRenderCapabilities15supportsComputeEv',
    )

  def maxWorkGroupCountX(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QRenderCapabilities::maxWorkGroupCountX()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapabilities.html
    """
    #  int Qt3DRender::QRenderCapabilities::maxWorkGroupCountX() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender19QRenderCapabilities18maxWorkGroupCountXEv',
    )

  def maxWorkGroupCountY(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QRenderCapabilities::maxWorkGroupCountY()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapabilities.html
    """
    #  int Qt3DRender::QRenderCapabilities::maxWorkGroupCountY() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender19QRenderCapabilities18maxWorkGroupCountYEv',
    )

  def maxWorkGroupCountZ(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QRenderCapabilities::maxWorkGroupCountZ()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapabilities.html
    """
    #  int Qt3DRender::QRenderCapabilities::maxWorkGroupCountZ() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender19QRenderCapabilities18maxWorkGroupCountZEv',
    )

  def maxWorkGroupSizeX(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QRenderCapabilities::maxWorkGroupSizeX()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapabilities.html
    """
    #  int Qt3DRender::QRenderCapabilities::maxWorkGroupSizeX() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender19QRenderCapabilities17maxWorkGroupSizeXEv',
    )

  def maxWorkGroupSizeY(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QRenderCapabilities::maxWorkGroupSizeY()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapabilities.html
    """
    #  int Qt3DRender::QRenderCapabilities::maxWorkGroupSizeY() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender19QRenderCapabilities17maxWorkGroupSizeYEv',
    )

  def maxWorkGroupSizeZ(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QRenderCapabilities::maxWorkGroupSizeZ()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapabilities.html
    """
    #  int Qt3DRender::QRenderCapabilities::maxWorkGroupSizeZ() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender19QRenderCapabilities17maxWorkGroupSizeZEv',
    )

  def maxComputeInvocations(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QRenderCapabilities::maxComputeInvocations()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapabilities.html
    """
    #  int Qt3DRender::QRenderCapabilities::maxComputeInvocations() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender19QRenderCapabilities21maxComputeInvocations'
        'Ev',
    )

  def maxComputeSharedMemorySize(self) -> int:
    """
    Calls Qt's 'int
    Qt3DRender::QRenderCapabilities::maxComputeSharedMemorySize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapabilities.html
    """
    #  int Qt3DRender::QRenderCapabilities::maxComputeSharedMemorySize()
    #      const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender19QRenderCapabilities26maxComputeSharedMemor'
        'ySizeEv',
    )

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QRenderCapabilities::QRenderCapabilities(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapabilities.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QRenderCapabilities::QRenderCapabilities(QObject *parent)
    self._noteCreation(QRenderCapabilities, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender19QRenderCapabilitiesC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def d_func(self) -> Optional[Qt3DRender.QRenderCapabilitiesPrivate]:
    """
    Calls Qt's 'QRenderCapabilitiesPrivate
    *Qt3DRender::QRenderCapabilities::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapabilities.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QRenderCapabilitiesPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRenderCapabilitiesPrivate *Qt3DRender::QRenderCapabilities::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender19QRenderCapabilities6d_funcEv',
    )
    return Qt3DRender.QRenderCapabilitiesPrivate._cuteAt(address)
