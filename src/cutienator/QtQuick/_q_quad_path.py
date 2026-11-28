"""
QQuadPath binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquadpath_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQuadPath to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QDebug, QRectF
  from ..QtGui import QPainterPath, QVector2D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDebug = WAIT['QDebug']
  QPainterPath = WAIT['QPainterPath']
  QVector2D = WAIT['QVector2D']


class QQuadPath(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuadPath: a plain Python object standing in front of
  one C++ QQuadPath.

  C++ hands a QQuadPath around as a copy, so every C++ QQuadPath behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuadPath that has a ritual and that Python can call
  so far, 30 names in all: 'moveTo', 'lineTo', 'quadTo', 'elementAt',
  'indexOfChildAt', 'controlPointRect', 'fillRule', 'setFillRule', 'reserve',
  'elementCount', 'isEmpty', 'elementCountRecursive', 'lineCount',
  'fromPainterPath', 'toPainterPath', 'asSvgString', 'addCurvatureData',
  'flattened', 'splitElementAt', 'contains', 'closestPointOnLine',
  'isPointOnLeft', 'isPointOnLine', 'isPointNearLine', 'testHint', 'setHint',
  'pathHints', 'setPathHints', 'addElement', '__rlshift__'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Element &QQuadPath::elementAt(int i)': gives a type Python has no
    way to take yet.
  - Qt's 'QQuadPath QQuadPath::subPathsClosed(bool *didClose) const': takes a
    number to change where it is.
  - Qt's 'QQuadPath QQuadPath::dashed(qreal lineWidth, const QList<qreal>
    &dashPattern, qreal dashOffset) const': takes a type Python has no way to
    hand over yet.
  - Qt's 'Element::FillSide QQuadPath::fillSideOf(int elementIdx, float
    elementT) const': gives the enum 'QQuadPath::Element::FillSide', whose
    class cannot be named here.
  - Qt's 'Element::FillSide QQuadPath::coordinateOrderOfElement(const Element
    &element) const': gives the enum 'QQuadPath::Element::FillSide', whose
    class cannot be named here.
  - Qt's 'QQuadPath::~QQuadPath()': the destructor: Python removes its C++
    QQuadPath by it, and has no other use for it.

  What has no ritual
  ------------------

  4 of the 42 functions Qt declares: 4 a template.

  What to expect
  --------------

  - The C++ QQuadPath is created at the first use, not by 'QQuadPath(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuadPath back gives a copy the ritual made for
    Python, in a new cute QQuadPath.
  - Each name of Qt's QQuadPath that has no cute function yet,
    'coordinateOrderOfElement', 'dashed', 'fillSideOf', 'iterateChildrenOf',
    'iterateElements', 'subPathsClosed', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuadPath, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class PathHint(CuteFlags, number='unsigned char'):
    """
    The flags enum 'QQuadPath::PathHint' of Qt, with the 7 names Qt gives in
    it. Qt names the type of its combinations 'QQuadPath::PathHints'.
    """

    PathLinear = 0x1
    PathQuadratic = 0x2
    PathConvex = 0x4
    PathFillOnRight = 0x8
    PathSolid = 0x10
    PathNonIntersecting = 0x20
    PathNonOverlappingControlPointTriangles = 0x40

  PathHints = PathHint

  #  The classes Qt writes inside QQuadPath, each a class in here as in C++.

  class Element(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuadPath::Element: a plain Python object standing
    in front of one C++ QQuadPath::Element.

    C++ hands a QQuadPath::Element around as a copy, so every C++
    QQuadPath::Element behind a cute one is Python's own: it is removed, by
    the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QQuadPath::Element that has a ritual and that
    Python can call so far, 22 names in all: 'isSubpathStart',
    'isSubpathEnd', 'isLine', 'isConvex', 'startPoint', 'controlPoint',
    'endPoint', 'midPoint', 'referencePoint', 'segmentFromTo', 'reversed',
    'childCount', 'indexOfChild', 'pointAtFraction', 'tangentAtFraction',
    'normalAtFraction', 'extent', 'setAsConvex', 'setFillOnRight',
    'isFillOnRight', 'isControlPointOnLeft', '__rlshift__'. It can be made
    from Python, in 3 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'int QQuadPath::Element::intersectionsAtY(float y, float
      *fractions, bool swapXY) const': takes a number to change where it is.
    - Qt's 'QQuadPath::Element::~Element()': the destructor: Python removes
      its C++ QQuadPath::Element by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QQuadPath::Element is created at the first use, not by
      'QQuadPath::Element(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuadPath::Element back gives a copy the ritual
      made for Python, in a new cute QQuadPath::Element.
    - Each name of Qt's QQuadPath::Element that has no cute function yet,
      'intersectionsAtY', holds a function that raises 'NotImplementedError',
      and its docstring says why.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QDebug = WAIT['QDebug']
      QVector2D = WAIT['QVector2D']

    #  The enums Qt writes inside QQuadPath::Element, each a class in here as
    #  in C++, and the names Qt has for the combinations of its flags enums.

    class CurvatureFlags(CuteNum):
      """
      The enum 'QQuadPath::Element::CurvatureFlags' of Qt, with the 3 names
      Qt gives in it.
      """

      CurvatureUndetermined = Kee[int](0)
      FillOnRight = Kee[int](1)
      Convex = Kee[int](2)

    class FillSide(CuteNum):
      """
      The enum 'QQuadPath::Element::FillSide' of Qt, with the 4 names Qt
      gives in it.
      """

      FillSideUndetermined = Kee[int](0)
      FillSideRight = Kee[int](1)
      FillSideLeft = Kee[int](2)
      FillSideBoth = Kee[int](3)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuadPath::Element'

    #  Qt's '~QQuadPath::Element()'. Naming it makes this a value class:
    #  Python owns every C++ QQuadPath::Element behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN9QQuadPath7ElementD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def isSubpathStart(self) -> bool:
      """
      Calls Qt's 'bool QQuadPath::Element::isSubpathStart() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquadpath-element.html#isSubpathStart
      """
      #  bool QQuadPath::Element::isSubpathStart() const
      return self.uglySide.call(
          'ritual_ZNK9QQuadPath7Element14isSubpathStartEv',
      )

    def isSubpathEnd(self) -> bool:
      """
      Calls Qt's 'bool QQuadPath::Element::isSubpathEnd() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquadpath-element.html#isSubpathEnd
      """
      #  bool QQuadPath::Element::isSubpathEnd() const
      return self.uglySide.call(
          'ritual_ZNK9QQuadPath7Element12isSubpathEndEv',
      )

    def isLine(self) -> bool:
      """
      Calls Qt's 'bool QQuadPath::Element::isLine() const'.

      Qt's own words: https://doc.qt.io/qt-6/qquadpath-element.html#isLine
      """
      #  bool QQuadPath::Element::isLine() const
      return self.uglySide.call('ritual_ZNK9QQuadPath7Element6isLineEv')

    def isConvex(self) -> bool:
      """
      Calls Qt's 'bool QQuadPath::Element::isConvex() const'.

      Qt's own words: https://doc.qt.io/qt-6/qquadpath-element.html#isConvex
      """
      #  bool QQuadPath::Element::isConvex() const
      return self.uglySide.call('ritual_ZNK9QQuadPath7Element8isConvexEv')

    def startPoint(self) -> QVector2D:
      """
      Calls Qt's 'QVector2D QQuadPath::Element::startPoint() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquadpath-element.html#startPoint

      Returns
      -------

      QVector2D
        A new cute QVector2D around the copy Qt gave back. Python owns it.
      """
      #  QVector2D QQuadPath::Element::startPoint() const
      address = self.uglySide.call(
          'ritual_ZNK9QQuadPath7Element10startPointEv',
      )
      from ..QtGui import QVector2D
      return QVector2D._cuteOwning(address)

    def controlPoint(self) -> QVector2D:
      """
      Calls Qt's 'QVector2D QQuadPath::Element::controlPoint() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquadpath-element.html#controlPoint

      Returns
      -------

      QVector2D
        A new cute QVector2D around the copy Qt gave back. Python owns it.
      """
      #  QVector2D QQuadPath::Element::controlPoint() const
      address = self.uglySide.call(
          'ritual_ZNK9QQuadPath7Element12controlPointEv',
      )
      from ..QtGui import QVector2D
      return QVector2D._cuteOwning(address)

    def endPoint(self) -> QVector2D:
      """
      Calls Qt's 'QVector2D QQuadPath::Element::endPoint() const'.

      Qt's own words: https://doc.qt.io/qt-6/qquadpath-element.html#endPoint

      Returns
      -------

      QVector2D
        A new cute QVector2D around the copy Qt gave back. Python owns it.
      """
      #  QVector2D QQuadPath::Element::endPoint() const
      address = self.uglySide.call('ritual_ZNK9QQuadPath7Element8endPointEv')
      from ..QtGui import QVector2D
      return QVector2D._cuteOwning(address)

    def midPoint(self) -> QVector2D:
      """
      Calls Qt's 'QVector2D QQuadPath::Element::midPoint() const'.

      Qt's own words: https://doc.qt.io/qt-6/qquadpath-element.html#midPoint

      Returns
      -------

      QVector2D
        A new cute QVector2D around the copy Qt gave back. Python owns it.
      """
      #  QVector2D QQuadPath::Element::midPoint() const
      address = self.uglySide.call('ritual_ZNK9QQuadPath7Element8midPointEv')
      from ..QtGui import QVector2D
      return QVector2D._cuteOwning(address)

    def referencePoint(self) -> QVector2D:
      """
      Calls Qt's 'QVector2D QQuadPath::Element::referencePoint() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquadpath-element.html#referencePoint

      Returns
      -------

      QVector2D
        A new cute QVector2D around the copy Qt gave back. Python owns it.
      """
      #  QVector2D QQuadPath::Element::referencePoint() const
      address = self.uglySide.call(
          'ritual_ZNK9QQuadPath7Element14referencePointEv',
      )
      from ..QtGui import QVector2D
      return QVector2D._cuteOwning(address)

    @overload(float, float)
    def segmentFromTo(self, t0: float, t1: float) -> QQuadPath.Element:
      """
      Calls Qt's 'Element QQuadPath::Element::segmentFromTo(float t0, float
      t1) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquadpath-element.html#segmentFromTo

      Parameters
      ----------

      t0 : float
        Passed on as it is.

      t1 : float
        Passed on as it is.

      Returns
      -------

      QQuadPath.Element
        A new cute QQuadPath::Element around the copy Qt gave back. Python
        owns it.
      """
      #  Element QQuadPath::Element::segmentFromTo(float t0, float t1) const
      address = self.uglySide.call(
          'ritual_ZNK9QQuadPath7Element13segmentFromToEff', t0, t1,
      )
      return QQuadPath.Element._cuteOwning(address)

    def reversed(self) -> QQuadPath.Element:
      """
      Calls Qt's 'Element QQuadPath::Element::reversed() const'.

      Qt's own words: https://doc.qt.io/qt-6/qquadpath-element.html#reversed

      Returns
      -------

      QQuadPath.Element
        A new cute QQuadPath::Element around the copy Qt gave back. Python
        owns it.
      """
      #  Element QQuadPath::Element::reversed() const
      address = self.uglySide.call('ritual_ZNK9QQuadPath7Element8reversedEv')
      return QQuadPath.Element._cuteOwning(address)

    def childCount(self) -> int:
      """
      Calls Qt's 'int QQuadPath::Element::childCount() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquadpath-element.html#childCount
      """
      #  int QQuadPath::Element::childCount() const
      return self.uglySide.call('ritual_ZNK9QQuadPath7Element10childCountEv')

    @overload(int)
    def indexOfChild(self, childNumber: int) -> int:
      """
      Calls Qt's 'int QQuadPath::Element::indexOfChild(int childNumber)
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquadpath-element.html#indexOfChild

      Parameters
      ----------

      childNumber : int
        Passed on as it is.
      """
      #  int QQuadPath::Element::indexOfChild(int childNumber) const
      return self.uglySide.call(
          'ritual_ZNK9QQuadPath7Element12indexOfChildEi', childNumber,
      )

    @overload(float)
    def pointAtFraction(self, t: float) -> QVector2D:
      """
      Calls Qt's 'QVector2D QQuadPath::Element::pointAtFraction(float t)
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquadpath-element.html#pointAtFraction

      Parameters
      ----------

      t : float
        Passed on as it is.

      Returns
      -------

      QVector2D
        A new cute QVector2D around the copy Qt gave back. Python owns it.
      """
      #  QVector2D QQuadPath::Element::pointAtFraction(float t) const
      address = self.uglySide.call(
          'ritual_ZNK9QQuadPath7Element15pointAtFractionEf', t,
      )
      from ..QtGui import QVector2D
      return QVector2D._cuteOwning(address)

    @overload(float)
    def tangentAtFraction(self, t: float) -> QVector2D:
      """
      Calls Qt's 'QVector2D QQuadPath::Element::tangentAtFraction(float t)
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquadpath-element.html#tangentAtFraction

      Parameters
      ----------

      t : float
        Passed on as it is.

      Returns
      -------

      QVector2D
        A new cute QVector2D around the copy Qt gave back. Python owns it.
      """
      #  QVector2D QQuadPath::Element::tangentAtFraction(float t) const
      address = self.uglySide.call(
          'ritual_ZNK9QQuadPath7Element17tangentAtFractionEf', t,
      )
      from ..QtGui import QVector2D
      return QVector2D._cuteOwning(address)

    @overload(float)
    def normalAtFraction(self, t: float) -> QVector2D:
      """
      Calls Qt's 'QVector2D QQuadPath::Element::normalAtFraction(float t)
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquadpath-element.html#normalAtFraction

      Parameters
      ----------

      t : float
        Passed on as it is.

      Returns
      -------

      QVector2D
        A new cute QVector2D around the copy Qt gave back. Python owns it.
      """
      #  QVector2D QQuadPath::Element::normalAtFraction(float t) const
      address = self.uglySide.call(
          'ritual_ZNK9QQuadPath7Element16normalAtFractionEf', t,
      )
      from ..QtGui import QVector2D
      return QVector2D._cuteOwning(address)

    def extent(self) -> float:
      """
      Calls Qt's 'float QQuadPath::Element::extent() const'.

      Qt's own words: https://doc.qt.io/qt-6/qquadpath-element.html#extent
      """
      #  float QQuadPath::Element::extent() const
      return self.uglySide.call('ritual_ZNK9QQuadPath7Element6extentEv')

    def isFillOnRight(self) -> bool:
      """
      Calls Qt's 'bool QQuadPath::Element::isFillOnRight() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquadpath-element.html#isFillOnRight
      """
      #  bool QQuadPath::Element::isFillOnRight() const
      return self.uglySide.call(
          'ritual_ZNK9QQuadPath7Element13isFillOnRightEv',
      )

    def isControlPointOnLeft(self) -> bool:
      """
      Calls Qt's 'bool QQuadPath::Element::isControlPointOnLeft() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquadpath-element.html#isControlPointOnLeft
      """
      #  bool QQuadPath::Element::isControlPointOnLeft() const
      return self.uglySide.call(
          'ritual_ZNK9QQuadPath7Element20isControlPointOnLeftEv',
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(bool)
    def setAsConvex(self, isConvex: bool) -> None:
      """
      Calls Qt's 'void QQuadPath::Element::setAsConvex(bool isConvex)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquadpath-element.html#setAsConvex

      Parameters
      ----------

      isConvex : bool
        Passed on as it is.
      """
      #  void QQuadPath::Element::setAsConvex(bool isConvex)
      self.uglySide.call(
          'ritual_ZN9QQuadPath7Element11setAsConvexEb', isConvex,
      )

    @overload(bool)
    def setFillOnRight(self, isFillOnRight: bool) -> None:
      """
      Calls Qt's 'void QQuadPath::Element::setFillOnRight(bool
      isFillOnRight)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquadpath-element.html#setFillOnRight

      Parameters
      ----------

      isFillOnRight : bool
        Passed on as it is.
      """
      #  void QQuadPath::Element::setFillOnRight(bool isFillOnRight)
      self.uglySide.call(
          'ritual_ZN9QQuadPath7Element14setFillOnRightEb', isFillOnRight,
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(QDebug)
    def __rlshift__(self, a0: QDebug) -> QDebug:
      """
      Calls Qt's 'QDebug operator<<(QDebug a0, const QQuadPath::Element
      &a1)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquadpath-element.html#operator<<

      Parameters
      ----------

      a0 : QDebug
        Passed on as a value: Qt reads the C++ QDebug, which stays Python's
        own.

      Returns
      -------

      QDebug
        A new cute QDebug around the copy Qt gave back. Python owns it.
      """
      #  QDebug operator<<(QDebug a0, const QQuadPath::Element &a1)
      address = Rituals.call(
          'ritual_Zls6QDebugRKN9QQuadPath7ElementE',
          CuteMixin._valueOf(a0), CuteMixin._valueOf(self),
      )
      from ..QtCore import QDebug
      return QDebug._cuteOwning(address)

    @overload.fallback
    def __rlshift__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's 'QQuadPath::Element::Element()', which
      is called at the first use.

      Qt's own words: https://doc.qt.io/qt-6/qquadpath-element.html#Element
      """
      #  QQuadPath::Element::Element()
      self._noteCreation(QQuadPath.Element, lambda: Rituals.call(
          'ritual_ZN9QQuadPath7ElementC1Ev',
      ))

    @overload(QVector2D, QVector2D, QVector2D)
    def __init__(self, s: QVector2D, c: QVector2D, e: QVector2D) -> None:
      """
      Notes what was given, for Qt's 'QQuadPath::Element::Element(QVector2D
      s, QVector2D c, QVector2D e)', which is called at the first use.

      Qt's own words: https://doc.qt.io/qt-6/qquadpath-element.html#Element

      Parameters
      ----------

      s : QVector2D
        Passed on as a value: Qt reads the C++ QVector2D, which stays
        Python's own.

      c : QVector2D
        Passed on as a value: Qt reads the C++ QVector2D, which stays
        Python's own.

      e : QVector2D
        Passed on as a value: Qt reads the C++ QVector2D, which stays
        Python's own.
      """
      #  QQuadPath::Element::Element(QVector2D s, QVector2D c, QVector2D e)
      self._noteCreation(QQuadPath.Element, lambda: Rituals.call(
          'ritual_ZN9QQuadPath7ElementC1E9QVector2DS1_S1_',
          self._valueOf(s), self._valueOf(c), self._valueOf(e),
      ))

    @overload(QVector2D, QVector2D)
    def __init__(self, s: QVector2D, e: QVector2D) -> None:
      """
      Notes what was given, for Qt's 'QQuadPath::Element::Element(QVector2D
      s, QVector2D e)', which is called at the first use.

      Qt's own words: https://doc.qt.io/qt-6/qquadpath-element.html#Element

      Parameters
      ----------

      s : QVector2D
        Passed on as a value: Qt reads the C++ QVector2D, which stays
        Python's own.

      e : QVector2D
        Passed on as a value: Qt reads the C++ QVector2D, which stays
        Python's own.
      """
      #  QQuadPath::Element::Element(QVector2D s, QVector2D e)
      self._noteCreation(QQuadPath.Element, lambda: Rituals.call(
          'ritual_ZN9QQuadPath7ElementC1E9QVector2DS1_',
          self._valueOf(s), self._valueOf(e),
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

    @staticmethod
    def intersectionsAtY(*__, **_) -> Never:
      """
      Qt's 'int QQuadPath::Element::intersectionsAtY(float y, float
      *fractions, bool swapXY) const': takes a number to change where it is.
      """
      raise NotImplementedError(
          "'QQuadPath.Element.intersectionsAtY' has no cute function yet. "
          "Qt's 'int QQuadPath::Element::intersectionsAtY(float y, float "
          "*fractions, bool swapXY) const': takes a number to change where "
          "it is.")

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QPainterPath)
  @overload(QPainterPath, PathHints)
  def fromPainterPath(
      path: QPainterPath,
      hints: PathHints = PathHints(),
  ) -> QQuadPath:
    """
    Calls Qt's 'QQuadPath QQuadPath::fromPainterPath(const QPainterPath
    &path, PathHints hints)'.

    Qt's own words: https://doc.qt.io/qt-6/qquadpath.html#fromPainterPath

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.

    hints : PathHints
      Passed on as its number. May be left out, as in Qt: it is then
      PathHints().

    Returns
    -------

    QQuadPath
      A new cute QQuadPath around the copy Qt gave back. Python owns it.
    """
    #  QQuadPath QQuadPath::fromPainterPath(const QPainterPath &path,
    #      PathHints hints)
    address = Rituals.call(
        'ritual_ZN9QQuadPath15fromPainterPathERK12QPainterPath6QFlagsINS_8P'
        'athHintEE',
        CuteMixin._valueOf(path), hints.value,
    )
    return QQuadPath._cuteOwning(address)

  @staticmethod
  @overload(QVector2D, QVector2D, QVector2D)
  def closestPointOnLine(
      p: QVector2D,
      sp: QVector2D,
      ep: QVector2D,
  ) -> QVector2D:
    """
    Calls Qt's 'QVector2D QQuadPath::closestPointOnLine(const QVector2D &p,
    const QVector2D &sp, const QVector2D &ep)'.

    Qt's own words: https://doc.qt.io/qt-6/qquadpath.html#closestPointOnLine

    Parameters
    ----------

    p : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    sp : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    ep : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    Returns
    -------

    QVector2D
      A new cute QVector2D around the copy Qt gave back. Python owns it.
    """
    #  QVector2D QQuadPath::closestPointOnLine(const QVector2D &p, const
    #      QVector2D &sp, const QVector2D &ep)
    address = Rituals.call(
        'ritual_ZN9QQuadPath18closestPointOnLineERK9QVector2DS2_S2_',
        CuteMixin._valueOf(p), CuteMixin._valueOf(sp),
        CuteMixin._valueOf(ep),
    )
    from ..QtGui import QVector2D
    return QVector2D._cuteOwning(address)

  @staticmethod
  @overload(QVector2D, QVector2D, QVector2D)
  def isPointOnLeft(p: QVector2D, sp: QVector2D, ep: QVector2D) -> bool:
    """
    Calls Qt's 'bool QQuadPath::isPointOnLeft(const QVector2D &p, const
    QVector2D &sp, const QVector2D &ep)'.

    Qt's own words: https://doc.qt.io/qt-6/qquadpath.html#isPointOnLeft

    Parameters
    ----------

    p : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    sp : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    ep : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  bool QQuadPath::isPointOnLeft(const QVector2D &p, const QVector2D &sp,
    #      const QVector2D &ep)
    return Rituals.call(
        'ritual_ZN9QQuadPath13isPointOnLeftERK9QVector2DS2_S2_',
        CuteMixin._valueOf(p), CuteMixin._valueOf(sp),
        CuteMixin._valueOf(ep),
    )

  @staticmethod
  @overload(QVector2D, QVector2D, QVector2D)
  def isPointOnLine(p: QVector2D, sp: QVector2D, ep: QVector2D) -> bool:
    """
    Calls Qt's 'bool QQuadPath::isPointOnLine(const QVector2D &p, const
    QVector2D &sp, const QVector2D &ep)'.

    Qt's own words: https://doc.qt.io/qt-6/qquadpath.html#isPointOnLine

    Parameters
    ----------

    p : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    sp : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    ep : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  bool QQuadPath::isPointOnLine(const QVector2D &p, const QVector2D &sp,
    #      const QVector2D &ep)
    return Rituals.call(
        'ritual_ZN9QQuadPath13isPointOnLineERK9QVector2DS2_S2_',
        CuteMixin._valueOf(p), CuteMixin._valueOf(sp),
        CuteMixin._valueOf(ep),
    )

  @staticmethod
  @overload(QVector2D, QVector2D, QVector2D)
  def isPointNearLine(p: QVector2D, sp: QVector2D, ep: QVector2D) -> bool:
    """
    Calls Qt's 'bool QQuadPath::isPointNearLine(const QVector2D &p, const
    QVector2D &sp, const QVector2D &ep)'.

    Qt's own words: https://doc.qt.io/qt-6/qquadpath.html#isPointNearLine

    Parameters
    ----------

    p : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    sp : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    ep : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  bool QQuadPath::isPointNearLine(const QVector2D &p, const QVector2D
    #      &sp, const QVector2D &ep)
    return Rituals.call(
        'ritual_ZN9QQuadPath15isPointNearLineERK9QVector2DS2_S2_',
        CuteMixin._valueOf(p), CuteMixin._valueOf(sp),
        CuteMixin._valueOf(ep),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuadPath'

  #  Qt's '~QQuadPath()'. Naming it makes this a value class: Python owns
  #  every C++ QQuadPath behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QQuadPathD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def elementAt(self, i: int) -> Element:
    """
    Calls Qt's 'const Element &QQuadPath::elementAt(int i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquadpath.html#elementAt

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    Element
      A new cute QQuadPath::Element around the copy Qt gave back. Python owns
      it.
    """
    #  const Element &QQuadPath::elementAt(int i) const
    address = self.uglySide.call('ritual_ZNK9QQuadPath9elementAtEi', i)
    return QQuadPath.Element._cuteOwning(address)

  @overload(int, int)
  def indexOfChildAt(self, i: int, childNumber: int) -> int:
    """
    Calls Qt's 'int QQuadPath::indexOfChildAt(int i, int childNumber) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquadpath.html#indexOfChildAt

    Parameters
    ----------

    i : int
      Passed on as it is.

    childNumber : int
      Passed on as it is.
    """
    #  int QQuadPath::indexOfChildAt(int i, int childNumber) const
    return self.uglySide.call(
        'ritual_ZNK9QQuadPath14indexOfChildAtEii', i, childNumber,
    )

  def controlPointRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QQuadPath::controlPointRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquadpath.html#controlPointRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuadPath::controlPointRect() const
    address = self.uglySide.call('ritual_ZNK9QQuadPath16controlPointRectEv')
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def fillRule(self) -> Qt.FillRule:
    """
    Calls Qt's 'Qt::FillRule QQuadPath::fillRule() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquadpath.html#fillRule

    Returns
    -------

    Qt.FillRule
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.FillRule(number)'
      gives.
    """
    #  Qt::FillRule QQuadPath::fillRule() const
    return Qt.FillRule(self.uglySide.call('ritual_ZNK9QQuadPath8fillRuleEv'))

  def elementCount(self) -> int:
    """
    Calls Qt's 'int QQuadPath::elementCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquadpath.html#elementCount
    """
    #  int QQuadPath::elementCount() const
    return self.uglySide.call('ritual_ZNK9QQuadPath12elementCountEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QQuadPath::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquadpath.html#isEmpty
    """
    #  bool QQuadPath::isEmpty() const
    return self.uglySide.call('ritual_ZNK9QQuadPath7isEmptyEv')

  def elementCountRecursive(self) -> int:
    """
    Calls Qt's 'int QQuadPath::elementCountRecursive() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquadpath.html#elementCountRecursive
    """
    #  int QQuadPath::elementCountRecursive() const
    return self.uglySide.call(
        'ritual_ZNK9QQuadPath21elementCountRecursiveEv',
    )

  def lineCount(self) -> int:
    """
    Calls Qt's 'int QQuadPath::lineCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquadpath.html#lineCount
    """
    #  int QQuadPath::lineCount() const
    return self.uglySide.call('ritual_ZNK9QQuadPath9lineCountEv')

  def toPainterPath(self) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QQuadPath::toPainterPath() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquadpath.html#toPainterPath

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QQuadPath::toPainterPath() const
    address = self.uglySide.call('ritual_ZNK9QQuadPath13toPainterPathEv')
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  def asSvgString(self) -> str:
    """
    Calls Qt's 'QString QQuadPath::asSvgString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquadpath.html#asSvgString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuadPath::asSvgString() const
    return self.uglySide.call('ritual_ZNK9QQuadPath11asSvgStringEv')

  def flattened(self) -> QQuadPath:
    """
    Calls Qt's 'QQuadPath QQuadPath::flattened() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquadpath.html#flattened

    Returns
    -------

    QQuadPath
      A new cute QQuadPath around the copy Qt gave back. Python owns it.
    """
    #  QQuadPath QQuadPath::flattened() const
    address = self.uglySide.call('ritual_ZNK9QQuadPath9flattenedEv')
    return QQuadPath._cuteOwning(address)

  @overload(QVector2D)
  def contains(self, point: QVector2D) -> bool:
    """
    Calls Qt's 'bool QQuadPath::contains(const QVector2D &point) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquadpath.html#contains

    Parameters
    ----------

    point : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  bool QQuadPath::contains(const QVector2D &point) const
    return self.uglySide.call(
        'ritual_ZNK9QQuadPath8containsERK9QVector2D', self._valueOf(point),
    )

  @overload(QVector2D, int, int)
  def contains(self, point: QVector2D, fromIndex: int, toIndex: int) -> bool:
    """
    Calls Qt's 'bool QQuadPath::contains(const QVector2D &point, int
    fromIndex, int toIndex) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquadpath.html#contains

    Parameters
    ----------

    point : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    fromIndex : int
      Passed on as it is.

    toIndex : int
      Passed on as it is.
    """
    #  bool QQuadPath::contains(const QVector2D &point, int fromIndex, int
    #      toIndex) const
    return self.uglySide.call(
        'ritual_ZNK9QQuadPath8containsERK9QVector2Dii',
        self._valueOf(point), fromIndex, toIndex,
    )

  @overload(PathHint)
  def testHint(self, hint: PathHint) -> bool:
    """
    Calls Qt's 'bool QQuadPath::testHint(PathHint hint) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquadpath.html#testHint

    Parameters
    ----------

    hint : PathHint
      Passed on as its number.
    """
    #  bool QQuadPath::testHint(PathHint hint) const
    return self.uglySide.call(
        'ritual_ZNK9QQuadPath8testHintENS_8PathHintE', hint.value,
    )

  def pathHints(self) -> PathHints:
    """
    Calls Qt's 'PathHints QQuadPath::pathHints() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquadpath.html#pathHints

    Returns
    -------

    PathHints
      The value standing for the combination Qt gave back.
    """
    #  PathHints QQuadPath::pathHints() const
    return QQuadPath.PathHints(self.uglySide.call(
        'ritual_ZNK9QQuadPath9pathHintsEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.FillRule)
  def setFillRule(self, rule: Qt.FillRule) -> None:
    """
    Calls Qt's 'void QQuadPath::setFillRule(Qt::FillRule rule)'.

    Qt's own words: https://doc.qt.io/qt-6/qquadpath.html#setFillRule

    Parameters
    ----------

    rule : Qt.FillRule
      Passed on as its number.
    """
    #  void QQuadPath::setFillRule(Qt::FillRule rule)
    self.uglySide.call(
        'ritual_ZN9QQuadPath11setFillRuleEN2Qt8FillRuleE', rule.value,
    )

  @overload(PathHint)
  @overload(PathHint, bool)
  def setHint(self, hint: PathHint, on: bool = True) -> None:
    """
    Calls Qt's 'void QQuadPath::setHint(PathHint hint, bool on)'.

    Qt's own words: https://doc.qt.io/qt-6/qquadpath.html#setHint

    Parameters
    ----------

    hint : PathHint
      Passed on as its number.

    on : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QQuadPath::setHint(PathHint hint, bool on)
    self.uglySide.call(
        'ritual_ZN9QQuadPath7setHintENS_8PathHintEb', hint.value, on,
    )

  @overload(PathHints)
  def setPathHints(self, newHints: PathHints) -> None:
    """
    Calls Qt's 'void QQuadPath::setPathHints(PathHints newHints)'.

    Qt's own words: https://doc.qt.io/qt-6/qquadpath.html#setPathHints

    Parameters
    ----------

    newHints : PathHints
      Passed on as its number.
    """
    #  void QQuadPath::setPathHints(PathHints newHints)
    self.uglySide.call(
        'ritual_ZN9QQuadPath12setPathHintsE6QFlagsINS_8PathHintEE',
        newHints.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDebug)
  def __rlshift__(self, a0: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug a0, const QQuadPath &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qquadpath.html#operator<<

    Parameters
    ----------

    a0 : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug a0, const QQuadPath &a1)
    address = Rituals.call(
        'ritual_Zls6QDebugRK9QQuadPath',
        CuteMixin._valueOf(a0), CuteMixin._valueOf(self),
    )
    from ..QtCore import QDebug
    return QDebug._cuteOwning(address)

  @overload.fallback
  def __rlshift__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

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

  @overload(QVector2D)
  def moveTo(self, to: QVector2D) -> None:
    """
    Calls Qt's 'void QQuadPath::moveTo(const QVector2D &to)'.

    Qt's own words: https://doc.qt.io/qt-6/qquadpath.html#moveTo

    Parameters
    ----------

    to : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  void QQuadPath::moveTo(const QVector2D &to)
    self.uglySide.call(
        'ritual_ZN9QQuadPath6moveToERK9QVector2D', self._valueOf(to),
    )

  @overload(QVector2D)
  def lineTo(self, to: QVector2D) -> None:
    """
    Calls Qt's 'void QQuadPath::lineTo(const QVector2D &to)'.

    Qt's own words: https://doc.qt.io/qt-6/qquadpath.html#lineTo

    Parameters
    ----------

    to : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  void QQuadPath::lineTo(const QVector2D &to)
    self.uglySide.call(
        'ritual_ZN9QQuadPath6lineToERK9QVector2D', self._valueOf(to),
    )

  @overload(QVector2D, QVector2D)
  def quadTo(self, control: QVector2D, to: QVector2D) -> None:
    """
    Calls Qt's 'void QQuadPath::quadTo(const QVector2D &control, const
    QVector2D &to)'.

    Qt's own words: https://doc.qt.io/qt-6/qquadpath.html#quadTo

    Parameters
    ----------

    control : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    to : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  void QQuadPath::quadTo(const QVector2D &control, const QVector2D &to)
    self.uglySide.call(
        'ritual_ZN9QQuadPath6quadToERK9QVector2DS2_',
        self._valueOf(control), self._valueOf(to),
    )

  @overload(int)
  def reserve(self, size: int) -> None:
    """
    Calls Qt's 'void QQuadPath::reserve(int size)'.

    Qt's own words: https://doc.qt.io/qt-6/qquadpath.html#reserve

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QQuadPath::reserve(int size)
    self.uglySide.call('ritual_ZN9QQuadPath7reserveEi', size)

  def addCurvatureData(self) -> None:
    """
    Calls Qt's 'void QQuadPath::addCurvatureData()'.

    Qt's own words: https://doc.qt.io/qt-6/qquadpath.html#addCurvatureData
    """
    #  void QQuadPath::addCurvatureData()
    self.uglySide.call('ritual_ZN9QQuadPath16addCurvatureDataEv')

  @overload(int)
  def splitElementAt(self, index: int) -> None:
    """
    Calls Qt's 'void QQuadPath::splitElementAt(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qquadpath.html#splitElementAt

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQuadPath::splitElementAt(int index)
    self.uglySide.call('ritual_ZN9QQuadPath14splitElementAtEi', index)

  @overload(QVector2D, QVector2D)
  @overload(QVector2D, QVector2D, bool)
  def addElement(
      self,
      control: QVector2D,
      to: QVector2D,
      isLine: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QQuadPath::addElement(const QVector2D &control, const
    QVector2D &to, bool isLine)'.

    Qt's own words: https://doc.qt.io/qt-6/qquadpath.html#addElement

    Parameters
    ----------

    control : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    to : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    isLine : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuadPath::addElement(const QVector2D &control, const QVector2D
    #      &to, bool isLine)
    self.uglySide.call(
        'ritual_ZN9QQuadPath10addElementERK9QVector2DS2_b',
        self._valueOf(control), self._valueOf(to), isLine,
    )

  @overload(Element)
  def addElement(self, e: Element) -> None:
    """
    Calls Qt's 'void QQuadPath::addElement(const Element &e)'.

    Qt's own words: https://doc.qt.io/qt-6/qquadpath.html#addElement

    Parameters
    ----------

    e : Element
      Passed on as a value: Qt reads the C++ QQuadPath::Element, which stays
      Python's own.
    """
    #  void QQuadPath::addElement(const Element &e)
    self.uglySide.call(
        'ritual_ZN9QQuadPath10addElementERKNS_7ElementE', self._valueOf(e),
    )

  @staticmethod
  def coordinateOrderOfElement(*__, **_) -> Never:
    """
    Qt's 'Element::FillSide QQuadPath::coordinateOrderOfElement(const Element
    &element) const': gives the enum 'QQuadPath::Element::FillSide', whose
    class cannot be named here.
    """
    raise NotImplementedError(
        "'QQuadPath.coordinateOrderOfElement' has no cute function yet. "
        "Qt's 'Element::FillSide QQuadPath::coordinateOrderOfElement(const "
        "Element &element) const': gives the enum "
        "'QQuadPath::Element::FillSide', whose class cannot be named here.")

  @staticmethod
  def dashed(*__, **_) -> Never:
    """
    Qt's 'QQuadPath QQuadPath::dashed(qreal lineWidth, const QList<qreal>
    &dashPattern, qreal dashOffset) const': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQuadPath.dashed' has no cute function yet. Qt's 'QQuadPath "
        "QQuadPath::dashed(qreal lineWidth, const QList<qreal> "
        "&dashPattern, qreal dashOffset) const': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def fillSideOf(*__, **_) -> Never:
    """
    Qt's 'Element::FillSide QQuadPath::fillSideOf(int elementIdx, float
    elementT) const': gives the enum 'QQuadPath::Element::FillSide', whose
    class cannot be named here.
    """
    raise NotImplementedError(
        "'QQuadPath.fillSideOf' has no cute function yet. Qt's "
        "'Element::FillSide QQuadPath::fillSideOf(int elementIdx, float "
        "elementT) const': gives the enum 'QQuadPath::Element::FillSide', "
        "whose class cannot be named here.")

  @staticmethod
  def iterateChildrenOf(*__, **_) -> Never:
    """
    Qt's 'QQuadPath::iterateChildrenOf': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QQuadPath.iterateChildrenOf' has no cute function yet. Qt's "
        "'QQuadPath::iterateChildrenOf': a template: a pattern and no "
        "single function.")

  @staticmethod
  def iterateElements(*__, **_) -> Never:
    """
    Qt's 'QQuadPath::iterateElements': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QQuadPath.iterateElements' has no cute function yet. Qt's "
        "'QQuadPath::iterateElements': a template: a pattern and no single "
        "function.")

  @staticmethod
  def subPathsClosed(*__, **_) -> Never:
    """
    Qt's 'QQuadPath QQuadPath::subPathsClosed(bool *didClose) const': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QQuadPath.subPathsClosed' has no cute function yet. Qt's "
        "'QQuadPath QQuadPath::subPathsClosed(bool *didClose) const': takes "
        "a number to change where it is.")
