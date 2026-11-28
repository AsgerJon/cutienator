"""
QGraphicsAnchorLayoutPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qgraphicsanchorlayout_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGraphicsAnchorLayoutPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QGraphicsLayoutPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRectF
  from . import QGraphicsAnchor, QGraphicsAnchorLayout, QGraphicsLayoutItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGraphicsAnchorLayout = WAIT['QGraphicsAnchorLayout']
  QGraphicsLayoutItem = WAIT['QGraphicsLayoutItem']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsAnchorLayoutPrivate(QGraphicsLayoutPrivate):
  """
  The cute side of Qt's QGraphicsAnchorLayoutPrivate: a plain Python object
  standing in front of one C++ QGraphicsAnchorLayoutPrivate.

  It is built on the cute 'QGraphicsLayoutPrivate', as Qt's
  QGraphicsAnchorLayoutPrivate is built on Qt's QGraphicsLayoutPrivate, and
  has everything that class has.

  C++ hands a QGraphicsAnchorLayoutPrivate around as a copy, so every C++
  QGraphicsAnchorLayoutPrivate behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QGraphicsAnchorLayoutPrivate that has a ritual and
  that Python can call so far, 15 names in all: 'q_func', 'get',
  'oppositeEdge', 'edgeOrientation', 'pickEdge', 'removeCenterConstraints',
  'getAnchor', 'restoreSimplifiedGraph', 'findPaths', 'updateAnchorSizes',
  'getGraphParts', 'setItemsGeometries', 'calculateVertexPositions',
  'setupEdgesInterpolation', 'dumpGraph'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QGraphicsAnchorLayout *QGraphicsAnchorLayoutPrivate::q_func()
    const': takes in Python what 'QGraphicsAnchorLayout
    *QGraphicsAnchorLayoutPrivate::q_func()' takes.
  - Qt's 'QGraphicsAnchor
    *QGraphicsAnchorLayoutPrivate::acquireGraphicsAnchor(AnchorData *data)':
    names 'AnchorData', which has no cute class yet.
  - Qt's 'QLayoutStyleInfo &QGraphicsAnchorLayoutPrivate::styleInfo() const':
    gives a type Python has no way to take yet.
  - Qt's 'void
    QGraphicsAnchorLayoutPrivate::restoreSimplifiedAnchor(AnchorData *edge)':
    names 'AnchorData', which has no cute class yet.
  - Qt's 'void QGraphicsAnchorLayoutPrivate::restoreSimplifiedConstraints(
    ParallelAnchorData *parallel)': names 'ParallelAnchorData', which has no
    cute class yet.
  - Qt's 'void QGraphicsAnchorLayoutPrivate::identifyFloatItems(const
    QSet<AnchorData *> &visited, Qt::Orientation orientation)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void
    QGraphicsAnchorLayoutPrivate::identifyNonFloatItems_helper(const
    AnchorData *ad, QSet<QGraphicsLayoutItem *>
    *nonFloatingItemsIdentifiedSoFar)': names 'AnchorData', which has no cute
    class yet.
  - Qt's 'AnchorVertex *QGraphicsAnchorLayoutPrivate::internalVertex(const
    std::pair<QGraphicsLayoutItem *, Qt::AnchorPoint> &itemEdge) const':
    takes a type Python has no way to hand over yet.
  - Qt's 'AnchorVertex *QGraphicsAnchorLayoutPrivate::internalVertex(const
    QGraphicsLayoutItem *item, Qt::AnchorPoint edge) const': gives
    'AnchorVertex', which has no cute class yet.
  - Qt's 'void
    QGraphicsAnchorLayoutPrivate::changeLayoutVertex(Qt::Orientation
    orientation, AnchorVertex *oldV, AnchorVertex *newV)': names
    'AnchorVertex', which has no cute class yet.
  - Qt's 'AnchorVertex
    *QGraphicsAnchorLayoutPrivate::addInternalVertex(QGraphicsLayoutItem
    *item, Qt::AnchorPoint edge)': gives 'AnchorVertex', which has no cute
    class yet.
  - Qt's 'void QGraphicsAnchorLayoutPrivate::interpolateEdge(AnchorVertex
    *base, AnchorData *edge)': names 'AnchorVertex', which has no cute class
    yet.
  - Qt's 'QGraphicsAnchorLayoutPrivate::~QGraphicsAnchorLayoutPrivate()': the
    destructor: Python removes its C++ QGraphicsAnchorLayoutPrivate by it,
    and has no other use for it.

  What has no ritual
  ------------------

  29 of the 58 functions Qt declares: 21 leans on 'QtGraphicsAnchorLayout; 7
  Qt's library has no name for it, and its code in Qt's source does not
  compile apart from its file; 1 takes or gives a type that cannot be passed
  yet.

  What to expect
  --------------

  - The C++ QGraphicsAnchorLayoutPrivate is created at the first use, not by
    'QGraphicsAnchorLayoutPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGraphicsAnchorLayoutPrivate back gives a copy the
    ritual made for Python, in a new cute QGraphicsAnchorLayoutPrivate.
  - Each name of Qt's QGraphicsAnchorLayoutPrivate that has no cute function
    yet, 'acquireGraphicsAnchor', 'addAnchor', 'addAnchorMaybeParallel',
    'addAnchor_helper', 'addInternalVertex', 'calculateGraphs',
    'calculateNonTrunk', 'calculateTrunk', 'changeLayoutVertex',
    'constraintsFromPaths', 'constraintsFromSizeHints',
    'correctEdgeDirection', 'createCenterAnchors', 'createItemEdges',
    'createLayoutEdges', 'deleteLayoutEdges', 'hasConflicts',
    'identifyFloatItems', 'identifyNonFloatItems_helper', 'internalVertex',
    'interpolateEdge', 'refreshAllSizeHints', 'removeAnchor',
    'removeAnchor_helper', 'removeAnchors', 'removeCenterAnchors',
    'removeInternalVertex', 'removeVertex', 'replaceVertex',
    'restoreSimplifiedAnchor', 'restoreSimplifiedConstraints',
    'restoreVertices', 'simplifyGraph', 'simplifyGraphIteration',
    'simplifyVertices', 'solveMinMax', 'solvePreferred', 'styleInfo', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QGraphicsAnchorLayoutPrivate, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Interval(CuteNum):
    """
    The enum 'QGraphicsAnchorLayoutPrivate::Interval' of Qt, with the 4 names
    Qt gives in it.
    """

    MinimumToMinPreferred = Kee[int](0)
    MinPreferredToPreferred = Kee[int](1)
    PreferredToMaxPreferred = Kee[int](2)
    MaxPreferredToMaximum = Kee[int](3)

  #  The classes Qt writes inside QGraphicsAnchorLayoutPrivate, each a class
  #  in here as in C++.

  class GraphParts(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QGraphicsAnchorLayoutPrivate::GraphParts: a plain
    Python object standing in front of one C++
    QGraphicsAnchorLayoutPrivate::GraphParts.

    C++ hands a QGraphicsAnchorLayoutPrivate::GraphParts around as a copy, so
    every C++ QGraphicsAnchorLayoutPrivate::GraphParts behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QGraphicsAnchorLayoutPrivate::GraphParts yet. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QGraphicsAnchorLayoutPrivate::GraphParts::~GraphParts()': the
      destructor: Python removes its C++
      QGraphicsAnchorLayoutPrivate::GraphParts by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QGraphicsAnchorLayoutPrivate::GraphParts is created at the
      first use, not by 'QGraphicsAnchorLayoutPrivate::GraphParts(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QGraphicsAnchorLayoutPrivate::GraphParts back gives
      a copy the ritual made for Python, in a new cute
      QGraphicsAnchorLayoutPrivate::GraphParts.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QGraphicsAnchorLayoutPrivate::GraphParts'

    #  Qt's '~QGraphicsAnchorLayoutPrivate::GraphParts()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QGraphicsAnchorLayoutPrivate::GraphParts behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN28QGraphicsAnchorLayoutPrivate10GraphPartsD1Ev')

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QGraphicsAnchorLayout)
  @overload(NoneType)
  def get(
      q: Optional[QGraphicsAnchorLayout],
  ) -> Optional[QGraphicsAnchorLayoutPrivate]:
    """
    Calls Qt's 'QGraphicsAnchorLayoutPrivate
    *QGraphicsAnchorLayoutPrivate::get(QGraphicsAnchorLayout *q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsanchorlayoutprivate.html#get

    Parameters
    ----------

    q : Optional[QGraphicsAnchorLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QGraphicsAnchorLayoutPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsAnchorLayoutPrivate
    #      *QGraphicsAnchorLayoutPrivate::get(QGraphicsAnchorLayout *q)
    address = Rituals.call(
        'ritual_ZN28QGraphicsAnchorLayoutPrivate3getEP21QGraphicsAnchorLayo'
        'ut',
        CuteMixin._addressOf(q),
    )
    return QGraphicsAnchorLayoutPrivate._cuteAt(address)

  @staticmethod
  @overload(Qt.AnchorPoint)
  def oppositeEdge(edge: Qt.AnchorPoint) -> Qt.AnchorPoint:
    """
    Calls Qt's 'Qt::AnchorPoint
    QGraphicsAnchorLayoutPrivate::oppositeEdge(Qt::AnchorPoint edge)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsanchorlayoutprivate.html#oppositeEdge

    Parameters
    ----------

    edge : Qt.AnchorPoint
      Passed on as its number.

    Returns
    -------

    Qt.AnchorPoint
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.AnchorPoint(number)'
      gives.
    """
    #  Qt::AnchorPoint
    #      QGraphicsAnchorLayoutPrivate::oppositeEdge(Qt::AnchorPoint edge)
    return Qt.AnchorPoint(Rituals.call(
        'ritual_ZN28QGraphicsAnchorLayoutPrivate12oppositeEdgeEN2Qt11Anchor'
        'PointE',
        edge.value,
    ))

  @staticmethod
  @overload(Qt.AnchorPoint)
  def edgeOrientation(edge: Qt.AnchorPoint) -> Qt.Orientation:
    """
    Calls Qt's 'Qt::Orientation
    QGraphicsAnchorLayoutPrivate::edgeOrientation(Qt::AnchorPoint edge)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsanchorlayoutprivate.html#edgeOrientation

    Parameters
    ----------

    edge : Qt.AnchorPoint
      Passed on as its number.

    Returns
    -------

    Qt.Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Orientation(number)'
      gives.
    """
    #  Qt::Orientation
    #      QGraphicsAnchorLayoutPrivate::edgeOrientation(Qt::AnchorPoint
    #      edge)
    return Qt.Orientation(Rituals.call(
        'ritual_ZN28QGraphicsAnchorLayoutPrivate15edgeOrientationEN2Qt11Anc'
        'horPointE',
        edge.value,
    ))

  @staticmethod
  @overload(Qt.AnchorPoint, Qt.Orientation)
  def pickEdge(
      edge: Qt.AnchorPoint,
      orientation: Qt.Orientation,
  ) -> Qt.AnchorPoint:
    """
    Calls Qt's 'Qt::AnchorPoint
    QGraphicsAnchorLayoutPrivate::pickEdge(Qt::AnchorPoint edge,
    Qt::Orientation orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsanchorlayoutprivate.html#pickEdge

    Parameters
    ----------

    edge : Qt.AnchorPoint
      Passed on as its number.

    orientation : Qt.Orientation
      Passed on as its number.

    Returns
    -------

    Qt.AnchorPoint
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.AnchorPoint(number)'
      gives.
    """
    #  Qt::AnchorPoint QGraphicsAnchorLayoutPrivate::pickEdge(Qt::AnchorPoint
    #      edge, Qt::Orientation orientation)
    return Qt.AnchorPoint(Rituals.call(
        'ritual_ZN28QGraphicsAnchorLayoutPrivate8pickEdgeEN2Qt11AnchorPoint'
        'ENS0_11OrientationE',
        edge.value, orientation.value,
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsAnchorLayoutPrivate'

  #  Qt's '~QGraphicsAnchorLayoutPrivate()'. Naming it makes this a value
  #  class: Python owns every C++ QGraphicsAnchorLayoutPrivate behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN28QGraphicsAnchorLayoutPrivateD1Ev'

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

  @overload(QRectF)
  def setItemsGeometries(self, geom: QRectF) -> None:
    """
    Calls Qt's 'void QGraphicsAnchorLayoutPrivate::setItemsGeometries(const
    QRectF &geom)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsanchorlayoutprivate.html

    Parameters
    ----------

    geom : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QGraphicsAnchorLayoutPrivate::setItemsGeometries(const QRectF
    #      &geom)
    self.uglySide.call(
        'ritual_ZN28QGraphicsAnchorLayoutPrivate18setItemsGeometriesERK6QRe'
        'ctF',
        self._valueOf(geom),
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
    Notes what was given, for Qt's
    'QGraphicsAnchorLayoutPrivate::QGraphicsAnchorLayoutPrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsanchorlayoutprivate.html
    """
    #  QGraphicsAnchorLayoutPrivate::QGraphicsAnchorLayoutPrivate()
    self._noteCreation(QGraphicsAnchorLayoutPrivate, lambda: Rituals.call(
        'ritual_ZN28QGraphicsAnchorLayoutPrivateC1Ev',
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

  def q_func(self) -> Optional[QGraphicsAnchorLayout]:
    """
    Calls Qt's 'QGraphicsAnchorLayout
    *QGraphicsAnchorLayoutPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsanchorlayoutprivate.html#q_func

    Returns
    -------

    Optional[QGraphicsAnchorLayout]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsAnchorLayout *QGraphicsAnchorLayoutPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN28QGraphicsAnchorLayoutPrivate6q_funcEv',
    )
    from . import QGraphicsAnchorLayout
    return QGraphicsAnchorLayout._cuteAt(address)

  @overload(QGraphicsLayoutItem, Qt.Orientation)
  @overload(NoneType, Qt.Orientation)
  def removeCenterConstraints(
      self,
      item: Optional[QGraphicsLayoutItem],
      orientation: Qt.Orientation,
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsAnchorLayoutPrivate::removeCenterConstraints(QGraphicsLayoutItem
    *item, Qt::Orientation orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsanchorlayoutprivate.html

    Parameters
    ----------

    item : Optional[QGraphicsLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  void QGraphicsAnchorLayoutPrivate::removeCenterConstraints(
    #      QGraphicsLayoutItem *item, Qt::Orientation orientation)
    self.uglySide.call(
        'ritual_ZN28QGraphicsAnchorLayoutPrivate23removeCenterConstraintsEP'
        '19QGraphicsLayoutItemN2Qt11OrientationE',
        self._addressOf(item, 'QGraphicsLayoutItem'), orientation.value,
    )

  @overload(
      QGraphicsLayoutItem, Qt.AnchorPoint, QGraphicsLayoutItem,
      Qt.AnchorPoint,
  )
  @overload(QGraphicsLayoutItem, Qt.AnchorPoint, NoneType, Qt.AnchorPoint)
  @overload(NoneType, Qt.AnchorPoint, QGraphicsLayoutItem, Qt.AnchorPoint)
  @overload(NoneType, Qt.AnchorPoint, NoneType, Qt.AnchorPoint)
  def getAnchor(
      self,
      firstItem: Optional[QGraphicsLayoutItem],
      firstEdge: Qt.AnchorPoint,
      secondItem: Optional[QGraphicsLayoutItem],
      secondEdge: Qt.AnchorPoint,
  ) -> Optional[QGraphicsAnchor]:
    """
    Calls Qt's 'QGraphicsAnchor
    *QGraphicsAnchorLayoutPrivate::getAnchor(QGraphicsLayoutItem *firstItem,
    Qt::AnchorPoint firstEdge, QGraphicsLayoutItem *secondItem,
    Qt::AnchorPoint secondEdge)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsanchorlayoutprivate.html#getAnchor

    Parameters
    ----------

    firstItem : Optional[QGraphicsLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstEdge : Qt.AnchorPoint
      Passed on as its number.

    secondItem : Optional[QGraphicsLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    secondEdge : Qt.AnchorPoint
      Passed on as its number.

    Returns
    -------

    Optional[QGraphicsAnchor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsAnchor
    #      *QGraphicsAnchorLayoutPrivate::getAnchor(QGraphicsLayoutItem
    #      *firstItem, Qt::AnchorPoint firstEdge, QGraphicsLayoutItem
    #      *secondItem, Qt::AnchorPoint secondEdge)
    address = self.uglySide.call(
        'ritual_ZN28QGraphicsAnchorLayoutPrivate9getAnchorEP19QGraphicsLayo'
        'utItemN2Qt11AnchorPointES1_S3_',
        self._addressOf(firstItem, 'QGraphicsLayoutItem'), firstEdge.value,
        self._addressOf(secondItem, 'QGraphicsLayoutItem'), secondEdge.value,
    )
    from . import QGraphicsAnchor
    return QGraphicsAnchor._cuteAt(address)

  @overload(Qt.Orientation)
  def restoreSimplifiedGraph(self, orientation: Qt.Orientation) -> None:
    """
    Calls Qt's 'void
    QGraphicsAnchorLayoutPrivate::restoreSimplifiedGraph(Qt::Orientation
    orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsanchorlayoutprivate.html

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  void QGraphicsAnchorLayoutPrivate::restoreSimplifiedGraph(Qt::
    #      Orientation orientation)
    self.uglySide.call(
        'ritual_ZN28QGraphicsAnchorLayoutPrivate22restoreSimplifiedGraphEN2'
        'Qt11OrientationE',
        orientation.value,
    )

  @overload(Qt.Orientation)
  def findPaths(self, orientation: Qt.Orientation) -> None:
    """
    Calls Qt's 'void QGraphicsAnchorLayoutPrivate::findPaths(Qt::Orientation
    orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsanchorlayoutprivate.html#findPaths

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  void QGraphicsAnchorLayoutPrivate::findPaths(Qt::Orientation
    #      orientation)
    self.uglySide.call(
        'ritual_ZN28QGraphicsAnchorLayoutPrivate9findPathsEN2Qt11Orientatio'
        'nE',
        orientation.value,
    )

  @overload(Qt.Orientation)
  def updateAnchorSizes(self, orientation: Qt.Orientation) -> None:
    """
    Calls Qt's 'void
    QGraphicsAnchorLayoutPrivate::updateAnchorSizes(Qt::Orientation
    orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsanchorlayoutprivate.html

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  void QGraphicsAnchorLayoutPrivate::updateAnchorSizes(Qt::Orientation
    #      orientation)
    self.uglySide.call(
        'ritual_ZN28QGraphicsAnchorLayoutPrivate17updateAnchorSizesEN2Qt11O'
        'rientationE',
        orientation.value,
    )

  @overload(Qt.Orientation)
  def getGraphParts(self, orientation: Qt.Orientation) -> GraphParts:
    """
    Calls Qt's 'GraphParts
    QGraphicsAnchorLayoutPrivate::getGraphParts(Qt::Orientation
    orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsanchorlayoutprivate.html#getGraphParts

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.

    Returns
    -------

    GraphParts
      A new cute QGraphicsAnchorLayoutPrivate::GraphParts around the copy Qt
      gave back. Python owns it.
    """
    #  GraphParts QGraphicsAnchorLayoutPrivate::getGraphParts(Qt::Orientation
    #      orientation)
    address = self.uglySide.call(
        'ritual_ZN28QGraphicsAnchorLayoutPrivate13getGraphPartsEN2Qt11Orien'
        'tationE',
        orientation.value,
    )
    return QGraphicsAnchorLayoutPrivate.GraphParts._cuteOwning(address)

  @overload(Qt.Orientation)
  def calculateVertexPositions(self, orientation: Qt.Orientation) -> None:
    """
    Calls Qt's 'void
    QGraphicsAnchorLayoutPrivate::calculateVertexPositions(Qt::Orientation
    orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsanchorlayoutprivate.html

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  void QGraphicsAnchorLayoutPrivate::calculateVertexPositions(Qt::
    #      Orientation orientation)
    self.uglySide.call(
        'ritual_ZN28QGraphicsAnchorLayoutPrivate24calculateVertexPositionsE'
        'N2Qt11OrientationE',
        orientation.value,
    )

  @overload(Qt.Orientation)
  def setupEdgesInterpolation(self, orientation: Qt.Orientation) -> None:
    """
    Calls Qt's 'void
    QGraphicsAnchorLayoutPrivate::setupEdgesInterpolation(Qt::Orientation
    orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsanchorlayoutprivate.html

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  void QGraphicsAnchorLayoutPrivate::setupEdgesInterpolation(Qt::
    #      Orientation orientation)
    self.uglySide.call(
        'ritual_ZN28QGraphicsAnchorLayoutPrivate23setupEdgesInterpolationEN'
        '2Qt11OrientationE',
        orientation.value,
    )

  @overload()
  @overload(str)
  def dumpGraph(self, name: str = '') -> None:
    """
    Calls Qt's 'void QGraphicsAnchorLayoutPrivate::dumpGraph(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsanchorlayoutprivate.html#dumpGraph

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QGraphicsAnchorLayoutPrivate::dumpGraph(const QString &name)
    self.uglySide.call(
        'ritual_ZN28QGraphicsAnchorLayoutPrivate9dumpGraphERK7QString', name,
    )

  @staticmethod
  def acquireGraphicsAnchor(*__, **_) -> Never:
    """
    Qt's 'QGraphicsAnchor
    *QGraphicsAnchorLayoutPrivate::acquireGraphicsAnchor(AnchorData *data)':
    names 'AnchorData', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QGraphicsAnchorLayoutPrivate.acquireGraphicsAnchor' has no cute "
        "function yet. Qt's 'QGraphicsAnchor "
        "*QGraphicsAnchorLayoutPrivate::acquireGraphicsAnchor(AnchorData "
        "*data)': names 'AnchorData', which has no cute class yet.")

  @staticmethod
  def addAnchor(*__, **_) -> Never:
    """
    Qt's 'QGraphicsAnchor
    *QGraphicsAnchorLayoutPrivate::addAnchor(QGraphicsLayoutItem *firstItem,
    Qt::AnchorPoint firstEdge, QGraphicsLayoutItem *secondItem,
    Qt::AnchorPoint secondEdge, qreal *spacing)': leans on
    'QtGraphicsAnchorLayout::AnchorData::refreshSizeHints(QLayoutStyleInfo
    const*)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsAnchorLayoutPrivate.addAnchor' has no cute function yet. "
        "Qt's 'QGraphicsAnchor "
        "*QGraphicsAnchorLayoutPrivate::addAnchor(QGraphicsLayoutItem "
        "*firstItem, Qt::AnchorPoint firstEdge, QGraphicsLayoutItem "
        "*secondItem, Qt::AnchorPoint secondEdge, qreal *spacing)': leans "
        "on "
        "'QtGraphicsAnchorLayout::AnchorData::refreshSizeHints(QLayoutStyleI"
        "nfo const*)', which Qt's source does not mark for use from outside "
        "Qt and has no code for that could be taken.")

  @staticmethod
  def addAnchorMaybeParallel(*__, **_) -> Never:
    """
    Qt's 'AnchorData
    *QGraphicsAnchorLayoutPrivate::addAnchorMaybeParallel(AnchorData
    *newAnchor, bool *feasible)': leans on
    'QtGraphicsAnchorLayout::AnchorData::~AnchorData()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QGraphicsAnchorLayoutPrivate.addAnchorMaybeParallel' has no cute "
        "function yet. Qt's 'AnchorData "
        "*QGraphicsAnchorLayoutPrivate::addAnchorMaybeParallel(AnchorData "
        "*newAnchor, bool *feasible)': leans on "
        "'QtGraphicsAnchorLayout::AnchorData::~AnchorData()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def addAnchor_helper(*__, **_) -> Never:
    """
    Qt's 'void
    QGraphicsAnchorLayoutPrivate::addAnchor_helper(QGraphicsLayoutItem
    *firstItem, Qt::AnchorPoint firstEdge, QGraphicsLayoutItem *secondItem,
    Qt::AnchorPoint secondEdge, AnchorData *data)': leans on
    'QtGraphicsAnchorLayout::AnchorData::refreshSizeHints(QLayoutStyleInfo
    const*)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsAnchorLayoutPrivate.addAnchor_helper' has no cute "
        "function yet. Qt's 'void "
        "QGraphicsAnchorLayoutPrivate::addAnchor_helper(QGraphicsLayoutItem "
        "*firstItem, Qt::AnchorPoint firstEdge, QGraphicsLayoutItem "
        "*secondItem, Qt::AnchorPoint secondEdge, AnchorData *data)': leans "
        "on "
        "'QtGraphicsAnchorLayout::AnchorData::refreshSizeHints(QLayoutStyleI"
        "nfo const*)', which Qt's source does not mark for use from outside "
        "Qt and has no code for that could be taken.")

  @staticmethod
  def addInternalVertex(*__, **_) -> Never:
    """
    Qt's 'AnchorVertex
    *QGraphicsAnchorLayoutPrivate::addInternalVertex(QGraphicsLayoutItem
    *item, Qt::AnchorPoint edge)': gives 'AnchorVertex', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QGraphicsAnchorLayoutPrivate.addInternalVertex' has no cute "
        "function yet. Qt's 'AnchorVertex "
        "*QGraphicsAnchorLayoutPrivate::addInternalVertex(QGraphicsLayoutIte"
        "m *item, Qt::AnchorPoint edge)': gives 'AnchorVertex', which has "
        "no cute class yet.")

  @staticmethod
  def calculateGraphs(*__, **_) -> Never:
    """
    - Qt's 'void
      QGraphicsAnchorLayoutPrivate::calculateGraphs(Qt::Orientation
      orientation)': Qt's library has no name for it, and its code in Qt's
      source does not compile apart from its file: use of undeclared
      identifier 'getVariables'.
    - Qt's 'void QGraphicsAnchorLayoutPrivate::calculateGraphs()': leans on
      'QtGraphicsAnchorLayout::AnchorData::refreshSizeHints(QLayoutStyleInfo
      const*)', which Qt's source does not mark for use from outside Qt and
      has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsAnchorLayoutPrivate.calculateGraphs' has no cute "
        "function yet. Qt's 'void "
        "QGraphicsAnchorLayoutPrivate::calculateGraphs(Qt::Orientation "
        "orientation)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'getVariables'. Qt's 'void "
        "QGraphicsAnchorLayoutPrivate::calculateGraphs()': leans on "
        "'QtGraphicsAnchorLayout::AnchorData::refreshSizeHints(QLayoutStyleI"
        "nfo const*)', which Qt's source does not mark for use from outside "
        "Qt and has no code for that could be taken.")

  @staticmethod
  def calculateNonTrunk(*__, **_) -> Never:
    """
    Qt's 'bool QGraphicsAnchorLayoutPrivate::calculateNonTrunk(const
    QList<QSimplexConstraint *> &constraints, const QList<AnchorData *>
    &variables)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'g_offset'.
    """
    raise NotImplementedError(
        "'QGraphicsAnchorLayoutPrivate.calculateNonTrunk' has no cute "
        "function yet. Qt's 'bool "
        "QGraphicsAnchorLayoutPrivate::calculateNonTrunk(const "
        "QList<QSimplexConstraint *> &constraints, const QList<AnchorData "
        "*> &variables)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'g_offset'.")

  @staticmethod
  def calculateTrunk(*__, **_) -> Never:
    """
    Qt's 'bool QGraphicsAnchorLayoutPrivate::calculateTrunk(Qt::Orientation
    orientation, const GraphPath &trunkPath, const QList<QSimplexConstraint
    *> &constraints, const QList<AnchorData *> &variables)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'g_offset'.
    """
    raise NotImplementedError(
        "'QGraphicsAnchorLayoutPrivate.calculateTrunk' has no cute function "
        "yet. Qt's 'bool "
        "QGraphicsAnchorLayoutPrivate::calculateTrunk(Qt::Orientation "
        "orientation, const GraphPath &trunkPath, const "
        "QList<QSimplexConstraint *> &constraints, const QList<AnchorData "
        "*> &variables)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'g_offset'.")

  @staticmethod
  def changeLayoutVertex(*__, **_) -> Never:
    """
    Qt's 'void
    QGraphicsAnchorLayoutPrivate::changeLayoutVertex(Qt::Orientation
    orientation, AnchorVertex *oldV, AnchorVertex *newV)': names
    'AnchorVertex', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QGraphicsAnchorLayoutPrivate.changeLayoutVertex' has no cute "
        "function yet. Qt's 'void "
        "QGraphicsAnchorLayoutPrivate::changeLayoutVertex(Qt::Orientation "
        "orientation, AnchorVertex *oldV, AnchorVertex *newV)': names "
        "'AnchorVertex', which has no cute class yet.")

  @staticmethod
  def constraintsFromPaths(*__, **_) -> Never:
    """
    Qt's 'void
    QGraphicsAnchorLayoutPrivate::constraintsFromPaths(Qt::Orientation
    orientation)': leans on
    'QtGraphicsAnchorLayout::GraphPath::constraint(QtGraphicsAnchorLayout::
    GraphPath const&) const', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsAnchorLayoutPrivate.constraintsFromPaths' has no cute "
        "function yet. Qt's 'void "
        "QGraphicsAnchorLayoutPrivate::constraintsFromPaths(Qt::Orientation "
        "orientation)': leans on "
        "'QtGraphicsAnchorLayout::GraphPath::constraint(QtGraphicsAnchorLayo"
        "ut::GraphPath const&) const', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def constraintsFromSizeHints(*__, **_) -> Never:
    """
    Qt's 'QList<QSimplexConstraint *>
    QGraphicsAnchorLayoutPrivate::constraintsFromSizeHints(const
    QList<AnchorData *> &anchors)': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'g_offset'.
    """
    raise NotImplementedError(
        "'QGraphicsAnchorLayoutPrivate.constraintsFromSizeHints' has no "
        "cute function yet. Qt's 'QList<QSimplexConstraint *> "
        "QGraphicsAnchorLayoutPrivate::constraintsFromSizeHints(const "
        "QList<AnchorData *> &anchors)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "use of undeclared identifier 'g_offset'.")

  @staticmethod
  def correctEdgeDirection(*__, **_) -> Never:
    """
    Qt's 'void
    QGraphicsAnchorLayoutPrivate::correctEdgeDirection(QGraphicsLayoutItem
    *&firstItem, Qt::AnchorPoint &firstEdge, QGraphicsLayoutItem
    *&secondItem, Qt::AnchorPoint &secondEdge)': takes or gives a type that
    cannot be passed yet: QGraphicsLayoutItem *&.
    """
    raise NotImplementedError(
        "'QGraphicsAnchorLayoutPrivate.correctEdgeDirection' has no cute "
        "function yet. Qt's 'void "
        "QGraphicsAnchorLayoutPrivate::correctEdgeDirection(QGraphicsLayoutI"
        "tem *&firstItem, Qt::AnchorPoint &firstEdge, QGraphicsLayoutItem "
        "*&secondItem, Qt::AnchorPoint &secondEdge)': takes or gives a type "
        "that cannot be passed yet: QGraphicsLayoutItem *&.")

  @staticmethod
  def createCenterAnchors(*__, **_) -> Never:
    """
    Qt's 'void
    QGraphicsAnchorLayoutPrivate::createCenterAnchors(QGraphicsLayoutItem
    *item, Qt::AnchorPoint centerEdge)': leans on
    'QtGraphicsAnchorLayout::AnchorData::refreshSizeHints(QLayoutStyleInfo
    const*)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsAnchorLayoutPrivate.createCenterAnchors' has no cute "
        "function yet. Qt's 'void "
        "QGraphicsAnchorLayoutPrivate::createCenterAnchors(QGraphicsLayoutIt"
        "em *item, Qt::AnchorPoint centerEdge)': leans on "
        "'QtGraphicsAnchorLayout::AnchorData::refreshSizeHints(QLayoutStyleI"
        "nfo const*)', which Qt's source does not mark for use from outside "
        "Qt and has no code for that could be taken.")

  @staticmethod
  def createItemEdges(*__, **_) -> Never:
    """
    Qt's 'void
    QGraphicsAnchorLayoutPrivate::createItemEdges(QGraphicsLayoutItem
    *item)': leans on
    'QtGraphicsAnchorLayout::AnchorData::refreshSizeHints(QLayoutStyleInfo
    const*)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsAnchorLayoutPrivate.createItemEdges' has no cute "
        "function yet. Qt's 'void "
        "QGraphicsAnchorLayoutPrivate::createItemEdges(QGraphicsLayoutItem "
        "*item)': leans on "
        "'QtGraphicsAnchorLayout::AnchorData::refreshSizeHints(QLayoutStyleI"
        "nfo const*)', which Qt's source does not mark for use from outside "
        "Qt and has no code for that could be taken.")

  @staticmethod
  def createLayoutEdges(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsAnchorLayoutPrivate::createLayoutEdges()': leans on
    'QtGraphicsAnchorLayout::AnchorData::refreshSizeHints(QLayoutStyleInfo
    const*)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsAnchorLayoutPrivate.createLayoutEdges' has no cute "
        "function yet. Qt's 'void "
        "QGraphicsAnchorLayoutPrivate::createLayoutEdges()': leans on "
        "'QtGraphicsAnchorLayout::AnchorData::refreshSizeHints(QLayoutStyleI"
        "nfo const*)', which Qt's source does not mark for use from outside "
        "Qt and has no code for that could be taken.")

  @staticmethod
  def deleteLayoutEdges(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsAnchorLayoutPrivate::deleteLayoutEdges()': leans on
    'QtGraphicsAnchorLayout::AnchorData::refreshSizeHints(QLayoutStyleInfo
    const*)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsAnchorLayoutPrivate.deleteLayoutEdges' has no cute "
        "function yet. Qt's 'void "
        "QGraphicsAnchorLayoutPrivate::deleteLayoutEdges()': leans on "
        "'QtGraphicsAnchorLayout::AnchorData::refreshSizeHints(QLayoutStyleI"
        "nfo const*)', which Qt's source does not mark for use from outside "
        "Qt and has no code for that could be taken.")

  @staticmethod
  def hasConflicts(*__, **_) -> Never:
    """
    Qt's 'bool QGraphicsAnchorLayoutPrivate::hasConflicts() const': leans on
    'QtGraphicsAnchorLayout::AnchorData::refreshSizeHints(QLayoutStyleInfo
    const*)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsAnchorLayoutPrivate.hasConflicts' has no cute function "
        "yet. Qt's 'bool QGraphicsAnchorLayoutPrivate::hasConflicts() "
        "const': leans on "
        "'QtGraphicsAnchorLayout::AnchorData::refreshSizeHints(QLayoutStyleI"
        "nfo const*)', which Qt's source does not mark for use from outside "
        "Qt and has no code for that could be taken.")

  @staticmethod
  def identifyFloatItems(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsAnchorLayoutPrivate::identifyFloatItems(const
    QSet<AnchorData *> &visited, Qt::Orientation orientation)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGraphicsAnchorLayoutPrivate.identifyFloatItems' has no cute "
        "function yet. Qt's 'void "
        "QGraphicsAnchorLayoutPrivate::identifyFloatItems(const "
        "QSet<AnchorData *> &visited, Qt::Orientation orientation)': takes "
        "a type Python has no way to hand over yet.")

  @staticmethod
  def identifyNonFloatItems_helper(*__, **_) -> Never:
    """
    Qt's 'void
    QGraphicsAnchorLayoutPrivate::identifyNonFloatItems_helper(const
    AnchorData *ad, QSet<QGraphicsLayoutItem *>
    *nonFloatingItemsIdentifiedSoFar)': names 'AnchorData', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QGraphicsAnchorLayoutPrivate.identifyNonFloatItems_helper' has no "
        "cute function yet. Qt's 'void "
        "QGraphicsAnchorLayoutPrivate::identifyNonFloatItems_helper(const "
        "AnchorData *ad, QSet<QGraphicsLayoutItem *> "
        "*nonFloatingItemsIdentifiedSoFar)': names 'AnchorData', which has "
        "no cute class yet.")

  @staticmethod
  def internalVertex(*__, **_) -> Never:
    """
    - Qt's 'AnchorVertex *QGraphicsAnchorLayoutPrivate::internalVertex(const
      std::pair<QGraphicsLayoutItem *, Qt::AnchorPoint> &itemEdge) const':
      takes a type Python has no way to hand over yet.
    - Qt's 'AnchorVertex *QGraphicsAnchorLayoutPrivate::internalVertex(const
      QGraphicsLayoutItem *item, Qt::AnchorPoint edge) const': gives
      'AnchorVertex', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QGraphicsAnchorLayoutPrivate.internalVertex' has no cute function "
        "yet. Qt's 'AnchorVertex "
        "*QGraphicsAnchorLayoutPrivate::internalVertex(const "
        "std::pair<QGraphicsLayoutItem *, Qt::AnchorPoint> &itemEdge) "
        "const': takes a type Python has no way to hand over yet. Qt's "
        "'AnchorVertex *QGraphicsAnchorLayoutPrivate::internalVertex(const "
        "QGraphicsLayoutItem *item, Qt::AnchorPoint edge) const': gives "
        "'AnchorVertex', which has no cute class yet.")

  @staticmethod
  def interpolateEdge(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsAnchorLayoutPrivate::interpolateEdge(AnchorVertex
    *base, AnchorData *edge)': names 'AnchorVertex', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QGraphicsAnchorLayoutPrivate.interpolateEdge' has no cute "
        "function yet. Qt's 'void "
        "QGraphicsAnchorLayoutPrivate::interpolateEdge(AnchorVertex *base, "
        "AnchorData *edge)': names 'AnchorVertex', which has no cute class "
        "yet.")

  @staticmethod
  def refreshAllSizeHints(*__, **_) -> Never:
    """
    Qt's 'void
    QGraphicsAnchorLayoutPrivate::refreshAllSizeHints(Qt::Orientation
    orientation)': leans on
    'QtGraphicsAnchorLayout::AnchorData::refreshSizeHints(QLayoutStyleInfo
    const*)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsAnchorLayoutPrivate.refreshAllSizeHints' has no cute "
        "function yet. Qt's 'void "
        "QGraphicsAnchorLayoutPrivate::refreshAllSizeHints(Qt::Orientation "
        "orientation)': leans on "
        "'QtGraphicsAnchorLayout::AnchorData::refreshSizeHints(QLayoutStyleI"
        "nfo const*)', which Qt's source does not mark for use from outside "
        "Qt and has no code for that could be taken.")

  @staticmethod
  def removeAnchor(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsAnchorLayoutPrivate::removeAnchor(AnchorVertex
    *firstVertex, AnchorVertex *secondVertex)': leans on
    'QtGraphicsAnchorLayout::AnchorData::refreshSizeHints(QLayoutStyleInfo
    const*)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsAnchorLayoutPrivate.removeAnchor' has no cute function "
        "yet. Qt's 'void "
        "QGraphicsAnchorLayoutPrivate::removeAnchor(AnchorVertex "
        "*firstVertex, AnchorVertex *secondVertex)': leans on "
        "'QtGraphicsAnchorLayout::AnchorData::refreshSizeHints(QLayoutStyleI"
        "nfo const*)', which Qt's source does not mark for use from outside "
        "Qt and has no code for that could be taken.")

  @staticmethod
  def removeAnchor_helper(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsAnchorLayoutPrivate::removeAnchor_helper(AnchorVertex
    *v1, AnchorVertex *v2)': leans on
    'QtGraphicsAnchorLayout::AnchorData::refreshSizeHints(QLayoutStyleInfo
    const*)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsAnchorLayoutPrivate.removeAnchor_helper' has no cute "
        "function yet. Qt's 'void "
        "QGraphicsAnchorLayoutPrivate::removeAnchor_helper(AnchorVertex "
        "*v1, AnchorVertex *v2)': leans on "
        "'QtGraphicsAnchorLayout::AnchorData::refreshSizeHints(QLayoutStyleI"
        "nfo const*)', which Qt's source does not mark for use from outside "
        "Qt and has no code for that could be taken.")

  @staticmethod
  def removeAnchors(*__, **_) -> Never:
    """
    Qt's 'void
    QGraphicsAnchorLayoutPrivate::removeAnchors(QGraphicsLayoutItem *item)':
    leans on
    'QtGraphicsAnchorLayout::AnchorData::refreshSizeHints(QLayoutStyleInfo
    const*)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsAnchorLayoutPrivate.removeAnchors' has no cute function "
        "yet. Qt's 'void "
        "QGraphicsAnchorLayoutPrivate::removeAnchors(QGraphicsLayoutItem "
        "*item)': leans on "
        "'QtGraphicsAnchorLayout::AnchorData::refreshSizeHints(QLayoutStyleI"
        "nfo const*)', which Qt's source does not mark for use from outside "
        "Qt and has no code for that could be taken.")

  @staticmethod
  def removeCenterAnchors(*__, **_) -> Never:
    """
    Qt's 'void
    QGraphicsAnchorLayoutPrivate::removeCenterAnchors(QGraphicsLayoutItem
    *item, Qt::AnchorPoint centerEdge, bool substitute)': leans on
    'QtGraphicsAnchorLayout::AnchorData::refreshSizeHints(QLayoutStyleInfo
    const*)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsAnchorLayoutPrivate.removeCenterAnchors' has no cute "
        "function yet. Qt's 'void "
        "QGraphicsAnchorLayoutPrivate::removeCenterAnchors(QGraphicsLayoutIt"
        "em *item, Qt::AnchorPoint centerEdge, bool substitute)': leans on "
        "'QtGraphicsAnchorLayout::AnchorData::refreshSizeHints(QLayoutStyleI"
        "nfo const*)', which Qt's source does not mark for use from outside "
        "Qt and has no code for that could be taken.")

  @staticmethod
  def removeInternalVertex(*__, **_) -> Never:
    """
    Qt's 'void
    QGraphicsAnchorLayoutPrivate::removeInternalVertex(QGraphicsLayoutItem
    *item, Qt::AnchorPoint edge)': leans on
    'QtGraphicsAnchorLayout::AnchorData::refreshSizeHints(QLayoutStyleInfo
    const*)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsAnchorLayoutPrivate.removeInternalVertex' has no cute "
        "function yet. Qt's 'void "
        "QGraphicsAnchorLayoutPrivate::removeInternalVertex(QGraphicsLayoutI"
        "tem *item, Qt::AnchorPoint edge)': leans on "
        "'QtGraphicsAnchorLayout::AnchorData::refreshSizeHints(QLayoutStyleI"
        "nfo const*)', which Qt's source does not mark for use from outside "
        "Qt and has no code for that could be taken.")

  @staticmethod
  def removeVertex(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsAnchorLayoutPrivate::removeVertex(QGraphicsLayoutItem
    *item, Qt::AnchorPoint edge)': leans on
    'QtGraphicsAnchorLayout::AnchorData::refreshSizeHints(QLayoutStyleInfo
    const*)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsAnchorLayoutPrivate.removeVertex' has no cute function "
        "yet. Qt's 'void "
        "QGraphicsAnchorLayoutPrivate::removeVertex(QGraphicsLayoutItem "
        "*item, Qt::AnchorPoint edge)': leans on "
        "'QtGraphicsAnchorLayout::AnchorData::refreshSizeHints(QLayoutStyleI"
        "nfo const*)', which Qt's source does not mark for use from outside "
        "Qt and has no code for that could be taken.")

  @staticmethod
  def replaceVertex(*__, **_) -> Never:
    """
    Qt's 'bool QGraphicsAnchorLayoutPrivate::replaceVertex(Qt::Orientation
    orientation, AnchorVertex *oldV, AnchorVertex *newV, const
    QList<AnchorData *> &edges)': leans on
    'QtGraphicsAnchorLayout::AnchorData::~AnchorData()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QGraphicsAnchorLayoutPrivate.replaceVertex' has no cute function "
        "yet. Qt's 'bool "
        "QGraphicsAnchorLayoutPrivate::replaceVertex(Qt::Orientation "
        "orientation, AnchorVertex *oldV, AnchorVertex *newV, const "
        "QList<AnchorData *> &edges)': leans on "
        "'QtGraphicsAnchorLayout::AnchorData::~AnchorData()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def restoreSimplifiedAnchor(*__, **_) -> Never:
    """
    Qt's 'void
    QGraphicsAnchorLayoutPrivate::restoreSimplifiedAnchor(AnchorData *edge)':
    names 'AnchorData', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QGraphicsAnchorLayoutPrivate.restoreSimplifiedAnchor' has no cute "
        "function yet. Qt's 'void "
        "QGraphicsAnchorLayoutPrivate::restoreSimplifiedAnchor(AnchorData "
        "*edge)': names 'AnchorData', which has no cute class yet.")

  @staticmethod
  def restoreSimplifiedConstraints(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsAnchorLayoutPrivate::restoreSimplifiedConstraints(
    ParallelAnchorData *parallel)': names 'ParallelAnchorData', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QGraphicsAnchorLayoutPrivate.restoreSimplifiedConstraints' has no "
        "cute function yet. Qt's 'void "
        "QGraphicsAnchorLayoutPrivate::restoreSimplifiedConstraints(Parallel"
        "AnchorData *parallel)': names 'ParallelAnchorData', which has no "
        "cute class yet.")

  @staticmethod
  def restoreVertices(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsAnchorLayoutPrivate::restoreVertices(Qt::Orientation
    orientation)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'replaceVertex_helper'.
    """
    raise NotImplementedError(
        "'QGraphicsAnchorLayoutPrivate.restoreVertices' has no cute "
        "function yet. Qt's 'void "
        "QGraphicsAnchorLayoutPrivate::restoreVertices(Qt::Orientation "
        "orientation)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'replaceVertex_helper'.")

  @staticmethod
  def simplifyGraph(*__, **_) -> Never:
    """
    Qt's 'bool QGraphicsAnchorLayoutPrivate::simplifyGraph(Qt::Orientation
    orientation)': leans on
    'QtGraphicsAnchorLayout::AnchorData::~AnchorData()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QGraphicsAnchorLayoutPrivate.simplifyGraph' has no cute function "
        "yet. Qt's 'bool "
        "QGraphicsAnchorLayoutPrivate::simplifyGraph(Qt::Orientation "
        "orientation)': leans on "
        "'QtGraphicsAnchorLayout::AnchorData::~AnchorData()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def simplifyGraphIteration(*__, **_) -> Never:
    """
    Qt's 'bool
    QGraphicsAnchorLayoutPrivate::simplifyGraphIteration(Qt::Orientation
    orientation, bool *feasible)': leans on
    'QtGraphicsAnchorLayout::AnchorData::~AnchorData()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QGraphicsAnchorLayoutPrivate.simplifyGraphIteration' has no cute "
        "function yet. Qt's 'bool "
        "QGraphicsAnchorLayoutPrivate::simplifyGraphIteration(Qt::Orientatio"
        "n orientation, bool *feasible)': leans on "
        "'QtGraphicsAnchorLayout::AnchorData::~AnchorData()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def simplifyVertices(*__, **_) -> Never:
    """
    Qt's 'bool QGraphicsAnchorLayoutPrivate::simplifyVertices(Qt::Orientation
    orientation)': leans on
    'QtGraphicsAnchorLayout::AnchorData::~AnchorData()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QGraphicsAnchorLayoutPrivate.simplifyVertices' has no cute "
        "function yet. Qt's 'bool "
        "QGraphicsAnchorLayoutPrivate::simplifyVertices(Qt::Orientation "
        "orientation)': leans on "
        "'QtGraphicsAnchorLayout::AnchorData::~AnchorData()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def solveMinMax(*__, **_) -> Never:
    """
    Qt's 'bool QGraphicsAnchorLayoutPrivate::solveMinMax(const
    QList<QSimplexConstraint *> &constraints, const GraphPath &path, qreal
    *min, qreal *max)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'g_offset'.
    """
    raise NotImplementedError(
        "'QGraphicsAnchorLayoutPrivate.solveMinMax' has no cute function "
        "yet. Qt's 'bool QGraphicsAnchorLayoutPrivate::solveMinMax(const "
        "QList<QSimplexConstraint *> &constraints, const GraphPath &path, "
        "qreal *min, qreal *max)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'g_offset'.")

  @staticmethod
  def solvePreferred(*__, **_) -> Never:
    """
    Qt's 'bool QGraphicsAnchorLayoutPrivate::solvePreferred(const
    QList<QSimplexConstraint *> &constraints, const QList<AnchorData *>
    &variables)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'g_offset'.
    """
    raise NotImplementedError(
        "'QGraphicsAnchorLayoutPrivate.solvePreferred' has no cute function "
        "yet. Qt's 'bool QGraphicsAnchorLayoutPrivate::solvePreferred(const "
        "QList<QSimplexConstraint *> &constraints, const QList<AnchorData "
        "*> &variables)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'g_offset'.")

  @staticmethod
  def styleInfo(*__, **_) -> Never:
    """
    Qt's 'QLayoutStyleInfo &QGraphicsAnchorLayoutPrivate::styleInfo() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGraphicsAnchorLayoutPrivate.styleInfo' has no cute function yet. "
        "Qt's 'QLayoutStyleInfo &QGraphicsAnchorLayoutPrivate::styleInfo() "
        "const': gives a type Python has no way to take yet.")
