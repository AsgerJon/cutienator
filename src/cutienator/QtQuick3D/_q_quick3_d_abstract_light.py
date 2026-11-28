"""
QQuick3DAbstractLight binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dabstractlight_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DAbstractLight to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QQuick3DNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QColor
  from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QSSGRenderGraphObject = WAIT['QSSGRenderGraphObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DAbstractLight(QQuick3DNode):
  """
  The cute side of Qt's QQuick3DAbstractLight: a plain Python object standing
  in front of one C++ QQuick3DAbstractLight.

  It is built on the cute 'QQuick3DNode', as Qt's QQuick3DAbstractLight is
  built on Qt's QQuick3DNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DAbstractLight that has a ritual and that
  Python can call so far, 47 names in all: 'metaObject', 'tr', 'color',
  'ambientColor', 'brightness', 'scope', 'castsShadow', 'shadowBias',
  'shadowFactor', 'shadowMapQuality', 'shadowMapFar', 'shadowFilter',
  'bakeMode', 'softShadowQuality', 'pcfFactor', 'use32BitShadowmap',
  'setColor', 'setAmbientColor', 'setBrightness', 'setScope',
  'setCastsShadow', 'setShadowBias', 'setShadowFactor',
  'setShadowMapQuality', 'setShadowMapFar', 'setShadowFilter', 'setBakeMode',
  'setSoftShadowQuality', 'setPcfFactor', 'setUse32BitShadowmap',
  'colorChanged', 'ambientColorChanged', 'brightnessChanged', 'scopeChanged',
  'castsShadowChanged', 'shadowBiasChanged', 'shadowFactorChanged',
  'shadowMapQualityChanged', 'shadowMapFarChanged', 'shadowFilterChanged',
  'bakeModeChanged', 'softShadowQualityChanged', 'pcfFactorChanged',
  'use32BitShadowmapChanged', 'updateSpatialNode', 'markAllDirty',
  'mapToShadowResolution'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DAbstractLight::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuick3DAbstractLight::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuick3DAbstractLight::qt_qmlMarker_uncreatable()': one of
    Qt's own inner workings.
  - Qt's 'QQuick3DAbstractLight::~QQuick3DAbstractLight()': the destructor:
    Python never removes a C++ QQuick3DAbstractLight.
  - Qt's 'QQuick3DAbstractLight::QQuick3DAbstractLight(QQuick3DNodePrivate
    &dd, QQuick3DNode *parent)': takes a type Python has no way to hand over
    yet.

  What has no ritual
  ------------------

  2 of the 54 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DAbstractLight is created at the first use, not by
    'QQuick3DAbstractLight(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DAbstractLight.
  - Qt tells when it has removed the C++ QQuick3DAbstractLight. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DAbstractLight that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QQuick3DAbstractLight, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class QSSGBakeMode(CuteNum, scoped=True):
    """
    The enum 'QQuick3DAbstractLight::QSSGBakeMode' of Qt, with the 3 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    BakeModeDisabled = Kee[int](0)
    BakeModeIndirect = Kee[int](1)
    BakeModeAll = Kee[int](2)

  class QSSGShadowMapQuality(CuteNum, scoped=True):
    """
    The enum 'QQuick3DAbstractLight::QSSGShadowMapQuality' of Qt, with the 5
    names Qt gives in it. C++ keeps these names inside the enum, so the class
    that holds the enum does not have them.
    """

    ShadowMapQualityLow = Kee[int](0)
    ShadowMapQualityMedium = Kee[int](1)
    ShadowMapQualityHigh = Kee[int](2)
    ShadowMapQualityVeryHigh = Kee[int](3)
    ShadowMapQualityUltra = Kee[int](4)

  class QSSGSoftShadowQuality(CuteNum, scoped=True):
    """
    The enum 'QQuick3DAbstractLight::QSSGSoftShadowQuality' of Qt, with the 6
    names Qt gives in it. C++ keeps these names inside the enum, so the class
    that holds the enum does not have them.
    """

    Hard = Kee[int](0)
    PCF4 = Kee[int](1)
    PCF8 = Kee[int](2)
    PCF16 = Kee[int](3)
    PCF32 = Kee[int](4)
    PCF64 = Kee[int](5)

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
    Calls Qt's 'QString QQuick3DAbstractLight::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dabstractlight.html#tr

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
    #  QString QQuick3DAbstractLight::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QQuick3DAbstractLight2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DAbstractLight'

  #  A C++ QQuick3DAbstractLight Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DAbstractLight'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DAbstractLight::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dabstractlight.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DAbstractLight::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuick3DAbstractLight10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QQuick3DAbstractLight::color() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dabstractlight.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuick3DAbstractLight::color() const
    address = self.uglySide.call('ritual_ZNK21QQuick3DAbstractLight5colorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def ambientColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuick3DAbstractLight::ambientColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dabstractlight.html#ambientColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuick3DAbstractLight::ambientColor() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuick3DAbstractLight12ambientColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def brightness(self) -> float:
    """
    Calls Qt's 'float QQuick3DAbstractLight::brightness() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dabstractlight.html#brightness
    """
    #  float QQuick3DAbstractLight::brightness() const
    return self.uglySide.call(
        'ritual_ZNK21QQuick3DAbstractLight10brightnessEv',
    )

  def scope(self) -> Optional[QQuick3DNode]:
    """
    Calls Qt's 'QQuick3DNode *QQuick3DAbstractLight::scope() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dabstractlight.html#scope

    Returns
    -------

    Optional[QQuick3DNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DNode *QQuick3DAbstractLight::scope() const
    address = self.uglySide.call('ritual_ZNK21QQuick3DAbstractLight5scopeEv')
    return QQuick3DNode._cuteAt(address)

  def castsShadow(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DAbstractLight::castsShadow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dabstractlight.html#castsShadow
    """
    #  bool QQuick3DAbstractLight::castsShadow() const
    return self.uglySide.call(
        'ritual_ZNK21QQuick3DAbstractLight11castsShadowEv',
    )

  def shadowBias(self) -> float:
    """
    Calls Qt's 'float QQuick3DAbstractLight::shadowBias() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dabstractlight.html#shadowBias
    """
    #  float QQuick3DAbstractLight::shadowBias() const
    return self.uglySide.call(
        'ritual_ZNK21QQuick3DAbstractLight10shadowBiasEv',
    )

  def shadowFactor(self) -> float:
    """
    Calls Qt's 'float QQuick3DAbstractLight::shadowFactor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dabstractlight.html#shadowFactor
    """
    #  float QQuick3DAbstractLight::shadowFactor() const
    return self.uglySide.call(
        'ritual_ZNK21QQuick3DAbstractLight12shadowFactorEv',
    )

  def shadowMapQuality(self) -> QSSGShadowMapQuality:
    """
    Calls Qt's 'QSSGShadowMapQuality
    QQuick3DAbstractLight::shadowMapQuality() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dabstractlight.html#shadowMapQuality

    Returns
    -------

    QSSGShadowMapQuality
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSSGShadowMapQuality(number)' gives.
    """
    #  QSSGShadowMapQuality QQuick3DAbstractLight::shadowMapQuality() const
    return QQuick3DAbstractLight.QSSGShadowMapQuality(self.uglySide.call(
        'ritual_ZNK21QQuick3DAbstractLight16shadowMapQualityEv',
    ))

  def shadowMapFar(self) -> float:
    """
    Calls Qt's 'float QQuick3DAbstractLight::shadowMapFar() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dabstractlight.html#shadowMapFar
    """
    #  float QQuick3DAbstractLight::shadowMapFar() const
    return self.uglySide.call(
        'ritual_ZNK21QQuick3DAbstractLight12shadowMapFarEv',
    )

  def shadowFilter(self) -> float:
    """
    Calls Qt's 'float QQuick3DAbstractLight::shadowFilter() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dabstractlight.html#shadowFilter
    """
    #  float QQuick3DAbstractLight::shadowFilter() const
    return self.uglySide.call(
        'ritual_ZNK21QQuick3DAbstractLight12shadowFilterEv',
    )

  def bakeMode(self) -> QSSGBakeMode:
    """
    Calls Qt's 'QSSGBakeMode QQuick3DAbstractLight::bakeMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dabstractlight.html#bakeMode

    Returns
    -------

    QSSGBakeMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QSSGBakeMode(number)'
      gives.
    """
    #  QSSGBakeMode QQuick3DAbstractLight::bakeMode() const
    return QQuick3DAbstractLight.QSSGBakeMode(self.uglySide.call(
        'ritual_ZNK21QQuick3DAbstractLight8bakeModeEv',
    ))

  def softShadowQuality(self) -> QSSGSoftShadowQuality:
    """
    Calls Qt's 'QSSGSoftShadowQuality
    QQuick3DAbstractLight::softShadowQuality() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dabstractlight.html#softShadowQuality

    Returns
    -------

    QSSGSoftShadowQuality
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSSGSoftShadowQuality(number)' gives.
    """
    #  QSSGSoftShadowQuality QQuick3DAbstractLight::softShadowQuality() const
    return QQuick3DAbstractLight.QSSGSoftShadowQuality(self.uglySide.call(
        'ritual_ZNK21QQuick3DAbstractLight17softShadowQualityEv',
    ))

  def pcfFactor(self) -> float:
    """
    Calls Qt's 'float QQuick3DAbstractLight::pcfFactor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dabstractlight.html#pcfFactor
    """
    #  float QQuick3DAbstractLight::pcfFactor() const
    return self.uglySide.call(
        'ritual_ZNK21QQuick3DAbstractLight9pcfFactorEv',
    )

  def use32BitShadowmap(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DAbstractLight::use32BitShadowmap() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dabstractlight.html#use32BitShadowmap
    """
    #  bool QQuick3DAbstractLight::use32BitShadowmap() const
    return self.uglySide.call(
        'ritual_ZNK21QQuick3DAbstractLight17use32BitShadowmapEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuick3DAbstractLight::setColor(const QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dabstractlight.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuick3DAbstractLight::setColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN21QQuick3DAbstractLight8setColorERK6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def setAmbientColor(self, ambientColor: QColor) -> None:
    """
    Calls Qt's 'void QQuick3DAbstractLight::setAmbientColor(const QColor
    &ambientColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dabstractlight.html#setAmbientColor

    Parameters
    ----------

    ambientColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuick3DAbstractLight::setAmbientColor(const QColor
    #      &ambientColor)
    self.uglySide.call(
        'ritual_ZN21QQuick3DAbstractLight15setAmbientColorERK6QColor',
        self._valueOf(ambientColor),
    )

  @overload(float)
  def setBrightness(self, brightness: float) -> None:
    """
    Calls Qt's 'void QQuick3DAbstractLight::setBrightness(float brightness)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dabstractlight.html#setBrightness

    Parameters
    ----------

    brightness : float
      Passed on as it is.
    """
    #  void QQuick3DAbstractLight::setBrightness(float brightness)
    self.uglySide.call(
        'ritual_ZN21QQuick3DAbstractLight13setBrightnessEf', brightness,
    )

  @overload(QQuick3DNode)
  @overload(NoneType)
  def setScope(self, scope: Optional[QQuick3DNode]) -> None:
    """
    Calls Qt's 'void QQuick3DAbstractLight::setScope(QQuick3DNode *scope)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dabstractlight.html#setScope

    Parameters
    ----------

    scope : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DAbstractLight::setScope(QQuick3DNode *scope)
    self.uglySide.call(
        'ritual_ZN21QQuick3DAbstractLight8setScopeEP12QQuick3DNode',
        self._addressOf(scope),
    )

  @overload(bool)
  def setCastsShadow(self, castsShadow: bool) -> None:
    """
    Calls Qt's 'void QQuick3DAbstractLight::setCastsShadow(bool
    castsShadow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dabstractlight.html#setCastsShadow

    Parameters
    ----------

    castsShadow : bool
      Passed on as it is.
    """
    #  void QQuick3DAbstractLight::setCastsShadow(bool castsShadow)
    self.uglySide.call(
        'ritual_ZN21QQuick3DAbstractLight14setCastsShadowEb', castsShadow,
    )

  @overload(float)
  def setShadowBias(self, shadowBias: float) -> None:
    """
    Calls Qt's 'void QQuick3DAbstractLight::setShadowBias(float shadowBias)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dabstractlight.html#setShadowBias

    Parameters
    ----------

    shadowBias : float
      Passed on as it is.
    """
    #  void QQuick3DAbstractLight::setShadowBias(float shadowBias)
    self.uglySide.call(
        'ritual_ZN21QQuick3DAbstractLight13setShadowBiasEf', shadowBias,
    )

  @overload(float)
  def setShadowFactor(self, shadowFactor: float) -> None:
    """
    Calls Qt's 'void QQuick3DAbstractLight::setShadowFactor(float
    shadowFactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dabstractlight.html#setShadowFactor

    Parameters
    ----------

    shadowFactor : float
      Passed on as it is.
    """
    #  void QQuick3DAbstractLight::setShadowFactor(float shadowFactor)
    self.uglySide.call(
        'ritual_ZN21QQuick3DAbstractLight15setShadowFactorEf', shadowFactor,
    )

  @overload(QSSGShadowMapQuality)
  def setShadowMapQuality(
      self,
      shadowMapQuality: QSSGShadowMapQuality,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DAbstractLight::setShadowMapQuality(QQuick3DAbstractLight::
    QSSGShadowMapQuality shadowMapQuality)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dabstractlight.html#setShadowMapQuality

    Parameters
    ----------

    shadowMapQuality : QSSGShadowMapQuality
      Passed on as its number.
    """
    #  void QQuick3DAbstractLight::setShadowMapQuality(
    #      QQuick3DAbstractLight::QSSGShadowMapQuality shadowMapQuality)
    self.uglySide.call(
        'ritual_ZN21QQuick3DAbstractLight19setShadowMapQualityENS_20QSSGSha'
        'dowMapQualityE',
        shadowMapQuality.value,
    )

  @overload(float)
  def setShadowMapFar(self, shadowMapFar: float) -> None:
    """
    Calls Qt's 'void QQuick3DAbstractLight::setShadowMapFar(float
    shadowMapFar)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dabstractlight.html#setShadowMapFar

    Parameters
    ----------

    shadowMapFar : float
      Passed on as it is.
    """
    #  void QQuick3DAbstractLight::setShadowMapFar(float shadowMapFar)
    self.uglySide.call(
        'ritual_ZN21QQuick3DAbstractLight15setShadowMapFarEf', shadowMapFar,
    )

  @overload(float)
  def setShadowFilter(self, shadowFilter: float) -> None:
    """
    Calls Qt's 'void QQuick3DAbstractLight::setShadowFilter(float
    shadowFilter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dabstractlight.html#setShadowFilter

    Parameters
    ----------

    shadowFilter : float
      Passed on as it is.
    """
    #  void QQuick3DAbstractLight::setShadowFilter(float shadowFilter)
    self.uglySide.call(
        'ritual_ZN21QQuick3DAbstractLight15setShadowFilterEf', shadowFilter,
    )

  @overload(QSSGBakeMode)
  def setBakeMode(self, bakeMode: QSSGBakeMode) -> None:
    """
    Calls Qt's 'void
    QQuick3DAbstractLight::setBakeMode(QQuick3DAbstractLight::QSSGBakeMode
    bakeMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dabstractlight.html#setBakeMode

    Parameters
    ----------

    bakeMode : QSSGBakeMode
      Passed on as its number.
    """
    #  void QQuick3DAbstractLight::setBakeMode(QQuick3DAbstractLight::
    #      QSSGBakeMode bakeMode)
    self.uglySide.call(
        'ritual_ZN21QQuick3DAbstractLight11setBakeModeENS_12QSSGBakeModeE',
        bakeMode.value,
    )

  @overload(QSSGSoftShadowQuality)
  def setSoftShadowQuality(
      self,
      softShadowQuality: QSSGSoftShadowQuality,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DAbstractLight::setSoftShadowQuality(QQuick3DAbstractLight::
    QSSGSoftShadowQuality softShadowQuality)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dabstractlight.html#setSoftShadowQuality

    Parameters
    ----------

    softShadowQuality : QSSGSoftShadowQuality
      Passed on as its number.
    """
    #  void QQuick3DAbstractLight::setSoftShadowQuality(
    #      QQuick3DAbstractLight::QSSGSoftShadowQuality softShadowQuality)
    self.uglySide.call(
        'ritual_ZN21QQuick3DAbstractLight20setSoftShadowQualityENS_21QSSGSo'
        'ftShadowQualityE',
        softShadowQuality.value,
    )

  @overload(float)
  def setPcfFactor(self, pcfFactor: float) -> None:
    """
    Calls Qt's 'void QQuick3DAbstractLight::setPcfFactor(float pcfFactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dabstractlight.html#setPcfFactor

    Parameters
    ----------

    pcfFactor : float
      Passed on as it is.
    """
    #  void QQuick3DAbstractLight::setPcfFactor(float pcfFactor)
    self.uglySide.call(
        'ritual_ZN21QQuick3DAbstractLight12setPcfFactorEf', pcfFactor,
    )

  @overload(bool)
  def setUse32BitShadowmap(self, use32BitShadowmap: bool) -> None:
    """
    Calls Qt's 'void QQuick3DAbstractLight::setUse32BitShadowmap(bool
    use32BitShadowmap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dabstractlight.html#setUse32BitShadowmap

    Parameters
    ----------

    use32BitShadowmap : bool
      Passed on as it is.
    """
    #  void QQuick3DAbstractLight::setUse32BitShadowmap(bool
    #      use32BitShadowmap)
    self.uglySide.call(
        'ritual_ZN21QQuick3DAbstractLight20setUse32BitShadowmapEb',
        use32BitShadowmap,
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
    Qt's 'QQuick3DAbstractLight::QQuick3DAbstractLight(QQuick3DNodePrivate
    &dd, QQuick3DNode *parent)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QQuick3DAbstractLight.__init__' has no cute function yet. Qt's "
        "'QQuick3DAbstractLight::QQuick3DAbstractLight(QQuick3DNodePrivate "
        "&dd, QQuick3DNode *parent)': takes a type Python has no way to "
        "hand over yet.")

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

  def colorChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DAbstractLight::colorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dabstractlight.html#colorChanged
    """
    #  void QQuick3DAbstractLight::colorChanged()
    self.uglySide.call('ritual_ZN21QQuick3DAbstractLight12colorChangedEv')

  def ambientColorChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DAbstractLight::ambientColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dabstractlight.html#ambientColorChanged
    """
    #  void QQuick3DAbstractLight::ambientColorChanged()
    self.uglySide.call(
        'ritual_ZN21QQuick3DAbstractLight19ambientColorChangedEv',
    )

  def brightnessChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DAbstractLight::brightnessChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dabstractlight.html#brightnessChanged
    """
    #  void QQuick3DAbstractLight::brightnessChanged()
    self.uglySide.call(
        'ritual_ZN21QQuick3DAbstractLight17brightnessChangedEv',
    )

  def scopeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DAbstractLight::scopeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dabstractlight.html#scopeChanged
    """
    #  void QQuick3DAbstractLight::scopeChanged()
    self.uglySide.call('ritual_ZN21QQuick3DAbstractLight12scopeChangedEv')

  def castsShadowChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DAbstractLight::castsShadowChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dabstractlight.html#castsShadowChanged
    """
    #  void QQuick3DAbstractLight::castsShadowChanged()
    self.uglySide.call(
        'ritual_ZN21QQuick3DAbstractLight18castsShadowChangedEv',
    )

  def shadowBiasChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DAbstractLight::shadowBiasChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dabstractlight.html#shadowBiasChanged
    """
    #  void QQuick3DAbstractLight::shadowBiasChanged()
    self.uglySide.call(
        'ritual_ZN21QQuick3DAbstractLight17shadowBiasChangedEv',
    )

  def shadowFactorChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DAbstractLight::shadowFactorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dabstractlight.html#shadowFactorChanged
    """
    #  void QQuick3DAbstractLight::shadowFactorChanged()
    self.uglySide.call(
        'ritual_ZN21QQuick3DAbstractLight19shadowFactorChangedEv',
    )

  def shadowMapQualityChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DAbstractLight::shadowMapQualityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dabstractlight.html#shadowMapQualityChanged
    """
    #  void QQuick3DAbstractLight::shadowMapQualityChanged()
    self.uglySide.call(
        'ritual_ZN21QQuick3DAbstractLight23shadowMapQualityChangedEv',
    )

  def shadowMapFarChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DAbstractLight::shadowMapFarChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dabstractlight.html#shadowMapFarChanged
    """
    #  void QQuick3DAbstractLight::shadowMapFarChanged()
    self.uglySide.call(
        'ritual_ZN21QQuick3DAbstractLight19shadowMapFarChangedEv',
    )

  def shadowFilterChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DAbstractLight::shadowFilterChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dabstractlight.html#shadowFilterChanged
    """
    #  void QQuick3DAbstractLight::shadowFilterChanged()
    self.uglySide.call(
        'ritual_ZN21QQuick3DAbstractLight19shadowFilterChangedEv',
    )

  def bakeModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DAbstractLight::bakeModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dabstractlight.html#bakeModeChanged
    """
    #  void QQuick3DAbstractLight::bakeModeChanged()
    self.uglySide.call('ritual_ZN21QQuick3DAbstractLight15bakeModeChangedEv')

  def softShadowQualityChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DAbstractLight::softShadowQualityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dabstractlight.html
    """
    #  void QQuick3DAbstractLight::softShadowQualityChanged()
    self.uglySide.call(
        'ritual_ZN21QQuick3DAbstractLight24softShadowQualityChangedEv',
    )

  def pcfFactorChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DAbstractLight::pcfFactorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dabstractlight.html#pcfFactorChanged
    """
    #  void QQuick3DAbstractLight::pcfFactorChanged()
    self.uglySide.call(
        'ritual_ZN21QQuick3DAbstractLight16pcfFactorChangedEv',
    )

  def use32BitShadowmapChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DAbstractLight::use32BitShadowmapChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dabstractlight.html
    """
    #  void QQuick3DAbstractLight::use32BitShadowmapChanged()
    self.uglySide.call(
        'ritual_ZN21QQuick3DAbstractLight24use32BitShadowmapChangedEv',
    )

  @overload(QSSGRenderGraphObject)
  @overload(NoneType)
  def updateSpatialNode(
      self,
      node: Optional[QSSGRenderGraphObject],
  ) -> Optional[QSSGRenderGraphObject]:
    """
    Calls Qt's 'QSSGRenderGraphObject
    *QQuick3DAbstractLight::updateSpatialNode(QSSGRenderGraphObject *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dabstractlight.html#updateSpatialNode

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
    #      *QQuick3DAbstractLight::updateSpatialNode(QSSGRenderGraphObject
    #      *node)
    ritual = (
        'ritual_ZN21QQuick3DAbstractLight17updateSpatialNodeEP21QSSGRenderG'
        'raphObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuick3DAbstractLight17updateSpatialNodeEP21QSSGR'
          'enderGraphObject')
    address = self.uglySide.call(ritual, self._addressOf(node))
    from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
    return QSSGRenderGraphObject._cuteAt(address)

  def markAllDirty(self) -> None:
    """
    Calls Qt's 'void QQuick3DAbstractLight::markAllDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dabstractlight.html#markAllDirty
    """
    #  void QQuick3DAbstractLight::markAllDirty()
    ritual = 'ritual_ZN21QQuick3DAbstractLight12markAllDirtyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QQuick3DAbstractLight12markAllDirtyEv'
    self.uglySide.call(ritual)

  @overload(QSSGShadowMapQuality)
  def mapToShadowResolution(self, resolution: QSSGShadowMapQuality) -> int:
    """
    Calls Qt's 'quint32
    QQuick3DAbstractLight::mapToShadowResolution(QSSGShadowMapQuality
    resolution)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dabstractlight.html#mapToShadowResolution

    Parameters
    ----------

    resolution : QSSGShadowMapQuality
      Passed on as its number.
    """
    #  quint32
    #      QQuick3DAbstractLight::mapToShadowResolution(QSSGShadowMapQuality
    #      resolution)
    return self.uglySide.call(
        'ritual_ZN21QQuick3DAbstractLight21mapToShadowResolutionENS_20QSSGS'
        'hadowMapQualityE',
        resolution.value,
    )
