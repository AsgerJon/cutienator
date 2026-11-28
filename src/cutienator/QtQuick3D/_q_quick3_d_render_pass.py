"""
QQuick3DRenderPass binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3drenderpass_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DRenderPass to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QQuick3DObject, QQuick3DPropertyChangedTracker

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QMetaProperty, QUrl
  from ..QtGui import QColor
  from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
  from . import QQuick3DMaterial, QQuick3DSceneManager
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QMetaProperty = WAIT['QMetaProperty']
  QQuick3DMaterial = WAIT['QQuick3DMaterial']
  QQuick3DSceneManager = WAIT['QQuick3DSceneManager']
  QSSGRenderGraphObject = WAIT['QSSGRenderGraphObject']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DRenderPass(QQuick3DObject, QQuick3DPropertyChangedTracker):
  """
  The cute side of Qt's QQuick3DRenderPass: a plain Python object standing in
  front of one C++ QQuick3DRenderPass.

  It is built on the cute 'QQuick3DObject', as Qt's QQuick3DRenderPass is
  built on Qt's QQuick3DObject, and has everything that class has. It is
  built on the cute 'QQuick3DPropertyChangedTracker' as well, as Qt's
  QQuick3DRenderPass is built on Qt's QQuick3DPropertyChangedTracker too, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DRenderPass that has a ritual and that Python
  can call so far, 34 names in all: 'metaObject', 'tr', 'clearColor',
  'setClearColor', 'materialMode', 'setMaterialMode', 'overrideMaterial',
  'setOverrideMaterial', 'augmentShader', 'setAugmentShader', 'passMode',
  'setPassMode', 'depthClearValue', 'setDepthClearValue',
  'stencilClearValue', 'setStencilClearValue', 'markAllDirty',
  'renderTargetFlags', 'setRenderTargetFlags', 'outputChanged',
  'materialModeChanged', 'clearColorChanged', 'overrideMaterialChanged',
  'augmentShaderChanged', 'passModeChanged', 'depthClearValueChanged',
  'stencilClearValueChanged', 'renderTargetFlagsChanged',
  'updateSpatialNode', 'itemChange', 'markTrackedPropertyDirty',
  'onMaterialDestroyed', 'onCommandChanged', 'updateSceneManager'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DRenderPass::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuick3DRenderPass::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlListProperty<QQuick3DShaderUtilsRenderCommand>
    QQuick3DRenderPass::commands()': gives a type Python has no way to take
    yet.
  - Qt's 'void QQuick3DRenderPass::qmlAppendCommand(
    QQmlListProperty<QQuick3DShaderUtilsRenderCommand> *list,
    QQuick3DShaderUtilsRenderCommand *command)': names
    'QQmlListProperty<QQuick3DShaderUtilsRenderCommand>', which has no cute
    class yet.
  - Qt's 'QQuick3DShaderUtilsRenderCommand *QQuick3DRenderPass::qmlCommandAt(
    QQmlListProperty<QQuick3DShaderUtilsRenderCommand> *list, qsizetype
    index)': names 'QQmlListProperty<QQuick3DShaderUtilsRenderCommand>',
    which has no cute class yet.
  - Qt's 'qsizetype QQuick3DRenderPass::qmlCommandCount(
    QQmlListProperty<QQuick3DShaderUtilsRenderCommand> *list)': names
    'QQmlListProperty<QQuick3DShaderUtilsRenderCommand>', which has no cute
    class yet.
  - Qt's 'void QQuick3DRenderPass::qmlCommandClear(
    QQmlListProperty<QQuick3DShaderUtilsRenderCommand> *list)': names
    'QQmlListProperty<QQuick3DShaderUtilsRenderCommand>', which has no cute
    class yet.
  - Qt's 'void QQuick3DRenderPass::markDirty(QQuick3DRenderPass::Dirty type,
    bool requestSecondaryUpdate)': names the enum
    'QQuick3DRenderPass::Dirty', whose class cannot be named here.
  - Qt's 'void QQuick3DRenderPass::clearDirty(QQuick3DRenderPass::Dirty
    type)': names the enum 'QQuick3DRenderPass::Dirty', whose class cannot be
    named here.

  What has no ritual
  ------------------

  2 of the 46 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DRenderPass is created at the first use, not by
    'QQuick3DRenderPass(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DRenderPass.
  - Qt tells when it has removed the C++ QQuick3DRenderPass. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DRenderPass that has no cute function yet,
    'clearDirty', 'commands', 'markDirty', 'qmlAppendCommand',
    'qmlCommandAt', 'qmlCommandClear', 'qmlCommandCount', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuick3DRenderPass, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class MaterialModes(CuteNum):
    """
    The enum 'QQuick3DRenderPass::MaterialModes' of Qt, with the 3 names Qt
    gives in it.
    """

    OriginalMaterial = Kee[int](0)
    AugmentMaterial = Kee[int](1)
    OverrideMaterial = Kee[int](2)

  class PassMode(CuteNum):
    """
    The enum 'QQuick3DRenderPass::PassMode' of Qt, with the 3 names Qt gives
    in it.
    """

    UserPass = Kee[int](0)
    SkyboxPass = Kee[int](1)
    Item2DPass = Kee[int](2)

  class RenderTargetFlag(CuteFlags, scoped=True):
    """
    The flags enum 'QQuick3DRenderPass::RenderTargetFlag' of Qt, with the 4
    names Qt gives in it. Qt names the type of its combinations
    'QQuick3DRenderPass::RenderTargetFlags'. C++ keeps these names inside the
    enum, so the class that holds the enum does not have them.
    """

    NULL = 0x0
    PreserveColorContents = 0x1
    PreserveDepthStencilContents = 0x2
    DoNotStoreDepthStencilContents = 0x4

  RenderTargetFlags = RenderTargetFlag

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
    Calls Qt's 'QString QQuick3DRenderPass::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3drenderpass.html#tr

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
    #  QString QQuick3DRenderPass::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QQuick3DRenderPass2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DRenderPass'

  #  Qt's QQuick3DRenderPass is built on more than one class. The part of a
  #  C++ QQuick3DRenderPass that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQuick3DPropertyChangedTracker':
          'ritual_cast_QQuick3DRenderPass_QQuick3DPropertyChangedTracker',
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DRenderPass::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3drenderpass.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DRenderPass::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuick3DRenderPass10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def clearColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuick3DRenderPass::clearColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3drenderpass.html#clearColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuick3DRenderPass::clearColor() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuick3DRenderPass10clearColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def materialMode(self) -> MaterialModes:
    """
    Calls Qt's 'MaterialModes QQuick3DRenderPass::materialMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderpass.html#materialMode

    Returns
    -------

    MaterialModes
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'MaterialModes(number)'
      gives.
    """
    #  MaterialModes QQuick3DRenderPass::materialMode() const
    return QQuick3DRenderPass.MaterialModes(self.uglySide.call(
        'ritual_ZNK18QQuick3DRenderPass12materialModeEv',
    ))

  def overrideMaterial(self) -> Optional[QQuick3DMaterial]:
    """
    Calls Qt's 'QQuick3DMaterial *QQuick3DRenderPass::overrideMaterial()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderpass.html#overrideMaterial

    Returns
    -------

    Optional[QQuick3DMaterial]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DMaterial *QQuick3DRenderPass::overrideMaterial() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuick3DRenderPass16overrideMaterialEv',
    )
    from . import QQuick3DMaterial
    return QQuick3DMaterial._cuteAt(address)

  def augmentShader(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuick3DRenderPass::augmentShader() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderpass.html#augmentShader

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuick3DRenderPass::augmentShader() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuick3DRenderPass13augmentShaderEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def passMode(self) -> PassMode:
    """
    Calls Qt's 'PassMode QQuick3DRenderPass::passMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3drenderpass.html#passMode

    Returns
    -------

    PassMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'PassMode(number)' gives.
    """
    #  PassMode QQuick3DRenderPass::passMode() const
    return QQuick3DRenderPass.PassMode(self.uglySide.call(
        'ritual_ZNK18QQuick3DRenderPass8passModeEv',
    ))

  def depthClearValue(self) -> float:
    """
    Calls Qt's 'float QQuick3DRenderPass::depthClearValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderpass.html#depthClearValue
    """
    #  float QQuick3DRenderPass::depthClearValue() const
    return self.uglySide.call(
        'ritual_ZNK18QQuick3DRenderPass15depthClearValueEv',
    )

  def stencilClearValue(self) -> int:
    """
    Calls Qt's 'quint32 QQuick3DRenderPass::stencilClearValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderpass.html#stencilClearValue
    """
    #  quint32 QQuick3DRenderPass::stencilClearValue() const
    return self.uglySide.call(
        'ritual_ZNK18QQuick3DRenderPass17stencilClearValueEv',
    )

  def renderTargetFlags(self) -> RenderTargetFlags:
    """
    Calls Qt's 'RenderTargetFlags QQuick3DRenderPass::renderTargetFlags()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderpass.html#renderTargetFlags

    Returns
    -------

    RenderTargetFlags
      The value standing for the combination Qt gave back.
    """
    #  RenderTargetFlags QQuick3DRenderPass::renderTargetFlags() const
    return QQuick3DRenderPass.RenderTargetFlags(self.uglySide.call(
        'ritual_ZNK18QQuick3DRenderPass17renderTargetFlagsEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setClearColor(self, newClearColor: QColor) -> None:
    """
    Calls Qt's 'void QQuick3DRenderPass::setClearColor(const QColor
    &newClearColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderpass.html#setClearColor

    Parameters
    ----------

    newClearColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuick3DRenderPass::setClearColor(const QColor &newClearColor)
    self.uglySide.call(
        'ritual_ZN18QQuick3DRenderPass13setClearColorERK6QColor',
        self._valueOf(newClearColor),
    )

  @overload(MaterialModes)
  def setMaterialMode(self, newMaterialMode: MaterialModes) -> None:
    """
    Calls Qt's 'void QQuick3DRenderPass::setMaterialMode(MaterialModes
    newMaterialMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderpass.html#setMaterialMode

    Parameters
    ----------

    newMaterialMode : MaterialModes
      Passed on as its number.
    """
    #  void QQuick3DRenderPass::setMaterialMode(MaterialModes
    #      newMaterialMode)
    self.uglySide.call(
        'ritual_ZN18QQuick3DRenderPass15setMaterialModeENS_13MaterialModesE',
        newMaterialMode.value,
    )

  @overload(QQuick3DMaterial)
  @overload(NoneType)
  def setOverrideMaterial(
      self,
      newOverrideMaterial: Optional[QQuick3DMaterial],
  ) -> None:
    """
    Calls Qt's 'void QQuick3DRenderPass::setOverrideMaterial(QQuick3DMaterial
    *newOverrideMaterial)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderpass.html#setOverrideMaterial

    Parameters
    ----------

    newOverrideMaterial : Optional[QQuick3DMaterial]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DRenderPass::setOverrideMaterial(QQuick3DMaterial
    #      *newOverrideMaterial)
    self.uglySide.call(
        'ritual_ZN18QQuick3DRenderPass19setOverrideMaterialEP16QQuick3DMate'
        'rial',
        self._addressOf(newOverrideMaterial),
    )

  @overload(QUrl)
  def setAugmentShader(self, newAugmentShader: QUrl) -> None:
    """
    Calls Qt's 'void QQuick3DRenderPass::setAugmentShader(const QUrl
    &newAugmentShader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderpass.html#setAugmentShader

    Parameters
    ----------

    newAugmentShader : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuick3DRenderPass::setAugmentShader(const QUrl
    #      &newAugmentShader)
    self.uglySide.call(
        'ritual_ZN18QQuick3DRenderPass16setAugmentShaderERK4QUrl',
        self._valueOf(newAugmentShader),
    )

  @overload(PassMode)
  def setPassMode(self, newPassMode: PassMode) -> None:
    """
    Calls Qt's 'void QQuick3DRenderPass::setPassMode(PassMode newPassMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderpass.html#setPassMode

    Parameters
    ----------

    newPassMode : PassMode
      Passed on as its number.
    """
    #  void QQuick3DRenderPass::setPassMode(PassMode newPassMode)
    self.uglySide.call(
        'ritual_ZN18QQuick3DRenderPass11setPassModeENS_8PassModeE',
        newPassMode.value,
    )

  @overload(float)
  def setDepthClearValue(self, newDepthClearValue: float) -> None:
    """
    Calls Qt's 'void QQuick3DRenderPass::setDepthClearValue(float
    newDepthClearValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderpass.html#setDepthClearValue

    Parameters
    ----------

    newDepthClearValue : float
      Passed on as it is.
    """
    #  void QQuick3DRenderPass::setDepthClearValue(float newDepthClearValue)
    self.uglySide.call(
        'ritual_ZN18QQuick3DRenderPass18setDepthClearValueEf',
        newDepthClearValue,
    )

  @overload(int)
  def setStencilClearValue(self, newStencilClearValue: int) -> None:
    """
    Calls Qt's 'void QQuick3DRenderPass::setStencilClearValue(quint32
    newStencilClearValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderpass.html#setStencilClearValue

    Parameters
    ----------

    newStencilClearValue : int
      Passed on as it is.
    """
    #  void QQuick3DRenderPass::setStencilClearValue(quint32
    #      newStencilClearValue)
    self.uglySide.call(
        'ritual_ZN18QQuick3DRenderPass20setStencilClearValueEj',
        newStencilClearValue,
    )

  @overload(RenderTargetFlags)
  def setRenderTargetFlags(
      self,
      newRenderTargetFlags: RenderTargetFlags,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DRenderPass::setRenderTargetFlags(RenderTargetFlags
    newRenderTargetFlags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderpass.html#setRenderTargetFlags

    Parameters
    ----------

    newRenderTargetFlags : RenderTargetFlags
      Passed on as its number.
    """
    #  void QQuick3DRenderPass::setRenderTargetFlags(RenderTargetFlags
    #      newRenderTargetFlags)
    self.uglySide.call(
        'ritual_ZN18QQuick3DRenderPass20setRenderTargetFlagsE6QFlagsINS_16R'
        'enderTargetFlagEE',
        newRenderTargetFlags.value,
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
  @overload(QQuick3DObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuick3DObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DRenderPass::QQuick3DRenderPass(QQuick3DObject *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderpass.html#QQuick3DRenderPass

    Parameters
    ----------

    parent : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DRenderPass::QQuick3DRenderPass(QQuick3DObject *parent)
    self._noteCreation(QQuick3DRenderPass, lambda: Rituals.call(
        'ritual_ZN18QQuick3DRenderPassC1EP14QQuick3DObject',
        self._addressOf(parent),
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

  def markAllDirty(self) -> None:
    """
    Calls Qt's 'void QQuick3DRenderPass::markAllDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderpass.html#markAllDirty
    """
    #  void QQuick3DRenderPass::markAllDirty()
    ritual = 'ritual_ZN18QQuick3DRenderPass12markAllDirtyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuick3DRenderPass12markAllDirtyEv'
    self.uglySide.call(ritual)

  def outputChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRenderPass::outputChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderpass.html#outputChanged
    """
    #  void QQuick3DRenderPass::outputChanged()
    self.uglySide.call('ritual_ZN18QQuick3DRenderPass13outputChangedEv')

  def materialModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRenderPass::materialModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderpass.html#materialModeChanged
    """
    #  void QQuick3DRenderPass::materialModeChanged()
    self.uglySide.call(
        'ritual_ZN18QQuick3DRenderPass19materialModeChangedEv',
    )

  def clearColorChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRenderPass::clearColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderpass.html#clearColorChanged
    """
    #  void QQuick3DRenderPass::clearColorChanged()
    self.uglySide.call('ritual_ZN18QQuick3DRenderPass17clearColorChangedEv')

  def overrideMaterialChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRenderPass::overrideMaterialChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderpass.html#overrideMaterialChanged
    """
    #  void QQuick3DRenderPass::overrideMaterialChanged()
    self.uglySide.call(
        'ritual_ZN18QQuick3DRenderPass23overrideMaterialChangedEv',
    )

  def augmentShaderChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRenderPass::augmentShaderChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderpass.html#augmentShaderChanged
    """
    #  void QQuick3DRenderPass::augmentShaderChanged()
    self.uglySide.call(
        'ritual_ZN18QQuick3DRenderPass20augmentShaderChangedEv',
    )

  def passModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRenderPass::passModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderpass.html#passModeChanged
    """
    #  void QQuick3DRenderPass::passModeChanged()
    self.uglySide.call('ritual_ZN18QQuick3DRenderPass15passModeChangedEv')

  def depthClearValueChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRenderPass::depthClearValueChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderpass.html#depthClearValueChanged
    """
    #  void QQuick3DRenderPass::depthClearValueChanged()
    self.uglySide.call(
        'ritual_ZN18QQuick3DRenderPass22depthClearValueChangedEv',
    )

  def stencilClearValueChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRenderPass::stencilClearValueChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderpass.html#stencilClearValueChanged
    """
    #  void QQuick3DRenderPass::stencilClearValueChanged()
    self.uglySide.call(
        'ritual_ZN18QQuick3DRenderPass24stencilClearValueChangedEv',
    )

  def renderTargetFlagsChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRenderPass::renderTargetFlagsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderpass.html#renderTargetFlagsChanged
    """
    #  void QQuick3DRenderPass::renderTargetFlagsChanged()
    self.uglySide.call(
        'ritual_ZN18QQuick3DRenderPass24renderTargetFlagsChangedEv',
    )

  @overload(QSSGRenderGraphObject)
  @overload(NoneType)
  def updateSpatialNode(
      self,
      node: Optional[QSSGRenderGraphObject],
  ) -> Optional[QSSGRenderGraphObject]:
    """
    Calls Qt's 'QSSGRenderGraphObject
    *QQuick3DRenderPass::updateSpatialNode(QSSGRenderGraphObject *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderpass.html#updateSpatialNode

    Parameters
    ----------

    node : Optional[QSSGRenderGraphObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSSGRenderGraphObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGRenderGraphObject
    #      *QQuick3DRenderPass::updateSpatialNode(QSSGRenderGraphObject
    #      *node)
    ritual = (
        'ritual_ZN18QQuick3DRenderPass17updateSpatialNodeEP21QSSGRenderGrap'
        'hObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QQuick3DRenderPass17updateSpatialNodeEP21QSSGRend'
          'erGraphObject')
    address = self.uglySide.call(ritual, self._addressOf(node))
    from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
    return QSSGRenderGraphObject._cuteAt(address)

  @overload(QQuick3DObject.ItemChange, QQuick3DObject.ItemChangeData)
  def itemChange(
      self,
      a0: QQuick3DObject.ItemChange,
      a1: QQuick3DObject.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DRenderPass::itemChange(QQuick3DObject::ItemChange a0, const
    QQuick3DObject::ItemChangeData &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3drenderpass.html#itemChange

    Parameters
    ----------

    a0 : QQuick3DObject.ItemChange
      Passed on as its number.

    a1 : QQuick3DObject.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuick3DObject::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuick3DRenderPass::itemChange(QQuick3DObject::ItemChange a0,
    #      const QQuick3DObject::ItemChangeData &a1)
    ritual = (
        'ritual_ZN18QQuick3DRenderPass10itemChangeEN14QQuick3DObject10ItemC'
        'hangeERKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QQuick3DRenderPass10itemChangeEN14QQuick3DObject1'
          '0ItemChangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, a0.value, self._valueOf(a1))

  @overload(QMetaProperty, QQuick3DPropertyChangedTracker.DirtyPropertyHint)
  def markTrackedPropertyDirty(
      self,
      property: QMetaProperty,
      hint: QQuick3DPropertyChangedTracker.DirtyPropertyHint,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DRenderPass::markTrackedPropertyDirty(QMetaProperty property,
    QQuick3DPropertyChangedTracker::DirtyPropertyHint hint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderpass.html#markTrackedPropertyDirty

    Parameters
    ----------

    property : QMetaProperty
      Passed on as a value: Qt reads the C++ QMetaProperty, which stays
      Python's own.

    hint : QQuick3DPropertyChangedTracker.DirtyPropertyHint
      Passed on as its number.
    """
    #  void QQuick3DRenderPass::markTrackedPropertyDirty(QMetaProperty
    #      property, QQuick3DPropertyChangedTracker::DirtyPropertyHint hint)
    ritual = (
        'ritual_ZN18QQuick3DRenderPass24markTrackedPropertyDirtyE13QMetaPro'
        'pertyN30QQuick3DPropertyChangedTracker17DirtyPropertyHintE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QQuick3DRenderPass24markTrackedPropertyDirtyE13QM'
          'etaPropertyN30QQuick3DPropertyChangedTracker17DirtyPropertyHintE')
    self.uglySide.call(ritual, self._valueOf(property), hint.value)

  @overload(QObject)
  @overload(NoneType)
  def onMaterialDestroyed(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuick3DRenderPass::onMaterialDestroyed(QObject
    *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderpass.html#onMaterialDestroyed

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DRenderPass::onMaterialDestroyed(QObject *object)
    self.uglySide.call(
        'ritual_ZN18QQuick3DRenderPass19onMaterialDestroyedEP7QObject',
        self._addressOf(object, 'QObject'),
    )

  def onCommandChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRenderPass::onCommandChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderpass.html#onCommandChanged
    """
    #  void QQuick3DRenderPass::onCommandChanged()
    self.uglySide.call('ritual_ZN18QQuick3DRenderPass16onCommandChangedEv')

  @overload(QQuick3DSceneManager)
  @overload(NoneType)
  def updateSceneManager(
      self,
      sceneManager: Optional[QQuick3DSceneManager],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DRenderPass::updateSceneManager(QQuick3DSceneManager
    *sceneManager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderpass.html#updateSceneManager

    Parameters
    ----------

    sceneManager : Optional[QQuick3DSceneManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DRenderPass::updateSceneManager(QQuick3DSceneManager
    #      *sceneManager)
    self.uglySide.call(
        'ritual_ZN18QQuick3DRenderPass18updateSceneManagerEP20QQuick3DScene'
        'Manager',
        self._addressOf(sceneManager),
    )

  @staticmethod
  def clearDirty(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DRenderPass::clearDirty(QQuick3DRenderPass::Dirty
    type)': names the enum 'QQuick3DRenderPass::Dirty', whose class cannot be
    named here.
    """
    raise NotImplementedError(
        "'QQuick3DRenderPass.clearDirty' has no cute function yet. Qt's "
        "'void QQuick3DRenderPass::clearDirty(QQuick3DRenderPass::Dirty "
        "type)': names the enum 'QQuick3DRenderPass::Dirty', whose class "
        "cannot be named here.")

  @staticmethod
  def commands(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuick3DShaderUtilsRenderCommand>
    QQuick3DRenderPass::commands()': gives a type Python has no way to take
    yet.
    """
    raise NotImplementedError(
        "'QQuick3DRenderPass.commands' has no cute function yet. Qt's "
        "'QQmlListProperty<QQuick3DShaderUtilsRenderCommand> "
        "QQuick3DRenderPass::commands()': gives a type Python has no way to "
        "take yet.")

  @staticmethod
  def markDirty(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DRenderPass::markDirty(QQuick3DRenderPass::Dirty type,
    bool requestSecondaryUpdate)': names the enum
    'QQuick3DRenderPass::Dirty', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QQuick3DRenderPass.markDirty' has no cute function yet. Qt's "
        "'void QQuick3DRenderPass::markDirty(QQuick3DRenderPass::Dirty "
        "type, bool requestSecondaryUpdate)': names the enum "
        "'QQuick3DRenderPass::Dirty', whose class cannot be named here.")

  @staticmethod
  def qmlAppendCommand(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DRenderPass::qmlAppendCommand(
    QQmlListProperty<QQuick3DShaderUtilsRenderCommand> *list,
    QQuick3DShaderUtilsRenderCommand *command)': names
    'QQmlListProperty<QQuick3DShaderUtilsRenderCommand>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuick3DRenderPass.qmlAppendCommand' has no cute function yet. "
        "Qt's 'void "
        "QQuick3DRenderPass::qmlAppendCommand(QQmlListProperty<QQuick3DShade"
        "rUtilsRenderCommand> *list, QQuick3DShaderUtilsRenderCommand "
        "*command)': names "
        "'QQmlListProperty<QQuick3DShaderUtilsRenderCommand>', which has no "
        "cute class yet.")

  @staticmethod
  def qmlCommandAt(*__, **_) -> Never:
    """
    Qt's 'QQuick3DShaderUtilsRenderCommand *QQuick3DRenderPass::qmlCommandAt(
    QQmlListProperty<QQuick3DShaderUtilsRenderCommand> *list, qsizetype
    index)': names 'QQmlListProperty<QQuick3DShaderUtilsRenderCommand>',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuick3DRenderPass.qmlCommandAt' has no cute function yet. Qt's "
        "'QQuick3DShaderUtilsRenderCommand "
        "*QQuick3DRenderPass::qmlCommandAt(QQmlListProperty<QQuick3DShaderUt"
        "ilsRenderCommand> *list, qsizetype index)': names "
        "'QQmlListProperty<QQuick3DShaderUtilsRenderCommand>', which has no "
        "cute class yet.")

  @staticmethod
  def qmlCommandClear(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DRenderPass::qmlCommandClear(
    QQmlListProperty<QQuick3DShaderUtilsRenderCommand> *list)': names
    'QQmlListProperty<QQuick3DShaderUtilsRenderCommand>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuick3DRenderPass.qmlCommandClear' has no cute function yet. "
        "Qt's 'void "
        "QQuick3DRenderPass::qmlCommandClear(QQmlListProperty<QQuick3DShader"
        "UtilsRenderCommand> *list)': names "
        "'QQmlListProperty<QQuick3DShaderUtilsRenderCommand>', which has no "
        "cute class yet.")

  @staticmethod
  def qmlCommandCount(*__, **_) -> Never:
    """
    Qt's 'qsizetype QQuick3DRenderPass::qmlCommandCount(
    QQmlListProperty<QQuick3DShaderUtilsRenderCommand> *list)': names
    'QQmlListProperty<QQuick3DShaderUtilsRenderCommand>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuick3DRenderPass.qmlCommandCount' has no cute function yet. "
        "Qt's 'qsizetype "
        "QQuick3DRenderPass::qmlCommandCount(QQmlListProperty<QQuick3DShader"
        "UtilsRenderCommand> *list)': names "
        "'QQmlListProperty<QQuick3DShaderUtilsRenderCommand>', which has no "
        "cute class yet.")
