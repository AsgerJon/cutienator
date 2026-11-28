"""
Qt3DRender::RayCasting::QRayCastingServicePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qraycastingservice_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::RayCasting::QRayCastingServicePrivate to be private:
#  it declares the class in a header it calls private. cutienator does not
#  care. Qt hands objects of the class out all the same, and a class we are
#  handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional


class QRayCastingServicePrivate(Qt3DRender.RayCasting.QAbstractCollisionQueryServicePrivate):
  """
  The cute side of Qt's Qt3DRender::RayCasting::QRayCastingServicePrivate: a
  plain Python object standing in front of one C++
  Qt3DRender::RayCasting::QRayCastingServicePrivate.

  It is built on the cute
  'Qt3DRender::RayCasting::QAbstractCollisionQueryServicePrivate', as Qt's
  Qt3DRender::RayCasting::QRayCastingServicePrivate is built on Qt's
  Qt3DRender::RayCasting::QAbstractCollisionQueryServicePrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::RayCasting::QRayCastingServicePrivate
  that has a ritual and that Python can call so far, 1 name in all: 'q_func'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QRayCastingService
    *Qt3DRender::RayCasting::QRayCastingServicePrivate::q_func() const':
    takes in Python what 'QRayCastingService
    *Qt3DRender::RayCasting::QRayCastingServicePrivate::q_func()' takes.

  What has no ritual
  ------------------

  2 of the 5 functions Qt declares: 2 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ Qt3DRender::RayCasting::QRayCastingServicePrivate is created at
    the first use, not by
    'Qt3DRender::RayCasting::QRayCastingServicePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    Qt3DRender::RayCasting::QRayCastingServicePrivate.
  - Each name of Qt's Qt3DRender::RayCasting::QRayCastingServicePrivate that
    has no cute function yet, 'collides', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside
  #  Qt3DRender::RayCasting::QRayCastingServicePrivate, each a class in here
  #  as in C++.

  class Query(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's
    Qt3DRender::RayCasting::QRayCastingServicePrivate::Query: a plain Python
    object standing in front of one C++
    Qt3DRender::RayCasting::QRayCastingServicePrivate::Query.

    C++ hands a Qt3DRender::RayCasting::QRayCastingServicePrivate::Query
    around as a copy, so every C++
    Qt3DRender::RayCasting::QRayCastingServicePrivate::Query behind a cute
    one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's
    Qt3DRender::RayCasting::QRayCastingServicePrivate::Query yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'Qt3DRender::RayCasting::QRayCastingServicePrivate::Query::~Query()':
      the destructor: Python removes its C++
      Qt3DRender::RayCasting::QRayCastingServicePrivate::Query by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ Qt3DRender::RayCasting::QRayCastingServicePrivate::Query is
      created at the first use, not by
      'Qt3DRender::RayCasting::QRayCastingServicePrivate::Query(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a
      Qt3DRender::RayCasting::QRayCastingServicePrivate::Query back gives a
      copy the ritual made for Python, in a new cute
      Qt3DRender::RayCasting::QRayCastingServicePrivate::Query.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'Qt3DRender::RayCasting::QRayCastingServicePrivate::Query'

    #  Qt's '~Qt3DRender::RayCasting::QRayCastingServicePrivate::Query()'.
    #  Naming it makes this a value class: Python owns every C++
    #  Qt3DRender::RayCasting::QRayCastingServicePrivate::Query behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN10Qt3DRender10RayCasting25QRayCastingServicePrivate5QueryD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::RayCasting::QRayCastingServicePrivate'

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

  @overload(str)
  def __init__(self, description: str) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::RayCasting::QRayCastingServicePrivate::
    QRayCastingServicePrivate(const QString &description)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-raycasting-qraycastingserviceprivate.html

    Parameters
    ----------

    description : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  Qt3DRender::RayCasting::QRayCastingServicePrivate::
    #      QRayCastingServicePrivate(const QString &description)
    self._noteCreation(QRayCastingServicePrivate, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender10RayCasting25QRayCastingServicePrivateC1ERK7'
        'QString',
        description,
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

  def q_func(self) -> Optional[Qt3DRender.RayCasting.QRayCastingService]:
    """
    Calls Qt's 'QRayCastingService
    *Qt3DRender::RayCasting::QRayCastingServicePrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-raycasting-qraycastingserviceprivate.html

    Returns
    -------

    Optional[Qt3DRender.RayCasting.QRayCastingService]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRayCastingService
    #      *Qt3DRender::RayCasting::QRayCastingServicePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender10RayCasting25QRayCastingServicePrivate6q_fun'
        'cEv',
    )
    return Qt3DRender.RayCasting.QRayCastingService._cuteAt(address)

  @staticmethod
  def collides(*__, **_) -> Never:
    """
    - Qt's 'QCollisionQueryResult
      Qt3DRender::RayCasting::QRayCastingServicePrivate::collides(const
      QRay3D &ray, QBoundingVolumeProvider *provider,
      QAbstractCollisionQueryService::QueryMode mode, const QQueryHandle
      &handle)': Qt's library has no name for it, and its code in Qt's source
      does not compile apart from its file: no member named 'intersects' in
      'Qt3DRender::RayCasting::QCollisionQueryResult::Hit'.
    - Qt's 'QCollisionQueryResult::Hit
      Qt3DRender::RayCasting::QRayCastingServicePrivate::collides(const
      QRay3D &ray, const QBoundingVolume *volume)': Qt's library has no name
      for it, and its code in Qt's source does not compile apart from its
      file: unknown type name 'Hit'; did you mean
      'QCollisionQueryResult::Hit'?.
    """
    raise NotImplementedError(
        "'Qt3DRender.RayCasting.QRayCastingServicePrivate.collides' has no "
        "cute function yet. Qt's 'QCollisionQueryResult "
        "Qt3DRender::RayCasting::QRayCastingServicePrivate::collides(const "
        "QRay3D &ray, QBoundingVolumeProvider *provider, "
        "QAbstractCollisionQueryService::QueryMode mode, const QQueryHandle "
        "&handle)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: no member named "
        "'intersects' in "
        "'Qt3DRender::RayCasting::QCollisionQueryResult::Hit'. Qt's "
        "'QCollisionQueryResult::Hit "
        "Qt3DRender::RayCasting::QRayCastingServicePrivate::collides(const "
        "QRay3D &ray, const QBoundingVolume *volume)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: unknown type name 'Hit'; did you mean "
        "'QCollisionQueryResult::Hit'?.")
