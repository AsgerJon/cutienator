"""
QCss::Selector binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qcssparser_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QCss::Selector to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class Selector(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCss::Selector: a plain Python object standing in
  front of one C++ QCss::Selector.

  C++ hands a QCss::Selector around as a copy, so every C++ QCss::Selector
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCss::Selector that has a ritual and that Python can
  call so far, 2 names in all: 'specificity', 'pseudoElement'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'quint64 QCss::Selector::pseudoClass(quint64 *negated) const': takes
    a number to change where it is.
  - Qt's 'QCss::Selector::~Selector()': the destructor: Python removes its
    C++ QCss::Selector by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QCss::Selector is created at the first use, not by
    'QCss::Selector(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCss::Selector back gives a copy the ritual made for
    Python, in a new cute QCss::Selector.
  - Each name of Qt's QCss::Selector that has no cute function yet,
    'pseudoClass', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCss::Selector'

  #  Qt's '~QCss::Selector()'. Naming it makes this a value class: Python
  #  owns every C++ QCss::Selector behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN4QCss8SelectorD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def specificity(self) -> int:
    """
    Calls Qt's 'int QCss::Selector::specificity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-selector.html#specificity
    """
    #  int QCss::Selector::specificity() const
    return self.uglySide.call('ritual_ZNK4QCss8Selector11specificityEv')

  def pseudoElement(self) -> str:
    """
    Calls Qt's 'QString QCss::Selector::pseudoElement() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-selector.html#pseudoElement

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCss::Selector::pseudoElement() const
    return self.uglySide.call('ritual_ZNK4QCss8Selector13pseudoElementEv')

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
  def pseudoClass(*__, **_) -> Never:
    """
    Qt's 'quint64 QCss::Selector::pseudoClass(quint64 *negated) const': takes
    a number to change where it is.
    """
    raise NotImplementedError(
        "'QCss.Selector.pseudoClass' has no cute function yet. Qt's "
        "'quint64 QCss::Selector::pseudoClass(quint64 *negated) const': "
        "takes a number to change where it is.")
