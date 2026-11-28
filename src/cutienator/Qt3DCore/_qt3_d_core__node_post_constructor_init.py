"""
Qt3DCore::NodePostConstructorInit binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/6.12.0/Qt3DCore/private/qnode_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means Qt3DCore::NodePostConstructorInit to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QObject
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class NodePostConstructorInit(QObject):
  """
  The cute side of Qt's Qt3DCore::NodePostConstructorInit: a plain Python
  object standing in front of one C++ Qt3DCore::NodePostConstructorInit.

  It is built on the cute 'QObject', as Qt's
  Qt3DCore::NodePostConstructorInit is built on Qt's QObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::NodePostConstructorInit that has a ritual
  and that Python can call so far, 4 names in all: 'metaObject',
  'removeNode', 'addNode', 'processNodes'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DCore::NodePostConstructorInit::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DCore::NodePostConstructorInit::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DCore::NodePostConstructorInit::~NodePostConstructorInit()': the
    destructor: Python never removes a C++ Qt3DCore::NodePostConstructorInit.

  What has no ritual
  ------------------

  4 of the 11 functions Qt declares: 2 not a gap; 2 leans on 'Qt3DCore.

  What to expect
  --------------

  - The C++ Qt3DCore::NodePostConstructorInit is created at the first use,
    not by 'Qt3DCore::NodePostConstructorInit(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::NodePostConstructorInit.
  - Qt tells when it has removed the C++ Qt3DCore::NodePostConstructorInit.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DCore::NodePostConstructorInit that has no cute
    function yet, '__init__', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::NodePostConstructorInit'

  #  A C++ Qt3DCore::NodePostConstructorInit Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_NodePostConstructorInit'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *Qt3DCore::NodePostConstructorInit::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-nodepostconstructorinit.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DCore::NodePostConstructorInit::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore23NodePostConstructorInit10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'Qt3DCore::NodePostConstructorInit::NodePostConstructorInit(QObject
    *parent)': leans on
    'Qt3DCore::NodePostConstructorInit::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DCore.NodePostConstructorInit.__init__' has no cute function "
        "yet. Qt's "
        "'Qt3DCore::NodePostConstructorInit::NodePostConstructorInit(QObject"
        " *parent)': leans on "
        "'Qt3DCore::NodePostConstructorInit::qt_metacall(QMetaObject::Call, "
        "int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

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
  def removeNode(self, node: Optional[Qt3DCore.QNode]) -> None:
    """
    Calls Qt's 'void Qt3DCore::NodePostConstructorInit::removeNode(QNode
    *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-nodepostconstructorinit.html#removeNode

    Parameters
    ----------

    node : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::NodePostConstructorInit::removeNode(QNode *node)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore23NodePostConstructorInit10removeNodeEPNS_5QNode'
        'E',
        self._addressOf(node),
    )

  @overload(WAIT['Qt3DCore.QNode'])
  @overload(NoneType)
  def addNode(self, node: Optional[Qt3DCore.QNode]) -> None:
    """
    Calls Qt's 'void Qt3DCore::NodePostConstructorInit::addNode(QNode
    *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-nodepostconstructorinit.html#addNode

    Parameters
    ----------

    node : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::NodePostConstructorInit::addNode(QNode *node)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore23NodePostConstructorInit7addNodeEPNS_5QNodeE',
        self._addressOf(node),
    )

  def processNodes(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::NodePostConstructorInit::processNodes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-nodepostconstructorinit.html#processNodes
    """
    #  void Qt3DCore::NodePostConstructorInit::processNodes()
    self.uglySide.call(
        'ritual_ZN8Qt3DCore23NodePostConstructorInit12processNodesEv',
    )
