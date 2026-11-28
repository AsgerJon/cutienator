"""
QSvgQualityStyle binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QSvgQualityStyle to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum
from ..occult import Rituals
from . import QSvgStyleProperty


class QSvgQualityStyle(QSvgStyleProperty):
  """
  The cute side of Qt's QSvgQualityStyle: a plain Python object standing in
  front of one C++ QSvgQualityStyle.

  It is built on the cute 'QSvgStyleProperty', as Qt's QSvgQualityStyle is
  built on Qt's QSvgStyleProperty, and has everything that class has.

  C++ hands a QSvgQualityStyle around as a copy, so every C++
  QSvgQualityStyle behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSvgQualityStyle that has a ritual and that Python
  can call so far, 2 names in all: 'type', 'setImageRendering'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgQualityStyle::~QSvgQualityStyle()': the destructor: Python
    removes its C++ QSvgQualityStyle by it, and has no other use for it.
  - Qt's 'void QSvgQualityStyle::apply(QPainter *p, const QSvgNode *node,
    QSvgExtraStates &states)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QSvgQualityStyle::revert(QPainter *p, QSvgExtraStates
    &states)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QSvgQualityStyle is created at the first use, not by
    'QSvgQualityStyle(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSvgQualityStyle back gives a copy the ritual made
    for Python, in a new cute QSvgQualityStyle.
  """

  #  The enums Qt writes inside QSvgQualityStyle, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ImageRendering(CuteNum):
    """
    The enum 'QSvgQualityStyle::ImageRendering' of Qt, with the 3 names Qt
    gives in it.
    """

    ImageRenderingAuto = Kee[int](0)
    ImageRenderingOptimizeSpeed = Kee[int](1)
    ImageRenderingOptimizeQuality = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgQualityStyle'

  #  A C++ QSvgQualityStyle Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgQualityStyle'

  #  Qt's '~QSvgQualityStyle()'. Naming it makes this a value class: Python
  #  owns every C++ QSvgQualityStyle behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QSvgQualityStyleD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> QSvgStyleProperty.Type:
    """
    Calls Qt's 'Type QSvgQualityStyle::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgqualitystyle.html#type

    Returns
    -------

    QSvgStyleProperty.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSvgStyleProperty.Type(number)' gives.
    """
    #  Type QSvgQualityStyle::type() const
    ritual = 'ritual_ZNK16QSvgQualityStyle4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QSvgQualityStyle4typeEv'
    return QSvgStyleProperty.Type(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(ImageRendering)
  def setImageRendering(self, a0: ImageRendering) -> None:
    """
    Calls Qt's 'void QSvgQualityStyle::setImageRendering(ImageRendering a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgqualitystyle.html#setImageRendering

    Parameters
    ----------

    a0 : ImageRendering
      Passed on as its number.
    """
    #  void QSvgQualityStyle::setImageRendering(ImageRendering a0)
    self.uglySide.call(
        'ritual_ZN16QSvgQualityStyle17setImageRenderingENS_14ImageRendering'
        'E',
        a0.value,
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

  @overload(int)
  def __init__(self, color: int) -> None:
    """
    Notes what was given, for Qt's 'QSvgQualityStyle::QSvgQualityStyle(int
    color)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgqualitystyle.html#QSvgQualityStyle

    Parameters
    ----------

    color : int
      Passed on as it is.
    """
    #  QSvgQualityStyle::QSvgQualityStyle(int color)
    self._noteCreation(QSvgQualityStyle, lambda: Rituals.call(
        'ritual_ZN16QSvgQualityStyleC1Ei', color,
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
