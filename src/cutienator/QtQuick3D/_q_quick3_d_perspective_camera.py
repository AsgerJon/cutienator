"""
QQuick3DPerspectiveCamera binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dperspectivecamera_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DPerspectiveCamera to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QQuick3DCamera, QQuick3DNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSSGRenderGraphObject = WAIT['QSSGRenderGraphObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DPerspectiveCamera(QQuick3DCamera):
  """
  The cute side of Qt's QQuick3DPerspectiveCamera: a plain Python object
  standing in front of one C++ QQuick3DPerspectiveCamera.

  It is built on the cute 'QQuick3DCamera', as Qt's QQuick3DPerspectiveCamera
  is built on Qt's QQuick3DCamera, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DPerspectiveCamera that has a ritual and that
  Python can call so far, 15 names in all: 'metaObject', 'tr', 'clipNear',
  'clipFar', 'fieldOfView', 'fieldOfViewOrientation', 'setClipNear',
  'setClipFar', 'setFieldOfView', 'setFieldOfViewOrientation',
  'clipNearChanged', 'clipFarChanged', 'fieldOfViewChanged',
  'fieldOfViewOrientationChanged', 'updateSpatialNode'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DPerspectiveCamera::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuick3DPerspectiveCamera::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's
    'QQuick3DPerspectiveCamera::QQuick3DPerspectiveCamera(QQuick3DNodePrivate
    &dd, QQuick3DNode *parent)': takes a type Python has no way to hand over
    yet.

  What has no ritual
  ------------------

  2 of the 21 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DPerspectiveCamera is created at the first use, not by
    'QQuick3DPerspectiveCamera(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DPerspectiveCamera.
  - Qt tells when it has removed the C++ QQuick3DPerspectiveCamera. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuick3DPerspectiveCamera, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class FieldOfViewOrientation(CuteNum):
    """
    The enum 'QQuick3DPerspectiveCamera::FieldOfViewOrientation' of Qt, with
    the 2 names Qt gives in it.
    """

    Vertical = Kee[int](0)
    Horizontal = Kee[int](1)

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
    Calls Qt's 'QString QQuick3DPerspectiveCamera::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dperspectivecamera.html#tr

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
    #  QString QQuick3DPerspectiveCamera::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN25QQuick3DPerspectiveCamera2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DPerspectiveCamera'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DPerspectiveCamera::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dperspectivecamera.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DPerspectiveCamera::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuick3DPerspectiveCamera10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def clipNear(self) -> float:
    """
    Calls Qt's 'float QQuick3DPerspectiveCamera::clipNear() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dperspectivecamera.html#clipNear
    """
    #  float QQuick3DPerspectiveCamera::clipNear() const
    return self.uglySide.call(
        'ritual_ZNK25QQuick3DPerspectiveCamera8clipNearEv',
    )

  def clipFar(self) -> float:
    """
    Calls Qt's 'float QQuick3DPerspectiveCamera::clipFar() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dperspectivecamera.html#clipFar
    """
    #  float QQuick3DPerspectiveCamera::clipFar() const
    return self.uglySide.call(
        'ritual_ZNK25QQuick3DPerspectiveCamera7clipFarEv',
    )

  def fieldOfView(self) -> float:
    """
    Calls Qt's 'float QQuick3DPerspectiveCamera::fieldOfView() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dperspectivecamera.html#fieldOfView
    """
    #  float QQuick3DPerspectiveCamera::fieldOfView() const
    return self.uglySide.call(
        'ritual_ZNK25QQuick3DPerspectiveCamera11fieldOfViewEv',
    )

  def fieldOfViewOrientation(self) -> FieldOfViewOrientation:
    """
    Calls Qt's 'FieldOfViewOrientation
    QQuick3DPerspectiveCamera::fieldOfViewOrientation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dperspectivecamera.html

    Returns
    -------

    FieldOfViewOrientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'FieldOfViewOrientation(number)' gives.
    """
    #  FieldOfViewOrientation
    #      QQuick3DPerspectiveCamera::fieldOfViewOrientation() const
    return QQuick3DPerspectiveCamera.FieldOfViewOrientation(
        self.uglySide.call(
            'ritual_ZNK25QQuick3DPerspectiveCamera22fieldOfViewOrientationE'
            'v',
        ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setClipNear(self, clipNear: float) -> None:
    """
    Calls Qt's 'void QQuick3DPerspectiveCamera::setClipNear(float clipNear)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dperspectivecamera.html#setClipNear

    Parameters
    ----------

    clipNear : float
      Passed on as it is.
    """
    #  void QQuick3DPerspectiveCamera::setClipNear(float clipNear)
    self.uglySide.call(
        'ritual_ZN25QQuick3DPerspectiveCamera11setClipNearEf', clipNear,
    )

  @overload(float)
  def setClipFar(self, clipFar: float) -> None:
    """
    Calls Qt's 'void QQuick3DPerspectiveCamera::setClipFar(float clipFar)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dperspectivecamera.html#setClipFar

    Parameters
    ----------

    clipFar : float
      Passed on as it is.
    """
    #  void QQuick3DPerspectiveCamera::setClipFar(float clipFar)
    self.uglySide.call(
        'ritual_ZN25QQuick3DPerspectiveCamera10setClipFarEf', clipFar,
    )

  @overload(float)
  def setFieldOfView(self, fieldOfView: float) -> None:
    """
    Calls Qt's 'void QQuick3DPerspectiveCamera::setFieldOfView(float
    fieldOfView)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dperspectivecamera.html#setFieldOfView

    Parameters
    ----------

    fieldOfView : float
      Passed on as it is.
    """
    #  void QQuick3DPerspectiveCamera::setFieldOfView(float fieldOfView)
    self.uglySide.call(
        'ritual_ZN25QQuick3DPerspectiveCamera14setFieldOfViewEf',
        fieldOfView,
    )

  @overload(FieldOfViewOrientation)
  def setFieldOfViewOrientation(
      self,
      fieldOfViewOrientation: FieldOfViewOrientation,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DPerspectiveCamera::setFieldOfViewOrientation(
    QQuick3DPerspectiveCamera::FieldOfViewOrientation
    fieldOfViewOrientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dperspectivecamera.html

    Parameters
    ----------

    fieldOfViewOrientation : FieldOfViewOrientation
      Passed on as its number.
    """
    #  void QQuick3DPerspectiveCamera::setFieldOfViewOrientation(
    #      QQuick3DPerspectiveCamera::FieldOfViewOrientation
    #      fieldOfViewOrientation)
    self.uglySide.call(
        'ritual_ZN25QQuick3DPerspectiveCamera25setFieldOfViewOrientationENS'
        '_22FieldOfViewOrientationE',
        fieldOfViewOrientation.value,
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
    'QQuick3DPerspectiveCamera::QQuick3DPerspectiveCamera(QQuick3DNode
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dperspectivecamera.html

    Parameters
    ----------

    parent : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DPerspectiveCamera::QQuick3DPerspectiveCamera(QQuick3DNode
    #      *parent)
    self._noteCreation(QQuick3DPerspectiveCamera, lambda: Rituals.call(
        'ritual_ZN25QQuick3DPerspectiveCameraC1EP12QQuick3DNode',
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

  def clipNearChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DPerspectiveCamera::clipNearChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dperspectivecamera.html#clipNearChanged
    """
    #  void QQuick3DPerspectiveCamera::clipNearChanged()
    self.uglySide.call(
        'ritual_ZN25QQuick3DPerspectiveCamera15clipNearChangedEv',
    )

  def clipFarChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DPerspectiveCamera::clipFarChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dperspectivecamera.html#clipFarChanged
    """
    #  void QQuick3DPerspectiveCamera::clipFarChanged()
    self.uglySide.call(
        'ritual_ZN25QQuick3DPerspectiveCamera14clipFarChangedEv',
    )

  def fieldOfViewChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DPerspectiveCamera::fieldOfViewChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dperspectivecamera.html#fieldOfViewChanged
    """
    #  void QQuick3DPerspectiveCamera::fieldOfViewChanged()
    self.uglySide.call(
        'ritual_ZN25QQuick3DPerspectiveCamera18fieldOfViewChangedEv',
    )

  def fieldOfViewOrientationChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DPerspectiveCamera::fieldOfViewOrientationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dperspectivecamera.html
    """
    #  void QQuick3DPerspectiveCamera::fieldOfViewOrientationChanged()
    self.uglySide.call(
        'ritual_ZN25QQuick3DPerspectiveCamera29fieldOfViewOrientationChange'
        'dEv',
    )

  @overload(QSSGRenderGraphObject)
  @overload(NoneType)
  def updateSpatialNode(
      self,
      node: Optional[QSSGRenderGraphObject],
  ) -> Optional[QSSGRenderGraphObject]:
    """
    Calls Qt's 'QSSGRenderGraphObject
    *QQuick3DPerspectiveCamera::updateSpatialNode(QSSGRenderGraphObject
    *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dperspectivecamera.html#updateSpatialNode

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
    #  QSSGRenderGraphObject *QQuick3DPerspectiveCamera::updateSpatialNode(
    #      QSSGRenderGraphObject *node)
    ritual = (
        'ritual_ZN25QQuick3DPerspectiveCamera17updateSpatialNodeEP21QSSGRen'
        'derGraphObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QQuick3DPerspectiveCamera17updateSpatialNodeEP21Q'
          'SSGRenderGraphObject')
    address = self.uglySide.call(ritual, self._addressOf(node))
    from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
    return QSSGRenderGraphObject._cuteAt(address)
