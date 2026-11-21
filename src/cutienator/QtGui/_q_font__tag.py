"""
QFont::Tag binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtGui/qfont.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QByteArray


class Tag(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QFont::Tag: a plain Python object standing in front
  of one C++ QFont::Tag.

  C++ hands a QFont::Tag around as a copy, so every C++ QFont::Tag behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QFont::Tag that has a ritual and that Python can
  call so far, 3 names in all: 'isValid', 'value', 'toString'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFont::Tag::~Tag()': the destructor: Python removes its C++
    QFont::Tag by it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 8 functions Qt declares: 2 takes or gives a type that cannot be
  passed yet; 1 a template.

  What to expect
  --------------

  - The C++ QFont::Tag is created at the first use, not by 'QFont::Tag(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QFont::Tag back gives a copy the ritual made for
    Python, in a new cute QFont::Tag.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFont::Tag'

  #  Qt's '~QFont::Tag()'. Naming it makes this a value class: Python owns
  #  every C++ QFont::Tag behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN5QFont3TagD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QFont::Tag::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfont-tag.html#isValid
    """
    #  bool QFont::Tag::isValid() const
    return self.uglySide.call('ritual_ZNK5QFont3Tag7isValidEv')

  def value(self) -> int:
    """
    Calls Qt's 'quint32 QFont::Tag::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfont-tag.html#value
    """
    #  quint32 QFont::Tag::value() const
    return self.uglySide.call('ritual_ZNK5QFont3Tag5valueEv')

  def toString(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QFont::Tag::toString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfont-tag.html#toString

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QFont::Tag::toString() const
    address = self.uglySide.call('ritual_ZNK5QFont3Tag8toStringEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

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
    Notes what was given, for Qt's 'QFont::Tag::Tag()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfont-tag.html#Tag
    """
    #  QFont::Tag::Tag()
    self._noteCreation(Tag, lambda: Rituals.call('ritual_ZN5QFont3TagC1Ev'))

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
