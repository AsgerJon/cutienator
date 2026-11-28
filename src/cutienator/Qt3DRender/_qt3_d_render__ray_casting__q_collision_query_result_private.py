"""
Qt3DRender::RayCasting::QCollisionQueryResultPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qcollisionqueryresult_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::RayCasting::QCollisionQueryResultPrivate to be
#  private: it declares the class in a header it calls private. cutienator
#  does not care. Qt hands objects of the class out all the same, and a class
#  we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QSharedData
from ..Qt3DCore import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtGui import QVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVector3D = WAIT['QVector3D']


class QCollisionQueryResultPrivate(QSharedData):
  """
  The cute side of Qt's Qt3DRender::RayCasting::QCollisionQueryResultPrivate:
  a plain Python object standing in front of one C++
  Qt3DRender::RayCasting::QCollisionQueryResultPrivate.

  It is built on the cute 'QSharedData', as Qt's
  Qt3DRender::RayCasting::QCollisionQueryResultPrivate is built on Qt's
  QSharedData, and has everything that class has.

  C++ hands a Qt3DRender::RayCasting::QCollisionQueryResultPrivate around as
  a copy, so every C++ Qt3DRender::RayCasting::QCollisionQueryResultPrivate
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's Qt3DRender::RayCasting::QCollisionQueryResultPrivate
  that has a ritual and that Python can call so far, 2 names in all:
  'setHandle', 'addEntityHit'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::RayCasting::QCollisionQueryResultPrivate::
    ~QCollisionQueryResultPrivate()': the destructor: Python removes its C++
    Qt3DRender::RayCasting::QCollisionQueryResultPrivate by it, and has no
    other use for it.

  What to expect
  --------------

  - The C++ Qt3DRender::RayCasting::QCollisionQueryResultPrivate is created
    at the first use, not by
    'Qt3DRender::RayCasting::QCollisionQueryResultPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DRender::RayCasting::QCollisionQueryResultPrivate
    back gives a copy the ritual made for Python, in a new cute
    Qt3DRender::RayCasting::QCollisionQueryResultPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::RayCasting::QCollisionQueryResultPrivate'

  #  Qt's '~Qt3DRender::RayCasting::QCollisionQueryResultPrivate()'. Naming
  #  it makes this a value class: Python owns every C++
  #  Qt3DRender::RayCasting::QCollisionQueryResultPrivate behind a cute one,
  #  and removes it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN10Qt3DRender10RayCasting28QCollisionQueryResultPrivateD1Ev')

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

  @overload(int)
  def setHandle(self, handle: int) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::RayCasting::QCollisionQueryResultPrivate::setHandle(const
    QQueryHandle &handle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-raycasting-qcollisionqueryresultprivate.html

    Parameters
    ----------

    handle : int
      Passed on as it is.
    """
    #  void Qt3DRender::RayCasting::QCollisionQueryResultPrivate::setHandle(
    #      const QQueryHandle &handle)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10RayCasting28QCollisionQueryResultPrivate9se'
        'tHandleERKi',
        handle,
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::RayCasting::QCollisionQueryResultPrivate::
    QCollisionQueryResultPrivate()', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-raycasting-qcollisionqueryresultprivate.html
    """
    #  Qt3DRender::RayCasting::QCollisionQueryResultPrivate::
    #      QCollisionQueryResultPrivate()
    self._noteCreation(QCollisionQueryResultPrivate, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender10RayCasting28QCollisionQueryResultPrivateC1E'
        'v',
    ))

  @overload(THIS)
  def __init__(self, copy: QCollisionQueryResultPrivate) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::RayCasting::QCollisionQueryResultPrivate::
    QCollisionQueryResultPrivate(const QCollisionQueryResultPrivate &copy)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-raycasting-qcollisionqueryresultprivate.html

    Parameters
    ----------

    copy : QCollisionQueryResultPrivate
      Passed on as a value: Qt reads the C++
      Qt3DRender::RayCasting::QCollisionQueryResultPrivate, which stays
      Python's own.
    """
    #  Qt3DRender::RayCasting::QCollisionQueryResultPrivate::
    #      QCollisionQueryResultPrivate(const QCollisionQueryResultPrivate
    #      &copy)
    self._noteCreation(QCollisionQueryResultPrivate, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender10RayCasting28QCollisionQueryResultPrivateC1E'
        'RKS1_',
        self._valueOf(copy),
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

  @overload(WAIT['Qt3DCore.QNodeId'], QVector3D, float, QVector3D)
  def addEntityHit(
      self,
      entity: Qt3DCore.QNodeId,
      intersection: QVector3D,
      distance: float,
      uvw: QVector3D,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::RayCasting::QCollisionQueryResultPrivate::addEntityHit(
    Qt3DCore::QNodeId entity, const Vector3D &intersection, float distance,
    const Vector3D &uvw)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-raycasting-qcollisionqueryresultprivate.html

    Parameters
    ----------

    entity : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.

    intersection : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    distance : float
      Passed on as it is.

    uvw : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DRender::RayCasting::QCollisionQueryResultPrivate::
    #      addEntityHit(Qt3DCore::QNodeId entity, const Vector3D
    #      &intersection, float distance, const Vector3D &uvw)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10RayCasting28QCollisionQueryResultPrivate12a'
        'ddEntityHitEN8Qt3DCore7QNodeIdERK9QVector3DfS6_',
        self._valueOf(entity), self._valueOf(intersection), distance,
        self._valueOf(uvw),
    )
