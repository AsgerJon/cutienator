"""
QPathSegments binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qpathclipper_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QPathSegments to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QLineF, QPointF, QRectF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']


class QPathSegments(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPathSegments: a plain Python object standing in
  front of one C++ QPathSegments.

  What exists
  -----------

  Every function of Qt's QPathSegments that has a ritual and that Python can
  call so far, 11 names in all: 'intersections', 'segments', 'points',
  'segmentAt', 'lineAt', 'elementBounds', 'pathId', 'pointAt', 'addPoint',
  'intersectionAt', 'addIntersection'. It can be made from Python, in 1 way;
  see '__init__'.

  What has no ritual
  ------------------

  3 of the 15 functions Qt declares: 2 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'QPathSegments.

  What to expect
  --------------

  - The C++ QPathSegments is created at the first use, not by
    'QPathSegments(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPathSegments.
  - Each name of Qt's QPathSegments that has no cute function yet, 'addPath',
    'mergePoints', 'setPath', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QPathSegments, each a class in here as in
  #  C++.

  class Intersection(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QPathSegments::Intersection: a plain Python object
    standing in front of one C++ QPathSegments::Intersection.

    C++ hands a QPathSegments::Intersection around as a copy, so every C++
    QPathSegments::Intersection behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QPathSegments::Intersection that has a ritual and
    that Python can call so far, 1 name in all: '__lt__'. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QPathSegments::Intersection::~Intersection()': the destructor:
      Python removes its C++ QPathSegments::Intersection by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QPathSegments::Intersection is created at the first use, not by
      'QPathSegments::Intersection(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QPathSegments::Intersection back gives a copy the
      ritual made for Python, in a new cute QPathSegments::Intersection.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QPathSegments::Intersection'

    #  Qt's '~QPathSegments::Intersection()'. Naming it makes this a value
    #  class: Python owns every C++ QPathSegments::Intersection behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN13QPathSegments12IntersectionD1Ev'

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

    @overload(THIS)
    def __lt__(self, o: QPathSegments.Intersection) -> bool:
      """
      Calls Qt's 'bool QPathSegments::Intersection::operator<(const
      Intersection &o) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qpathsegments-intersection.html#operator<

      Parameters
      ----------

      o : QPathSegments.Intersection
        Passed on as a value: Qt reads the C++ QPathSegments::Intersection,
        which stays Python's own.
      """
      #  bool QPathSegments::Intersection::operator<(const Intersection &o)
      #      const
      return self.uglySide.call(
          'ritual_ZNK13QPathSegments12IntersectionltERKS0_',
          self._valueOf(o),
      )

    @overload.fallback
    def __lt__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

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

  class Segment(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QPathSegments::Segment: a plain Python object
    standing in front of one C++ QPathSegments::Segment.

    C++ hands a QPathSegments::Segment around as a copy, so every C++
    QPathSegments::Segment behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QPathSegments::Segment yet. It can be made from
    Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QPathSegments::Segment::~Segment()': the destructor: Python
      removes its C++ QPathSegments::Segment by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QPathSegments::Segment is created at the first use, not by
      'QPathSegments::Segment(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QPathSegments::Segment back gives a copy the ritual
      made for Python, in a new cute QPathSegments::Segment.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QPathSegments::Segment'

    #  Qt's '~QPathSegments::Segment()'. Naming it makes this a value class:
    #  Python owns every C++ QPathSegments::Segment behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN13QPathSegments7SegmentD1Ev'

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

    @overload(int, int, int)
    def __init__(self, pathId: int, vertexA: int, vertexB: int) -> None:
      """
      Notes what was given, for Qt's 'QPathSegments::Segment::Segment(int
      pathId, int vertexA, int vertexB)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qpathsegments-segment.html#Segment

      Parameters
      ----------

      pathId : int
        Passed on as it is.

      vertexA : int
        Passed on as it is.

      vertexB : int
        Passed on as it is.
      """
      #  QPathSegments::Segment::Segment(int pathId, int vertexA, int
      #      vertexB)
      self._noteCreation(QPathSegments.Segment, lambda: Rituals.call(
          'ritual_ZN13QPathSegments7SegmentC1Eiii', pathId, vertexA, vertexB,
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
  __qt_class__ = 'QPathSegments'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def intersections(self) -> int:
    """
    Calls Qt's 'int QPathSegments::intersections() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpathsegments.html#intersections
    """
    #  int QPathSegments::intersections() const
    return self.uglySide.call('ritual_ZNK13QPathSegments13intersectionsEv')

  def segments(self) -> int:
    """
    Calls Qt's 'int QPathSegments::segments() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpathsegments.html#segments
    """
    #  int QPathSegments::segments() const
    return self.uglySide.call('ritual_ZNK13QPathSegments8segmentsEv')

  def points(self) -> int:
    """
    Calls Qt's 'int QPathSegments::points() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpathsegments.html#points
    """
    #  int QPathSegments::points() const
    return self.uglySide.call('ritual_ZNK13QPathSegments6pointsEv')

  @overload(int)
  def segmentAt(self, index: int) -> Segment:
    """
    Calls Qt's 'const Segment &QPathSegments::segmentAt(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpathsegments.html#segmentAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Segment
      A new cute QPathSegments::Segment around the copy Qt gave back. Python
      owns it.
    """
    #  const Segment &QPathSegments::segmentAt(int index) const
    address = self.uglySide.call(
        'ritual_ZNK13QPathSegments9segmentAtEi', index,
    )
    return QPathSegments.Segment._cuteOwning(address)

  @overload(int)
  def lineAt(self, index: int) -> QLineF:
    """
    Calls Qt's 'const QLineF QPathSegments::lineAt(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpathsegments.html#lineAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QLineF
      A new cute QLineF around the copy Qt gave back. Python owns it.
    """
    #  const QLineF QPathSegments::lineAt(int index) const
    address = self.uglySide.call('ritual_ZNK13QPathSegments6lineAtEi', index)
    from ..QtCore import QLineF
    return QLineF._cuteOwning(address)

  @overload(int)
  def elementBounds(self, index: int) -> QRectF:
    """
    Calls Qt's 'const QRectF &QPathSegments::elementBounds(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpathsegments.html#elementBounds

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  const QRectF &QPathSegments::elementBounds(int index) const
    address = self.uglySide.call(
        'ritual_ZNK13QPathSegments13elementBoundsEi', index,
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(int)
  def pathId(self, index: int) -> int:
    """
    Calls Qt's 'int QPathSegments::pathId(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpathsegments.html#pathId

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  int QPathSegments::pathId(int index) const
    return self.uglySide.call('ritual_ZNK13QPathSegments6pathIdEi', index)

  @overload(int)
  def pointAt(self, vertex: int) -> QPointF:
    """
    Calls Qt's 'const QPointF &QPathSegments::pointAt(int vertex) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpathsegments.html#pointAt

    Parameters
    ----------

    vertex : int
      Passed on as it is.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  const QPointF &QPathSegments::pointAt(int vertex) const
    address = self.uglySide.call(
        'ritual_ZNK13QPathSegments7pointAtEi', vertex,
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(int)
  def intersectionAt(self, index: int) -> Optional[Intersection]:
    """
    Calls Qt's 'const Intersection *QPathSegments::intersectionAt(int index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qpathsegments.html#intersectionAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[Intersection]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Intersection *QPathSegments::intersectionAt(int index) const
    address = self.uglySide.call(
        'ritual_ZNK13QPathSegments14intersectionAtEi', index,
    )
    return QPathSegments.Intersection._cuteAt(address)

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

  @overload(int)
  def __init__(self, reserve: int) -> None:
    """
    Notes what was given, for Qt's 'QPathSegments::QPathSegments(int
    reserve)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpathsegments.html#QPathSegments

    Parameters
    ----------

    reserve : int
      Passed on as it is.
    """
    #  QPathSegments::QPathSegments(int reserve)
    self._noteCreation(QPathSegments, lambda: Rituals.call(
        'ritual_ZN13QPathSegmentsC1Ei', reserve,
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

  @overload(QPointF)
  def addPoint(self, point: QPointF) -> int:
    """
    Calls Qt's 'int QPathSegments::addPoint(const QPointF &point)'.

    Qt's own words: https://doc.qt.io/qt-6/qpathsegments.html#addPoint

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  int QPathSegments::addPoint(const QPointF &point)
    return self.uglySide.call(
        'ritual_ZN13QPathSegments8addPointERK7QPointF',
        self._valueOf(point, 'QPointF'),
    )

  @overload(int, Intersection)
  def addIntersection(self, index: int, intersection: Intersection) -> None:
    """
    Calls Qt's 'void QPathSegments::addIntersection(int index, const
    Intersection &intersection)'.

    Qt's own words: https://doc.qt.io/qt-6/qpathsegments.html#addIntersection

    Parameters
    ----------

    index : int
      Passed on as it is.

    intersection : Intersection
      Passed on as a value: Qt reads the C++ QPathSegments::Intersection,
      which stays Python's own.
    """
    #  void QPathSegments::addIntersection(int index, const Intersection
    #      &intersection)
    self.uglySide.call(
        'ritual_ZN13QPathSegments15addIntersectionEiRKNS_12IntersectionE',
        index, self._valueOf(intersection),
    )

  @staticmethod
  def addPath(*__, **_) -> Never:
    """
    Qt's 'void QPathSegments::addPath(const QPainterPath &path)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'comparePoints'.
    """
    raise NotImplementedError(
        "'QPathSegments.addPath' has no cute function yet. Qt's 'void "
        "QPathSegments::addPath(const QPainterPath &path)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'comparePoints'.")

  @staticmethod
  def mergePoints(*__, **_) -> Never:
    """
    Qt's 'void QPathSegments::mergePoints()': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file: no
    member named 'qTraverseKdPointTree' in the global namespace.
    """
    raise NotImplementedError(
        "'QPathSegments.mergePoints' has no cute function yet. Qt's 'void "
        "QPathSegments::mergePoints()': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "no member named 'qTraverseKdPointTree' in the global namespace.")

  @staticmethod
  def setPath(*__, **_) -> Never:
    """
    Qt's 'void QPathSegments::setPath(const QPainterPath &path)': leans on
    'QPathSegments::addPath(QPainterPath const&)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QPathSegments.setPath' has no cute function yet. Qt's 'void "
        "QPathSegments::setPath(const QPainterPath &path)': leans on "
        "'QPathSegments::addPath(QPainterPath const&)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")
