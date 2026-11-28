"""
QCamera binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/qcamera.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QCameraDevice

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPointF
  from . import QCameraFormat, QCameraPrivate, QMediaCaptureSession
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCameraFormat = WAIT['QCameraFormat']
  QMediaCaptureSession = WAIT['QMediaCaptureSession']
  QPointF = WAIT['QPointF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCamera(QObject):
  """
  The cute side of Qt's QCamera: a plain Python object standing in front of
  one C++ QCamera.

  It is built on the cute 'QObject', as Qt's QCamera is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCamera that has a ritual and that Python can call
  so far, 87 names in all: 'metaObject', 'tr', 'isAvailable', 'isActive',
  'captureSession', 'cameraDevice', 'setCameraDevice', 'cameraFormat',
  'setCameraFormat', 'error', 'errorString', 'supportedFeatures',
  'focusMode', 'setFocusMode', 'isFocusModeSupported', 'focusPoint',
  'customFocusPoint', 'setCustomFocusPoint', 'setFocusDistance',
  'focusDistance', 'minimumZoomFactor', 'maximumZoomFactor', 'zoomFactor',
  'setZoomFactor', 'flashMode', 'isFlashModeSupported', 'isFlashReady',
  'torchMode', 'isTorchModeSupported', 'exposureMode',
  'isExposureModeSupported', 'exposureCompensation', 'isoSensitivity',
  'manualIsoSensitivity', 'exposureTime', 'manualExposureTime',
  'minimumIsoSensitivity', 'maximumIsoSensitivity', 'minimumExposureTime',
  'maximumExposureTime', 'whiteBalanceMode', 'isWhiteBalanceModeSupported',
  'colorTemperature', 'setActive', 'start', 'stop', 'zoomTo', 'setFlashMode',
  'setTorchMode', 'setExposureMode', 'setExposureCompensation',
  'setManualIsoSensitivity', 'setAutoIsoSensitivity',
  'setManualExposureTime', 'setAutoExposureTime', 'setWhiteBalanceMode',
  'setColorTemperature', 'activeChanged', 'errorChanged', 'errorOccurred',
  'cameraDeviceChanged', 'cameraFormatChanged', 'supportedFeaturesChanged',
  'focusModeChanged', 'zoomFactorChanged', 'minimumZoomFactorChanged',
  'maximumZoomFactorChanged', 'focusDistanceChanged', 'focusPointChanged',
  'customFocusPointChanged', 'flashReady', 'flashModeChanged',
  'torchModeChanged', 'exposureTimeChanged', 'manualExposureTimeChanged',
  'isoSensitivityChanged', 'manualIsoSensitivityChanged',
  'exposureCompensationChanged', 'exposureModeChanged',
  'whiteBalanceModeChanged', 'colorTemperatureChanged', 'brightnessChanged',
  'contrastChanged', 'saturationChanged', 'hueChanged', 'setCaptureSession',
  'd_func'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QCamera::qt_metacast(const char *a0)': one of Qt's own inner
    workings.
  - Qt's 'int QCamera::qt_metacall(QMetaObject::Call a0, int a1, void **a2)':
    one of Qt's own inner workings.
  - Qt's 'QCamera::~QCamera()': the destructor: Python never removes a C++
    QCamera.
  - Qt's 'class QPlatformCamera *QCamera::platformCamera()': gives 'class
    QPlatformCamera', which has no cute class yet.
  - Qt's 'const QCameraPrivate *QCamera::d_func() const': takes in Python
    what 'QCameraPrivate *QCamera::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 99 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QCamera is created at the first use, not by 'QCamera(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCamera.
  - Qt tells when it has removed the C++ QCamera. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QCamera that has no cute function yet,
    'platformCamera', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QCamera, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class Error(CuteNum):
    """The enum 'QCamera::Error' of Qt, with the 2 names Qt gives in it."""

    NoError = Kee[int](0)
    CameraError = Kee[int](1)

  class ExposureMode(CuteNum):
    """
    The enum 'QCamera::ExposureMode' of Qt, with the 17 names Qt gives in it.
    """

    ExposureAuto = Kee[int](0)
    ExposureManual = Kee[int](1)
    ExposurePortrait = Kee[int](2)
    ExposureNight = Kee[int](3)
    ExposureSports = Kee[int](4)
    ExposureSnow = Kee[int](5)
    ExposureBeach = Kee[int](6)
    ExposureAction = Kee[int](7)
    ExposureLandscape = Kee[int](8)
    ExposureNightPortrait = Kee[int](9)
    ExposureTheatre = Kee[int](10)
    ExposureSunset = Kee[int](11)
    ExposureSteadyPhoto = Kee[int](12)
    ExposureFireworks = Kee[int](13)
    ExposureParty = Kee[int](14)
    ExposureCandlelight = Kee[int](15)
    ExposureBarcode = Kee[int](16)

  class Feature(CuteFlags, scoped=True):
    """
    The flags enum 'QCamera::Feature' of Qt, with the 6 names Qt gives in it.
    Qt names the type of its combinations 'QCamera::Features'. C++ keeps
    these names inside the enum, so the class that holds the enum does not
    have them.
    """

    ColorTemperature = 0x1
    ExposureCompensation = 0x2
    IsoSensitivity = 0x4
    ManualExposureTime = 0x8
    CustomFocusPoint = 0x10
    FocusDistance = 0x20

  Features = Feature

  class FlashMode(CuteNum):
    """
    The enum 'QCamera::FlashMode' of Qt, with the 3 names Qt gives in it.
    """

    FlashOff = Kee[int](0)
    FlashOn = Kee[int](1)
    FlashAuto = Kee[int](2)

  class FocusMode(CuteNum):
    """
    The enum 'QCamera::FocusMode' of Qt, with the 6 names Qt gives in it.
    """

    FocusModeAuto = Kee[int](0)
    FocusModeAutoNear = Kee[int](1)
    FocusModeAutoFar = Kee[int](2)
    FocusModeHyperfocal = Kee[int](3)
    FocusModeInfinity = Kee[int](4)
    FocusModeManual = Kee[int](5)

  class TorchMode(CuteNum):
    """
    The enum 'QCamera::TorchMode' of Qt, with the 3 names Qt gives in it.
    """

    TorchOff = Kee[int](0)
    TorchOn = Kee[int](1)
    TorchAuto = Kee[int](2)

  class WhiteBalanceMode(CuteNum):
    """
    The enum 'QCamera::WhiteBalanceMode' of Qt, with the 9 names Qt gives in
    it.
    """

    WhiteBalanceAuto = Kee[int](0)
    WhiteBalanceManual = Kee[int](1)
    WhiteBalanceSunlight = Kee[int](2)
    WhiteBalanceCloudy = Kee[int](3)
    WhiteBalanceShade = Kee[int](4)
    WhiteBalanceTungsten = Kee[int](5)
    WhiteBalanceFluorescent = Kee[int](6)
    WhiteBalanceFlash = Kee[int](7)
    WhiteBalanceSunset = Kee[int](8)

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
    Calls Qt's 'QString QCamera::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#tr

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
    #  QString QCamera::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN7QCamera2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCamera'

  #  A C++ QCamera Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCamera'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QCamera::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QCamera::metaObject() const
    address = self.uglySide.call('ritual_ZNK7QCamera10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isAvailable(self) -> bool:
    """
    Calls Qt's 'bool QCamera::isAvailable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#isAvailable
    """
    #  bool QCamera::isAvailable() const
    return self.uglySide.call('ritual_ZNK7QCamera11isAvailableEv')

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool QCamera::isActive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#isActive
    """
    #  bool QCamera::isActive() const
    return self.uglySide.call('ritual_ZNK7QCamera8isActiveEv')

  def captureSession(self) -> Optional[QMediaCaptureSession]:
    """
    Calls Qt's 'QMediaCaptureSession *QCamera::captureSession() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#captureSession

    Returns
    -------

    Optional[QMediaCaptureSession]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMediaCaptureSession *QCamera::captureSession() const
    address = self.uglySide.call('ritual_ZNK7QCamera14captureSessionEv')
    from . import QMediaCaptureSession
    return QMediaCaptureSession._cuteAt(address)

  def cameraDevice(self) -> QCameraDevice:
    """
    Calls Qt's 'QCameraDevice QCamera::cameraDevice() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#cameraDevice

    Returns
    -------

    QCameraDevice
      A new cute QCameraDevice around the copy Qt gave back. Python owns it.
    """
    #  QCameraDevice QCamera::cameraDevice() const
    address = self.uglySide.call('ritual_ZNK7QCamera12cameraDeviceEv')
    return QCameraDevice._cuteOwning(address)

  def cameraFormat(self) -> QCameraFormat:
    """
    Calls Qt's 'QCameraFormat QCamera::cameraFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#cameraFormat

    Returns
    -------

    QCameraFormat
      A new cute QCameraFormat around the copy Qt gave back. Python owns it.
    """
    #  QCameraFormat QCamera::cameraFormat() const
    address = self.uglySide.call('ritual_ZNK7QCamera12cameraFormatEv')
    from . import QCameraFormat
    return QCameraFormat._cuteOwning(address)

  def error(self) -> Error:
    """
    Calls Qt's 'Error QCamera::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#error

    Returns
    -------

    Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Error(number)' gives.
    """
    #  Error QCamera::error() const
    return QCamera.Error(self.uglySide.call('ritual_ZNK7QCamera5errorEv'))

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QCamera::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCamera::errorString() const
    return self.uglySide.call('ritual_ZNK7QCamera11errorStringEv')

  def supportedFeatures(self) -> Features:
    """
    Calls Qt's 'Features QCamera::supportedFeatures() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#supportedFeatures

    Returns
    -------

    Features
      The value standing for the combination Qt gave back.
    """
    #  Features QCamera::supportedFeatures() const
    return QCamera.Features(self.uglySide.call(
        'ritual_ZNK7QCamera17supportedFeaturesEv',
    ))

  def focusMode(self) -> FocusMode:
    """
    Calls Qt's 'FocusMode QCamera::focusMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#focusMode

    Returns
    -------

    FocusMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'FocusMode(number)' gives.
    """
    #  FocusMode QCamera::focusMode() const
    return QCamera.FocusMode(self.uglySide.call(
        'ritual_ZNK7QCamera9focusModeEv',
    ))

  @overload(FocusMode)
  def isFocusModeSupported(self, mode: FocusMode) -> bool:
    """
    Calls Qt's 'bool QCamera::isFocusModeSupported(FocusMode mode) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#isFocusModeSupported

    Parameters
    ----------

    mode : FocusMode
      Passed on as its number.
    """
    #  bool QCamera::isFocusModeSupported(FocusMode mode) const
    return self.uglySide.call(
        'ritual_ZNK7QCamera20isFocusModeSupportedENS_9FocusModeE',
        mode.value,
    )

  def focusPoint(self) -> QPointF:
    """
    Calls Qt's 'QPointF QCamera::focusPoint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#focusPoint

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QCamera::focusPoint() const
    address = self.uglySide.call('ritual_ZNK7QCamera10focusPointEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def customFocusPoint(self) -> QPointF:
    """
    Calls Qt's 'QPointF QCamera::customFocusPoint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#customFocusPoint

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QCamera::customFocusPoint() const
    address = self.uglySide.call('ritual_ZNK7QCamera16customFocusPointEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def focusDistance(self) -> float:
    """
    Calls Qt's 'float QCamera::focusDistance() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#focusDistance
    """
    #  float QCamera::focusDistance() const
    return self.uglySide.call('ritual_ZNK7QCamera13focusDistanceEv')

  def minimumZoomFactor(self) -> float:
    """
    Calls Qt's 'float QCamera::minimumZoomFactor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#minimumZoomFactor
    """
    #  float QCamera::minimumZoomFactor() const
    return self.uglySide.call('ritual_ZNK7QCamera17minimumZoomFactorEv')

  def maximumZoomFactor(self) -> float:
    """
    Calls Qt's 'float QCamera::maximumZoomFactor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#maximumZoomFactor
    """
    #  float QCamera::maximumZoomFactor() const
    return self.uglySide.call('ritual_ZNK7QCamera17maximumZoomFactorEv')

  def zoomFactor(self) -> float:
    """
    Calls Qt's 'float QCamera::zoomFactor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#zoomFactor
    """
    #  float QCamera::zoomFactor() const
    return self.uglySide.call('ritual_ZNK7QCamera10zoomFactorEv')

  def flashMode(self) -> FlashMode:
    """
    Calls Qt's 'FlashMode QCamera::flashMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#flashMode

    Returns
    -------

    FlashMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'FlashMode(number)' gives.
    """
    #  FlashMode QCamera::flashMode() const
    return QCamera.FlashMode(self.uglySide.call(
        'ritual_ZNK7QCamera9flashModeEv',
    ))

  @overload(FlashMode)
  def isFlashModeSupported(self, mode: FlashMode) -> bool:
    """
    Calls Qt's 'bool QCamera::isFlashModeSupported(FlashMode mode) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#isFlashModeSupported

    Parameters
    ----------

    mode : FlashMode
      Passed on as its number.
    """
    #  bool QCamera::isFlashModeSupported(FlashMode mode) const
    return self.uglySide.call(
        'ritual_ZNK7QCamera20isFlashModeSupportedENS_9FlashModeE',
        mode.value,
    )

  def isFlashReady(self) -> bool:
    """
    Calls Qt's 'bool QCamera::isFlashReady() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#isFlashReady
    """
    #  bool QCamera::isFlashReady() const
    return self.uglySide.call('ritual_ZNK7QCamera12isFlashReadyEv')

  def torchMode(self) -> TorchMode:
    """
    Calls Qt's 'TorchMode QCamera::torchMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#torchMode

    Returns
    -------

    TorchMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TorchMode(number)' gives.
    """
    #  TorchMode QCamera::torchMode() const
    return QCamera.TorchMode(self.uglySide.call(
        'ritual_ZNK7QCamera9torchModeEv',
    ))

  @overload(TorchMode)
  def isTorchModeSupported(self, mode: TorchMode) -> bool:
    """
    Calls Qt's 'bool QCamera::isTorchModeSupported(TorchMode mode) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#isTorchModeSupported

    Parameters
    ----------

    mode : TorchMode
      Passed on as its number.
    """
    #  bool QCamera::isTorchModeSupported(TorchMode mode) const
    return self.uglySide.call(
        'ritual_ZNK7QCamera20isTorchModeSupportedENS_9TorchModeE',
        mode.value,
    )

  def exposureMode(self) -> ExposureMode:
    """
    Calls Qt's 'ExposureMode QCamera::exposureMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#exposureMode

    Returns
    -------

    ExposureMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ExposureMode(number)'
      gives.
    """
    #  ExposureMode QCamera::exposureMode() const
    return QCamera.ExposureMode(self.uglySide.call(
        'ritual_ZNK7QCamera12exposureModeEv',
    ))

  @overload(ExposureMode)
  def isExposureModeSupported(self, mode: ExposureMode) -> bool:
    """
    Calls Qt's 'bool QCamera::isExposureModeSupported(ExposureMode mode)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcamera.html#isExposureModeSupported

    Parameters
    ----------

    mode : ExposureMode
      Passed on as its number.
    """
    #  bool QCamera::isExposureModeSupported(ExposureMode mode) const
    return self.uglySide.call(
        'ritual_ZNK7QCamera23isExposureModeSupportedENS_12ExposureModeE',
        mode.value,
    )

  def exposureCompensation(self) -> float:
    """
    Calls Qt's 'float QCamera::exposureCompensation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#exposureCompensation
    """
    #  float QCamera::exposureCompensation() const
    return self.uglySide.call('ritual_ZNK7QCamera20exposureCompensationEv')

  def isoSensitivity(self) -> int:
    """
    Calls Qt's 'int QCamera::isoSensitivity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#isoSensitivity
    """
    #  int QCamera::isoSensitivity() const
    return self.uglySide.call('ritual_ZNK7QCamera14isoSensitivityEv')

  def manualIsoSensitivity(self) -> int:
    """
    Calls Qt's 'int QCamera::manualIsoSensitivity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#manualIsoSensitivity
    """
    #  int QCamera::manualIsoSensitivity() const
    return self.uglySide.call('ritual_ZNK7QCamera20manualIsoSensitivityEv')

  def exposureTime(self) -> float:
    """
    Calls Qt's 'float QCamera::exposureTime() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#exposureTime
    """
    #  float QCamera::exposureTime() const
    return self.uglySide.call('ritual_ZNK7QCamera12exposureTimeEv')

  def manualExposureTime(self) -> float:
    """
    Calls Qt's 'float QCamera::manualExposureTime() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#manualExposureTime
    """
    #  float QCamera::manualExposureTime() const
    return self.uglySide.call('ritual_ZNK7QCamera18manualExposureTimeEv')

  def minimumIsoSensitivity(self) -> int:
    """
    Calls Qt's 'int QCamera::minimumIsoSensitivity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#minimumIsoSensitivity
    """
    #  int QCamera::minimumIsoSensitivity() const
    return self.uglySide.call('ritual_ZNK7QCamera21minimumIsoSensitivityEv')

  def maximumIsoSensitivity(self) -> int:
    """
    Calls Qt's 'int QCamera::maximumIsoSensitivity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#maximumIsoSensitivity
    """
    #  int QCamera::maximumIsoSensitivity() const
    return self.uglySide.call('ritual_ZNK7QCamera21maximumIsoSensitivityEv')

  def minimumExposureTime(self) -> float:
    """
    Calls Qt's 'float QCamera::minimumExposureTime() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#minimumExposureTime
    """
    #  float QCamera::minimumExposureTime() const
    return self.uglySide.call('ritual_ZNK7QCamera19minimumExposureTimeEv')

  def maximumExposureTime(self) -> float:
    """
    Calls Qt's 'float QCamera::maximumExposureTime() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#maximumExposureTime
    """
    #  float QCamera::maximumExposureTime() const
    return self.uglySide.call('ritual_ZNK7QCamera19maximumExposureTimeEv')

  def whiteBalanceMode(self) -> WhiteBalanceMode:
    """
    Calls Qt's 'WhiteBalanceMode QCamera::whiteBalanceMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#whiteBalanceMode

    Returns
    -------

    WhiteBalanceMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'WhiteBalanceMode(number)'
      gives.
    """
    #  WhiteBalanceMode QCamera::whiteBalanceMode() const
    return QCamera.WhiteBalanceMode(self.uglySide.call(
        'ritual_ZNK7QCamera16whiteBalanceModeEv',
    ))

  @overload(WhiteBalanceMode)
  def isWhiteBalanceModeSupported(self, mode: WhiteBalanceMode) -> bool:
    """
    Calls Qt's 'bool QCamera::isWhiteBalanceModeSupported(WhiteBalanceMode
    mode) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcamera.html#isWhiteBalanceModeSupported

    Parameters
    ----------

    mode : WhiteBalanceMode
      Passed on as its number.
    """
    #  bool QCamera::isWhiteBalanceModeSupported(WhiteBalanceMode mode) const
    return self.uglySide.call(
        'ritual_ZNK7QCamera27isWhiteBalanceModeSupportedENS_16WhiteBalanceM'
        'odeE',
        mode.value,
    )

  def colorTemperature(self) -> int:
    """
    Calls Qt's 'int QCamera::colorTemperature() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#colorTemperature
    """
    #  int QCamera::colorTemperature() const
    return self.uglySide.call('ritual_ZNK7QCamera16colorTemperatureEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QCameraDevice)
  def setCameraDevice(self, cameraDevice: QCameraDevice) -> None:
    """
    Calls Qt's 'void QCamera::setCameraDevice(const QCameraDevice
    &cameraDevice)'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#setCameraDevice

    Parameters
    ----------

    cameraDevice : QCameraDevice
      Passed on as a value: Qt reads the C++ QCameraDevice, which stays
      Python's own.
    """
    #  void QCamera::setCameraDevice(const QCameraDevice &cameraDevice)
    self.uglySide.call(
        'ritual_ZN7QCamera15setCameraDeviceERK13QCameraDevice',
        self._valueOf(cameraDevice),
    )

  @overload(QCameraFormat)
  def setCameraFormat(self, format: QCameraFormat) -> None:
    """
    Calls Qt's 'void QCamera::setCameraFormat(const QCameraFormat &format)'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#setCameraFormat

    Parameters
    ----------

    format : QCameraFormat
      Passed on as a value: Qt reads the C++ QCameraFormat, which stays
      Python's own.
    """
    #  void QCamera::setCameraFormat(const QCameraFormat &format)
    self.uglySide.call(
        'ritual_ZN7QCamera15setCameraFormatERK13QCameraFormat',
        self._valueOf(format),
    )

  @overload(FocusMode)
  def setFocusMode(self, mode: FocusMode) -> None:
    """
    Calls Qt's 'void QCamera::setFocusMode(FocusMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#setFocusMode

    Parameters
    ----------

    mode : FocusMode
      Passed on as its number.
    """
    #  void QCamera::setFocusMode(FocusMode mode)
    self.uglySide.call(
        'ritual_ZN7QCamera12setFocusModeENS_9FocusModeE', mode.value,
    )

  @overload(QPointF)
  def setCustomFocusPoint(self, point: QPointF) -> None:
    """
    Calls Qt's 'void QCamera::setCustomFocusPoint(const QPointF &point)'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#setCustomFocusPoint

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QCamera::setCustomFocusPoint(const QPointF &point)
    self.uglySide.call(
        'ritual_ZN7QCamera19setCustomFocusPointERK7QPointF',
        self._valueOf(point, 'QPointF'),
    )

  @overload(float)
  def setFocusDistance(self, d: float) -> None:
    """
    Calls Qt's 'void QCamera::setFocusDistance(float d)'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#setFocusDistance

    Parameters
    ----------

    d : float
      Passed on as it is.
    """
    #  void QCamera::setFocusDistance(float d)
    self.uglySide.call('ritual_ZN7QCamera16setFocusDistanceEf', d)

  @overload(float)
  def setZoomFactor(self, factor: float) -> None:
    """
    Calls Qt's 'void QCamera::setZoomFactor(float factor)'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#setZoomFactor

    Parameters
    ----------

    factor : float
      Passed on as it is.
    """
    #  void QCamera::setZoomFactor(float factor)
    self.uglySide.call('ritual_ZN7QCamera13setZoomFactorEf', factor)

  @overload(bool)
  def setActive(self, active: bool) -> None:
    """
    Calls Qt's 'void QCamera::setActive(bool active)'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#setActive

    Parameters
    ----------

    active : bool
      Passed on as it is.
    """
    #  void QCamera::setActive(bool active)
    self.uglySide.call('ritual_ZN7QCamera9setActiveEb', active)

  @overload(FlashMode)
  def setFlashMode(self, mode: FlashMode) -> None:
    """
    Calls Qt's 'void QCamera::setFlashMode(FlashMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#setFlashMode

    Parameters
    ----------

    mode : FlashMode
      Passed on as its number.
    """
    #  void QCamera::setFlashMode(FlashMode mode)
    self.uglySide.call(
        'ritual_ZN7QCamera12setFlashModeENS_9FlashModeE', mode.value,
    )

  @overload(TorchMode)
  def setTorchMode(self, mode: TorchMode) -> None:
    """
    Calls Qt's 'void QCamera::setTorchMode(TorchMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#setTorchMode

    Parameters
    ----------

    mode : TorchMode
      Passed on as its number.
    """
    #  void QCamera::setTorchMode(TorchMode mode)
    self.uglySide.call(
        'ritual_ZN7QCamera12setTorchModeENS_9TorchModeE', mode.value,
    )

  @overload(ExposureMode)
  def setExposureMode(self, mode: ExposureMode) -> None:
    """
    Calls Qt's 'void QCamera::setExposureMode(ExposureMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#setExposureMode

    Parameters
    ----------

    mode : ExposureMode
      Passed on as its number.
    """
    #  void QCamera::setExposureMode(ExposureMode mode)
    self.uglySide.call(
        'ritual_ZN7QCamera15setExposureModeENS_12ExposureModeE', mode.value,
    )

  @overload(float)
  def setExposureCompensation(self, ev: float) -> None:
    """
    Calls Qt's 'void QCamera::setExposureCompensation(float ev)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcamera.html#setExposureCompensation

    Parameters
    ----------

    ev : float
      Passed on as it is.
    """
    #  void QCamera::setExposureCompensation(float ev)
    self.uglySide.call('ritual_ZN7QCamera23setExposureCompensationEf', ev)

  @overload(int)
  def setManualIsoSensitivity(self, iso: int) -> None:
    """
    Calls Qt's 'void QCamera::setManualIsoSensitivity(int iso)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcamera.html#setManualIsoSensitivity

    Parameters
    ----------

    iso : int
      Passed on as it is.
    """
    #  void QCamera::setManualIsoSensitivity(int iso)
    self.uglySide.call('ritual_ZN7QCamera23setManualIsoSensitivityEi', iso)

  def setAutoIsoSensitivity(self) -> None:
    """
    Calls Qt's 'void QCamera::setAutoIsoSensitivity()'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#setAutoIsoSensitivity
    """
    #  void QCamera::setAutoIsoSensitivity()
    self.uglySide.call('ritual_ZN7QCamera21setAutoIsoSensitivityEv')

  @overload(float)
  def setManualExposureTime(self, seconds: float) -> None:
    """
    Calls Qt's 'void QCamera::setManualExposureTime(float seconds)'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#setManualExposureTime

    Parameters
    ----------

    seconds : float
      Passed on as it is.
    """
    #  void QCamera::setManualExposureTime(float seconds)
    self.uglySide.call('ritual_ZN7QCamera21setManualExposureTimeEf', seconds)

  def setAutoExposureTime(self) -> None:
    """
    Calls Qt's 'void QCamera::setAutoExposureTime()'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#setAutoExposureTime
    """
    #  void QCamera::setAutoExposureTime()
    self.uglySide.call('ritual_ZN7QCamera19setAutoExposureTimeEv')

  @overload(WhiteBalanceMode)
  def setWhiteBalanceMode(self, mode: WhiteBalanceMode) -> None:
    """
    Calls Qt's 'void QCamera::setWhiteBalanceMode(WhiteBalanceMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#setWhiteBalanceMode

    Parameters
    ----------

    mode : WhiteBalanceMode
      Passed on as its number.
    """
    #  void QCamera::setWhiteBalanceMode(WhiteBalanceMode mode)
    self.uglySide.call(
        'ritual_ZN7QCamera19setWhiteBalanceModeENS_16WhiteBalanceModeE',
        mode.value,
    )

  @overload(int)
  def setColorTemperature(self, colorTemperature: int) -> None:
    """
    Calls Qt's 'void QCamera::setColorTemperature(int colorTemperature)'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#setColorTemperature

    Parameters
    ----------

    colorTemperature : int
      Passed on as it is.
    """
    #  void QCamera::setColorTemperature(int colorTemperature)
    self.uglySide.call(
        'ritual_ZN7QCamera19setColorTemperatureEi', colorTemperature,
    )

  @overload(QMediaCaptureSession)
  @overload(NoneType)
  def setCaptureSession(
      self,
      session: Optional[QMediaCaptureSession],
  ) -> None:
    """
    Calls Qt's 'void QCamera::setCaptureSession(QMediaCaptureSession
    *session)'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#setCaptureSession

    Parameters
    ----------

    session : Optional[QMediaCaptureSession]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCamera::setCaptureSession(QMediaCaptureSession *session)
    self.uglySide.call(
        'ritual_ZN7QCamera17setCaptureSessionEP20QMediaCaptureSession',
        self._addressOf(session),
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
    Notes what was given, for Qt's 'QCamera::QCamera(QObject *parent)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#QCamera

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QCamera::QCamera(QObject *parent)
    self._noteCreation(QCamera, lambda: Rituals.call(
        'ritual_ZN7QCameraC1EP7QObject', self._addressOf(parent, 'QObject'),
    ))

  @overload(QCameraDevice)
  @overload(QCameraDevice, QObject)
  @overload(QCameraDevice, NoneType)
  def __init__(
      self,
      cameraDevice: QCameraDevice,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QCamera::QCamera(const QCameraDevice
    &cameraDevice, QObject *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#QCamera

    Parameters
    ----------

    cameraDevice : QCameraDevice
      Passed on as a value: Qt reads the C++ QCameraDevice, which stays
      Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QCamera::QCamera(const QCameraDevice &cameraDevice, QObject *parent)
    self._noteCreation(QCamera, lambda: Rituals.call(
        'ritual_ZN7QCameraC1ERK13QCameraDeviceP7QObject',
        self._valueOf(cameraDevice), self._addressOf(parent, 'QObject'),
    ))

  @overload(QCameraDevice.Position)
  @overload(QCameraDevice.Position, QObject)
  @overload(QCameraDevice.Position, NoneType)
  def __init__(
      self,
      position: QCameraDevice.Position,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QCamera::QCamera(QCameraDevice::Position
    position, QObject *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#QCamera

    Parameters
    ----------

    position : QCameraDevice.Position
      Passed on as its number.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QCamera::QCamera(QCameraDevice::Position position, QObject *parent)
    self._noteCreation(QCamera, lambda: Rituals.call(
        'ritual_ZN7QCameraC1EN13QCameraDevice8PositionEP7QObject',
        position.value, self._addressOf(parent, 'QObject'),
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

  def start(self) -> None:
    """
    Calls Qt's 'void QCamera::start()'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#start
    """
    #  void QCamera::start()
    self.uglySide.call('ritual_ZN7QCamera5startEv')

  def stop(self) -> None:
    """
    Calls Qt's 'void QCamera::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#stop
    """
    #  void QCamera::stop()
    self.uglySide.call('ritual_ZN7QCamera4stopEv')

  @overload(float, float)
  def zoomTo(self, zoom: float, rate: float) -> None:
    """
    Calls Qt's 'void QCamera::zoomTo(float zoom, float rate)'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#zoomTo

    Parameters
    ----------

    zoom : float
      Passed on as it is.

    rate : float
      Passed on as it is.
    """
    #  void QCamera::zoomTo(float zoom, float rate)
    self.uglySide.call('ritual_ZN7QCamera6zoomToEff', zoom, rate)

  @overload(bool)
  def activeChanged(self, a0: bool) -> None:
    """
    Calls Qt's 'void QCamera::activeChanged(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#activeChanged

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QCamera::activeChanged(bool a0)
    self.uglySide.call('ritual_ZN7QCamera13activeChangedEb', a0)

  def errorChanged(self) -> None:
    """
    Calls Qt's 'void QCamera::errorChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#errorChanged
    """
    #  void QCamera::errorChanged()
    self.uglySide.call('ritual_ZN7QCamera12errorChangedEv')

  @overload(Error, str)
  def errorOccurred(self, error: Error, errorString: str) -> None:
    """
    Calls Qt's 'void QCamera::errorOccurred(QCamera::Error error, const
    QString &errorString)'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#errorOccurred

    Parameters
    ----------

    error : Error
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QCamera::errorOccurred(QCamera::Error error, const QString
    #      &errorString)
    self.uglySide.call(
        'ritual_ZN7QCamera13errorOccurredENS_5ErrorERK7QString',
        error.value, errorString,
    )

  def cameraDeviceChanged(self) -> None:
    """
    Calls Qt's 'void QCamera::cameraDeviceChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#cameraDeviceChanged
    """
    #  void QCamera::cameraDeviceChanged()
    self.uglySide.call('ritual_ZN7QCamera19cameraDeviceChangedEv')

  def cameraFormatChanged(self) -> None:
    """
    Calls Qt's 'void QCamera::cameraFormatChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#cameraFormatChanged
    """
    #  void QCamera::cameraFormatChanged()
    self.uglySide.call('ritual_ZN7QCamera19cameraFormatChangedEv')

  def supportedFeaturesChanged(self) -> None:
    """
    Calls Qt's 'void QCamera::supportedFeaturesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcamera.html#supportedFeaturesChanged
    """
    #  void QCamera::supportedFeaturesChanged()
    self.uglySide.call('ritual_ZN7QCamera24supportedFeaturesChangedEv')

  def focusModeChanged(self) -> None:
    """
    Calls Qt's 'void QCamera::focusModeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#focusModeChanged
    """
    #  void QCamera::focusModeChanged()
    self.uglySide.call('ritual_ZN7QCamera16focusModeChangedEv')

  @overload(float)
  def zoomFactorChanged(self, a0: float) -> None:
    """
    Calls Qt's 'void QCamera::zoomFactorChanged(float a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#zoomFactorChanged

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QCamera::zoomFactorChanged(float a0)
    self.uglySide.call('ritual_ZN7QCamera17zoomFactorChangedEf', a0)

  @overload(float)
  def minimumZoomFactorChanged(self, a0: float) -> None:
    """
    Calls Qt's 'void QCamera::minimumZoomFactorChanged(float a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcamera.html#minimumZoomFactorChanged

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QCamera::minimumZoomFactorChanged(float a0)
    self.uglySide.call('ritual_ZN7QCamera24minimumZoomFactorChangedEf', a0)

  @overload(float)
  def maximumZoomFactorChanged(self, a0: float) -> None:
    """
    Calls Qt's 'void QCamera::maximumZoomFactorChanged(float a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcamera.html#maximumZoomFactorChanged

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QCamera::maximumZoomFactorChanged(float a0)
    self.uglySide.call('ritual_ZN7QCamera24maximumZoomFactorChangedEf', a0)

  @overload(float)
  def focusDistanceChanged(self, a0: float) -> None:
    """
    Calls Qt's 'void QCamera::focusDistanceChanged(float a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#focusDistanceChanged

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QCamera::focusDistanceChanged(float a0)
    self.uglySide.call('ritual_ZN7QCamera20focusDistanceChangedEf', a0)

  def focusPointChanged(self) -> None:
    """
    Calls Qt's 'void QCamera::focusPointChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#focusPointChanged
    """
    #  void QCamera::focusPointChanged()
    self.uglySide.call('ritual_ZN7QCamera17focusPointChangedEv')

  def customFocusPointChanged(self) -> None:
    """
    Calls Qt's 'void QCamera::customFocusPointChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcamera.html#customFocusPointChanged
    """
    #  void QCamera::customFocusPointChanged()
    self.uglySide.call('ritual_ZN7QCamera23customFocusPointChangedEv')

  @overload(bool)
  def flashReady(self, a0: bool) -> None:
    """
    Calls Qt's 'void QCamera::flashReady(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#flashReady

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QCamera::flashReady(bool a0)
    self.uglySide.call('ritual_ZN7QCamera10flashReadyEb', a0)

  def flashModeChanged(self) -> None:
    """
    Calls Qt's 'void QCamera::flashModeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#flashModeChanged
    """
    #  void QCamera::flashModeChanged()
    self.uglySide.call('ritual_ZN7QCamera16flashModeChangedEv')

  def torchModeChanged(self) -> None:
    """
    Calls Qt's 'void QCamera::torchModeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#torchModeChanged
    """
    #  void QCamera::torchModeChanged()
    self.uglySide.call('ritual_ZN7QCamera16torchModeChangedEv')

  @overload(float)
  def exposureTimeChanged(self, speed: float) -> None:
    """
    Calls Qt's 'void QCamera::exposureTimeChanged(float speed)'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#exposureTimeChanged

    Parameters
    ----------

    speed : float
      Passed on as it is.
    """
    #  void QCamera::exposureTimeChanged(float speed)
    self.uglySide.call('ritual_ZN7QCamera19exposureTimeChangedEf', speed)

  @overload(float)
  def manualExposureTimeChanged(self, speed: float) -> None:
    """
    Calls Qt's 'void QCamera::manualExposureTimeChanged(float speed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcamera.html#manualExposureTimeChanged

    Parameters
    ----------

    speed : float
      Passed on as it is.
    """
    #  void QCamera::manualExposureTimeChanged(float speed)
    self.uglySide.call(
        'ritual_ZN7QCamera25manualExposureTimeChangedEf', speed,
    )

  @overload(int)
  def isoSensitivityChanged(self, a0: int) -> None:
    """
    Calls Qt's 'void QCamera::isoSensitivityChanged(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#isoSensitivityChanged

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QCamera::isoSensitivityChanged(int a0)
    self.uglySide.call('ritual_ZN7QCamera21isoSensitivityChangedEi', a0)

  @overload(int)
  def manualIsoSensitivityChanged(self, a0: int) -> None:
    """
    Calls Qt's 'void QCamera::manualIsoSensitivityChanged(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcamera.html#manualIsoSensitivityChanged

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QCamera::manualIsoSensitivityChanged(int a0)
    self.uglySide.call(
        'ritual_ZN7QCamera27manualIsoSensitivityChangedEi', a0,
    )

  @overload(float)
  def exposureCompensationChanged(self, a0: float) -> None:
    """
    Calls Qt's 'void QCamera::exposureCompensationChanged(float a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcamera.html#exposureCompensationChanged

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QCamera::exposureCompensationChanged(float a0)
    self.uglySide.call(
        'ritual_ZN7QCamera27exposureCompensationChangedEf', a0,
    )

  def exposureModeChanged(self) -> None:
    """
    Calls Qt's 'void QCamera::exposureModeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#exposureModeChanged
    """
    #  void QCamera::exposureModeChanged()
    self.uglySide.call('ritual_ZN7QCamera19exposureModeChangedEv')

  def whiteBalanceModeChanged(self) -> None:
    """
    Calls Qt's 'void QCamera::whiteBalanceModeChanged() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcamera.html#whiteBalanceModeChanged
    """
    #  void QCamera::whiteBalanceModeChanged() const
    self.uglySide.call('ritual_ZNK7QCamera23whiteBalanceModeChangedEv')

  def colorTemperatureChanged(self) -> None:
    """
    Calls Qt's 'void QCamera::colorTemperatureChanged() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcamera.html#colorTemperatureChanged
    """
    #  void QCamera::colorTemperatureChanged() const
    self.uglySide.call('ritual_ZNK7QCamera23colorTemperatureChangedEv')

  def brightnessChanged(self) -> None:
    """
    Calls Qt's 'void QCamera::brightnessChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#brightnessChanged
    """
    #  void QCamera::brightnessChanged()
    self.uglySide.call('ritual_ZN7QCamera17brightnessChangedEv')

  def contrastChanged(self) -> None:
    """
    Calls Qt's 'void QCamera::contrastChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#contrastChanged
    """
    #  void QCamera::contrastChanged()
    self.uglySide.call('ritual_ZN7QCamera15contrastChangedEv')

  def saturationChanged(self) -> None:
    """
    Calls Qt's 'void QCamera::saturationChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#saturationChanged
    """
    #  void QCamera::saturationChanged()
    self.uglySide.call('ritual_ZN7QCamera17saturationChangedEv')

  def hueChanged(self) -> None:
    """
    Calls Qt's 'void QCamera::hueChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#hueChanged
    """
    #  void QCamera::hueChanged()
    self.uglySide.call('ritual_ZN7QCamera10hueChangedEv')

  def d_func(self) -> Optional[QCameraPrivate]:
    """
    Calls Qt's 'QCameraPrivate *QCamera::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qcamera.html#d_func

    Returns
    -------

    Optional[QCameraPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCameraPrivate *QCamera::d_func()
    address = self.uglySide.call('ritual_ZN7QCamera6d_funcEv')
    from . import QCameraPrivate
    return QCameraPrivate._cuteAt(address)

  @staticmethod
  def platformCamera(*__, **_) -> Never:
    """
    Qt's 'class QPlatformCamera *QCamera::platformCamera()': gives 'class
    QPlatformCamera', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QCamera.platformCamera' has no cute function yet. Qt's 'class "
        "QPlatformCamera *QCamera::platformCamera()': gives 'class "
        "QPlatformCamera', which has no cute class yet.")
