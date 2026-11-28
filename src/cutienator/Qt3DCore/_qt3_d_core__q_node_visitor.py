"""
Qt3DCore::QNodeVisitor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/6.12.0/Qt3DCore/private/qnodevisitor_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means Qt3DCore::QNodeVisitor to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QNodeVisitor(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DCore::QNodeVisitor: a plain Python object
  standing in front of one C++ Qt3DCore::QNodeVisitor.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QNodeVisitor that has a ritual and that
  Python can call so far, 4 names in all: 'rootNode', 'currentNode',
  'append', 'pop_back'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DCore::QNodeVisitor::~QNodeVisitor()': the destructor: Python
    never removes a C++ Qt3DCore::QNodeVisitor.
  - Qt's 'void Qt3DCore::QNodeVisitor::setPath(QNodeVector path)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QNodeVector Qt3DCore::QNodeVisitor::path() const': gives a type
    Python has no way to take yet.

  What has no ritual
  ------------------

  19 of the 27 functions Qt declares: 17 a template; 2 forbidden.

  What to expect
  --------------

  - The C++ Qt3DCore::QNodeVisitor is created at the first use, not by
    'Qt3DCore::QNodeVisitor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QNodeVisitor.
  - Each name of Qt's Qt3DCore::QNodeVisitor that has no cute function yet,
    'createFunctor', 'outerVisitNode', 'path', 'setPath', 'startTraversing',
    'traverse', 'traverseChildren', 'visitEntity', 'visitNode', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QNodeVisitor'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def rootNode(self) -> Optional[Qt3DCore.QNode]:
    """
    Calls Qt's 'QNode *Qt3DCore::QNodeVisitor::rootNode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qnodevisitor.html#rootNode

    Returns
    -------

    Optional[Qt3DCore.QNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNode *Qt3DCore::QNodeVisitor::rootNode() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore12QNodeVisitor8rootNodeEv',
    )
    return Qt3DCore.QNode._cuteAt(address)

  def currentNode(self) -> Optional[Qt3DCore.QNode]:
    """
    Calls Qt's 'QNode *Qt3DCore::QNodeVisitor::currentNode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qnodevisitor.html#currentNode

    Returns
    -------

    Optional[Qt3DCore.QNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNode *Qt3DCore::QNodeVisitor::currentNode() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore12QNodeVisitor11currentNodeEv',
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'Qt3DCore::QNodeVisitor::QNodeVisitor()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qnodevisitor.html#QNodeVisitor
    """
    #  Qt3DCore::QNodeVisitor::QNodeVisitor()
    self._noteCreation(QNodeVisitor, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore12QNodeVisitorC1Ev',
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
  def append(self, n: Optional[Qt3DCore.QNode]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QNodeVisitor::append(QNode *n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qnodevisitor.html#append

    Parameters
    ----------

    n : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QNodeVisitor::append(QNode *n)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore12QNodeVisitor6appendEPNS_5QNodeE',
        self._addressOf(n),
    )

  def pop_back(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QNodeVisitor::pop_back()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qnodevisitor.html#pop_back
    """
    #  void Qt3DCore::QNodeVisitor::pop_back()
    self.uglySide.call('ritual_ZN8Qt3DCore12QNodeVisitor8pop_backEv')

  @staticmethod
  def createFunctor(*__, **_) -> Never:
    """
    Qt's 'Qt3DCore::QNodeVisitor::createFunctor': a template: a pattern and
    no single function.
    """
    raise NotImplementedError(
        "'Qt3DCore.QNodeVisitor.createFunctor' has no cute function yet. "
        "Qt's 'Qt3DCore::QNodeVisitor::createFunctor': a template: a "
        "pattern and no single function.")

  @staticmethod
  def outerVisitNode(*__, **_) -> Never:
    """
    Qt's 'Qt3DCore::QNodeVisitor::outerVisitNode': a template: a pattern and
    no single function.
    """
    raise NotImplementedError(
        "'Qt3DCore.QNodeVisitor.outerVisitNode' has no cute function yet. "
        "Qt's 'Qt3DCore::QNodeVisitor::outerVisitNode': a template: a "
        "pattern and no single function.")

  @staticmethod
  def path(*__, **_) -> Never:
    """
    Qt's 'QNodeVector Qt3DCore::QNodeVisitor::path() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QNodeVisitor.path' has no cute function yet. Qt's "
        "'QNodeVector Qt3DCore::QNodeVisitor::path() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def setPath(*__, **_) -> Never:
    """
    Qt's 'void Qt3DCore::QNodeVisitor::setPath(QNodeVector path)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QNodeVisitor.setPath' has no cute function yet. Qt's "
        "'void Qt3DCore::QNodeVisitor::setPath(QNodeVector path)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def startTraversing(*__, **_) -> Never:
    """
    Qt's 'Qt3DCore::QNodeVisitor::startTraversing': a template: a pattern and
    no single function.
    """
    raise NotImplementedError(
        "'Qt3DCore.QNodeVisitor.startTraversing' has no cute function yet. "
        "Qt's 'Qt3DCore::QNodeVisitor::startTraversing': a template: a "
        "pattern and no single function.")

  @staticmethod
  def traverse(*__, **_) -> Never:
    """
    Qt's 'Qt3DCore::QNodeVisitor::traverse': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'Qt3DCore.QNodeVisitor.traverse' has no cute function yet. Qt's "
        "'Qt3DCore::QNodeVisitor::traverse': a template: a pattern and no "
        "single function.")

  @staticmethod
  def traverseChildren(*__, **_) -> Never:
    """
    Qt's 'Qt3DCore::QNodeVisitor::traverseChildren': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'Qt3DCore.QNodeVisitor.traverseChildren' has no cute function yet. "
        "Qt's 'Qt3DCore::QNodeVisitor::traverseChildren': a template: a "
        "pattern and no single function.")

  @staticmethod
  def visitEntity(*__, **_) -> Never:
    """
    Qt's 'Qt3DCore::QNodeVisitor::visitEntity': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'Qt3DCore.QNodeVisitor.visitEntity' has no cute function yet. Qt's "
        "'Qt3DCore::QNodeVisitor::visitEntity': a template: a pattern and "
        "no single function.")

  @staticmethod
  def visitNode(*__, **_) -> Never:
    """
    Qt's 'Qt3DCore::QNodeVisitor::visitNode': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'Qt3DCore.QNodeVisitor.visitNode' has no cute function yet. Qt's "
        "'Qt3DCore::QNodeVisitor::visitNode': a template: a pattern and no "
        "single function.")
