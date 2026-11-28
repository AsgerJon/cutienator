"""
Qt3DRender::QShaderGraph binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qshadergraph_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DRender::QShaderGraph to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..QtCore import QStringList
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QUuid


class QShaderGraph(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DRender::QShaderGraph: a plain Python object
  standing in front of one C++ Qt3DRender::QShaderGraph.

  C++ hands a Qt3DRender::QShaderGraph around as a copy, so every C++
  Qt3DRender::QShaderGraph behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QShaderGraph that has a ritual and that
  Python can call so far, 4 names in all: 'addNode', 'removeNode', 'addEdge',
  'removeEdge'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QList<QShaderNode> Qt3DRender::QShaderGraph::nodes() const': gives
    a type Python has no way to take yet.
  - Qt's 'QList<Edge> Qt3DRender::QShaderGraph::edges() const': gives a type
    Python has no way to take yet.
  - Qt's 'QList<Statement> Qt3DRender::QShaderGraph::createStatements(const
    QStringList &enabledLayers) const': gives a type Python has no way to
    take yet.
  - Qt's 'Qt3DRender::QShaderGraph::~QShaderGraph()': the destructor: Python
    removes its C++ Qt3DRender::QShaderGraph by it, and has no other use for
    it.

  What to expect
  --------------

  - The C++ Qt3DRender::QShaderGraph is created at the first use, not by
    'Qt3DRender::QShaderGraph(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DRender::QShaderGraph back gives a copy the ritual
    made for Python, in a new cute Qt3DRender::QShaderGraph.
  - Each name of Qt's Qt3DRender::QShaderGraph that has no cute function yet,
    'createStatements', 'edges', 'nodes', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside Qt3DRender::QShaderGraph, each a class in
  #  here as in C++.

  class Edge(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's Qt3DRender::QShaderGraph::Edge: a plain Python
    object standing in front of one C++ Qt3DRender::QShaderGraph::Edge.

    C++ hands a Qt3DRender::QShaderGraph::Edge around as a copy, so every C++
    Qt3DRender::QShaderGraph::Edge behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's Qt3DRender::QShaderGraph::Edge yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'Qt3DRender::QShaderGraph::Edge::~Edge()': the destructor: Python
      removes its C++ Qt3DRender::QShaderGraph::Edge by it, and has no other
      use for it.

    What to expect
    --------------

    - The C++ Qt3DRender::QShaderGraph::Edge is created at the first use, not
      by 'Qt3DRender::QShaderGraph::Edge(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a Qt3DRender::QShaderGraph::Edge back gives a copy
      the ritual made for Python, in a new cute
      Qt3DRender::QShaderGraph::Edge.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'Qt3DRender::QShaderGraph::Edge'

    #  Qt's '~Qt3DRender::QShaderGraph::Edge()'. Naming it makes this a value
    #  class: Python owns every C++ Qt3DRender::QShaderGraph::Edge behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN10Qt3DRender12QShaderGraph4EdgeD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  class Statement(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's Qt3DRender::QShaderGraph::Statement: a plain Python
    object standing in front of one C++ Qt3DRender::QShaderGraph::Statement.

    C++ hands a Qt3DRender::QShaderGraph::Statement around as a copy, so
    every C++ Qt3DRender::QShaderGraph::Statement behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's Qt3DRender::QShaderGraph::Statement that has a
    ritual and that Python can call so far, 2 names in all: 'uuid',
    'portIndex'. None can be made from Python: one comes out of a function of
    another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'Qt3DRender::QShaderGraph::Statement::~Statement()': the
      destructor: Python removes its C++ Qt3DRender::QShaderGraph::Statement
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ Qt3DRender::QShaderGraph::Statement is created at the first
      use, not by 'Qt3DRender::QShaderGraph::Statement(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a Qt3DRender::QShaderGraph::Statement back gives a
      copy the ritual made for Python, in a new cute
      Qt3DRender::QShaderGraph::Statement.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'Qt3DRender::QShaderGraph::Statement'

    #  Qt's '~Qt3DRender::QShaderGraph::Statement()'. Naming it makes this a
    #  value class: Python owns every C++ Qt3DRender::QShaderGraph::Statement
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN10Qt3DRender12QShaderGraph9StatementD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def uuid(self) -> QUuid:
      """
      Calls Qt's 'QUuid Qt3DRender::QShaderGraph::Statement::uuid() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qt3drender-qshadergraph-statement.html#uuid

      Returns
      -------

      QUuid
        A new cute QUuid around the copy Qt gave back. Python owns it.
      """
      #  QUuid Qt3DRender::QShaderGraph::Statement::uuid() const
      address = self.uglySide.call(
          'ritual_ZNK10Qt3DRender12QShaderGraph9Statement4uuidEv',
      )
      from ..QtCore import QUuid
      return QUuid._cuteOwning(address)

    @overload(Qt3DRender.QShaderNodePort.Direction, str)
    def portIndex(
        self,
        direction: Qt3DRender.QShaderNodePort.Direction,
        portName: str,
    ) -> int:
      """
      Calls Qt's 'int
      Qt3DRender::QShaderGraph::Statement::portIndex(QShaderNodePort::
      Direction direction, const QString &portName) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qt3drender-qshadergraph-statement.html#portIndex

      Parameters
      ----------

      direction : Qt3DRender.QShaderNodePort.Direction
        Passed on as its number.

      portName : str
        Passed on as it is: a QString is made of it for the call.
      """
      #  int Qt3DRender::QShaderGraph::Statement::portIndex(
      #      QShaderNodePort::Direction direction, const QString &portName)
      #      const
      return self.uglySide.call(
          'ritual_ZNK10Qt3DRender12QShaderGraph9Statement9portIndexENS_15QS'
          'haderNodePort9DirectionERK7QString',
          direction.value, portName,
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
  __qt_class__ = 'Qt3DRender::QShaderGraph'

  #  Qt's '~Qt3DRender::QShaderGraph()'. Naming it makes this a value class:
  #  Python owns every C++ Qt3DRender::QShaderGraph behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10Qt3DRender12QShaderGraphD1Ev'

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

  @overload(WAIT['Qt3DRender.QShaderNode'])
  def addNode(self, node: Qt3DRender.QShaderNode) -> None:
    """
    Calls Qt's 'void Qt3DRender::QShaderGraph::addNode(const QShaderNode
    &node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshadergraph.html#addNode

    Parameters
    ----------

    node : Qt3DRender.QShaderNode
      Passed on as a value: Qt reads the C++ Qt3DRender::QShaderNode, which
      stays Python's own.
    """
    #  void Qt3DRender::QShaderGraph::addNode(const QShaderNode &node)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender12QShaderGraph7addNodeERKNS_11QShaderNodeE',
        self._valueOf(node),
    )

  @overload(WAIT['Qt3DRender.QShaderNode'])
  def removeNode(self, node: Qt3DRender.QShaderNode) -> None:
    """
    Calls Qt's 'void Qt3DRender::QShaderGraph::removeNode(const QShaderNode
    &node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshadergraph.html#removeNode

    Parameters
    ----------

    node : Qt3DRender.QShaderNode
      Passed on as a value: Qt reads the C++ Qt3DRender::QShaderNode, which
      stays Python's own.
    """
    #  void Qt3DRender::QShaderGraph::removeNode(const QShaderNode &node)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender12QShaderGraph10removeNodeERKNS_11QShaderNode'
        'E',
        self._valueOf(node),
    )

  @overload(Edge)
  def addEdge(self, edge: Edge) -> None:
    """
    Calls Qt's 'void Qt3DRender::QShaderGraph::addEdge(const Edge &edge)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshadergraph.html#addEdge

    Parameters
    ----------

    edge : Edge
      Passed on as a value: Qt reads the C++ Qt3DRender::QShaderGraph::Edge,
      which stays Python's own.
    """
    #  void Qt3DRender::QShaderGraph::addEdge(const Edge &edge)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender12QShaderGraph7addEdgeERKNS0_4EdgeE',
        self._valueOf(edge),
    )

  @overload(Edge)
  def removeEdge(self, edge: Edge) -> None:
    """
    Calls Qt's 'void Qt3DRender::QShaderGraph::removeEdge(const Edge &edge)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshadergraph.html#removeEdge

    Parameters
    ----------

    edge : Edge
      Passed on as a value: Qt reads the C++ Qt3DRender::QShaderGraph::Edge,
      which stays Python's own.
    """
    #  void Qt3DRender::QShaderGraph::removeEdge(const Edge &edge)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender12QShaderGraph10removeEdgeERKNS0_4EdgeE',
        self._valueOf(edge),
    )

  @staticmethod
  def createStatements(*__, **_) -> Never:
    """
    Qt's 'QList<Statement> Qt3DRender::QShaderGraph::createStatements(const
    QStringList &enabledLayers) const': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QShaderGraph.createStatements' has no cute function "
        "yet. Qt's 'QList<Statement> "
        "Qt3DRender::QShaderGraph::createStatements(const QStringList "
        "&enabledLayers) const': gives a type Python has no way to take yet."
    )

  @staticmethod
  def edges(*__, **_) -> Never:
    """
    Qt's 'QList<Edge> Qt3DRender::QShaderGraph::edges() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QShaderGraph.edges' has no cute function yet. Qt's "
        "'QList<Edge> Qt3DRender::QShaderGraph::edges() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def nodes(*__, **_) -> Never:
    """
    Qt's 'QList<QShaderNode> Qt3DRender::QShaderGraph::nodes() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QShaderGraph.nodes' has no cute function yet. Qt's "
        "'QList<QShaderNode> Qt3DRender::QShaderGraph::nodes() const': "
        "gives a type Python has no way to take yet.")
