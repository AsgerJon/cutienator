"""
Qt3DCore::QChangeArbiter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/6.12.0/Qt3DCore/private/qchangearbiter_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DCore::QChangeArbiter to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QChangeArbiter(QObject):
  """
  The cute side of Qt's Qt3DCore::QChangeArbiter: a plain Python object
  standing in front of one C++ Qt3DCore::QChangeArbiter.

  It is built on the cute 'QObject', as Qt's Qt3DCore::QChangeArbiter is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QChangeArbiter that has a ritual and that
  Python can call so far, 8 names in all: 'metaObject', 'tr',
  'addDirtyFrontEndNode', 'addDirtyEntityComponentNodes',
  'removeDirtyFrontEndNode', 'setScene', 'scene', 'receivedChange'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DCore::QChangeArbiter::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int Qt3DCore::QChangeArbiter::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DCore::QChangeArbiter::~QChangeArbiter()': the destructor:
    Python never removes a C++ Qt3DCore::QChangeArbiter.
  - Qt's 'QList<QNode *> Qt3DCore::QChangeArbiter::takeDirtyFrontEndNodes()':
    gives a type Python has no way to take yet.
  - Qt's 'QList<ComponentRelationshipChange>
    Qt3DCore::QChangeArbiter::takeDirtyEntityComponentNodes()': gives a type
    Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DCore::QChangeArbiter is created at the first use, not by
    'Qt3DCore::QChangeArbiter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QChangeArbiter.
  - Qt tells when it has removed the C++ Qt3DCore::QChangeArbiter. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DCore::QChangeArbiter that has no cute function yet,
    'takeDirtyEntityComponentNodes', 'takeDirtyFrontEndNodes', holds a
    function that raises 'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString Qt3DCore::QChangeArbiter::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qchangearbiter.html#tr

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
    #  QString Qt3DCore::QChangeArbiter::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN8Qt3DCore14QChangeArbiter2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QChangeArbiter'

  #  A C++ Qt3DCore::QChangeArbiter Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_QChangeArbiter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DCore::QChangeArbiter::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qchangearbiter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DCore::QChangeArbiter::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore14QChangeArbiter10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def scene(self) -> Optional[Qt3DCore.QScene]:
    """
    Calls Qt's 'QScene *Qt3DCore::QChangeArbiter::scene() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qchangearbiter.html#scene

    Returns
    -------

    Optional[Qt3DCore.QScene]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScene *Qt3DCore::QChangeArbiter::scene() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore14QChangeArbiter5sceneEv',
    )
    return Qt3DCore.QScene._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DCore.QScene'])
  @overload(NoneType)
  def setScene(self, scene: Optional[Qt3DCore.QScene]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QChangeArbiter::setScene(Qt3DCore::QScene
    *scene)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qchangearbiter.html#setScene

    Parameters
    ----------

    scene : Optional[Qt3DCore.QScene]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QChangeArbiter::setScene(Qt3DCore::QScene *scene)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore14QChangeArbiter8setSceneEPNS_6QSceneE',
        self._addressOf(scene),
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DCore::QChangeArbiter::QChangeArbiter(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qchangearbiter.html#QChangeArbiter

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DCore::QChangeArbiter::QChangeArbiter(QObject *parent)
    self._noteCreation(QChangeArbiter, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore14QChangeArbiterC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  @overload(WAIT['Qt3DCore.QNode'])
  @overload(NoneType)
  def addDirtyFrontEndNode(self, node: Optional[Qt3DCore.QNode]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QChangeArbiter::addDirtyFrontEndNode(QNode
    *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qchangearbiter.html#addDirtyFrontEndNode

    Parameters
    ----------

    node : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QChangeArbiter::addDirtyFrontEndNode(QNode *node)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore14QChangeArbiter20addDirtyFrontEndNodeEPNS_5QNod'
        'eE',
        self._addressOf(node),
    )

  @overload(
      WAIT['Qt3DCore.QEntity'], WAIT['Qt3DCore.QComponent'],
      Qt3DCore.ComponentRelationshipChange.RelationShip,
  )
  @overload(
      WAIT['Qt3DCore.QEntity'], NoneType,
      Qt3DCore.ComponentRelationshipChange.RelationShip,
  )
  @overload(
      NoneType, WAIT['Qt3DCore.QComponent'],
      Qt3DCore.ComponentRelationshipChange.RelationShip,
  )
  @overload(
      NoneType, NoneType, Qt3DCore.ComponentRelationshipChange.RelationShip,
  )
  def addDirtyEntityComponentNodes(
      self,
      entity: Optional[Qt3DCore.QEntity],
      component: Optional[Qt3DCore.QComponent],
      change: Qt3DCore.ComponentRelationshipChange.RelationShip,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::QChangeArbiter::addDirtyEntityComponentNodes(QEntity *entity,
    QComponent *component, ComponentRelationshipChange::RelationShip
    change)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qchangearbiter.html

    Parameters
    ----------

    entity : Optional[Qt3DCore.QEntity]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    component : Optional[Qt3DCore.QComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    change : Qt3DCore.ComponentRelationshipChange.RelationShip
      Passed on as its number.
    """
    #  void Qt3DCore::QChangeArbiter::addDirtyEntityComponentNodes(QEntity
    #      *entity, QComponent *component,
    #      ComponentRelationshipChange::RelationShip change)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore14QChangeArbiter28addDirtyEntityComponentNodesEP'
        'NS_7QEntityEPNS_10QComponentENS_27ComponentRelationshipChange12Rel'
        'ationShipE',
        self._addressOf(entity), self._addressOf(component), change.value,
    )

  @overload(WAIT['Qt3DCore.QNode'])
  @overload(NoneType)
  def removeDirtyFrontEndNode(self, node: Optional[Qt3DCore.QNode]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QChangeArbiter::removeDirtyFrontEndNode(QNode
    *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qchangearbiter.html

    Parameters
    ----------

    node : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QChangeArbiter::removeDirtyFrontEndNode(QNode *node)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore14QChangeArbiter23removeDirtyFrontEndNodeEPNS_5Q'
        'NodeE',
        self._addressOf(node),
    )

  def receivedChange(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QChangeArbiter::receivedChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qchangearbiter.html#receivedChange
    """
    #  void Qt3DCore::QChangeArbiter::receivedChange()
    self.uglySide.call(
        'ritual_ZN8Qt3DCore14QChangeArbiter14receivedChangeEv',
    )

  @staticmethod
  def takeDirtyEntityComponentNodes(*__, **_) -> Never:
    """
    Qt's 'QList<ComponentRelationshipChange>
    Qt3DCore::QChangeArbiter::takeDirtyEntityComponentNodes()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QChangeArbiter.takeDirtyEntityComponentNodes' has no "
        "cute function yet. Qt's 'QList<ComponentRelationshipChange> "
        "Qt3DCore::QChangeArbiter::takeDirtyEntityComponentNodes()': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def takeDirtyFrontEndNodes(*__, **_) -> Never:
    """
    Qt's 'QList<QNode *> Qt3DCore::QChangeArbiter::takeDirtyFrontEndNodes()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QChangeArbiter.takeDirtyFrontEndNodes' has no cute "
        "function yet. Qt's 'QList<QNode *> "
        "Qt3DCore::QChangeArbiter::takeDirtyFrontEndNodes()': gives a type "
        "Python has no way to take yet.")
