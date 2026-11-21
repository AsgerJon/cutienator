"""
QTextLength binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qtextformat.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals


class QTextLength(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTextLength: a plain Python object standing in front
  of one C++ QTextLength.

  C++ hands a QTextLength around as a copy, so every C++ QTextLength behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTextLength that has a ritual and that Python can
  call so far, 3 names in all: 'type', 'value', 'rawValue'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool QTextLength::operator==(const QTextLength &other) const': an
    operator, which is not reflected yet.
  - Qt's 'bool QTextLength::operator!=(const QTextLength &other) const': an
    operator, which is not reflected yet.
  - Qt's 'QVariant QTextLength::operator QVariant() const': an operator,
    which is not reflected yet.
  - Qt's 'QTextLength::~QTextLength()': the destructor: Python removes its
    C++ QTextLength by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QTextLength is created at the first use, not by
    'QTextLength(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTextLength back gives a copy the ritual made for
    Python, in a new cute QTextLength.
  """

  #  The enums Qt writes inside QTextLength, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Type(CuteNum):
    """
    The enum 'QTextLength::Type' of Qt, with the 3 names Qt gives in it.
    """

    VariableLength = Kee[int](0)
    FixedLength = Kee[int](1)
    PercentageLength = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextLength'

  #  Qt's '~QTextLength()'. Naming it makes this a value class: Python owns
  #  every C++ QTextLength behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QTextLengthD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> Type:
    """
    Calls Qt's 'Type QTextLength::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlength.html#type

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type QTextLength::type() const
    return QTextLength.Type(self.uglySide.call(
        'ritual_ZNK11QTextLength4typeEv',
    ))

  @overload(float)
  def value(self, maximumLength: float) -> float:
    """
    Calls Qt's 'qreal QTextLength::value(qreal maximumLength) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlength.html#value

    Parameters
    ----------

    maximumLength : float
      Passed on as it is.
    """
    #  qreal QTextLength::value(qreal maximumLength) const
    return self.uglySide.call(
        'ritual_ZNK11QTextLength5valueEd', maximumLength,
    )

  def rawValue(self) -> float:
    """
    Calls Qt's 'qreal QTextLength::rawValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlength.html#rawValue
    """
    #  qreal QTextLength::rawValue() const
    return self.uglySide.call('ritual_ZNK11QTextLength8rawValueEv')

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
    Notes what was given, for Qt's 'QTextLength::QTextLength()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtextlength.html#QTextLength
    """
    #  QTextLength::QTextLength()
    self._noteCreation(QTextLength, lambda: Rituals.call(
        'ritual_ZN11QTextLengthC1Ev',
    ))

  @overload(Type, float)
  def __init__(self, type: Type, value: float) -> None:
    """
    Notes what was given, for Qt's 'QTextLength::QTextLength(Type type, qreal
    value)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtextlength.html#QTextLength

    Parameters
    ----------

    type : Type
      Passed on as its number.

    value : float
      Passed on as it is.
    """
    #  QTextLength::QTextLength(Type type, qreal value)
    self._noteCreation(QTextLength, lambda: Rituals.call(
        'ritual_ZN11QTextLengthC1ENS_4TypeEd', type.value, value,
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
