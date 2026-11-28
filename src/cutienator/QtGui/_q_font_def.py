"""
QFontDef binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qfont_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QFontDef to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QFontDef(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QFontDef: a plain Python object standing in front of
  one C++ QFontDef.

  C++ hands a QFontDef around as a copy, so every C++ QFontDef behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QFontDef that has a ritual and that Python can call
  so far, 4 names in all: 'family', 'exactMatch', '__eq__', '__lt__'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFontDef::~QFontDef()': the destructor: Python removes its C++
    QFontDef by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QFontDef is created at the first use, not by 'QFontDef(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QFontDef back gives a copy the ritual made for
    Python, in a new cute QFontDef.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFontDef'

  #  Qt's '~QFontDef()'. Naming it makes this a value class: Python owns
  #  every C++ QFontDef behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN8QFontDefD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def family(self) -> str:
    """
    Calls Qt's 'QString QFontDef::family() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontdef.html#family

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFontDef::family() const
    return self.uglySide.call('ritual_ZNK8QFontDef6familyEv')

  @overload(THIS)
  def exactMatch(self, other: QFontDef) -> bool:
    """
    Calls Qt's 'bool QFontDef::exactMatch(const QFontDef &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontdef.html#exactMatch

    Parameters
    ----------

    other : QFontDef
      Passed on as a value: Qt reads the C++ QFontDef, which stays Python's
      own.
    """
    #  bool QFontDef::exactMatch(const QFontDef &other) const
    return self.uglySide.call(
        'ritual_ZNK8QFontDef10exactMatchERKS_', self._valueOf(other),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QFontDef) -> bool:
    """
    Calls Qt's 'bool QFontDef::operator==(const QFontDef &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontdef.html#operator==

    Parameters
    ----------

    other : QFontDef
      Passed on as a value: Qt reads the C++ QFontDef, which stays Python's
      own.
    """
    #  bool QFontDef::operator==(const QFontDef &other) const
    return self.uglySide.call(
        'ritual_ZNK8QFontDefeqERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __lt__(self, other: QFontDef) -> bool:
    """
    Calls Qt's 'bool QFontDef::operator<(const QFontDef &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontdef.html#operator<

    Parameters
    ----------

    other : QFontDef
      Passed on as a value: Qt reads the C++ QFontDef, which stays Python's
      own.
    """
    #  bool QFontDef::operator<(const QFontDef &other) const
    return self.uglySide.call(
        'ritual_ZNK8QFontDefltERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __lt__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QFontDef::QFontDef()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfontdef.html#QFontDef
    """
    #  QFontDef::QFontDef()
    self._noteCreation(QFontDef, lambda: Rituals.call(
        'ritual_ZN8QFontDefC1Ev',
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
