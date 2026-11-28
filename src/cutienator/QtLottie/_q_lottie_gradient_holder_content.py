"""
QLottieGradientHolderContent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLottie/6.12.0/QtLottie/private/qlottiegradientholder_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QLottieGradientHolderContent to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..QtGui import QGradient

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPointF


class QLottieGradientHolderContent(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QLottieGradientHolderContent: a plain Python object
  standing in front of one C++ QLottieGradientHolderContent.

  C++ hands a QLottieGradientHolderContent around as a copy, so every C++
  QLottieGradientHolderContent behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QLottieGradientHolderContent that has a ritual and
  that Python can call so far, 8 names in all: 'value', 'gradientType',
  'startPoint', 'endPoint', 'highlightLength', 'highlightAngle',
  'setGradient', 'updateGradientProperties'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QLottieGradientHolderContent::~QLottieGradientHolderContent()': the
    destructor: Python removes its C++ QLottieGradientHolderContent by it,
    and has no other use for it.

  What to expect
  --------------

  - The C++ QLottieGradientHolderContent is created at the first use, not by
    'QLottieGradientHolderContent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLottieGradientHolderContent back gives a copy the
    ritual made for Python, in a new cute QLottieGradientHolderContent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLottieGradientHolderContent'

  #  Qt's '~QLottieGradientHolderContent()'. Naming it makes this a value
  #  class: Python owns every C++ QLottieGradientHolderContent behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN28QLottieGradientHolderContentD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def value(self) -> Optional[QGradient]:
    """
    Calls Qt's 'QGradient *QLottieGradientHolderContent::value() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiegradientholdercontent.html#value

    Returns
    -------

    Optional[QGradient]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGradient *QLottieGradientHolderContent::value() const
    address = self.uglySide.call(
        'ritual_ZNK28QLottieGradientHolderContent5valueEv',
    )
    return QGradient._cuteAt(address)

  def gradientType(self) -> QGradient.Type:
    """
    Calls Qt's 'QGradient::Type QLottieGradientHolderContent::gradientType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiegradientholdercontent.html#gradientType

    Returns
    -------

    QGradient.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QGradient.Type(number)'
      gives.
    """
    #  QGradient::Type QLottieGradientHolderContent::gradientType() const
    return QGradient.Type(self.uglySide.call(
        'ritual_ZNK28QLottieGradientHolderContent12gradientTypeEv',
    ))

  def startPoint(self) -> QPointF:
    """
    Calls Qt's 'QPointF QLottieGradientHolderContent::startPoint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiegradientholdercontent.html#startPoint

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QLottieGradientHolderContent::startPoint() const
    address = self.uglySide.call(
        'ritual_ZNK28QLottieGradientHolderContent10startPointEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def endPoint(self) -> QPointF:
    """
    Calls Qt's 'QPointF QLottieGradientHolderContent::endPoint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiegradientholdercontent.html#endPoint

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QLottieGradientHolderContent::endPoint() const
    address = self.uglySide.call(
        'ritual_ZNK28QLottieGradientHolderContent8endPointEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def highlightLength(self) -> float:
    """
    Calls Qt's 'qreal QLottieGradientHolderContent::highlightLength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiegradientholdercontent.html#highlightLength
    """
    #  qreal QLottieGradientHolderContent::highlightLength() const
    return self.uglySide.call(
        'ritual_ZNK28QLottieGradientHolderContent15highlightLengthEv',
    )

  def highlightAngle(self) -> float:
    """
    Calls Qt's 'qreal QLottieGradientHolderContent::highlightAngle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiegradientholdercontent.html#highlightAngle
    """
    #  qreal QLottieGradientHolderContent::highlightAngle() const
    return self.uglySide.call(
        'ritual_ZNK28QLottieGradientHolderContent14highlightAngleEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setGradient(self, opacity: float) -> None:
    """
    Calls Qt's 'void QLottieGradientHolderContent::setGradient(qreal
    opacity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiegradientholdercontent.html#setGradient

    Parameters
    ----------

    opacity : float
      Passed on as it is.
    """
    #  void QLottieGradientHolderContent::setGradient(qreal opacity)
    self.uglySide.call(
        'ritual_ZN28QLottieGradientHolderContent11setGradientEd', opacity,
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

  @overload(int)
  def updateGradientProperties(self, frame: int) -> None:
    """
    Calls Qt's 'void
    QLottieGradientHolderContent::updateGradientProperties(int frame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiegradientholdercontent.html

    Parameters
    ----------

    frame : int
      Passed on as it is.
    """
    #  void QLottieGradientHolderContent::updateGradientProperties(int frame)
    self.uglySide.call(
        'ritual_ZN28QLottieGradientHolderContent24updateGradientPropertiesE'
        'i',
        frame,
    )
