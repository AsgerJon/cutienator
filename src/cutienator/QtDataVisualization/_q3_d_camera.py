"""
Q3DCamera binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/q3dcamera.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import Q3DObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Q3DCamera(Q3DObject):
  """
  The cute side of Qt's Q3DCamera: a plain Python object standing in front of
  one C++ Q3DCamera.

  It is built on the cute 'Q3DObject', as Qt's Q3DCamera is built on Qt's
  Q3DObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Q3DCamera that has a ritual and that Python can call
  so far, 30 names in all: 'metaObject', 'tr', 'xRotation', 'setXRotation',
  'yRotation', 'setYRotation', 'wrapXRotation', 'setWrapXRotation',
  'wrapYRotation', 'setWrapYRotation', 'cameraPreset', 'setCameraPreset',
  'zoomLevel', 'setZoomLevel', 'minZoomLevel', 'setMinZoomLevel',
  'maxZoomLevel', 'setMaxZoomLevel', 'setCameraPosition', 'target',
  'setTarget', 'xRotationChanged', 'yRotationChanged', 'zoomLevelChanged',
  'cameraPresetChanged', 'wrapXRotationChanged', 'wrapYRotationChanged',
  'targetChanged', 'minZoomLevelChanged', 'maxZoomLevelChanged'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Q3DCamera::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int Q3DCamera::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'Q3DCamera::~Q3DCamera()': the destructor: Python never removes a
    C++ Q3DCamera.
  - Qt's 'void Q3DCamera::copyValuesFrom(const Q3DObject &source)': takes a
    type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 39 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ Q3DCamera is created at the first use, not by 'Q3DCamera(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Q3DCamera.
  - Qt tells when it has removed the C++ Q3DCamera. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside Q3DCamera, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class CameraPreset(CuteNum):
    """
    The enum 'Q3DCamera::CameraPreset' of Qt, with the 25 names Qt gives in
    it.
    """

    CameraPresetNone = Kee[int](-1)
    CameraPresetFrontLow = Kee[int](0)
    CameraPresetFront = Kee[int](1)
    CameraPresetFrontHigh = Kee[int](2)
    CameraPresetLeftLow = Kee[int](3)
    CameraPresetLeft = Kee[int](4)
    CameraPresetLeftHigh = Kee[int](5)
    CameraPresetRightLow = Kee[int](6)
    CameraPresetRight = Kee[int](7)
    CameraPresetRightHigh = Kee[int](8)
    CameraPresetBehindLow = Kee[int](9)
    CameraPresetBehind = Kee[int](10)
    CameraPresetBehindHigh = Kee[int](11)
    CameraPresetIsometricLeft = Kee[int](12)
    CameraPresetIsometricLeftHigh = Kee[int](13)
    CameraPresetIsometricRight = Kee[int](14)
    CameraPresetIsometricRightHigh = Kee[int](15)
    CameraPresetDirectlyAbove = Kee[int](16)
    CameraPresetDirectlyAboveCW45 = Kee[int](17)
    CameraPresetDirectlyAboveCCW45 = Kee[int](18)
    CameraPresetFrontBelow = Kee[int](19)
    CameraPresetLeftBelow = Kee[int](20)
    CameraPresetRightBelow = Kee[int](21)
    CameraPresetBehindBelow = Kee[int](22)
    CameraPresetDirectlyBelow = Kee[int](23)

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
    Calls Qt's 'QString Q3DCamera::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dcamera.html#tr

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
    #  QString Q3DCamera::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN9Q3DCamera2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Q3DCamera'

  #  A C++ Q3DCamera Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Q3DCamera'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Q3DCamera::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dcamera.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Q3DCamera::metaObject() const
    address = self.uglySide.call('ritual_ZNK9Q3DCamera10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def xRotation(self) -> float:
    """
    Calls Qt's 'float Q3DCamera::xRotation() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dcamera.html#xRotation
    """
    #  float Q3DCamera::xRotation() const
    return self.uglySide.call('ritual_ZNK9Q3DCamera9xRotationEv')

  def yRotation(self) -> float:
    """
    Calls Qt's 'float Q3DCamera::yRotation() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dcamera.html#yRotation
    """
    #  float Q3DCamera::yRotation() const
    return self.uglySide.call('ritual_ZNK9Q3DCamera9yRotationEv')

  def wrapXRotation(self) -> bool:
    """
    Calls Qt's 'bool Q3DCamera::wrapXRotation() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dcamera.html#wrapXRotation
    """
    #  bool Q3DCamera::wrapXRotation() const
    return self.uglySide.call('ritual_ZNK9Q3DCamera13wrapXRotationEv')

  def wrapYRotation(self) -> bool:
    """
    Calls Qt's 'bool Q3DCamera::wrapYRotation() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dcamera.html#wrapYRotation
    """
    #  bool Q3DCamera::wrapYRotation() const
    return self.uglySide.call('ritual_ZNK9Q3DCamera13wrapYRotationEv')

  def cameraPreset(self) -> CameraPreset:
    """
    Calls Qt's 'CameraPreset Q3DCamera::cameraPreset() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dcamera.html#cameraPreset

    Returns
    -------

    CameraPreset
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'CameraPreset(number)'
      gives.
    """
    #  CameraPreset Q3DCamera::cameraPreset() const
    return Q3DCamera.CameraPreset(self.uglySide.call(
        'ritual_ZNK9Q3DCamera12cameraPresetEv',
    ))

  def zoomLevel(self) -> float:
    """
    Calls Qt's 'float Q3DCamera::zoomLevel() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dcamera.html#zoomLevel
    """
    #  float Q3DCamera::zoomLevel() const
    return self.uglySide.call('ritual_ZNK9Q3DCamera9zoomLevelEv')

  def minZoomLevel(self) -> float:
    """
    Calls Qt's 'float Q3DCamera::minZoomLevel() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dcamera.html#minZoomLevel
    """
    #  float Q3DCamera::minZoomLevel() const
    return self.uglySide.call('ritual_ZNK9Q3DCamera12minZoomLevelEv')

  def maxZoomLevel(self) -> float:
    """
    Calls Qt's 'float Q3DCamera::maxZoomLevel() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dcamera.html#maxZoomLevel
    """
    #  float Q3DCamera::maxZoomLevel() const
    return self.uglySide.call('ritual_ZNK9Q3DCamera12maxZoomLevelEv')

  def target(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D Q3DCamera::target() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dcamera.html#target

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Q3DCamera::target() const
    address = self.uglySide.call('ritual_ZNK9Q3DCamera6targetEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setXRotation(self, rotation: float) -> None:
    """
    Calls Qt's 'void Q3DCamera::setXRotation(float rotation)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dcamera.html#setXRotation

    Parameters
    ----------

    rotation : float
      Passed on as it is.
    """
    #  void Q3DCamera::setXRotation(float rotation)
    self.uglySide.call('ritual_ZN9Q3DCamera12setXRotationEf', rotation)

  @overload(float)
  def setYRotation(self, rotation: float) -> None:
    """
    Calls Qt's 'void Q3DCamera::setYRotation(float rotation)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dcamera.html#setYRotation

    Parameters
    ----------

    rotation : float
      Passed on as it is.
    """
    #  void Q3DCamera::setYRotation(float rotation)
    self.uglySide.call('ritual_ZN9Q3DCamera12setYRotationEf', rotation)

  @overload(bool)
  def setWrapXRotation(self, isEnabled: bool) -> None:
    """
    Calls Qt's 'void Q3DCamera::setWrapXRotation(bool isEnabled)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dcamera.html#setWrapXRotation

    Parameters
    ----------

    isEnabled : bool
      Passed on as it is.
    """
    #  void Q3DCamera::setWrapXRotation(bool isEnabled)
    self.uglySide.call('ritual_ZN9Q3DCamera16setWrapXRotationEb', isEnabled)

  @overload(bool)
  def setWrapYRotation(self, isEnabled: bool) -> None:
    """
    Calls Qt's 'void Q3DCamera::setWrapYRotation(bool isEnabled)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dcamera.html#setWrapYRotation

    Parameters
    ----------

    isEnabled : bool
      Passed on as it is.
    """
    #  void Q3DCamera::setWrapYRotation(bool isEnabled)
    self.uglySide.call('ritual_ZN9Q3DCamera16setWrapYRotationEb', isEnabled)

  @overload(CameraPreset)
  def setCameraPreset(self, preset: CameraPreset) -> None:
    """
    Calls Qt's 'void Q3DCamera::setCameraPreset(CameraPreset preset)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dcamera.html#setCameraPreset

    Parameters
    ----------

    preset : CameraPreset
      Passed on as its number.
    """
    #  void Q3DCamera::setCameraPreset(CameraPreset preset)
    self.uglySide.call(
        'ritual_ZN9Q3DCamera15setCameraPresetENS_12CameraPresetE',
        preset.value,
    )

  @overload(float)
  def setZoomLevel(self, zoomLevel: float) -> None:
    """
    Calls Qt's 'void Q3DCamera::setZoomLevel(float zoomLevel)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dcamera.html#setZoomLevel

    Parameters
    ----------

    zoomLevel : float
      Passed on as it is.
    """
    #  void Q3DCamera::setZoomLevel(float zoomLevel)
    self.uglySide.call('ritual_ZN9Q3DCamera12setZoomLevelEf', zoomLevel)

  @overload(float)
  def setMinZoomLevel(self, zoomLevel: float) -> None:
    """
    Calls Qt's 'void Q3DCamera::setMinZoomLevel(float zoomLevel)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dcamera.html#setMinZoomLevel

    Parameters
    ----------

    zoomLevel : float
      Passed on as it is.
    """
    #  void Q3DCamera::setMinZoomLevel(float zoomLevel)
    self.uglySide.call('ritual_ZN9Q3DCamera15setMinZoomLevelEf', zoomLevel)

  @overload(float)
  def setMaxZoomLevel(self, zoomLevel: float) -> None:
    """
    Calls Qt's 'void Q3DCamera::setMaxZoomLevel(float zoomLevel)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dcamera.html#setMaxZoomLevel

    Parameters
    ----------

    zoomLevel : float
      Passed on as it is.
    """
    #  void Q3DCamera::setMaxZoomLevel(float zoomLevel)
    self.uglySide.call('ritual_ZN9Q3DCamera15setMaxZoomLevelEf', zoomLevel)

  @overload(float, float)
  @overload(float, float, float)
  def setCameraPosition(
      self,
      horizontal: float,
      vertical: float,
      zoom: float = 100.0,
  ) -> None:
    """
    Calls Qt's 'void Q3DCamera::setCameraPosition(float horizontal, float
    vertical, float zoom)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dcamera.html#setCameraPosition

    Parameters
    ----------

    horizontal : float
      Passed on as it is.

    vertical : float
      Passed on as it is.

    zoom : float
      Passed on as it is. May be left out, as in Qt: it is then 100.0.
    """
    #  void Q3DCamera::setCameraPosition(float horizontal, float vertical,
    #      float zoom)
    self.uglySide.call(
        'ritual_ZN9Q3DCamera17setCameraPositionEfff',
        horizontal, vertical, zoom,
    )

  @overload(QVector3D)
  def setTarget(self, target: QVector3D) -> None:
    """
    Calls Qt's 'void Q3DCamera::setTarget(const QVector3D &target)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dcamera.html#setTarget

    Parameters
    ----------

    target : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Q3DCamera::setTarget(const QVector3D &target)
    self.uglySide.call(
        'ritual_ZN9Q3DCamera9setTargetERK9QVector3D', self._valueOf(target),
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'Q3DCamera::Q3DCamera(QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/q3dcamera.html#Q3DCamera

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Q3DCamera::Q3DCamera(QObject *parent)
    self._noteCreation(Q3DCamera, lambda: Rituals.call(
        'ritual_ZN9Q3DCameraC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  @overload(float)
  def xRotationChanged(self, rotation: float) -> None:
    """
    Calls Qt's 'void Q3DCamera::xRotationChanged(float rotation)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dcamera.html#xRotationChanged

    Parameters
    ----------

    rotation : float
      Passed on as it is.
    """
    #  void Q3DCamera::xRotationChanged(float rotation)
    self.uglySide.call('ritual_ZN9Q3DCamera16xRotationChangedEf', rotation)

  @overload(float)
  def yRotationChanged(self, rotation: float) -> None:
    """
    Calls Qt's 'void Q3DCamera::yRotationChanged(float rotation)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dcamera.html#yRotationChanged

    Parameters
    ----------

    rotation : float
      Passed on as it is.
    """
    #  void Q3DCamera::yRotationChanged(float rotation)
    self.uglySide.call('ritual_ZN9Q3DCamera16yRotationChangedEf', rotation)

  @overload(float)
  def zoomLevelChanged(self, zoomLevel: float) -> None:
    """
    Calls Qt's 'void Q3DCamera::zoomLevelChanged(float zoomLevel)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dcamera.html#zoomLevelChanged

    Parameters
    ----------

    zoomLevel : float
      Passed on as it is.
    """
    #  void Q3DCamera::zoomLevelChanged(float zoomLevel)
    self.uglySide.call('ritual_ZN9Q3DCamera16zoomLevelChangedEf', zoomLevel)

  @overload(CameraPreset)
  def cameraPresetChanged(self, preset: CameraPreset) -> None:
    """
    Calls Qt's 'void Q3DCamera::cameraPresetChanged(Q3DCamera::CameraPreset
    preset)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dcamera.html#cameraPresetChanged

    Parameters
    ----------

    preset : CameraPreset
      Passed on as its number.
    """
    #  void Q3DCamera::cameraPresetChanged(Q3DCamera::CameraPreset preset)
    self.uglySide.call(
        'ritual_ZN9Q3DCamera19cameraPresetChangedENS_12CameraPresetE',
        preset.value,
    )

  @overload(bool)
  def wrapXRotationChanged(self, isEnabled: bool) -> None:
    """
    Calls Qt's 'void Q3DCamera::wrapXRotationChanged(bool isEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dcamera.html#wrapXRotationChanged

    Parameters
    ----------

    isEnabled : bool
      Passed on as it is.
    """
    #  void Q3DCamera::wrapXRotationChanged(bool isEnabled)
    self.uglySide.call(
        'ritual_ZN9Q3DCamera20wrapXRotationChangedEb', isEnabled,
    )

  @overload(bool)
  def wrapYRotationChanged(self, isEnabled: bool) -> None:
    """
    Calls Qt's 'void Q3DCamera::wrapYRotationChanged(bool isEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dcamera.html#wrapYRotationChanged

    Parameters
    ----------

    isEnabled : bool
      Passed on as it is.
    """
    #  void Q3DCamera::wrapYRotationChanged(bool isEnabled)
    self.uglySide.call(
        'ritual_ZN9Q3DCamera20wrapYRotationChangedEb', isEnabled,
    )

  @overload(QVector3D)
  def targetChanged(self, target: QVector3D) -> None:
    """
    Calls Qt's 'void Q3DCamera::targetChanged(const QVector3D &target)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dcamera.html#targetChanged

    Parameters
    ----------

    target : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Q3DCamera::targetChanged(const QVector3D &target)
    self.uglySide.call(
        'ritual_ZN9Q3DCamera13targetChangedERK9QVector3D',
        self._valueOf(target),
    )

  @overload(float)
  def minZoomLevelChanged(self, zoomLevel: float) -> None:
    """
    Calls Qt's 'void Q3DCamera::minZoomLevelChanged(float zoomLevel)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dcamera.html#minZoomLevelChanged

    Parameters
    ----------

    zoomLevel : float
      Passed on as it is.
    """
    #  void Q3DCamera::minZoomLevelChanged(float zoomLevel)
    self.uglySide.call(
        'ritual_ZN9Q3DCamera19minZoomLevelChangedEf', zoomLevel,
    )

  @overload(float)
  def maxZoomLevelChanged(self, zoomLevel: float) -> None:
    """
    Calls Qt's 'void Q3DCamera::maxZoomLevelChanged(float zoomLevel)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dcamera.html#maxZoomLevelChanged

    Parameters
    ----------

    zoomLevel : float
      Passed on as it is.
    """
    #  void Q3DCamera::maxZoomLevelChanged(float zoomLevel)
    self.uglySide.call(
        'ritual_ZN9Q3DCamera19maxZoomLevelChangedEf', zoomLevel,
    )
