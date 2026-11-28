"""
Qt3DRender::QCameraLensPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qcameralens_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DRender::QCameraLensPrivate to be private: it declares the
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

  from ..QtGui import QVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVector3D = WAIT['QVector3D']


class QCameraLensPrivate(Qt3DCore.QComponentPrivate):
  """
  The cute side of Qt's Qt3DRender::QCameraLensPrivate: a plain Python object
  standing in front of one C++ Qt3DRender::QCameraLensPrivate.

  It is built on the cute 'Qt3DCore::QComponentPrivate', as Qt's
  Qt3DRender::QCameraLensPrivate is built on Qt's
  Qt3DCore::QComponentPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QCameraLensPrivate that has a ritual and
  that Python can call so far, 6 names in all: 'updateProjectionMatrix',
  'q_func', 'processViewAllResult', 'updatePerpectiveProjection',
  'updateOrthographicProjection', 'updateFrustumProjection'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QCameraLens *Qt3DRender::QCameraLensPrivate::q_func() const':
    takes in Python what 'QCameraLens
    *Qt3DRender::QCameraLensPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ Qt3DRender::QCameraLensPrivate is created at the first use, not
    by 'Qt3DRender::QCameraLensPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QCameraLensPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QCameraLensPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    'Qt3DRender::QCameraLensPrivate::QCameraLensPrivate()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcameralensprivate.html
    """
    #  Qt3DRender::QCameraLensPrivate::QCameraLensPrivate()
    self._noteCreation(QCameraLensPrivate, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender18QCameraLensPrivateC1Ev',
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

  def updateProjectionMatrix(self) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QCameraLensPrivate::updateProjectionMatrix()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcameralensprivate.html
    """
    #  void Qt3DRender::QCameraLensPrivate::updateProjectionMatrix()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender18QCameraLensPrivate22updateProjectionMatrixE'
        'v',
    )

  def q_func(self) -> Optional[Qt3DRender.QCameraLens]:
    """
    Calls Qt's 'QCameraLens *Qt3DRender::QCameraLensPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcameralensprivate.html#q_func

    Returns
    -------

    Optional[Qt3DRender.QCameraLens]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCameraLens *Qt3DRender::QCameraLensPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender18QCameraLensPrivate6q_funcEv',
    )
    return Qt3DRender.QCameraLens._cuteAt(address)

  @overload(WAIT['Qt3DCore.QNodeId'], QVector3D, float)
  def processViewAllResult(
      self,
      requestId: Qt3DCore.QNodeId,
      center: QVector3D,
      radius: float,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QCameraLensPrivate::processViewAllResult(Qt3DCore::QNodeId
    requestId, const QVector3D &center, float radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcameralensprivate.html

    Parameters
    ----------

    requestId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.

    center : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    radius : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCameraLensPrivate::processViewAllResult(Qt3DCore::
    #      QNodeId requestId, const QVector3D &center, float radius)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender18QCameraLensPrivate20processViewAllResultEN8'
        'Qt3DCore7QNodeIdERK9QVector3Df',
        self._valueOf(requestId), self._valueOf(center), radius,
    )

  def updatePerpectiveProjection(self) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QCameraLensPrivate::updatePerpectiveProjection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcameralensprivate.html
    """
    #  void Qt3DRender::QCameraLensPrivate::updatePerpectiveProjection()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender18QCameraLensPrivate26updatePerpectiveProject'
        'ionEv',
    )

  def updateOrthographicProjection(self) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QCameraLensPrivate::updateOrthographicProjection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcameralensprivate.html
    """
    #  void Qt3DRender::QCameraLensPrivate::updateOrthographicProjection()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender18QCameraLensPrivate28updateOrthographicProje'
        'ctionEv',
    )

  def updateFrustumProjection(self) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QCameraLensPrivate::updateFrustumProjection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcameralensprivate.html
    """
    #  void Qt3DRender::QCameraLensPrivate::updateFrustumProjection()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender18QCameraLensPrivate23updateFrustumProjection'
        'Ev',
    )
