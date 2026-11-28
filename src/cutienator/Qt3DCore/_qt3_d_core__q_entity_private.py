"""
Qt3DCore::QEntityPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/6.12.0/Qt3DCore/private/qentity_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means Qt3DCore::QEntityPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QEntityPrivate(Qt3DCore.QNodePrivate):
  """
  The cute side of Qt's Qt3DCore::QEntityPrivate: a plain Python object
  standing in front of one C++ Qt3DCore::QEntityPrivate.

  It is built on the cute 'Qt3DCore::QNodePrivate', as Qt's
  Qt3DCore::QEntityPrivate is built on Qt's Qt3DCore::QNodePrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QEntityPrivate that has a ritual and that
  Python can call so far, 6 names in all: 'q_func', 'get', 'parentEntityId',
  'updateComponentRelationShip', 'dumpSceneGraph',
  'removeDestroyedComponent'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DCore::QEntityPrivate::~QEntityPrivate()': the destructor:
    Python never removes a C++ Qt3DCore::QEntityPrivate.
  - Qt's 'const QEntity *Qt3DCore::QEntityPrivate::q_func() const': takes in
    Python what 'QEntity *Qt3DCore::QEntityPrivate::q_func()' takes.

  What has no ritual
  ------------------

  1 of the 10 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ Qt3DCore::QEntityPrivate is created at the first use, not by
    'Qt3DCore::QEntityPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QEntityPrivate.
  - Each name of Qt's Qt3DCore::QEntityPrivate that has no cute function yet,
    'componentsOfType', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['Qt3DCore.QEntity'])
  @overload(NoneType)
  def get(q: Optional[Qt3DCore.QEntity]) -> Optional[QEntityPrivate]:
    """
    Calls Qt's 'QEntityPrivate *Qt3DCore::QEntityPrivate::get(QEntity *q)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qentityprivate.html#get

    Parameters
    ----------

    q : Optional[Qt3DCore.QEntity]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QEntityPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QEntityPrivate *Qt3DCore::QEntityPrivate::get(QEntity *q)
    address = Rituals.call(
        'ritual_ZN8Qt3DCore14QEntityPrivate3getEPNS_7QEntityE',
        CuteMixin._addressOf(q),
    )
    return QEntityPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QEntityPrivate'

  #  A C++ Qt3DCore::QEntityPrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_QEntityPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def parentEntityId(self) -> Qt3DCore.QNodeId:
    """
    Calls Qt's 'QNodeId Qt3DCore::QEntityPrivate::parentEntityId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qentityprivate.html#parentEntityId

    Returns
    -------

    Qt3DCore.QNodeId
      A new cute Qt3DCore::QNodeId around the copy Qt gave back. Python owns
      it.
    """
    #  QNodeId Qt3DCore::QEntityPrivate::parentEntityId() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore14QEntityPrivate14parentEntityIdEv',
    )
    return Qt3DCore.QNodeId._cuteOwning(address)

  def dumpSceneGraph(self) -> str:
    """
    Calls Qt's 'QString Qt3DCore::QEntityPrivate::dumpSceneGraph() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qentityprivate.html#dumpSceneGraph

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DCore::QEntityPrivate::dumpSceneGraph() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore14QEntityPrivate14dumpSceneGraphEv',
    )

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
    'Qt3DCore::QEntityPrivate::QEntityPrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qentityprivate.html#QEntityPrivate
    """
    #  Qt3DCore::QEntityPrivate::QEntityPrivate()
    self._noteCreation(QEntityPrivate, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore14QEntityPrivateC1Ev',
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

  def q_func(self) -> Optional[Qt3DCore.QEntity]:
    """
    Calls Qt's 'QEntity *Qt3DCore::QEntityPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qentityprivate.html#q_func

    Returns
    -------

    Optional[Qt3DCore.QEntity]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QEntity *Qt3DCore::QEntityPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN8Qt3DCore14QEntityPrivate6q_funcEv',
    )
    return Qt3DCore.QEntity._cuteAt(address)

  @overload(
      WAIT['Qt3DCore.QComponent'],
      Qt3DCore.ComponentRelationshipChange.RelationShip,
  )
  @overload(NoneType, Qt3DCore.ComponentRelationshipChange.RelationShip)
  def updateComponentRelationShip(
      self,
      component: Optional[Qt3DCore.QComponent],
      change: Qt3DCore.ComponentRelationshipChange.RelationShip,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::QEntityPrivate::updateComponentRelationShip(QComponent
    *component, ComponentRelationshipChange::RelationShip change)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qentityprivate.html

    Parameters
    ----------

    component : Optional[Qt3DCore.QComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    change : Qt3DCore.ComponentRelationshipChange.RelationShip
      Passed on as its number.
    """
    #  void Qt3DCore::QEntityPrivate::updateComponentRelationShip(QComponent
    #      *component, ComponentRelationshipChange::RelationShip change)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore14QEntityPrivate27updateComponentRelationShipEPN'
        'S_10QComponentENS_27ComponentRelationshipChange12RelationShipE',
        self._addressOf(component), change.value,
    )

  @overload(WAIT['Qt3DCore.QComponent'])
  @overload(NoneType)
  def removeDestroyedComponent(
      self,
      comp: Optional[Qt3DCore.QComponent],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::QEntityPrivate::removeDestroyedComponent(QComponent *comp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qentityprivate.html

    Parameters
    ----------

    comp : Optional[Qt3DCore.QComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QEntityPrivate::removeDestroyedComponent(QComponent
    #      *comp)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore14QEntityPrivate24removeDestroyedComponentEPNS_1'
        '0QComponentE',
        self._addressOf(comp),
    )

  @staticmethod
  def componentsOfType(*__, **_) -> Never:
    """
    Qt's 'Qt3DCore::QEntityPrivate::componentsOfType': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'Qt3DCore.QEntityPrivate.componentsOfType' has no cute function "
        "yet. Qt's 'Qt3DCore::QEntityPrivate::componentsOfType': a "
        "template: a pattern and no single function.")
