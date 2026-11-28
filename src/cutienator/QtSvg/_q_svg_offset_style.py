"""
QSvgOffsetStyle binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QSvgOffsetStyle to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QtSvg, QSvgStyleProperty

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtGui import QPainterPath
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainterPath = WAIT['QPainterPath']


class QSvgOffsetStyle(QSvgStyleProperty):
  """
  The cute side of Qt's QSvgOffsetStyle: a plain Python object standing in
  front of one C++ QSvgOffsetStyle.

  It is built on the cute 'QSvgStyleProperty', as Qt's QSvgOffsetStyle is
  built on Qt's QSvgStyleProperty, and has everything that class has.

  C++ hands a QSvgOffsetStyle around as a copy, so every C++ QSvgOffsetStyle
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSvgOffsetStyle that has a ritual and that Python
  can call so far, 9 names in all: 'type', 'setPath', 'path',
  'setRotateAngle', 'rotateAngle', 'setRotateType', 'rotateType',
  'setDistance', 'distance'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgOffsetStyle::~QSvgOffsetStyle()': the destructor: Python
    removes its C++ QSvgOffsetStyle by it, and has no other use for it.
  - Qt's 'void QSvgOffsetStyle::apply(QPainter *p, const QSvgNode *node,
    QSvgExtraStates &states)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QSvgOffsetStyle::revert(QPainter *p, QSvgExtraStates
    &states)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QSvgOffsetStyle is created at the first use, not by
    'QSvgOffsetStyle(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSvgOffsetStyle back gives a copy the ritual made for
    Python, in a new cute QSvgOffsetStyle.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgOffsetStyle'

  #  A C++ QSvgOffsetStyle Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgOffsetStyle'

  #  Qt's '~QSvgOffsetStyle()'. Naming it makes this a value class: Python
  #  owns every C++ QSvgOffsetStyle behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QSvgOffsetStyleD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> QSvgStyleProperty.Type:
    """
    Calls Qt's 'Type QSvgOffsetStyle::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgoffsetstyle.html#type

    Returns
    -------

    QSvgStyleProperty.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSvgStyleProperty.Type(number)' gives.
    """
    #  Type QSvgOffsetStyle::type() const
    ritual = 'ritual_ZNK15QSvgOffsetStyle4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QSvgOffsetStyle4typeEv'
    return QSvgStyleProperty.Type(self.uglySide.call(ritual))

  def path(self) -> QPainterPath:
    """
    Calls Qt's 'const QPainterPath &QSvgOffsetStyle::path() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgoffsetstyle.html#path

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  const QPainterPath &QSvgOffsetStyle::path() const
    address = self.uglySide.call('ritual_ZNK15QSvgOffsetStyle4pathEv')
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  def rotateAngle(self) -> float:
    """
    Calls Qt's 'qreal QSvgOffsetStyle::rotateAngle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgoffsetstyle.html#rotateAngle
    """
    #  qreal QSvgOffsetStyle::rotateAngle() const
    return self.uglySide.call('ritual_ZNK15QSvgOffsetStyle11rotateAngleEv')

  def rotateType(self) -> QtSvg.OffsetRotateType:
    """
    Calls Qt's 'QtSvg::OffsetRotateType QSvgOffsetStyle::rotateType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgoffsetstyle.html#rotateType

    Returns
    -------

    QtSvg.OffsetRotateType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QtSvg.OffsetRotateType(number)' gives.
    """
    #  QtSvg::OffsetRotateType QSvgOffsetStyle::rotateType() const
    return QtSvg.OffsetRotateType(self.uglySide.call(
        'ritual_ZNK15QSvgOffsetStyle10rotateTypeEv',
    ))

  def distance(self) -> float:
    """
    Calls Qt's 'qreal QSvgOffsetStyle::distance() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgoffsetstyle.html#distance
    """
    #  qreal QSvgOffsetStyle::distance() const
    return self.uglySide.call('ritual_ZNK15QSvgOffsetStyle8distanceEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPainterPath)
  def setPath(self, path: QPainterPath) -> None:
    """
    Calls Qt's 'void QSvgOffsetStyle::setPath(const QPainterPath &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgoffsetstyle.html#setPath

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.
    """
    #  void QSvgOffsetStyle::setPath(const QPainterPath &path)
    self.uglySide.call(
        'ritual_ZN15QSvgOffsetStyle7setPathERK12QPainterPath',
        self._valueOf(path),
    )

  @overload(float)
  def setRotateAngle(self, angle: float) -> None:
    """
    Calls Qt's 'void QSvgOffsetStyle::setRotateAngle(qreal angle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgoffsetstyle.html#setRotateAngle

    Parameters
    ----------

    angle : float
      Passed on as it is.
    """
    #  void QSvgOffsetStyle::setRotateAngle(qreal angle)
    self.uglySide.call('ritual_ZN15QSvgOffsetStyle14setRotateAngleEd', angle)

  @overload(QtSvg.OffsetRotateType)
  def setRotateType(self, type: QtSvg.OffsetRotateType) -> None:
    """
    Calls Qt's 'void QSvgOffsetStyle::setRotateType(QtSvg::OffsetRotateType
    type)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgoffsetstyle.html#setRotateType

    Parameters
    ----------

    type : QtSvg.OffsetRotateType
      Passed on as its number.
    """
    #  void QSvgOffsetStyle::setRotateType(QtSvg::OffsetRotateType type)
    self.uglySide.call(
        'ritual_ZN15QSvgOffsetStyle13setRotateTypeEN5QtSvg16OffsetRotateTyp'
        'eE',
        type.value,
    )

  @overload(float)
  def setDistance(self, distance: float) -> None:
    """
    Calls Qt's 'void QSvgOffsetStyle::setDistance(qreal distance)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgoffsetstyle.html#setDistance

    Parameters
    ----------

    distance : float
      Passed on as it is.
    """
    #  void QSvgOffsetStyle::setDistance(qreal distance)
    self.uglySide.call('ritual_ZN15QSvgOffsetStyle11setDistanceEd', distance)

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
    Notes what was given, for Qt's 'QSvgOffsetStyle::QSvgOffsetStyle()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgoffsetstyle.html#QSvgOffsetStyle
    """
    #  QSvgOffsetStyle::QSvgOffsetStyle()
    self._noteCreation(QSvgOffsetStyle, lambda: Rituals.call(
        'ritual_ZN15QSvgOffsetStyleC1Ev',
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
