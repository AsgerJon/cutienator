"""
icutils::Node binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/inlinecomponentutils_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means icutils::Node to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class Node(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's icutils::Node: a plain Python object standing in
  front of one C++ icutils::Node.

  C++ hands a icutils::Node around as a copy, so every C++ icutils::Node
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's icutils::Node that has a ritual and that Python can
  call so far, 6 names in all: '__eq__', 'hasPermanentMark',
  'hasTemporaryMark', 'setPermanentMark', 'setTemporaryMark', 'index'. It can
  be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'icutils::Node::Node(Node &&a0)': takes a type Python has no way to
    hand over yet.
  - Qt's 'Node &icutils::Node::operator=(const Node &a0)': assignment: Python
    binds a name and has no operator for it.
  - Qt's 'Node &icutils::Node::operator=(Node &&a0)': assignment: Python
    binds a name and has no operator for it.
  - Qt's 'icutils::Node::~Node()': the destructor: Python removes its C++
    icutils::Node by it, and has no other use for it.

  What to expect
  --------------

  - The C++ icutils::Node is created at the first use, not by
    'icutils::Node(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a icutils::Node back gives a copy the ritual made for
    Python, in a new cute icutils::Node.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'icutils::Node'

  #  Qt's '~icutils::Node()'. Naming it makes this a value class: Python owns
  #  every C++ icutils::Node behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN7icutils4NodeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasPermanentMark(self) -> bool:
    """
    Calls Qt's 'bool icutils::Node::hasPermanentMark() const'.

    Qt's own words: https://doc.qt.io/qt-6/icutils-node.html#hasPermanentMark
    """
    #  bool icutils::Node::hasPermanentMark() const
    return self.uglySide.call('ritual_ZNK7icutils4Node16hasPermanentMarkEv')

  def hasTemporaryMark(self) -> bool:
    """
    Calls Qt's 'bool icutils::Node::hasTemporaryMark() const'.

    Qt's own words: https://doc.qt.io/qt-6/icutils-node.html#hasTemporaryMark
    """
    #  bool icutils::Node::hasTemporaryMark() const
    return self.uglySide.call('ritual_ZNK7icutils4Node16hasTemporaryMarkEv')

  def index(self) -> int:
    """
    Calls Qt's 'IndexType icutils::Node::index() const'.

    Qt's own words: https://doc.qt.io/qt-6/icutils-node.html#index
    """
    #  IndexType icutils::Node::index() const
    return self.uglySide.call('ritual_ZNK7icutils4Node5indexEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setPermanentMark(self) -> None:
    """
    Calls Qt's 'void icutils::Node::setPermanentMark()'.

    Qt's own words: https://doc.qt.io/qt-6/icutils-node.html#setPermanentMark
    """
    #  void icutils::Node::setPermanentMark()
    self.uglySide.call('ritual_ZN7icutils4Node16setPermanentMarkEv')

  def setTemporaryMark(self) -> None:
    """
    Calls Qt's 'void icutils::Node::setTemporaryMark()'.

    Qt's own words: https://doc.qt.io/qt-6/icutils-node.html#setTemporaryMark
    """
    #  void icutils::Node::setTemporaryMark()
    self.uglySide.call('ritual_ZN7icutils4Node16setTemporaryMarkEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: Node) -> bool:
    """
    Calls Qt's 'bool icutils::Node::operator==(const Node &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/icutils-node.html#operator==

    Parameters
    ----------

    other : Node
      Passed on as a value: Qt reads the C++ icutils::Node, which stays
      Python's own.
    """
    #  bool icutils::Node::operator==(const Node &other) const
    return self.uglySide.call(
        'ritual_ZNK7icutils4NodeeqERKS0_', self._valueOf(other),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'icutils::Node::Node()', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/icutils-node.html#Node
    """
    #  icutils::Node::Node()
    self._noteCreation(Node, lambda: Rituals.call(
        'ritual_ZN7icutils4NodeC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: Node) -> None:
    """
    Notes what was given, for Qt's 'icutils::Node::Node(const Node &a0)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/icutils-node.html#Node

    Parameters
    ----------

    a0 : Node
      Passed on as a value: Qt reads the C++ icutils::Node, which stays
      Python's own.
    """
    #  icutils::Node::Node(const Node &a0)
    self._noteCreation(Node, lambda: Rituals.call(
        'ritual_ZN7icutils4NodeC1ERKS0_', self._valueOf(a0),
    ))

  @overload(int)
  def __init__(self, s: int) -> None:
    """
    Notes what was given, for Qt's 'icutils::Node::Node(IndexType s)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/icutils-node.html#Node

    Parameters
    ----------

    s : int
      Passed on as it is.
    """
    #  icutils::Node::Node(IndexType s)
    self._noteCreation(Node, lambda: Rituals.call(
        'ritual_ZN7icutils4NodeC1Em', s,
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
