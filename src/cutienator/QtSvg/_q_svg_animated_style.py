"""
QSvgAnimatedStyle binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QSvgAnimatedStyle to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QSvgAnimatedStyle(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSvgAnimatedStyle: a plain Python object standing in
  front of one C++ QSvgAnimatedStyle.

  C++ hands a QSvgAnimatedStyle around as a copy, so every C++
  QSvgAnimatedStyle behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QSvgAnimatedStyle yet. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgAnimatedStyle::~QSvgAnimatedStyle()': the destructor: Python
    removes its C++ QSvgAnimatedStyle by it, and has no other use for it.
  - Qt's 'void QSvgAnimatedStyle::apply(QPainter *p, const QSvgNode *node,
    QSvgExtraStates &states)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QSvgAnimatedStyle::revert(QPainter *p, QSvgExtraStates
    &states)': takes a type Python has no way to hand over yet.
  - Qt's 'void QSvgAnimatedStyle::savePaintingState(const QPainter *p, const
    QSvgNode *node, QSvgExtraStates &states)': takes a type Python has no way
    to hand over yet.
  - Qt's 'void QSvgAnimatedStyle::fetchStyleState(const QSvgAbstractAnimation
    *animation, QSvgStyleState &currentStyle)': takes a type Python has no
    way to hand over yet.
  - Qt's 'void QSvgAnimatedStyle::applyStyle(QPainter *p, QSvgExtraStates
    &states, const QSvgStyleState &currentStyle)': takes a type Python has no
    way to hand over yet.

  What to expect
  --------------

  - The C++ QSvgAnimatedStyle is created at the first use, not by
    'QSvgAnimatedStyle(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSvgAnimatedStyle back gives a copy the ritual made
    for Python, in a new cute QSvgAnimatedStyle.
  - Each name of Qt's QSvgAnimatedStyle that has no cute function yet,
    'apply', 'applyStyle', 'fetchStyleState', 'revert', 'savePaintingState',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgAnimatedStyle'

  #  Qt's '~QSvgAnimatedStyle()'. Naming it makes this a value class: Python
  #  owns every C++ QSvgAnimatedStyle behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QSvgAnimatedStyleD1Ev'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QSvgAnimatedStyle::QSvgAnimatedStyle()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvganimatedstyle.html#QSvgAnimatedStyle
    """
    #  QSvgAnimatedStyle::QSvgAnimatedStyle()
    self._noteCreation(QSvgAnimatedStyle, lambda: Rituals.call(
        'ritual_ZN17QSvgAnimatedStyleC1Ev',
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

  @staticmethod
  def apply(*__, **_) -> Never:
    """
    Qt's 'void QSvgAnimatedStyle::apply(QPainter *p, const QSvgNode *node,
    QSvgExtraStates &states)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QSvgAnimatedStyle.apply' has no cute function yet. Qt's 'void "
        "QSvgAnimatedStyle::apply(QPainter *p, const QSvgNode *node, "
        "QSvgExtraStates &states)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def applyStyle(*__, **_) -> Never:
    """
    Qt's 'void QSvgAnimatedStyle::applyStyle(QPainter *p, QSvgExtraStates
    &states, const QSvgStyleState &currentStyle)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QSvgAnimatedStyle.applyStyle' has no cute function yet. Qt's "
        "'void QSvgAnimatedStyle::applyStyle(QPainter *p, QSvgExtraStates "
        "&states, const QSvgStyleState &currentStyle)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def fetchStyleState(*__, **_) -> Never:
    """
    Qt's 'void QSvgAnimatedStyle::fetchStyleState(const QSvgAbstractAnimation
    *animation, QSvgStyleState &currentStyle)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QSvgAnimatedStyle.fetchStyleState' has no cute function yet. Qt's "
        "'void QSvgAnimatedStyle::fetchStyleState(const "
        "QSvgAbstractAnimation *animation, QSvgStyleState &currentStyle)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def revert(*__, **_) -> Never:
    """
    Qt's 'void QSvgAnimatedStyle::revert(QPainter *p, QSvgExtraStates
    &states)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSvgAnimatedStyle.revert' has no cute function yet. Qt's 'void "
        "QSvgAnimatedStyle::revert(QPainter *p, QSvgExtraStates &states)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def savePaintingState(*__, **_) -> Never:
    """
    Qt's 'void QSvgAnimatedStyle::savePaintingState(const QPainter *p, const
    QSvgNode *node, QSvgExtraStates &states)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QSvgAnimatedStyle.savePaintingState' has no cute function yet. "
        "Qt's 'void QSvgAnimatedStyle::savePaintingState(const QPainter *p, "
        "const QSvgNode *node, QSvgExtraStates &states)': takes a type "
        "Python has no way to hand over yet.")
