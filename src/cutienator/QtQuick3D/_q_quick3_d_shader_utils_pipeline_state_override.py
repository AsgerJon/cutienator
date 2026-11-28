"""
QQuick3DShaderUtilsPipelineStateOverride binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dshaderutils_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DShaderUtilsPipelineStateOverride to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QQuick3DShaderUtilsRenderCommand

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRect, QRectF
  from ..QtQuick3DRuntimeRender import QSSGCommand
  from . import QQuick3DRenderPassTargetBlend
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuick3DRenderPassTargetBlend = WAIT['QQuick3DRenderPassTargetBlend']
  QRect = WAIT['QRect']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DShaderUtilsPipelineStateOverride(QQuick3DShaderUtilsRenderCommand):
  """
  The cute side of Qt's QQuick3DShaderUtilsPipelineStateOverride: a plain
  Python object standing in front of one C++
  QQuick3DShaderUtilsPipelineStateOverride.

  It is built on the cute 'QQuick3DShaderUtilsRenderCommand', as Qt's
  QQuick3DShaderUtilsPipelineStateOverride is built on Qt's
  QQuick3DShaderUtilsRenderCommand, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DShaderUtilsPipelineStateOverride that has a
  ritual and that Python can call so far, 83 names in all: 'metaObject',
  'tr', 'depthTestEnabled', 'setDepthTestEnabled', 'resetDepthTestEnabled',
  'depthWriteEnabled', 'setDepthWriteEnabled', 'resetDepthWriteEnabled',
  'blendEnabled', 'setBlendEnabled', 'resetBlendEnabled',
  'usesStencilReference', 'setUsesStencilReference',
  'resetUsesStencilReference', 'usesScissor', 'setUsesScissor',
  'resetUsesScissor', 'depthFunction', 'setDepthFunction',
  'resetDepthFunction', 'cullMode', 'setCullMode', 'resetCullMode',
  'polygonMode', 'setPolygonMode', 'resetPolygonMode', 'stencilWriteMask',
  'setStencilWriteMask', 'resetStencilWriteMask', 'stencilReference',
  'setStencilReference', 'resetStencilReference', 'viewport', 'setViewport',
  'resetViewport', 'scissor', 'setScissor', 'resetScissor', 'targetBlend0',
  'setTargetBlend0', 'resetTargetBlend0', 'targetBlend1', 'setTargetBlend1',
  'resetTargetBlend1', 'targetBlend2', 'setTargetBlend2',
  'resetTargetBlend2', 'targetBlend3', 'setTargetBlend3',
  'resetTargetBlend3', 'targetBlend4', 'setTargetBlend4',
  'resetTargetBlend4', 'targetBlend5', 'setTargetBlend5',
  'resetTargetBlend5', 'targetBlend6', 'setTargetBlend6',
  'resetTargetBlend6', 'targetBlend7', 'setTargetBlend7',
  'resetTargetBlend7', 'depthTestEnabledChanged', 'depthWriteEnabledChanged',
  'blendEnabledChanged', 'usesStencilReferenceChanged', 'usesScissorChanged',
  'depthFunctionChanged', 'cullModeChanged', 'polygonModeChanged',
  'stencilWriteMaskChanged', 'stencilReferenceChanged', 'viewportChanged',
  'scissorChanged', 'targetBlend0Changed', 'targetBlend1Changed',
  'targetBlend2Changed', 'targetBlend3Changed', 'targetBlend4Changed',
  'targetBlend5Changed', 'targetBlend6Changed', 'targetBlend7Changed',
  'cloneCommand'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DShaderUtilsPipelineStateOverride::qt_metacast(const
    char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QQuick3DShaderUtilsPipelineStateOverride::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DShaderUtilsPipelineStateOverride::
    ~QQuick3DShaderUtilsPipelineStateOverride()': the destructor: Python
    never removes a C++ QQuick3DShaderUtilsPipelineStateOverride.

  What has no ritual
  ------------------

  2 of the 89 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DShaderUtilsPipelineStateOverride is created at the first
    use, not by 'QQuick3DShaderUtilsPipelineStateOverride(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DShaderUtilsPipelineStateOverride.
  - Qt tells when it has removed the C++
    QQuick3DShaderUtilsPipelineStateOverride. Every call on the cute object,
    and every use of it as an argument, then raises 'RuntimeError', and
    nothing reaches C++.
  """

  #  The enums Qt writes inside QQuick3DShaderUtilsPipelineStateOverride,
  #  each a class in here as in C++, and the names Qt has for the
  #  combinations of its flags enums.

  class CompareOperation(CuteNum, scoped=True):
    """
    The enum 'QQuick3DShaderUtilsPipelineStateOverride::CompareOperation' of
    Qt, with the 8 names Qt gives in it. C++ keeps these names inside the
    enum, so the class that holds the enum does not have them.
    """

    Never = Kee[int](0)
    Less = Kee[int](1)
    Equal = Kee[int](2)
    LessOrEqual = Kee[int](3)
    Greater = Kee[int](4)
    NotEqual = Kee[int](5)
    GreaterOrEqual = Kee[int](6)
    Always = Kee[int](7)

  class CullMode(CuteNum, scoped=True):
    """
    The enum 'QQuick3DShaderUtilsPipelineStateOverride::CullMode' of Qt, with
    the 3 names Qt gives in it. C++ keeps these names inside the enum, so the
    class that holds the enum does not have them.
    """

    NULL = Kee[int](0)
    Front = Kee[int](1)
    Back = Kee[int](2)

  class PolygonMode(CuteNum, scoped=True):
    """
    The enum 'QQuick3DShaderUtilsPipelineStateOverride::PolygonMode' of Qt,
    with the 2 names Qt gives in it. C++ keeps these names inside the enum,
    so the class that holds the enum does not have them.
    """

    Fill = Kee[int](0)
    Line = Kee[int](1)

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
    Calls Qt's 'QString QQuick3DShaderUtilsPipelineStateOverride::tr(const
    char *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html#tr

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
    #  QString QQuick3DShaderUtilsPipelineStateOverride::tr(const char *s,
    #      const char *c, int n)
    return Rituals.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DShaderUtilsPipelineStateOverride'

  #  A C++ QQuick3DShaderUtilsPipelineStateOverride Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DShaderUtilsPipelineStateOverride'

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
    *QQuick3DShaderUtilsPipelineStateOverride::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *QQuick3DShaderUtilsPipelineStateOverride::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK40QQuick3DShaderUtilsPipelineStateOverride10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def depthTestEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    QQuick3DShaderUtilsPipelineStateOverride::depthTestEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  bool QQuick3DShaderUtilsPipelineStateOverride::depthTestEnabled()
    #      const
    return self.uglySide.call(
        'ritual_ZNK40QQuick3DShaderUtilsPipelineStateOverride16depthTestEna'
        'bledEv',
    )

  def depthWriteEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    QQuick3DShaderUtilsPipelineStateOverride::depthWriteEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  bool QQuick3DShaderUtilsPipelineStateOverride::depthWriteEnabled()
    #      const
    return self.uglySide.call(
        'ritual_ZNK40QQuick3DShaderUtilsPipelineStateOverride17depthWriteEn'
        'abledEv',
    )

  def blendEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DShaderUtilsPipelineStateOverride::blendEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  bool QQuick3DShaderUtilsPipelineStateOverride::blendEnabled() const
    return self.uglySide.call(
        'ritual_ZNK40QQuick3DShaderUtilsPipelineStateOverride12blendEnabled'
        'Ev',
    )

  def usesStencilReference(self) -> bool:
    """
    Calls Qt's 'bool
    QQuick3DShaderUtilsPipelineStateOverride::usesStencilReference() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  bool QQuick3DShaderUtilsPipelineStateOverride::usesStencilReference()
    #      const
    return self.uglySide.call(
        'ritual_ZNK40QQuick3DShaderUtilsPipelineStateOverride20usesStencilR'
        'eferenceEv',
    )

  def usesScissor(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DShaderUtilsPipelineStateOverride::usesScissor()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  bool QQuick3DShaderUtilsPipelineStateOverride::usesScissor() const
    return self.uglySide.call(
        'ritual_ZNK40QQuick3DShaderUtilsPipelineStateOverride11usesScissorE'
        'v',
    )

  def depthFunction(self) -> CompareOperation:
    """
    Calls Qt's 'CompareOperation
    QQuick3DShaderUtilsPipelineStateOverride::depthFunction() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html

    Returns
    -------

    CompareOperation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'CompareOperation(number)'
      gives.
    """
    #  CompareOperation
    #      QQuick3DShaderUtilsPipelineStateOverride::depthFunction() const
    return QQuick3DShaderUtilsPipelineStateOverride.CompareOperation(
        self.uglySide.call(
            'ritual_ZNK40QQuick3DShaderUtilsPipelineStateOverride13depthFun'
            'ctionEv',
        ))

  def cullMode(self) -> CullMode:
    """
    Calls Qt's 'CullMode QQuick3DShaderUtilsPipelineStateOverride::cullMode()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html

    Returns
    -------

    CullMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'CullMode(number)' gives.
    """
    #  CullMode QQuick3DShaderUtilsPipelineStateOverride::cullMode() const
    return QQuick3DShaderUtilsPipelineStateOverride.CullMode(
        self.uglySide.call(
            'ritual_ZNK40QQuick3DShaderUtilsPipelineStateOverride8cullModeE'
            'v',
        ))

  def polygonMode(self) -> PolygonMode:
    """
    Calls Qt's 'PolygonMode
    QQuick3DShaderUtilsPipelineStateOverride::polygonMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html

    Returns
    -------

    PolygonMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'PolygonMode(number)'
      gives.
    """
    #  PolygonMode QQuick3DShaderUtilsPipelineStateOverride::polygonMode()
    #      const
    return QQuick3DShaderUtilsPipelineStateOverride.PolygonMode(
        self.uglySide.call(
            'ritual_ZNK40QQuick3DShaderUtilsPipelineStateOverride11polygonM'
            'odeEv',
        ))

  def stencilWriteMask(self) -> int:
    """
    Calls Qt's 'quint32
    QQuick3DShaderUtilsPipelineStateOverride::stencilWriteMask() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  quint32 QQuick3DShaderUtilsPipelineStateOverride::stencilWriteMask()
    #      const
    return self.uglySide.call(
        'ritual_ZNK40QQuick3DShaderUtilsPipelineStateOverride16stencilWrite'
        'MaskEv',
    )

  def stencilReference(self) -> int:
    """
    Calls Qt's 'quint32
    QQuick3DShaderUtilsPipelineStateOverride::stencilReference() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  quint32 QQuick3DShaderUtilsPipelineStateOverride::stencilReference()
    #      const
    return self.uglySide.call(
        'ritual_ZNK40QQuick3DShaderUtilsPipelineStateOverride16stencilRefer'
        'enceEv',
    )

  def viewport(self) -> QRectF:
    """
    Calls Qt's 'QRectF QQuick3DShaderUtilsPipelineStateOverride::viewport()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuick3DShaderUtilsPipelineStateOverride::viewport() const
    address = self.uglySide.call(
        'ritual_ZNK40QQuick3DShaderUtilsPipelineStateOverride8viewportEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def scissor(self) -> QRect:
    """
    Calls Qt's 'QRect QQuick3DShaderUtilsPipelineStateOverride::scissor()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QQuick3DShaderUtilsPipelineStateOverride::scissor() const
    address = self.uglySide.call(
        'ritual_ZNK40QQuick3DShaderUtilsPipelineStateOverride7scissorEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def targetBlend0(self) -> QQuick3DRenderPassTargetBlend:
    """
    Calls Qt's 'QQuick3DRenderPassTargetBlend
    QQuick3DShaderUtilsPipelineStateOverride::targetBlend0() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html

    Returns
    -------

    QQuick3DRenderPassTargetBlend
      A new cute QQuick3DRenderPassTargetBlend around the copy Qt gave back.
      Python owns it.
    """
    #  QQuick3DRenderPassTargetBlend
    #      QQuick3DShaderUtilsPipelineStateOverride::targetBlend0() const
    address = self.uglySide.call(
        'ritual_ZNK40QQuick3DShaderUtilsPipelineStateOverride12targetBlend0'
        'Ev',
    )
    from . import QQuick3DRenderPassTargetBlend
    return QQuick3DRenderPassTargetBlend._cuteOwning(address)

  def targetBlend1(self) -> QQuick3DRenderPassTargetBlend:
    """
    Calls Qt's 'QQuick3DRenderPassTargetBlend
    QQuick3DShaderUtilsPipelineStateOverride::targetBlend1() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html

    Returns
    -------

    QQuick3DRenderPassTargetBlend
      A new cute QQuick3DRenderPassTargetBlend around the copy Qt gave back.
      Python owns it.
    """
    #  QQuick3DRenderPassTargetBlend
    #      QQuick3DShaderUtilsPipelineStateOverride::targetBlend1() const
    address = self.uglySide.call(
        'ritual_ZNK40QQuick3DShaderUtilsPipelineStateOverride12targetBlend1'
        'Ev',
    )
    from . import QQuick3DRenderPassTargetBlend
    return QQuick3DRenderPassTargetBlend._cuteOwning(address)

  def targetBlend2(self) -> QQuick3DRenderPassTargetBlend:
    """
    Calls Qt's 'QQuick3DRenderPassTargetBlend
    QQuick3DShaderUtilsPipelineStateOverride::targetBlend2() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html

    Returns
    -------

    QQuick3DRenderPassTargetBlend
      A new cute QQuick3DRenderPassTargetBlend around the copy Qt gave back.
      Python owns it.
    """
    #  QQuick3DRenderPassTargetBlend
    #      QQuick3DShaderUtilsPipelineStateOverride::targetBlend2() const
    address = self.uglySide.call(
        'ritual_ZNK40QQuick3DShaderUtilsPipelineStateOverride12targetBlend2'
        'Ev',
    )
    from . import QQuick3DRenderPassTargetBlend
    return QQuick3DRenderPassTargetBlend._cuteOwning(address)

  def targetBlend3(self) -> QQuick3DRenderPassTargetBlend:
    """
    Calls Qt's 'QQuick3DRenderPassTargetBlend
    QQuick3DShaderUtilsPipelineStateOverride::targetBlend3() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html

    Returns
    -------

    QQuick3DRenderPassTargetBlend
      A new cute QQuick3DRenderPassTargetBlend around the copy Qt gave back.
      Python owns it.
    """
    #  QQuick3DRenderPassTargetBlend
    #      QQuick3DShaderUtilsPipelineStateOverride::targetBlend3() const
    address = self.uglySide.call(
        'ritual_ZNK40QQuick3DShaderUtilsPipelineStateOverride12targetBlend3'
        'Ev',
    )
    from . import QQuick3DRenderPassTargetBlend
    return QQuick3DRenderPassTargetBlend._cuteOwning(address)

  def targetBlend4(self) -> QQuick3DRenderPassTargetBlend:
    """
    Calls Qt's 'QQuick3DRenderPassTargetBlend
    QQuick3DShaderUtilsPipelineStateOverride::targetBlend4() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html

    Returns
    -------

    QQuick3DRenderPassTargetBlend
      A new cute QQuick3DRenderPassTargetBlend around the copy Qt gave back.
      Python owns it.
    """
    #  QQuick3DRenderPassTargetBlend
    #      QQuick3DShaderUtilsPipelineStateOverride::targetBlend4() const
    address = self.uglySide.call(
        'ritual_ZNK40QQuick3DShaderUtilsPipelineStateOverride12targetBlend4'
        'Ev',
    )
    from . import QQuick3DRenderPassTargetBlend
    return QQuick3DRenderPassTargetBlend._cuteOwning(address)

  def targetBlend5(self) -> QQuick3DRenderPassTargetBlend:
    """
    Calls Qt's 'QQuick3DRenderPassTargetBlend
    QQuick3DShaderUtilsPipelineStateOverride::targetBlend5() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html

    Returns
    -------

    QQuick3DRenderPassTargetBlend
      A new cute QQuick3DRenderPassTargetBlend around the copy Qt gave back.
      Python owns it.
    """
    #  QQuick3DRenderPassTargetBlend
    #      QQuick3DShaderUtilsPipelineStateOverride::targetBlend5() const
    address = self.uglySide.call(
        'ritual_ZNK40QQuick3DShaderUtilsPipelineStateOverride12targetBlend5'
        'Ev',
    )
    from . import QQuick3DRenderPassTargetBlend
    return QQuick3DRenderPassTargetBlend._cuteOwning(address)

  def targetBlend6(self) -> QQuick3DRenderPassTargetBlend:
    """
    Calls Qt's 'QQuick3DRenderPassTargetBlend
    QQuick3DShaderUtilsPipelineStateOverride::targetBlend6() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html

    Returns
    -------

    QQuick3DRenderPassTargetBlend
      A new cute QQuick3DRenderPassTargetBlend around the copy Qt gave back.
      Python owns it.
    """
    #  QQuick3DRenderPassTargetBlend
    #      QQuick3DShaderUtilsPipelineStateOverride::targetBlend6() const
    address = self.uglySide.call(
        'ritual_ZNK40QQuick3DShaderUtilsPipelineStateOverride12targetBlend6'
        'Ev',
    )
    from . import QQuick3DRenderPassTargetBlend
    return QQuick3DRenderPassTargetBlend._cuteOwning(address)

  def targetBlend7(self) -> QQuick3DRenderPassTargetBlend:
    """
    Calls Qt's 'QQuick3DRenderPassTargetBlend
    QQuick3DShaderUtilsPipelineStateOverride::targetBlend7() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html

    Returns
    -------

    QQuick3DRenderPassTargetBlend
      A new cute QQuick3DRenderPassTargetBlend around the copy Qt gave back.
      Python owns it.
    """
    #  QQuick3DRenderPassTargetBlend
    #      QQuick3DShaderUtilsPipelineStateOverride::targetBlend7() const
    address = self.uglySide.call(
        'ritual_ZNK40QQuick3DShaderUtilsPipelineStateOverride12targetBlend7'
        'Ev',
    )
    from . import QQuick3DRenderPassTargetBlend
    return QQuick3DRenderPassTargetBlend._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setDepthTestEnabled(self, newDepthTestEnabled: bool) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::setDepthTestEnabled(bool
    newDepthTestEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html

    Parameters
    ----------

    newDepthTestEnabled : bool
      Passed on as it is.
    """
    #  void
    #      QQuick3DShaderUtilsPipelineStateOverride::setDepthTestEnabled(bool
    #      newDepthTestEnabled)
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride19setDepthTestE'
        'nabledEb',
        newDepthTestEnabled,
    )

  @overload(bool)
  def setDepthWriteEnabled(self, newDepthWriteEnabled: bool) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::setDepthWriteEnabled(bool
    newDepthWriteEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html

    Parameters
    ----------

    newDepthWriteEnabled : bool
      Passed on as it is.
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::setDepthWriteEnabled(
    #      bool newDepthWriteEnabled)
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride20setDepthWrite'
        'EnabledEb',
        newDepthWriteEnabled,
    )

  @overload(bool)
  def setBlendEnabled(self, newBlendEnabled: bool) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::setBlendEnabled(bool
    newBlendEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html

    Parameters
    ----------

    newBlendEnabled : bool
      Passed on as it is.
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::setBlendEnabled(bool
    #      newBlendEnabled)
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride15setBlendEnabl'
        'edEb',
        newBlendEnabled,
    )

  @overload(bool)
  def setUsesStencilReference(self, newUsesStencilReference: bool) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::setUsesStencilReference(bool
    newUsesStencilReference)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html

    Parameters
    ----------

    newUsesStencilReference : bool
      Passed on as it is.
    """
    #  void
    #      QQuick3DShaderUtilsPipelineStateOverride::setUsesStencilReference(
    #      bool newUsesStencilReference)
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride23setUsesStenci'
        'lReferenceEb',
        newUsesStencilReference,
    )

  @overload(bool)
  def setUsesScissor(self, newUsesScissor: bool) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::setUsesScissor(bool
    newUsesScissor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html

    Parameters
    ----------

    newUsesScissor : bool
      Passed on as it is.
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::setUsesScissor(bool
    #      newUsesScissor)
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride14setUsesScisso'
        'rEb',
        newUsesScissor,
    )

  @overload(CompareOperation)
  def setDepthFunction(self, newDepthFunction: CompareOperation) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::setDepthFunction(
    CompareOperation newDepthFunction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html

    Parameters
    ----------

    newDepthFunction : CompareOperation
      Passed on as its number.
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::setDepthFunction(
    #      CompareOperation newDepthFunction)
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride16setDepthFunct'
        'ionENS_16CompareOperationE',
        newDepthFunction.value,
    )

  @overload(CullMode)
  def setCullMode(self, newCullMode: CullMode) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::setCullMode(CullMode
    newCullMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html

    Parameters
    ----------

    newCullMode : CullMode
      Passed on as its number.
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::setCullMode(CullMode
    #      newCullMode)
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride11setCullModeEN'
        'S_8CullModeE',
        newCullMode.value,
    )

  @overload(PolygonMode)
  def setPolygonMode(self, newPolygonMode: PolygonMode) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::setPolygonMode(PolygonMode
    newPolygonMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html

    Parameters
    ----------

    newPolygonMode : PolygonMode
      Passed on as its number.
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::setPolygonMode(
    #      PolygonMode newPolygonMode)
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride14setPolygonMod'
        'eENS_11PolygonModeE',
        newPolygonMode.value,
    )

  @overload(int)
  def setStencilWriteMask(self, newStencilWriteMask: int) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::setStencilWriteMask(quint32
    newStencilWriteMask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html

    Parameters
    ----------

    newStencilWriteMask : int
      Passed on as it is.
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::setStencilWriteMask(
    #      quint32 newStencilWriteMask)
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride19setStencilWri'
        'teMaskEj',
        newStencilWriteMask,
    )

  @overload(int)
  def setStencilReference(self, newStencilReference: int) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::setStencilReference(quint32
    newStencilReference)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html

    Parameters
    ----------

    newStencilReference : int
      Passed on as it is.
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::setStencilReference(
    #      quint32 newStencilReference)
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride19setStencilRef'
        'erenceEj',
        newStencilReference,
    )

  @overload(QRectF)
  def setViewport(self, newViewport: QRectF) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::setViewport(const QRectF
    &newViewport)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html

    Parameters
    ----------

    newViewport : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::setViewport(const
    #      QRectF &newViewport)
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride11setViewportER'
        'K6QRectF',
        self._valueOf(newViewport),
    )

  @overload(QRect)
  def setScissor(self, newScissor: QRect) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::setScissor(const QRect
    &newScissor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html

    Parameters
    ----------

    newScissor : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::setScissor(const QRect
    #      &newScissor)
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride10setScissorERK'
        '5QRect',
        self._valueOf(newScissor),
    )

  @overload(QQuick3DRenderPassTargetBlend)
  def setTargetBlend0(
      self,
      newTargetBlend0: QQuick3DRenderPassTargetBlend,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::setTargetBlend0(const
    QQuick3DRenderPassTargetBlend &newTargetBlend0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html

    Parameters
    ----------

    newTargetBlend0 : QQuick3DRenderPassTargetBlend
      Passed on as a value: Qt reads the C++ QQuick3DRenderPassTargetBlend,
      which stays Python's own.
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::setTargetBlend0(const
    #      QQuick3DRenderPassTargetBlend &newTargetBlend0)
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride15setTargetBlen'
        'd0ERK29QQuick3DRenderPassTargetBlend',
        self._valueOf(newTargetBlend0),
    )

  @overload(QQuick3DRenderPassTargetBlend)
  def setTargetBlend1(
      self,
      newTargetBlend1: QQuick3DRenderPassTargetBlend,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::setTargetBlend1(const
    QQuick3DRenderPassTargetBlend &newTargetBlend1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html

    Parameters
    ----------

    newTargetBlend1 : QQuick3DRenderPassTargetBlend
      Passed on as a value: Qt reads the C++ QQuick3DRenderPassTargetBlend,
      which stays Python's own.
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::setTargetBlend1(const
    #      QQuick3DRenderPassTargetBlend &newTargetBlend1)
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride15setTargetBlen'
        'd1ERK29QQuick3DRenderPassTargetBlend',
        self._valueOf(newTargetBlend1),
    )

  @overload(QQuick3DRenderPassTargetBlend)
  def setTargetBlend2(
      self,
      newTargetBlend2: QQuick3DRenderPassTargetBlend,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::setTargetBlend2(const
    QQuick3DRenderPassTargetBlend &newTargetBlend2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html

    Parameters
    ----------

    newTargetBlend2 : QQuick3DRenderPassTargetBlend
      Passed on as a value: Qt reads the C++ QQuick3DRenderPassTargetBlend,
      which stays Python's own.
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::setTargetBlend2(const
    #      QQuick3DRenderPassTargetBlend &newTargetBlend2)
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride15setTargetBlen'
        'd2ERK29QQuick3DRenderPassTargetBlend',
        self._valueOf(newTargetBlend2),
    )

  @overload(QQuick3DRenderPassTargetBlend)
  def setTargetBlend3(
      self,
      newTargetBlend3: QQuick3DRenderPassTargetBlend,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::setTargetBlend3(const
    QQuick3DRenderPassTargetBlend &newTargetBlend3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html

    Parameters
    ----------

    newTargetBlend3 : QQuick3DRenderPassTargetBlend
      Passed on as a value: Qt reads the C++ QQuick3DRenderPassTargetBlend,
      which stays Python's own.
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::setTargetBlend3(const
    #      QQuick3DRenderPassTargetBlend &newTargetBlend3)
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride15setTargetBlen'
        'd3ERK29QQuick3DRenderPassTargetBlend',
        self._valueOf(newTargetBlend3),
    )

  @overload(QQuick3DRenderPassTargetBlend)
  def setTargetBlend4(
      self,
      newTargetBlend4: QQuick3DRenderPassTargetBlend,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::setTargetBlend4(const
    QQuick3DRenderPassTargetBlend &newTargetBlend4)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html

    Parameters
    ----------

    newTargetBlend4 : QQuick3DRenderPassTargetBlend
      Passed on as a value: Qt reads the C++ QQuick3DRenderPassTargetBlend,
      which stays Python's own.
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::setTargetBlend4(const
    #      QQuick3DRenderPassTargetBlend &newTargetBlend4)
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride15setTargetBlen'
        'd4ERK29QQuick3DRenderPassTargetBlend',
        self._valueOf(newTargetBlend4),
    )

  @overload(QQuick3DRenderPassTargetBlend)
  def setTargetBlend5(
      self,
      newTargetBlend5: QQuick3DRenderPassTargetBlend,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::setTargetBlend5(const
    QQuick3DRenderPassTargetBlend &newTargetBlend5)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html

    Parameters
    ----------

    newTargetBlend5 : QQuick3DRenderPassTargetBlend
      Passed on as a value: Qt reads the C++ QQuick3DRenderPassTargetBlend,
      which stays Python's own.
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::setTargetBlend5(const
    #      QQuick3DRenderPassTargetBlend &newTargetBlend5)
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride15setTargetBlen'
        'd5ERK29QQuick3DRenderPassTargetBlend',
        self._valueOf(newTargetBlend5),
    )

  @overload(QQuick3DRenderPassTargetBlend)
  def setTargetBlend6(
      self,
      newTargetBlend6: QQuick3DRenderPassTargetBlend,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::setTargetBlend6(const
    QQuick3DRenderPassTargetBlend &newTargetBlend6)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html

    Parameters
    ----------

    newTargetBlend6 : QQuick3DRenderPassTargetBlend
      Passed on as a value: Qt reads the C++ QQuick3DRenderPassTargetBlend,
      which stays Python's own.
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::setTargetBlend6(const
    #      QQuick3DRenderPassTargetBlend &newTargetBlend6)
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride15setTargetBlen'
        'd6ERK29QQuick3DRenderPassTargetBlend',
        self._valueOf(newTargetBlend6),
    )

  @overload(QQuick3DRenderPassTargetBlend)
  def setTargetBlend7(
      self,
      newTargetBlend7: QQuick3DRenderPassTargetBlend,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::setTargetBlend7(const
    QQuick3DRenderPassTargetBlend &newTargetBlend7)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html

    Parameters
    ----------

    newTargetBlend7 : QQuick3DRenderPassTargetBlend
      Passed on as a value: Qt reads the C++ QQuick3DRenderPassTargetBlend,
      which stays Python's own.
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::setTargetBlend7(const
    #      QQuick3DRenderPassTargetBlend &newTargetBlend7)
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride15setTargetBlen'
        'd7ERK29QQuick3DRenderPassTargetBlend',
        self._valueOf(newTargetBlend7),
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
    Notes what was given, for Qt's
    'QQuick3DShaderUtilsPipelineStateOverride::
    QQuick3DShaderUtilsPipelineStateOverride()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  QQuick3DShaderUtilsPipelineStateOverride::
    #      QQuick3DShaderUtilsPipelineStateOverride()
    self._noteCreation(
        QQuick3DShaderUtilsPipelineStateOverride, lambda: Rituals.call(
            'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverrideC1Ev',
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

  def resetDepthTestEnabled(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::resetDepthTestEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::resetDepthTestEnabled()
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride21resetDepthTes'
        'tEnabledEv',
    )

  def resetDepthWriteEnabled(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::resetDepthWriteEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  void
    #      QQuick3DShaderUtilsPipelineStateOverride::resetDepthWriteEnabled()
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride22resetDepthWri'
        'teEnabledEv',
    )

  def resetBlendEnabled(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::resetBlendEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::resetBlendEnabled()
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride17resetBlendEna'
        'bledEv',
    )

  def resetUsesStencilReference(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::resetUsesStencilReference()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::
    #      resetUsesStencilReference()
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride25resetUsesSten'
        'cilReferenceEv',
    )

  def resetUsesScissor(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::resetUsesScissor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::resetUsesScissor()
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride16resetUsesScis'
        'sorEv',
    )

  def resetDepthFunction(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::resetDepthFunction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::resetDepthFunction()
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride18resetDepthFun'
        'ctionEv',
    )

  def resetCullMode(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::resetCullMode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::resetCullMode()
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride13resetCullMode'
        'Ev',
    )

  def resetPolygonMode(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::resetPolygonMode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::resetPolygonMode()
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride16resetPolygonM'
        'odeEv',
    )

  def resetStencilWriteMask(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::resetStencilWriteMask()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::resetStencilWriteMask()
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride21resetStencilW'
        'riteMaskEv',
    )

  def resetStencilReference(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::resetStencilReference()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::resetStencilReference()
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride21resetStencilR'
        'eferenceEv',
    )

  def resetViewport(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::resetViewport()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::resetViewport()
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride13resetViewport'
        'Ev',
    )

  def resetScissor(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::resetScissor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::resetScissor()
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride12resetScissorE'
        'v',
    )

  def resetTargetBlend0(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::resetTargetBlend0()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::resetTargetBlend0()
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride17resetTargetBl'
        'end0Ev',
    )

  def resetTargetBlend1(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::resetTargetBlend1()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::resetTargetBlend1()
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride17resetTargetBl'
        'end1Ev',
    )

  def resetTargetBlend2(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::resetTargetBlend2()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::resetTargetBlend2()
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride17resetTargetBl'
        'end2Ev',
    )

  def resetTargetBlend3(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::resetTargetBlend3()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::resetTargetBlend3()
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride17resetTargetBl'
        'end3Ev',
    )

  def resetTargetBlend4(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::resetTargetBlend4()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::resetTargetBlend4()
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride17resetTargetBl'
        'end4Ev',
    )

  def resetTargetBlend5(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::resetTargetBlend5()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::resetTargetBlend5()
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride17resetTargetBl'
        'end5Ev',
    )

  def resetTargetBlend6(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::resetTargetBlend6()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::resetTargetBlend6()
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride17resetTargetBl'
        'end6Ev',
    )

  def resetTargetBlend7(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::resetTargetBlend7()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::resetTargetBlend7()
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride17resetTargetBl'
        'end7Ev',
    )

  def depthTestEnabledChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::depthTestEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  void
    #      QQuick3DShaderUtilsPipelineStateOverride::depthTestEnabledChanged(
    #      )
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride23depthTestEnab'
        'ledChangedEv',
    )

  def depthWriteEnabledChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::depthWriteEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::
    #      depthWriteEnabledChanged()
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride24depthWriteEna'
        'bledChangedEv',
    )

  def blendEnabledChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::blendEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::blendEnabledChanged()
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride19blendEnabledC'
        'hangedEv',
    )

  def usesStencilReferenceChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::usesStencilReferenceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::
    #      usesStencilReferenceChanged()
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride27usesStencilRe'
        'ferenceChangedEv',
    )

  def usesScissorChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::usesScissorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::usesScissorChanged()
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride18usesScissorCh'
        'angedEv',
    )

  def depthFunctionChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::depthFunctionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::depthFunctionChanged()
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride20depthFunction'
        'ChangedEv',
    )

  def cullModeChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::cullModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::cullModeChanged()
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride15cullModeChang'
        'edEv',
    )

  def polygonModeChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::polygonModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::polygonModeChanged()
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride18polygonModeCh'
        'angedEv',
    )

  def stencilWriteMaskChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::stencilWriteMaskChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  void
    #      QQuick3DShaderUtilsPipelineStateOverride::stencilWriteMaskChanged(
    #      )
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride23stencilWriteM'
        'askChangedEv',
    )

  def stencilReferenceChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::stencilReferenceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  void
    #      QQuick3DShaderUtilsPipelineStateOverride::stencilReferenceChanged(
    #      )
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride23stencilRefere'
        'nceChangedEv',
    )

  def viewportChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::viewportChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::viewportChanged()
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride15viewportChang'
        'edEv',
    )

  def scissorChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::scissorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::scissorChanged()
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride14scissorChange'
        'dEv',
    )

  def targetBlend0Changed(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::targetBlend0Changed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::targetBlend0Changed()
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride19targetBlend0C'
        'hangedEv',
    )

  def targetBlend1Changed(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::targetBlend1Changed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::targetBlend1Changed()
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride19targetBlend1C'
        'hangedEv',
    )

  def targetBlend2Changed(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::targetBlend2Changed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::targetBlend2Changed()
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride19targetBlend2C'
        'hangedEv',
    )

  def targetBlend3Changed(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::targetBlend3Changed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::targetBlend3Changed()
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride19targetBlend3C'
        'hangedEv',
    )

  def targetBlend4Changed(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::targetBlend4Changed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::targetBlend4Changed()
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride19targetBlend4C'
        'hangedEv',
    )

  def targetBlend5Changed(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::targetBlend5Changed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::targetBlend5Changed()
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride19targetBlend5C'
        'hangedEv',
    )

  def targetBlend6Changed(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::targetBlend6Changed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::targetBlend6Changed()
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride19targetBlend6C'
        'hangedEv',
    )

  def targetBlend7Changed(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsPipelineStateOverride::targetBlend7Changed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html
    """
    #  void QQuick3DShaderUtilsPipelineStateOverride::targetBlend7Changed()
    self.uglySide.call(
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride19targetBlend7C'
        'hangedEv',
    )

  def cloneCommand(self) -> Optional[QSSGCommand]:
    """
    Calls Qt's 'QSSGCommand
    *QQuick3DShaderUtilsPipelineStateOverride::cloneCommand()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilspipelinestateoverride.html

    Returns
    -------

    Optional[QSSGCommand]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGCommand *QQuick3DShaderUtilsPipelineStateOverride::cloneCommand()
    ritual = (
        'ritual_ZN40QQuick3DShaderUtilsPipelineStateOverride12cloneCommandE'
        'v')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN40QQuick3DShaderUtilsPipelineStateOverride12cloneCo'
          'mmandEv')
    address = self.uglySide.call(ritual)
    from ..QtQuick3DRuntimeRender import QSSGCommand
    return QSSGCommand._cuteAt(address)
