"""
Qt3DCore::QAbstractFrontEndNodeManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/6.12.0/Qt3DCore/private/qabstractfrontendnodemanager_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DCore::QAbstractFrontEndNodeManager to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute, WAIT
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional


class QAbstractFrontEndNodeManager(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DCore::QAbstractFrontEndNodeManager: a plain
  Python object standing in front of one C++
  Qt3DCore::QAbstractFrontEndNodeManager.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QAbstractFrontEndNodeManager that has a
  ritual and that Python can call so far, 1 name in all: 'lookupNode'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'Qt3DCore::QAbstractFrontEndNodeManager::~QAbstractFrontEndNodeManager(
    )': the destructor: Python never removes a C++
    Qt3DCore::QAbstractFrontEndNodeManager.
  - Qt's 'QList<QNode *>
    Qt3DCore::QAbstractFrontEndNodeManager::lookupNodes(const QList<QNodeId>
    &ids) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  1 of the 4 functions Qt declares: 1 the class is abstract, so C++ cannot
  make one, and the C++ class of ours does not fill in every function it
  leaves open.

  What to expect
  --------------

  - The C++ Qt3DCore::QAbstractFrontEndNodeManager is created at the first
    use, not by 'Qt3DCore::QAbstractFrontEndNodeManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QAbstractFrontEndNodeManager.
  - Each name of Qt's Qt3DCore::QAbstractFrontEndNodeManager that has no cute
    function yet, '__init__', 'lookupNodes', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside Qt3DCore::QAbstractFrontEndNodeManager, each
  #  a class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class DirtyNodeFlag(CuteFlags):
    """
    The flags enum 'Qt3DCore::QAbstractFrontEndNodeManager::DirtyNodeFlag' of
    Qt, with the 5 names Qt gives in it. Qt names the type of its
    combinations 'Qt3DCore::QAbstractFrontEndNodeManager::DirtyNodeSet'.
    """

    TransformDirty = 0x1
    GeometryDirty = 0x2
    EntityEnabledDirty = 0x4
    BuffersDirty = 0x8
    AllDirty = 0xffffff

  DirtyNodeSet = DirtyNodeFlag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QAbstractFrontEndNodeManager'

  #  A C++ Qt3DCore::QAbstractFrontEndNodeManager Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_QAbstractFrontEndNodeManager'

  #  The functions Qt calls itself that
  #  Qt3DCore::QAbstractFrontEndNodeManager is the first to declare and that
  #  cannot be handed to Python yet, each as Qt declares it. A class of a
  #  program that writes one of them anew is refused, since Qt would never
  #  call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'lookupNodes': (
          'QList<QNode *> '
          'Qt3DCore::QAbstractFrontEndNodeManager::lookupNodes(const '
          'QList<QNodeId> &) const',
      ),
  }

  #  The functions Qt calls itself that
  #  Qt3DCore::QAbstractFrontEndNodeManager is the first to declare. A class
  #  of a program built on it can write one anew, and Qt then calls that. For
  #  each name: the key C++ knows the function by, what it gives, and what it
  #  takes.
  __virtual_functions__ = {
      'lookupNode': (
          ('_ZNK8Qt3DCore28QAbstractFrontEndNodeManager10lookupNodeENS_7QNo'
           'deIdE',
           ('address', 'address', 'Qt3DCore:Qt3DCore.QNode'),
           (
               ('address', 'value', 'Qt3DCore:Qt3DCore.QNodeId'),
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

  @overload(WAIT['Qt3DCore.QNodeId'])
  def lookupNode(self, id: Qt3DCore.QNodeId) -> Optional[Qt3DCore.QNode]:
    """
    Calls Qt's 'QNode
    *Qt3DCore::QAbstractFrontEndNodeManager::lookupNode(QNodeId id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractfrontendnodemanager.html

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
    #  QNode *Qt3DCore::QAbstractFrontEndNodeManager::lookupNode(QNodeId id)
    #      const
    address = self._callAs(
        'Qt3DCore::QAbstractFrontEndNodeManager',
        'ritual_ZNK8Qt3DCore28QAbstractFrontEndNodeManager10lookupNodeENS_7'
        'QNodeIdE',
        self._valueOf(id),
    )
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's
    'Qt3DCore::QAbstractFrontEndNodeManager::QAbstractFrontEndNodeManager()':
    the class is abstract, so C++ cannot make one, and the C++ class of ours
    does not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'Qt3DCore.QAbstractFrontEndNodeManager.__init__' has no cute "
        "function yet. Qt's "
        "'Qt3DCore::QAbstractFrontEndNodeManager::QAbstractFrontEndNodeManag"
        "er()': the class is abstract, so C++ cannot make one, and the C++ "
        "class of ours does not fill in every function it leaves open.")

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

  @staticmethod
  def lookupNodes(*__, **_) -> Never:
    """
    Qt's 'QList<QNode *>
    Qt3DCore::QAbstractFrontEndNodeManager::lookupNodes(const QList<QNodeId>
    &ids) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QAbstractFrontEndNodeManager.lookupNodes' has no cute "
        "function yet. Qt's 'QList<QNode *> "
        "Qt3DCore::QAbstractFrontEndNodeManager::lookupNodes(const "
        "QList<QNodeId> &ids) const': takes a type Python has no way to "
        "hand over yet.")
