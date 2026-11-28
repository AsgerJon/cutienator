"""
QWingedEdge binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qpathclipper_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QWingedEdge to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QPathEdge

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPointF
  from . import QPathVertex
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPathVertex = WAIT['QPathVertex']
  QPointF = WAIT['QPointF']


class QWingedEdge(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWingedEdge: a plain Python object standing in front
  of one C++ QWingedEdge.

  What exists
  -----------

  Every function of Qt's QWingedEdge that has a ritual and that Python can
  call so far, 14 names in all: 'simplify', 'edgeCount', 'edge',
  'vertexCount', 'addVertex', 'vertex', 'next', 'addEdge', 'isInside',
  'flip', 'removeEdge', 'insert', 'findInsertStatus', 'delta'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QPathEdge *QWingedEdge::edge(int edge) const': takes in
    Python what 'QPathEdge *QWingedEdge::edge(int edge)' takes.
  - Qt's 'const QPathVertex *QWingedEdge::vertex(int vertex) const': takes in
    Python what 'QPathVertex *QWingedEdge::vertex(int vertex)' takes.

  What has no ritual
  ------------------

  4 of the 23 functions Qt declares: 2 leans on 'QPathSegments; 1 not a gap;
  1 Qt's library has no name for it, and its code in Qt's source does not
  compile apart from its file.

  What to expect
  --------------

  - The C++ QWingedEdge is created at the first use, not by
    'QWingedEdge(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWingedEdge.
  - Each name of Qt's QWingedEdge that has no cute function yet,
    'intersectAndAdd', 'toPath', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QWingedEdge, each a class in here as in
  #  C++.

  class TraversalStatus(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QWingedEdge::TraversalStatus: a plain Python object
    standing in front of one C++ QWingedEdge::TraversalStatus.

    C++ hands a QWingedEdge::TraversalStatus around as a copy, so every C++
    QWingedEdge::TraversalStatus behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QWingedEdge::TraversalStatus that has a ritual and
    that Python can call so far, 3 names in all: 'flipDirection',
    'flipTraversal', 'flip'. None can be made from Python: one comes out of a
    function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QWingedEdge::TraversalStatus::~TraversalStatus()': the
      destructor: Python removes its C++ QWingedEdge::TraversalStatus by it,
      and has no other use for it.

    What to expect
    --------------

    - The C++ QWingedEdge::TraversalStatus is created at the first use, not
      by 'QWingedEdge::TraversalStatus(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QWingedEdge::TraversalStatus back gives a copy the
      ritual made for Python, in a new cute QWingedEdge::TraversalStatus.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QWingedEdge::TraversalStatus'

    #  Qt's '~QWingedEdge::TraversalStatus()'. Naming it makes this a value
    #  class: Python owns every C++ QWingedEdge::TraversalStatus behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN11QWingedEdge15TraversalStatusD1Ev'

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

    def flipDirection(self) -> None:
      """
      Calls Qt's 'void QWingedEdge::TraversalStatus::flipDirection()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qwingededge-traversalstatus.html#flipDirection
      """
      #  void QWingedEdge::TraversalStatus::flipDirection()
      self.uglySide.call(
          'ritual_ZN11QWingedEdge15TraversalStatus13flipDirectionEv',
      )

    def flipTraversal(self) -> None:
      """
      Calls Qt's 'void QWingedEdge::TraversalStatus::flipTraversal()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qwingededge-traversalstatus.html#flipTraversal
      """
      #  void QWingedEdge::TraversalStatus::flipTraversal()
      self.uglySide.call(
          'ritual_ZN11QWingedEdge15TraversalStatus13flipTraversalEv',
      )

    def flip(self) -> None:
      """
      Calls Qt's 'void QWingedEdge::TraversalStatus::flip()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qwingededge-traversalstatus.html#flip
      """
      #  void QWingedEdge::TraversalStatus::flip()
      self.uglySide.call('ritual_ZN11QWingedEdge15TraversalStatus4flipEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QPathEdge.Traversal)
  def flip(traversal: QPathEdge.Traversal) -> QPathEdge.Traversal:
    """
    Calls Qt's 'QPathEdge::Traversal QWingedEdge::flip(QPathEdge::Traversal
    traversal)'.

    Qt's own words: https://doc.qt.io/qt-6/qwingededge.html#flip

    Parameters
    ----------

    traversal : QPathEdge.Traversal
      Passed on as its number.

    Returns
    -------

    QPathEdge.Traversal
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QPathEdge.Traversal(number)' gives.
    """
    #  QPathEdge::Traversal QWingedEdge::flip(QPathEdge::Traversal traversal)
    return QPathEdge.Traversal(Rituals.call(
        'ritual_ZN11QWingedEdge4flipEN9QPathEdge9TraversalE',
        traversal.value,
    ))

  @staticmethod
  @overload(QPathEdge.Direction)
  def flip(direction: QPathEdge.Direction) -> QPathEdge.Direction:
    """
    Calls Qt's 'QPathEdge::Direction QWingedEdge::flip(QPathEdge::Direction
    direction)'.

    Qt's own words: https://doc.qt.io/qt-6/qwingededge.html#flip

    Parameters
    ----------

    direction : QPathEdge.Direction
      Passed on as its number.

    Returns
    -------

    QPathEdge.Direction
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QPathEdge.Direction(number)' gives.
    """
    #  QPathEdge::Direction QWingedEdge::flip(QPathEdge::Direction direction)
    return QPathEdge.Direction(Rituals.call(
        'ritual_ZN11QWingedEdge4flipEN9QPathEdge9DirectionE',
        direction.value,
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWingedEdge'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def edgeCount(self) -> int:
    """
    Calls Qt's 'int QWingedEdge::edgeCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwingededge.html#edgeCount
    """
    #  int QWingedEdge::edgeCount() const
    return self.uglySide.call('ritual_ZNK11QWingedEdge9edgeCountEv')

  def vertexCount(self) -> int:
    """
    Calls Qt's 'int QWingedEdge::vertexCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwingededge.html#vertexCount
    """
    #  int QWingedEdge::vertexCount() const
    return self.uglySide.call('ritual_ZNK11QWingedEdge11vertexCountEv')

  @overload(TraversalStatus)
  def next(self, status: TraversalStatus) -> TraversalStatus:
    """
    Calls Qt's 'TraversalStatus QWingedEdge::next(const TraversalStatus
    &status) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwingededge.html#next

    Parameters
    ----------

    status : TraversalStatus
      Passed on as a value: Qt reads the C++ QWingedEdge::TraversalStatus,
      which stays Python's own.

    Returns
    -------

    TraversalStatus
      A new cute QWingedEdge::TraversalStatus around the copy Qt gave back.
      Python owns it.
    """
    #  TraversalStatus QWingedEdge::next(const TraversalStatus &status) const
    address = self.uglySide.call(
        'ritual_ZNK11QWingedEdge4nextERKNS_15TraversalStatusE',
        self._valueOf(status),
    )
    return QWingedEdge.TraversalStatus._cuteOwning(address)

  @overload(float, float)
  def isInside(self, x: float, y: float) -> bool:
    """
    Calls Qt's 'bool QWingedEdge::isInside(qreal x, qreal y) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwingededge.html#isInside

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  bool QWingedEdge::isInside(qreal x, qreal y) const
    return self.uglySide.call('ritual_ZNK11QWingedEdge8isInsideEdd', x, y)

  @overload(int, int)
  def findInsertStatus(self, vertex: int, edge: int) -> TraversalStatus:
    """
    Calls Qt's 'TraversalStatus QWingedEdge::findInsertStatus(int vertex, int
    edge) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwingededge.html#findInsertStatus

    Parameters
    ----------

    vertex : int
      Passed on as it is.

    edge : int
      Passed on as it is.

    Returns
    -------

    TraversalStatus
      A new cute QWingedEdge::TraversalStatus around the copy Qt gave back.
      Python owns it.
    """
    #  TraversalStatus QWingedEdge::findInsertStatus(int vertex, int edge)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK11QWingedEdge16findInsertStatusEii', vertex, edge,
    )
    return QWingedEdge.TraversalStatus._cuteOwning(address)

  @overload(int, int, int)
  def delta(self, vertex: int, a: int, b: int) -> float:
    """
    Calls Qt's 'qreal QWingedEdge::delta(int vertex, int a, int b) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwingededge.html#delta

    Parameters
    ----------

    vertex : int
      Passed on as it is.

    a : int
      Passed on as it is.

    b : int
      Passed on as it is.
    """
    #  qreal QWingedEdge::delta(int vertex, int a, int b) const
    return self.uglySide.call(
        'ritual_ZNK11QWingedEdge5deltaEiii', vertex, a, b,
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
    Notes what was given, for Qt's 'QWingedEdge::QWingedEdge()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qwingededge.html#QWingedEdge
    """
    #  QWingedEdge::QWingedEdge()
    self._noteCreation(QWingedEdge, lambda: Rituals.call(
        'ritual_ZN11QWingedEdgeC1Ev',
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

  def simplify(self) -> None:
    """
    Calls Qt's 'void QWingedEdge::simplify()'.

    Qt's own words: https://doc.qt.io/qt-6/qwingededge.html#simplify
    """
    #  void QWingedEdge::simplify()
    self.uglySide.call('ritual_ZN11QWingedEdge8simplifyEv')

  @overload(int)
  def edge(self, edge: int) -> Optional[QPathEdge]:
    """
    Calls Qt's 'QPathEdge *QWingedEdge::edge(int edge)'.

    Qt's own words: https://doc.qt.io/qt-6/qwingededge.html#edge

    Parameters
    ----------

    edge : int
      Passed on as it is.

    Returns
    -------

    Optional[QPathEdge]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPathEdge *QWingedEdge::edge(int edge)
    address = self.uglySide.call('ritual_ZN11QWingedEdge4edgeEi', edge)
    return QPathEdge._cuteAt(address)

  @overload(QPointF)
  def addVertex(self, p: QPointF) -> int:
    """
    Calls Qt's 'int QWingedEdge::addVertex(const QPointF &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qwingededge.html#addVertex

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  int QWingedEdge::addVertex(const QPointF &p)
    return self.uglySide.call(
        'ritual_ZN11QWingedEdge9addVertexERK7QPointF',
        self._valueOf(p, 'QPointF'),
    )

  @overload(int)
  def vertex(self, vertex: int) -> Optional[QPathVertex]:
    """
    Calls Qt's 'QPathVertex *QWingedEdge::vertex(int vertex)'.

    Qt's own words: https://doc.qt.io/qt-6/qwingededge.html#vertex

    Parameters
    ----------

    vertex : int
      Passed on as it is.

    Returns
    -------

    Optional[QPathVertex]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPathVertex *QWingedEdge::vertex(int vertex)
    address = self.uglySide.call('ritual_ZN11QWingedEdge6vertexEi', vertex)
    from . import QPathVertex
    return QPathVertex._cuteAt(address)

  @overload(QPointF, QPointF)
  def addEdge(self, a: QPointF, b: QPointF) -> int:
    """
    Calls Qt's 'int QWingedEdge::addEdge(const QPointF &a, const QPointF
    &b)'.

    Qt's own words: https://doc.qt.io/qt-6/qwingededge.html#addEdge

    Parameters
    ----------

    a : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    b : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  int QWingedEdge::addEdge(const QPointF &a, const QPointF &b)
    return self.uglySide.call(
        'ritual_ZN11QWingedEdge7addEdgeERK7QPointFS2_',
        self._valueOf(a, 'QPointF'), self._valueOf(b, 'QPointF'),
    )

  @overload(int, int)
  def addEdge(self, vertexA: int, vertexB: int) -> int:
    """
    Calls Qt's 'int QWingedEdge::addEdge(int vertexA, int vertexB)'.

    Qt's own words: https://doc.qt.io/qt-6/qwingededge.html#addEdge

    Parameters
    ----------

    vertexA : int
      Passed on as it is.

    vertexB : int
      Passed on as it is.
    """
    #  int QWingedEdge::addEdge(int vertexA, int vertexB)
    return self.uglySide.call(
        'ritual_ZN11QWingedEdge7addEdgeEii', vertexA, vertexB,
    )

  @overload(int)
  def removeEdge(self, ei: int) -> None:
    """
    Calls Qt's 'void QWingedEdge::removeEdge(int ei)'.

    Qt's own words: https://doc.qt.io/qt-6/qwingededge.html#removeEdge

    Parameters
    ----------

    ei : int
      Passed on as it is.
    """
    #  void QWingedEdge::removeEdge(int ei)
    self.uglySide.call('ritual_ZN11QWingedEdge10removeEdgeEi', ei)

  @overload(QPathVertex)
  def insert(self, vertex: QPathVertex) -> int:
    """
    Calls Qt's 'int QWingedEdge::insert(const QPathVertex &vertex)'.

    Qt's own words: https://doc.qt.io/qt-6/qwingededge.html#insert

    Parameters
    ----------

    vertex : QPathVertex
      Passed on as a value: Qt reads the C++ QPathVertex, which stays
      Python's own.
    """
    #  int QWingedEdge::insert(const QPathVertex &vertex)
    return self.uglySide.call(
        'ritual_ZN11QWingedEdge6insertERK11QPathVertex',
        self._valueOf(vertex),
    )

  @staticmethod
  def intersectAndAdd(*__, **_) -> Never:
    """
    Qt's 'void QWingedEdge::intersectAndAdd()': leans on
    'QPathSegments::mergePoints()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QWingedEdge.intersectAndAdd' has no cute function yet. Qt's 'void "
        "QWingedEdge::intersectAndAdd()': leans on "
        "'QPathSegments::mergePoints()', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def toPath(*__, **_) -> Never:
    """
    Qt's 'QPainterPath QWingedEdge::toPath() const': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'add'.
    """
    raise NotImplementedError(
        "'QWingedEdge.toPath' has no cute function yet. Qt's 'QPainterPath "
        "QWingedEdge::toPath() const': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'add'.")
