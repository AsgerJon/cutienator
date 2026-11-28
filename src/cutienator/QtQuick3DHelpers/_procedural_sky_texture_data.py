"""
ProceduralSkyTextureData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/proceduralskytexturedata_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means ProceduralSkyTextureData to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QColor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ProceduralSkyTextureData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's ProceduralSkyTextureData: a plain Python object
  standing in front of one C++ ProceduralSkyTextureData.

  What exists
  -----------

  Every function of Qt's ProceduralSkyTextureData that has a ritual and that
  Python can call so far, 52 names in all: 'metaObject', 'tr', 'skyTopColor',
  'skyHorizonColor', 'skyCurve', 'skyEnergy', 'groundBottomColor',
  'groundHorizonColor', 'groundCurve', 'groundEnergy', 'sunColor',
  'sunLatitude', 'sunLongitude', 'sunAngleMin', 'sunAngleMax', 'sunCurve',
  'sunEnergy', 'textureQuality', 'setSkyTopColor', 'setSkyHorizonColor',
  'setSkyCurve', 'setSkyEnergy', 'setGroundBottomColor',
  'setGroundHorizonColor', 'setGroundCurve', 'setGroundEnergy',
  'setSunColor', 'setSunLatitude', 'setSunLongitude', 'setSunAngleMin',
  'setSunAngleMax', 'setSunCurve', 'setSunEnergy', 'setTextureQuality',
  'generateRGBA16FTexture', 'skyTopColorChanged', 'skyHorizonColorChanged',
  'skyCurveChanged', 'skyEnergyChanged', 'groundBottomColorChanged',
  'groundHorizonColorChanged', 'groundCurveChanged', 'groundEnergyChanged',
  'sunColorChanged', 'sunLatitudeChanged', 'sunLongitudeChanged',
  'sunAngleMinChanged', 'sunAngleMaxChanged', 'sunCurveChanged',
  'sunEnergyChanged', 'textureQualityChanged', 'scheduleTextureUpdate'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *ProceduralSkyTextureData::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int ProceduralSkyTextureData::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'ProceduralSkyTextureData::~ProceduralSkyTextureData()': the
    destructor: Python never removes a C++ ProceduralSkyTextureData.
  - Qt's 'QByteArray ProceduralSkyTextureData::generateSkyTexture(int width,
    int height, QByteArray &imageData, bool isRGBE) const': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 59 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ ProceduralSkyTextureData is created at the first use, not by
    'ProceduralSkyTextureData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ ProceduralSkyTextureData.
  - Qt tells when it has removed the C++ ProceduralSkyTextureData. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's ProceduralSkyTextureData that has no cute function yet,
    'generateSkyTexture', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside ProceduralSkyTextureData, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class SkyTextureQuality(CuteNum, scoped=True):
    """
    The enum 'ProceduralSkyTextureData::SkyTextureQuality' of Qt, with the 4
    names Qt gives in it. C++ keeps these names inside the enum, so the class
    that holds the enum does not have them.
    """

    SkyTextureQualityLow = Kee[int](0)
    SkyTextureQualityMedium = Kee[int](1)
    SkyTextureQualityHigh = Kee[int](2)
    SkyTextureQualityVeryHigh = Kee[int](3)

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
    Calls Qt's 'QString ProceduralSkyTextureData::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/proceduralskytexturedata.html#tr

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
    #  QString ProceduralSkyTextureData::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24ProceduralSkyTextureData2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'ProceduralSkyTextureData'

  #  A C++ ProceduralSkyTextureData Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_ProceduralSkyTextureData'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *ProceduralSkyTextureData::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *ProceduralSkyTextureData::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24ProceduralSkyTextureData10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def skyTopColor(self) -> QColor:
    """
    Calls Qt's 'QColor ProceduralSkyTextureData::skyTopColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html#skyTopColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor ProceduralSkyTextureData::skyTopColor() const
    address = self.uglySide.call(
        'ritual_ZNK24ProceduralSkyTextureData11skyTopColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def skyHorizonColor(self) -> QColor:
    """
    Calls Qt's 'QColor ProceduralSkyTextureData::skyHorizonColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html#skyHorizonColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor ProceduralSkyTextureData::skyHorizonColor() const
    address = self.uglySide.call(
        'ritual_ZNK24ProceduralSkyTextureData15skyHorizonColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def skyCurve(self) -> float:
    """
    Calls Qt's 'float ProceduralSkyTextureData::skyCurve() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html#skyCurve
    """
    #  float ProceduralSkyTextureData::skyCurve() const
    return self.uglySide.call(
        'ritual_ZNK24ProceduralSkyTextureData8skyCurveEv',
    )

  def skyEnergy(self) -> float:
    """
    Calls Qt's 'float ProceduralSkyTextureData::skyEnergy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html#skyEnergy
    """
    #  float ProceduralSkyTextureData::skyEnergy() const
    return self.uglySide.call(
        'ritual_ZNK24ProceduralSkyTextureData9skyEnergyEv',
    )

  def groundBottomColor(self) -> QColor:
    """
    Calls Qt's 'QColor ProceduralSkyTextureData::groundBottomColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html#groundBottomColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor ProceduralSkyTextureData::groundBottomColor() const
    address = self.uglySide.call(
        'ritual_ZNK24ProceduralSkyTextureData17groundBottomColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def groundHorizonColor(self) -> QColor:
    """
    Calls Qt's 'QColor ProceduralSkyTextureData::groundHorizonColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html#groundHorizonColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor ProceduralSkyTextureData::groundHorizonColor() const
    address = self.uglySide.call(
        'ritual_ZNK24ProceduralSkyTextureData18groundHorizonColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def groundCurve(self) -> float:
    """
    Calls Qt's 'float ProceduralSkyTextureData::groundCurve() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html#groundCurve
    """
    #  float ProceduralSkyTextureData::groundCurve() const
    return self.uglySide.call(
        'ritual_ZNK24ProceduralSkyTextureData11groundCurveEv',
    )

  def groundEnergy(self) -> float:
    """
    Calls Qt's 'float ProceduralSkyTextureData::groundEnergy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html#groundEnergy
    """
    #  float ProceduralSkyTextureData::groundEnergy() const
    return self.uglySide.call(
        'ritual_ZNK24ProceduralSkyTextureData12groundEnergyEv',
    )

  def sunColor(self) -> QColor:
    """
    Calls Qt's 'QColor ProceduralSkyTextureData::sunColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html#sunColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor ProceduralSkyTextureData::sunColor() const
    address = self.uglySide.call(
        'ritual_ZNK24ProceduralSkyTextureData8sunColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def sunLatitude(self) -> float:
    """
    Calls Qt's 'float ProceduralSkyTextureData::sunLatitude() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html#sunLatitude
    """
    #  float ProceduralSkyTextureData::sunLatitude() const
    return self.uglySide.call(
        'ritual_ZNK24ProceduralSkyTextureData11sunLatitudeEv',
    )

  def sunLongitude(self) -> float:
    """
    Calls Qt's 'float ProceduralSkyTextureData::sunLongitude() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html#sunLongitude
    """
    #  float ProceduralSkyTextureData::sunLongitude() const
    return self.uglySide.call(
        'ritual_ZNK24ProceduralSkyTextureData12sunLongitudeEv',
    )

  def sunAngleMin(self) -> float:
    """
    Calls Qt's 'float ProceduralSkyTextureData::sunAngleMin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html#sunAngleMin
    """
    #  float ProceduralSkyTextureData::sunAngleMin() const
    return self.uglySide.call(
        'ritual_ZNK24ProceduralSkyTextureData11sunAngleMinEv',
    )

  def sunAngleMax(self) -> float:
    """
    Calls Qt's 'float ProceduralSkyTextureData::sunAngleMax() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html#sunAngleMax
    """
    #  float ProceduralSkyTextureData::sunAngleMax() const
    return self.uglySide.call(
        'ritual_ZNK24ProceduralSkyTextureData11sunAngleMaxEv',
    )

  def sunCurve(self) -> float:
    """
    Calls Qt's 'float ProceduralSkyTextureData::sunCurve() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html#sunCurve
    """
    #  float ProceduralSkyTextureData::sunCurve() const
    return self.uglySide.call(
        'ritual_ZNK24ProceduralSkyTextureData8sunCurveEv',
    )

  def sunEnergy(self) -> float:
    """
    Calls Qt's 'float ProceduralSkyTextureData::sunEnergy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html#sunEnergy
    """
    #  float ProceduralSkyTextureData::sunEnergy() const
    return self.uglySide.call(
        'ritual_ZNK24ProceduralSkyTextureData9sunEnergyEv',
    )

  def textureQuality(self) -> SkyTextureQuality:
    """
    Calls Qt's 'SkyTextureQuality ProceduralSkyTextureData::textureQuality()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html#textureQuality

    Returns
    -------

    SkyTextureQuality
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'SkyTextureQuality(number)' gives.
    """
    #  SkyTextureQuality ProceduralSkyTextureData::textureQuality() const
    return ProceduralSkyTextureData.SkyTextureQuality(self.uglySide.call(
        'ritual_ZNK24ProceduralSkyTextureData14textureQualityEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setSkyTopColor(self, skyTopColor: QColor) -> None:
    """
    Calls Qt's 'void ProceduralSkyTextureData::setSkyTopColor(QColor
    skyTopColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html#setSkyTopColor

    Parameters
    ----------

    skyTopColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void ProceduralSkyTextureData::setSkyTopColor(QColor skyTopColor)
    self.uglySide.call(
        'ritual_ZN24ProceduralSkyTextureData14setSkyTopColorE6QColor',
        self._valueOf(skyTopColor),
    )

  @overload(QColor)
  def setSkyHorizonColor(self, skyHorizonColor: QColor) -> None:
    """
    Calls Qt's 'void ProceduralSkyTextureData::setSkyHorizonColor(QColor
    skyHorizonColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html#setSkyHorizonColor

    Parameters
    ----------

    skyHorizonColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void ProceduralSkyTextureData::setSkyHorizonColor(QColor
    #      skyHorizonColor)
    self.uglySide.call(
        'ritual_ZN24ProceduralSkyTextureData18setSkyHorizonColorE6QColor',
        self._valueOf(skyHorizonColor),
    )

  @overload(float)
  def setSkyCurve(self, skyCurve: float) -> None:
    """
    Calls Qt's 'void ProceduralSkyTextureData::setSkyCurve(float skyCurve)'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html#setSkyCurve

    Parameters
    ----------

    skyCurve : float
      Passed on as it is.
    """
    #  void ProceduralSkyTextureData::setSkyCurve(float skyCurve)
    self.uglySide.call(
        'ritual_ZN24ProceduralSkyTextureData11setSkyCurveEf', skyCurve,
    )

  @overload(float)
  def setSkyEnergy(self, skyEnergy: float) -> None:
    """
    Calls Qt's 'void ProceduralSkyTextureData::setSkyEnergy(float
    skyEnergy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html#setSkyEnergy

    Parameters
    ----------

    skyEnergy : float
      Passed on as it is.
    """
    #  void ProceduralSkyTextureData::setSkyEnergy(float skyEnergy)
    self.uglySide.call(
        'ritual_ZN24ProceduralSkyTextureData12setSkyEnergyEf', skyEnergy,
    )

  @overload(QColor)
  def setGroundBottomColor(self, groundBottomColor: QColor) -> None:
    """
    Calls Qt's 'void ProceduralSkyTextureData::setGroundBottomColor(QColor
    groundBottomColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html#setGroundBottomColor

    Parameters
    ----------

    groundBottomColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void ProceduralSkyTextureData::setGroundBottomColor(QColor
    #      groundBottomColor)
    self.uglySide.call(
        'ritual_ZN24ProceduralSkyTextureData20setGroundBottomColorE6QColor',
        self._valueOf(groundBottomColor),
    )

  @overload(QColor)
  def setGroundHorizonColor(self, groundHorizonColor: QColor) -> None:
    """
    Calls Qt's 'void ProceduralSkyTextureData::setGroundHorizonColor(QColor
    groundHorizonColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html

    Parameters
    ----------

    groundHorizonColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void ProceduralSkyTextureData::setGroundHorizonColor(QColor
    #      groundHorizonColor)
    self.uglySide.call(
        'ritual_ZN24ProceduralSkyTextureData21setGroundHorizonColorE6QColor',
        self._valueOf(groundHorizonColor),
    )

  @overload(float)
  def setGroundCurve(self, groundCurve: float) -> None:
    """
    Calls Qt's 'void ProceduralSkyTextureData::setGroundCurve(float
    groundCurve)'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html#setGroundCurve

    Parameters
    ----------

    groundCurve : float
      Passed on as it is.
    """
    #  void ProceduralSkyTextureData::setGroundCurve(float groundCurve)
    self.uglySide.call(
        'ritual_ZN24ProceduralSkyTextureData14setGroundCurveEf', groundCurve,
    )

  @overload(float)
  def setGroundEnergy(self, groundEnergy: float) -> None:
    """
    Calls Qt's 'void ProceduralSkyTextureData::setGroundEnergy(float
    groundEnergy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html#setGroundEnergy

    Parameters
    ----------

    groundEnergy : float
      Passed on as it is.
    """
    #  void ProceduralSkyTextureData::setGroundEnergy(float groundEnergy)
    self.uglySide.call(
        'ritual_ZN24ProceduralSkyTextureData15setGroundEnergyEf',
        groundEnergy,
    )

  @overload(QColor)
  def setSunColor(self, sunColor: QColor) -> None:
    """
    Calls Qt's 'void ProceduralSkyTextureData::setSunColor(QColor sunColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html#setSunColor

    Parameters
    ----------

    sunColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void ProceduralSkyTextureData::setSunColor(QColor sunColor)
    self.uglySide.call(
        'ritual_ZN24ProceduralSkyTextureData11setSunColorE6QColor',
        self._valueOf(sunColor),
    )

  @overload(float)
  def setSunLatitude(self, sunLatitude: float) -> None:
    """
    Calls Qt's 'void ProceduralSkyTextureData::setSunLatitude(float
    sunLatitude)'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html#setSunLatitude

    Parameters
    ----------

    sunLatitude : float
      Passed on as it is.
    """
    #  void ProceduralSkyTextureData::setSunLatitude(float sunLatitude)
    self.uglySide.call(
        'ritual_ZN24ProceduralSkyTextureData14setSunLatitudeEf', sunLatitude,
    )

  @overload(float)
  def setSunLongitude(self, sunLongitude: float) -> None:
    """
    Calls Qt's 'void ProceduralSkyTextureData::setSunLongitude(float
    sunLongitude)'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html#setSunLongitude

    Parameters
    ----------

    sunLongitude : float
      Passed on as it is.
    """
    #  void ProceduralSkyTextureData::setSunLongitude(float sunLongitude)
    self.uglySide.call(
        'ritual_ZN24ProceduralSkyTextureData15setSunLongitudeEf',
        sunLongitude,
    )

  @overload(float)
  def setSunAngleMin(self, sunAngleMin: float) -> None:
    """
    Calls Qt's 'void ProceduralSkyTextureData::setSunAngleMin(float
    sunAngleMin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html#setSunAngleMin

    Parameters
    ----------

    sunAngleMin : float
      Passed on as it is.
    """
    #  void ProceduralSkyTextureData::setSunAngleMin(float sunAngleMin)
    self.uglySide.call(
        'ritual_ZN24ProceduralSkyTextureData14setSunAngleMinEf', sunAngleMin,
    )

  @overload(float)
  def setSunAngleMax(self, sunAngleMax: float) -> None:
    """
    Calls Qt's 'void ProceduralSkyTextureData::setSunAngleMax(float
    sunAngleMax)'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html#setSunAngleMax

    Parameters
    ----------

    sunAngleMax : float
      Passed on as it is.
    """
    #  void ProceduralSkyTextureData::setSunAngleMax(float sunAngleMax)
    self.uglySide.call(
        'ritual_ZN24ProceduralSkyTextureData14setSunAngleMaxEf', sunAngleMax,
    )

  @overload(float)
  def setSunCurve(self, sunCurve: float) -> None:
    """
    Calls Qt's 'void ProceduralSkyTextureData::setSunCurve(float sunCurve)'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html#setSunCurve

    Parameters
    ----------

    sunCurve : float
      Passed on as it is.
    """
    #  void ProceduralSkyTextureData::setSunCurve(float sunCurve)
    self.uglySide.call(
        'ritual_ZN24ProceduralSkyTextureData11setSunCurveEf', sunCurve,
    )

  @overload(float)
  def setSunEnergy(self, sunEnergy: float) -> None:
    """
    Calls Qt's 'void ProceduralSkyTextureData::setSunEnergy(float
    sunEnergy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html#setSunEnergy

    Parameters
    ----------

    sunEnergy : float
      Passed on as it is.
    """
    #  void ProceduralSkyTextureData::setSunEnergy(float sunEnergy)
    self.uglySide.call(
        'ritual_ZN24ProceduralSkyTextureData12setSunEnergyEf', sunEnergy,
    )

  @overload(SkyTextureQuality)
  def setTextureQuality(self, textureQuality: SkyTextureQuality) -> None:
    """
    Calls Qt's 'void
    ProceduralSkyTextureData::setTextureQuality(SkyTextureQuality
    textureQuality)'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html#setTextureQuality

    Parameters
    ----------

    textureQuality : SkyTextureQuality
      Passed on as its number.
    """
    #  void ProceduralSkyTextureData::setTextureQuality(SkyTextureQuality
    #      textureQuality)
    self.uglySide.call(
        'ritual_ZN24ProceduralSkyTextureData17setTextureQualityENS_17SkyTex'
        'tureQualityE',
        textureQuality.value,
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
    'ProceduralSkyTextureData::ProceduralSkyTextureData()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html
    """
    #  ProceduralSkyTextureData::ProceduralSkyTextureData()
    self._noteCreation(ProceduralSkyTextureData, lambda: Rituals.call(
        'ritual_ZN24ProceduralSkyTextureDataC1Ev',
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

  def generateRGBA16FTexture(self) -> None:
    """
    Calls Qt's 'void ProceduralSkyTextureData::generateRGBA16FTexture()'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html
    """
    #  void ProceduralSkyTextureData::generateRGBA16FTexture()
    self.uglySide.call(
        'ritual_ZN24ProceduralSkyTextureData22generateRGBA16FTextureEv',
    )

  @overload(QColor)
  def skyTopColorChanged(self, skyTopColor: QColor) -> None:
    """
    Calls Qt's 'void ProceduralSkyTextureData::skyTopColorChanged(QColor
    skyTopColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html#skyTopColorChanged

    Parameters
    ----------

    skyTopColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void ProceduralSkyTextureData::skyTopColorChanged(QColor skyTopColor)
    self.uglySide.call(
        'ritual_ZN24ProceduralSkyTextureData18skyTopColorChangedE6QColor',
        self._valueOf(skyTopColor),
    )

  @overload(QColor)
  def skyHorizonColorChanged(self, skyHorizonColor: QColor) -> None:
    """
    Calls Qt's 'void ProceduralSkyTextureData::skyHorizonColorChanged(QColor
    skyHorizonColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html

    Parameters
    ----------

    skyHorizonColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void ProceduralSkyTextureData::skyHorizonColorChanged(QColor
    #      skyHorizonColor)
    self.uglySide.call(
        'ritual_ZN24ProceduralSkyTextureData22skyHorizonColorChangedE6QColo'
        'r',
        self._valueOf(skyHorizonColor),
    )

  @overload(float)
  def skyCurveChanged(self, skyCurve: float) -> None:
    """
    Calls Qt's 'void ProceduralSkyTextureData::skyCurveChanged(float
    skyCurve)'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html#skyCurveChanged

    Parameters
    ----------

    skyCurve : float
      Passed on as it is.
    """
    #  void ProceduralSkyTextureData::skyCurveChanged(float skyCurve)
    self.uglySide.call(
        'ritual_ZN24ProceduralSkyTextureData15skyCurveChangedEf', skyCurve,
    )

  @overload(float)
  def skyEnergyChanged(self, skyEnergy: float) -> None:
    """
    Calls Qt's 'void ProceduralSkyTextureData::skyEnergyChanged(float
    skyEnergy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html#skyEnergyChanged

    Parameters
    ----------

    skyEnergy : float
      Passed on as it is.
    """
    #  void ProceduralSkyTextureData::skyEnergyChanged(float skyEnergy)
    self.uglySide.call(
        'ritual_ZN24ProceduralSkyTextureData16skyEnergyChangedEf', skyEnergy,
    )

  @overload(QColor)
  def groundBottomColorChanged(self, groundBottomColor: QColor) -> None:
    """
    Calls Qt's 'void
    ProceduralSkyTextureData::groundBottomColorChanged(QColor
    groundBottomColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html

    Parameters
    ----------

    groundBottomColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void ProceduralSkyTextureData::groundBottomColorChanged(QColor
    #      groundBottomColor)
    self.uglySide.call(
        'ritual_ZN24ProceduralSkyTextureData24groundBottomColorChangedE6QCo'
        'lor',
        self._valueOf(groundBottomColor),
    )

  @overload(QColor)
  def groundHorizonColorChanged(self, groundHorizonColor: QColor) -> None:
    """
    Calls Qt's 'void
    ProceduralSkyTextureData::groundHorizonColorChanged(QColor
    groundHorizonColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html

    Parameters
    ----------

    groundHorizonColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void ProceduralSkyTextureData::groundHorizonColorChanged(QColor
    #      groundHorizonColor)
    self.uglySide.call(
        'ritual_ZN24ProceduralSkyTextureData25groundHorizonColorChangedE6QC'
        'olor',
        self._valueOf(groundHorizonColor),
    )

  @overload(float)
  def groundCurveChanged(self, groundCurve: float) -> None:
    """
    Calls Qt's 'void ProceduralSkyTextureData::groundCurveChanged(float
    groundCurve)'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html#groundCurveChanged

    Parameters
    ----------

    groundCurve : float
      Passed on as it is.
    """
    #  void ProceduralSkyTextureData::groundCurveChanged(float groundCurve)
    self.uglySide.call(
        'ritual_ZN24ProceduralSkyTextureData18groundCurveChangedEf',
        groundCurve,
    )

  @overload(float)
  def groundEnergyChanged(self, groundEnergy: float) -> None:
    """
    Calls Qt's 'void ProceduralSkyTextureData::groundEnergyChanged(float
    groundEnergy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html#groundEnergyChanged

    Parameters
    ----------

    groundEnergy : float
      Passed on as it is.
    """
    #  void ProceduralSkyTextureData::groundEnergyChanged(float groundEnergy)
    self.uglySide.call(
        'ritual_ZN24ProceduralSkyTextureData19groundEnergyChangedEf',
        groundEnergy,
    )

  @overload(QColor)
  def sunColorChanged(self, sunColor: QColor) -> None:
    """
    Calls Qt's 'void ProceduralSkyTextureData::sunColorChanged(QColor
    sunColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html#sunColorChanged

    Parameters
    ----------

    sunColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void ProceduralSkyTextureData::sunColorChanged(QColor sunColor)
    self.uglySide.call(
        'ritual_ZN24ProceduralSkyTextureData15sunColorChangedE6QColor',
        self._valueOf(sunColor),
    )

  @overload(float)
  def sunLatitudeChanged(self, sunLatitude: float) -> None:
    """
    Calls Qt's 'void ProceduralSkyTextureData::sunLatitudeChanged(float
    sunLatitude)'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html#sunLatitudeChanged

    Parameters
    ----------

    sunLatitude : float
      Passed on as it is.
    """
    #  void ProceduralSkyTextureData::sunLatitudeChanged(float sunLatitude)
    self.uglySide.call(
        'ritual_ZN24ProceduralSkyTextureData18sunLatitudeChangedEf',
        sunLatitude,
    )

  @overload(float)
  def sunLongitudeChanged(self, sunLongitude: float) -> None:
    """
    Calls Qt's 'void ProceduralSkyTextureData::sunLongitudeChanged(float
    sunLongitude)'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html#sunLongitudeChanged

    Parameters
    ----------

    sunLongitude : float
      Passed on as it is.
    """
    #  void ProceduralSkyTextureData::sunLongitudeChanged(float sunLongitude)
    self.uglySide.call(
        'ritual_ZN24ProceduralSkyTextureData19sunLongitudeChangedEf',
        sunLongitude,
    )

  @overload(float)
  def sunAngleMinChanged(self, sunAngleMin: float) -> None:
    """
    Calls Qt's 'void ProceduralSkyTextureData::sunAngleMinChanged(float
    sunAngleMin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html#sunAngleMinChanged

    Parameters
    ----------

    sunAngleMin : float
      Passed on as it is.
    """
    #  void ProceduralSkyTextureData::sunAngleMinChanged(float sunAngleMin)
    self.uglySide.call(
        'ritual_ZN24ProceduralSkyTextureData18sunAngleMinChangedEf',
        sunAngleMin,
    )

  @overload(float)
  def sunAngleMaxChanged(self, sunAngleMax: float) -> None:
    """
    Calls Qt's 'void ProceduralSkyTextureData::sunAngleMaxChanged(float
    sunAngleMax)'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html#sunAngleMaxChanged

    Parameters
    ----------

    sunAngleMax : float
      Passed on as it is.
    """
    #  void ProceduralSkyTextureData::sunAngleMaxChanged(float sunAngleMax)
    self.uglySide.call(
        'ritual_ZN24ProceduralSkyTextureData18sunAngleMaxChangedEf',
        sunAngleMax,
    )

  @overload(float)
  def sunCurveChanged(self, sunCurve: float) -> None:
    """
    Calls Qt's 'void ProceduralSkyTextureData::sunCurveChanged(float
    sunCurve)'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html#sunCurveChanged

    Parameters
    ----------

    sunCurve : float
      Passed on as it is.
    """
    #  void ProceduralSkyTextureData::sunCurveChanged(float sunCurve)
    self.uglySide.call(
        'ritual_ZN24ProceduralSkyTextureData15sunCurveChangedEf', sunCurve,
    )

  @overload(float)
  def sunEnergyChanged(self, sunEnergy: float) -> None:
    """
    Calls Qt's 'void ProceduralSkyTextureData::sunEnergyChanged(float
    sunEnergy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html#sunEnergyChanged

    Parameters
    ----------

    sunEnergy : float
      Passed on as it is.
    """
    #  void ProceduralSkyTextureData::sunEnergyChanged(float sunEnergy)
    self.uglySide.call(
        'ritual_ZN24ProceduralSkyTextureData16sunEnergyChangedEf', sunEnergy,
    )

  @overload(SkyTextureQuality)
  def textureQualityChanged(self, textureQuality: SkyTextureQuality) -> None:
    """
    Calls Qt's 'void
    ProceduralSkyTextureData::textureQualityChanged(SkyTextureQuality
    textureQuality)'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html

    Parameters
    ----------

    textureQuality : SkyTextureQuality
      Passed on as its number.
    """
    #  void ProceduralSkyTextureData::textureQualityChanged(SkyTextureQuality
    #      textureQuality)
    self.uglySide.call(
        'ritual_ZN24ProceduralSkyTextureData21textureQualityChangedENS_17Sk'
        'yTextureQualityE',
        textureQuality.value,
    )

  def scheduleTextureUpdate(self) -> None:
    """
    Calls Qt's 'void ProceduralSkyTextureData::scheduleTextureUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralskytexturedata.html
    """
    #  void ProceduralSkyTextureData::scheduleTextureUpdate()
    self.uglySide.call(
        'ritual_ZN24ProceduralSkyTextureData21scheduleTextureUpdateEv',
    )

  @staticmethod
  def generateSkyTexture(*__, **_) -> Never:
    """
    Qt's 'QByteArray ProceduralSkyTextureData::generateSkyTexture(int width,
    int height, QByteArray &imageData, bool isRGBE) const': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'ProceduralSkyTextureData.generateSkyTexture' has no cute function "
        "yet. Qt's 'QByteArray "
        "ProceduralSkyTextureData::generateSkyTexture(int width, int "
        "height, QByteArray &imageData, bool isRGBE) const': takes a type "
        "Python has no way to hand over yet.")
