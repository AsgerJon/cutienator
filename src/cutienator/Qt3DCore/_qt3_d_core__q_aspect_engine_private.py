"""
Qt3DCore::QAspectEnginePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/6.12.0/Qt3DCore/private/qaspectengine_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DCore::QAspectEnginePrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAspectEnginePrivate(QObjectPrivate, Qt3DCore.QAbstractFrontEndNodeManager):
  """
  The cute side of Qt's Qt3DCore::QAspectEnginePrivate: a plain Python object
  standing in front of one C++ Qt3DCore::QAspectEnginePrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  Qt3DCore::QAspectEnginePrivate is built on Qt's QObjectPrivate, and has
  everything that class has. It is built on the cute
  'Qt3DCore::QAbstractFrontEndNodeManager' as well, as Qt's
  Qt3DCore::QAspectEnginePrivate is built on Qt's
  Qt3DCore::QAbstractFrontEndNodeManager too, and has everything that class
  has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QAspectEnginePrivate that has a ritual and
  that Python can call so far, 11 names in all: 'q_func', 'initialize',
  'shutdown', 'exitSimulationLoop', 'initNodeTree', 'initNode', 'initEntity',
  'addNode', 'removeNode', 'lookupNode', 'get'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DCore::QAspectEnginePrivate::~QAspectEnginePrivate()': the
    destructor: Python never removes a C++ Qt3DCore::QAspectEnginePrivate.
  - Qt's 'const QAspectEngine *Qt3DCore::QAspectEnginePrivate::q_func()
    const': takes in Python what 'QAspectEngine
    *Qt3DCore::QAspectEnginePrivate::q_func()' takes.
  - Qt's 'QList<QNode *> Qt3DCore::QAspectEnginePrivate::lookupNodes(const
    QList<QNodeId> &ids) const': takes a type Python has no way to hand over
    yet.

  What to expect
  --------------

  - The C++ Qt3DCore::QAspectEnginePrivate is created at the first use, not
    by 'Qt3DCore::QAspectEnginePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QAspectEnginePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['Qt3DCore.QAspectEngine'])
  @overload(NoneType)
  def get(
      engine: Optional[Qt3DCore.QAspectEngine],
  ) -> Optional[QAspectEnginePrivate]:
    """
    Calls Qt's 'QAspectEnginePrivate
    *Qt3DCore::QAspectEnginePrivate::get(QAspectEngine *engine)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectengineprivate.html#get

    Parameters
    ----------

    engine : Optional[Qt3DCore.QAspectEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QAspectEnginePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAspectEnginePrivate
    #      *Qt3DCore::QAspectEnginePrivate::get(QAspectEngine *engine)
    address = Rituals.call(
        'ritual_ZN8Qt3DCore20QAspectEnginePrivate3getEPNS_13QAspectEngineE',
        CuteMixin._addressOf(engine),
    )
    return QAspectEnginePrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QAspectEnginePrivate'

  #  Qt's Qt3DCore::QAspectEnginePrivate is built on more than one class. The
  #  part of a C++ Qt3DCore::QAspectEnginePrivate that belongs to a class
  #  after the first begins somewhere inside the object, and the ritual named
  #  for that class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'Qt3DCore::QAbstractFrontEndNodeManager':
          'ritual_cast_Qt3DCore_QAspectEnginePrivate_Qt3DCore_QAbstractFrontEndNodeManager',
  }

  #  A C++ Qt3DCore::QAspectEnginePrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_QAspectEnginePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DCore.QNodeId'])
  def lookupNode(self, id: Qt3DCore.QNodeId) -> Optional[Qt3DCore.QNode]:
    """
    Calls Qt's 'QNode *Qt3DCore::QAspectEnginePrivate::lookupNode(QNodeId id)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectengineprivate.html#lookupNode

    Parameters
    ----------

    id : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.

    Returns
    -------

    Optional[Qt3DCore.QNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNode *Qt3DCore::QAspectEnginePrivate::lookupNode(QNodeId id) const
    ritual = (
        'ritual_ZNK8Qt3DCore20QAspectEnginePrivate10lookupNodeENS_7QNodeIdE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK8Qt3DCore20QAspectEnginePrivate10lookupNodeENS_7QN'
          'odeIdE')
    address = self.uglySide.call(ritual, self._valueOf(id))
    return Qt3DCore.QNode._cuteAt(address)

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
    'Qt3DCore::QAspectEnginePrivate::QAspectEnginePrivate()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectengineprivate.html
    """
    #  Qt3DCore::QAspectEnginePrivate::QAspectEnginePrivate()
    self._noteCreation(QAspectEnginePrivate, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore20QAspectEnginePrivateC1Ev',
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

  def q_func(self) -> Optional[Qt3DCore.QAspectEngine]:
    """
    Calls Qt's 'QAspectEngine *Qt3DCore::QAspectEnginePrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectengineprivate.html#q_func

    Returns
    -------

    Optional[Qt3DCore.QAspectEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAspectEngine *Qt3DCore::QAspectEnginePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN8Qt3DCore20QAspectEnginePrivate6q_funcEv',
    )
    return Qt3DCore.QAspectEngine._cuteAt(address)

  def initialize(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAspectEnginePrivate::initialize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectengineprivate.html#initialize
    """
    #  void Qt3DCore::QAspectEnginePrivate::initialize()
    self.uglySide.call(
        'ritual_ZN8Qt3DCore20QAspectEnginePrivate10initializeEv',
    )

  def shutdown(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAspectEnginePrivate::shutdown()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectengineprivate.html#shutdown
    """
    #  void Qt3DCore::QAspectEnginePrivate::shutdown()
    self.uglySide.call('ritual_ZN8Qt3DCore20QAspectEnginePrivate8shutdownEv')

  def exitSimulationLoop(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAspectEnginePrivate::exitSimulationLoop()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectengineprivate.html
    """
    #  void Qt3DCore::QAspectEnginePrivate::exitSimulationLoop()
    self.uglySide.call(
        'ritual_ZN8Qt3DCore20QAspectEnginePrivate18exitSimulationLoopEv',
    )

  @overload(WAIT['Qt3DCore.QNode'])
  @overload(NoneType)
  def initNodeTree(self, node: Optional[Qt3DCore.QNode]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAspectEnginePrivate::initNodeTree(QNode
    *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectengineprivate.html#initNodeTree

    Parameters
    ----------

    node : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QAspectEnginePrivate::initNodeTree(QNode *node)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore20QAspectEnginePrivate12initNodeTreeEPNS_5QNodeE',
        self._addressOf(node),
    )

  @overload(WAIT['Qt3DCore.QNode'])
  @overload(NoneType)
  def initNode(self, node: Optional[Qt3DCore.QNode]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAspectEnginePrivate::initNode(QNode *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectengineprivate.html#initNode

    Parameters
    ----------

    node : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QAspectEnginePrivate::initNode(QNode *node)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore20QAspectEnginePrivate8initNodeEPNS_5QNodeE',
        self._addressOf(node),
    )

  @overload(WAIT['Qt3DCore.QEntity'])
  @overload(NoneType)
  def initEntity(self, entity: Optional[Qt3DCore.QEntity]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAspectEnginePrivate::initEntity(QEntity
    *entity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectengineprivate.html#initEntity

    Parameters
    ----------

    entity : Optional[Qt3DCore.QEntity]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QAspectEnginePrivate::initEntity(QEntity *entity)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore20QAspectEnginePrivate10initEntityEPNS_7QEntityE',
        self._addressOf(entity),
    )

  @overload(WAIT['Qt3DCore.QNode'])
  @overload(NoneType)
  def addNode(self, node: Optional[Qt3DCore.QNode]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAspectEnginePrivate::addNode(QNode *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectengineprivate.html#addNode

    Parameters
    ----------

    node : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QAspectEnginePrivate::addNode(QNode *node)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore20QAspectEnginePrivate7addNodeEPNS_5QNodeE',
        self._addressOf(node),
    )

  @overload(WAIT['Qt3DCore.QNode'])
  @overload(NoneType)
  def removeNode(self, node: Optional[Qt3DCore.QNode]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAspectEnginePrivate::removeNode(QNode
    *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectengineprivate.html#removeNode

    Parameters
    ----------

    node : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QAspectEnginePrivate::removeNode(QNode *node)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore20QAspectEnginePrivate10removeNodeEPNS_5QNodeE',
        self._addressOf(node),
    )
