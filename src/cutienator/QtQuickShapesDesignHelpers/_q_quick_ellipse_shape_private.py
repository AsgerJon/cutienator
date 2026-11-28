"""
QQuickEllipseShapePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickShapesDesignHelpers/6.12.0/QtQuickShapesDesignHelpers/private/qquickellipseshape_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickEllipseShapePrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtQuick import QQuickPathArc

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQuickEllipseShape
  from ..QtGui import QVector2D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVector2D = WAIT['QVector2D']


class QQuickEllipseShapePrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickEllipseShapePrivate: a plain Python object
  standing in front of one C++ QQuickEllipseShapePrivate.

  What exists
  -----------

  Every function of Qt's QQuickEllipseShapePrivate that has a ritual and that
  Python can call so far, 19 names in all: 'q_func', 'addLine', 'addArc',
  'getBorderOffset', 'roundCenter', 'roundBeginEnd', 'roundOuter',
  'roundInner', 'drawCenterCorner', 'drawInnerEndCorner',
  'drawInnerBeginCorner', 'drawOuterBeginCorner', 'drawOuterArcRounded',
  'drawInnerArcRounded', 'drawOuterArc', 'drawFullInnerArc',
  'drawWithInnerRadius', 'drawWithoutInnerRadius', 'updatePath'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickEllipseShape *QQuickEllipseShapePrivate::q_func()
    const': takes in Python what 'QQuickEllipseShape
    *QQuickEllipseShapePrivate::q_func()' takes.
  - Qt's 'QQuickEllipseShapePrivate::~QQuickEllipseShapePrivate()': the
    destructor: Python never removes a C++ QQuickEllipseShapePrivate.

  What to expect
  --------------

  - The C++ QQuickEllipseShapePrivate is created at the first use, not by
    'QQuickEllipseShapePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickEllipseShapePrivate.
  """

  #  The enums Qt writes inside QQuickEllipseShapePrivate, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class RoundedCornerIndex(CuteNum, scoped=True):
    """
    The enum 'QQuickEllipseShapePrivate::RoundedCornerIndex' of Qt, with the
    5 names Qt gives in it. C++ keeps these names inside the enum, so the
    class that holds the enum does not have them.
    """

    Center = Kee[int](0)
    InnerEnd = Kee[int](1)
    OuterEnd = Kee[int](2)
    InnerBegin = Kee[int](3)
    OuterBegin = Kee[int](4)

  #  The classes Qt writes inside QQuickEllipseShapePrivate, each a class in
  #  here as in C++.

  class RoundedCorner(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuickEllipseShapePrivate::RoundedCorner: a plain
    Python object standing in front of one C++
    QQuickEllipseShapePrivate::RoundedCorner.

    C++ hands a QQuickEllipseShapePrivate::RoundedCorner around as a copy, so
    every C++ QQuickEllipseShapePrivate::RoundedCorner behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's QQuickEllipseShapePrivate::RoundedCorner that has
    a ritual and that Python can call so far, 2 names in all: 'update',
    'reset'. None can be made from Python: one comes out of a function of
    another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuickEllipseShapePrivate::RoundedCorner::~RoundedCorner()': the
      destructor: Python removes its C++
      QQuickEllipseShapePrivate::RoundedCorner by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QQuickEllipseShapePrivate::RoundedCorner is created at the
      first use, not by 'QQuickEllipseShapePrivate::RoundedCorner(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuickEllipseShapePrivate::RoundedCorner back gives
      a copy the ritual made for Python, in a new cute
      QQuickEllipseShapePrivate::RoundedCorner.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QVector2D = WAIT['QVector2D']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuickEllipseShapePrivate::RoundedCorner'

    #  Qt's '~QQuickEllipseShapePrivate::RoundedCorner()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QQuickEllipseShapePrivate::RoundedCorner behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN25QQuickEllipseShapePrivate13RoundedCornerD1Ev')

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

    @overload(float, QVector2D, QVector2D, QVector2D, float, float)
    def update(
        self,
        diff: float,
        a: QVector2D,
        b: QVector2D,
        c: QVector2D,
        alpha: float,
        radius: float,
    ) -> None:
      """
      Calls Qt's 'void QQuickEllipseShapePrivate::RoundedCorner::update(qreal
      diff, QVector2D a, QVector2D b, QVector2D c, qreal alpha, qreal
      radius)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquickellipseshapeprivate-roundedcorner.html

      Parameters
      ----------

      diff : float
        Passed on as it is.

      a : QVector2D
        Passed on as a value: Qt reads the C++ QVector2D, which stays
        Python's own.

      b : QVector2D
        Passed on as a value: Qt reads the C++ QVector2D, which stays
        Python's own.

      c : QVector2D
        Passed on as a value: Qt reads the C++ QVector2D, which stays
        Python's own.

      alpha : float
        Passed on as it is.

      radius : float
        Passed on as it is.
      """
      #  void QQuickEllipseShapePrivate::RoundedCorner::update(qreal diff,
      #      QVector2D a, QVector2D b, QVector2D c, qreal alpha, qreal
      #      radius)
      self.uglySide.call(
          'ritual_ZN25QQuickEllipseShapePrivate13RoundedCorner6updateEd9QVe'
          'ctor2DS1_S1_dd',
          diff, self._valueOf(a), self._valueOf(b), self._valueOf(c), alpha,
          radius,
      )

    def reset(self) -> None:
      """
      Calls Qt's 'void QQuickEllipseShapePrivate::RoundedCorner::reset()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquickellipseshapeprivate-roundedcorner.html
      """
      #  void QQuickEllipseShapePrivate::RoundedCorner::reset()
      self.uglySide.call(
          'ritual_ZN25QQuickEllipseShapePrivate13RoundedCorner5resetEv',
      )

  class RoundedCornerArray(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuickEllipseShapePrivate::RoundedCornerArray: a
    plain Python object standing in front of one C++
    QQuickEllipseShapePrivate::RoundedCornerArray.

    C++ hands a QQuickEllipseShapePrivate::RoundedCornerArray around as a
    copy, so every C++ QQuickEllipseShapePrivate::RoundedCornerArray behind a
    cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QQuickEllipseShapePrivate::RoundedCornerArray that
    has a ritual and that Python can call so far, 1 name in all: 'reset'.
    None can be made from Python: one comes out of a function of another
    class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'RoundedCorner
      &QQuickEllipseShapePrivate::RoundedCornerArray::operator[](
      RoundedCornerIndex index)': names the enum
      'QQuickEllipseShapePrivate::RoundedCornerIndex', whose class cannot be
      named here.
    - Qt's
      'QQuickEllipseShapePrivate::RoundedCornerArray::~RoundedCornerArray()':
      the destructor: Python removes its C++
      QQuickEllipseShapePrivate::RoundedCornerArray by it, and has no other
      use for it.

    What to expect
    --------------

    - The C++ QQuickEllipseShapePrivate::RoundedCornerArray is created at the
      first use, not by 'QQuickEllipseShapePrivate::RoundedCornerArray(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuickEllipseShapePrivate::RoundedCornerArray back
      gives a copy the ritual made for Python, in a new cute
      QQuickEllipseShapePrivate::RoundedCornerArray.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuickEllipseShapePrivate::RoundedCornerArray'

    #  Qt's '~QQuickEllipseShapePrivate::RoundedCornerArray()'. Naming it
    #  makes this a value class: Python owns every C++
    #  QQuickEllipseShapePrivate::RoundedCornerArray behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN25QQuickEllipseShapePrivate18RoundedCornerArrayD1Ev')

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

    def reset(self) -> None:
      """
      Calls Qt's 'void
      QQuickEllipseShapePrivate::RoundedCornerArray::reset()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquickellipseshapeprivate-roundedcornerarray.html
      """
      #  void QQuickEllipseShapePrivate::RoundedCornerArray::reset()
      self.uglySide.call(
          'ritual_ZN25QQuickEllipseShapePrivate18RoundedCornerArray5resetEv',
      )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickEllipseShapePrivate'

  #  A C++ QQuickEllipseShapePrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickEllipseShapePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getBorderOffset(self) -> float:
    """
    Calls Qt's 'qreal QQuickEllipseShapePrivate::getBorderOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshapeprivate.html#getBorderOffset
    """
    #  qreal QQuickEllipseShapePrivate::getBorderOffset() const
    return self.uglySide.call(
        'ritual_ZNK25QQuickEllipseShapePrivate15getBorderOffsetEv',
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
    Notes what was given, for Qt's
    'QQuickEllipseShapePrivate::QQuickEllipseShapePrivate()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshapeprivate.html
    """
    #  QQuickEllipseShapePrivate::QQuickEllipseShapePrivate()
    self._noteCreation(QQuickEllipseShapePrivate, lambda: Rituals.call(
        'ritual_ZN25QQuickEllipseShapePrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickEllipseShape]:
    """
    Calls Qt's 'QQuickEllipseShape *QQuickEllipseShapePrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshapeprivate.html#q_func

    Returns
    -------

    Optional[QQuickEllipseShape]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickEllipseShape *QQuickEllipseShapePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN25QQuickEllipseShapePrivate6q_funcEv',
    )
    from . import QQuickEllipseShape
    return QQuickEllipseShape._cuteAt(address)

  @overload(QVector2D)
  def addLine(self, point: QVector2D) -> None:
    """
    Calls Qt's 'void QQuickEllipseShapePrivate::addLine(QVector2D point)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshapeprivate.html#addLine

    Parameters
    ----------

    point : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  void QQuickEllipseShapePrivate::addLine(QVector2D point)
    self.uglySide.call(
        'ritual_ZN25QQuickEllipseShapePrivate7addLineE9QVector2D',
        self._valueOf(point),
    )

  @overload(QVector2D, QVector2D, QQuickPathArc.ArcDirection)
  @overload(QVector2D, QVector2D, QQuickPathArc.ArcDirection, bool)
  def addArc(
      self,
      point: QVector2D,
      arcRadius: QVector2D,
      dir: QQuickPathArc.ArcDirection,
      largeArc: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QQuickEllipseShapePrivate::addArc(QVector2D point,
    QVector2D arcRadius, QQuickPathArc::ArcDirection dir, bool largeArc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshapeprivate.html#addArc

    Parameters
    ----------

    point : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    arcRadius : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    dir : QQuickPathArc.ArcDirection
      Passed on as its number.

    largeArc : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickEllipseShapePrivate::addArc(QVector2D point, QVector2D
    #      arcRadius, QQuickPathArc::ArcDirection dir, bool largeArc)
    self.uglySide.call(
        'ritual_ZN25QQuickEllipseShapePrivate6addArcE9QVector2DS0_N13QQuick'
        'PathArc12ArcDirectionEb',
        self._valueOf(point), self._valueOf(arcRadius), dir.value, largeArc,
    )

  @overload(QVector2D, QVector2D)
  def roundCenter(self, center: QVector2D, ellipseRadius: QVector2D) -> None:
    """
    Calls Qt's 'void QQuickEllipseShapePrivate::roundCenter(QVector2D center,
    QVector2D ellipseRadius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshapeprivate.html#roundCenter

    Parameters
    ----------

    center : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    ellipseRadius : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  void QQuickEllipseShapePrivate::roundCenter(QVector2D center,
    #      QVector2D ellipseRadius)
    self.uglySide.call(
        'ritual_ZN25QQuickEllipseShapePrivate11roundCenterE9QVector2DS0_',
        self._valueOf(center), self._valueOf(ellipseRadius),
    )

  @overload(QVector2D, QVector2D)
  def roundBeginEnd(
      self,
      center: QVector2D,
      ellipseRadius: QVector2D,
  ) -> None:
    """
    Calls Qt's 'void QQuickEllipseShapePrivate::roundBeginEnd(QVector2D
    center, QVector2D ellipseRadius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshapeprivate.html#roundBeginEnd

    Parameters
    ----------

    center : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    ellipseRadius : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  void QQuickEllipseShapePrivate::roundBeginEnd(QVector2D center,
    #      QVector2D ellipseRadius)
    self.uglySide.call(
        'ritual_ZN25QQuickEllipseShapePrivate13roundBeginEndE9QVector2DS0_',
        self._valueOf(center), self._valueOf(ellipseRadius),
    )

  @overload(QVector2D, QVector2D, float, float, float, RoundedCornerIndex)
  def roundOuter(
      self,
      center: QVector2D,
      ellipseRadius: QVector2D,
      deg: float,
      arcAngle1: float,
      arcAngle2: float,
      index: RoundedCornerIndex,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickEllipseShapePrivate::roundOuter(QVector2D center,
    QVector2D ellipseRadius, qreal deg, qreal arcAngle1, qreal arcAngle2,
    RoundedCornerIndex index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshapeprivate.html#roundOuter

    Parameters
    ----------

    center : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    ellipseRadius : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    deg : float
      Passed on as it is.

    arcAngle1 : float
      Passed on as it is.

    arcAngle2 : float
      Passed on as it is.

    index : RoundedCornerIndex
      Passed on as its number.
    """
    #  bool QQuickEllipseShapePrivate::roundOuter(QVector2D center, QVector2D
    #      ellipseRadius, qreal deg, qreal arcAngle1, qreal arcAngle2,
    #      RoundedCornerIndex index)
    return self.uglySide.call(
        'ritual_ZN25QQuickEllipseShapePrivate10roundOuterE9QVector2DS0_dddN'
        'S_18RoundedCornerIndexE',
        self._valueOf(center), self._valueOf(ellipseRadius), deg, arcAngle1,
        arcAngle2, index.value,
    )

  @overload(QVector2D, QVector2D, float, float, float, RoundedCornerIndex)
  def roundInner(
      self,
      center: QVector2D,
      ellipseRadius: QVector2D,
      deg: float,
      arcAngle1: float,
      arcAngle2: float,
      index: RoundedCornerIndex,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickEllipseShapePrivate::roundInner(QVector2D center,
    QVector2D ellipseRadius, qreal deg, qreal arcAngle1, qreal arcAngle2,
    RoundedCornerIndex index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshapeprivate.html#roundInner

    Parameters
    ----------

    center : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    ellipseRadius : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    deg : float
      Passed on as it is.

    arcAngle1 : float
      Passed on as it is.

    arcAngle2 : float
      Passed on as it is.

    index : RoundedCornerIndex
      Passed on as its number.
    """
    #  bool QQuickEllipseShapePrivate::roundInner(QVector2D center, QVector2D
    #      ellipseRadius, qreal deg, qreal arcAngle1, qreal arcAngle2,
    #      RoundedCornerIndex index)
    return self.uglySide.call(
        'ritual_ZN25QQuickEllipseShapePrivate10roundInnerE9QVector2DS0_dddN'
        'S_18RoundedCornerIndexE',
        self._valueOf(center), self._valueOf(ellipseRadius), deg, arcAngle1,
        arcAngle2, index.value,
    )

  def drawCenterCorner(self) -> None:
    """
    Calls Qt's 'void QQuickEllipseShapePrivate::drawCenterCorner()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshapeprivate.html#drawCenterCorner
    """
    #  void QQuickEllipseShapePrivate::drawCenterCorner()
    self.uglySide.call(
        'ritual_ZN25QQuickEllipseShapePrivate16drawCenterCornerEv',
    )

  def drawInnerEndCorner(self) -> None:
    """
    Calls Qt's 'void QQuickEllipseShapePrivate::drawInnerEndCorner()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshapeprivate.html#drawInnerEndCorner
    """
    #  void QQuickEllipseShapePrivate::drawInnerEndCorner()
    self.uglySide.call(
        'ritual_ZN25QQuickEllipseShapePrivate18drawInnerEndCornerEv',
    )

  def drawInnerBeginCorner(self) -> None:
    """
    Calls Qt's 'void QQuickEllipseShapePrivate::drawInnerBeginCorner()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshapeprivate.html
    """
    #  void QQuickEllipseShapePrivate::drawInnerBeginCorner()
    self.uglySide.call(
        'ritual_ZN25QQuickEllipseShapePrivate20drawInnerBeginCornerEv',
    )

  def drawOuterBeginCorner(self) -> None:
    """
    Calls Qt's 'void QQuickEllipseShapePrivate::drawOuterBeginCorner()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshapeprivate.html
    """
    #  void QQuickEllipseShapePrivate::drawOuterBeginCorner()
    self.uglySide.call(
        'ritual_ZN25QQuickEllipseShapePrivate20drawOuterBeginCornerEv',
    )

  @overload(QVector2D, QVector2D)
  def drawOuterArcRounded(
      self,
      center: QVector2D,
      ellipseRadius: QVector2D,
  ) -> None:
    """
    Calls Qt's 'void QQuickEllipseShapePrivate::drawOuterArcRounded(QVector2D
    center, QVector2D ellipseRadius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshapeprivate.html#drawOuterArcRounded

    Parameters
    ----------

    center : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    ellipseRadius : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  void QQuickEllipseShapePrivate::drawOuterArcRounded(QVector2D center,
    #      QVector2D ellipseRadius)
    self.uglySide.call(
        'ritual_ZN25QQuickEllipseShapePrivate19drawOuterArcRoundedE9QVector'
        '2DS0_',
        self._valueOf(center), self._valueOf(ellipseRadius),
    )

  @overload(QVector2D, QVector2D)
  def drawInnerArcRounded(
      self,
      center: QVector2D,
      ellipseRadius: QVector2D,
  ) -> None:
    """
    Calls Qt's 'void QQuickEllipseShapePrivate::drawInnerArcRounded(QVector2D
    center, QVector2D ellipseRadius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshapeprivate.html#drawInnerArcRounded

    Parameters
    ----------

    center : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    ellipseRadius : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  void QQuickEllipseShapePrivate::drawInnerArcRounded(QVector2D center,
    #      QVector2D ellipseRadius)
    self.uglySide.call(
        'ritual_ZN25QQuickEllipseShapePrivate19drawInnerArcRoundedE9QVector'
        '2DS0_',
        self._valueOf(center), self._valueOf(ellipseRadius),
    )

  @overload(QVector2D, QVector2D)
  def drawOuterArc(
      self,
      center: QVector2D,
      ellipseRadius: QVector2D,
  ) -> None:
    """
    Calls Qt's 'void QQuickEllipseShapePrivate::drawOuterArc(QVector2D
    center, QVector2D ellipseRadius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshapeprivate.html#drawOuterArc

    Parameters
    ----------

    center : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    ellipseRadius : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  void QQuickEllipseShapePrivate::drawOuterArc(QVector2D center,
    #      QVector2D ellipseRadius)
    self.uglySide.call(
        'ritual_ZN25QQuickEllipseShapePrivate12drawOuterArcE9QVector2DS0_',
        self._valueOf(center), self._valueOf(ellipseRadius),
    )

  @overload(QVector2D, QVector2D)
  def drawFullInnerArc(
      self,
      center: QVector2D,
      ellipseRadius: QVector2D,
  ) -> None:
    """
    Calls Qt's 'void QQuickEllipseShapePrivate::drawFullInnerArc(QVector2D
    center, QVector2D ellipseRadius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshapeprivate.html#drawFullInnerArc

    Parameters
    ----------

    center : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    ellipseRadius : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  void QQuickEllipseShapePrivate::drawFullInnerArc(QVector2D center,
    #      QVector2D ellipseRadius)
    self.uglySide.call(
        'ritual_ZN25QQuickEllipseShapePrivate16drawFullInnerArcE9QVector2DS'
        '0_',
        self._valueOf(center), self._valueOf(ellipseRadius),
    )

  @overload(QVector2D, QVector2D)
  def drawWithInnerRadius(
      self,
      center: QVector2D,
      ellipseRadius: QVector2D,
  ) -> None:
    """
    Calls Qt's 'void QQuickEllipseShapePrivate::drawWithInnerRadius(QVector2D
    center, QVector2D ellipseRadius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshapeprivate.html#drawWithInnerRadius

    Parameters
    ----------

    center : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    ellipseRadius : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  void QQuickEllipseShapePrivate::drawWithInnerRadius(QVector2D center,
    #      QVector2D ellipseRadius)
    self.uglySide.call(
        'ritual_ZN25QQuickEllipseShapePrivate19drawWithInnerRadiusE9QVector'
        '2DS0_',
        self._valueOf(center), self._valueOf(ellipseRadius),
    )

  @overload(QVector2D, QVector2D)
  def drawWithoutInnerRadius(
      self,
      center: QVector2D,
      ellipseRadius: QVector2D,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickEllipseShapePrivate::drawWithoutInnerRadius(QVector2D center,
    QVector2D ellipseRadius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshapeprivate.html

    Parameters
    ----------

    center : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    ellipseRadius : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  void QQuickEllipseShapePrivate::drawWithoutInnerRadius(QVector2D
    #      center, QVector2D ellipseRadius)
    self.uglySide.call(
        'ritual_ZN25QQuickEllipseShapePrivate22drawWithoutInnerRadiusE9QVec'
        'tor2DS0_',
        self._valueOf(center), self._valueOf(ellipseRadius),
    )

  def updatePath(self) -> None:
    """
    Calls Qt's 'void QQuickEllipseShapePrivate::updatePath()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshapeprivate.html#updatePath
    """
    #  void QQuickEllipseShapePrivate::updatePath()
    self.uglySide.call('ritual_ZN25QQuickEllipseShapePrivate10updatePathEv')
