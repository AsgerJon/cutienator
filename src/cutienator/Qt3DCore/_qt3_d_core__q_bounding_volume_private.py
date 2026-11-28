"""
Qt3DCore::QBoundingVolumePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/6.12.0/Qt3DCore/private/qboundingvolume_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DCore::QBoundingVolumePrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBoundingVolumePrivate(Qt3DCore.QComponentPrivate):
  """
  The cute side of Qt's Qt3DCore::QBoundingVolumePrivate: a plain Python
  object standing in front of one C++ Qt3DCore::QBoundingVolumePrivate.

  It is built on the cute 'Qt3DCore::QComponentPrivate', as Qt's
  Qt3DCore::QBoundingVolumePrivate is built on Qt's
  Qt3DCore::QComponentPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QBoundingVolumePrivate that has a ritual
  and that Python can call so far, 4 names in all: 'q_func',
  'setImplicitBounds', 'setView', 'get'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QBoundingVolume *Qt3DCore::QBoundingVolumePrivate::q_func()
    const': takes in Python what 'QBoundingVolume
    *Qt3DCore::QBoundingVolumePrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ Qt3DCore::QBoundingVolumePrivate is created at the first use, not
    by 'Qt3DCore::QBoundingVolumePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QBoundingVolumePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['Qt3DCore.QBoundingVolume'])
  @overload(NoneType)
  def get(
      q: Optional[Qt3DCore.QBoundingVolume],
  ) -> Optional[QBoundingVolumePrivate]:
    """
    Calls Qt's 'QBoundingVolumePrivate
    *Qt3DCore::QBoundingVolumePrivate::get(QBoundingVolume *q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qboundingvolumeprivate.html#get

    Parameters
    ----------

    q : Optional[Qt3DCore.QBoundingVolume]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QBoundingVolumePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBoundingVolumePrivate
    #      *Qt3DCore::QBoundingVolumePrivate::get(QBoundingVolume *q)
    address = Rituals.call(
        'ritual_ZN8Qt3DCore22QBoundingVolumePrivate3getEPNS_15QBoundingVolu'
        'meE',
        CuteMixin._addressOf(q),
    )
    return QBoundingVolumePrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QBoundingVolumePrivate'

  #  A C++ Qt3DCore::QBoundingVolumePrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_QBoundingVolumePrivate'

  #  The functions Qt calls itself that Qt3DCore::QBoundingVolumePrivate is
  #  the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'setView': (
          ('_ZN8Qt3DCore22QBoundingVolumePrivate7setViewEPNS_13QGeometryVie'
           'wE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'Qt3DCore:Qt3DCore.QGeometryView'),
           )),
      ),
  }

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

  @overload(QVector3D, QVector3D, QVector3D, float)
  def setImplicitBounds(
      self,
      minPoint: QVector3D,
      maxPoint: QVector3D,
      center: QVector3D,
      radius: float,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::QBoundingVolumePrivate::setImplicitBounds(const QVector3D
    &minPoint, const QVector3D &maxPoint, const QVector3D &center, float
    radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qboundingvolumeprivate.html

    Parameters
    ----------

    minPoint : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    maxPoint : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    center : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    radius : float
      Passed on as it is.
    """
    #  void Qt3DCore::QBoundingVolumePrivate::setImplicitBounds(const
    #      QVector3D &minPoint, const QVector3D &maxPoint, const QVector3D
    #      &center, float radius)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore22QBoundingVolumePrivate17setImplicitBoundsERK9Q'
        'Vector3DS3_S3_f',
        self._valueOf(minPoint), self._valueOf(maxPoint),
        self._valueOf(center), radius,
    )

  @overload(WAIT['Qt3DCore.QGeometryView'])
  @overload(NoneType)
  def setView(self, view: Optional[Qt3DCore.QGeometryView]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QBoundingVolumePrivate::setView(QGeometryView
    *view)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qboundingvolumeprivate.html#setView

    Parameters
    ----------

    view : Optional[Qt3DCore.QGeometryView]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QBoundingVolumePrivate::setView(QGeometryView *view)
    ritual = (
        'ritual_ZN8Qt3DCore22QBoundingVolumePrivate7setViewEPNS_13QGeometry'
        'ViewE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN8Qt3DCore22QBoundingVolumePrivate7setViewEPNS_13QGe'
          'ometryViewE')
    self.uglySide.call(ritual, self._addressOf(view))

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
    'Qt3DCore::QBoundingVolumePrivate::QBoundingVolumePrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qboundingvolumeprivate.html
    """
    #  Qt3DCore::QBoundingVolumePrivate::QBoundingVolumePrivate()
    self._noteCreation(QBoundingVolumePrivate, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore22QBoundingVolumePrivateC1Ev',
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

  def q_func(self) -> Optional[Qt3DCore.QBoundingVolume]:
    """
    Calls Qt's 'QBoundingVolume *Qt3DCore::QBoundingVolumePrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qboundingvolumeprivate.html#q_func

    Returns
    -------

    Optional[Qt3DCore.QBoundingVolume]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBoundingVolume *Qt3DCore::QBoundingVolumePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN8Qt3DCore22QBoundingVolumePrivate6q_funcEv',
    )
    return Qt3DCore.QBoundingVolume._cuteAt(address)
