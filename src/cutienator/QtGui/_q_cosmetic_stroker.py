"""
QCosmeticStroker binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qcosmeticstroker_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QCosmeticStroker to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPoint, QPointF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']
  QPointF = WAIT['QPointF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCosmeticStroker(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCosmeticStroker: a plain Python object standing in
  front of one C++ QCosmeticStroker.

  C++ hands a QCosmeticStroker around as a copy, so every C++
  QCosmeticStroker behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCosmeticStroker that has a ritual and that Python
  can call so far, 3 names in all: 'drawPoints', 'renderCubic',
  'renderCubicSubdivision'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCosmeticStroker::~QCosmeticStroker()': the destructor: Python
    removes its C++ QCosmeticStroker by it, and has no other use for it.
  - Qt's 'bool QCosmeticStroker::clipLine(qreal &x1, qreal &y1, qreal &x2,
    qreal &y2)': takes a number to change where it is.

  What has no ritual
  ------------------

  6 of the 11 functions Qt declares: 3 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 3 leans on
  'QCosmeticStroker.

  What to expect
  --------------

  - The C++ QCosmeticStroker is created at the first use, not by
    'QCosmeticStroker(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCosmeticStroker back gives a copy the ritual made
    for Python, in a new cute QCosmeticStroker.
  - Each name of Qt's QCosmeticStroker that has no cute function yet,
    '__init__', 'calculateLastPoint', 'clipLine', 'drawLine', 'drawPath',
    'setup', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QCosmeticStroker, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Caps(CuteNum):
    """
    The enum 'QCosmeticStroker::Caps' of Qt, with the 3 names Qt gives in it.
    """

    NoCaps = Kee[int](0)
    CapBegin = Kee[int](1)
    CapEnd = Kee[int](2)

  class Direction(CuteNum):
    """
    The enum 'QCosmeticStroker::Direction' of Qt, with the 7 names Qt gives
    in it.
    """

    NoDirection = Kee[int](0)
    TopToBottom = Kee[int](1)
    BottomToTop = Kee[int](2)
    LeftToRight = Kee[int](4)
    RightToLeft = Kee[int](8)
    VerticalMask = Kee[int](3)
    HorizontalMask = Kee[int](12)

  #  The classes Qt writes inside QCosmeticStroker, each a class in here as
  #  in C++.

  class Point(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QCosmeticStroker::Point: a plain Python object
    standing in front of one C++ QCosmeticStroker::Point.

    C++ hands a QCosmeticStroker::Point around as a copy, so every C++
    QCosmeticStroker::Point behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QCosmeticStroker::Point yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QCosmeticStroker::Point::~Point()': the destructor: Python
      removes its C++ QCosmeticStroker::Point by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QCosmeticStroker::Point is created at the first use, not by
      'QCosmeticStroker::Point(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QCosmeticStroker::Point back gives a copy the
      ritual made for Python, in a new cute QCosmeticStroker::Point.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QCosmeticStroker::Point'

    #  Qt's '~QCosmeticStroker::Point()'. Naming it makes this a value class:
    #  Python owns every C++ QCosmeticStroker::Point behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN16QCosmeticStroker5PointD1Ev'

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

  class PointF(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QCosmeticStroker::PointF: a plain Python object
    standing in front of one C++ QCosmeticStroker::PointF.

    C++ hands a QCosmeticStroker::PointF around as a copy, so every C++
    QCosmeticStroker::PointF behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QCosmeticStroker::PointF yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QCosmeticStroker::PointF::~PointF()': the destructor: Python
      removes its C++ QCosmeticStroker::PointF by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QCosmeticStroker::PointF is created at the first use, not by
      'QCosmeticStroker::PointF(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QCosmeticStroker::PointF back gives a copy the
      ritual made for Python, in a new cute QCosmeticStroker::PointF.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QCosmeticStroker::PointF'

    #  Qt's '~QCosmeticStroker::PointF()'. Naming it makes this a value
    #  class: Python owns every C++ QCosmeticStroker::PointF behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN16QCosmeticStroker6PointFD1Ev'

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCosmeticStroker'

  #  Qt's '~QCosmeticStroker()'. Naming it makes this a value class: Python
  #  owns every C++ QCosmeticStroker behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QCosmeticStrokerD1Ev'

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QCosmeticStroker::QCosmeticStroker(QRasterPaintEngineState *s,
    const QRect &dr, const QRect &dr_unclipped)': leans on
    'QCosmeticStroker::setup()', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCosmeticStroker.__init__' has no cute function yet. Qt's "
        "'QCosmeticStroker::QCosmeticStroker(QRasterPaintEngineState *s, "
        "const QRect &dr, const QRect &dr_unclipped)': leans on "
        "'QCosmeticStroker::setup()', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

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

  @overload(QPoint, int)
  @overload(NoneType, int)
  def drawPoints(self, points: Optional[QPoint], num: int) -> None:
    """
    Calls Qt's 'void QCosmeticStroker::drawPoints(const QPoint *points, int
    num)'.

    Qt's own words: https://doc.qt.io/qt-6/qcosmeticstroker.html#drawPoints

    Parameters
    ----------

    points : Optional[QPoint]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    num : int
      Passed on as it is.
    """
    #  void QCosmeticStroker::drawPoints(const QPoint *points, int num)
    self.uglySide.call(
        'ritual_ZN16QCosmeticStroker10drawPointsEPK6QPointi',
        self._addressOf(points), num,
    )

  @overload(QPointF, QPointF, QPointF, QPointF, int)
  def renderCubic(
      self,
      p1: QPointF,
      p2: QPointF,
      p3: QPointF,
      p4: QPointF,
      caps: int,
  ) -> None:
    """
    Calls Qt's 'void QCosmeticStroker::renderCubic(const QPointF &p1, const
    QPointF &p2, const QPointF &p3, const QPointF &p4, int caps)'.

    Qt's own words: https://doc.qt.io/qt-6/qcosmeticstroker.html#renderCubic

    Parameters
    ----------

    p1 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    p2 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    p3 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    p4 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    caps : int
      Passed on as it is.
    """
    #  void QCosmeticStroker::renderCubic(const QPointF &p1, const QPointF
    #      &p2, const QPointF &p3, const QPointF &p4, int caps)
    self.uglySide.call(
        'ritual_ZN16QCosmeticStroker11renderCubicERK7QPointFS2_S2_S2_i',
        self._valueOf(p1, 'QPointF'), self._valueOf(p2, 'QPointF'),
        self._valueOf(p3, 'QPointF'), self._valueOf(p4, 'QPointF'), caps,
    )

  @overload(PointF, int, int)
  @overload(NoneType, int, int)
  def renderCubicSubdivision(
      self,
      points: Optional[PointF],
      level: int,
      caps: int,
  ) -> None:
    """
    Calls Qt's 'void QCosmeticStroker::renderCubicSubdivision(PointF *points,
    int level, int caps)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcosmeticstroker.html#renderCubicSubdivision

    Parameters
    ----------

    points : Optional[PointF]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    level : int
      Passed on as it is.

    caps : int
      Passed on as it is.
    """
    #  void QCosmeticStroker::renderCubicSubdivision(PointF *points, int
    #      level, int caps)
    self.uglySide.call(
        'ritual_ZN16QCosmeticStroker22renderCubicSubdivisionEPNS_6PointFEii',
        self._addressOf(points), level, caps,
    )

  @staticmethod
  def calculateLastPoint(*__, **_) -> Never:
    """
    Qt's 'void QCosmeticStroker::calculateLastPoint(qreal rx1, qreal ry1,
    qreal rx2, qreal ry2)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: use of undeclared
    identifier 'toF26Dot6'.
    """
    raise NotImplementedError(
        "'QCosmeticStroker.calculateLastPoint' has no cute function yet. "
        "Qt's 'void QCosmeticStroker::calculateLastPoint(qreal rx1, qreal "
        "ry1, qreal rx2, qreal ry2)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'toF26Dot6'.")

  @staticmethod
  def clipLine(*__, **_) -> Never:
    """
    Qt's 'bool QCosmeticStroker::clipLine(qreal &x1, qreal &y1, qreal &x2,
    qreal &y2)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QCosmeticStroker.clipLine' has no cute function yet. Qt's 'bool "
        "QCosmeticStroker::clipLine(qreal &x1, qreal &y1, qreal &x2, qreal "
        "&y2)': takes a number to change where it is.")

  @staticmethod
  def drawLine(*__, **_) -> Never:
    """
    Qt's 'void QCosmeticStroker::drawLine(const QPointF &p1, const QPointF
    &p2)': leans on 'QCosmeticStroker::drawPoints(QPointF const*, int)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QCosmeticStroker.drawLine' has no cute function yet. Qt's 'void "
        "QCosmeticStroker::drawLine(const QPointF &p1, const QPointF &p2)': "
        "leans on 'QCosmeticStroker::drawPoints(QPointF const*, int)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def drawPath(*__, **_) -> Never:
    """
    Qt's 'void QCosmeticStroker::drawPath(const QVectorPath &path)': leans on
    'QCosmeticStroker::calculateLastPoint(double, double, double, double)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QCosmeticStroker.drawPath' has no cute function yet. Qt's 'void "
        "QCosmeticStroker::drawPath(const QVectorPath &path)': leans on "
        "'QCosmeticStroker::calculateLastPoint(double, double, double, "
        "double)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def setup(*__, **_) -> Never:
    """
    Qt's 'void QCosmeticStroker::setup()': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'FastDraw'.
    """
    raise NotImplementedError(
        "'QCosmeticStroker.setup' has no cute function yet. Qt's 'void "
        "QCosmeticStroker::setup()': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'FastDraw'.")
