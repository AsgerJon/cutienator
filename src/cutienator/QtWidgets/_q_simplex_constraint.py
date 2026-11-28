"""
QSimplexConstraint binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qsimplex_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSimplexConstraint to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals
from ..QtCore import QList


class QSimplexConstraint(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSimplexConstraint: a plain Python object standing in
  front of one C++ QSimplexConstraint.

  What exists
  -----------

  Every function of Qt's QSimplexConstraint that has a ritual and that Python
  can call so far, 3 names in all: 'invert', 'isSatisfied', 'toString'. It
  can be made from Python, in 1 way; see '__init__'.

  What has no ritual
  ------------------

  4 of the 8 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QSimplexConstraint is created at the first use, not by
    'QSimplexConstraint(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSimplexConstraint.
  """

  #  The enums Qt writes inside QSimplexConstraint, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Ratio(CuteNum):
    """
    The enum 'QSimplexConstraint::Ratio' of Qt, with the 3 names Qt gives in
    it.
    """

    LessOrEqual = Kee[int](0)
    Equal = Kee[int](1)
    MoreOrEqual = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSimplexConstraint'

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
    Notes what was given, for Qt's
    'QSimplexConstraint::QSimplexConstraint()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsimplexconstraint.html#QSimplexConstraint
    """
    #  QSimplexConstraint::QSimplexConstraint()
    self._noteCreation(QSimplexConstraint, lambda: Rituals.call(
        'ritual_ZN18QSimplexConstraintC1Ev',
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

  def invert(self) -> None:
    """
    Calls Qt's 'void QSimplexConstraint::invert()'.

    Qt's own words: https://doc.qt.io/qt-6/qsimplexconstraint.html#invert
    """
    #  void QSimplexConstraint::invert()
    self.uglySide.call('ritual_ZN18QSimplexConstraint6invertEv')

  def isSatisfied(self) -> bool:
    """
    Calls Qt's 'bool QSimplexConstraint::isSatisfied()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsimplexconstraint.html#isSatisfied
    """
    #  bool QSimplexConstraint::isSatisfied()
    return self.uglySide.call('ritual_ZN18QSimplexConstraint11isSatisfiedEv')

  def toString(self) -> str:
    """
    Calls Qt's 'QString QSimplexConstraint::toString()'.

    Qt's own words: https://doc.qt.io/qt-6/qsimplexconstraint.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSimplexConstraint::toString()
    return self.uglySide.call('ritual_ZN18QSimplexConstraint8toStringEv')


#  Qt's 'QList<QSimplexConstraint *>': the list of QSimplexConstraint, which
#  'QList[QSimplexConstraint]' gives. It is made here, so that there is one
#  as soon as there can be a QSimplexConstraint.
QList.createKind(
    QSimplexConstraint, 'address',
    make='ritual_list_make_QSimplexConstraint_ptr',
    add='ritual_list_add_QSimplexConstraint_ptr',
    size='ritual_list_size_QSimplexConstraint_ptr',
    at='ritual_list_at_QSimplexConstraint_ptr',
    drop='ritual_list_drop_QSimplexConstraint_ptr',
)
