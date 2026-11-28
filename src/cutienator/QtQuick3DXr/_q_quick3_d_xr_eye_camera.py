"""
QQuick3DXrEyeCamera binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrcamera_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DXrEyeCamera to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtQuick3D import QQuick3DCamera

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QMatrix4x4
  from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
  from . import QQuick3DXrOrigin
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMatrix4x4 = WAIT['QMatrix4x4']
  QQuick3DXrOrigin = WAIT['QQuick3DXrOrigin']
  QSSGRenderGraphObject = WAIT['QSSGRenderGraphObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DXrEyeCamera(QQuick3DCamera):
  """
  The cute side of Qt's QQuick3DXrEyeCamera: a plain Python object standing
  in front of one C++ QQuick3DXrEyeCamera.

  It is built on the cute 'QQuick3DCamera', as Qt's QQuick3DXrEyeCamera is
  built on Qt's QQuick3DCamera, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DXrEyeCamera that has a ritual and that
  Python can call so far, 23 names in all: 'metaObject', 'tr', 'leftTangent',
  'rightTangent', 'upTangent', 'downTangent', 'clipNear', 'clipFar',
  'setLeftTangent', 'setRightTangent', 'setUpTangent', 'setDownTangent',
  'setClipNear', 'setClipFar', 'setProjection', 'leftTangentChanged',
  'rightTangentChanged', 'upTangentChanged', 'downTangentChanged',
  'clipNearChanged', 'clipFarChanged', 'updateSpatialNode',
  'maybeUpdateProjection'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DXrEyeCamera::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuick3DXrEyeCamera::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuick3DXrEyeCamera::markDirty(DirtyFlag flag)': names the
    enum 'QQuick3DXrEyeCamera::DirtyFlag', whose class cannot be named here.

  What has no ritual
  ------------------

  2 of the 29 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DXrEyeCamera is created at the first use, not by
    'QQuick3DXrEyeCamera(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DXrEyeCamera.
  - Qt tells when it has removed the C++ QQuick3DXrEyeCamera. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DXrEyeCamera that has no cute function yet,
    'markDirty', holds a function that raises 'NotImplementedError', and its
    docstring says why.
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
    Calls Qt's 'QString QQuick3DXrEyeCamera::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxreyecamera.html#tr

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
    #  QString QQuick3DXrEyeCamera::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QQuick3DXrEyeCamera2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DXrEyeCamera'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DXrEyeCamera::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxreyecamera.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DXrEyeCamera::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuick3DXrEyeCamera10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def leftTangent(self) -> float:
    """
    Calls Qt's 'float QQuick3DXrEyeCamera::leftTangent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxreyecamera.html#leftTangent
    """
    #  float QQuick3DXrEyeCamera::leftTangent() const
    return self.uglySide.call(
        'ritual_ZNK19QQuick3DXrEyeCamera11leftTangentEv',
    )

  def rightTangent(self) -> float:
    """
    Calls Qt's 'float QQuick3DXrEyeCamera::rightTangent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxreyecamera.html#rightTangent
    """
    #  float QQuick3DXrEyeCamera::rightTangent() const
    return self.uglySide.call(
        'ritual_ZNK19QQuick3DXrEyeCamera12rightTangentEv',
    )

  def upTangent(self) -> float:
    """
    Calls Qt's 'float QQuick3DXrEyeCamera::upTangent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxreyecamera.html#upTangent
    """
    #  float QQuick3DXrEyeCamera::upTangent() const
    return self.uglySide.call('ritual_ZNK19QQuick3DXrEyeCamera9upTangentEv')

  def downTangent(self) -> float:
    """
    Calls Qt's 'float QQuick3DXrEyeCamera::downTangent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxreyecamera.html#downTangent
    """
    #  float QQuick3DXrEyeCamera::downTangent() const
    return self.uglySide.call(
        'ritual_ZNK19QQuick3DXrEyeCamera11downTangentEv',
    )

  def clipNear(self) -> float:
    """
    Calls Qt's 'float QQuick3DXrEyeCamera::clipNear() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxreyecamera.html#clipNear
    """
    #  float QQuick3DXrEyeCamera::clipNear() const
    return self.uglySide.call('ritual_ZNK19QQuick3DXrEyeCamera8clipNearEv')

  def clipFar(self) -> float:
    """
    Calls Qt's 'float QQuick3DXrEyeCamera::clipFar() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxreyecamera.html#clipFar
    """
    #  float QQuick3DXrEyeCamera::clipFar() const
    return self.uglySide.call('ritual_ZNK19QQuick3DXrEyeCamera7clipFarEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setLeftTangent(self, leftTangent: float) -> None:
    """
    Calls Qt's 'void QQuick3DXrEyeCamera::setLeftTangent(float leftTangent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxreyecamera.html#setLeftTangent

    Parameters
    ----------

    leftTangent : float
      Passed on as it is.
    """
    #  void QQuick3DXrEyeCamera::setLeftTangent(float leftTangent)
    self.uglySide.call(
        'ritual_ZN19QQuick3DXrEyeCamera14setLeftTangentEf', leftTangent,
    )

  @overload(float)
  def setRightTangent(self, rightTangent: float) -> None:
    """
    Calls Qt's 'void QQuick3DXrEyeCamera::setRightTangent(float
    rightTangent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxreyecamera.html#setRightTangent

    Parameters
    ----------

    rightTangent : float
      Passed on as it is.
    """
    #  void QQuick3DXrEyeCamera::setRightTangent(float rightTangent)
    self.uglySide.call(
        'ritual_ZN19QQuick3DXrEyeCamera15setRightTangentEf', rightTangent,
    )

  @overload(float)
  def setUpTangent(self, upTangent: float) -> None:
    """
    Calls Qt's 'void QQuick3DXrEyeCamera::setUpTangent(float upTangent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxreyecamera.html#setUpTangent

    Parameters
    ----------

    upTangent : float
      Passed on as it is.
    """
    #  void QQuick3DXrEyeCamera::setUpTangent(float upTangent)
    self.uglySide.call(
        'ritual_ZN19QQuick3DXrEyeCamera12setUpTangentEf', upTangent,
    )

  @overload(float)
  def setDownTangent(self, downTangent: float) -> None:
    """
    Calls Qt's 'void QQuick3DXrEyeCamera::setDownTangent(float downTangent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxreyecamera.html#setDownTangent

    Parameters
    ----------

    downTangent : float
      Passed on as it is.
    """
    #  void QQuick3DXrEyeCamera::setDownTangent(float downTangent)
    self.uglySide.call(
        'ritual_ZN19QQuick3DXrEyeCamera14setDownTangentEf', downTangent,
    )

  @overload(float)
  def setClipNear(self, clipNear: float) -> None:
    """
    Calls Qt's 'void QQuick3DXrEyeCamera::setClipNear(float clipNear)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxreyecamera.html#setClipNear

    Parameters
    ----------

    clipNear : float
      Passed on as it is.
    """
    #  void QQuick3DXrEyeCamera::setClipNear(float clipNear)
    self.uglySide.call(
        'ritual_ZN19QQuick3DXrEyeCamera11setClipNearEf', clipNear,
    )

  @overload(float)
  def setClipFar(self, clipFar: float) -> None:
    """
    Calls Qt's 'void QQuick3DXrEyeCamera::setClipFar(float clipFar)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxreyecamera.html#setClipFar

    Parameters
    ----------

    clipFar : float
      Passed on as it is.
    """
    #  void QQuick3DXrEyeCamera::setClipFar(float clipFar)
    self.uglySide.call(
        'ritual_ZN19QQuick3DXrEyeCamera10setClipFarEf', clipFar,
    )

  @overload(QMatrix4x4)
  def setProjection(self, projection: QMatrix4x4) -> None:
    """
    Calls Qt's 'void QQuick3DXrEyeCamera::setProjection(const QMatrix4x4
    &projection)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxreyecamera.html#setProjection

    Parameters
    ----------

    projection : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.
    """
    #  void QQuick3DXrEyeCamera::setProjection(const QMatrix4x4 &projection)
    self.uglySide.call(
        'ritual_ZN19QQuick3DXrEyeCamera13setProjectionERK10QMatrix4x4',
        self._valueOf(projection),
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
  @overload(QQuick3DXrOrigin)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuick3DXrOrigin] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DXrEyeCamera::QQuick3DXrEyeCamera(QQuick3DXrOrigin *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxreyecamera.html#QQuick3DXrEyeCamera

    Parameters
    ----------

    parent : Optional[QQuick3DXrOrigin]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DXrEyeCamera::QQuick3DXrEyeCamera(QQuick3DXrOrigin *parent)
    self._noteCreation(QQuick3DXrEyeCamera, lambda: Rituals.call(
        'ritual_ZN19QQuick3DXrEyeCameraC1EP16QQuick3DXrOrigin',
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

  @overload(float)
  def leftTangentChanged(self, leftTangent: float) -> None:
    """
    Calls Qt's 'void QQuick3DXrEyeCamera::leftTangentChanged(float
    leftTangent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxreyecamera.html#leftTangentChanged

    Parameters
    ----------

    leftTangent : float
      Passed on as it is.
    """
    #  void QQuick3DXrEyeCamera::leftTangentChanged(float leftTangent)
    self.uglySide.call(
        'ritual_ZN19QQuick3DXrEyeCamera18leftTangentChangedEf', leftTangent,
    )

  @overload(float)
  def rightTangentChanged(self, rightTangent: float) -> None:
    """
    Calls Qt's 'void QQuick3DXrEyeCamera::rightTangentChanged(float
    rightTangent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxreyecamera.html#rightTangentChanged

    Parameters
    ----------

    rightTangent : float
      Passed on as it is.
    """
    #  void QQuick3DXrEyeCamera::rightTangentChanged(float rightTangent)
    self.uglySide.call(
        'ritual_ZN19QQuick3DXrEyeCamera19rightTangentChangedEf',
        rightTangent,
    )

  @overload(float)
  def upTangentChanged(self, upTangent: float) -> None:
    """
    Calls Qt's 'void QQuick3DXrEyeCamera::upTangentChanged(float upTangent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxreyecamera.html#upTangentChanged

    Parameters
    ----------

    upTangent : float
      Passed on as it is.
    """
    #  void QQuick3DXrEyeCamera::upTangentChanged(float upTangent)
    self.uglySide.call(
        'ritual_ZN19QQuick3DXrEyeCamera16upTangentChangedEf', upTangent,
    )

  @overload(float)
  def downTangentChanged(self, downTangent: float) -> None:
    """
    Calls Qt's 'void QQuick3DXrEyeCamera::downTangentChanged(float
    downTangent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxreyecamera.html#downTangentChanged

    Parameters
    ----------

    downTangent : float
      Passed on as it is.
    """
    #  void QQuick3DXrEyeCamera::downTangentChanged(float downTangent)
    self.uglySide.call(
        'ritual_ZN19QQuick3DXrEyeCamera18downTangentChangedEf', downTangent,
    )

  @overload(float)
  def clipNearChanged(self, clipNear: float) -> None:
    """
    Calls Qt's 'void QQuick3DXrEyeCamera::clipNearChanged(float clipNear)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxreyecamera.html#clipNearChanged

    Parameters
    ----------

    clipNear : float
      Passed on as it is.
    """
    #  void QQuick3DXrEyeCamera::clipNearChanged(float clipNear)
    self.uglySide.call(
        'ritual_ZN19QQuick3DXrEyeCamera15clipNearChangedEf', clipNear,
    )

  @overload(float)
  def clipFarChanged(self, clipFar: float) -> None:
    """
    Calls Qt's 'void QQuick3DXrEyeCamera::clipFarChanged(float clipFar)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxreyecamera.html#clipFarChanged

    Parameters
    ----------

    clipFar : float
      Passed on as it is.
    """
    #  void QQuick3DXrEyeCamera::clipFarChanged(float clipFar)
    self.uglySide.call(
        'ritual_ZN19QQuick3DXrEyeCamera14clipFarChangedEf', clipFar,
    )

  @overload(QSSGRenderGraphObject)
  @overload(NoneType)
  def updateSpatialNode(
      self,
      node: Optional[QSSGRenderGraphObject],
  ) -> Optional[QSSGRenderGraphObject]:
    """
    Calls Qt's 'QSSGRenderGraphObject
    *QQuick3DXrEyeCamera::updateSpatialNode(QSSGRenderGraphObject *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxreyecamera.html#updateSpatialNode

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
    #      *QQuick3DXrEyeCamera::updateSpatialNode(QSSGRenderGraphObject
    #      *node)
    ritual = (
        'ritual_ZN19QQuick3DXrEyeCamera17updateSpatialNodeEP21QSSGRenderGra'
        'phObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuick3DXrEyeCamera17updateSpatialNodeEP21QSSGRen'
          'derGraphObject')
    address = self.uglySide.call(ritual, self._addressOf(node))
    from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
    return QSSGRenderGraphObject._cuteAt(address)

  def maybeUpdateProjection(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrEyeCamera::maybeUpdateProjection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxreyecamera.html#maybeUpdateProjection
    """
    #  void QQuick3DXrEyeCamera::maybeUpdateProjection()
    self.uglySide.call(
        'ritual_ZN19QQuick3DXrEyeCamera21maybeUpdateProjectionEv',
    )

  @staticmethod
  def markDirty(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrEyeCamera::markDirty(DirtyFlag flag)': names the
    enum 'QQuick3DXrEyeCamera::DirtyFlag', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QQuick3DXrEyeCamera.markDirty' has no cute function yet. Qt's "
        "'void QQuick3DXrEyeCamera::markDirty(DirtyFlag flag)': names the "
        "enum 'QQuick3DXrEyeCamera::DirtyFlag', whose class cannot be named "
        "here.")
