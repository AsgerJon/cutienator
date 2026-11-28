"""
LookAtNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/lookatnode_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means LookAtNode to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtQuick3D import QQuick3DNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuick3DNode = WAIT['QQuick3DNode']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class LookAtNode(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's LookAtNode: a plain Python object standing in front
  of one C++ LookAtNode.

  What exists
  -----------

  Every function of Qt's LookAtNode that has a ritual and that Python can
  call so far, 6 names in all: 'metaObject', 'tr', 'target', 'setTarget',
  'targetChanged', 'updateLookAt'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *LookAtNode::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int LookAtNode::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'LookAtNode::~LookAtNode()': the destructor: Python never removes a
    C++ LookAtNode.

  What has no ritual
  ------------------

  2 of the 12 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ LookAtNode is created at the first use, not by 'LookAtNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ LookAtNode.
  - Qt tells when it has removed the C++ LookAtNode. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
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
    Calls Qt's 'QString LookAtNode::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/lookatnode.html#tr

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
    #  QString LookAtNode::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10LookAtNode2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'LookAtNode'

  #  A C++ LookAtNode Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_LookAtNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *LookAtNode::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/lookatnode.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *LookAtNode::metaObject() const
    address = self.uglySide.call('ritual_ZNK10LookAtNode10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def target(self) -> Optional[QQuick3DNode]:
    """
    Calls Qt's 'QQuick3DNode *LookAtNode::target() const'.

    Qt's own words: https://doc.qt.io/qt-6/lookatnode.html#target

    Returns
    -------

    Optional[QQuick3DNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DNode *LookAtNode::target() const
    address = self.uglySide.call('ritual_ZNK10LookAtNode6targetEv')
    from ..QtQuick3D import QQuick3DNode
    return QQuick3DNode._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuick3DNode)
  @overload(NoneType)
  def setTarget(self, node: Optional[QQuick3DNode]) -> None:
    """
    Calls Qt's 'void LookAtNode::setTarget(QQuick3DNode *node)'.

    Qt's own words: https://doc.qt.io/qt-6/lookatnode.html#setTarget

    Parameters
    ----------

    node : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void LookAtNode::setTarget(QQuick3DNode *node)
    self.uglySide.call(
        'ritual_ZN10LookAtNode9setTargetEP12QQuick3DNode',
        self._addressOf(node),
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'LookAtNode::LookAtNode()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/lookatnode.html#LookAtNode
    """
    #  LookAtNode::LookAtNode()
    self._noteCreation(LookAtNode, lambda: Rituals.call(
        'ritual_ZN10LookAtNodeC1Ev',
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

  def targetChanged(self) -> None:
    """
    Calls Qt's 'void LookAtNode::targetChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/lookatnode.html#targetChanged
    """
    #  void LookAtNode::targetChanged()
    self.uglySide.call('ritual_ZN10LookAtNode13targetChangedEv')

  def updateLookAt(self) -> None:
    """
    Calls Qt's 'void LookAtNode::updateLookAt()'.

    Qt's own words: https://doc.qt.io/qt-6/lookatnode.html#updateLookAt
    """
    #  void LookAtNode::updateLookAt()
    self.uglySide.call('ritual_ZN10LookAtNode12updateLookAtEv')
