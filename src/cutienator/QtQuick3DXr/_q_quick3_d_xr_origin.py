"""
QQuick3DXrOrigin binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrorigin_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DXrOrigin to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtQuick3D import QQuick3DNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QMatrix4x4, QQuaternion, QVector3D
  from . import QQuick3DXrCamera, QQuick3DXrEyeCamera
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMatrix4x4 = WAIT['QMatrix4x4']
  QQuaternion = WAIT['QQuaternion']
  QQuick3DXrCamera = WAIT['QQuick3DXrCamera']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DXrOrigin(QQuick3DNode):
  """
  The cute side of Qt's QQuick3DXrOrigin: a plain Python object standing in
  front of one C++ QQuick3DXrOrigin.

  It is built on the cute 'QQuick3DNode', as Qt's QQuick3DXrOrigin is built
  on Qt's QQuick3DNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DXrOrigin that has a ritual and that Python
  can call so far, 9 names in all: 'metaObject', 'tr', 'camera', 'setCamera',
  'cameraChanged', 'eyeCamera', 'syncCameraSettings', 'resetCameraSettings',
  'updateTrackedCamera'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DXrOrigin::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuick3DXrOrigin::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DXrOrigin::~QQuick3DXrOrigin()': the destructor: Python
    never removes a C++ QQuick3DXrOrigin.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DXrOrigin is created at the first use, not by
    'QQuick3DXrOrigin(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DXrOrigin.
  - Qt tells when it has removed the C++ QQuick3DXrOrigin. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QQuick3DXrOrigin::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxrorigin.html#tr

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
    #  QString QQuick3DXrOrigin::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QQuick3DXrOrigin2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DXrOrigin'

  #  A C++ QQuick3DXrOrigin Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DXrOrigin'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DXrOrigin::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxrorigin.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DXrOrigin::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuick3DXrOrigin10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def camera(self) -> Optional[QQuick3DXrCamera]:
    """
    Calls Qt's 'QQuick3DXrCamera *QQuick3DXrOrigin::camera() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxrorigin.html#camera

    Returns
    -------

    Optional[QQuick3DXrCamera]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DXrCamera *QQuick3DXrOrigin::camera() const
    address = self.uglySide.call('ritual_ZNK16QQuick3DXrOrigin6cameraEv')
    from . import QQuick3DXrCamera
    return QQuick3DXrCamera._cuteAt(address)

  @overload(int)
  def eyeCamera(self, index: int) -> Optional[QQuick3DXrEyeCamera]:
    """
    Calls Qt's 'QQuick3DXrEyeCamera *QQuick3DXrOrigin::eyeCamera(int index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxrorigin.html#eyeCamera

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QQuick3DXrEyeCamera]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DXrEyeCamera *QQuick3DXrOrigin::eyeCamera(int index) const
    address = self.uglySide.call(
        'ritual_ZNK16QQuick3DXrOrigin9eyeCameraEi', index,
    )
    from . import QQuick3DXrEyeCamera
    return QQuick3DXrEyeCamera._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuick3DXrCamera)
  @overload(NoneType)
  def setCamera(self, newCamera: Optional[QQuick3DXrCamera]) -> None:
    """
    Calls Qt's 'void QQuick3DXrOrigin::setCamera(QQuick3DXrCamera
    *newCamera)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxrorigin.html#setCamera

    Parameters
    ----------

    newCamera : Optional[QQuick3DXrCamera]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DXrOrigin::setCamera(QQuick3DXrCamera *newCamera)
    self.uglySide.call(
        'ritual_ZN16QQuick3DXrOrigin9setCameraEP16QQuick3DXrCamera',
        self._addressOf(newCamera),
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
  @overload(QQuick3DNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuick3DNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DXrOrigin::QQuick3DXrOrigin(QQuick3DNode *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrorigin.html#QQuick3DXrOrigin

    Parameters
    ----------

    parent : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DXrOrigin::QQuick3DXrOrigin(QQuick3DNode *parent)
    self._noteCreation(QQuick3DXrOrigin, lambda: Rituals.call(
        'ritual_ZN16QQuick3DXrOriginC1EP12QQuick3DNode',
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

  def cameraChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrOrigin::cameraChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrorigin.html#cameraChanged
    """
    #  void QQuick3DXrOrigin::cameraChanged()
    self.uglySide.call('ritual_ZN16QQuick3DXrOrigin13cameraChangedEv')

  def syncCameraSettings(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrOrigin::syncCameraSettings()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrorigin.html#syncCameraSettings
    """
    #  void QQuick3DXrOrigin::syncCameraSettings()
    self.uglySide.call('ritual_ZN16QQuick3DXrOrigin18syncCameraSettingsEv')

  def resetCameraSettings(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrOrigin::resetCameraSettings()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrorigin.html#resetCameraSettings
    """
    #  void QQuick3DXrOrigin::resetCameraSettings()
    self.uglySide.call('ritual_ZN16QQuick3DXrOrigin19resetCameraSettingsEv')

  @overload(QMatrix4x4)
  def updateTrackedCamera(self, transform: QMatrix4x4) -> None:
    """
    Calls Qt's 'void QQuick3DXrOrigin::updateTrackedCamera(const QMatrix4x4
    &transform)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrorigin.html#updateTrackedCamera

    Parameters
    ----------

    transform : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.
    """
    #  void QQuick3DXrOrigin::updateTrackedCamera(const QMatrix4x4
    #      &transform)
    self.uglySide.call(
        'ritual_ZN16QQuick3DXrOrigin19updateTrackedCameraERK10QMatrix4x4',
        self._valueOf(transform),
    )

  @overload(QVector3D, QQuaternion)
  def updateTrackedCamera(
      self,
      position: QVector3D,
      rotation: QQuaternion,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DXrOrigin::updateTrackedCamera(QVector3D
    position, QQuaternion rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrorigin.html#updateTrackedCamera

    Parameters
    ----------

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    rotation : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.
    """
    #  void QQuick3DXrOrigin::updateTrackedCamera(QVector3D position,
    #      QQuaternion rotation)
    self.uglySide.call(
        'ritual_ZN16QQuick3DXrOrigin19updateTrackedCameraE9QVector3D11QQuat'
        'ernion',
        self._valueOf(position), self._valueOf(rotation),
    )
