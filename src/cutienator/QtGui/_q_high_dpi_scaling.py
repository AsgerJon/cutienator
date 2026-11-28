"""
QHighDpiScaling binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qhighdpiscaling_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QHighDpiScaling to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPoint
  from . import QPlatformScreen, QScreen, QWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPlatformScreen = WAIT['QPlatformScreen']
  QPoint = WAIT['QPoint']
  QScreen = WAIT['QScreen']
  QWindow = WAIT['QWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHighDpiScaling(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QHighDpiScaling: a plain Python object standing in
  front of one C++ QHighDpiScaling.

  What exists
  -----------

  Every function of Qt's QHighDpiScaling that has a ritual and that Python
  can call so far, 12 names in all: 'initHighDpiScaling',
  'updateHighDpiScaling', 'setGlobalFactor', 'setScreenFactor', 'isActive',
  'scaleAndOrigin', 'mapPositionFromNative', 'mapPositionToNative',
  'roundScaleFactor', 'rawScaleFactor', 'screenSubfactor',
  'screenForPosition'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDpi QHighDpiScaling::logicalDpi(const QScreen *screen)': gives a
    type Python has no way to take yet.
  - Qt's 'QDpi QHighDpiScaling::effectiveLogicalDpi(const QPlatformScreen
    *screen, qreal rawFactor, qreal roundedFactor)': gives a type Python has
    no way to take yet.
  - Qt's 'QList<QHighDpiScaling::ScreenFactor>
    QHighDpiScaling::parseScreenScaleFactorsSpec(QStringView
    screenScaleFactors)': gives a type Python has no way to take yet.
  - Qt's 'QDebug operator<<(QDebug a0, const ScreenFactor &a1)': an operator
    between other classes, written inside this one.

  What has no ritual
  ------------------

  10 of the 28 functions Qt declares: 6 forbidden; 3 not a gap; 1 a template.

  What to expect
  --------------

  - The C++ QHighDpiScaling is created at the first use, not by
    'QHighDpiScaling(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHighDpiScaling.
  - Each name of Qt's QHighDpiScaling that has no cute function yet,
    'effectiveLogicalDpi', 'factor', 'logicalDpi',
    'parseScreenScaleFactorsSpec', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QHighDpiScaling, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class DpiAdjustmentPolicy(CuteNum, scoped=True):
    """
    The enum 'QHighDpiScaling::DpiAdjustmentPolicy' of Qt, with the 4 names
    Qt gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Unset = Kee[int](0)
    Enabled = Kee[int](1)
    Disabled = Kee[int](2)
    UpOnly = Kee[int](3)

  #  The classes Qt writes inside QHighDpiScaling, each a class in here as in
  #  C++.

  class Point(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QHighDpiScaling::Point: a plain Python object
    standing in front of one C++ QHighDpiScaling::Point.

    C++ hands a QHighDpiScaling::Point around as a copy, so every C++
    QHighDpiScaling::Point behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QHighDpiScaling::Point yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QHighDpiScaling::Point::~Point()': the destructor: Python removes
      its C++ QHighDpiScaling::Point by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QHighDpiScaling::Point is created at the first use, not by
      'QHighDpiScaling::Point(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QHighDpiScaling::Point back gives a copy the ritual
      made for Python, in a new cute QHighDpiScaling::Point.
    """

    #  The enums Qt writes inside QHighDpiScaling::Point, each a class in
    #  here as in C++, and the names Qt has for the combinations of its flags
    #  enums.

    class Kind(CuteNum):
      """
      The enum 'QHighDpiScaling::Point::Kind' of Qt, with the 3 names Qt
      gives in it.
      """

      Invalid = Kee[int](0)
      DeviceIndependent = Kee[int](1)
      Native = Kee[int](2)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QHighDpiScaling::Point'

    #  Qt's '~QHighDpiScaling::Point()'. Naming it makes this a value class:
    #  Python owns every C++ QHighDpiScaling::Point behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN15QHighDpiScaling5PointD1Ev'

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

  class ScaleAndOrigin(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QHighDpiScaling::ScaleAndOrigin: a plain Python
    object standing in front of one C++ QHighDpiScaling::ScaleAndOrigin.

    C++ hands a QHighDpiScaling::ScaleAndOrigin around as a copy, so every
    C++ QHighDpiScaling::ScaleAndOrigin behind a cute one is Python's own: it
    is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QHighDpiScaling::ScaleAndOrigin yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QHighDpiScaling::ScaleAndOrigin::~ScaleAndOrigin()': the
      destructor: Python removes its C++ QHighDpiScaling::ScaleAndOrigin by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QHighDpiScaling::ScaleAndOrigin is created at the first use,
      not by 'QHighDpiScaling::ScaleAndOrigin(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QHighDpiScaling::ScaleAndOrigin back gives a copy
      the ritual made for Python, in a new cute
      QHighDpiScaling::ScaleAndOrigin.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QHighDpiScaling::ScaleAndOrigin'

    #  Qt's '~QHighDpiScaling::ScaleAndOrigin()'. Naming it makes this a
    #  value class: Python owns every C++ QHighDpiScaling::ScaleAndOrigin
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN15QHighDpiScaling14ScaleAndOriginD1Ev'

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
  def initHighDpiScaling() -> None:
    """
    Calls Qt's 'void QHighDpiScaling::initHighDpiScaling()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhighdpiscaling.html#initHighDpiScaling
    """
    #  void QHighDpiScaling::initHighDpiScaling()
    Rituals.call('ritual_ZN15QHighDpiScaling18initHighDpiScalingEv')

  @staticmethod
  def updateHighDpiScaling() -> None:
    """
    Calls Qt's 'void QHighDpiScaling::updateHighDpiScaling()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhighdpiscaling.html#updateHighDpiScaling
    """
    #  void QHighDpiScaling::updateHighDpiScaling()
    Rituals.call('ritual_ZN15QHighDpiScaling20updateHighDpiScalingEv')

  @staticmethod
  @overload(float)
  def setGlobalFactor(factor: float) -> None:
    """
    Calls Qt's 'void QHighDpiScaling::setGlobalFactor(qreal factor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhighdpiscaling.html#setGlobalFactor

    Parameters
    ----------

    factor : float
      Passed on as it is.
    """
    #  void QHighDpiScaling::setGlobalFactor(qreal factor)
    Rituals.call('ritual_ZN15QHighDpiScaling15setGlobalFactorEd', factor)

  @staticmethod
  @overload(QScreen, float)
  @overload(NoneType, float)
  def setScreenFactor(screen: Optional[QScreen], factor: float) -> None:
    """
    Calls Qt's 'void QHighDpiScaling::setScreenFactor(QScreen *screen, qreal
    factor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhighdpiscaling.html#setScreenFactor

    Parameters
    ----------

    screen : Optional[QScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    factor : float
      Passed on as it is.
    """
    #  void QHighDpiScaling::setScreenFactor(QScreen *screen, qreal factor)
    Rituals.call(
        'ritual_ZN15QHighDpiScaling15setScreenFactorEP7QScreend',
        CuteMixin._addressOf(screen), factor,
    )

  @staticmethod
  def isActive() -> bool:
    """
    Calls Qt's 'bool QHighDpiScaling::isActive()'.

    Qt's own words: https://doc.qt.io/qt-6/qhighdpiscaling.html#isActive
    """
    #  bool QHighDpiScaling::isActive()
    return Rituals.call('ritual_ZN15QHighDpiScaling8isActiveEv')

  @staticmethod
  @overload(QPlatformScreen, Point)
  @overload(NoneType, Point)
  def scaleAndOrigin(
      platformScreen: Optional[QPlatformScreen],
      position: Point,
  ) -> ScaleAndOrigin:
    """
    Calls Qt's 'ScaleAndOrigin QHighDpiScaling::scaleAndOrigin(const
    QPlatformScreen *platformScreen, Point position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhighdpiscaling.html#scaleAndOrigin

    Parameters
    ----------

    platformScreen : Optional[QPlatformScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    position : Point
      Passed on as a value: Qt reads the C++ QHighDpiScaling::Point, which
      stays Python's own.

    Returns
    -------

    ScaleAndOrigin
      A new cute QHighDpiScaling::ScaleAndOrigin around the copy Qt gave
      back. Python owns it.
    """
    #  ScaleAndOrigin QHighDpiScaling::scaleAndOrigin(const QPlatformScreen
    #      *platformScreen, Point position)
    address = Rituals.call(
        'ritual_ZN15QHighDpiScaling14scaleAndOriginEPK15QPlatformScreenNS_5'
        'PointE',
        CuteMixin._addressOf(platformScreen), CuteMixin._valueOf(position),
    )
    return QHighDpiScaling.ScaleAndOrigin._cuteOwning(address)

  @staticmethod
  @overload(QScreen, Point)
  def scaleAndOrigin(
      screen: Optional[QScreen],
      position: Point,
  ) -> ScaleAndOrigin:
    """
    Calls Qt's 'ScaleAndOrigin QHighDpiScaling::scaleAndOrigin(const QScreen
    *screen, Point position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhighdpiscaling.html#scaleAndOrigin

    Parameters
    ----------

    screen : Optional[QScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    position : Point
      Passed on as a value: Qt reads the C++ QHighDpiScaling::Point, which
      stays Python's own.

    Returns
    -------

    ScaleAndOrigin
      A new cute QHighDpiScaling::ScaleAndOrigin around the copy Qt gave
      back. Python owns it.
    """
    #  ScaleAndOrigin QHighDpiScaling::scaleAndOrigin(const QScreen *screen,
    #      Point position)
    address = Rituals.call(
        'ritual_ZN15QHighDpiScaling14scaleAndOriginEPK7QScreenNS_5PointE',
        CuteMixin._addressOf(screen), CuteMixin._valueOf(position),
    )
    return QHighDpiScaling.ScaleAndOrigin._cuteOwning(address)

  @staticmethod
  @overload(QWindow, Point)
  def scaleAndOrigin(
      platformScreen: Optional[QWindow],
      position: Point,
  ) -> ScaleAndOrigin:
    """
    Calls Qt's 'ScaleAndOrigin QHighDpiScaling::scaleAndOrigin(const QWindow
    *platformScreen, Point position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhighdpiscaling.html#scaleAndOrigin

    Parameters
    ----------

    platformScreen : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    position : Point
      Passed on as a value: Qt reads the C++ QHighDpiScaling::Point, which
      stays Python's own.

    Returns
    -------

    ScaleAndOrigin
      A new cute QHighDpiScaling::ScaleAndOrigin around the copy Qt gave
      back. Python owns it.
    """
    #  ScaleAndOrigin QHighDpiScaling::scaleAndOrigin(const QWindow
    #      *platformScreen, Point position)
    address = Rituals.call(
        'ritual_ZN15QHighDpiScaling14scaleAndOriginEPK7QWindowNS_5PointE',
        CuteMixin._addressOf(platformScreen), CuteMixin._valueOf(position),
    )
    return QHighDpiScaling.ScaleAndOrigin._cuteOwning(address)

  @staticmethod
  @overload(QPoint, QPlatformScreen)
  @overload(QPoint, NoneType)
  def mapPositionFromNative(
      pos: QPoint,
      platformScreen: Optional[QPlatformScreen],
  ) -> QPoint:
    """
    Calls Qt's 'QPoint QHighDpiScaling::mapPositionFromNative(const QPoint
    &pos, const QPlatformScreen *platformScreen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhighdpiscaling.html#mapPositionFromNative

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    platformScreen : Optional[QPlatformScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QHighDpiScaling::mapPositionFromNative(const QPoint &pos, const
    #      QPlatformScreen *platformScreen)
    address = Rituals.call(
        'ritual_ZN15QHighDpiScaling21mapPositionFromNativeERK6QPointPK15QPl'
        'atformScreen',
        CuteMixin._valueOf(pos), CuteMixin._addressOf(platformScreen),
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  @staticmethod
  @overload(QPoint, QPlatformScreen)
  @overload(QPoint, NoneType)
  def mapPositionToNative(
      pos: QPoint,
      platformScreen: Optional[QPlatformScreen],
  ) -> QPoint:
    """
    Calls Qt's 'QPoint QHighDpiScaling::mapPositionToNative(const QPoint
    &pos, const QPlatformScreen *platformScreen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhighdpiscaling.html#mapPositionToNative

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    platformScreen : Optional[QPlatformScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QHighDpiScaling::mapPositionToNative(const QPoint &pos, const
    #      QPlatformScreen *platformScreen)
    address = Rituals.call(
        'ritual_ZN15QHighDpiScaling19mapPositionToNativeERK6QPointPK15QPlat'
        'formScreen',
        CuteMixin._valueOf(pos), CuteMixin._addressOf(platformScreen),
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  @staticmethod
  @overload(float)
  def roundScaleFactor(rawFactor: float) -> float:
    """
    Calls Qt's 'qreal QHighDpiScaling::roundScaleFactor(qreal rawFactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhighdpiscaling.html#roundScaleFactor

    Parameters
    ----------

    rawFactor : float
      Passed on as it is.
    """
    #  qreal QHighDpiScaling::roundScaleFactor(qreal rawFactor)
    return Rituals.call(
        'ritual_ZN15QHighDpiScaling16roundScaleFactorEd', rawFactor,
    )

  @staticmethod
  @overload(QPlatformScreen)
  @overload(NoneType)
  def rawScaleFactor(screen: Optional[QPlatformScreen]) -> float:
    """
    Calls Qt's 'qreal QHighDpiScaling::rawScaleFactor(const QPlatformScreen
    *screen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhighdpiscaling.html#rawScaleFactor

    Parameters
    ----------

    screen : Optional[QPlatformScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qreal QHighDpiScaling::rawScaleFactor(const QPlatformScreen *screen)
    return Rituals.call(
        'ritual_ZN15QHighDpiScaling14rawScaleFactorEPK15QPlatformScreen',
        CuteMixin._addressOf(screen),
    )

  @staticmethod
  @overload(QPlatformScreen)
  @overload(NoneType)
  def screenSubfactor(screen: Optional[QPlatformScreen]) -> float:
    """
    Calls Qt's 'qreal QHighDpiScaling::screenSubfactor(const QPlatformScreen
    *screen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhighdpiscaling.html#screenSubfactor

    Parameters
    ----------

    screen : Optional[QPlatformScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qreal QHighDpiScaling::screenSubfactor(const QPlatformScreen *screen)
    return Rituals.call(
        'ritual_ZN15QHighDpiScaling15screenSubfactorEPK15QPlatformScreen',
        CuteMixin._addressOf(screen),
    )

  @staticmethod
  @overload(Point, QScreen)
  @overload(Point, NoneType)
  def screenForPosition(
      position: Point,
      guess: Optional[QScreen],
  ) -> Optional[QScreen]:
    """
    Calls Qt's 'QScreen *QHighDpiScaling::screenForPosition(Point position,
    QScreen *guess)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhighdpiscaling.html#screenForPosition

    Parameters
    ----------

    position : Point
      Passed on as a value: Qt reads the C++ QHighDpiScaling::Point, which
      stays Python's own.

    guess : Optional[QScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QScreen]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScreen *QHighDpiScaling::screenForPosition(Point position, QScreen
    #      *guess)
    address = Rituals.call(
        'ritual_ZN15QHighDpiScaling17screenForPositionENS_5PointEP7QScreen',
        CuteMixin._valueOf(position), CuteMixin._addressOf(guess),
    )
    from . import QScreen
    return QScreen._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHighDpiScaling'

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

  @staticmethod
  def effectiveLogicalDpi(*__, **_) -> Never:
    """
    Qt's 'QDpi QHighDpiScaling::effectiveLogicalDpi(const QPlatformScreen
    *screen, qreal rawFactor, qreal roundedFactor)': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QHighDpiScaling.effectiveLogicalDpi' has no cute function yet. "
        "Qt's 'QDpi QHighDpiScaling::effectiveLogicalDpi(const "
        "QPlatformScreen *screen, qreal rawFactor, qreal roundedFactor)': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def factor(*__, **_) -> Never:
    """
    Qt's 'QHighDpiScaling::factor': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QHighDpiScaling.factor' has no cute function yet. Qt's "
        "'QHighDpiScaling::factor': a template: a pattern and no single "
        "function.")

  @staticmethod
  def logicalDpi(*__, **_) -> Never:
    """
    Qt's 'QDpi QHighDpiScaling::logicalDpi(const QScreen *screen)': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QHighDpiScaling.logicalDpi' has no cute function yet. Qt's 'QDpi "
        "QHighDpiScaling::logicalDpi(const QScreen *screen)': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def parseScreenScaleFactorsSpec(*__, **_) -> Never:
    """
    Qt's 'QList<QHighDpiScaling::ScreenFactor>
    QHighDpiScaling::parseScreenScaleFactorsSpec(QStringView
    screenScaleFactors)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QHighDpiScaling.parseScreenScaleFactorsSpec' has no cute function "
        "yet. Qt's 'QList<QHighDpiScaling::ScreenFactor> "
        "QHighDpiScaling::parseScreenScaleFactorsSpec(QStringView "
        "screenScaleFactors)': gives a type Python has no way to take yet.")
