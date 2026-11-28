"""
QQuickGraphicsInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickgraphicsinfo_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickGraphicsInfo to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QQuickWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickWindow = WAIT['QQuickWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickGraphicsInfo(QObject):
  """
  The cute side of Qt's QQuickGraphicsInfo: a plain Python object standing in
  front of one C++ QQuickGraphicsInfo.

  It is built on the cute 'QObject', as Qt's QQuickGraphicsInfo is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickGraphicsInfo that has a ritual and that Python
  can call so far, 19 names in all: 'metaObject', 'api', 'shaderType',
  'shaderCompilationType', 'shaderSourceType', 'majorVersion',
  'minorVersion', 'profile', 'renderableType', 'apiChanged',
  'shaderTypeChanged', 'shaderCompilationTypeChanged',
  'shaderSourceTypeChanged', 'majorVersionChanged', 'minorVersionChanged',
  'profileChanged', 'renderableTypeChanged', 'updateInfo', 'setWindow'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickGraphicsInfo::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickGraphicsInfo::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickGraphicsInfo::qt_qmlMarker_uncreatable()': one of Qt's
    own inner workings.
  - Qt's 'void QQuickGraphicsInfo::qt_qmlMarker_attached()': one of Qt's own
    inner workings.

  What has no ritual
  ------------------

  6 of the 29 functions Qt declares: 3 leans on 'QQuickGraphicsInfo; 2 not a
  gap; 1 leans on 'vtable for QQuickGraphicsInfo', which Qt's source does not
  mark for use from outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QQuickGraphicsInfo is created at the first use, not by
    'QQuickGraphicsInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickGraphicsInfo.
  - Qt tells when it has removed the C++ QQuickGraphicsInfo. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickGraphicsInfo that has no cute function yet,
    '__init__', 'qmlAttachedProperties', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuickGraphicsInfo, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class GraphicsApi(CuteNum):
    """
    The enum 'QQuickGraphicsInfo::GraphicsApi' of Qt, with the 14 names Qt
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

  class OpenGLContextProfile(CuteNum):
    """
    The enum 'QQuickGraphicsInfo::OpenGLContextProfile' of Qt, with the 3
    names Qt gives in it.
    """

    OpenGLNoProfile = Kee[int](0)
    OpenGLCoreProfile = Kee[int](1)
    OpenGLCompatibilityProfile = Kee[int](2)

  class RenderableType(CuteNum):
    """
    The enum 'QQuickGraphicsInfo::RenderableType' of Qt, with the 3 names Qt
    gives in it.
    """

    SurfaceFormatUnspecified = Kee[int](0)
    SurfaceFormatOpenGL = Kee[int](1)
    SurfaceFormatOpenGLES = Kee[int](2)

  class ShaderCompilationType(CuteNum):
    """
    The enum 'QQuickGraphicsInfo::ShaderCompilationType' of Qt, with the 2
    names Qt gives in it.
    """

    RuntimeCompilation = Kee[int](1)
    OfflineCompilation = Kee[int](2)

  class ShaderSourceType(CuteNum):
    """
    The enum 'QQuickGraphicsInfo::ShaderSourceType' of Qt, with the 3 names
    Qt gives in it.
    """

    ShaderSourceString = Kee[int](1)
    ShaderSourceFile = Kee[int](2)
    ShaderByteCode = Kee[int](4)

  class ShaderType(CuteNum):
    """
    The enum 'QQuickGraphicsInfo::ShaderType' of Qt, with the 4 names Qt
    gives in it.
    """

    UnknownShadingLanguage = Kee[int](0)
    GLSL = Kee[int](1)
    HLSL = Kee[int](2)
    RhiShader = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickGraphicsInfo'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickGraphicsInfo::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphicsinfo.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickGraphicsInfo::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickGraphicsInfo10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def api(self) -> GraphicsApi:
    """
    Calls Qt's 'GraphicsApi QQuickGraphicsInfo::api() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphicsinfo.html#api

    Returns
    -------

    GraphicsApi
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'GraphicsApi(number)'
      gives.
    """
    #  GraphicsApi QQuickGraphicsInfo::api() const
    return QQuickGraphicsInfo.GraphicsApi(self.uglySide.call(
        'ritual_ZNK18QQuickGraphicsInfo3apiEv',
    ))

  def shaderType(self) -> ShaderType:
    """
    Calls Qt's 'ShaderType QQuickGraphicsInfo::shaderType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphicsinfo.html#shaderType

    Returns
    -------

    ShaderType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ShaderType(number)'
      gives.
    """
    #  ShaderType QQuickGraphicsInfo::shaderType() const
    return QQuickGraphicsInfo.ShaderType(self.uglySide.call(
        'ritual_ZNK18QQuickGraphicsInfo10shaderTypeEv',
    ))

  def shaderCompilationType(self) -> ShaderCompilationType:
    """
    Calls Qt's 'ShaderCompilationType
    QQuickGraphicsInfo::shaderCompilationType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphicsinfo.html#shaderCompilationType

    Returns
    -------

    ShaderCompilationType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'ShaderCompilationType(number)' gives.
    """
    #  ShaderCompilationType QQuickGraphicsInfo::shaderCompilationType()
    #      const
    return QQuickGraphicsInfo.ShaderCompilationType(self.uglySide.call(
        'ritual_ZNK18QQuickGraphicsInfo21shaderCompilationTypeEv',
    ))

  def shaderSourceType(self) -> ShaderSourceType:
    """
    Calls Qt's 'ShaderSourceType QQuickGraphicsInfo::shaderSourceType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphicsinfo.html#shaderSourceType

    Returns
    -------

    ShaderSourceType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ShaderSourceType(number)'
      gives.
    """
    #  ShaderSourceType QQuickGraphicsInfo::shaderSourceType() const
    return QQuickGraphicsInfo.ShaderSourceType(self.uglySide.call(
        'ritual_ZNK18QQuickGraphicsInfo16shaderSourceTypeEv',
    ))

  def majorVersion(self) -> int:
    """
    Calls Qt's 'int QQuickGraphicsInfo::majorVersion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphicsinfo.html#majorVersion
    """
    #  int QQuickGraphicsInfo::majorVersion() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickGraphicsInfo12majorVersionEv',
    )

  def minorVersion(self) -> int:
    """
    Calls Qt's 'int QQuickGraphicsInfo::minorVersion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphicsinfo.html#minorVersion
    """
    #  int QQuickGraphicsInfo::minorVersion() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickGraphicsInfo12minorVersionEv',
    )

  def profile(self) -> OpenGLContextProfile:
    """
    Calls Qt's 'OpenGLContextProfile QQuickGraphicsInfo::profile() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphicsinfo.html#profile

    Returns
    -------

    OpenGLContextProfile
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'OpenGLContextProfile(number)' gives.
    """
    #  OpenGLContextProfile QQuickGraphicsInfo::profile() const
    return QQuickGraphicsInfo.OpenGLContextProfile(self.uglySide.call(
        'ritual_ZNK18QQuickGraphicsInfo7profileEv',
    ))

  def renderableType(self) -> RenderableType:
    """
    Calls Qt's 'RenderableType QQuickGraphicsInfo::renderableType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphicsinfo.html#renderableType

    Returns
    -------

    RenderableType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'RenderableType(number)'
      gives.
    """
    #  RenderableType QQuickGraphicsInfo::renderableType() const
    return QQuickGraphicsInfo.RenderableType(self.uglySide.call(
        'ritual_ZNK18QQuickGraphicsInfo14renderableTypeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickWindow)
  @overload(NoneType)
  def setWindow(self, window: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QQuickGraphicsInfo::setWindow(QQuickWindow *window)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphicsinfo.html#setWindow

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphicsInfo::setWindow(QQuickWindow *window)
    self.uglySide.call(
        'ritual_ZN18QQuickGraphicsInfo9setWindowEP12QQuickWindow',
        self._addressOf(window),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    - Qt's 'QQuickGraphicsInfo::QQuickGraphicsInfo(QQuickItem *item)': leans
      on 'QQuickGraphicsInfo::staticMetaObject', which Qt's source does not
      mark for use from outside Qt and has no code for that could be taken.
    - Qt's 'QQuickGraphicsInfo::QQuickGraphicsInfo(QQuickWindow *window)':
      leans on 'vtable for QQuickGraphicsInfo', which Qt's source does not
      mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickGraphicsInfo.__init__' has no cute function yet. Qt's "
        "'QQuickGraphicsInfo::QQuickGraphicsInfo(QQuickItem *item)': leans "
        "on 'QQuickGraphicsInfo::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken. Qt's 'QQuickGraphicsInfo::QQuickGraphicsInfo(QQuickWindow "
        "*window)': leans on 'vtable for QQuickGraphicsInfo', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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

  def apiChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGraphicsInfo::apiChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphicsinfo.html#apiChanged
    """
    #  void QQuickGraphicsInfo::apiChanged()
    self.uglySide.call('ritual_ZN18QQuickGraphicsInfo10apiChangedEv')

  def shaderTypeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGraphicsInfo::shaderTypeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphicsinfo.html#shaderTypeChanged
    """
    #  void QQuickGraphicsInfo::shaderTypeChanged()
    self.uglySide.call('ritual_ZN18QQuickGraphicsInfo17shaderTypeChangedEv')

  def shaderCompilationTypeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGraphicsInfo::shaderCompilationTypeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphicsinfo.html
    """
    #  void QQuickGraphicsInfo::shaderCompilationTypeChanged()
    self.uglySide.call(
        'ritual_ZN18QQuickGraphicsInfo28shaderCompilationTypeChangedEv',
    )

  def shaderSourceTypeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGraphicsInfo::shaderSourceTypeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphicsinfo.html#shaderSourceTypeChanged
    """
    #  void QQuickGraphicsInfo::shaderSourceTypeChanged()
    self.uglySide.call(
        'ritual_ZN18QQuickGraphicsInfo23shaderSourceTypeChangedEv',
    )

  def majorVersionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGraphicsInfo::majorVersionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphicsinfo.html#majorVersionChanged
    """
    #  void QQuickGraphicsInfo::majorVersionChanged()
    self.uglySide.call(
        'ritual_ZN18QQuickGraphicsInfo19majorVersionChangedEv',
    )

  def minorVersionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGraphicsInfo::minorVersionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphicsinfo.html#minorVersionChanged
    """
    #  void QQuickGraphicsInfo::minorVersionChanged()
    self.uglySide.call(
        'ritual_ZN18QQuickGraphicsInfo19minorVersionChangedEv',
    )

  def profileChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGraphicsInfo::profileChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphicsinfo.html#profileChanged
    """
    #  void QQuickGraphicsInfo::profileChanged()
    self.uglySide.call('ritual_ZN18QQuickGraphicsInfo14profileChangedEv')

  def renderableTypeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGraphicsInfo::renderableTypeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphicsinfo.html#renderableTypeChanged
    """
    #  void QQuickGraphicsInfo::renderableTypeChanged()
    self.uglySide.call(
        'ritual_ZN18QQuickGraphicsInfo21renderableTypeChangedEv',
    )

  def updateInfo(self) -> None:
    """
    Calls Qt's 'void QQuickGraphicsInfo::updateInfo()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphicsinfo.html#updateInfo
    """
    #  void QQuickGraphicsInfo::updateInfo()
    self.uglySide.call('ritual_ZN18QQuickGraphicsInfo10updateInfoEv')

  @staticmethod
  def qmlAttachedProperties(*__, **_) -> Never:
    """
    Qt's 'QQuickGraphicsInfo
    *QQuickGraphicsInfo::qmlAttachedProperties(QObject *object)': leans on
    'QQuickGraphicsInfo::staticMetaObject', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickGraphicsInfo.qmlAttachedProperties' has no cute function "
        "yet. Qt's 'QQuickGraphicsInfo "
        "*QQuickGraphicsInfo::qmlAttachedProperties(QObject *object)': "
        "leans on 'QQuickGraphicsInfo::staticMetaObject', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")
