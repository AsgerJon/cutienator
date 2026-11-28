"""
QQuick3DAudioRoom binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DSpatialAudio/6.12.0/QtQuick3DSpatialAudio/private/qquick3daudioroom_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DAudioRoom to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVector3D = WAIT['QVector3D']


class QQuick3DAudioRoom(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuick3DAudioRoom: a plain Python object standing in
  front of one C++ QQuick3DAudioRoom.

  What exists
  -----------

  Every function of Qt's QQuick3DAudioRoom that has a ritual and that Python
  can call so far, 33 names in all: 'metaObject', 'setDimensions',
  'dimensions', 'setLeftMaterial', 'leftMaterial', 'setRightMaterial',
  'rightMaterial', 'setFrontMaterial', 'frontMaterial', 'setBackMaterial',
  'backMaterial', 'setFloorMaterial', 'floorMaterial', 'setCeilingMaterial',
  'ceilingMaterial', 'setReflectionGain', 'reflectionGain', 'setReverbGain',
  'reverbGain', 'setReverbTime', 'reverbTime', 'setReverbBrightness',
  'reverbBrightness', 'positionChanged', 'dimensionsChanged',
  'rotationChanged', 'wallsChanged', 'reflectionGainChanged',
  'reverbGainChanged', 'reverbTimeChanged', 'reverbBrightnessChanged',
  'updatePosition', 'updateRotation'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DAudioRoom::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuick3DAudioRoom::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DAudioRoom::~QQuick3DAudioRoom()': the destructor: Python
    never removes a C++ QQuick3DAudioRoom.

  What has no ritual
  ------------------

  4 of the 40 functions Qt declares: 2 not a gap; 2 leans on
  'QQuick3DAudioRoom.

  What to expect
  --------------

  - The C++ QQuick3DAudioRoom is created at the first use, not by
    'QQuick3DAudioRoom(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DAudioRoom.
  - Qt tells when it has removed the C++ QQuick3DAudioRoom. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DAudioRoom that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QQuick3DAudioRoom, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Material(CuteNum):
    """
    The enum 'QQuick3DAudioRoom::Material' of Qt, with the 24 names Qt gives
    in it.
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
    Uniform = Kee[int](23)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DAudioRoom'

  #  A C++ QQuick3DAudioRoom Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DAudioRoom'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DAudioRoom::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3daudioroom.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DAudioRoom::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuick3DAudioRoom10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def dimensions(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DAudioRoom::dimensions() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3daudioroom.html#dimensions

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DAudioRoom::dimensions() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuick3DAudioRoom10dimensionsEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def leftMaterial(self) -> Material:
    """
    Calls Qt's 'Material QQuick3DAudioRoom::leftMaterial() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3daudioroom.html#leftMaterial

    Returns
    -------

    Material
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Material(number)' gives.
    """
    #  Material QQuick3DAudioRoom::leftMaterial() const
    return QQuick3DAudioRoom.Material(self.uglySide.call(
        'ritual_ZNK17QQuick3DAudioRoom12leftMaterialEv',
    ))

  def rightMaterial(self) -> Material:
    """
    Calls Qt's 'Material QQuick3DAudioRoom::rightMaterial() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3daudioroom.html#rightMaterial

    Returns
    -------

    Material
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Material(number)' gives.
    """
    #  Material QQuick3DAudioRoom::rightMaterial() const
    return QQuick3DAudioRoom.Material(self.uglySide.call(
        'ritual_ZNK17QQuick3DAudioRoom13rightMaterialEv',
    ))

  def frontMaterial(self) -> Material:
    """
    Calls Qt's 'Material QQuick3DAudioRoom::frontMaterial() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3daudioroom.html#frontMaterial

    Returns
    -------

    Material
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Material(number)' gives.
    """
    #  Material QQuick3DAudioRoom::frontMaterial() const
    return QQuick3DAudioRoom.Material(self.uglySide.call(
        'ritual_ZNK17QQuick3DAudioRoom13frontMaterialEv',
    ))

  def backMaterial(self) -> Material:
    """
    Calls Qt's 'Material QQuick3DAudioRoom::backMaterial() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3daudioroom.html#backMaterial

    Returns
    -------

    Material
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Material(number)' gives.
    """
    #  Material QQuick3DAudioRoom::backMaterial() const
    return QQuick3DAudioRoom.Material(self.uglySide.call(
        'ritual_ZNK17QQuick3DAudioRoom12backMaterialEv',
    ))

  def floorMaterial(self) -> Material:
    """
    Calls Qt's 'Material QQuick3DAudioRoom::floorMaterial() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3daudioroom.html#floorMaterial

    Returns
    -------

    Material
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Material(number)' gives.
    """
    #  Material QQuick3DAudioRoom::floorMaterial() const
    return QQuick3DAudioRoom.Material(self.uglySide.call(
        'ritual_ZNK17QQuick3DAudioRoom13floorMaterialEv',
    ))

  def ceilingMaterial(self) -> Material:
    """
    Calls Qt's 'Material QQuick3DAudioRoom::ceilingMaterial() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3daudioroom.html#ceilingMaterial

    Returns
    -------

    Material
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Material(number)' gives.
    """
    #  Material QQuick3DAudioRoom::ceilingMaterial() const
    return QQuick3DAudioRoom.Material(self.uglySide.call(
        'ritual_ZNK17QQuick3DAudioRoom15ceilingMaterialEv',
    ))

  def reflectionGain(self) -> float:
    """
    Calls Qt's 'float QQuick3DAudioRoom::reflectionGain() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3daudioroom.html#reflectionGain
    """
    #  float QQuick3DAudioRoom::reflectionGain() const
    return self.uglySide.call(
        'ritual_ZNK17QQuick3DAudioRoom14reflectionGainEv',
    )

  def reverbGain(self) -> float:
    """
    Calls Qt's 'float QQuick3DAudioRoom::reverbGain() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3daudioroom.html#reverbGain
    """
    #  float QQuick3DAudioRoom::reverbGain() const
    return self.uglySide.call('ritual_ZNK17QQuick3DAudioRoom10reverbGainEv')

  def reverbTime(self) -> float:
    """
    Calls Qt's 'float QQuick3DAudioRoom::reverbTime() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3daudioroom.html#reverbTime
    """
    #  float QQuick3DAudioRoom::reverbTime() const
    return self.uglySide.call('ritual_ZNK17QQuick3DAudioRoom10reverbTimeEv')

  def reverbBrightness(self) -> float:
    """
    Calls Qt's 'float QQuick3DAudioRoom::reverbBrightness() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3daudioroom.html#reverbBrightness
    """
    #  float QQuick3DAudioRoom::reverbBrightness() const
    return self.uglySide.call(
        'ritual_ZNK17QQuick3DAudioRoom16reverbBrightnessEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVector3D)
  def setDimensions(self, pos: QVector3D) -> None:
    """
    Calls Qt's 'void QQuick3DAudioRoom::setDimensions(QVector3D pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3daudioroom.html#setDimensions

    Parameters
    ----------

    pos : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuick3DAudioRoom::setDimensions(QVector3D pos)
    self.uglySide.call(
        'ritual_ZN17QQuick3DAudioRoom13setDimensionsE9QVector3D',
        self._valueOf(pos),
    )

  @overload(Material)
  def setLeftMaterial(self, material: Material) -> None:
    """
    Calls Qt's 'void QQuick3DAudioRoom::setLeftMaterial(Material material)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3daudioroom.html#setLeftMaterial

    Parameters
    ----------

    material : Material
      Passed on as its number.
    """
    #  void QQuick3DAudioRoom::setLeftMaterial(Material material)
    self.uglySide.call(
        'ritual_ZN17QQuick3DAudioRoom15setLeftMaterialENS_8MaterialE',
        material.value,
    )

  @overload(Material)
  def setRightMaterial(self, material: Material) -> None:
    """
    Calls Qt's 'void QQuick3DAudioRoom::setRightMaterial(Material material)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3daudioroom.html#setRightMaterial

    Parameters
    ----------

    material : Material
      Passed on as its number.
    """
    #  void QQuick3DAudioRoom::setRightMaterial(Material material)
    self.uglySide.call(
        'ritual_ZN17QQuick3DAudioRoom16setRightMaterialENS_8MaterialE',
        material.value,
    )

  @overload(Material)
  def setFrontMaterial(self, material: Material) -> None:
    """
    Calls Qt's 'void QQuick3DAudioRoom::setFrontMaterial(Material material)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3daudioroom.html#setFrontMaterial

    Parameters
    ----------

    material : Material
      Passed on as its number.
    """
    #  void QQuick3DAudioRoom::setFrontMaterial(Material material)
    self.uglySide.call(
        'ritual_ZN17QQuick3DAudioRoom16setFrontMaterialENS_8MaterialE',
        material.value,
    )

  @overload(Material)
  def setBackMaterial(self, material: Material) -> None:
    """
    Calls Qt's 'void QQuick3DAudioRoom::setBackMaterial(Material material)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3daudioroom.html#setBackMaterial

    Parameters
    ----------

    material : Material
      Passed on as its number.
    """
    #  void QQuick3DAudioRoom::setBackMaterial(Material material)
    self.uglySide.call(
        'ritual_ZN17QQuick3DAudioRoom15setBackMaterialENS_8MaterialE',
        material.value,
    )

  @overload(Material)
  def setFloorMaterial(self, material: Material) -> None:
    """
    Calls Qt's 'void QQuick3DAudioRoom::setFloorMaterial(Material material)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3daudioroom.html#setFloorMaterial

    Parameters
    ----------

    material : Material
      Passed on as its number.
    """
    #  void QQuick3DAudioRoom::setFloorMaterial(Material material)
    self.uglySide.call(
        'ritual_ZN17QQuick3DAudioRoom16setFloorMaterialENS_8MaterialE',
        material.value,
    )

  @overload(Material)
  def setCeilingMaterial(self, material: Material) -> None:
    """
    Calls Qt's 'void QQuick3DAudioRoom::setCeilingMaterial(Material
    material)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3daudioroom.html#setCeilingMaterial

    Parameters
    ----------

    material : Material
      Passed on as its number.
    """
    #  void QQuick3DAudioRoom::setCeilingMaterial(Material material)
    self.uglySide.call(
        'ritual_ZN17QQuick3DAudioRoom18setCeilingMaterialENS_8MaterialE',
        material.value,
    )

  @overload(float)
  def setReflectionGain(self, factor: float) -> None:
    """
    Calls Qt's 'void QQuick3DAudioRoom::setReflectionGain(float factor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3daudioroom.html#setReflectionGain

    Parameters
    ----------

    factor : float
      Passed on as it is.
    """
    #  void QQuick3DAudioRoom::setReflectionGain(float factor)
    self.uglySide.call(
        'ritual_ZN17QQuick3DAudioRoom17setReflectionGainEf', factor,
    )

  @overload(float)
  def setReverbGain(self, factor: float) -> None:
    """
    Calls Qt's 'void QQuick3DAudioRoom::setReverbGain(float factor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3daudioroom.html#setReverbGain

    Parameters
    ----------

    factor : float
      Passed on as it is.
    """
    #  void QQuick3DAudioRoom::setReverbGain(float factor)
    self.uglySide.call(
        'ritual_ZN17QQuick3DAudioRoom13setReverbGainEf', factor,
    )

  @overload(float)
  def setReverbTime(self, factor: float) -> None:
    """
    Calls Qt's 'void QQuick3DAudioRoom::setReverbTime(float factor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3daudioroom.html#setReverbTime

    Parameters
    ----------

    factor : float
      Passed on as it is.
    """
    #  void QQuick3DAudioRoom::setReverbTime(float factor)
    self.uglySide.call(
        'ritual_ZN17QQuick3DAudioRoom13setReverbTimeEf', factor,
    )

  @overload(float)
  def setReverbBrightness(self, factor: float) -> None:
    """
    Calls Qt's 'void QQuick3DAudioRoom::setReverbBrightness(float factor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3daudioroom.html#setReverbBrightness

    Parameters
    ----------

    factor : float
      Passed on as it is.
    """
    #  void QQuick3DAudioRoom::setReverbBrightness(float factor)
    self.uglySide.call(
        'ritual_ZN17QQuick3DAudioRoom19setReverbBrightnessEf', factor,
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
    Qt's 'QQuick3DAudioRoom::QQuick3DAudioRoom()': leans on
    'QQuick3DAudioRoom::qt_metacall(QMetaObject::Call, int, void**)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DAudioRoom.__init__' has no cute function yet. Qt's "
        "'QQuick3DAudioRoom::QQuick3DAudioRoom()': leans on "
        "'QQuick3DAudioRoom::qt_metacall(QMetaObject::Call, int, void**)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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
    Calls Qt's 'void QQuick3DAudioRoom::positionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3daudioroom.html#positionChanged
    """
    #  void QQuick3DAudioRoom::positionChanged()
    self.uglySide.call('ritual_ZN17QQuick3DAudioRoom15positionChangedEv')

  def dimensionsChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DAudioRoom::dimensionsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3daudioroom.html#dimensionsChanged
    """
    #  void QQuick3DAudioRoom::dimensionsChanged()
    self.uglySide.call('ritual_ZN17QQuick3DAudioRoom17dimensionsChangedEv')

  def rotationChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DAudioRoom::rotationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3daudioroom.html#rotationChanged
    """
    #  void QQuick3DAudioRoom::rotationChanged()
    self.uglySide.call('ritual_ZN17QQuick3DAudioRoom15rotationChangedEv')

  def wallsChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DAudioRoom::wallsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3daudioroom.html#wallsChanged
    """
    #  void QQuick3DAudioRoom::wallsChanged()
    self.uglySide.call('ritual_ZN17QQuick3DAudioRoom12wallsChangedEv')

  def reflectionGainChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DAudioRoom::reflectionGainChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3daudioroom.html#reflectionGainChanged
    """
    #  void QQuick3DAudioRoom::reflectionGainChanged()
    self.uglySide.call(
        'ritual_ZN17QQuick3DAudioRoom21reflectionGainChangedEv',
    )

  def reverbGainChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DAudioRoom::reverbGainChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3daudioroom.html#reverbGainChanged
    """
    #  void QQuick3DAudioRoom::reverbGainChanged()
    self.uglySide.call('ritual_ZN17QQuick3DAudioRoom17reverbGainChangedEv')

  def reverbTimeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DAudioRoom::reverbTimeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3daudioroom.html#reverbTimeChanged
    """
    #  void QQuick3DAudioRoom::reverbTimeChanged()
    self.uglySide.call('ritual_ZN17QQuick3DAudioRoom17reverbTimeChangedEv')

  def reverbBrightnessChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DAudioRoom::reverbBrightnessChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3daudioroom.html#reverbBrightnessChanged
    """
    #  void QQuick3DAudioRoom::reverbBrightnessChanged()
    self.uglySide.call(
        'ritual_ZN17QQuick3DAudioRoom23reverbBrightnessChangedEv',
    )

  def updatePosition(self) -> None:
    """
    Calls Qt's 'void QQuick3DAudioRoom::updatePosition()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3daudioroom.html#updatePosition
    """
    #  void QQuick3DAudioRoom::updatePosition()
    self.uglySide.call('ritual_ZN17QQuick3DAudioRoom14updatePositionEv')

  def updateRotation(self) -> None:
    """
    Calls Qt's 'void QQuick3DAudioRoom::updateRotation()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3daudioroom.html#updateRotation
    """
    #  void QQuick3DAudioRoom::updateRotation()
    self.uglySide.call('ritual_ZN17QQuick3DAudioRoom14updateRotationEv')
