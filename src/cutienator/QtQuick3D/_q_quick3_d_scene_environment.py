"""
QQuick3DSceneEnvironment binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dsceneenvironment_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DSceneEnvironment to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QQuick3DObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QRect
  from ..QtGui import QColor, QVector3D
  from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
  from . import QQuick3DCubeMapTexture, QQuick3DDebugSettings, QQuick3DFog
  from . import QQuick3DLightmapper, QQuick3DSceneManager
  from . import QQuick3DSkyMaterial, QQuick3DTexture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QQuick3DCubeMapTexture = WAIT['QQuick3DCubeMapTexture']
  QQuick3DDebugSettings = WAIT['QQuick3DDebugSettings']
  QQuick3DFog = WAIT['QQuick3DFog']
  QQuick3DLightmapper = WAIT['QQuick3DLightmapper']
  QQuick3DSceneManager = WAIT['QQuick3DSceneManager']
  QQuick3DSkyMaterial = WAIT['QQuick3DSkyMaterial']
  QQuick3DTexture = WAIT['QQuick3DTexture']
  QRect = WAIT['QRect']
  QSSGRenderGraphObject = WAIT['QSSGRenderGraphObject']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DSceneEnvironment(QQuick3DObject):
  """
  The cute side of Qt's QQuick3DSceneEnvironment: a plain Python object
  standing in front of one C++ QQuick3DSceneEnvironment.

  It is built on the cute 'QQuick3DObject', as Qt's QQuick3DSceneEnvironment
  is built on Qt's QQuick3DObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DSceneEnvironment that has a ritual and that
  Python can call so far, 102 names in all: 'metaObject', 'tr',
  'antialiasingMode', 'antialiasingQuality', 'temporalAAMode',
  'temporalAAEnabled', 'temporalAAStrength', 'backgroundMode', 'clearColor',
  'aoStrength', 'aoDistance', 'aoSoftness', 'aoDither', 'aoSampleRate',
  'aoBias', 'aoEnabled', 'setAoEnabled', 'lightProbe', 'skyMaterial',
  'probeExposure', 'probeHorizon', 'probeOrientation', 'depthTestEnabled',
  'depthPrePassEnabled', 'tonemapMode', 'skyboxBlurAmount',
  'specularAAEnabled', 'lightmapper', 'skyBoxCubeMap', 'debugSettings',
  'scissorRect', 'fog', 'oitMethod', 'gridEnabled', 'setGridEnabled',
  'gridScale', 'setGridScale', 'gridFlags', 'setGridFlags',
  'setAntialiasingMode', 'setAntialiasingQuality', 'setTemporalAAEnabled',
  'setTemporalAAStrength', 'setBackgroundMode', 'setClearColor',
  'setAoStrength', 'setAoDistance', 'setAoSoftness', 'setAoDither',
  'setAoSampleRate', 'setAoBias', 'setLightProbe', 'setSkyMaterial',
  'setProbeExposure', 'setProbeHorizon', 'setProbeOrientation',
  'setDepthTestEnabled', 'setDepthPrePassEnabled', 'setTonemapMode',
  'setSkyboxBlurAmount', 'setSpecularAAEnabled', 'setSkyBoxCubeMap',
  'setLightmapper', 'setDebugSettings', 'setScissorRect', 'setFog',
  'setOitMethod', 'antialiasingModeChanged', 'antialiasingQualityChanged',
  'temporalAAModeChanged', 'temporalAAEnabledChanged',
  'temporalAAStrengthChanged', 'backgroundModeChanged', 'clearColorChanged',
  'aoStrengthChanged', 'aoDistanceChanged', 'aoSoftnessChanged',
  'aoDitherChanged', 'aoSampleRateChanged', 'aoBiasChanged',
  'aoEnabledChanged', 'lightProbeChanged', 'skyMaterialChanged',
  'probeExposureChanged', 'probeHorizonChanged', 'probeOrientationChanged',
  'depthTestEnabledChanged', 'depthPrePassEnabledChanged',
  'tonemapModeChanged', 'skyboxBlurAmountChanged',
  'specularAAEnabledChanged', 'lightmapperChanged', 'skyBoxCubeMapChanged',
  'debugSettingsChanged', 'scissorRectChanged', 'fogChanged',
  'oitMethodChanged', 'updateSpatialNode', 'itemChange',
  'useBuiltinTonemapper', 'defaultAoDistance', 'updateSceneManager'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DSceneEnvironment::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuick3DSceneEnvironment::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DSceneEnvironment::~QQuick3DSceneEnvironment()': the
    destructor: Python never removes a C++ QQuick3DSceneEnvironment.
  - Qt's 'QQmlListProperty<QQuick3DEffect>
    QQuick3DSceneEnvironment::effects()': gives a type Python has no way to
    take yet.
  - Qt's 'void QQuick3DSceneEnvironment::setTemporalAAMode(const
    QQuick3DEnvironmentTemporalAAMode &newTemporalAAMode)': takes a type
    Python has no way to hand over yet.
  - Qt's 'const QVector<QQuick3DEffect *>
    &QQuick3DSceneEnvironment::effectList() const': gives a type Python has
    no way to take yet.
  - Qt's 'void QQuick3DSceneEnvironment::qmlAppendEffect(
    QQmlListProperty<QQuick3DEffect> *list, QQuick3DEffect *effect)': names
    'QQmlListProperty<QQuick3DEffect>', which has no cute class yet.
  - Qt's 'QQuick3DEffect
    *QQuick3DSceneEnvironment::qmlEffectAt(QQmlListProperty<QQuick3DEffect>
    *list, qsizetype index)': names 'QQmlListProperty<QQuick3DEffect>', which
    has no cute class yet.
  - Qt's 'qsizetype QQuick3DSceneEnvironment::qmlEffectsCount(
    QQmlListProperty<QQuick3DEffect> *list)': names
    'QQmlListProperty<QQuick3DEffect>', which has no cute class yet.
  - Qt's 'void QQuick3DSceneEnvironment::qmlClearEffects(
    QQmlListProperty<QQuick3DEffect> *list)': names
    'QQmlListProperty<QQuick3DEffect>', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 115 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DSceneEnvironment is created at the first use, not by
    'QQuick3DSceneEnvironment(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DSceneEnvironment.
  - Qt tells when it has removed the C++ QQuick3DSceneEnvironment. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DSceneEnvironment that has no cute function yet,
    'effectList', 'effects', 'qmlAppendEffect', 'qmlClearEffects',
    'qmlEffectAt', 'qmlEffectsCount', 'setTemporalAAMode', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuick3DSceneEnvironment, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class QQuick3DEnvironmentAAModeValues(CuteNum):
    """
    The enum 'QQuick3DSceneEnvironment::QQuick3DEnvironmentAAModeValues' of
    Qt, with the 4 names Qt gives in it.
    """

    NoAA = Kee[int](0)
    SSAA = Kee[int](1)
    MSAA = Kee[int](2)
    ProgressiveAA = Kee[int](3)

  class QQuick3DEnvironmentAAQualityValues(CuteNum):
    """
    The enum 'QQuick3DSceneEnvironment::QQuick3DEnvironmentAAQualityValues'
    of Qt, with the 3 names Qt gives in it.
    """

    Medium = Kee[int](2)
    High = Kee[int](4)
    VeryHigh = Kee[int](8)

  class QQuick3DEnvironmentBackgroundTypes(CuteNum):
    """
    The enum 'QQuick3DSceneEnvironment::QQuick3DEnvironmentBackgroundTypes'
    of Qt, with the 6 names Qt gives in it.
    """

    Transparent = Kee[int](0)
    Unspecified = Kee[int](1)
    Color = Kee[int](2)
    SkyBox = Kee[int](3)
    SkyBoxCubeMap = Kee[int](4)
    SkyMaterial = Kee[int](5)

  class QQuick3DEnvironmentOITMethod(CuteNum):
    """
    The enum 'QQuick3DSceneEnvironment::QQuick3DEnvironmentOITMethod' of Qt,
    with the 3 names Qt gives in it.
    """

    OITNone = Kee[int](0)
    OITWeightedBlended = Kee[int](1)
    OITLinkedList = Kee[int](2)

  class QQuick3DEnvironmentTemporalAAMode(CuteNum):
    """
    The enum 'QQuick3DSceneEnvironment::QQuick3DEnvironmentTemporalAAMode' of
    Qt, with the 2 names Qt gives in it.
    """

    TAADefault = Kee[int](0)
    TAAMotionVector = Kee[int](1)

  class QQuick3DEnvironmentTonemapModes(CuteNum):
    """
    The enum 'QQuick3DSceneEnvironment::QQuick3DEnvironmentTonemapModes' of
    Qt, with the 5 names Qt gives in it.
    """

    TonemapModeNone = Kee[int](0)
    TonemapModeLinear = Kee[int](1)
    TonemapModeAces = Kee[int](2)
    TonemapModeHejlDawson = Kee[int](3)
    TonemapModeFilmic = Kee[int](4)

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
    Calls Qt's 'QString QQuick3DSceneEnvironment::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#tr

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
    #  QString QQuick3DSceneEnvironment::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24QQuick3DSceneEnvironment2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def defaultAoDistance() -> float:
    """
    Calls Qt's 'float QQuick3DSceneEnvironment::defaultAoDistance()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#defaultAoDistance
    """
    #  float QQuick3DSceneEnvironment::defaultAoDistance()
    return Rituals.call(
        'ritual_ZN24QQuick3DSceneEnvironment17defaultAoDistanceEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DSceneEnvironment'

  #  A C++ QQuick3DSceneEnvironment Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DSceneEnvironment'

  #  The functions Qt calls itself that QQuick3DSceneEnvironment is the first
  #  to declare and that cannot be handed to Python yet, each as Qt declares
  #  it. A class of a program that writes one of them anew is refused, since
  #  Qt would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'effectList': (
          'const QVector<QQuick3DEffect *> '
          '&QQuick3DSceneEnvironment::effectList() const',
      ),
  }

  #  The functions Qt calls itself that QQuick3DSceneEnvironment is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'useBuiltinTonemapper': (
          ('_ZNK24QQuick3DSceneEnvironment20useBuiltinTonemapperEv',
           ('bool', 'number', ''),
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DSceneEnvironment::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DSceneEnvironment::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuick3DSceneEnvironment10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def antialiasingMode(self) -> QQuick3DEnvironmentAAModeValues:
    """
    Calls Qt's 'QQuick3DEnvironmentAAModeValues
    QQuick3DSceneEnvironment::antialiasingMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#antialiasingMode

    Returns
    -------

    QQuick3DEnvironmentAAModeValues
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuick3DEnvironmentAAModeValues(number)' gives.
    """
    #  QQuick3DEnvironmentAAModeValues
    #      QQuick3DSceneEnvironment::antialiasingMode() const
    return QQuick3DSceneEnvironment.QQuick3DEnvironmentAAModeValues(
        self.uglySide.call(
            'ritual_ZNK24QQuick3DSceneEnvironment16antialiasingModeEv',
        ))

  def antialiasingQuality(self) -> QQuick3DEnvironmentAAQualityValues:
    """
    Calls Qt's 'QQuick3DEnvironmentAAQualityValues
    QQuick3DSceneEnvironment::antialiasingQuality() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#antialiasingQuality

    Returns
    -------

    QQuick3DEnvironmentAAQualityValues
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuick3DEnvironmentAAQualityValues(number)' gives.
    """
    #  QQuick3DEnvironmentAAQualityValues
    #      QQuick3DSceneEnvironment::antialiasingQuality() const
    return QQuick3DSceneEnvironment.QQuick3DEnvironmentAAQualityValues(
        self.uglySide.call(
            'ritual_ZNK24QQuick3DSceneEnvironment19antialiasingQualityEv',
        ))

  def temporalAAMode(self) -> QQuick3DEnvironmentTemporalAAMode:
    """
    Calls Qt's 'QQuick3DEnvironmentTemporalAAMode
    QQuick3DSceneEnvironment::temporalAAMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#temporalAAMode

    Returns
    -------

    QQuick3DEnvironmentTemporalAAMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuick3DEnvironmentTemporalAAMode(number)' gives.
    """
    #  QQuick3DEnvironmentTemporalAAMode
    #      QQuick3DSceneEnvironment::temporalAAMode() const
    return QQuick3DSceneEnvironment.QQuick3DEnvironmentTemporalAAMode(
        self.uglySide.call(
            'ritual_ZNK24QQuick3DSceneEnvironment14temporalAAModeEv',
        ))

  def temporalAAEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DSceneEnvironment::temporalAAEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#temporalAAEnabled
    """
    #  bool QQuick3DSceneEnvironment::temporalAAEnabled() const
    return self.uglySide.call(
        'ritual_ZNK24QQuick3DSceneEnvironment17temporalAAEnabledEv',
    )

  def temporalAAStrength(self) -> float:
    """
    Calls Qt's 'float QQuick3DSceneEnvironment::temporalAAStrength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#temporalAAStrength
    """
    #  float QQuick3DSceneEnvironment::temporalAAStrength() const
    return self.uglySide.call(
        'ritual_ZNK24QQuick3DSceneEnvironment18temporalAAStrengthEv',
    )

  def backgroundMode(self) -> QQuick3DEnvironmentBackgroundTypes:
    """
    Calls Qt's 'QQuick3DEnvironmentBackgroundTypes
    QQuick3DSceneEnvironment::backgroundMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#backgroundMode

    Returns
    -------

    QQuick3DEnvironmentBackgroundTypes
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuick3DEnvironmentBackgroundTypes(number)' gives.
    """
    #  QQuick3DEnvironmentBackgroundTypes
    #      QQuick3DSceneEnvironment::backgroundMode() const
    return QQuick3DSceneEnvironment.QQuick3DEnvironmentBackgroundTypes(
        self.uglySide.call(
            'ritual_ZNK24QQuick3DSceneEnvironment14backgroundModeEv',
        ))

  def clearColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuick3DSceneEnvironment::clearColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#clearColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuick3DSceneEnvironment::clearColor() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuick3DSceneEnvironment10clearColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def aoStrength(self) -> float:
    """
    Calls Qt's 'float QQuick3DSceneEnvironment::aoStrength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#aoStrength
    """
    #  float QQuick3DSceneEnvironment::aoStrength() const
    return self.uglySide.call(
        'ritual_ZNK24QQuick3DSceneEnvironment10aoStrengthEv',
    )

  def aoDistance(self) -> float:
    """
    Calls Qt's 'float QQuick3DSceneEnvironment::aoDistance() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#aoDistance
    """
    #  float QQuick3DSceneEnvironment::aoDistance() const
    return self.uglySide.call(
        'ritual_ZNK24QQuick3DSceneEnvironment10aoDistanceEv',
    )

  def aoSoftness(self) -> float:
    """
    Calls Qt's 'float QQuick3DSceneEnvironment::aoSoftness() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#aoSoftness
    """
    #  float QQuick3DSceneEnvironment::aoSoftness() const
    return self.uglySide.call(
        'ritual_ZNK24QQuick3DSceneEnvironment10aoSoftnessEv',
    )

  def aoDither(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DSceneEnvironment::aoDither() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#aoDither
    """
    #  bool QQuick3DSceneEnvironment::aoDither() const
    return self.uglySide.call(
        'ritual_ZNK24QQuick3DSceneEnvironment8aoDitherEv',
    )

  def aoSampleRate(self) -> int:
    """
    Calls Qt's 'int QQuick3DSceneEnvironment::aoSampleRate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#aoSampleRate
    """
    #  int QQuick3DSceneEnvironment::aoSampleRate() const
    return self.uglySide.call(
        'ritual_ZNK24QQuick3DSceneEnvironment12aoSampleRateEv',
    )

  def aoBias(self) -> float:
    """
    Calls Qt's 'float QQuick3DSceneEnvironment::aoBias() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#aoBias
    """
    #  float QQuick3DSceneEnvironment::aoBias() const
    return self.uglySide.call(
        'ritual_ZNK24QQuick3DSceneEnvironment6aoBiasEv',
    )

  def aoEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DSceneEnvironment::aoEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#aoEnabled
    """
    #  bool QQuick3DSceneEnvironment::aoEnabled() const
    return self.uglySide.call(
        'ritual_ZNK24QQuick3DSceneEnvironment9aoEnabledEv',
    )

  def lightProbe(self) -> Optional[QQuick3DTexture]:
    """
    Calls Qt's 'QQuick3DTexture *QQuick3DSceneEnvironment::lightProbe()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#lightProbe

    Returns
    -------

    Optional[QQuick3DTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DTexture *QQuick3DSceneEnvironment::lightProbe() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuick3DSceneEnvironment10lightProbeEv',
    )
    from . import QQuick3DTexture
    return QQuick3DTexture._cuteAt(address)

  def skyMaterial(self) -> Optional[QQuick3DSkyMaterial]:
    """
    Calls Qt's 'QQuick3DSkyMaterial *QQuick3DSceneEnvironment::skyMaterial()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#skyMaterial

    Returns
    -------

    Optional[QQuick3DSkyMaterial]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DSkyMaterial *QQuick3DSceneEnvironment::skyMaterial() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuick3DSceneEnvironment11skyMaterialEv',
    )
    from . import QQuick3DSkyMaterial
    return QQuick3DSkyMaterial._cuteAt(address)

  def probeExposure(self) -> float:
    """
    Calls Qt's 'float QQuick3DSceneEnvironment::probeExposure() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#probeExposure
    """
    #  float QQuick3DSceneEnvironment::probeExposure() const
    return self.uglySide.call(
        'ritual_ZNK24QQuick3DSceneEnvironment13probeExposureEv',
    )

  def probeHorizon(self) -> float:
    """
    Calls Qt's 'float QQuick3DSceneEnvironment::probeHorizon() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#probeHorizon
    """
    #  float QQuick3DSceneEnvironment::probeHorizon() const
    return self.uglySide.call(
        'ritual_ZNK24QQuick3DSceneEnvironment12probeHorizonEv',
    )

  def probeOrientation(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DSceneEnvironment::probeOrientation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#probeOrientation

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DSceneEnvironment::probeOrientation() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuick3DSceneEnvironment16probeOrientationEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def depthTestEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DSceneEnvironment::depthTestEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#depthTestEnabled
    """
    #  bool QQuick3DSceneEnvironment::depthTestEnabled() const
    return self.uglySide.call(
        'ritual_ZNK24QQuick3DSceneEnvironment16depthTestEnabledEv',
    )

  def depthPrePassEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DSceneEnvironment::depthPrePassEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#depthPrePassEnabled
    """
    #  bool QQuick3DSceneEnvironment::depthPrePassEnabled() const
    return self.uglySide.call(
        'ritual_ZNK24QQuick3DSceneEnvironment19depthPrePassEnabledEv',
    )

  def tonemapMode(self) -> QQuick3DEnvironmentTonemapModes:
    """
    Calls Qt's 'QQuick3DEnvironmentTonemapModes
    QQuick3DSceneEnvironment::tonemapMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#tonemapMode

    Returns
    -------

    QQuick3DEnvironmentTonemapModes
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuick3DEnvironmentTonemapModes(number)' gives.
    """
    #  QQuick3DEnvironmentTonemapModes
    #      QQuick3DSceneEnvironment::tonemapMode() const
    return QQuick3DSceneEnvironment.QQuick3DEnvironmentTonemapModes(
        self.uglySide.call(
            'ritual_ZNK24QQuick3DSceneEnvironment11tonemapModeEv',
        ))

  def skyboxBlurAmount(self) -> float:
    """
    Calls Qt's 'float QQuick3DSceneEnvironment::skyboxBlurAmount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#skyboxBlurAmount
    """
    #  float QQuick3DSceneEnvironment::skyboxBlurAmount() const
    return self.uglySide.call(
        'ritual_ZNK24QQuick3DSceneEnvironment16skyboxBlurAmountEv',
    )

  def specularAAEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DSceneEnvironment::specularAAEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#specularAAEnabled
    """
    #  bool QQuick3DSceneEnvironment::specularAAEnabled() const
    return self.uglySide.call(
        'ritual_ZNK24QQuick3DSceneEnvironment17specularAAEnabledEv',
    )

  def lightmapper(self) -> Optional[QQuick3DLightmapper]:
    """
    Calls Qt's 'QQuick3DLightmapper *QQuick3DSceneEnvironment::lightmapper()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#lightmapper

    Returns
    -------

    Optional[QQuick3DLightmapper]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DLightmapper *QQuick3DSceneEnvironment::lightmapper() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuick3DSceneEnvironment11lightmapperEv',
    )
    from . import QQuick3DLightmapper
    return QQuick3DLightmapper._cuteAt(address)

  def skyBoxCubeMap(self) -> Optional[QQuick3DCubeMapTexture]:
    """
    Calls Qt's 'QQuick3DCubeMapTexture
    *QQuick3DSceneEnvironment::skyBoxCubeMap() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#skyBoxCubeMap

    Returns
    -------

    Optional[QQuick3DCubeMapTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DCubeMapTexture *QQuick3DSceneEnvironment::skyBoxCubeMap()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK24QQuick3DSceneEnvironment13skyBoxCubeMapEv',
    )
    from . import QQuick3DCubeMapTexture
    return QQuick3DCubeMapTexture._cuteAt(address)

  def debugSettings(self) -> Optional[QQuick3DDebugSettings]:
    """
    Calls Qt's 'QQuick3DDebugSettings
    *QQuick3DSceneEnvironment::debugSettings() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#debugSettings

    Returns
    -------

    Optional[QQuick3DDebugSettings]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DDebugSettings *QQuick3DSceneEnvironment::debugSettings() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuick3DSceneEnvironment13debugSettingsEv',
    )
    from . import QQuick3DDebugSettings
    return QQuick3DDebugSettings._cuteAt(address)

  def scissorRect(self) -> QRect:
    """
    Calls Qt's 'QRect QQuick3DSceneEnvironment::scissorRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#scissorRect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QQuick3DSceneEnvironment::scissorRect() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuick3DSceneEnvironment11scissorRectEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def fog(self) -> Optional[QQuick3DFog]:
    """
    Calls Qt's 'QQuick3DFog *QQuick3DSceneEnvironment::fog() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#fog

    Returns
    -------

    Optional[QQuick3DFog]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DFog *QQuick3DSceneEnvironment::fog() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuick3DSceneEnvironment3fogEv',
    )
    from . import QQuick3DFog
    return QQuick3DFog._cuteAt(address)

  def oitMethod(self) -> QQuick3DEnvironmentOITMethod:
    """
    Calls Qt's 'QQuick3DEnvironmentOITMethod
    QQuick3DSceneEnvironment::oitMethod() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#oitMethod

    Returns
    -------

    QQuick3DEnvironmentOITMethod
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuick3DEnvironmentOITMethod(number)' gives.
    """
    #  QQuick3DEnvironmentOITMethod QQuick3DSceneEnvironment::oitMethod()
    #      const
    return QQuick3DSceneEnvironment.QQuick3DEnvironmentOITMethod(
        self.uglySide.call(
            'ritual_ZNK24QQuick3DSceneEnvironment9oitMethodEv',
        ))

  def gridEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DSceneEnvironment::gridEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#gridEnabled
    """
    #  bool QQuick3DSceneEnvironment::gridEnabled() const
    return self.uglySide.call(
        'ritual_ZNK24QQuick3DSceneEnvironment11gridEnabledEv',
    )

  def gridScale(self) -> float:
    """
    Calls Qt's 'float QQuick3DSceneEnvironment::gridScale() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#gridScale
    """
    #  float QQuick3DSceneEnvironment::gridScale() const
    return self.uglySide.call(
        'ritual_ZNK24QQuick3DSceneEnvironment9gridScaleEv',
    )

  def gridFlags(self) -> int:
    """
    Calls Qt's 'uint QQuick3DSceneEnvironment::gridFlags() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#gridFlags
    """
    #  uint QQuick3DSceneEnvironment::gridFlags() const
    return self.uglySide.call(
        'ritual_ZNK24QQuick3DSceneEnvironment9gridFlagsEv',
    )

  def useBuiltinTonemapper(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DSceneEnvironment::useBuiltinTonemapper() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#useBuiltinTonemapper
    """
    #  bool QQuick3DSceneEnvironment::useBuiltinTonemapper() const
    ritual = 'ritual_ZNK24QQuick3DSceneEnvironment20useBuiltinTonemapperEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QQuick3DSceneEnvironment20useBuiltinTonemapperEv')
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setAoEnabled(self, newAoEnabled: bool) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::setAoEnabled(bool
    newAoEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#setAoEnabled

    Parameters
    ----------

    newAoEnabled : bool
      Passed on as it is.
    """
    #  void QQuick3DSceneEnvironment::setAoEnabled(bool newAoEnabled)
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment12setAoEnabledEb', newAoEnabled,
    )

  @overload(bool)
  def setGridEnabled(self, newGridEnabled: bool) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::setGridEnabled(bool
    newGridEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#setGridEnabled

    Parameters
    ----------

    newGridEnabled : bool
      Passed on as it is.
    """
    #  void QQuick3DSceneEnvironment::setGridEnabled(bool newGridEnabled)
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment14setGridEnabledEb',
        newGridEnabled,
    )

  @overload(float)
  def setGridScale(self, newGridScale: float) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::setGridScale(float
    newGridScale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#setGridScale

    Parameters
    ----------

    newGridScale : float
      Passed on as it is.
    """
    #  void QQuick3DSceneEnvironment::setGridScale(float newGridScale)
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment12setGridScaleEf', newGridScale,
    )

  @overload(int)
  def setGridFlags(self, newGridFlags: int) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::setGridFlags(uint
    newGridFlags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#setGridFlags

    Parameters
    ----------

    newGridFlags : int
      Passed on as it is.
    """
    #  void QQuick3DSceneEnvironment::setGridFlags(uint newGridFlags)
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment12setGridFlagsEj', newGridFlags,
    )

  @overload(QQuick3DEnvironmentAAModeValues)
  def setAntialiasingMode(
      self,
      antialiasingMode: QQuick3DEnvironmentAAModeValues,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DSceneEnvironment::setAntialiasingMode(QQuick3DSceneEnvironment::
    QQuick3DEnvironmentAAModeValues antialiasingMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#setAntialiasingMode

    Parameters
    ----------

    antialiasingMode : QQuick3DEnvironmentAAModeValues
      Passed on as its number.
    """
    #  void QQuick3DSceneEnvironment::setAntialiasingMode(
    #      QQuick3DSceneEnvironment::QQuick3DEnvironmentAAModeValues
    #      antialiasingMode)
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment19setAntialiasingModeENS_31QQui'
        'ck3DEnvironmentAAModeValuesE',
        antialiasingMode.value,
    )

  @overload(QQuick3DEnvironmentAAQualityValues)
  def setAntialiasingQuality(
      self,
      antialiasingQuality: QQuick3DEnvironmentAAQualityValues,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::setAntialiasingQuality(
    QQuick3DSceneEnvironment::QQuick3DEnvironmentAAQualityValues
    antialiasingQuality)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html

    Parameters
    ----------

    antialiasingQuality : QQuick3DEnvironmentAAQualityValues
      Passed on as its number.
    """
    #  void QQuick3DSceneEnvironment::setAntialiasingQuality(
    #      QQuick3DSceneEnvironment::QQuick3DEnvironmentAAQualityValues
    #      antialiasingQuality)
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment22setAntialiasingQualityENS_34Q'
        'Quick3DEnvironmentAAQualityValuesE',
        antialiasingQuality.value,
    )

  @overload(bool)
  def setTemporalAAEnabled(self, temporalAAEnabled: bool) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::setTemporalAAEnabled(bool
    temporalAAEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#setTemporalAAEnabled

    Parameters
    ----------

    temporalAAEnabled : bool
      Passed on as it is.
    """
    #  void QQuick3DSceneEnvironment::setTemporalAAEnabled(bool
    #      temporalAAEnabled)
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment20setTemporalAAEnabledEb',
        temporalAAEnabled,
    )

  @overload(float)
  def setTemporalAAStrength(self, strength: float) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::setTemporalAAStrength(float
    strength)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html

    Parameters
    ----------

    strength : float
      Passed on as it is.
    """
    #  void QQuick3DSceneEnvironment::setTemporalAAStrength(float strength)
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment21setTemporalAAStrengthEf',
        strength,
    )

  @overload(QQuick3DEnvironmentBackgroundTypes)
  def setBackgroundMode(
      self,
      backgroundMode: QQuick3DEnvironmentBackgroundTypes,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DSceneEnvironment::setBackgroundMode(QQuick3DSceneEnvironment::
    QQuick3DEnvironmentBackgroundTypes backgroundMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#setBackgroundMode

    Parameters
    ----------

    backgroundMode : QQuick3DEnvironmentBackgroundTypes
      Passed on as its number.
    """
    #  void QQuick3DSceneEnvironment::setBackgroundMode(
    #      QQuick3DSceneEnvironment::QQuick3DEnvironmentBackgroundTypes
    #      backgroundMode)
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment17setBackgroundModeENS_34QQuick'
        '3DEnvironmentBackgroundTypesE',
        backgroundMode.value,
    )

  @overload(QColor)
  def setClearColor(self, clearColor: QColor) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::setClearColor(const QColor
    &clearColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#setClearColor

    Parameters
    ----------

    clearColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuick3DSceneEnvironment::setClearColor(const QColor &clearColor)
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment13setClearColorERK6QColor',
        self._valueOf(clearColor),
    )

  @overload(float)
  def setAoStrength(self, aoStrength: float) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::setAoStrength(float
    aoStrength)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#setAoStrength

    Parameters
    ----------

    aoStrength : float
      Passed on as it is.
    """
    #  void QQuick3DSceneEnvironment::setAoStrength(float aoStrength)
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment13setAoStrengthEf', aoStrength,
    )

  @overload(float)
  def setAoDistance(self, aoDistance: float) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::setAoDistance(float
    aoDistance)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#setAoDistance

    Parameters
    ----------

    aoDistance : float
      Passed on as it is.
    """
    #  void QQuick3DSceneEnvironment::setAoDistance(float aoDistance)
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment13setAoDistanceEf', aoDistance,
    )

  @overload(float)
  def setAoSoftness(self, aoSoftness: float) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::setAoSoftness(float
    aoSoftness)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#setAoSoftness

    Parameters
    ----------

    aoSoftness : float
      Passed on as it is.
    """
    #  void QQuick3DSceneEnvironment::setAoSoftness(float aoSoftness)
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment13setAoSoftnessEf', aoSoftness,
    )

  @overload(bool)
  def setAoDither(self, aoDither: bool) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::setAoDither(bool aoDither)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#setAoDither

    Parameters
    ----------

    aoDither : bool
      Passed on as it is.
    """
    #  void QQuick3DSceneEnvironment::setAoDither(bool aoDither)
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment11setAoDitherEb', aoDither,
    )

  @overload(int)
  def setAoSampleRate(self, aoSampleRate: int) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::setAoSampleRate(int
    aoSampleRate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#setAoSampleRate

    Parameters
    ----------

    aoSampleRate : int
      Passed on as it is.
    """
    #  void QQuick3DSceneEnvironment::setAoSampleRate(int aoSampleRate)
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment15setAoSampleRateEi',
        aoSampleRate,
    )

  @overload(float)
  def setAoBias(self, aoBias: float) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::setAoBias(float aoBias)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#setAoBias

    Parameters
    ----------

    aoBias : float
      Passed on as it is.
    """
    #  void QQuick3DSceneEnvironment::setAoBias(float aoBias)
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment9setAoBiasEf', aoBias,
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def setLightProbe(self, lightProbe: Optional[QQuick3DTexture]) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::setLightProbe(QQuick3DTexture
    *lightProbe)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#setLightProbe

    Parameters
    ----------

    lightProbe : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DSceneEnvironment::setLightProbe(QQuick3DTexture
    #      *lightProbe)
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment13setLightProbeEP15QQuick3DText'
        'ure',
        self._addressOf(lightProbe),
    )

  @overload(QQuick3DSkyMaterial)
  @overload(NoneType)
  def setSkyMaterial(
      self,
      skyMaterial: Optional[QQuick3DSkyMaterial],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DSceneEnvironment::setSkyMaterial(QQuick3DSkyMaterial
    *skyMaterial)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#setSkyMaterial

    Parameters
    ----------

    skyMaterial : Optional[QQuick3DSkyMaterial]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DSceneEnvironment::setSkyMaterial(QQuick3DSkyMaterial
    #      *skyMaterial)
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment14setSkyMaterialEP19QQuick3DSky'
        'Material',
        self._addressOf(skyMaterial),
    )

  @overload(float)
  def setProbeExposure(self, probeExposure: float) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::setProbeExposure(float
    probeExposure)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#setProbeExposure

    Parameters
    ----------

    probeExposure : float
      Passed on as it is.
    """
    #  void QQuick3DSceneEnvironment::setProbeExposure(float probeExposure)
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment16setProbeExposureEf',
        probeExposure,
    )

  @overload(float)
  def setProbeHorizon(self, probeHorizon: float) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::setProbeHorizon(float
    probeHorizon)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#setProbeHorizon

    Parameters
    ----------

    probeHorizon : float
      Passed on as it is.
    """
    #  void QQuick3DSceneEnvironment::setProbeHorizon(float probeHorizon)
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment15setProbeHorizonEf',
        probeHorizon,
    )

  @overload(QVector3D)
  def setProbeOrientation(self, orientation: QVector3D) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::setProbeOrientation(const
    QVector3D &orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#setProbeOrientation

    Parameters
    ----------

    orientation : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuick3DSceneEnvironment::setProbeOrientation(const QVector3D
    #      &orientation)
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment19setProbeOrientationERK9QVecto'
        'r3D',
        self._valueOf(orientation),
    )

  @overload(bool)
  def setDepthTestEnabled(self, depthTestEnabled: bool) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::setDepthTestEnabled(bool
    depthTestEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#setDepthTestEnabled

    Parameters
    ----------

    depthTestEnabled : bool
      Passed on as it is.
    """
    #  void QQuick3DSceneEnvironment::setDepthTestEnabled(bool
    #      depthTestEnabled)
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment19setDepthTestEnabledEb',
        depthTestEnabled,
    )

  @overload(bool)
  def setDepthPrePassEnabled(self, depthPrePassEnabled: bool) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::setDepthPrePassEnabled(bool
    depthPrePassEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html

    Parameters
    ----------

    depthPrePassEnabled : bool
      Passed on as it is.
    """
    #  void QQuick3DSceneEnvironment::setDepthPrePassEnabled(bool
    #      depthPrePassEnabled)
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment22setDepthPrePassEnabledEb',
        depthPrePassEnabled,
    )

  @overload(QQuick3DEnvironmentTonemapModes)
  def setTonemapMode(
      self,
      tonemapMode: QQuick3DEnvironmentTonemapModes,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DSceneEnvironment::setTonemapMode(QQuick3DSceneEnvironment::
    QQuick3DEnvironmentTonemapModes tonemapMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#setTonemapMode

    Parameters
    ----------

    tonemapMode : QQuick3DEnvironmentTonemapModes
      Passed on as its number.
    """
    #  void QQuick3DSceneEnvironment::setTonemapMode(
    #      QQuick3DSceneEnvironment::QQuick3DEnvironmentTonemapModes
    #      tonemapMode)
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment14setTonemapModeENS_31QQuick3DE'
        'nvironmentTonemapModesE',
        tonemapMode.value,
    )

  @overload(float)
  def setSkyboxBlurAmount(self, newSkyboxBlurAmount: float) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::setSkyboxBlurAmount(float
    newSkyboxBlurAmount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#setSkyboxBlurAmount

    Parameters
    ----------

    newSkyboxBlurAmount : float
      Passed on as it is.
    """
    #  void QQuick3DSceneEnvironment::setSkyboxBlurAmount(float
    #      newSkyboxBlurAmount)
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment19setSkyboxBlurAmountEf',
        newSkyboxBlurAmount,
    )

  @overload(bool)
  def setSpecularAAEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::setSpecularAAEnabled(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#setSpecularAAEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuick3DSceneEnvironment::setSpecularAAEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment20setSpecularAAEnabledEb',
        enabled,
    )

  @overload(QQuick3DCubeMapTexture)
  @overload(NoneType)
  def setSkyBoxCubeMap(
      self,
      newSkyBoxCubeMap: Optional[QQuick3DCubeMapTexture],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DSceneEnvironment::setSkyBoxCubeMap(QQuick3DCubeMapTexture
    *newSkyBoxCubeMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#setSkyBoxCubeMap

    Parameters
    ----------

    newSkyBoxCubeMap : Optional[QQuick3DCubeMapTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DSceneEnvironment::setSkyBoxCubeMap(QQuick3DCubeMapTexture
    #      *newSkyBoxCubeMap)
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment16setSkyBoxCubeMapEP22QQuick3DC'
        'ubeMapTexture',
        self._addressOf(newSkyBoxCubeMap),
    )

  @overload(QQuick3DLightmapper)
  @overload(NoneType)
  def setLightmapper(
      self,
      lightmapper: Optional[QQuick3DLightmapper],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DSceneEnvironment::setLightmapper(QQuick3DLightmapper
    *lightmapper)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#setLightmapper

    Parameters
    ----------

    lightmapper : Optional[QQuick3DLightmapper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DSceneEnvironment::setLightmapper(QQuick3DLightmapper
    #      *lightmapper)
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment14setLightmapperEP19QQuick3DLig'
        'htmapper',
        self._addressOf(lightmapper),
    )

  @overload(QQuick3DDebugSettings)
  @overload(NoneType)
  def setDebugSettings(
      self,
      newDebugSettings: Optional[QQuick3DDebugSettings],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DSceneEnvironment::setDebugSettings(QQuick3DDebugSettings
    *newDebugSettings)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#setDebugSettings

    Parameters
    ----------

    newDebugSettings : Optional[QQuick3DDebugSettings]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DSceneEnvironment::setDebugSettings(QQuick3DDebugSettings
    #      *newDebugSettings)
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment16setDebugSettingsEP21QQuick3DD'
        'ebugSettings',
        self._addressOf(newDebugSettings),
    )

  @overload(QRect)
  def setScissorRect(self, scissorRect: QRect) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::setScissorRect(QRect
    scissorRect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#setScissorRect

    Parameters
    ----------

    scissorRect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QQuick3DSceneEnvironment::setScissorRect(QRect scissorRect)
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment14setScissorRectE5QRect',
        self._valueOf(scissorRect),
    )

  @overload(QQuick3DFog)
  @overload(NoneType)
  def setFog(self, fog: Optional[QQuick3DFog]) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::setFog(QQuick3DFog *fog)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#setFog

    Parameters
    ----------

    fog : Optional[QQuick3DFog]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DSceneEnvironment::setFog(QQuick3DFog *fog)
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment6setFogEP11QQuick3DFog',
        self._addressOf(fog),
    )

  @overload(QQuick3DEnvironmentOITMethod)
  def setOitMethod(self, mode: QQuick3DEnvironmentOITMethod) -> None:
    """
    Calls Qt's 'void
    QQuick3DSceneEnvironment::setOitMethod(QQuick3DSceneEnvironment::
    QQuick3DEnvironmentOITMethod mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#setOitMethod

    Parameters
    ----------

    mode : QQuick3DEnvironmentOITMethod
      Passed on as its number.
    """
    #  void QQuick3DSceneEnvironment::setOitMethod(QQuick3DSceneEnvironment::
    #      QQuick3DEnvironmentOITMethod mode)
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment12setOitMethodENS_28QQuick3DEnv'
        'ironmentOITMethodE',
        mode.value,
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
    'QQuick3DSceneEnvironment::QQuick3DSceneEnvironment(QQuick3DObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html

    Parameters
    ----------

    parent : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DSceneEnvironment::QQuick3DSceneEnvironment(QQuick3DObject
    #      *parent)
    self._noteCreation(QQuick3DSceneEnvironment, lambda: Rituals.call(
        'ritual_ZN24QQuick3DSceneEnvironmentC1EP14QQuick3DObject',
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

  def antialiasingModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::antialiasingModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html
    """
    #  void QQuick3DSceneEnvironment::antialiasingModeChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment23antialiasingModeChangedEv',
    )

  def antialiasingQualityChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::antialiasingQualityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html
    """
    #  void QQuick3DSceneEnvironment::antialiasingQualityChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment26antialiasingQualityChangedEv',
    )

  def temporalAAModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::temporalAAModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html
    """
    #  void QQuick3DSceneEnvironment::temporalAAModeChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment21temporalAAModeChangedEv',
    )

  def temporalAAEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::temporalAAEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html
    """
    #  void QQuick3DSceneEnvironment::temporalAAEnabledChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment24temporalAAEnabledChangedEv',
    )

  def temporalAAStrengthChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::temporalAAStrengthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html
    """
    #  void QQuick3DSceneEnvironment::temporalAAStrengthChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment25temporalAAStrengthChangedEv',
    )

  def backgroundModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::backgroundModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html
    """
    #  void QQuick3DSceneEnvironment::backgroundModeChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment21backgroundModeChangedEv',
    )

  def clearColorChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::clearColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#clearColorChanged
    """
    #  void QQuick3DSceneEnvironment::clearColorChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment17clearColorChangedEv',
    )

  def aoStrengthChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::aoStrengthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#aoStrengthChanged
    """
    #  void QQuick3DSceneEnvironment::aoStrengthChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment17aoStrengthChangedEv',
    )

  def aoDistanceChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::aoDistanceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#aoDistanceChanged
    """
    #  void QQuick3DSceneEnvironment::aoDistanceChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment17aoDistanceChangedEv',
    )

  def aoSoftnessChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::aoSoftnessChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#aoSoftnessChanged
    """
    #  void QQuick3DSceneEnvironment::aoSoftnessChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment17aoSoftnessChangedEv',
    )

  def aoDitherChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::aoDitherChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#aoDitherChanged
    """
    #  void QQuick3DSceneEnvironment::aoDitherChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment15aoDitherChangedEv',
    )

  def aoSampleRateChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::aoSampleRateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#aoSampleRateChanged
    """
    #  void QQuick3DSceneEnvironment::aoSampleRateChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment19aoSampleRateChangedEv',
    )

  def aoBiasChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::aoBiasChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#aoBiasChanged
    """
    #  void QQuick3DSceneEnvironment::aoBiasChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment13aoBiasChangedEv',
    )

  def aoEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::aoEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#aoEnabledChanged
    """
    #  void QQuick3DSceneEnvironment::aoEnabledChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment16aoEnabledChangedEv',
    )

  def lightProbeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::lightProbeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#lightProbeChanged
    """
    #  void QQuick3DSceneEnvironment::lightProbeChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment17lightProbeChangedEv',
    )

  def skyMaterialChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::skyMaterialChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#skyMaterialChanged
    """
    #  void QQuick3DSceneEnvironment::skyMaterialChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment18skyMaterialChangedEv',
    )

  def probeExposureChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::probeExposureChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#probeExposureChanged
    """
    #  void QQuick3DSceneEnvironment::probeExposureChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment20probeExposureChangedEv',
    )

  def probeHorizonChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::probeHorizonChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#probeHorizonChanged
    """
    #  void QQuick3DSceneEnvironment::probeHorizonChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment19probeHorizonChangedEv',
    )

  def probeOrientationChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::probeOrientationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html
    """
    #  void QQuick3DSceneEnvironment::probeOrientationChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment23probeOrientationChangedEv',
    )

  def depthTestEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::depthTestEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html
    """
    #  void QQuick3DSceneEnvironment::depthTestEnabledChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment23depthTestEnabledChangedEv',
    )

  def depthPrePassEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::depthPrePassEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html
    """
    #  void QQuick3DSceneEnvironment::depthPrePassEnabledChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment26depthPrePassEnabledChangedEv',
    )

  def tonemapModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::tonemapModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#tonemapModeChanged
    """
    #  void QQuick3DSceneEnvironment::tonemapModeChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment18tonemapModeChangedEv',
    )

  def skyboxBlurAmountChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::skyboxBlurAmountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html
    """
    #  void QQuick3DSceneEnvironment::skyboxBlurAmountChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment23skyboxBlurAmountChangedEv',
    )

  def specularAAEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::specularAAEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html
    """
    #  void QQuick3DSceneEnvironment::specularAAEnabledChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment24specularAAEnabledChangedEv',
    )

  def lightmapperChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::lightmapperChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#lightmapperChanged
    """
    #  void QQuick3DSceneEnvironment::lightmapperChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment18lightmapperChangedEv',
    )

  def skyBoxCubeMapChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::skyBoxCubeMapChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#skyBoxCubeMapChanged
    """
    #  void QQuick3DSceneEnvironment::skyBoxCubeMapChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment20skyBoxCubeMapChangedEv',
    )

  def debugSettingsChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::debugSettingsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#debugSettingsChanged
    """
    #  void QQuick3DSceneEnvironment::debugSettingsChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment20debugSettingsChangedEv',
    )

  def scissorRectChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::scissorRectChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#scissorRectChanged
    """
    #  void QQuick3DSceneEnvironment::scissorRectChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment18scissorRectChangedEv',
    )

  def fogChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::fogChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#fogChanged
    """
    #  void QQuick3DSceneEnvironment::fogChanged()
    self.uglySide.call('ritual_ZN24QQuick3DSceneEnvironment10fogChangedEv')

  def oitMethodChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSceneEnvironment::oitMethodChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#oitMethodChanged
    """
    #  void QQuick3DSceneEnvironment::oitMethodChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment16oitMethodChangedEv',
    )

  @overload(QSSGRenderGraphObject)
  @overload(NoneType)
  def updateSpatialNode(
      self,
      node: Optional[QSSGRenderGraphObject],
  ) -> Optional[QSSGRenderGraphObject]:
    """
    Calls Qt's 'QSSGRenderGraphObject
    *QQuick3DSceneEnvironment::updateSpatialNode(QSSGRenderGraphObject
    *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#updateSpatialNode

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
    #      *QQuick3DSceneEnvironment::updateSpatialNode(QSSGRenderGraphObject
    #      *node)
    ritual = (
        'ritual_ZN24QQuick3DSceneEnvironment17updateSpatialNodeEP21QSSGRend'
        'erGraphObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuick3DSceneEnvironment17updateSpatialNodeEP21QS'
          'SGRenderGraphObject')
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
    Calls Qt's 'void QQuick3DSceneEnvironment::itemChange(ItemChange a0,
    const ItemChangeData &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#itemChange

    Parameters
    ----------

    a0 : QQuick3DObject.ItemChange
      Passed on as its number.

    a1 : QQuick3DObject.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuick3DObject::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuick3DSceneEnvironment::itemChange(ItemChange a0, const
    #      ItemChangeData &a1)
    ritual = (
        'ritual_ZN24QQuick3DSceneEnvironment10itemChangeEN14QQuick3DObject1'
        '0ItemChangeERKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuick3DSceneEnvironment10itemChangeEN14QQuick3DO'
          'bject10ItemChangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, a0.value, self._valueOf(a1))

  @overload(QQuick3DSceneManager)
  @overload(NoneType)
  def updateSceneManager(
      self,
      manager: Optional[QQuick3DSceneManager],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DSceneEnvironment::updateSceneManager(QQuick3DSceneManager
    *manager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsceneenvironment.html#updateSceneManager

    Parameters
    ----------

    manager : Optional[QQuick3DSceneManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DSceneEnvironment::updateSceneManager(QQuick3DSceneManager
    #      *manager)
    self.uglySide.call(
        'ritual_ZN24QQuick3DSceneEnvironment18updateSceneManagerEP20QQuick3'
        'DSceneManager',
        self._addressOf(manager),
    )

  @staticmethod
  def effectList(*__, **_) -> Never:
    """
    Qt's 'const QVector<QQuick3DEffect *>
    &QQuick3DSceneEnvironment::effectList() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QQuick3DSceneEnvironment.effectList' has no cute function yet. "
        "Qt's 'const QVector<QQuick3DEffect *> "
        "&QQuick3DSceneEnvironment::effectList() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def effects(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuick3DEffect>
    QQuick3DSceneEnvironment::effects()': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QQuick3DSceneEnvironment.effects' has no cute function yet. Qt's "
        "'QQmlListProperty<QQuick3DEffect> "
        "QQuick3DSceneEnvironment::effects()': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def qmlAppendEffect(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DSceneEnvironment::qmlAppendEffect(
    QQmlListProperty<QQuick3DEffect> *list, QQuick3DEffect *effect)': names
    'QQmlListProperty<QQuick3DEffect>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuick3DSceneEnvironment.qmlAppendEffect' has no cute function "
        "yet. Qt's 'void "
        "QQuick3DSceneEnvironment::qmlAppendEffect(QQmlListProperty<QQuick3D"
        "Effect> *list, QQuick3DEffect *effect)': names "
        "'QQmlListProperty<QQuick3DEffect>', which has no cute class yet.")

  @staticmethod
  def qmlClearEffects(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DSceneEnvironment::qmlClearEffects(
    QQmlListProperty<QQuick3DEffect> *list)': names
    'QQmlListProperty<QQuick3DEffect>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuick3DSceneEnvironment.qmlClearEffects' has no cute function "
        "yet. Qt's 'void "
        "QQuick3DSceneEnvironment::qmlClearEffects(QQmlListProperty<QQuick3D"
        "Effect> *list)': names 'QQmlListProperty<QQuick3DEffect>', which "
        "has no cute class yet.")

  @staticmethod
  def qmlEffectAt(*__, **_) -> Never:
    """
    Qt's 'QQuick3DEffect
    *QQuick3DSceneEnvironment::qmlEffectAt(QQmlListProperty<QQuick3DEffect>
    *list, qsizetype index)': names 'QQmlListProperty<QQuick3DEffect>', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuick3DSceneEnvironment.qmlEffectAt' has no cute function yet. "
        "Qt's 'QQuick3DEffect "
        "*QQuick3DSceneEnvironment::qmlEffectAt(QQmlListProperty<QQuick3DEff"
        "ect> *list, qsizetype index)': names "
        "'QQmlListProperty<QQuick3DEffect>', which has no cute class yet.")

  @staticmethod
  def qmlEffectsCount(*__, **_) -> Never:
    """
    Qt's 'qsizetype QQuick3DSceneEnvironment::qmlEffectsCount(
    QQmlListProperty<QQuick3DEffect> *list)': names
    'QQmlListProperty<QQuick3DEffect>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuick3DSceneEnvironment.qmlEffectsCount' has no cute function "
        "yet. Qt's 'qsizetype "
        "QQuick3DSceneEnvironment::qmlEffectsCount(QQmlListProperty<QQuick3D"
        "Effect> *list)': names 'QQmlListProperty<QQuick3DEffect>', which "
        "has no cute class yet.")

  @staticmethod
  def setTemporalAAMode(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DSceneEnvironment::setTemporalAAMode(const
    QQuick3DEnvironmentTemporalAAMode &newTemporalAAMode)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuick3DSceneEnvironment.setTemporalAAMode' has no cute function "
        "yet. Qt's 'void QQuick3DSceneEnvironment::setTemporalAAMode(const "
        "QQuick3DEnvironmentTemporalAAMode &newTemporalAAMode)': takes a "
        "type Python has no way to hand over yet.")
