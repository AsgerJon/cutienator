"""
QSGNodeVisitor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/qsgnode.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QSGClipNode, QSGGeometryNode, QSGNode, QSGOpacityNode
  from . import QSGTransformNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSGClipNode = WAIT['QSGClipNode']
  QSGGeometryNode = WAIT['QSGGeometryNode']
  QSGNode = WAIT['QSGNode']
  QSGOpacityNode = WAIT['QSGOpacityNode']
  QSGTransformNode = WAIT['QSGTransformNode']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGNodeVisitor(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSGNodeVisitor: a plain Python object standing in
  front of one C++ QSGNodeVisitor.

  C++ hands a QSGNodeVisitor around as a copy, so every C++ QSGNodeVisitor
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSGNodeVisitor that has a ritual and that Python can
  call so far, 10 names in all: 'enterTransformNode', 'leaveTransformNode',
  'enterClipNode', 'leaveClipNode', 'enterGeometryNode', 'leaveGeometryNode',
  'enterOpacityNode', 'leaveOpacityNode', 'visitNode', 'visitChildren'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGNodeVisitor::~QSGNodeVisitor()': the destructor: Python removes
    its C++ QSGNodeVisitor by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSGNodeVisitor is created at the first use, not by
    'QSGNodeVisitor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSGNodeVisitor back gives a copy the ritual made for
    Python, in a new cute QSGNodeVisitor.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGNodeVisitor'

  #  A C++ QSGNodeVisitor Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGNodeVisitor'

  #  The functions Qt calls itself that QSGNodeVisitor is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'enterTransformNode': (
          ('_ZN14QSGNodeVisitor18enterTransformNodeEP16QSGTransformNode',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QSGTransformNode'),
           )),
      ),
      'leaveTransformNode': (
          ('_ZN14QSGNodeVisitor18leaveTransformNodeEP16QSGTransformNode',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QSGTransformNode'),
           )),
      ),
      'enterClipNode': (
          ('_ZN14QSGNodeVisitor13enterClipNodeEP11QSGClipNode',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QSGClipNode'),
           )),
      ),
      'leaveClipNode': (
          ('_ZN14QSGNodeVisitor13leaveClipNodeEP11QSGClipNode',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QSGClipNode'),
           )),
      ),
      'enterGeometryNode': (
          ('_ZN14QSGNodeVisitor17enterGeometryNodeEP15QSGGeometryNode',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QSGGeometryNode'),
           )),
      ),
      'leaveGeometryNode': (
          ('_ZN14QSGNodeVisitor17leaveGeometryNodeEP15QSGGeometryNode',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QSGGeometryNode'),
           )),
      ),
      'enterOpacityNode': (
          ('_ZN14QSGNodeVisitor16enterOpacityNodeEP14QSGOpacityNode',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QSGOpacityNode'),
           )),
      ),
      'leaveOpacityNode': (
          ('_ZN14QSGNodeVisitor16leaveOpacityNodeEP14QSGOpacityNode',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QSGOpacityNode'),
           )),
      ),
      'visitNode': (
          ('_ZN14QSGNodeVisitor9visitNodeEP7QSGNode',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QSGNode'),
           )),
      ),
      'visitChildren': (
          ('_ZN14QSGNodeVisitor13visitChildrenEP7QSGNode',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QSGNode'),
           )),
      ),
  }

  #  Qt's '~QSGNodeVisitor()'. Naming it makes this a value class: Python
  #  owns every C++ QSGNodeVisitor behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QSGNodeVisitorD1Ev'

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

  @overload(QSGTransformNode)
  @overload(NoneType)
  def enterTransformNode(self, a0: Optional[QSGTransformNode]) -> None:
    """
    Calls Qt's 'void QSGNodeVisitor::enterTransformNode(QSGTransformNode
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgnodevisitor.html#enterTransformNode

    Parameters
    ----------

    a0 : Optional[QSGTransformNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGNodeVisitor::enterTransformNode(QSGTransformNode *a0)
    ritual = (
        'ritual_ZN14QSGNodeVisitor18enterTransformNodeEP16QSGTransformNode')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QSGNodeVisitor18enterTransformNodeEP16QSGTransfor'
          'mNode')
    self.uglySide.call(ritual, self._addressOf(a0, 'QSGTransformNode'))

  @overload(QSGTransformNode)
  @overload(NoneType)
  def leaveTransformNode(self, a0: Optional[QSGTransformNode]) -> None:
    """
    Calls Qt's 'void QSGNodeVisitor::leaveTransformNode(QSGTransformNode
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgnodevisitor.html#leaveTransformNode

    Parameters
    ----------

    a0 : Optional[QSGTransformNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGNodeVisitor::leaveTransformNode(QSGTransformNode *a0)
    ritual = (
        'ritual_ZN14QSGNodeVisitor18leaveTransformNodeEP16QSGTransformNode')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QSGNodeVisitor18leaveTransformNodeEP16QSGTransfor'
          'mNode')
    self.uglySide.call(ritual, self._addressOf(a0, 'QSGTransformNode'))

  @overload(QSGClipNode)
  @overload(NoneType)
  def enterClipNode(self, a0: Optional[QSGClipNode]) -> None:
    """
    Calls Qt's 'void QSGNodeVisitor::enterClipNode(QSGClipNode *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnodevisitor.html#enterClipNode

    Parameters
    ----------

    a0 : Optional[QSGClipNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGNodeVisitor::enterClipNode(QSGClipNode *a0)
    ritual = 'ritual_ZN14QSGNodeVisitor13enterClipNodeEP11QSGClipNode'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QSGNodeVisitor13enterClipNodeEP11QSGClipNode'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QSGClipNode)
  @overload(NoneType)
  def leaveClipNode(self, a0: Optional[QSGClipNode]) -> None:
    """
    Calls Qt's 'void QSGNodeVisitor::leaveClipNode(QSGClipNode *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnodevisitor.html#leaveClipNode

    Parameters
    ----------

    a0 : Optional[QSGClipNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGNodeVisitor::leaveClipNode(QSGClipNode *a0)
    ritual = 'ritual_ZN14QSGNodeVisitor13leaveClipNodeEP11QSGClipNode'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QSGNodeVisitor13leaveClipNodeEP11QSGClipNode'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QSGGeometryNode)
  @overload(NoneType)
  def enterGeometryNode(self, a0: Optional[QSGGeometryNode]) -> None:
    """
    Calls Qt's 'void QSGNodeVisitor::enterGeometryNode(QSGGeometryNode *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgnodevisitor.html#enterGeometryNode

    Parameters
    ----------

    a0 : Optional[QSGGeometryNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGNodeVisitor::enterGeometryNode(QSGGeometryNode *a0)
    ritual = (
        'ritual_ZN14QSGNodeVisitor17enterGeometryNodeEP15QSGGeometryNode')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QSGNodeVisitor17enterGeometryNodeEP15QSGGeometryN'
          'ode')
    self.uglySide.call(ritual, self._addressOf(a0, 'QSGGeometryNode'))

  @overload(QSGGeometryNode)
  @overload(NoneType)
  def leaveGeometryNode(self, a0: Optional[QSGGeometryNode]) -> None:
    """
    Calls Qt's 'void QSGNodeVisitor::leaveGeometryNode(QSGGeometryNode *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgnodevisitor.html#leaveGeometryNode

    Parameters
    ----------

    a0 : Optional[QSGGeometryNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGNodeVisitor::leaveGeometryNode(QSGGeometryNode *a0)
    ritual = (
        'ritual_ZN14QSGNodeVisitor17leaveGeometryNodeEP15QSGGeometryNode')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QSGNodeVisitor17leaveGeometryNodeEP15QSGGeometryN'
          'ode')
    self.uglySide.call(ritual, self._addressOf(a0, 'QSGGeometryNode'))

  @overload(QSGOpacityNode)
  @overload(NoneType)
  def enterOpacityNode(self, a0: Optional[QSGOpacityNode]) -> None:
    """
    Calls Qt's 'void QSGNodeVisitor::enterOpacityNode(QSGOpacityNode *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgnodevisitor.html#enterOpacityNode

    Parameters
    ----------

    a0 : Optional[QSGOpacityNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGNodeVisitor::enterOpacityNode(QSGOpacityNode *a0)
    ritual = 'ritual_ZN14QSGNodeVisitor16enterOpacityNodeEP14QSGOpacityNode'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QSGNodeVisitor16enterOpacityNodeEP14QSGOpacityNod'
          'e')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QSGOpacityNode)
  @overload(NoneType)
  def leaveOpacityNode(self, a0: Optional[QSGOpacityNode]) -> None:
    """
    Calls Qt's 'void QSGNodeVisitor::leaveOpacityNode(QSGOpacityNode *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgnodevisitor.html#leaveOpacityNode

    Parameters
    ----------

    a0 : Optional[QSGOpacityNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGNodeVisitor::leaveOpacityNode(QSGOpacityNode *a0)
    ritual = 'ritual_ZN14QSGNodeVisitor16leaveOpacityNodeEP14QSGOpacityNode'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QSGNodeVisitor16leaveOpacityNodeEP14QSGOpacityNod'
          'e')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QSGNode)
  @overload(NoneType)
  def visitNode(self, n: Optional[QSGNode]) -> None:
    """
    Calls Qt's 'void QSGNodeVisitor::visitNode(QSGNode *n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnodevisitor.html#visitNode

    Parameters
    ----------

    n : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGNodeVisitor::visitNode(QSGNode *n)
    ritual = 'ritual_ZN14QSGNodeVisitor9visitNodeEP7QSGNode'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QSGNodeVisitor9visitNodeEP7QSGNode'
    self.uglySide.call(ritual, self._addressOf(n, 'QSGNode'))

  @overload(QSGNode)
  @overload(NoneType)
  def visitChildren(self, n: Optional[QSGNode]) -> None:
    """
    Calls Qt's 'void QSGNodeVisitor::visitChildren(QSGNode *n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnodevisitor.html#visitChildren

    Parameters
    ----------

    n : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGNodeVisitor::visitChildren(QSGNode *n)
    ritual = 'ritual_ZN14QSGNodeVisitor13visitChildrenEP7QSGNode'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QSGNodeVisitor13visitChildrenEP7QSGNode'
    self.uglySide.call(ritual, self._addressOf(n, 'QSGNode'))
