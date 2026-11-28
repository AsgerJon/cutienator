"""
Qt3DRender::Render::Transform binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/transform_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DRender::Render::Transform to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QMatrix4x4, QQuaternion, QVector3D

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Transform(Qt3DRender.Render.BackendNode):
  """
  The cute side of Qt's Qt3DRender::Render::Transform: a plain Python object
  standing in front of one C++ Qt3DRender::Render::Transform.

  It is built on the cute 'Qt3DRender::Render::BackendNode', as Qt's
  Qt3DRender::Render::Transform is built on Qt's
  Qt3DRender::Render::BackendNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::Transform that has a ritual and
  that Python can call so far, 9 names in all: 'cleanup', 'transformMatrix',
  'hasViewMatrix', 'viewMatrix', 'scale', 'rotation', 'translation',
  'syncFromFrontEnd', 'updateMatrix'. It can be made from Python, in 1 way;
  see '__init__'.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::Transform is created at the first use, not by
    'Qt3DRender::Render::Transform(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::Transform.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::Transform'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def transformMatrix(self) -> QMatrix4x4:
    """
    Calls Qt's 'Matrix4x4 Qt3DRender::Render::Transform::transformMatrix()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-transform.html#transformMatrix

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  Matrix4x4 Qt3DRender::Render::Transform::transformMatrix() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render9Transform15transformMatrixEv',
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  def hasViewMatrix(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Render::Transform::hasViewMatrix() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-transform.html#hasViewMatrix
    """
    #  bool Qt3DRender::Render::Transform::hasViewMatrix() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render9Transform13hasViewMatrixEv',
    )

  def viewMatrix(self) -> QMatrix4x4:
    """
    Calls Qt's 'const Matrix4x4 &Qt3DRender::Render::Transform::viewMatrix()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-transform.html#viewMatrix

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  const Matrix4x4 &Qt3DRender::Render::Transform::viewMatrix() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render9Transform10viewMatrixEv',
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  def scale(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D Qt3DRender::Render::Transform::scale() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-transform.html#scale

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Qt3DRender::Render::Transform::scale() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render9Transform5scaleEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def rotation(self) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion Qt3DRender::Render::Transform::rotation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-transform.html#rotation

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion Qt3DRender::Render::Transform::rotation() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render9Transform8rotationEv',
    )
    from ..QtGui import QQuaternion
    return QQuaternion._cuteOwning(address)

  def translation(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D Qt3DRender::Render::Transform::translation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-transform.html#translation

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Qt3DRender::Render::Transform::translation() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render9Transform11translationEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::Render::Transform::Transform()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-transform.html#Transform
    """
    #  Qt3DRender::Render::Transform::Transform()
    self._noteCreation(Transform, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render9TransformC1Ev',
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

  def cleanup(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Transform::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-transform.html#cleanup
    """
    #  void Qt3DRender::Render::Transform::cleanup()
    self.uglySide.call('ritual_ZN10Qt3DRender6Render9Transform7cleanupEv')

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Transform::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-transform.html#syncFromFrontEnd

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Render::Transform::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render9Transform16syncFromFrontEndEPKN8Qt3DC'
        'ore5QNodeEb',
        self._addressOf(frontEnd), firstTime,
    )

  def updateMatrix(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Transform::updateMatrix()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-transform.html#updateMatrix
    """
    #  void Qt3DRender::Render::Transform::updateMatrix()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render9Transform12updateMatrixEv',
    )
