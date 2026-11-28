"""
Qt3DExtras::QOrbitCameraController binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/qorbitcameracontroller.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DExtras

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


class QOrbitCameraController(Qt3DExtras.QAbstractCameraController):
  """
  The cute side of Qt's Qt3DExtras::QOrbitCameraController: a plain Python
  object standing in front of one C++ Qt3DExtras::QOrbitCameraController.

  It is built on the cute 'Qt3DExtras::QAbstractCameraController', as Qt's
  Qt3DExtras::QOrbitCameraController is built on Qt's
  Qt3DExtras::QAbstractCameraController, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QOrbitCameraController that has a ritual
  and that Python can call so far, 25 names in all: 'metaObject', 'tr',
  'zoomInLimit', 'upVector', 'inverseXTranslate', 'inverseYTranslate',
  'inversePan', 'inverseTilt', 'zoomTranslateViewCenter', 'setZoomInLimit',
  'setUpVector', 'setInverseXTranslate', 'setInverseYTranslate',
  'setInversePan', 'setInverseTilt', 'setZoomTranslateViewCenter',
  'zoomInLimitChanged', 'upVectorChanged', 'inverseXTranslateChanged',
  'inverseYTranslateChanged', 'inversePanChanged', 'inverseTiltChanged',
  'zoomTranslateViewCenterChanged', 'moveCamera', 'd_func'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DExtras::QOrbitCameraController::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DExtras::QOrbitCameraController::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DExtras::QOrbitCameraController::~QOrbitCameraController()': the
    destructor: Python never removes a C++
    Qt3DExtras::QOrbitCameraController.
  - Qt's 'Qt3DExtras::QOrbitCameraController::QOrbitCameraController(
    QOrbitCameraControllerPrivate &dd, Qt3DCore::QNode *parent)': takes a
    type Python has no way to hand over yet.
  - Qt's 'const QOrbitCameraControllerPrivate
    *Qt3DExtras::QOrbitCameraController::d_func() const': takes in Python
    what 'QOrbitCameraControllerPrivate
    *Qt3DExtras::QOrbitCameraController::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 33 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DExtras::QOrbitCameraController is created at the first use,
    not by 'Qt3DExtras::QOrbitCameraController(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QOrbitCameraController.
  - Qt tells when it has removed the C++ Qt3DExtras::QOrbitCameraController.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  """

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
    Calls Qt's 'QString Qt3DExtras::QOrbitCameraController::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qorbitcameracontroller.html#tr

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
    #  QString Qt3DExtras::QOrbitCameraController::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN10Qt3DExtras22QOrbitCameraController2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::QOrbitCameraController'

  #  A C++ Qt3DExtras::QOrbitCameraController Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_QOrbitCameraController'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *Qt3DExtras::QOrbitCameraController::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qorbitcameracontroller.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DExtras::QOrbitCameraController::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras22QOrbitCameraController10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def zoomInLimit(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QOrbitCameraController::zoomInLimit()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qorbitcameracontroller.html#zoomInLimit
    """
    #  float Qt3DExtras::QOrbitCameraController::zoomInLimit() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras22QOrbitCameraController11zoomInLimitEv',
    )

  def upVector(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D Qt3DExtras::QOrbitCameraController::upVector()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qorbitcameracontroller.html#upVector

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Qt3DExtras::QOrbitCameraController::upVector() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras22QOrbitCameraController8upVectorEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def inverseXTranslate(self) -> bool:
    """
    Calls Qt's 'bool Qt3DExtras::QOrbitCameraController::inverseXTranslate()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qorbitcameracontroller.html
    """
    #  bool Qt3DExtras::QOrbitCameraController::inverseXTranslate() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras22QOrbitCameraController17inverseXTranslateE'
        'v',
    )

  def inverseYTranslate(self) -> bool:
    """
    Calls Qt's 'bool Qt3DExtras::QOrbitCameraController::inverseYTranslate()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qorbitcameracontroller.html
    """
    #  bool Qt3DExtras::QOrbitCameraController::inverseYTranslate() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras22QOrbitCameraController17inverseYTranslateE'
        'v',
    )

  def inversePan(self) -> bool:
    """
    Calls Qt's 'bool Qt3DExtras::QOrbitCameraController::inversePan() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qorbitcameracontroller.html#inversePan
    """
    #  bool Qt3DExtras::QOrbitCameraController::inversePan() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras22QOrbitCameraController10inversePanEv',
    )

  def inverseTilt(self) -> bool:
    """
    Calls Qt's 'bool Qt3DExtras::QOrbitCameraController::inverseTilt()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qorbitcameracontroller.html#inverseTilt
    """
    #  bool Qt3DExtras::QOrbitCameraController::inverseTilt() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras22QOrbitCameraController11inverseTiltEv',
    )

  def zoomTranslateViewCenter(self) -> bool:
    """
    Calls Qt's 'bool
    Qt3DExtras::QOrbitCameraController::zoomTranslateViewCenter() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qorbitcameracontroller.html
    """
    #  bool Qt3DExtras::QOrbitCameraController::zoomTranslateViewCenter()
    #      const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras22QOrbitCameraController23zoomTranslateViewC'
        'enterEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setZoomInLimit(self, zoomInLimit: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QOrbitCameraController::setZoomInLimit(float
    zoomInLimit)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qorbitcameracontroller.html

    Parameters
    ----------

    zoomInLimit : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QOrbitCameraController::setZoomInLimit(float
    #      zoomInLimit)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras22QOrbitCameraController14setZoomInLimitEf',
        zoomInLimit,
    )

  @overload(QVector3D)
  def setUpVector(self, upVector: QVector3D) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QOrbitCameraController::setUpVector(const
    QVector3D &upVector)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qorbitcameracontroller.html#setUpVector

    Parameters
    ----------

    upVector : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DExtras::QOrbitCameraController::setUpVector(const QVector3D
    #      &upVector)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras22QOrbitCameraController11setUpVectorERK9QVec'
        'tor3D',
        self._valueOf(upVector),
    )

  @overload(bool)
  def setInverseXTranslate(self, isInverse: bool) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QOrbitCameraController::setInverseXTranslate(bool
    isInverse)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qorbitcameracontroller.html

    Parameters
    ----------

    isInverse : bool
      Passed on as it is.
    """
    #  void Qt3DExtras::QOrbitCameraController::setInverseXTranslate(bool
    #      isInverse)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras22QOrbitCameraController20setInverseXTranslat'
        'eEb',
        isInverse,
    )

  @overload(bool)
  def setInverseYTranslate(self, isInverse: bool) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QOrbitCameraController::setInverseYTranslate(bool
    isInverse)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qorbitcameracontroller.html

    Parameters
    ----------

    isInverse : bool
      Passed on as it is.
    """
    #  void Qt3DExtras::QOrbitCameraController::setInverseYTranslate(bool
    #      isInverse)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras22QOrbitCameraController20setInverseYTranslat'
        'eEb',
        isInverse,
    )

  @overload(bool)
  def setInversePan(self, isInverse: bool) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QOrbitCameraController::setInversePan(bool
    isInverse)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qorbitcameracontroller.html

    Parameters
    ----------

    isInverse : bool
      Passed on as it is.
    """
    #  void Qt3DExtras::QOrbitCameraController::setInversePan(bool isInverse)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras22QOrbitCameraController13setInversePanEb',
        isInverse,
    )

  @overload(bool)
  def setInverseTilt(self, isInverse: bool) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QOrbitCameraController::setInverseTilt(bool
    isInverse)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qorbitcameracontroller.html

    Parameters
    ----------

    isInverse : bool
      Passed on as it is.
    """
    #  void Qt3DExtras::QOrbitCameraController::setInverseTilt(bool
    #      isInverse)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras22QOrbitCameraController14setInverseTiltEb',
        isInverse,
    )

  @overload(bool)
  def setZoomTranslateViewCenter(self, isTranslate: bool) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QOrbitCameraController::setZoomTranslateViewCenter(bool
    isTranslate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qorbitcameracontroller.html

    Parameters
    ----------

    isTranslate : bool
      Passed on as it is.
    """
    #  void Qt3DExtras::QOrbitCameraController::setZoomTranslateViewCenter(
    #      bool isTranslate)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras22QOrbitCameraController26setZoomTranslateVie'
        'wCenterEb',
        isTranslate,
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
    'Qt3DExtras::QOrbitCameraController::QOrbitCameraController(Qt3DCore::
    QNode *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qorbitcameracontroller.html

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DExtras::QOrbitCameraController::QOrbitCameraController(
    #      Qt3DCore::QNode *parent)
    self._noteCreation(QOrbitCameraController, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras22QOrbitCameraControllerC1EPN8Qt3DCore5QNodeE',
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

  def zoomInLimitChanged(self) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QOrbitCameraController::zoomInLimitChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qorbitcameracontroller.html
    """
    #  void Qt3DExtras::QOrbitCameraController::zoomInLimitChanged()
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras22QOrbitCameraController18zoomInLimitChangedE'
        'v',
    )

  @overload(QVector3D)
  def upVectorChanged(self, upVector: QVector3D) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QOrbitCameraController::upVectorChanged(const QVector3D
    &upVector)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qorbitcameracontroller.html

    Parameters
    ----------

    upVector : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DExtras::QOrbitCameraController::upVectorChanged(const
    #      QVector3D &upVector)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras22QOrbitCameraController15upVectorChangedERK9'
        'QVector3D',
        self._valueOf(upVector),
    )

  @overload(bool)
  def inverseXTranslateChanged(self, isInverse: bool) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QOrbitCameraController::inverseXTranslateChanged(bool
    isInverse)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qorbitcameracontroller.html

    Parameters
    ----------

    isInverse : bool
      Passed on as it is.
    """
    #  void Qt3DExtras::QOrbitCameraController::inverseXTranslateChanged(bool
    #      isInverse)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras22QOrbitCameraController24inverseXTranslateCh'
        'angedEb',
        isInverse,
    )

  @overload(bool)
  def inverseYTranslateChanged(self, isInverse: bool) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QOrbitCameraController::inverseYTranslateChanged(bool
    isInverse)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qorbitcameracontroller.html

    Parameters
    ----------

    isInverse : bool
      Passed on as it is.
    """
    #  void Qt3DExtras::QOrbitCameraController::inverseYTranslateChanged(bool
    #      isInverse)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras22QOrbitCameraController24inverseYTranslateCh'
        'angedEb',
        isInverse,
    )

  @overload(bool)
  def inversePanChanged(self, isInverse: bool) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QOrbitCameraController::inversePanChanged(bool isInverse)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qorbitcameracontroller.html

    Parameters
    ----------

    isInverse : bool
      Passed on as it is.
    """
    #  void Qt3DExtras::QOrbitCameraController::inversePanChanged(bool
    #      isInverse)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras22QOrbitCameraController17inversePanChangedEb',
        isInverse,
    )

  @overload(bool)
  def inverseTiltChanged(self, isInverse: bool) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QOrbitCameraController::inverseTiltChanged(bool isInverse)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qorbitcameracontroller.html

    Parameters
    ----------

    isInverse : bool
      Passed on as it is.
    """
    #  void Qt3DExtras::QOrbitCameraController::inverseTiltChanged(bool
    #      isInverse)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras22QOrbitCameraController18inverseTiltChangedE'
        'b',
        isInverse,
    )

  @overload(bool)
  def zoomTranslateViewCenterChanged(self, isTranslate: bool) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QOrbitCameraController::zoomTranslateViewCenterChanged(bool
    isTranslate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qorbitcameracontroller.html

    Parameters
    ----------

    isTranslate : bool
      Passed on as it is.
    """
    #  void Qt3DExtras::QOrbitCameraController::
    #      zoomTranslateViewCenterChanged(bool isTranslate)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras22QOrbitCameraController30zoomTranslateViewCe'
        'nterChangedEb',
        isTranslate,
    )

  @overload(Qt3DExtras.QAbstractCameraController.InputState, float)
  def moveCamera(
      self,
      state: Qt3DExtras.QAbstractCameraController.InputState,
      dt: float,
  ) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QOrbitCameraController::moveCamera(const
    QAbstractCameraController::InputState &state, float dt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qorbitcameracontroller.html#moveCamera

    Parameters
    ----------

    state : Qt3DExtras.QAbstractCameraController.InputState
      Passed on as a value: Qt reads the C++
      Qt3DExtras::QAbstractCameraController::InputState, which stays Python's
      own.

    dt : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QOrbitCameraController::moveCamera(const
    #      QAbstractCameraController::InputState &state, float dt)
    ritual = (
        'ritual_ZN10Qt3DExtras22QOrbitCameraController10moveCameraERKNS_25Q'
        'AbstractCameraController10InputStateEf')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DExtras22QOrbitCameraController10moveCameraERK'
          'NS_25QAbstractCameraController10InputStateEf')
    self.uglySide.call(ritual, self._valueOf(state), dt)

  def d_func(self) -> Optional[Qt3DExtras.QOrbitCameraControllerPrivate]:
    """
    Calls Qt's 'QOrbitCameraControllerPrivate
    *Qt3DExtras::QOrbitCameraController::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qorbitcameracontroller.html#d_func

    Returns
    -------

    Optional[Qt3DExtras.QOrbitCameraControllerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOrbitCameraControllerPrivate
    #      *Qt3DExtras::QOrbitCameraController::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DExtras22QOrbitCameraController6d_funcEv',
    )
    return Qt3DExtras.QOrbitCameraControllerPrivate._cuteAt(address)
