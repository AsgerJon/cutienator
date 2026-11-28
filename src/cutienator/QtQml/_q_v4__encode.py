"""
QV4::Encode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4staticvalue_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::Encode to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Encode(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::Encode: a plain Python object standing in front
  of one C++ QV4::Encode.

  C++ hands a QV4::Encode around as a copy, so every C++ QV4::Encode behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QV4::Encode that has a ritual and that Python can
  call so far, 3 names in all: 'undefined', 'null', 'smallestNumber'. It can
  be made from Python, in 5 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::Encode::Encode(uint i)': takes in Python what
    'QV4::Encode::Encode(int i)' takes.
  - Qt's 'QV4::Encode::Encode(ReturnedValue v)': takes in Python what
    'QV4::Encode::Encode(int i)' takes.
  - Qt's 'ReturnedValue QV4::Encode::operator unsigned long long() const': an
    operator Python has no name for.
  - Qt's 'QV4::Encode::~Encode()': the destructor: Python removes its C++
    QV4::Encode by it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 1 a template; 1 not a gap.

  What to expect
  --------------

  - The C++ QV4::Encode is created at the first use, not by
    'QV4::Encode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::Encode back gives a copy the ritual made for
    Python, in a new cute QV4::Encode.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def undefined() -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Encode::undefined()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-encode.html#undefined
    """
    #  ReturnedValue QV4::Encode::undefined()
    return Rituals.call('ritual_ZN3QV46Encode9undefinedEv')

  @staticmethod
  def null() -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Encode::null()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-encode.html#null
    """
    #  ReturnedValue QV4::Encode::null()
    return Rituals.call('ritual_ZN3QV46Encode4nullEv')

  @staticmethod
  @overload(float)
  def smallestNumber(d: float) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Encode::smallestNumber(double d)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-encode.html#smallestNumber

    Parameters
    ----------

    d : float
      Passed on as it is.
    """
    #  ReturnedValue QV4::Encode::smallestNumber(double d)
    return Rituals.call('ritual_ZN3QV46Encode14smallestNumberEd', d)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Encode'

  #  Qt's '~QV4::Encode()'. Naming it makes this a value class: Python owns
  #  every C++ QV4::Encode behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV46EncodeD1Ev'

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

  @overload(bool)
  def __init__(self, b: bool) -> None:
    """
    Notes what was given, for Qt's 'QV4::Encode::Encode(bool b)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qv4-encode.html#Encode

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  QV4::Encode::Encode(bool b)
    self._noteCreation(Encode, lambda: Rituals.call(
        'ritual_ZN3QV46EncodeC1Eb', b,
    ))

  @overload(float)
  def __init__(self, d: float) -> None:
    """
    Notes what was given, for Qt's 'QV4::Encode::Encode(double d)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qv4-encode.html#Encode

    Parameters
    ----------

    d : float
      Passed on as it is.
    """
    #  QV4::Encode::Encode(double d)
    self._noteCreation(Encode, lambda: Rituals.call(
        'ritual_ZN3QV46EncodeC1Ed', d,
    ))

  @overload(int)
  def __init__(self, i: int) -> None:
    """
    Notes what was given, for Qt's 'QV4::Encode::Encode(int i)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qv4-encode.html#Encode

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  QV4::Encode::Encode(int i)
    self._noteCreation(Encode, lambda: Rituals.call(
        'ritual_ZN3QV46EncodeC1Ei', i,
    ))

  @overload(WAIT['QV4.StaticValue'])
  def __init__(self, v: QV4.StaticValue) -> None:
    """
    Notes what was given, for Qt's 'QV4::Encode::Encode(StaticValue v)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qv4-encode.html#Encode

    Parameters
    ----------

    v : QV4.StaticValue
      Passed on as a value: Qt reads the C++ QV4::StaticValue, which stays
      Python's own.
    """
    #  QV4::Encode::Encode(StaticValue v)
    self._noteCreation(Encode, lambda: Rituals.call(
        'ritual_ZN3QV46EncodeC1ENS_11StaticValueE', self._valueOf(v),
    ))

  @overload(NoneType)
  def __init__(self, o: Optional[QV4.StaticValue]) -> None:
    """
    Notes what was given, for Qt's 'QV4::Encode::Encode(StaticValue *o)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qv4-encode.html#Encode

    Parameters
    ----------

    o : Optional[QV4.StaticValue]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QV4::Encode::Encode(StaticValue *o)
    self._noteCreation(Encode, lambda: Rituals.call(
        'ritual_ZN3QV46EncodeC1EPNS_11StaticValueE', self._addressOf(o),
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
