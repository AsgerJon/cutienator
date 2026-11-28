"""
Qt3DCore::QComponentPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/6.12.0/Qt3DCore/private/qcomponent_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means Qt3DCore::QComponentPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QComponentPrivate(Qt3DCore.QNodePrivate):
  """
  The cute side of Qt's Qt3DCore::QComponentPrivate: a plain Python object
  standing in front of one C++ Qt3DCore::QComponentPrivate.

  It is built on the cute 'Qt3DCore::QNodePrivate', as Qt's
  Qt3DCore::QComponentPrivate is built on Qt's Qt3DCore::QNodePrivate, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QComponentPrivate that has a ritual and
  that Python can call so far, 3 names in all: 'addEntity', 'removeEntity',
  'q_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DCore::QComponentPrivate::~QComponentPrivate()': the destructor:
    Python never removes a C++ Qt3DCore::QComponentPrivate.
  - Qt's 'const QComponent *Qt3DCore::QComponentPrivate::q_func() const':
    takes in Python what 'QComponent *Qt3DCore::QComponentPrivate::q_func()'
    takes.

  What to expect
  --------------

  - The C++ Qt3DCore::QComponentPrivate is created at the first use, not by
    'Qt3DCore::QComponentPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QComponentPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QComponentPrivate'

  #  A C++ Qt3DCore::QComponentPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_QComponentPrivate'

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
    'Qt3DCore::QComponentPrivate::QComponentPrivate()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qcomponentprivate.html#QComponentPrivate
    """
    #  Qt3DCore::QComponentPrivate::QComponentPrivate()
    self._noteCreation(QComponentPrivate, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore17QComponentPrivateC1Ev',
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

  @overload(WAIT['Qt3DCore.QEntity'])
  @overload(NoneType)
  def addEntity(self, entity: Optional[Qt3DCore.QEntity]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QComponentPrivate::addEntity(QEntity
    *entity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qcomponentprivate.html#addEntity

    Parameters
    ----------

    entity : Optional[Qt3DCore.QEntity]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QComponentPrivate::addEntity(QEntity *entity)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore17QComponentPrivate9addEntityEPNS_7QEntityE',
        self._addressOf(entity),
    )

  @overload(WAIT['Qt3DCore.QEntity'])
  @overload(NoneType)
  def removeEntity(self, entity: Optional[Qt3DCore.QEntity]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QComponentPrivate::removeEntity(QEntity
    *entity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qcomponentprivate.html#removeEntity

    Parameters
    ----------

    entity : Optional[Qt3DCore.QEntity]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QComponentPrivate::removeEntity(QEntity *entity)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore17QComponentPrivate12removeEntityEPNS_7QEntityE',
        self._addressOf(entity),
    )

  def q_func(self) -> Optional[Qt3DCore.QComponent]:
    """
    Calls Qt's 'QComponent *Qt3DCore::QComponentPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qcomponentprivate.html#q_func

    Returns
    -------

    Optional[Qt3DCore.QComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QComponent *Qt3DCore::QComponentPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN8Qt3DCore17QComponentPrivate6q_funcEv',
    )
    return Qt3DCore.QComponent._cuteAt(address)
