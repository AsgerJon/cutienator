"""
QQuick3DFrustumCamera binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dfrustumcamera_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DFrustumCamera to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QQuick3DNode, QQuick3DPerspectiveCamera

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


class QQuick3DFrustumCamera(QQuick3DPerspectiveCamera):
  """
  The cute side of Qt's QQuick3DFrustumCamera: a plain Python object standing
  in front of one C++ QQuick3DFrustumCamera.

  It is built on the cute 'QQuick3DPerspectiveCamera', as Qt's
  QQuick3DFrustumCamera is built on Qt's QQuick3DPerspectiveCamera, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DFrustumCamera that has a ritual and that
  Python can call so far, 15 names in all: 'metaObject', 'tr', 'top',
  'bottom', 'right', 'left', 'setTop', 'setBottom', 'setRight', 'setLeft',
  'topChanged', 'bottomChanged', 'rightChanged', 'leftChanged',
  'updateSpatialNode'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DFrustumCamera::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuick3DFrustumCamera::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 20 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DFrustumCamera is created at the first use, not by
    'QQuick3DFrustumCamera(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DFrustumCamera.
  - Qt tells when it has removed the C++ QQuick3DFrustumCamera. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuick3DFrustumCamera::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dfrustumcamera.html#tr

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
    #  QString QQuick3DFrustumCamera::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QQuick3DFrustumCamera2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DFrustumCamera'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DFrustumCamera::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dfrustumcamera.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DFrustumCamera::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuick3DFrustumCamera10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def top(self) -> float:
    """
    Calls Qt's 'float QQuick3DFrustumCamera::top() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dfrustumcamera.html#top
    """
    #  float QQuick3DFrustumCamera::top() const
    return self.uglySide.call('ritual_ZNK21QQuick3DFrustumCamera3topEv')

  def bottom(self) -> float:
    """
    Calls Qt's 'float QQuick3DFrustumCamera::bottom() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dfrustumcamera.html#bottom
    """
    #  float QQuick3DFrustumCamera::bottom() const
    return self.uglySide.call('ritual_ZNK21QQuick3DFrustumCamera6bottomEv')

  def right(self) -> float:
    """
    Calls Qt's 'float QQuick3DFrustumCamera::right() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dfrustumcamera.html#right
    """
    #  float QQuick3DFrustumCamera::right() const
    return self.uglySide.call('ritual_ZNK21QQuick3DFrustumCamera5rightEv')

  def left(self) -> float:
    """
    Calls Qt's 'float QQuick3DFrustumCamera::left() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dfrustumcamera.html#left
    """
    #  float QQuick3DFrustumCamera::left() const
    return self.uglySide.call('ritual_ZNK21QQuick3DFrustumCamera4leftEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setTop(self, top: float) -> None:
    """
    Calls Qt's 'void QQuick3DFrustumCamera::setTop(float top)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dfrustumcamera.html#setTop

    Parameters
    ----------

    top : float
      Passed on as it is.
    """
    #  void QQuick3DFrustumCamera::setTop(float top)
    self.uglySide.call('ritual_ZN21QQuick3DFrustumCamera6setTopEf', top)

  @overload(float)
  def setBottom(self, bottom: float) -> None:
    """
    Calls Qt's 'void QQuick3DFrustumCamera::setBottom(float bottom)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dfrustumcamera.html#setBottom

    Parameters
    ----------

    bottom : float
      Passed on as it is.
    """
    #  void QQuick3DFrustumCamera::setBottom(float bottom)
    self.uglySide.call(
        'ritual_ZN21QQuick3DFrustumCamera9setBottomEf', bottom,
    )

  @overload(float)
  def setRight(self, right: float) -> None:
    """
    Calls Qt's 'void QQuick3DFrustumCamera::setRight(float right)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dfrustumcamera.html#setRight

    Parameters
    ----------

    right : float
      Passed on as it is.
    """
    #  void QQuick3DFrustumCamera::setRight(float right)
    self.uglySide.call('ritual_ZN21QQuick3DFrustumCamera8setRightEf', right)

  @overload(float)
  def setLeft(self, left: float) -> None:
    """
    Calls Qt's 'void QQuick3DFrustumCamera::setLeft(float left)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dfrustumcamera.html#setLeft

    Parameters
    ----------

    left : float
      Passed on as it is.
    """
    #  void QQuick3DFrustumCamera::setLeft(float left)
    self.uglySide.call('ritual_ZN21QQuick3DFrustumCamera7setLeftEf', left)

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
    'QQuick3DFrustumCamera::QQuick3DFrustumCamera(QQuick3DNode *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dfrustumcamera.html#QQuick3DFrustumCamera

    Parameters
    ----------

    parent : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DFrustumCamera::QQuick3DFrustumCamera(QQuick3DNode *parent)
    self._noteCreation(QQuick3DFrustumCamera, lambda: Rituals.call(
        'ritual_ZN21QQuick3DFrustumCameraC1EP12QQuick3DNode',
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

  def topChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DFrustumCamera::topChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dfrustumcamera.html#topChanged
    """
    #  void QQuick3DFrustumCamera::topChanged()
    self.uglySide.call('ritual_ZN21QQuick3DFrustumCamera10topChangedEv')

  def bottomChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DFrustumCamera::bottomChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dfrustumcamera.html#bottomChanged
    """
    #  void QQuick3DFrustumCamera::bottomChanged()
    self.uglySide.call('ritual_ZN21QQuick3DFrustumCamera13bottomChangedEv')

  def rightChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DFrustumCamera::rightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dfrustumcamera.html#rightChanged
    """
    #  void QQuick3DFrustumCamera::rightChanged()
    self.uglySide.call('ritual_ZN21QQuick3DFrustumCamera12rightChangedEv')

  def leftChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DFrustumCamera::leftChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dfrustumcamera.html#leftChanged
    """
    #  void QQuick3DFrustumCamera::leftChanged()
    self.uglySide.call('ritual_ZN21QQuick3DFrustumCamera11leftChangedEv')

  @overload(QSSGRenderGraphObject)
  @overload(NoneType)
  def updateSpatialNode(
      self,
      node: Optional[QSSGRenderGraphObject],
  ) -> Optional[QSSGRenderGraphObject]:
    """
    Calls Qt's 'QSSGRenderGraphObject
    *QQuick3DFrustumCamera::updateSpatialNode(QSSGRenderGraphObject *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dfrustumcamera.html#updateSpatialNode

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
    #      *QQuick3DFrustumCamera::updateSpatialNode(QSSGRenderGraphObject
    #      *node)
    ritual = (
        'ritual_ZN21QQuick3DFrustumCamera17updateSpatialNodeEP21QSSGRenderG'
        'raphObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuick3DFrustumCamera17updateSpatialNodeEP21QSSGR'
          'enderGraphObject')
    address = self.uglySide.call(ritual, self._addressOf(node))
    from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
    return QSSGRenderGraphObject._cuteAt(address)
