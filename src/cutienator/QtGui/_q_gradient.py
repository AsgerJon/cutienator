"""
QGradient binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtGui/qbrush.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QColor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']


class QGradient(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGradient: a plain Python object standing in front of
  one C++ QGradient.

  C++ hands a QGradient around as a copy, so every C++ QGradient behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGradient that has a ritual and that Python can call
  so far, 10 names in all: 'type', 'setSpread', 'spread', 'setColorAt',
  'coordinateMode', 'setCoordinateMode', 'interpolationMode',
  'setInterpolationMode', '__eq__', '__ne__'. It can be made from Python, in
  2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGradient::~QGradient()': the destructor: Python removes its C++
    QGradient by it, and has no other use for it.

  What has no ritual
  ------------------

  5 of the 18 functions Qt declares: 2 takes or gives a type that cannot be
  passed yet; 1 declared and nowhere to be found; 1 a template; 1 private.

  What to expect
  --------------

  - The C++ QGradient is created at the first use, not by 'QGradient(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGradient back gives a copy the ritual made for
    Python, in a new cute QGradient.
  """

  #  The enums Qt writes inside QGradient, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class CoordinateMode(CuteNum):
    """
    The enum 'QGradient::CoordinateMode' of Qt, with the 4 names Qt gives in
    it.
    """

    LogicalMode = Kee[int](0)
    StretchToDeviceMode = Kee[int](1)
    ObjectBoundingMode = Kee[int](2)
    ObjectMode = Kee[int](3)

  class InterpolationMode(CuteNum):
    """
    The enum 'QGradient::InterpolationMode' of Qt, with the 2 names Qt gives
    in it.
    """

    ColorInterpolation = Kee[int](0)
    ComponentInterpolation = Kee[int](1)

  class Preset(CuteNum):
    """
    The enum 'QGradient::Preset' of Qt, with the 169 names Qt gives in it.
    """

    WarmFlame = Kee[int](1)
    NightFade = Kee[int](2)
    SpringWarmth = Kee[int](3)
    JuicyPeach = Kee[int](4)
    YoungPassion = Kee[int](5)
    LadyLips = Kee[int](6)
    SunnyMorning = Kee[int](7)
    RainyAshville = Kee[int](8)
    FrozenDreams = Kee[int](9)
    WinterNeva = Kee[int](10)
    DustyGrass = Kee[int](11)
    TemptingAzure = Kee[int](12)
    HeavyRain = Kee[int](13)
    AmyCrisp = Kee[int](14)
    MeanFruit = Kee[int](15)
    DeepBlue = Kee[int](16)
    RipeMalinka = Kee[int](17)
    CloudyKnoxville = Kee[int](18)
    MalibuBeach = Kee[int](19)
    NewLife = Kee[int](20)
    TrueSunset = Kee[int](21)
    MorpheusDen = Kee[int](22)
    RareWind = Kee[int](23)
    NearMoon = Kee[int](24)
    WildApple = Kee[int](25)
    SaintPetersburg = Kee[int](26)
    PlumPlate = Kee[int](28)
    EverlastingSky = Kee[int](29)
    HappyFisher = Kee[int](30)
    Blessing = Kee[int](31)
    SharpeyeEagle = Kee[int](32)
    LadogaBottom = Kee[int](33)
    LemonGate = Kee[int](34)
    ItmeoBranding = Kee[int](35)
    ZeusMiracle = Kee[int](36)
    OldHat = Kee[int](37)
    StarWine = Kee[int](38)
    HappyAcid = Kee[int](41)
    AwesomePine = Kee[int](42)
    NewYork = Kee[int](43)
    ShyRainbow = Kee[int](44)
    MixedHopes = Kee[int](46)
    FlyHigh = Kee[int](47)
    StrongBliss = Kee[int](48)
    FreshMilk = Kee[int](49)
    SnowAgain = Kee[int](50)
    FebruaryInk = Kee[int](51)
    KindSteel = Kee[int](52)
    SoftGrass = Kee[int](53)
    GrownEarly = Kee[int](54)
    SharpBlues = Kee[int](55)
    ShadyWater = Kee[int](56)
    DirtyBeauty = Kee[int](57)
    GreatWhale = Kee[int](58)
    TeenNotebook = Kee[int](59)
    PoliteRumors = Kee[int](60)
    SweetPeriod = Kee[int](61)
    WideMatrix = Kee[int](62)
    SoftCherish = Kee[int](63)
    RedSalvation = Kee[int](64)
    BurningSpring = Kee[int](65)
    NightParty = Kee[int](66)
    SkyGlider = Kee[int](67)
    HeavenPeach = Kee[int](68)
    PurpleDivision = Kee[int](69)
    AquaSplash = Kee[int](70)
    SpikyNaga = Kee[int](72)
    LoveKiss = Kee[int](73)
    CleanMirror = Kee[int](75)
    PremiumDark = Kee[int](76)
    ColdEvening = Kee[int](77)
    CochitiLake = Kee[int](78)
    SummerGames = Kee[int](79)
    PassionateBed = Kee[int](80)
    MountainRock = Kee[int](81)
    DesertHump = Kee[int](82)
    JungleDay = Kee[int](83)
    PhoenixStart = Kee[int](84)
    OctoberSilence = Kee[int](85)
    FarawayRiver = Kee[int](86)
    AlchemistLab = Kee[int](87)
    OverSun = Kee[int](88)
    PremiumWhite = Kee[int](89)
    MarsParty = Kee[int](90)
    EternalConstance = Kee[int](91)
    JapanBlush = Kee[int](92)
    SmilingRain = Kee[int](93)
    CloudyApple = Kee[int](94)
    BigMango = Kee[int](95)
    HealthyWater = Kee[int](96)
    AmourAmour = Kee[int](97)
    RiskyConcrete = Kee[int](98)
    StrongStick = Kee[int](99)
    ViciousStance = Kee[int](100)
    PaloAlto = Kee[int](101)
    HappyMemories = Kee[int](102)
    MidnightBloom = Kee[int](103)
    Crystalline = Kee[int](104)
    PartyBliss = Kee[int](106)
    ConfidentCloud = Kee[int](107)
    LeCocktail = Kee[int](108)
    RiverCity = Kee[int](109)
    FrozenBerry = Kee[int](110)
    ChildCare = Kee[int](112)
    FlyingLemon = Kee[int](113)
    NewRetrowave = Kee[int](114)
    HiddenJaguar = Kee[int](115)
    AboveTheSky = Kee[int](116)
    Nega = Kee[int](117)
    DenseWater = Kee[int](118)
    Seashore = Kee[int](120)
    MarbleWall = Kee[int](121)
    CheerfulCaramel = Kee[int](122)
    NightSky = Kee[int](123)
    MagicLake = Kee[int](124)
    YoungGrass = Kee[int](125)
    ColorfulPeach = Kee[int](126)
    GentleCare = Kee[int](127)
    PlumBath = Kee[int](128)
    HappyUnicorn = Kee[int](129)
    AfricanField = Kee[int](131)
    SolidStone = Kee[int](132)
    OrangeJuice = Kee[int](133)
    GlassWater = Kee[int](134)
    NorthMiracle = Kee[int](136)
    FruitBlend = Kee[int](137)
    MillenniumPine = Kee[int](138)
    HighFlight = Kee[int](139)
    MoleHall = Kee[int](140)
    SpaceShift = Kee[int](142)
    ForestInei = Kee[int](143)
    RoyalGarden = Kee[int](144)
    RichMetal = Kee[int](145)
    JuicyCake = Kee[int](146)
    SmartIndigo = Kee[int](147)
    SandStrike = Kee[int](148)
    NorseBeauty = Kee[int](149)
    AquaGuidance = Kee[int](150)
    SunVeggie = Kee[int](151)
    SeaLord = Kee[int](152)
    BlackSea = Kee[int](153)
    GrassShampoo = Kee[int](154)
    LandingAircraft = Kee[int](155)
    WitchDance = Kee[int](156)
    SleeplessNight = Kee[int](157)
    AngelCare = Kee[int](158)
    CrystalRiver = Kee[int](159)
    SoftLipstick = Kee[int](160)
    SaltMountain = Kee[int](161)
    PerfectWhite = Kee[int](162)
    FreshOasis = Kee[int](163)
    StrictNovember = Kee[int](164)
    MorningSalad = Kee[int](165)
    DeepRelief = Kee[int](166)
    SeaStrike = Kee[int](167)
    NightCall = Kee[int](168)
    SupremeSky = Kee[int](169)
    LightBlue = Kee[int](170)
    MindCrawl = Kee[int](171)
    LilyMeadow = Kee[int](172)
    SugarLollipop = Kee[int](173)
    SweetDessert = Kee[int](174)
    MagicRay = Kee[int](175)
    TeenParty = Kee[int](176)
    FrozenHeat = Kee[int](177)
    GagarinView = Kee[int](178)
    FabledSunset = Kee[int](179)
    PerfectBlue = Kee[int](180)
    NumPresets = Kee[int](181)

  class Spread(CuteNum):
    """
    The enum 'QGradient::Spread' of Qt, with the 3 names Qt gives in it.
    """

    PadSpread = Kee[int](0)
    ReflectSpread = Kee[int](1)
    RepeatSpread = Kee[int](2)

  class Type(CuteNum):
    """The enum 'QGradient::Type' of Qt, with the 4 names Qt gives in it."""

    LinearGradient = Kee[int](0)
    RadialGradient = Kee[int](1)
    ConicalGradient = Kee[int](2)
    NoGradient = Kee[int](3)

  #  The classes Qt writes inside QGradient, each a class in here as in C++.

  class QGradientData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QGradient::QGradientData: a plain Python object
    standing in front of one C++ QGradient::QGradientData.

    C++ hands a QGradient::QGradientData around as a copy, so every C++
    QGradient::QGradientData behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QGradient::QGradientData yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QGradient::QGradientData::~QGradientData()': the destructor:
      Python removes its C++ QGradient::QGradientData by it, and has no other
      use for it.

    What to expect
    --------------

    - The C++ QGradient::QGradientData is created at the first use, not by
      'QGradient::QGradientData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QGradient::QGradientData back gives a copy the
      ritual made for Python, in a new cute QGradient::QGradientData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QGradient::QGradientData'

    #  Qt's '~QGradient::QGradientData()'. Naming it makes this a value
    #  class: Python owns every C++ QGradient::QGradientData behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN9QGradient13QGradientDataD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGradient'

  #  Qt's '~QGradient()'. Naming it makes this a value class: Python owns
  #  every C++ QGradient behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QGradientD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> Type:
    """
    Calls Qt's 'Type QGradient::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgradient.html#type

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type QGradient::type() const
    return QGradient.Type(self.uglySide.call('ritual_ZNK9QGradient4typeEv'))

  def spread(self) -> Spread:
    """
    Calls Qt's 'Spread QGradient::spread() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgradient.html#spread

    Returns
    -------

    Spread
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Spread(number)' gives.
    """
    #  Spread QGradient::spread() const
    return QGradient.Spread(self.uglySide.call(
        'ritual_ZNK9QGradient6spreadEv',
    ))

  def coordinateMode(self) -> CoordinateMode:
    """
    Calls Qt's 'CoordinateMode QGradient::coordinateMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgradient.html#coordinateMode

    Returns
    -------

    CoordinateMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'CoordinateMode(number)'
      gives.
    """
    #  CoordinateMode QGradient::coordinateMode() const
    return QGradient.CoordinateMode(self.uglySide.call(
        'ritual_ZNK9QGradient14coordinateModeEv',
    ))

  def interpolationMode(self) -> InterpolationMode:
    """
    Calls Qt's 'InterpolationMode QGradient::interpolationMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgradient.html#interpolationMode

    Returns
    -------

    InterpolationMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'InterpolationMode(number)' gives.
    """
    #  InterpolationMode QGradient::interpolationMode() const
    return QGradient.InterpolationMode(self.uglySide.call(
        'ritual_ZNK9QGradient17interpolationModeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Spread)
  def setSpread(self, spread: Spread) -> None:
    """
    Calls Qt's 'void QGradient::setSpread(Spread spread)'.

    Qt's own words: https://doc.qt.io/qt-6/qgradient.html#setSpread

    Parameters
    ----------

    spread : Spread
      Passed on as its number.
    """
    #  void QGradient::setSpread(Spread spread)
    self.uglySide.call(
        'ritual_ZN9QGradient9setSpreadENS_6SpreadE', spread.value,
    )

  @overload(float, QColor)
  def setColorAt(self, pos: float, color: QColor) -> None:
    """
    Calls Qt's 'void QGradient::setColorAt(qreal pos, const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qgradient.html#setColorAt

    Parameters
    ----------

    pos : float
      Passed on as it is.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QGradient::setColorAt(qreal pos, const QColor &color)
    self.uglySide.call(
        'ritual_ZN9QGradient10setColorAtEdRK6QColor',
        pos, self._valueOf(color),
    )

  @overload(CoordinateMode)
  def setCoordinateMode(self, mode: CoordinateMode) -> None:
    """
    Calls Qt's 'void QGradient::setCoordinateMode(CoordinateMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qgradient.html#setCoordinateMode

    Parameters
    ----------

    mode : CoordinateMode
      Passed on as its number.
    """
    #  void QGradient::setCoordinateMode(CoordinateMode mode)
    self.uglySide.call(
        'ritual_ZN9QGradient17setCoordinateModeENS_14CoordinateModeE',
        mode.value,
    )

  @overload(InterpolationMode)
  def setInterpolationMode(self, mode: InterpolationMode) -> None:
    """
    Calls Qt's 'void QGradient::setInterpolationMode(InterpolationMode
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgradient.html#setInterpolationMode

    Parameters
    ----------

    mode : InterpolationMode
      Passed on as its number.
    """
    #  void QGradient::setInterpolationMode(InterpolationMode mode)
    self.uglySide.call(
        'ritual_ZN9QGradient20setInterpolationModeENS_17InterpolationModeE',
        mode.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, gradient: QGradient) -> bool:
    """
    Calls Qt's 'bool QGradient::operator==(const QGradient &gradient) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgradient.html#operator==

    Parameters
    ----------

    gradient : QGradient
      Passed on as a value: Qt reads the C++ QGradient, which stays Python's
      own.
    """
    #  bool QGradient::operator==(const QGradient &gradient) const
    return self.uglySide.call(
        'ritual_ZNK9QGradienteqERKS_', self._valueOf(gradient),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, other: QGradient) -> bool:
    """
    Calls Qt's 'bool QGradient::operator!=(const QGradient &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgradient.html#operator!=

    Parameters
    ----------

    other : QGradient
      Passed on as a value: Qt reads the C++ QGradient, which stays Python's
      own.
    """
    #  bool QGradient::operator!=(const QGradient &other) const
    return self.uglySide.call(
        'ritual_ZNK9QGradientneERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QGradient::QGradient()', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgradient.html#QGradient
    """
    #  QGradient::QGradient()
    self._noteCreation(QGradient, lambda: Rituals.call(
        'ritual_ZN9QGradientC1Ev',
    ))

  @overload(Preset)
  def __init__(self, a0: Preset) -> None:
    """
    Notes what was given, for Qt's 'QGradient::QGradient(Preset a0)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgradient.html#QGradient

    Parameters
    ----------

    a0 : Preset
      Passed on as its number.
    """
    #  QGradient::QGradient(Preset a0)
    self._noteCreation(QGradient, lambda: Rituals.call(
        'ritual_ZN9QGradientC1ENS_6PresetE', a0.value,
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
