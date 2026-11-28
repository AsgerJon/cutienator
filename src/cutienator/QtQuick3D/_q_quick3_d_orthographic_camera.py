"""
QQuick3DOrthographicCamera binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dorthographiccamera_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DOrthographicCamera to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
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


class QQuick3DOrthographicCamera(QQuick3DCamera):
  """
  The cute side of Qt's QQuick3DOrthographicCamera: a plain Python object
  standing in front of one C++ QQuick3DOrthographicCamera.

  It is built on the cute 'QQuick3DCamera', as Qt's
  QQuick3DOrthographicCamera is built on Qt's QQuick3DCamera, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DOrthographicCamera that has a ritual and
  that Python can call so far, 15 names in all: 'metaObject', 'tr',
  'clipNear', 'clipFar', 'horizontalMagnification', 'verticalMagnification',
  'setClipNear', 'setClipFar', 'setHorizontalMagnification',
  'setVerticalMagnification', 'clipNearChanged', 'clipFarChanged',
  'horizontalMagnificationChanged', 'verticalMagnificationChanged',
  'updateSpatialNode'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DOrthographicCamera::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuick3DOrthographicCamera::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 20 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DOrthographicCamera is created at the first use, not by
    'QQuick3DOrthographicCamera(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DOrthographicCamera.
  - Qt tells when it has removed the C++ QQuick3DOrthographicCamera. Every
    call on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuick3DOrthographicCamera::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dorthographiccamera.html#tr

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
    #  QString QQuick3DOrthographicCamera::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN26QQuick3DOrthographicCamera2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DOrthographicCamera'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DOrthographicCamera::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dorthographiccamera.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DOrthographicCamera::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuick3DOrthographicCamera10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def clipNear(self) -> float:
    """
    Calls Qt's 'float QQuick3DOrthographicCamera::clipNear() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dorthographiccamera.html#clipNear
    """
    #  float QQuick3DOrthographicCamera::clipNear() const
    return self.uglySide.call(
        'ritual_ZNK26QQuick3DOrthographicCamera8clipNearEv',
    )

  def clipFar(self) -> float:
    """
    Calls Qt's 'float QQuick3DOrthographicCamera::clipFar() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dorthographiccamera.html#clipFar
    """
    #  float QQuick3DOrthographicCamera::clipFar() const
    return self.uglySide.call(
        'ritual_ZNK26QQuick3DOrthographicCamera7clipFarEv',
    )

  def horizontalMagnification(self) -> float:
    """
    Calls Qt's 'float QQuick3DOrthographicCamera::horizontalMagnification()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dorthographiccamera.html
    """
    #  float QQuick3DOrthographicCamera::horizontalMagnification() const
    return self.uglySide.call(
        'ritual_ZNK26QQuick3DOrthographicCamera23horizontalMagnificationEv',
    )

  def verticalMagnification(self) -> float:
    """
    Calls Qt's 'float QQuick3DOrthographicCamera::verticalMagnification()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dorthographiccamera.html
    """
    #  float QQuick3DOrthographicCamera::verticalMagnification() const
    return self.uglySide.call(
        'ritual_ZNK26QQuick3DOrthographicCamera21verticalMagnificationEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setClipNear(self, clipNear: float) -> None:
    """
    Calls Qt's 'void QQuick3DOrthographicCamera::setClipNear(float
    clipNear)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dorthographiccamera.html#setClipNear

    Parameters
    ----------

    clipNear : float
      Passed on as it is.
    """
    #  void QQuick3DOrthographicCamera::setClipNear(float clipNear)
    self.uglySide.call(
        'ritual_ZN26QQuick3DOrthographicCamera11setClipNearEf', clipNear,
    )

  @overload(float)
  def setClipFar(self, clipFar: float) -> None:
    """
    Calls Qt's 'void QQuick3DOrthographicCamera::setClipFar(float clipFar)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dorthographiccamera.html#setClipFar

    Parameters
    ----------

    clipFar : float
      Passed on as it is.
    """
    #  void QQuick3DOrthographicCamera::setClipFar(float clipFar)
    self.uglySide.call(
        'ritual_ZN26QQuick3DOrthographicCamera10setClipFarEf', clipFar,
    )

  @overload(float)
  def setHorizontalMagnification(
      self,
      horizontalMagnification: float,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DOrthographicCamera::setHorizontalMagnification(float
    horizontalMagnification)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dorthographiccamera.html

    Parameters
    ----------

    horizontalMagnification : float
      Passed on as it is.
    """
    #  void QQuick3DOrthographicCamera::setHorizontalMagnification(float
    #      horizontalMagnification)
    self.uglySide.call(
        'ritual_ZN26QQuick3DOrthographicCamera26setHorizontalMagnificationE'
        'f',
        horizontalMagnification,
    )

  @overload(float)
  def setVerticalMagnification(self, horizontalMagnification: float) -> None:
    """
    Calls Qt's 'void
    QQuick3DOrthographicCamera::setVerticalMagnification(float
    horizontalMagnification)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dorthographiccamera.html

    Parameters
    ----------

    horizontalMagnification : float
      Passed on as it is.
    """
    #  void QQuick3DOrthographicCamera::setVerticalMagnification(float
    #      horizontalMagnification)
    self.uglySide.call(
        'ritual_ZN26QQuick3DOrthographicCamera24setVerticalMagnificationEf',
        horizontalMagnification,
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
    'QQuick3DOrthographicCamera::QQuick3DOrthographicCamera(QQuick3DNode
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dorthographiccamera.html

    Parameters
    ----------

    parent : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DOrthographicCamera::QQuick3DOrthographicCamera(QQuick3DNode
    #      *parent)
    self._noteCreation(QQuick3DOrthographicCamera, lambda: Rituals.call(
        'ritual_ZN26QQuick3DOrthographicCameraC1EP12QQuick3DNode',
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
    Calls Qt's 'void QQuick3DOrthographicCamera::clipNearChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dorthographiccamera.html#clipNearChanged
    """
    #  void QQuick3DOrthographicCamera::clipNearChanged()
    self.uglySide.call(
        'ritual_ZN26QQuick3DOrthographicCamera15clipNearChangedEv',
    )

  def clipFarChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DOrthographicCamera::clipFarChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dorthographiccamera.html#clipFarChanged
    """
    #  void QQuick3DOrthographicCamera::clipFarChanged()
    self.uglySide.call(
        'ritual_ZN26QQuick3DOrthographicCamera14clipFarChangedEv',
    )

  def horizontalMagnificationChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DOrthographicCamera::horizontalMagnificationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dorthographiccamera.html
    """
    #  void QQuick3DOrthographicCamera::horizontalMagnificationChanged()
    self.uglySide.call(
        'ritual_ZN26QQuick3DOrthographicCamera30horizontalMagnificationChan'
        'gedEv',
    )

  def verticalMagnificationChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DOrthographicCamera::verticalMagnificationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dorthographiccamera.html
    """
    #  void QQuick3DOrthographicCamera::verticalMagnificationChanged()
    self.uglySide.call(
        'ritual_ZN26QQuick3DOrthographicCamera28verticalMagnificationChange'
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
    *QQuick3DOrthographicCamera::updateSpatialNode(QSSGRenderGraphObject
    *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dorthographiccamera.html#updateSpatialNode

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
    #  QSSGRenderGraphObject *QQuick3DOrthographicCamera::updateSpatialNode(
    #      QSSGRenderGraphObject *node)
    ritual = (
        'ritual_ZN26QQuick3DOrthographicCamera17updateSpatialNodeEP21QSSGRe'
        'nderGraphObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QQuick3DOrthographicCamera17updateSpatialNodeEP21'
          'QSSGRenderGraphObject')
    address = self.uglySide.call(ritual, self._addressOf(node))
    from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
    return QSSGRenderGraphObject._cuteAt(address)
