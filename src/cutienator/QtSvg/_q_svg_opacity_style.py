"""
QSvgOpacityStyle binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QSvgOpacityStyle to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QSvgStyleProperty


class QSvgOpacityStyle(QSvgStyleProperty):
  """
  The cute side of Qt's QSvgOpacityStyle: a plain Python object standing in
  front of one C++ QSvgOpacityStyle.

  It is built on the cute 'QSvgStyleProperty', as Qt's QSvgOpacityStyle is
  built on Qt's QSvgStyleProperty, and has everything that class has.

  C++ hands a QSvgOpacityStyle around as a copy, so every C++
  QSvgOpacityStyle behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSvgOpacityStyle that has a ritual and that Python
  can call so far, 3 names in all: 'type', 'opacity', 'isDefault'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgOpacityStyle::~QSvgOpacityStyle()': the destructor: Python
    removes its C++ QSvgOpacityStyle by it, and has no other use for it.
  - Qt's 'void QSvgOpacityStyle::apply(QPainter *p, const QSvgNode *node,
    QSvgExtraStates &states)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QSvgOpacityStyle::revert(QPainter *p, QSvgExtraStates
    &states)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QSvgOpacityStyle is created at the first use, not by
    'QSvgOpacityStyle(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSvgOpacityStyle back gives a copy the ritual made
    for Python, in a new cute QSvgOpacityStyle.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgOpacityStyle'

  #  A C++ QSvgOpacityStyle Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgOpacityStyle'

  #  Qt's '~QSvgOpacityStyle()'. Naming it makes this a value class: Python
  #  owns every C++ QSvgOpacityStyle behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QSvgOpacityStyleD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> QSvgStyleProperty.Type:
    """
    Calls Qt's 'Type QSvgOpacityStyle::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgopacitystyle.html#type

    Returns
    -------

    QSvgStyleProperty.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSvgStyleProperty.Type(number)' gives.
    """
    #  Type QSvgOpacityStyle::type() const
    ritual = 'ritual_ZNK16QSvgOpacityStyle4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QSvgOpacityStyle4typeEv'
    return QSvgStyleProperty.Type(self.uglySide.call(ritual))

  def opacity(self) -> float:
    """
    Calls Qt's 'qreal QSvgOpacityStyle::opacity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgopacitystyle.html#opacity
    """
    #  qreal QSvgOpacityStyle::opacity() const
    return self.uglySide.call('ritual_ZNK16QSvgOpacityStyle7opacityEv')

  def isDefault(self) -> bool:
    """
    Calls Qt's 'bool QSvgOpacityStyle::isDefault() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgopacitystyle.html#isDefault
    """
    #  bool QSvgOpacityStyle::isDefault() const
    ritual = 'ritual_ZNK16QSvgOpacityStyle9isDefaultEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QSvgOpacityStyle9isDefaultEv'
    return self.uglySide.call(ritual)

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

  @overload(float)
  def __init__(self, opacity: float) -> None:
    """
    Notes what was given, for Qt's 'QSvgOpacityStyle::QSvgOpacityStyle(qreal
    opacity)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgopacitystyle.html#QSvgOpacityStyle

    Parameters
    ----------

    opacity : float
      Passed on as it is.
    """
    #  QSvgOpacityStyle::QSvgOpacityStyle(qreal opacity)
    self._noteCreation(QSvgOpacityStyle, lambda: Rituals.call(
        'ritual_ZN16QSvgOpacityStyleC1Ed', opacity,
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
