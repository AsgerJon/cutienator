"""
Qt3DRender::QLevelOfDetail binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qlevelofdetail.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

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


class QLevelOfDetail(Qt3DCore.QComponent):
  """
  The cute side of Qt's Qt3DRender::QLevelOfDetail: a plain Python object
  standing in front of one C++ Qt3DRender::QLevelOfDetail.

  It is built on the cute 'Qt3DCore::QComponent', as Qt's
  Qt3DRender::QLevelOfDetail is built on Qt's Qt3DCore::QComponent, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QLevelOfDetail that has a ritual and
  that Python can call so far, 16 names in all: 'metaObject', 'tr', 'camera',
  'currentIndex', 'thresholdType', 'volumeOverride', 'createBoundingSphere',
  'setCamera', 'setCurrentIndex', 'setThresholdType', 'setVolumeOverride',
  'cameraChanged', 'currentIndexChanged', 'thresholdTypeChanged',
  'volumeOverrideChanged', 'd_func'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QLevelOfDetail::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int Qt3DRender::QLevelOfDetail::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QLevelOfDetail::~QLevelOfDetail()': the destructor:
    Python never removes a C++ Qt3DRender::QLevelOfDetail.
  - Qt's 'QList<qreal> Qt3DRender::QLevelOfDetail::thresholds() const': gives
    a type Python has no way to take yet.
  - Qt's 'void Qt3DRender::QLevelOfDetail::setThresholds(const QList<qreal>
    &thresholds)': takes a type Python has no way to hand over yet.
  - Qt's 'void Qt3DRender::QLevelOfDetail::thresholdsChanged(const
    QList<qreal> &thresholds)': takes a type Python has no way to hand over
    yet.
  - Qt's 'Qt3DRender::QLevelOfDetail::QLevelOfDetail(QLevelOfDetailPrivate
    &dd, Qt3DCore::QNode *parent)': takes a type Python has no way to hand
    over yet.
  - Qt's 'const QLevelOfDetailPrivate *Qt3DRender::QLevelOfDetail::d_func()
    const': takes in Python what 'QLevelOfDetailPrivate
    *Qt3DRender::QLevelOfDetail::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 27 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QLevelOfDetail is created at the first use, not by
    'Qt3DRender::QLevelOfDetail(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QLevelOfDetail.
  - Qt tells when it has removed the C++ Qt3DRender::QLevelOfDetail. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DRender::QLevelOfDetail that has no cute function
    yet, 'setThresholds', 'thresholds', 'thresholdsChanged', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside Qt3DRender::QLevelOfDetail, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class ThresholdType(CuteNum):
    """
    The enum 'Qt3DRender::QLevelOfDetail::ThresholdType' of Qt, with the 2
    names Qt gives in it.
    """

    DistanceToCameraThreshold = Kee[int](0)
    ProjectedScreenPixelSizeThreshold = Kee[int](1)

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
    Calls Qt's 'QString Qt3DRender::QLevelOfDetail::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qlevelofdetail.html#tr

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
    #  QString Qt3DRender::QLevelOfDetail::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender14QLevelOfDetail2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QLevelOfDetail'

  #  A C++ Qt3DRender::QLevelOfDetail Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QLevelOfDetail'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QLevelOfDetail::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qlevelofdetail.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QLevelOfDetail::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender14QLevelOfDetail10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def camera(self) -> Optional[Qt3DRender.QCamera]:
    """
    Calls Qt's 'QCamera *Qt3DRender::QLevelOfDetail::camera() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qlevelofdetail.html#camera

    Returns
    -------

    Optional[Qt3DRender.QCamera]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCamera *Qt3DRender::QLevelOfDetail::camera() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender14QLevelOfDetail6cameraEv',
    )
    return Qt3DRender.QCamera._cuteAt(address)

  def currentIndex(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QLevelOfDetail::currentIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qlevelofdetail.html#currentIndex
    """
    #  int Qt3DRender::QLevelOfDetail::currentIndex() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender14QLevelOfDetail12currentIndexEv',
    )

  def thresholdType(self) -> ThresholdType:
    """
    Calls Qt's 'ThresholdType Qt3DRender::QLevelOfDetail::thresholdType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qlevelofdetail.html#thresholdType

    Returns
    -------

    ThresholdType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ThresholdType(number)'
      gives.
    """
    #  ThresholdType Qt3DRender::QLevelOfDetail::thresholdType() const
    return QLevelOfDetail.ThresholdType(self.uglySide.call(
        'ritual_ZNK10Qt3DRender14QLevelOfDetail13thresholdTypeEv',
    ))

  def volumeOverride(self) -> Qt3DRender.QLevelOfDetailBoundingSphere:
    """
    Calls Qt's 'QLevelOfDetailBoundingSphere
    Qt3DRender::QLevelOfDetail::volumeOverride() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qlevelofdetail.html#volumeOverride

    Returns
    -------

    Qt3DRender.QLevelOfDetailBoundingSphere
      A new cute Qt3DRender::QLevelOfDetailBoundingSphere around the copy Qt
      gave back. Python owns it.
    """
    #  QLevelOfDetailBoundingSphere
    #      Qt3DRender::QLevelOfDetail::volumeOverride() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender14QLevelOfDetail14volumeOverrideEv',
    )
    return Qt3DRender.QLevelOfDetailBoundingSphere._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DRender.QCamera'])
  @overload(NoneType)
  def setCamera(self, camera: Optional[Qt3DRender.QCamera]) -> None:
    """
    Calls Qt's 'void Qt3DRender::QLevelOfDetail::setCamera(QCamera *camera)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qlevelofdetail.html#setCamera

    Parameters
    ----------

    camera : Optional[Qt3DRender.QCamera]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QLevelOfDetail::setCamera(QCamera *camera)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QLevelOfDetail9setCameraEPNS_7QCameraE',
        self._addressOf(camera),
    )

  @overload(int)
  def setCurrentIndex(self, currentIndex: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QLevelOfDetail::setCurrentIndex(int
    currentIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qlevelofdetail.html#setCurrentIndex

    Parameters
    ----------

    currentIndex : int
      Passed on as it is.
    """
    #  void Qt3DRender::QLevelOfDetail::setCurrentIndex(int currentIndex)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QLevelOfDetail15setCurrentIndexEi',
        currentIndex,
    )

  @overload(ThresholdType)
  def setThresholdType(self, thresholdType: ThresholdType) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QLevelOfDetail::setThresholdType(ThresholdType
    thresholdType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qlevelofdetail.html#setThresholdType

    Parameters
    ----------

    thresholdType : ThresholdType
      Passed on as its number.
    """
    #  void Qt3DRender::QLevelOfDetail::setThresholdType(ThresholdType
    #      thresholdType)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QLevelOfDetail16setThresholdTypeENS0_13Thre'
        'sholdTypeE',
        thresholdType.value,
    )

  @overload(WAIT['Qt3DRender.QLevelOfDetailBoundingSphere'])
  def setVolumeOverride(
      self,
      volumeOverride: Qt3DRender.QLevelOfDetailBoundingSphere,
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::QLevelOfDetail::setVolumeOverride(const
    QLevelOfDetailBoundingSphere &volumeOverride)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qlevelofdetail.html#setVolumeOverride

    Parameters
    ----------

    volumeOverride : Qt3DRender.QLevelOfDetailBoundingSphere
      Passed on as a value: Qt reads the C++
      Qt3DRender::QLevelOfDetailBoundingSphere, which stays Python's own.
    """
    #  void Qt3DRender::QLevelOfDetail::setVolumeOverride(const
    #      QLevelOfDetailBoundingSphere &volumeOverride)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QLevelOfDetail17setVolumeOverrideERKNS_28QL'
        'evelOfDetailBoundingSphereE',
        self._valueOf(volumeOverride),
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
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QLevelOfDetail::QLevelOfDetail(Qt3DCore::QNode *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qlevelofdetail.html#QLevelOfDetail

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QLevelOfDetail::QLevelOfDetail(Qt3DCore::QNode *parent)
    self._noteCreation(QLevelOfDetail, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender14QLevelOfDetailC1EPN8Qt3DCore5QNodeE',
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

  @overload(QVector3D, float)
  def createBoundingSphere(
      self,
      center: QVector3D,
      radius: float,
  ) -> Qt3DRender.QLevelOfDetailBoundingSphere:
    """
    Calls Qt's 'Qt3DRender::QLevelOfDetailBoundingSphere
    Qt3DRender::QLevelOfDetail::createBoundingSphere(const QVector3D &center,
    float radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qlevelofdetail.html

    Parameters
    ----------

    center : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    radius : float
      Passed on as it is.

    Returns
    -------

    Qt3DRender.QLevelOfDetailBoundingSphere
      A new cute Qt3DRender::QLevelOfDetailBoundingSphere around the copy Qt
      gave back. Python owns it.
    """
    #  Qt3DRender::QLevelOfDetailBoundingSphere
    #      Qt3DRender::QLevelOfDetail::createBoundingSphere(const QVector3D
    #      &center, float radius)
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender14QLevelOfDetail20createBoundingSphereERK9QVe'
        'ctor3Df',
        self._valueOf(center), radius,
    )
    return Qt3DRender.QLevelOfDetailBoundingSphere._cuteOwning(address)

  @overload(WAIT['Qt3DRender.QCamera'])
  @overload(NoneType)
  def cameraChanged(self, camera: Optional[Qt3DRender.QCamera]) -> None:
    """
    Calls Qt's 'void Qt3DRender::QLevelOfDetail::cameraChanged(QCamera
    *camera)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qlevelofdetail.html#cameraChanged

    Parameters
    ----------

    camera : Optional[Qt3DRender.QCamera]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QLevelOfDetail::cameraChanged(QCamera *camera)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QLevelOfDetail13cameraChangedEPNS_7QCameraE',
        self._addressOf(camera),
    )

  @overload(int)
  def currentIndexChanged(self, currentIndex: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QLevelOfDetail::currentIndexChanged(int
    currentIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qlevelofdetail.html#currentIndexChanged

    Parameters
    ----------

    currentIndex : int
      Passed on as it is.
    """
    #  void Qt3DRender::QLevelOfDetail::currentIndexChanged(int currentIndex)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QLevelOfDetail19currentIndexChangedEi',
        currentIndex,
    )

  @overload(ThresholdType)
  def thresholdTypeChanged(self, thresholdType: ThresholdType) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QLevelOfDetail::thresholdTypeChanged(ThresholdType
    thresholdType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qlevelofdetail.html

    Parameters
    ----------

    thresholdType : ThresholdType
      Passed on as its number.
    """
    #  void Qt3DRender::QLevelOfDetail::thresholdTypeChanged(ThresholdType
    #      thresholdType)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QLevelOfDetail20thresholdTypeChangedENS0_13'
        'ThresholdTypeE',
        thresholdType.value,
    )

  @overload(WAIT['Qt3DRender.QLevelOfDetailBoundingSphere'])
  def volumeOverrideChanged(
      self,
      volumeOverride: Qt3DRender.QLevelOfDetailBoundingSphere,
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::QLevelOfDetail::volumeOverrideChanged(const
    QLevelOfDetailBoundingSphere &volumeOverride)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qlevelofdetail.html

    Parameters
    ----------

    volumeOverride : Qt3DRender.QLevelOfDetailBoundingSphere
      Passed on as a value: Qt reads the C++
      Qt3DRender::QLevelOfDetailBoundingSphere, which stays Python's own.
    """
    #  void Qt3DRender::QLevelOfDetail::volumeOverrideChanged(const
    #      QLevelOfDetailBoundingSphere &volumeOverride)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QLevelOfDetail21volumeOverrideChangedERKNS_'
        '28QLevelOfDetailBoundingSphereE',
        self._valueOf(volumeOverride),
    )

  def d_func(self) -> Optional[Qt3DRender.QLevelOfDetailPrivate]:
    """
    Calls Qt's 'QLevelOfDetailPrivate *Qt3DRender::QLevelOfDetail::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qlevelofdetail.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QLevelOfDetailPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLevelOfDetailPrivate *Qt3DRender::QLevelOfDetail::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender14QLevelOfDetail6d_funcEv',
    )
    return Qt3DRender.QLevelOfDetailPrivate._cuteAt(address)

  @staticmethod
  def setThresholds(*__, **_) -> Never:
    """
    Qt's 'void Qt3DRender::QLevelOfDetail::setThresholds(const QList<qreal>
    &thresholds)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QLevelOfDetail.setThresholds' has no cute function "
        "yet. Qt's 'void Qt3DRender::QLevelOfDetail::setThresholds(const "
        "QList<qreal> &thresholds)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def thresholds(*__, **_) -> Never:
    """
    Qt's 'QList<qreal> Qt3DRender::QLevelOfDetail::thresholds() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QLevelOfDetail.thresholds' has no cute function yet. "
        "Qt's 'QList<qreal> Qt3DRender::QLevelOfDetail::thresholds() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def thresholdsChanged(*__, **_) -> Never:
    """
    Qt's 'void Qt3DRender::QLevelOfDetail::thresholdsChanged(const
    QList<qreal> &thresholds)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QLevelOfDetail.thresholdsChanged' has no cute function "
        "yet. Qt's 'void "
        "Qt3DRender::QLevelOfDetail::thresholdsChanged(const QList<qreal> "
        "&thresholds)': takes a type Python has no way to hand over yet.")
