"""
QSGNodeUpdater binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgnodeupdater_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSGNodeUpdater to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QSGClipNode, QSGGeometryNode, QSGNode, QSGOpacityNode
  from . import QSGRenderNode, QSGTransformNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSGClipNode = WAIT['QSGClipNode']
  QSGGeometryNode = WAIT['QSGGeometryNode']
  QSGNode = WAIT['QSGNode']
  QSGOpacityNode = WAIT['QSGOpacityNode']
  QSGRenderNode = WAIT['QSGRenderNode']
  QSGTransformNode = WAIT['QSGTransformNode']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGNodeUpdater(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSGNodeUpdater: a plain Python object standing in
  front of one C++ QSGNodeUpdater.

  What exists
  -----------

  Every function of Qt's QSGNodeUpdater that has a ritual and that Python can
  call so far, 14 names in all: 'updateStates', 'isNodeBlocked',
  'enterTransformNode', 'leaveTransformNode', 'enterClipNode',
  'leaveClipNode', 'enterOpacityNode', 'leaveOpacityNode',
  'enterGeometryNode', 'leaveGeometryNode', 'enterRenderNode',
  'leaveRenderNode', 'visitNode', 'visitChildren'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGNodeUpdater::~QSGNodeUpdater()': the destructor: Python never
    removes a C++ QSGNodeUpdater.

  What to expect
  --------------

  - The C++ QSGNodeUpdater is created at the first use, not by
    'QSGNodeUpdater(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGNodeUpdater.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGNodeUpdater'

  #  A C++ QSGNodeUpdater Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGNodeUpdater'

  #  The functions Qt calls itself that QSGNodeUpdater is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'updateStates': (
          ('_ZN14QSGNodeUpdater12updateStatesEP7QSGNode',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QSGNode'),
           )),
      ),
      'isNodeBlocked': (
          ('_ZNK14QSGNodeUpdater13isNodeBlockedEP7QSGNodeS1_',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtQuick:QSGNode'),
               ('address', 'address', 'QtQuick:QSGNode'),
           )),
      ),
      'enterTransformNode': (
          ('_ZN14QSGNodeUpdater18enterTransformNodeEP16QSGTransformNode',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QSGTransformNode'),
           )),
      ),
      'leaveTransformNode': (
          ('_ZN14QSGNodeUpdater18leaveTransformNodeEP16QSGTransformNode',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QSGTransformNode'),
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

  @overload(QSGNode, QSGNode)
  @overload(QSGNode, NoneType)
  @overload(NoneType, QSGNode)
  @overload(NoneType, NoneType)
  def isNodeBlocked(
      self,
      n: Optional[QSGNode],
      root: Optional[QSGNode],
  ) -> bool:
    """
    Calls Qt's 'bool QSGNodeUpdater::isNodeBlocked(QSGNode *n, QSGNode *root)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnodeupdater.html#isNodeBlocked

    Parameters
    ----------

    n : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    root : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSGNodeUpdater::isNodeBlocked(QSGNode *n, QSGNode *root) const
    ritual = 'ritual_ZNK14QSGNodeUpdater13isNodeBlockedEP7QSGNodeS1_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QSGNodeUpdater13isNodeBlockedEP7QSGNodeS1_'
    return self.uglySide.call(
        ritual,
        self._addressOf(n, 'QSGNode'), self._addressOf(root, 'QSGNode'),
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
    Notes what was given, for Qt's 'QSGNodeUpdater::QSGNodeUpdater()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsgnodeupdater.html#QSGNodeUpdater
    """
    #  QSGNodeUpdater::QSGNodeUpdater()
    self._noteCreation(QSGNodeUpdater, lambda: Rituals.call(
        'ritual_ZN14QSGNodeUpdaterC1Ev',
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

  @overload(QSGNode)
  @overload(NoneType)
  def updateStates(self, n: Optional[QSGNode]) -> None:
    """
    Calls Qt's 'void QSGNodeUpdater::updateStates(QSGNode *n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnodeupdater.html#updateStates

    Parameters
    ----------

    n : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGNodeUpdater::updateStates(QSGNode *n)
    ritual = 'ritual_ZN14QSGNodeUpdater12updateStatesEP7QSGNode'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QSGNodeUpdater12updateStatesEP7QSGNode'
    self.uglySide.call(ritual, self._addressOf(n, 'QSGNode'))

  @overload(QSGTransformNode)
  @overload(NoneType)
  def enterTransformNode(self, a0: Optional[QSGTransformNode]) -> None:
    """
    Calls Qt's 'void QSGNodeUpdater::enterTransformNode(QSGTransformNode
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgnodeupdater.html#enterTransformNode

    Parameters
    ----------

    a0 : Optional[QSGTransformNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGNodeUpdater::enterTransformNode(QSGTransformNode *a0)
    ritual = (
        'ritual_ZN14QSGNodeUpdater18enterTransformNodeEP16QSGTransformNode')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QSGNodeUpdater18enterTransformNodeEP16QSGTransfor'
          'mNode')
    self.uglySide.call(ritual, self._addressOf(a0, 'QSGTransformNode'))

  @overload(QSGTransformNode)
  @overload(NoneType)
  def leaveTransformNode(self, a0: Optional[QSGTransformNode]) -> None:
    """
    Calls Qt's 'void QSGNodeUpdater::leaveTransformNode(QSGTransformNode
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgnodeupdater.html#leaveTransformNode

    Parameters
    ----------

    a0 : Optional[QSGTransformNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGNodeUpdater::leaveTransformNode(QSGTransformNode *a0)
    ritual = (
        'ritual_ZN14QSGNodeUpdater18leaveTransformNodeEP16QSGTransformNode')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QSGNodeUpdater18leaveTransformNodeEP16QSGTransfor'
          'mNode')
    self.uglySide.call(ritual, self._addressOf(a0, 'QSGTransformNode'))

  @overload(QSGClipNode)
  @overload(NoneType)
  def enterClipNode(self, c: Optional[QSGClipNode]) -> None:
    """
    Calls Qt's 'void QSGNodeUpdater::enterClipNode(QSGClipNode *c)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnodeupdater.html#enterClipNode

    Parameters
    ----------

    c : Optional[QSGClipNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGNodeUpdater::enterClipNode(QSGClipNode *c)
    self.uglySide.call(
        'ritual_ZN14QSGNodeUpdater13enterClipNodeEP11QSGClipNode',
        self._addressOf(c),
    )

  @overload(QSGClipNode)
  @overload(NoneType)
  def leaveClipNode(self, c: Optional[QSGClipNode]) -> None:
    """
    Calls Qt's 'void QSGNodeUpdater::leaveClipNode(QSGClipNode *c)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnodeupdater.html#leaveClipNode

    Parameters
    ----------

    c : Optional[QSGClipNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGNodeUpdater::leaveClipNode(QSGClipNode *c)
    self.uglySide.call(
        'ritual_ZN14QSGNodeUpdater13leaveClipNodeEP11QSGClipNode',
        self._addressOf(c),
    )

  @overload(QSGOpacityNode)
  @overload(NoneType)
  def enterOpacityNode(self, o: Optional[QSGOpacityNode]) -> None:
    """
    Calls Qt's 'void QSGNodeUpdater::enterOpacityNode(QSGOpacityNode *o)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgnodeupdater.html#enterOpacityNode

    Parameters
    ----------

    o : Optional[QSGOpacityNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGNodeUpdater::enterOpacityNode(QSGOpacityNode *o)
    self.uglySide.call(
        'ritual_ZN14QSGNodeUpdater16enterOpacityNodeEP14QSGOpacityNode',
        self._addressOf(o),
    )

  @overload(QSGOpacityNode)
  @overload(NoneType)
  def leaveOpacityNode(self, o: Optional[QSGOpacityNode]) -> None:
    """
    Calls Qt's 'void QSGNodeUpdater::leaveOpacityNode(QSGOpacityNode *o)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgnodeupdater.html#leaveOpacityNode

    Parameters
    ----------

    o : Optional[QSGOpacityNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGNodeUpdater::leaveOpacityNode(QSGOpacityNode *o)
    self.uglySide.call(
        'ritual_ZN14QSGNodeUpdater16leaveOpacityNodeEP14QSGOpacityNode',
        self._addressOf(o),
    )

  @overload(QSGGeometryNode)
  @overload(NoneType)
  def enterGeometryNode(self, a0: Optional[QSGGeometryNode]) -> None:
    """
    Calls Qt's 'void QSGNodeUpdater::enterGeometryNode(QSGGeometryNode *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgnodeupdater.html#enterGeometryNode

    Parameters
    ----------

    a0 : Optional[QSGGeometryNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGNodeUpdater::enterGeometryNode(QSGGeometryNode *a0)
    self.uglySide.call(
        'ritual_ZN14QSGNodeUpdater17enterGeometryNodeEP15QSGGeometryNode',
        self._addressOf(a0, 'QSGGeometryNode'),
    )

  @overload(QSGGeometryNode)
  @overload(NoneType)
  def leaveGeometryNode(self, a0: Optional[QSGGeometryNode]) -> None:
    """
    Calls Qt's 'void QSGNodeUpdater::leaveGeometryNode(QSGGeometryNode *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgnodeupdater.html#leaveGeometryNode

    Parameters
    ----------

    a0 : Optional[QSGGeometryNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGNodeUpdater::leaveGeometryNode(QSGGeometryNode *a0)
    self.uglySide.call(
        'ritual_ZN14QSGNodeUpdater17leaveGeometryNodeEP15QSGGeometryNode',
        self._addressOf(a0, 'QSGGeometryNode'),
    )

  @overload(QSGRenderNode)
  @overload(NoneType)
  def enterRenderNode(self, a0: Optional[QSGRenderNode]) -> None:
    """
    Calls Qt's 'void QSGNodeUpdater::enterRenderNode(QSGRenderNode *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgnodeupdater.html#enterRenderNode

    Parameters
    ----------

    a0 : Optional[QSGRenderNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGNodeUpdater::enterRenderNode(QSGRenderNode *a0)
    self.uglySide.call(
        'ritual_ZN14QSGNodeUpdater15enterRenderNodeEP13QSGRenderNode',
        self._addressOf(a0),
    )

  @overload(QSGRenderNode)
  @overload(NoneType)
  def leaveRenderNode(self, a0: Optional[QSGRenderNode]) -> None:
    """
    Calls Qt's 'void QSGNodeUpdater::leaveRenderNode(QSGRenderNode *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgnodeupdater.html#leaveRenderNode

    Parameters
    ----------

    a0 : Optional[QSGRenderNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGNodeUpdater::leaveRenderNode(QSGRenderNode *a0)
    self.uglySide.call(
        'ritual_ZN14QSGNodeUpdater15leaveRenderNodeEP13QSGRenderNode',
        self._addressOf(a0),
    )

  @overload(QSGNode)
  @overload(NoneType)
  def visitNode(self, n: Optional[QSGNode]) -> None:
    """
    Calls Qt's 'void QSGNodeUpdater::visitNode(QSGNode *n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnodeupdater.html#visitNode

    Parameters
    ----------

    n : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGNodeUpdater::visitNode(QSGNode *n)
    self.uglySide.call(
        'ritual_ZN14QSGNodeUpdater9visitNodeEP7QSGNode',
        self._addressOf(n, 'QSGNode'),
    )

  @overload(QSGNode)
  @overload(NoneType)
  def visitChildren(self, n: Optional[QSGNode]) -> None:
    """
    Calls Qt's 'void QSGNodeUpdater::visitChildren(QSGNode *n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnodeupdater.html#visitChildren

    Parameters
    ----------

    n : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGNodeUpdater::visitChildren(QSGNode *n)
    self.uglySide.call(
        'ritual_ZN14QSGNodeUpdater13visitChildrenEP7QSGNode',
        self._addressOf(n, 'QSGNode'),
    )
