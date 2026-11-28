"""
QtCbor::Element binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qcborvalue_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QtCbor::Element to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute, WAIT
from ..occult import Rituals
from . import QCborValue

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QCborContainerPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCborContainerPrivate = WAIT['QCborContainerPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Element(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtCbor::Element: a plain Python object standing in
  front of one C++ QtCbor::Element.

  C++ hands a QtCbor::Element around as a copy, so every C++ QtCbor::Element
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QtCbor::Element that has a ritual and that Python
  can call so far, 1 name in all: 'fpvalue'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtCbor::Element::~Element()': the destructor: Python removes its
    C++ QtCbor::Element by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QtCbor::Element is created at the first use, not by
    'QtCbor::Element(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtCbor::Element back gives a copy the ritual made for
    Python, in a new cute QtCbor::Element.
  """

  #  The enums Qt writes inside QtCbor::Element, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ValueFlag(CuteFlags, number='unsigned int'):
    """
    The flags enum 'QtCbor::Element::ValueFlag' of Qt, with the 4 names Qt
    gives in it. Qt names the type of its combinations
    'QtCbor::Element::ValueFlags'.
    """

    IsContainer = 0x1
    HasByteData = 0x2
    StringIsUtf16 = 0x4
    StringIsAscii = 0x8

  ValueFlags = ValueFlag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtCbor::Element'

  #  Qt's '~QtCbor::Element()'. Naming it makes this a value class: Python
  #  owns every C++ QtCbor::Element behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN6QtCbor7ElementD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def fpvalue(self) -> float:
    """
    Calls Qt's 'double QtCbor::Element::fpvalue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtcbor-element.html#fpvalue
    """
    #  double QtCbor::Element::fpvalue() const
    return self.uglySide.call('ritual_ZNK6QtCbor7Element7fpvalueEv')

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
  @overload(int)
  @overload(int, QCborValue.Type)
  @overload(int, QCborValue.Type, ValueFlags)
  def __init__(
      self,
      v: int = 0,
      t: QCborValue.Type = QCborValue.Type.Undefined,
      f: ValueFlags = ValueFlags(),
  ) -> None:
    """
    Notes what was given, for Qt's 'QtCbor::Element::Element(qint64 v,
    QCborValue::Type t, ValueFlags f)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtcbor-element.html#Element

    Parameters
    ----------

    v : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    t : QCborValue.Type
      Passed on as its number. May be left out, as in Qt: it is then
      QCborValue.Type.Undefined.

    f : ValueFlags
      Passed on as its number. May be left out, as in Qt: it is then
      ValueFlags().
    """
    #  QtCbor::Element::Element(qint64 v, QCborValue::Type t, ValueFlags f)
    self._noteCreation(Element, lambda: Rituals.call(
        'ritual_ZN6QtCbor7ElementC1ExN10QCborValue4TypeE6QFlagsINS0_9ValueF'
        'lagEE',
        v, t.value, f.value,
    ))

  @overload(QCborContainerPrivate, QCborValue.Type)
  @overload(NoneType, QCborValue.Type)
  @overload(QCborContainerPrivate, QCborValue.Type, ValueFlags)
  @overload(NoneType, QCborValue.Type, ValueFlags)
  def __init__(
      self,
      d: Optional[QCborContainerPrivate],
      t: QCborValue.Type,
      f: ValueFlags = ValueFlags(),
  ) -> None:
    """
    Notes what was given, for Qt's
    'QtCbor::Element::Element(QCborContainerPrivate *d, QCborValue::Type t,
    ValueFlags f)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtcbor-element.html#Element

    Parameters
    ----------

    d : Optional[QCborContainerPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    t : QCborValue.Type
      Passed on as its number.

    f : ValueFlags
      Passed on as its number. May be left out, as in Qt: it is then
      ValueFlags().
    """
    #  QtCbor::Element::Element(QCborContainerPrivate *d, QCborValue::Type t,
    #      ValueFlags f)
    self._noteCreation(Element, lambda: Rituals.call(
        'ritual_ZN6QtCbor7ElementC1EP21QCborContainerPrivateN10QCborValue4T'
        'ypeE6QFlagsINS0_9ValueFlagEE',
        self._addressOf(d), t.value, f.value,
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
