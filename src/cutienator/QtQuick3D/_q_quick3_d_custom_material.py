"""
QQuick3DCustomMaterial binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dcustommaterial_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DCustomMaterial to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QQuick3DMaterial, QQuick3DObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QUrl
  from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
  from . import QQuick3DShaderUtilsTextureInput
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuick3DShaderUtilsTextureInput = WAIT['QQuick3DShaderUtilsTextureInput']
  QSSGRenderGraphObject = WAIT['QSSGRenderGraphObject']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DCustomMaterial(QQuick3DMaterial):
  """
  The cute side of Qt's QQuick3DCustomMaterial: a plain Python object
  standing in front of one C++ QQuick3DCustomMaterial.

  It is built on the cute 'QQuick3DMaterial', as Qt's QQuick3DCustomMaterial
  is built on Qt's QQuick3DMaterial, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DCustomMaterial that has a ritual and that
  Python can call so far, 41 names in all: 'metaObject', 'tr', 'shadingMode',
  'vertexShader', 'fragmentShader', 'vertexShaderCode', 'fragmentShaderCode',
  'srcBlend', 'dstBlend', 'srcAlphaBlend', 'dstAlphaBlend', 'alwaysDirty',
  'lineWidth', 'setShadingMode', 'setVertexShader', 'setFragmentShader',
  'setVertexShaderCode', 'setFragmentShaderCode', 'setSrcBlend',
  'setDstBlend', 'setSrcAlphaBlend', 'setDstAlphaBlend', 'setAlwaysDirty',
  'setLineWidth', 'shadingModeChanged', 'vertexShaderChanged',
  'fragmentShaderChanged', 'vertexShaderCodeChanged',
  'fragmentShaderCodeChanged', 'srcBlendChanged', 'dstBlendChanged',
  'srcAlphaBlendChanged', 'dstAlphaBlendChanged', 'alwaysDirtyChanged',
  'lineWidthChanged', 'updateSpatialNode', 'itemChange', 'markAllDirty',
  'onPropertyDirty', 'onTextureDirty', 'setDynamicTextureMap'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DCustomMaterial::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuick3DCustomMaterial::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DCustomMaterial::~QQuick3DCustomMaterial()': the destructor:
    Python never removes a C++ QQuick3DCustomMaterial.
  - Qt's 'void QQuick3DCustomMaterial::markDirty(QQuick3DCustomMaterial
    &that, QQuick3DCustomMaterial::Dirty type)': takes a type Python has no
    way to hand over yet.

  What has no ritual
  ------------------

  2 of the 48 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DCustomMaterial is created at the first use, not by
    'QQuick3DCustomMaterial(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DCustomMaterial.
  - Qt tells when it has removed the C++ QQuick3DCustomMaterial. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DCustomMaterial that has no cute function yet,
    'markDirty', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QQuick3DCustomMaterial, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class BlendMode(CuteNum, scoped=True):
    """
    The enum 'QQuick3DCustomMaterial::BlendMode' of Qt, with the 16 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    NoBlend = Kee[int](0)
    Zero = Kee[int](1)
    One = Kee[int](2)
    SrcColor = Kee[int](3)
    OneMinusSrcColor = Kee[int](4)
    DstColor = Kee[int](5)
    OneMinusDstColor = Kee[int](6)
    SrcAlpha = Kee[int](7)
    OneMinusSrcAlpha = Kee[int](8)
    DstAlpha = Kee[int](9)
    OneMinusDstAlpha = Kee[int](10)
    ConstantColor = Kee[int](11)
    OneMinusConstantColor = Kee[int](12)
    ConstantAlpha = Kee[int](13)
    OneMinusConstantAlpha = Kee[int](14)
    SrcAlphaSaturate = Kee[int](15)

  class ShadingMode(CuteNum, scoped=True):
    """
    The enum 'QQuick3DCustomMaterial::ShadingMode' of Qt, with the 2 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Unshaded = Kee[int](0)
    Shaded = Kee[int](1)

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
    Calls Qt's 'QString QQuick3DCustomMaterial::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dcustommaterial.html#tr

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
    #  QString QQuick3DCustomMaterial::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN22QQuick3DCustomMaterial2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DCustomMaterial'

  #  A C++ QQuick3DCustomMaterial Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DCustomMaterial'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DCustomMaterial::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcustommaterial.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DCustomMaterial::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuick3DCustomMaterial10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def shadingMode(self) -> ShadingMode:
    """
    Calls Qt's 'ShadingMode QQuick3DCustomMaterial::shadingMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcustommaterial.html#shadingMode

    Returns
    -------

    ShadingMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ShadingMode(number)'
      gives.
    """
    #  ShadingMode QQuick3DCustomMaterial::shadingMode() const
    return QQuick3DCustomMaterial.ShadingMode(self.uglySide.call(
        'ritual_ZNK22QQuick3DCustomMaterial11shadingModeEv',
    ))

  def vertexShader(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuick3DCustomMaterial::vertexShader() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcustommaterial.html#vertexShader

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuick3DCustomMaterial::vertexShader() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuick3DCustomMaterial12vertexShaderEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def fragmentShader(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuick3DCustomMaterial::fragmentShader() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcustommaterial.html#fragmentShader

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuick3DCustomMaterial::fragmentShader() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuick3DCustomMaterial14fragmentShaderEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def vertexShaderCode(self) -> str:
    """
    Calls Qt's 'QString QQuick3DCustomMaterial::vertexShaderCode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcustommaterial.html#vertexShaderCode

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuick3DCustomMaterial::vertexShaderCode() const
    return self.uglySide.call(
        'ritual_ZNK22QQuick3DCustomMaterial16vertexShaderCodeEv',
    )

  def fragmentShaderCode(self) -> str:
    """
    Calls Qt's 'QString QQuick3DCustomMaterial::fragmentShaderCode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcustommaterial.html#fragmentShaderCode

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuick3DCustomMaterial::fragmentShaderCode() const
    return self.uglySide.call(
        'ritual_ZNK22QQuick3DCustomMaterial18fragmentShaderCodeEv',
    )

  def srcBlend(self) -> BlendMode:
    """
    Calls Qt's 'BlendMode QQuick3DCustomMaterial::srcBlend() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcustommaterial.html#srcBlend

    Returns
    -------

    BlendMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'BlendMode(number)' gives.
    """
    #  BlendMode QQuick3DCustomMaterial::srcBlend() const
    return QQuick3DCustomMaterial.BlendMode(self.uglySide.call(
        'ritual_ZNK22QQuick3DCustomMaterial8srcBlendEv',
    ))

  def dstBlend(self) -> BlendMode:
    """
    Calls Qt's 'BlendMode QQuick3DCustomMaterial::dstBlend() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcustommaterial.html#dstBlend

    Returns
    -------

    BlendMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'BlendMode(number)' gives.
    """
    #  BlendMode QQuick3DCustomMaterial::dstBlend() const
    return QQuick3DCustomMaterial.BlendMode(self.uglySide.call(
        'ritual_ZNK22QQuick3DCustomMaterial8dstBlendEv',
    ))

  def srcAlphaBlend(self) -> BlendMode:
    """
    Calls Qt's 'BlendMode QQuick3DCustomMaterial::srcAlphaBlend() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcustommaterial.html#srcAlphaBlend

    Returns
    -------

    BlendMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'BlendMode(number)' gives.
    """
    #  BlendMode QQuick3DCustomMaterial::srcAlphaBlend() const
    return QQuick3DCustomMaterial.BlendMode(self.uglySide.call(
        'ritual_ZNK22QQuick3DCustomMaterial13srcAlphaBlendEv',
    ))

  def dstAlphaBlend(self) -> BlendMode:
    """
    Calls Qt's 'BlendMode QQuick3DCustomMaterial::dstAlphaBlend() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcustommaterial.html#dstAlphaBlend

    Returns
    -------

    BlendMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'BlendMode(number)' gives.
    """
    #  BlendMode QQuick3DCustomMaterial::dstAlphaBlend() const
    return QQuick3DCustomMaterial.BlendMode(self.uglySide.call(
        'ritual_ZNK22QQuick3DCustomMaterial13dstAlphaBlendEv',
    ))

  def alwaysDirty(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DCustomMaterial::alwaysDirty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcustommaterial.html#alwaysDirty
    """
    #  bool QQuick3DCustomMaterial::alwaysDirty() const
    return self.uglySide.call(
        'ritual_ZNK22QQuick3DCustomMaterial11alwaysDirtyEv',
    )

  def lineWidth(self) -> float:
    """
    Calls Qt's 'float QQuick3DCustomMaterial::lineWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcustommaterial.html#lineWidth
    """
    #  float QQuick3DCustomMaterial::lineWidth() const
    return self.uglySide.call(
        'ritual_ZNK22QQuick3DCustomMaterial9lineWidthEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(ShadingMode)
  def setShadingMode(self, mode: ShadingMode) -> None:
    """
    Calls Qt's 'void
    QQuick3DCustomMaterial::setShadingMode(QQuick3DCustomMaterial::
    ShadingMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcustommaterial.html#setShadingMode

    Parameters
    ----------

    mode : ShadingMode
      Passed on as its number.
    """
    #  void QQuick3DCustomMaterial::setShadingMode(QQuick3DCustomMaterial::
    #      ShadingMode mode)
    self.uglySide.call(
        'ritual_ZN22QQuick3DCustomMaterial14setShadingModeENS_11ShadingMode'
        'E',
        mode.value,
    )

  @overload(QUrl)
  def setVertexShader(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QQuick3DCustomMaterial::setVertexShader(const QUrl
    &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcustommaterial.html#setVertexShader

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuick3DCustomMaterial::setVertexShader(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN22QQuick3DCustomMaterial15setVertexShaderERK4QUrl',
        self._valueOf(url),
    )

  @overload(QUrl)
  def setFragmentShader(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QQuick3DCustomMaterial::setFragmentShader(const QUrl
    &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcustommaterial.html#setFragmentShader

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuick3DCustomMaterial::setFragmentShader(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN22QQuick3DCustomMaterial17setFragmentShaderERK4QUrl',
        self._valueOf(url),
    )

  @overload(str)
  def setVertexShaderCode(self, code: str) -> None:
    """
    Calls Qt's 'void QQuick3DCustomMaterial::setVertexShaderCode(const
    QString &code)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcustommaterial.html#setVertexShaderCode

    Parameters
    ----------

    code : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuick3DCustomMaterial::setVertexShaderCode(const QString &code)
    self.uglySide.call(
        'ritual_ZN22QQuick3DCustomMaterial19setVertexShaderCodeERK7QString',
        code,
    )

  @overload(str)
  def setFragmentShaderCode(self, code: str) -> None:
    """
    Calls Qt's 'void QQuick3DCustomMaterial::setFragmentShaderCode(const
    QString &code)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcustommaterial.html#setFragmentShaderCode

    Parameters
    ----------

    code : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuick3DCustomMaterial::setFragmentShaderCode(const QString
    #      &code)
    self.uglySide.call(
        'ritual_ZN22QQuick3DCustomMaterial21setFragmentShaderCodeERK7QStrin'
        'g',
        code,
    )

  @overload(BlendMode)
  def setSrcBlend(self, mode: BlendMode) -> None:
    """
    Calls Qt's 'void
    QQuick3DCustomMaterial::setSrcBlend(QQuick3DCustomMaterial::BlendMode
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcustommaterial.html#setSrcBlend

    Parameters
    ----------

    mode : BlendMode
      Passed on as its number.
    """
    #  void QQuick3DCustomMaterial::setSrcBlend(QQuick3DCustomMaterial::
    #      BlendMode mode)
    self.uglySide.call(
        'ritual_ZN22QQuick3DCustomMaterial11setSrcBlendENS_9BlendModeE',
        mode.value,
    )

  @overload(BlendMode)
  def setDstBlend(self, mode: BlendMode) -> None:
    """
    Calls Qt's 'void
    QQuick3DCustomMaterial::setDstBlend(QQuick3DCustomMaterial::BlendMode
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcustommaterial.html#setDstBlend

    Parameters
    ----------

    mode : BlendMode
      Passed on as its number.
    """
    #  void QQuick3DCustomMaterial::setDstBlend(QQuick3DCustomMaterial::
    #      BlendMode mode)
    self.uglySide.call(
        'ritual_ZN22QQuick3DCustomMaterial11setDstBlendENS_9BlendModeE',
        mode.value,
    )

  @overload(BlendMode)
  def setSrcAlphaBlend(self, mode: BlendMode) -> None:
    """
    Calls Qt's 'void
    QQuick3DCustomMaterial::setSrcAlphaBlend(QQuick3DCustomMaterial::
    BlendMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcustommaterial.html#setSrcAlphaBlend

    Parameters
    ----------

    mode : BlendMode
      Passed on as its number.
    """
    #  void QQuick3DCustomMaterial::setSrcAlphaBlend(QQuick3DCustomMaterial::
    #      BlendMode mode)
    self.uglySide.call(
        'ritual_ZN22QQuick3DCustomMaterial16setSrcAlphaBlendENS_9BlendModeE',
        mode.value,
    )

  @overload(BlendMode)
  def setDstAlphaBlend(self, mode: BlendMode) -> None:
    """
    Calls Qt's 'void
    QQuick3DCustomMaterial::setDstAlphaBlend(QQuick3DCustomMaterial::
    BlendMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcustommaterial.html#setDstAlphaBlend

    Parameters
    ----------

    mode : BlendMode
      Passed on as its number.
    """
    #  void QQuick3DCustomMaterial::setDstAlphaBlend(QQuick3DCustomMaterial::
    #      BlendMode mode)
    self.uglySide.call(
        'ritual_ZN22QQuick3DCustomMaterial16setDstAlphaBlendENS_9BlendModeE',
        mode.value,
    )

  @overload(bool)
  def setAlwaysDirty(self, alwaysDirty: bool) -> None:
    """
    Calls Qt's 'void QQuick3DCustomMaterial::setAlwaysDirty(bool
    alwaysDirty)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcustommaterial.html#setAlwaysDirty

    Parameters
    ----------

    alwaysDirty : bool
      Passed on as it is.
    """
    #  void QQuick3DCustomMaterial::setAlwaysDirty(bool alwaysDirty)
    self.uglySide.call(
        'ritual_ZN22QQuick3DCustomMaterial14setAlwaysDirtyEb', alwaysDirty,
    )

  @overload(float)
  def setLineWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QQuick3DCustomMaterial::setLineWidth(float width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcustommaterial.html#setLineWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QQuick3DCustomMaterial::setLineWidth(float width)
    self.uglySide.call(
        'ritual_ZN22QQuick3DCustomMaterial12setLineWidthEf', width,
    )

  @overload(QQuick3DShaderUtilsTextureInput)
  @overload(NoneType)
  def setDynamicTextureMap(
      self,
      textureMap: Optional[QQuick3DShaderUtilsTextureInput],
  ) -> None:
    """
    Calls Qt's 'void QQuick3DCustomMaterial::setDynamicTextureMap(
    QQuick3DShaderUtilsTextureInput *textureMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcustommaterial.html#setDynamicTextureMap

    Parameters
    ----------

    textureMap : Optional[QQuick3DShaderUtilsTextureInput]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DCustomMaterial::setDynamicTextureMap(
    #      QQuick3DShaderUtilsTextureInput *textureMap)
    self.uglySide.call(
        'ritual_ZN22QQuick3DCustomMaterial20setDynamicTextureMapEP31QQuick3'
        'DShaderUtilsTextureInput',
        self._addressOf(textureMap),
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
    'QQuick3DCustomMaterial::QQuick3DCustomMaterial(QQuick3DObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcustommaterial.html#QQuick3DCustomMaterial

    Parameters
    ----------

    parent : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DCustomMaterial::QQuick3DCustomMaterial(QQuick3DObject *parent)
    self._noteCreation(QQuick3DCustomMaterial, lambda: Rituals.call(
        'ritual_ZN22QQuick3DCustomMaterialC1EP14QQuick3DObject',
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

  def shadingModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DCustomMaterial::shadingModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcustommaterial.html#shadingModeChanged
    """
    #  void QQuick3DCustomMaterial::shadingModeChanged()
    self.uglySide.call(
        'ritual_ZN22QQuick3DCustomMaterial18shadingModeChangedEv',
    )

  def vertexShaderChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DCustomMaterial::vertexShaderChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcustommaterial.html#vertexShaderChanged
    """
    #  void QQuick3DCustomMaterial::vertexShaderChanged()
    self.uglySide.call(
        'ritual_ZN22QQuick3DCustomMaterial19vertexShaderChangedEv',
    )

  def fragmentShaderChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DCustomMaterial::fragmentShaderChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcustommaterial.html#fragmentShaderChanged
    """
    #  void QQuick3DCustomMaterial::fragmentShaderChanged()
    self.uglySide.call(
        'ritual_ZN22QQuick3DCustomMaterial21fragmentShaderChangedEv',
    )

  def vertexShaderCodeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DCustomMaterial::vertexShaderCodeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcustommaterial.html
    """
    #  void QQuick3DCustomMaterial::vertexShaderCodeChanged()
    self.uglySide.call(
        'ritual_ZN22QQuick3DCustomMaterial23vertexShaderCodeChangedEv',
    )

  def fragmentShaderCodeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DCustomMaterial::fragmentShaderCodeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcustommaterial.html
    """
    #  void QQuick3DCustomMaterial::fragmentShaderCodeChanged()
    self.uglySide.call(
        'ritual_ZN22QQuick3DCustomMaterial25fragmentShaderCodeChangedEv',
    )

  def srcBlendChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DCustomMaterial::srcBlendChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcustommaterial.html#srcBlendChanged
    """
    #  void QQuick3DCustomMaterial::srcBlendChanged()
    self.uglySide.call(
        'ritual_ZN22QQuick3DCustomMaterial15srcBlendChangedEv',
    )

  def dstBlendChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DCustomMaterial::dstBlendChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcustommaterial.html#dstBlendChanged
    """
    #  void QQuick3DCustomMaterial::dstBlendChanged()
    self.uglySide.call(
        'ritual_ZN22QQuick3DCustomMaterial15dstBlendChangedEv',
    )

  def srcAlphaBlendChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DCustomMaterial::srcAlphaBlendChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcustommaterial.html#srcAlphaBlendChanged
    """
    #  void QQuick3DCustomMaterial::srcAlphaBlendChanged()
    self.uglySide.call(
        'ritual_ZN22QQuick3DCustomMaterial20srcAlphaBlendChangedEv',
    )

  def dstAlphaBlendChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DCustomMaterial::dstAlphaBlendChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcustommaterial.html#dstAlphaBlendChanged
    """
    #  void QQuick3DCustomMaterial::dstAlphaBlendChanged()
    self.uglySide.call(
        'ritual_ZN22QQuick3DCustomMaterial20dstAlphaBlendChangedEv',
    )

  def alwaysDirtyChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DCustomMaterial::alwaysDirtyChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcustommaterial.html#alwaysDirtyChanged
    """
    #  void QQuick3DCustomMaterial::alwaysDirtyChanged()
    self.uglySide.call(
        'ritual_ZN22QQuick3DCustomMaterial18alwaysDirtyChangedEv',
    )

  def lineWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DCustomMaterial::lineWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcustommaterial.html#lineWidthChanged
    """
    #  void QQuick3DCustomMaterial::lineWidthChanged()
    self.uglySide.call(
        'ritual_ZN22QQuick3DCustomMaterial16lineWidthChangedEv',
    )

  @overload(QSSGRenderGraphObject)
  @overload(NoneType)
  def updateSpatialNode(
      self,
      node: Optional[QSSGRenderGraphObject],
  ) -> Optional[QSSGRenderGraphObject]:
    """
    Calls Qt's 'QSSGRenderGraphObject
    *QQuick3DCustomMaterial::updateSpatialNode(QSSGRenderGraphObject *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcustommaterial.html#updateSpatialNode

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
    #      *QQuick3DCustomMaterial::updateSpatialNode(QSSGRenderGraphObject
    #      *node)
    ritual = (
        'ritual_ZN22QQuick3DCustomMaterial17updateSpatialNodeEP21QSSGRender'
        'GraphObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuick3DCustomMaterial17updateSpatialNodeEP21QSSG'
          'RenderGraphObject')
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
    Calls Qt's 'void QQuick3DCustomMaterial::itemChange(ItemChange a0, const
    ItemChangeData &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcustommaterial.html#itemChange

    Parameters
    ----------

    a0 : QQuick3DObject.ItemChange
      Passed on as its number.

    a1 : QQuick3DObject.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuick3DObject::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuick3DCustomMaterial::itemChange(ItemChange a0, const
    #      ItemChangeData &a1)
    ritual = (
        'ritual_ZN22QQuick3DCustomMaterial10itemChangeEN14QQuick3DObject10I'
        'temChangeERKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuick3DCustomMaterial10itemChangeEN14QQuick3DObj'
          'ect10ItemChangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, a0.value, self._valueOf(a1))

  def markAllDirty(self) -> None:
    """
    Calls Qt's 'void QQuick3DCustomMaterial::markAllDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcustommaterial.html#markAllDirty
    """
    #  void QQuick3DCustomMaterial::markAllDirty()
    ritual = 'ritual_ZN22QQuick3DCustomMaterial12markAllDirtyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuick3DCustomMaterial12markAllDirtyEv'
    self.uglySide.call(ritual)

  def onPropertyDirty(self) -> None:
    """
    Calls Qt's 'void QQuick3DCustomMaterial::onPropertyDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcustommaterial.html#onPropertyDirty
    """
    #  void QQuick3DCustomMaterial::onPropertyDirty()
    self.uglySide.call(
        'ritual_ZN22QQuick3DCustomMaterial15onPropertyDirtyEv',
    )

  def onTextureDirty(self) -> None:
    """
    Calls Qt's 'void QQuick3DCustomMaterial::onTextureDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dcustommaterial.html#onTextureDirty
    """
    #  void QQuick3DCustomMaterial::onTextureDirty()
    self.uglySide.call('ritual_ZN22QQuick3DCustomMaterial14onTextureDirtyEv')

  @staticmethod
  def markDirty(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DCustomMaterial::markDirty(QQuick3DCustomMaterial
    &that, QQuick3DCustomMaterial::Dirty type)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuick3DCustomMaterial.markDirty' has no cute function yet. Qt's "
        "'void QQuick3DCustomMaterial::markDirty(QQuick3DCustomMaterial "
        "&that, QQuick3DCustomMaterial::Dirty type)': takes a type Python "
        "has no way to hand over yet.")
