"""
QSSGMeshBVHNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgmeshbvh_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSSGMeshBVHNode to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QSSGMeshBVH

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSSGMeshBVHNode(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGMeshBVHNode: a plain Python object standing in
  front of one C++ QSSGMeshBVHNode.

  C++ hands a QSSGMeshBVHNode around as a copy, so every C++ QSSGMeshBVHNode
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QSSGMeshBVHNode yet. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGMeshBVHNode::~QSSGMeshBVHNode()': the destructor: Python
    removes its C++ QSSGMeshBVHNode by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSSGMeshBVHNode is created at the first use, not by
    'QSSGMeshBVHNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGMeshBVHNode back gives a copy the ritual made for
    Python, in a new cute QSSGMeshBVHNode.
  """

  #  The classes Qt writes inside QSSGMeshBVHNode, each a class in here as in
  #  C++.

  class Handle(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGMeshBVHNode::Handle: a plain Python object
    standing in front of one C++ QSSGMeshBVHNode::Handle.

    C++ hands a QSSGMeshBVHNode::Handle around as a copy, so every C++
    QSSGMeshBVHNode::Handle behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QSSGMeshBVHNode::Handle that has a ritual and that
    Python can call so far, 1 name in all: 'isNull'. It can be made from
    Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'const QSSGMeshBVHNode *QSSGMeshBVHNode::Handle::operator const
      QSSGMeshBVHNode *() const': an operator Python has no name for.
    - Qt's 'QSSGMeshBVHNode *QSSGMeshBVHNode::Handle::operator->() const': an
      operator Python has no name for.
    - Qt's 'QSSGMeshBVHNode::Handle::~Handle()': the destructor: Python
      removes its C++ QSSGMeshBVHNode::Handle by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QSSGMeshBVHNode::Handle is created at the first use, not by
      'QSSGMeshBVHNode::Handle(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGMeshBVHNode::Handle back gives a copy the
      ritual made for Python, in a new cute QSSGMeshBVHNode::Handle.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QSSGMeshBVH = WAIT['QSSGMeshBVH']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGMeshBVHNode::Handle'

    #  Qt's '~QSSGMeshBVHNode::Handle()'. Naming it makes this a value class:
    #  Python owns every C++ QSSGMeshBVHNode::Handle behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN15QSSGMeshBVHNode6HandleD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def isNull(self) -> bool:
      """
      Calls Qt's 'bool QSSGMeshBVHNode::Handle::isNull() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qssgmeshbvhnode-handle.html#isNull
      """
      #  bool QSSGMeshBVHNode::Handle::isNull() const
      return self.uglySide.call(
          'ritual_ZNK15QSSGMeshBVHNode6Handle6isNullEv',
      )

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

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's 'QSSGMeshBVHNode::Handle::Handle()',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qssgmeshbvhnode-handle.html#Handle
      """
      #  QSSGMeshBVHNode::Handle::Handle()
      self._noteCreation(QSSGMeshBVHNode.Handle, lambda: Rituals.call(
          'ritual_ZN15QSSGMeshBVHNode6HandleC1Ev',
      ))

    @overload(QSSGMeshBVH, int)
    @overload(NoneType, int)
    def __init__(self, owner: Optional[QSSGMeshBVH], idx: int) -> None:
      """
      Notes what was given, for Qt's
      'QSSGMeshBVHNode::Handle::Handle(QSSGMeshBVH *owner, size_t idx)',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qssgmeshbvhnode-handle.html#Handle

      Parameters
      ----------

      owner : Optional[QSSGMeshBVH]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      idx : int
        Passed on as it is.
      """
      #  QSSGMeshBVHNode::Handle::Handle(QSSGMeshBVH *owner, size_t idx)
      self._noteCreation(QSSGMeshBVHNode.Handle, lambda: Rituals.call(
          'ritual_ZN15QSSGMeshBVHNode6HandleC1EP11QSSGMeshBVHm',
          self._addressOf(owner), idx,
      ))

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
  __qt_class__ = 'QSSGMeshBVHNode'

  #  Qt's '~QSSGMeshBVHNode()'. Naming it makes this a value class: Python
  #  owns every C++ QSSGMeshBVHNode behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QSSGMeshBVHNodeD1Ev'

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
