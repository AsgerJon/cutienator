"""
QSSGSceneDesc::Node binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DAssetUtils/6.12.0/QtQuick3DAssetUtils/private/qssgscenedesc_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGSceneDesc::Node to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class Node(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGSceneDesc::Node: a plain Python object standing
  in front of one C++ QSSGSceneDesc::Node.

  C++ hands a QSSGSceneDesc::Node around as a copy, so every C++
  QSSGSceneDesc::Node behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSSGSceneDesc::Node that has a ritual and that
  Python can call so far, 1 name in all: 'cleanupChildren'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGSceneDesc::Node::~Node()': the destructor: Python removes its
    C++ QSSGSceneDesc::Node by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSSGSceneDesc::Node is created at the first use, not by
    'QSSGSceneDesc::Node(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGSceneDesc::Node back gives a copy the ritual made
    for Python, in a new cute QSSGSceneDesc::Node.
  """

  #  The enums Qt writes inside QSSGSceneDesc::Node, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Type(CuteNum, scoped=True):
    """
    The enum 'QSSGSceneDesc::Node::Type' of Qt, with the 11 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Transform = Kee[int](0)
    Camera = Kee[int](1)
    Model = Kee[int](2)
    Texture = Kee[int](3)
    Material = Kee[int](4)
    Light = Kee[int](5)
    Mesh = Kee[int](6)
    Skin = Kee[int](7)
    Skeleton = Kee[int](8)
    Joint = Kee[int](9)
    MorphTarget = Kee[int](10)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGSceneDesc::Node'

  #  Qt's '~QSSGSceneDesc::Node()'. Naming it makes this a value class:
  #  Python owns every C++ QSSGSceneDesc::Node behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN13QSSGSceneDesc4NodeD1Ev'

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

  @overload(QByteArray, Type, QSSGRenderGraphObject.Type)
  def __init__(
      self,
      name: QByteArray,
      type: Type,
      rt: QSSGRenderGraphObject.Type,
  ) -> None:
    """
    Notes what was given, for Qt's 'QSSGSceneDesc::Node::Node(QByteArray
    name, Node::Type type, Node::RuntimeType rt)', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qssgscenedesc-node.html#Node

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    type : Type
      Passed on as its number.

    rt : QSSGRenderGraphObject.Type
      Passed on as its number.
    """
    #  QSSGSceneDesc::Node::Node(QByteArray name, Node::Type type,
    #      Node::RuntimeType rt)
    self._noteCreation(Node, lambda: Rituals.call(
        'ritual_ZN13QSSGSceneDesc4NodeC1E10QByteArrayNS0_4TypeEN21QSSGRende'
        'rGraphObject4TypeE',
        self._valueOf(name), type.value, rt.value,
    ))

  @overload(Type, QSSGRenderGraphObject.Type)
  def __init__(self, type: Type, rt: QSSGRenderGraphObject.Type) -> None:
    """
    Notes what was given, for Qt's 'QSSGSceneDesc::Node::Node(Node::Type
    type, Node::RuntimeType rt)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qssgscenedesc-node.html#Node

    Parameters
    ----------

    type : Type
      Passed on as its number.

    rt : QSSGRenderGraphObject.Type
      Passed on as its number.
    """
    #  QSSGSceneDesc::Node::Node(Node::Type type, Node::RuntimeType rt)
    self._noteCreation(Node, lambda: Rituals.call(
        'ritual_ZN13QSSGSceneDesc4NodeC1ENS0_4TypeEN21QSSGRenderGraphObject'
        '4TypeE',
        type.value, rt.value,
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

  def cleanupChildren(self) -> None:
    """
    Calls Qt's 'void QSSGSceneDesc::Node::cleanupChildren()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgscenedesc-node.html#cleanupChildren
    """
    #  void QSSGSceneDesc::Node::cleanupChildren()
    self.uglySide.call('ritual_ZN13QSSGSceneDesc4Node15cleanupChildrenEv')
