"""
QPalettePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qpalette_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QPalettePrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QSharedData
from . import QPalette


class QPalettePrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPalettePrivate: a plain Python object standing in
  front of one C++ QPalettePrivate.

  C++ hands a QPalettePrivate around as a copy, so every C++ QPalettePrivate
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPalettePrivate that has a ritual and that Python
  can call so far, 2 names in all: 'colorRoleOffset', 'bitPosition'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPalettePrivate::QPalettePrivate(const
    QExplicitlySharedDataPointer<Data> &data)': takes a type Python has no
    way to hand over yet.
  - Qt's 'QPalettePrivate::~QPalettePrivate()': the destructor: Python
    removes its C++ QPalettePrivate by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QPalettePrivate is created at the first use, not by
    'QPalettePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPalettePrivate back gives a copy the ritual made for
    Python, in a new cute QPalettePrivate.
  """

  #  The classes Qt writes inside QPalettePrivate, each a class in here as in
  #  C++.

  class Data(QSharedData):
    """
    The cute side of Qt's QPalettePrivate::Data: a plain Python object
    standing in front of one C++ QPalettePrivate::Data.

    It is built on the cute 'QSharedData', as Qt's QPalettePrivate::Data is
    built on Qt's QSharedData, and has everything that class has.

    C++ hands a QPalettePrivate::Data around as a copy, so every C++
    QPalettePrivate::Data behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QPalettePrivate::Data yet. It can be made from
    Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QPalettePrivate::Data::~Data()': the destructor: Python removes
      its C++ QPalettePrivate::Data by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QPalettePrivate::Data is created at the first use, not by
      'QPalettePrivate::Data(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QPalettePrivate::Data back gives a copy the ritual
      made for Python, in a new cute QPalettePrivate::Data.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QPalettePrivate::Data'

    #  Qt's '~QPalettePrivate::Data()'. Naming it makes this a value class:
    #  Python owns every C++ QPalettePrivate::Data behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN15QPalettePrivate4DataD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(THIS)
    def __init__(self, other: QPalettePrivate.Data) -> None:
      """
      Notes what was given, for Qt's 'QPalettePrivate::Data::Data(const Data
      &other)', which is called at the first use.

      Qt's own words: https://doc.qt.io/qt-6/qpaletteprivate-data.html#Data

      Parameters
      ----------

      other : QPalettePrivate.Data
        Passed on as a value: Qt reads the C++ QPalettePrivate::Data, which
        stays Python's own.
      """
      #  QPalettePrivate::Data::Data(const Data &other)
      self._noteCreation(QPalettePrivate.Data, lambda: Rituals.call(
          'ritual_ZN15QPalettePrivate4DataC1ERKS0_', self._valueOf(other),
      ))

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's 'QPalettePrivate::Data::Data()', which
      is called at the first use.

      Qt's own words: https://doc.qt.io/qt-6/qpaletteprivate-data.html#Data
      """
      #  QPalettePrivate::Data::Data()
      self._noteCreation(QPalettePrivate.Data, lambda: Rituals.call(
          'ritual_ZN15QPalettePrivate4DataC1Ev',
      ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QPalette.ColorGroup)
  def colorRoleOffset(colorGroup: QPalette.ColorGroup) -> int:
    """
    Calls Qt's 'QPalette::ResolveMask
    QPalettePrivate::colorRoleOffset(QPalette::ColorGroup colorGroup)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaletteprivate.html#colorRoleOffset

    Parameters
    ----------

    colorGroup : QPalette.ColorGroup
      Passed on as its number.
    """
    #  QPalette::ResolveMask
    #      QPalettePrivate::colorRoleOffset(QPalette::ColorGroup colorGroup)
    return Rituals.call(
        'ritual_ZN15QPalettePrivate15colorRoleOffsetEN8QPalette10ColorGroup'
        'E',
        colorGroup.value,
    )

  @staticmethod
  @overload(QPalette.ColorGroup, QPalette.ColorRole)
  def bitPosition(
      colorGroup: QPalette.ColorGroup,
      colorRole: QPalette.ColorRole,
  ) -> int:
    """
    Calls Qt's 'QPalette::ResolveMask
    QPalettePrivate::bitPosition(QPalette::ColorGroup colorGroup,
    QPalette::ColorRole colorRole)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaletteprivate.html#bitPosition

    Parameters
    ----------

    colorGroup : QPalette.ColorGroup
      Passed on as its number.

    colorRole : QPalette.ColorRole
      Passed on as its number.
    """
    #  QPalette::ResolveMask
    #      QPalettePrivate::bitPosition(QPalette::ColorGroup colorGroup,
    #      QPalette::ColorRole colorRole)
    return Rituals.call(
        'ritual_ZN15QPalettePrivate11bitPositionEN8QPalette10ColorGroupENS0'
        '_9ColorRoleE',
        colorGroup.value, colorRole.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPalettePrivate'

  #  Qt's '~QPalettePrivate()'. Naming it makes this a value class: Python
  #  owns every C++ QPalettePrivate behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QPalettePrivateD1Ev'

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
    Notes what was given, for Qt's 'QPalettePrivate::QPalettePrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaletteprivate.html#QPalettePrivate
    """
    #  QPalettePrivate::QPalettePrivate()
    self._noteCreation(QPalettePrivate, lambda: Rituals.call(
        'ritual_ZN15QPalettePrivateC1Ev',
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
