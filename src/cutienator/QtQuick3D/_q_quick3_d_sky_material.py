"""
QQuick3DSkyMaterial binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dskymaterial_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DSkyMaterial to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QQuick3DObject, QQuick3DPropertyChangedTracker

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QMetaProperty, QUrl
  from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaProperty = WAIT['QMetaProperty']
  QSSGRenderGraphObject = WAIT['QSSGRenderGraphObject']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DSkyMaterial(QQuick3DObject, QQuick3DPropertyChangedTracker):
  """
  The cute side of Qt's QQuick3DSkyMaterial: a plain Python object standing
  in front of one C++ QQuick3DSkyMaterial.

  It is built on the cute 'QQuick3DObject', as Qt's QQuick3DSkyMaterial is
  built on Qt's QQuick3DObject, and has everything that class has. It is
  built on the cute 'QQuick3DPropertyChangedTracker' as well, as Qt's
  QQuick3DSkyMaterial is built on Qt's QQuick3DPropertyChangedTracker too,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DSkyMaterial that has a ritual and that
  Python can call so far, 25 names in all: 'metaObject', 'tr',
  'radianceMapSize', 'fragmentShader', 'enableIBL', 'fragmentShaderCode',
  'iblSampleCount', 'iblRenderFrames', 'skyboxMode', 'setRadianceMapSize',
  'setFragmentShader', 'setFragmentShaderCode', 'setEnableIBL',
  'setIblSampleCount', 'setIblRenderFrames', 'setSkyboxMode',
  'radianceMapSizeChanged', 'fragmentShaderChanged',
  'fragmentShaderCodeChanged', 'enableIBLChanged', 'iblSampleCountChanged',
  'iblRenderFramesChanged', 'skyboxModeChanged', 'updateSpatialNode',
  'markTrackedPropertyDirty'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DSkyMaterial::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuick3DSkyMaterial::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuick3DSkyMaterial::markDirty(Dirty v)': names the enum
    'QQuick3DSkyMaterial::Dirty', whose class cannot be named here.

  What has no ritual
  ------------------

  2 of the 31 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DSkyMaterial is created at the first use, not by
    'QQuick3DSkyMaterial(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DSkyMaterial.
  - Qt tells when it has removed the C++ QQuick3DSkyMaterial. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DSkyMaterial that has no cute function yet,
    'markDirty', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QQuick3DSkyMaterial, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class SkyboxMode(CuteNum, scoped=True):
    """
    The enum 'QQuick3DSkyMaterial::SkyboxMode' of Qt, with the 4 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Cubemap = Kee[int](0)
    ScreenSpaceFull = Kee[int](1)
    ScreenSpaceHalf = Kee[int](2)
    ScreenSpaceQuarter = Kee[int](3)

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
    Calls Qt's 'QString QQuick3DSkyMaterial::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dskymaterial.html#tr

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
    #  QString QQuick3DSkyMaterial::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QQuick3DSkyMaterial2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DSkyMaterial'

  #  Qt's QQuick3DSkyMaterial is built on more than one class. The part of a
  #  C++ QQuick3DSkyMaterial that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQuick3DPropertyChangedTracker':
          'ritual_cast_QQuick3DSkyMaterial_QQuick3DPropertyChangedTracker',
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
    Calls Qt's 'const QMetaObject *QQuick3DSkyMaterial::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dskymaterial.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DSkyMaterial::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuick3DSkyMaterial10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def radianceMapSize(self) -> int:
    """
    Calls Qt's 'int QQuick3DSkyMaterial::radianceMapSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dskymaterial.html#radianceMapSize
    """
    #  int QQuick3DSkyMaterial::radianceMapSize() const
    return self.uglySide.call(
        'ritual_ZNK19QQuick3DSkyMaterial15radianceMapSizeEv',
    )

  def fragmentShader(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuick3DSkyMaterial::fragmentShader() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dskymaterial.html#fragmentShader

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuick3DSkyMaterial::fragmentShader() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuick3DSkyMaterial14fragmentShaderEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def enableIBL(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DSkyMaterial::enableIBL() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dskymaterial.html#enableIBL
    """
    #  bool QQuick3DSkyMaterial::enableIBL() const
    return self.uglySide.call('ritual_ZNK19QQuick3DSkyMaterial9enableIBLEv')

  def fragmentShaderCode(self) -> str:
    """
    Calls Qt's 'QString QQuick3DSkyMaterial::fragmentShaderCode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dskymaterial.html#fragmentShaderCode

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuick3DSkyMaterial::fragmentShaderCode() const
    return self.uglySide.call(
        'ritual_ZNK19QQuick3DSkyMaterial18fragmentShaderCodeEv',
    )

  def iblSampleCount(self) -> int:
    """
    Calls Qt's 'int QQuick3DSkyMaterial::iblSampleCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dskymaterial.html#iblSampleCount
    """
    #  int QQuick3DSkyMaterial::iblSampleCount() const
    return self.uglySide.call(
        'ritual_ZNK19QQuick3DSkyMaterial14iblSampleCountEv',
    )

  def iblRenderFrames(self) -> int:
    """
    Calls Qt's 'int QQuick3DSkyMaterial::iblRenderFrames() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dskymaterial.html#iblRenderFrames
    """
    #  int QQuick3DSkyMaterial::iblRenderFrames() const
    return self.uglySide.call(
        'ritual_ZNK19QQuick3DSkyMaterial15iblRenderFramesEv',
    )

  def skyboxMode(self) -> SkyboxMode:
    """
    Calls Qt's 'SkyboxMode QQuick3DSkyMaterial::skyboxMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dskymaterial.html#skyboxMode

    Returns
    -------

    SkyboxMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SkyboxMode(number)'
      gives.
    """
    #  SkyboxMode QQuick3DSkyMaterial::skyboxMode() const
    return QQuick3DSkyMaterial.SkyboxMode(self.uglySide.call(
        'ritual_ZNK19QQuick3DSkyMaterial10skyboxModeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setRadianceMapSize(self, radianceMapSize: int) -> None:
    """
    Calls Qt's 'void QQuick3DSkyMaterial::setRadianceMapSize(int
    radianceMapSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dskymaterial.html#setRadianceMapSize

    Parameters
    ----------

    radianceMapSize : int
      Passed on as it is.
    """
    #  void QQuick3DSkyMaterial::setRadianceMapSize(int radianceMapSize)
    self.uglySide.call(
        'ritual_ZN19QQuick3DSkyMaterial18setRadianceMapSizeEi',
        radianceMapSize,
    )

  @overload(QUrl)
  def setFragmentShader(self, newFragmentShader: QUrl) -> None:
    """
    Calls Qt's 'void QQuick3DSkyMaterial::setFragmentShader(const QUrl
    &newFragmentShader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dskymaterial.html#setFragmentShader

    Parameters
    ----------

    newFragmentShader : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuick3DSkyMaterial::setFragmentShader(const QUrl
    #      &newFragmentShader)
    self.uglySide.call(
        'ritual_ZN19QQuick3DSkyMaterial17setFragmentShaderERK4QUrl',
        self._valueOf(newFragmentShader),
    )

  @overload(str)
  def setFragmentShaderCode(self, newFragmentShaderCode: str) -> None:
    """
    Calls Qt's 'void QQuick3DSkyMaterial::setFragmentShaderCode(const QString
    &newFragmentShaderCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dskymaterial.html#setFragmentShaderCode

    Parameters
    ----------

    newFragmentShaderCode : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuick3DSkyMaterial::setFragmentShaderCode(const QString
    #      &newFragmentShaderCode)
    self.uglySide.call(
        'ritual_ZN19QQuick3DSkyMaterial21setFragmentShaderCodeERK7QString',
        newFragmentShaderCode,
    )

  @overload(bool)
  def setEnableIBL(self, newEnableIBL: bool) -> None:
    """
    Calls Qt's 'void QQuick3DSkyMaterial::setEnableIBL(bool newEnableIBL)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dskymaterial.html#setEnableIBL

    Parameters
    ----------

    newEnableIBL : bool
      Passed on as it is.
    """
    #  void QQuick3DSkyMaterial::setEnableIBL(bool newEnableIBL)
    self.uglySide.call(
        'ritual_ZN19QQuick3DSkyMaterial12setEnableIBLEb', newEnableIBL,
    )

  @overload(int)
  def setIblSampleCount(self, newIblSampleCount: int) -> None:
    """
    Calls Qt's 'void QQuick3DSkyMaterial::setIblSampleCount(int
    newIblSampleCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dskymaterial.html#setIblSampleCount

    Parameters
    ----------

    newIblSampleCount : int
      Passed on as it is.
    """
    #  void QQuick3DSkyMaterial::setIblSampleCount(int newIblSampleCount)
    self.uglySide.call(
        'ritual_ZN19QQuick3DSkyMaterial17setIblSampleCountEi',
        newIblSampleCount,
    )

  @overload(int)
  def setIblRenderFrames(self, newIblRenderFrames: int) -> None:
    """
    Calls Qt's 'void QQuick3DSkyMaterial::setIblRenderFrames(int
    newIblRenderFrames)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dskymaterial.html#setIblRenderFrames

    Parameters
    ----------

    newIblRenderFrames : int
      Passed on as it is.
    """
    #  void QQuick3DSkyMaterial::setIblRenderFrames(int newIblRenderFrames)
    self.uglySide.call(
        'ritual_ZN19QQuick3DSkyMaterial18setIblRenderFramesEi',
        newIblRenderFrames,
    )

  @overload(SkyboxMode)
  def setSkyboxMode(self, skyboxMode: SkyboxMode) -> None:
    """
    Calls Qt's 'void QQuick3DSkyMaterial::setSkyboxMode(SkyboxMode
    skyboxMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dskymaterial.html#setSkyboxMode

    Parameters
    ----------

    skyboxMode : SkyboxMode
      Passed on as its number.
    """
    #  void QQuick3DSkyMaterial::setSkyboxMode(SkyboxMode skyboxMode)
    self.uglySide.call(
        'ritual_ZN19QQuick3DSkyMaterial13setSkyboxModeENS_10SkyboxModeE',
        skyboxMode.value,
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
    'QQuick3DSkyMaterial::QQuick3DSkyMaterial(QQuick3DObject *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dskymaterial.html#QQuick3DSkyMaterial

    Parameters
    ----------

    parent : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DSkyMaterial::QQuick3DSkyMaterial(QQuick3DObject *parent)
    self._noteCreation(QQuick3DSkyMaterial, lambda: Rituals.call(
        'ritual_ZN19QQuick3DSkyMaterialC1EP14QQuick3DObject',
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

  def radianceMapSizeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSkyMaterial::radianceMapSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dskymaterial.html#radianceMapSizeChanged
    """
    #  void QQuick3DSkyMaterial::radianceMapSizeChanged()
    self.uglySide.call(
        'ritual_ZN19QQuick3DSkyMaterial22radianceMapSizeChangedEv',
    )

  def fragmentShaderChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSkyMaterial::fragmentShaderChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dskymaterial.html#fragmentShaderChanged
    """
    #  void QQuick3DSkyMaterial::fragmentShaderChanged()
    self.uglySide.call(
        'ritual_ZN19QQuick3DSkyMaterial21fragmentShaderChangedEv',
    )

  def fragmentShaderCodeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSkyMaterial::fragmentShaderCodeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dskymaterial.html#fragmentShaderCodeChanged
    """
    #  void QQuick3DSkyMaterial::fragmentShaderCodeChanged()
    self.uglySide.call(
        'ritual_ZN19QQuick3DSkyMaterial25fragmentShaderCodeChangedEv',
    )

  def enableIBLChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSkyMaterial::enableIBLChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dskymaterial.html#enableIBLChanged
    """
    #  void QQuick3DSkyMaterial::enableIBLChanged()
    self.uglySide.call('ritual_ZN19QQuick3DSkyMaterial16enableIBLChangedEv')

  def iblSampleCountChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSkyMaterial::iblSampleCountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dskymaterial.html#iblSampleCountChanged
    """
    #  void QQuick3DSkyMaterial::iblSampleCountChanged()
    self.uglySide.call(
        'ritual_ZN19QQuick3DSkyMaterial21iblSampleCountChangedEv',
    )

  def iblRenderFramesChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSkyMaterial::iblRenderFramesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dskymaterial.html#iblRenderFramesChanged
    """
    #  void QQuick3DSkyMaterial::iblRenderFramesChanged()
    self.uglySide.call(
        'ritual_ZN19QQuick3DSkyMaterial22iblRenderFramesChangedEv',
    )

  def skyboxModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSkyMaterial::skyboxModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dskymaterial.html#skyboxModeChanged
    """
    #  void QQuick3DSkyMaterial::skyboxModeChanged()
    self.uglySide.call('ritual_ZN19QQuick3DSkyMaterial17skyboxModeChangedEv')

  @overload(QSSGRenderGraphObject)
  @overload(NoneType)
  def updateSpatialNode(
      self,
      node: Optional[QSSGRenderGraphObject],
  ) -> Optional[QSSGRenderGraphObject]:
    """
    Calls Qt's 'QSSGRenderGraphObject
    *QQuick3DSkyMaterial::updateSpatialNode(QSSGRenderGraphObject *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dskymaterial.html#updateSpatialNode

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
    #      *QQuick3DSkyMaterial::updateSpatialNode(QSSGRenderGraphObject
    #      *node)
    ritual = (
        'ritual_ZN19QQuick3DSkyMaterial17updateSpatialNodeEP21QSSGRenderGra'
        'phObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuick3DSkyMaterial17updateSpatialNodeEP21QSSGRen'
          'derGraphObject')
    address = self.uglySide.call(ritual, self._addressOf(node))
    from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
    return QSSGRenderGraphObject._cuteAt(address)

  @overload(QMetaProperty, QQuick3DPropertyChangedTracker.DirtyPropertyHint)
  def markTrackedPropertyDirty(
      self,
      property: QMetaProperty,
      hint: QQuick3DPropertyChangedTracker.DirtyPropertyHint,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DSkyMaterial::markTrackedPropertyDirty(QMetaProperty property,
    DirtyPropertyHint hint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dskymaterial.html#markTrackedPropertyDirty

    Parameters
    ----------

    property : QMetaProperty
      Passed on as a value: Qt reads the C++ QMetaProperty, which stays
      Python's own.

    hint : QQuick3DPropertyChangedTracker.DirtyPropertyHint
      Passed on as its number.
    """
    #  void QQuick3DSkyMaterial::markTrackedPropertyDirty(QMetaProperty
    #      property, DirtyPropertyHint hint)
    ritual = (
        'ritual_ZN19QQuick3DSkyMaterial24markTrackedPropertyDirtyE13QMetaPr'
        'opertyN30QQuick3DPropertyChangedTracker17DirtyPropertyHintE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuick3DSkyMaterial24markTrackedPropertyDirtyE13Q'
          'MetaPropertyN30QQuick3DPropertyChangedTracker17DirtyPropertyHint'
          'E')
    self.uglySide.call(ritual, self._valueOf(property), hint.value)

  @staticmethod
  def markDirty(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DSkyMaterial::markDirty(Dirty v)': names the enum
    'QQuick3DSkyMaterial::Dirty', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QQuick3DSkyMaterial.markDirty' has no cute function yet. Qt's "
        "'void QQuick3DSkyMaterial::markDirty(Dirty v)': names the enum "
        "'QQuick3DSkyMaterial::Dirty', whose class cannot be named here.")
