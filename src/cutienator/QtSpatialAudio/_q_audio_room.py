"""
QAudioRoom binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSpatialAudio/qaudioroom.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QQuaternion, QVector3D
  from . import QAudioEngine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAudioEngine = WAIT['QAudioEngine']
  QQuaternion = WAIT['QQuaternion']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAudioRoom(QObject):
  """
  The cute side of Qt's QAudioRoom: a plain Python object standing in front
  of one C++ QAudioRoom.

  It is built on the cute 'QObject', as Qt's QAudioRoom is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAudioRoom that has a ritual and that Python can
  call so far, 26 names in all: 'metaObject', 'tr', 'setPosition',
  'position', 'setDimensions', 'dimensions', 'setRotation', 'rotation',
  'setWallMaterial', 'wallMaterial', 'setReflectionGain', 'reflectionGain',
  'setReverbGain', 'reverbGain', 'setReverbTime', 'reverbTime',
  'setReverbBrightness', 'reverbBrightness', 'positionChanged',
  'dimensionsChanged', 'rotationChanged', 'wallsChanged',
  'reflectionGainChanged', 'reverbGainChanged', 'reverbTimeChanged',
  'reverbBrightnessChanged'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAudioRoom::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QAudioRoom::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QAudioRoom::~QAudioRoom()': the destructor: Python never removes a
    C++ QAudioRoom.
  - Qt's 'QAudioRoomPrivate *QAudioRoom::d_func()': gives
    'QAudioRoomPrivate', which has no cute class yet.
  - Qt's 'const QAudioRoomPrivate *QAudioRoom::d_func() const': gives
    'QAudioRoomPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 34 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QAudioRoom is created at the first use, not by 'QAudioRoom(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAudioRoom.
  - Qt tells when it has removed the C++ QAudioRoom. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QAudioRoom, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Material(CuteNum):
    """
    The enum 'QAudioRoom::Material' of Qt, with the 24 names Qt gives in it.
    """

    Transparent = Kee[int](0)
    AcousticCeilingTiles = Kee[int](1)
    BrickBare = Kee[int](2)
    BrickPainted = Kee[int](3)
    ConcreteBlockCoarse = Kee[int](4)
    ConcreteBlockPainted = Kee[int](5)
    CurtainHeavy = Kee[int](6)
    FiberGlassInsulation = Kee[int](7)
    GlassThin = Kee[int](8)
    GlassThick = Kee[int](9)
    Grass = Kee[int](10)
    LinoleumOnConcrete = Kee[int](11)
    Marble = Kee[int](12)
    Metal = Kee[int](13)
    ParquetOnConcrete = Kee[int](14)
    PlasterRough = Kee[int](15)
    PlasterSmooth = Kee[int](16)
    PlywoodPanel = Kee[int](17)
    PolishedConcreteOrTile = Kee[int](18)
    Sheetrock = Kee[int](19)
    WaterOrIceSurface = Kee[int](20)
    WoodCeiling = Kee[int](21)
    WoodPanel = Kee[int](22)
    UniformMaterial = Kee[int](23)

  class Wall(CuteNum):
    """The enum 'QAudioRoom::Wall' of Qt, with the 6 names Qt gives in it."""

    LeftWall = Kee[int](0)
    RightWall = Kee[int](1)
    Floor = Kee[int](2)
    Ceiling = Kee[int](3)
    FrontWall = Kee[int](4)
    BackWall = Kee[int](5)

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
    Calls Qt's 'QString QAudioRoom::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioroom.html#tr

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
    #  QString QAudioRoom::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QAudioRoom2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAudioRoom'

  #  A C++ QAudioRoom Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAudioRoom'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAudioRoom::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioroom.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAudioRoom::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QAudioRoom10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def position(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QAudioRoom::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioroom.html#position

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QAudioRoom::position() const
    address = self.uglySide.call('ritual_ZNK10QAudioRoom8positionEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def dimensions(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QAudioRoom::dimensions() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioroom.html#dimensions

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QAudioRoom::dimensions() const
    address = self.uglySide.call('ritual_ZNK10QAudioRoom10dimensionsEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def rotation(self) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion QAudioRoom::rotation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioroom.html#rotation

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion QAudioRoom::rotation() const
    address = self.uglySide.call('ritual_ZNK10QAudioRoom8rotationEv')
    from ..QtGui import QQuaternion
    return QQuaternion._cuteOwning(address)

  @overload(Wall)
  def wallMaterial(self, wall: Wall) -> Material:
    """
    Calls Qt's 'Material QAudioRoom::wallMaterial(Wall wall) const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioroom.html#wallMaterial

    Parameters
    ----------

    wall : Wall
      Passed on as its number.

    Returns
    -------

    Material
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Material(number)' gives.
    """
    #  Material QAudioRoom::wallMaterial(Wall wall) const
    return QAudioRoom.Material(self.uglySide.call(
        'ritual_ZNK10QAudioRoom12wallMaterialENS_4WallE', wall.value,
    ))

  def reflectionGain(self) -> float:
    """
    Calls Qt's 'float QAudioRoom::reflectionGain() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioroom.html#reflectionGain
    """
    #  float QAudioRoom::reflectionGain() const
    return self.uglySide.call('ritual_ZNK10QAudioRoom14reflectionGainEv')

  def reverbGain(self) -> float:
    """
    Calls Qt's 'float QAudioRoom::reverbGain() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioroom.html#reverbGain
    """
    #  float QAudioRoom::reverbGain() const
    return self.uglySide.call('ritual_ZNK10QAudioRoom10reverbGainEv')

  def reverbTime(self) -> float:
    """
    Calls Qt's 'float QAudioRoom::reverbTime() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioroom.html#reverbTime
    """
    #  float QAudioRoom::reverbTime() const
    return self.uglySide.call('ritual_ZNK10QAudioRoom10reverbTimeEv')

  def reverbBrightness(self) -> float:
    """
    Calls Qt's 'float QAudioRoom::reverbBrightness() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioroom.html#reverbBrightness
    """
    #  float QAudioRoom::reverbBrightness() const
    return self.uglySide.call('ritual_ZNK10QAudioRoom16reverbBrightnessEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVector3D)
  def setPosition(self, pos: QVector3D) -> None:
    """
    Calls Qt's 'void QAudioRoom::setPosition(QVector3D pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioroom.html#setPosition

    Parameters
    ----------

    pos : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QAudioRoom::setPosition(QVector3D pos)
    self.uglySide.call(
        'ritual_ZN10QAudioRoom11setPositionE9QVector3D', self._valueOf(pos),
    )

  @overload(QVector3D)
  def setDimensions(self, dim: QVector3D) -> None:
    """
    Calls Qt's 'void QAudioRoom::setDimensions(QVector3D dim)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioroom.html#setDimensions

    Parameters
    ----------

    dim : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QAudioRoom::setDimensions(QVector3D dim)
    self.uglySide.call(
        'ritual_ZN10QAudioRoom13setDimensionsE9QVector3D',
        self._valueOf(dim),
    )

  @overload(QQuaternion)
  def setRotation(self, q: QQuaternion) -> None:
    """
    Calls Qt's 'void QAudioRoom::setRotation(const QQuaternion &q)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioroom.html#setRotation

    Parameters
    ----------

    q : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.
    """
    #  void QAudioRoom::setRotation(const QQuaternion &q)
    self.uglySide.call(
        'ritual_ZN10QAudioRoom11setRotationERK11QQuaternion',
        self._valueOf(q),
    )

  @overload(Wall, Material)
  def setWallMaterial(self, wall: Wall, material: Material) -> None:
    """
    Calls Qt's 'void QAudioRoom::setWallMaterial(Wall wall, Material
    material)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioroom.html#setWallMaterial

    Parameters
    ----------

    wall : Wall
      Passed on as its number.

    material : Material
      Passed on as its number.
    """
    #  void QAudioRoom::setWallMaterial(Wall wall, Material material)
    self.uglySide.call(
        'ritual_ZN10QAudioRoom15setWallMaterialENS_4WallENS_8MaterialE',
        wall.value, material.value,
    )

  @overload(float)
  def setReflectionGain(self, factor: float) -> None:
    """
    Calls Qt's 'void QAudioRoom::setReflectionGain(float factor)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioroom.html#setReflectionGain

    Parameters
    ----------

    factor : float
      Passed on as it is.
    """
    #  void QAudioRoom::setReflectionGain(float factor)
    self.uglySide.call('ritual_ZN10QAudioRoom17setReflectionGainEf', factor)

  @overload(float)
  def setReverbGain(self, factor: float) -> None:
    """
    Calls Qt's 'void QAudioRoom::setReverbGain(float factor)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioroom.html#setReverbGain

    Parameters
    ----------

    factor : float
      Passed on as it is.
    """
    #  void QAudioRoom::setReverbGain(float factor)
    self.uglySide.call('ritual_ZN10QAudioRoom13setReverbGainEf', factor)

  @overload(float)
  def setReverbTime(self, factor: float) -> None:
    """
    Calls Qt's 'void QAudioRoom::setReverbTime(float factor)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioroom.html#setReverbTime

    Parameters
    ----------

    factor : float
      Passed on as it is.
    """
    #  void QAudioRoom::setReverbTime(float factor)
    self.uglySide.call('ritual_ZN10QAudioRoom13setReverbTimeEf', factor)

  @overload(float)
  def setReverbBrightness(self, factor: float) -> None:
    """
    Calls Qt's 'void QAudioRoom::setReverbBrightness(float factor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudioroom.html#setReverbBrightness

    Parameters
    ----------

    factor : float
      Passed on as it is.
    """
    #  void QAudioRoom::setReverbBrightness(float factor)
    self.uglySide.call(
        'ritual_ZN10QAudioRoom19setReverbBrightnessEf', factor,
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

  @overload(QAudioEngine)
  @overload(NoneType)
  def __init__(self, engine: Optional[QAudioEngine]) -> None:
    """
    Notes what was given, for Qt's 'QAudioRoom::QAudioRoom(QAudioEngine
    *engine)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qaudioroom.html#QAudioRoom

    Parameters
    ----------

    engine : Optional[QAudioEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QAudioRoom::QAudioRoom(QAudioEngine *engine)
    self._noteCreation(QAudioRoom, lambda: Rituals.call(
        'ritual_ZN10QAudioRoomC1EP12QAudioEngine', self._addressOf(engine),
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

  def positionChanged(self) -> None:
    """
    Calls Qt's 'void QAudioRoom::positionChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioroom.html#positionChanged
    """
    #  void QAudioRoom::positionChanged()
    self.uglySide.call('ritual_ZN10QAudioRoom15positionChangedEv')

  def dimensionsChanged(self) -> None:
    """
    Calls Qt's 'void QAudioRoom::dimensionsChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioroom.html#dimensionsChanged
    """
    #  void QAudioRoom::dimensionsChanged()
    self.uglySide.call('ritual_ZN10QAudioRoom17dimensionsChangedEv')

  def rotationChanged(self) -> None:
    """
    Calls Qt's 'void QAudioRoom::rotationChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioroom.html#rotationChanged
    """
    #  void QAudioRoom::rotationChanged()
    self.uglySide.call('ritual_ZN10QAudioRoom15rotationChangedEv')

  def wallsChanged(self) -> None:
    """
    Calls Qt's 'void QAudioRoom::wallsChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioroom.html#wallsChanged
    """
    #  void QAudioRoom::wallsChanged()
    self.uglySide.call('ritual_ZN10QAudioRoom12wallsChangedEv')

  def reflectionGainChanged(self) -> None:
    """
    Calls Qt's 'void QAudioRoom::reflectionGainChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudioroom.html#reflectionGainChanged
    """
    #  void QAudioRoom::reflectionGainChanged()
    self.uglySide.call('ritual_ZN10QAudioRoom21reflectionGainChangedEv')

  def reverbGainChanged(self) -> None:
    """
    Calls Qt's 'void QAudioRoom::reverbGainChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioroom.html#reverbGainChanged
    """
    #  void QAudioRoom::reverbGainChanged()
    self.uglySide.call('ritual_ZN10QAudioRoom17reverbGainChangedEv')

  def reverbTimeChanged(self) -> None:
    """
    Calls Qt's 'void QAudioRoom::reverbTimeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioroom.html#reverbTimeChanged
    """
    #  void QAudioRoom::reverbTimeChanged()
    self.uglySide.call('ritual_ZN10QAudioRoom17reverbTimeChangedEv')

  def reverbBrightnessChanged(self) -> None:
    """
    Calls Qt's 'void QAudioRoom::reverbBrightnessChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudioroom.html#reverbBrightnessChanged
    """
    #  void QAudioRoom::reverbBrightnessChanged()
    self.uglySide.call('ritual_ZN10QAudioRoom23reverbBrightnessChangedEv')
