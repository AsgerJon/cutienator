"""
QQuickRectangleShapePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickShapesDesignHelpers/6.12.0/QtQuickShapesDesignHelpers/private/qquickrectangleshape_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickRectangleShapePrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtQml import QQml

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQuickRectangleShape
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickRectangleShape = WAIT['QQuickRectangleShape']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickRectangleShapePrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickRectangleShapePrivate: a plain Python object
  standing in front of one C++ QQuickRectangleShapePrivate.

  What exists
  -----------

  Every function of Qt's QQuickRectangleShapePrivate that has a ritual and
  that Python can call so far, 12 names in all: 'q_func', 'get',
  'setTopLeftRadius', 'setTopRightRadius', 'setBottomLeftRadius',
  'setBottomRightRadius', 'setTopLeftBevel', 'setTopRightBevel',
  'setBottomLeftBevel', 'setBottomRightBevel', 'maybeUpdateElements',
  'calculateIndependentRadii'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickRectangleShape *QQuickRectangleShapePrivate::q_func()
    const': takes in Python what 'QQuickRectangleShape
    *QQuickRectangleShapePrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QQuickRectangleShapePrivate is created at the first use, not by
    'QQuickRectangleShapePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickRectangleShapePrivate.
  """

  #  The enums Qt writes inside QQuickRectangleShapePrivate, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Edge(CuteNum, scoped=True):
    """
    The enum 'QQuickRectangleShapePrivate::Edge' of Qt, with the 5 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Top = Kee[int](0)
    Right = Kee[int](1)
    Bottom = Kee[int](2)
    Left = Kee[int](3)
    NEdges = Kee[int](4)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickRectangleShape)
  @overload(NoneType)
  def get(
      p: Optional[QQuickRectangleShape],
  ) -> Optional[QQuickRectangleShapePrivate]:
    """
    Calls Qt's 'QQuickRectangleShapePrivate
    *QQuickRectangleShapePrivate::get(QQuickRectangleShape *p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshapeprivate.html#get

    Parameters
    ----------

    p : Optional[QQuickRectangleShape]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickRectangleShapePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickRectangleShapePrivate
    #      *QQuickRectangleShapePrivate::get(QQuickRectangleShape *p)
    address = Rituals.call(
        'ritual_ZN27QQuickRectangleShapePrivate3getEP20QQuickRectangleShape',
        CuteMixin._addressOf(p),
    )
    return QQuickRectangleShapePrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickRectangleShapePrivate'

  #  A C++ QQuickRectangleShapePrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickRectangleShapePrivate'

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

  @overload(int, QQml.PropertyUtils.State)
  def setTopLeftRadius(
      self,
      topLeftRadius: int,
      propertyState: QQml.PropertyUtils.State,
  ) -> None:
    """
    Calls Qt's 'void QQuickRectangleShapePrivate::setTopLeftRadius(int
    topLeftRadius, QQml::PropertyUtils::State propertyState)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshapeprivate.html#setTopLeftRadius

    Parameters
    ----------

    topLeftRadius : int
      Passed on as it is.

    propertyState : QQml.PropertyUtils.State
      Passed on as its number.
    """
    #  void QQuickRectangleShapePrivate::setTopLeftRadius(int topLeftRadius,
    #      QQml::PropertyUtils::State propertyState)
    self.uglySide.call(
        'ritual_ZN27QQuickRectangleShapePrivate16setTopLeftRadiusEiN4QQml13'
        'PropertyUtils5StateE',
        topLeftRadius, propertyState.value,
    )

  @overload(int, QQml.PropertyUtils.State)
  def setTopRightRadius(
      self,
      topRightRadius: int,
      propertyState: QQml.PropertyUtils.State,
  ) -> None:
    """
    Calls Qt's 'void QQuickRectangleShapePrivate::setTopRightRadius(int
    topRightRadius, QQml::PropertyUtils::State propertyState)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshapeprivate.html#setTopRightRadius

    Parameters
    ----------

    topRightRadius : int
      Passed on as it is.

    propertyState : QQml.PropertyUtils.State
      Passed on as its number.
    """
    #  void QQuickRectangleShapePrivate::setTopRightRadius(int
    #      topRightRadius, QQml::PropertyUtils::State propertyState)
    self.uglySide.call(
        'ritual_ZN27QQuickRectangleShapePrivate17setTopRightRadiusEiN4QQml1'
        '3PropertyUtils5StateE',
        topRightRadius, propertyState.value,
    )

  @overload(int, QQml.PropertyUtils.State)
  def setBottomLeftRadius(
      self,
      bottomLeftRadius: int,
      propertyState: QQml.PropertyUtils.State,
  ) -> None:
    """
    Calls Qt's 'void QQuickRectangleShapePrivate::setBottomLeftRadius(int
    bottomLeftRadius, QQml::PropertyUtils::State propertyState)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshapeprivate.html

    Parameters
    ----------

    bottomLeftRadius : int
      Passed on as it is.

    propertyState : QQml.PropertyUtils.State
      Passed on as its number.
    """
    #  void QQuickRectangleShapePrivate::setBottomLeftRadius(int
    #      bottomLeftRadius, QQml::PropertyUtils::State propertyState)
    self.uglySide.call(
        'ritual_ZN27QQuickRectangleShapePrivate19setBottomLeftRadiusEiN4QQm'
        'l13PropertyUtils5StateE',
        bottomLeftRadius, propertyState.value,
    )

  @overload(int, QQml.PropertyUtils.State)
  def setBottomRightRadius(
      self,
      bottomRightRadius: int,
      propertyState: QQml.PropertyUtils.State,
  ) -> None:
    """
    Calls Qt's 'void QQuickRectangleShapePrivate::setBottomRightRadius(int
    bottomRightRadius, QQml::PropertyUtils::State propertyState)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshapeprivate.html

    Parameters
    ----------

    bottomRightRadius : int
      Passed on as it is.

    propertyState : QQml.PropertyUtils.State
      Passed on as its number.
    """
    #  void QQuickRectangleShapePrivate::setBottomRightRadius(int
    #      bottomRightRadius, QQml::PropertyUtils::State propertyState)
    self.uglySide.call(
        'ritual_ZN27QQuickRectangleShapePrivate20setBottomRightRadiusEiN4QQ'
        'ml13PropertyUtils5StateE',
        bottomRightRadius, propertyState.value,
    )

  @overload(bool, QQml.PropertyUtils.State)
  def setTopLeftBevel(
      self,
      topLeftBevel: bool,
      propertyState: QQml.PropertyUtils.State,
  ) -> None:
    """
    Calls Qt's 'void QQuickRectangleShapePrivate::setTopLeftBevel(bool
    topLeftBevel, QQml::PropertyUtils::State propertyState)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshapeprivate.html#setTopLeftBevel

    Parameters
    ----------

    topLeftBevel : bool
      Passed on as it is.

    propertyState : QQml.PropertyUtils.State
      Passed on as its number.
    """
    #  void QQuickRectangleShapePrivate::setTopLeftBevel(bool topLeftBevel,
    #      QQml::PropertyUtils::State propertyState)
    self.uglySide.call(
        'ritual_ZN27QQuickRectangleShapePrivate15setTopLeftBevelEbN4QQml13P'
        'ropertyUtils5StateE',
        topLeftBevel, propertyState.value,
    )

  @overload(bool, QQml.PropertyUtils.State)
  def setTopRightBevel(
      self,
      topRightBevel: bool,
      propertyState: QQml.PropertyUtils.State,
  ) -> None:
    """
    Calls Qt's 'void QQuickRectangleShapePrivate::setTopRightBevel(bool
    topRightBevel, QQml::PropertyUtils::State propertyState)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshapeprivate.html#setTopRightBevel

    Parameters
    ----------

    topRightBevel : bool
      Passed on as it is.

    propertyState : QQml.PropertyUtils.State
      Passed on as its number.
    """
    #  void QQuickRectangleShapePrivate::setTopRightBevel(bool topRightBevel,
    #      QQml::PropertyUtils::State propertyState)
    self.uglySide.call(
        'ritual_ZN27QQuickRectangleShapePrivate16setTopRightBevelEbN4QQml13'
        'PropertyUtils5StateE',
        topRightBevel, propertyState.value,
    )

  @overload(bool, QQml.PropertyUtils.State)
  def setBottomLeftBevel(
      self,
      bottomLeftBevel: bool,
      propertyState: QQml.PropertyUtils.State,
  ) -> None:
    """
    Calls Qt's 'void QQuickRectangleShapePrivate::setBottomLeftBevel(bool
    bottomLeftBevel, QQml::PropertyUtils::State propertyState)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshapeprivate.html

    Parameters
    ----------

    bottomLeftBevel : bool
      Passed on as it is.

    propertyState : QQml.PropertyUtils.State
      Passed on as its number.
    """
    #  void QQuickRectangleShapePrivate::setBottomLeftBevel(bool
    #      bottomLeftBevel, QQml::PropertyUtils::State propertyState)
    self.uglySide.call(
        'ritual_ZN27QQuickRectangleShapePrivate18setBottomLeftBevelEbN4QQml'
        '13PropertyUtils5StateE',
        bottomLeftBevel, propertyState.value,
    )

  @overload(bool, QQml.PropertyUtils.State)
  def setBottomRightBevel(
      self,
      bottomRightBevel: bool,
      propertyState: QQml.PropertyUtils.State,
  ) -> None:
    """
    Calls Qt's 'void QQuickRectangleShapePrivate::setBottomRightBevel(bool
    bottomRightBevel, QQml::PropertyUtils::State propertyState)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshapeprivate.html

    Parameters
    ----------

    bottomRightBevel : bool
      Passed on as it is.

    propertyState : QQml.PropertyUtils.State
      Passed on as its number.
    """
    #  void QQuickRectangleShapePrivate::setBottomRightBevel(bool
    #      bottomRightBevel, QQml::PropertyUtils::State propertyState)
    self.uglySide.call(
        'ritual_ZN27QQuickRectangleShapePrivate19setBottomRightBevelEbN4QQm'
        'l13PropertyUtils5StateE',
        bottomRightBevel, propertyState.value,
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
    'QQuickRectangleShapePrivate::QQuickRectangleShapePrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshapeprivate.html
    """
    #  QQuickRectangleShapePrivate::QQuickRectangleShapePrivate()
    self._noteCreation(QQuickRectangleShapePrivate, lambda: Rituals.call(
        'ritual_ZN27QQuickRectangleShapePrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickRectangleShape]:
    """
    Calls Qt's 'QQuickRectangleShape *QQuickRectangleShapePrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshapeprivate.html#q_func

    Returns
    -------

    Optional[QQuickRectangleShape]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickRectangleShape *QQuickRectangleShapePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN27QQuickRectangleShapePrivate6q_funcEv',
    )
    from . import QQuickRectangleShape
    return QQuickRectangleShape._cuteAt(address)

  def maybeUpdateElements(self) -> None:
    """
    Calls Qt's 'void QQuickRectangleShapePrivate::maybeUpdateElements()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshapeprivate.html
    """
    #  void QQuickRectangleShapePrivate::maybeUpdateElements()
    self.uglySide.call(
        'ritual_ZN27QQuickRectangleShapePrivate19maybeUpdateElementsEv',
    )

  def calculateIndependentRadii(self) -> None:
    """
    Calls Qt's 'void
    QQuickRectangleShapePrivate::calculateIndependentRadii()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangleshapeprivate.html
    """
    #  void QQuickRectangleShapePrivate::calculateIndependentRadii()
    self.uglySide.call(
        'ritual_ZN27QQuickRectangleShapePrivate25calculateIndependentRadiiE'
        'v',
    )
