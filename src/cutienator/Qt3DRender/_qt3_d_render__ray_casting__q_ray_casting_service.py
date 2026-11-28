"""
Qt3DRender::RayCasting::QRayCastingService binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qraycastingservice_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::RayCasting::QRayCastingService to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRayCastingService(Qt3DRender.RayCasting.QAbstractCollisionQueryService):
  """
  The cute side of Qt's Qt3DRender::RayCasting::QRayCastingService: a plain
  Python object standing in front of one C++
  Qt3DRender::RayCasting::QRayCastingService.

  It is built on the cute
  'Qt3DRender::RayCasting::QAbstractCollisionQueryService', as Qt's
  Qt3DRender::RayCasting::QRayCastingService is built on Qt's
  Qt3DRender::RayCasting::QAbstractCollisionQueryService, and has everything
  that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::RayCasting::QRayCastingService that has
  a ritual and that Python can call so far, 3 names in all: 'query',
  'fetchResult', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QList<QCollisionQueryResult>
    Qt3DRender::RayCasting::QRayCastingService::fetchAllResults() const':
    gives a type Python has no way to take yet.
  - Qt's 'Qt3DRender::RayCasting::QRayCastingService::QRayCastingService(
    QRayCastingServicePrivate &dd)': takes a type Python has no way to hand
    over yet.
  - Qt's 'const QRayCastingServicePrivate
    *Qt3DRender::RayCasting::QRayCastingService::d_func() const': takes in
    Python what 'QRayCastingServicePrivate
    *Qt3DRender::RayCasting::QRayCastingService::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 10 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ Qt3DRender::RayCasting::QRayCastingService is created at the
    first use, not by 'Qt3DRender::RayCasting::QRayCastingService(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::RayCasting::QRayCastingService.
  - Qt tells when it has removed the C++
    Qt3DRender::RayCasting::QRayCastingService. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::RayCasting::QRayCastingService'

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
    'Qt3DRender::RayCasting::QRayCastingService::QRayCastingService()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-raycasting-qraycastingservice.html
    """
    #  Qt3DRender::RayCasting::QRayCastingService::QRayCastingService()
    self._noteCreation(QRayCastingService, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender10RayCasting18QRayCastingServiceC1Ev',
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

  @overload(
      WAIT['Qt3DRender.RayCasting.QRay3D'],
      Qt3DRender.RayCasting.QAbstractCollisionQueryService.QueryMode,
      WAIT['Qt3DRender.RayCasting.QBoundingVolumeProvider'],
  )
  @overload(
      WAIT['Qt3DRender.RayCasting.QRay3D'],
      Qt3DRender.RayCasting.QAbstractCollisionQueryService.QueryMode,
      NoneType,
  )
  def query(
      self,
      ray: Qt3DRender.RayCasting.QRay3D,
      mode: Qt3DRender.RayCasting.QAbstractCollisionQueryService.QueryMode,
      provider: Optional[Qt3DRender.RayCasting.QBoundingVolumeProvider],
  ) -> int:
    """
    Calls Qt's 'QQueryHandle
    Qt3DRender::RayCasting::QRayCastingService::query(const QRay3D &ray,
    QueryMode mode, QBoundingVolumeProvider *provider)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-raycasting-qraycastingservice.html

    Parameters
    ----------

    ray : Qt3DRender.RayCasting.QRay3D
      Passed on as a value: Qt reads the C++ Qt3DRender::RayCasting::QRay3D,
      which stays Python's own.

    mode : Qt3DRender.RayCasting.QAbstractCollisionQueryService.QueryMode
      Passed on as its number.

    provider : Optional[Qt3DRender.RayCasting.QBoundingVolumeProvider]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQueryHandle Qt3DRender::RayCasting::QRayCastingService::query(const
    #      QRay3D &ray, QueryMode mode, QBoundingVolumeProvider *provider)
    ritual = (
        'ritual_ZN10Qt3DRender10RayCasting18QRayCastingService5queryERKNS0_'
        '6QRay3DENS0_30QAbstractCollisionQueryService9QueryModeEPNS0_23QBou'
        'ndingVolumeProviderE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender10RayCasting18QRayCastingService5queryE'
          'RKNS0_6QRay3DENS0_30QAbstractCollisionQueryService9QueryModeEPNS'
          '0_23QBoundingVolumeProviderE')
    return self.uglySide.call(
        ritual, self._valueOf(ray), mode.value, self._addressOf(provider),
    )

  @overload(
      WAIT['Qt3DRender.RayCasting.QRay3D'],
      WAIT['Qt3DRender.RayCasting.QBoundingVolume'],
  )
  @overload(WAIT['Qt3DRender.RayCasting.QRay3D'], NoneType)
  def query(
      self,
      ray: Qt3DRender.RayCasting.QRay3D,
      volume: Optional[Qt3DRender.RayCasting.QBoundingVolume],
  ) -> Qt3DRender.RayCasting.QCollisionQueryResult.Hit:
    """
    Calls Qt's 'QCollisionQueryResult::Hit
    Qt3DRender::RayCasting::QRayCastingService::query(const QRay3D &ray,
    const QBoundingVolume *volume)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-raycasting-qraycastingservice.html

    Parameters
    ----------

    ray : Qt3DRender.RayCasting.QRay3D
      Passed on as a value: Qt reads the C++ Qt3DRender::RayCasting::QRay3D,
      which stays Python's own.

    volume : Optional[Qt3DRender.RayCasting.QBoundingVolume]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Qt3DRender.RayCasting.QCollisionQueryResult.Hit
      A new cute Qt3DRender::RayCasting::QCollisionQueryResult::Hit around
      the copy Qt gave back. Python owns it.
    """
    #  QCollisionQueryResult::Hit
    #      Qt3DRender::RayCasting::QRayCastingService::query(const QRay3D
    #      &ray, const QBoundingVolume *volume)
    ritual = (
        'ritual_ZN10Qt3DRender10RayCasting18QRayCastingService5queryERKNS0_'
        '6QRay3DEPKNS0_15QBoundingVolumeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender10RayCasting18QRayCastingService5queryE'
          'RKNS0_6QRay3DEPKNS0_15QBoundingVolumeE')
    address = self.uglySide.call(
        ritual, self._valueOf(ray), self._addressOf(volume),
    )
    return Qt3DRender.RayCasting.QCollisionQueryResult.Hit._cuteOwning(address)

  @overload(int)
  def fetchResult(
      self,
      handle: int,
  ) -> Qt3DRender.RayCasting.QCollisionQueryResult:
    """
    Calls Qt's 'QCollisionQueryResult
    Qt3DRender::RayCasting::QRayCastingService::fetchResult(const
    QQueryHandle &handle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-raycasting-qraycastingservice.html

    Parameters
    ----------

    handle : int
      Passed on as it is.

    Returns
    -------

    Qt3DRender.RayCasting.QCollisionQueryResult
      A new cute Qt3DRender::RayCasting::QCollisionQueryResult around the
      copy Qt gave back. Python owns it.
    """
    #  QCollisionQueryResult
    #      Qt3DRender::RayCasting::QRayCastingService::fetchResult(const
    #      QQueryHandle &handle)
    ritual = (
        'ritual_ZN10Qt3DRender10RayCasting18QRayCastingService11fetchResult'
        'ERKi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender10RayCasting18QRayCastingService11fetch'
          'ResultERKi')
    address = self.uglySide.call(ritual, handle)
    return Qt3DRender.RayCasting.QCollisionQueryResult._cuteOwning(address)

  def d_func(
      self,
  ) -> Optional[Qt3DRender.RayCasting.QRayCastingServicePrivate]:
    """
    Calls Qt's 'QRayCastingServicePrivate
    *Qt3DRender::RayCasting::QRayCastingService::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-raycasting-qraycastingservice.html

    Returns
    -------

    Optional[Qt3DRender.RayCasting.QRayCastingServicePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRayCastingServicePrivate
    #      *Qt3DRender::RayCasting::QRayCastingService::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender10RayCasting18QRayCastingService6d_funcEv',
    )
    return Qt3DRender.RayCasting.QRayCastingServicePrivate._cuteAt(address)
