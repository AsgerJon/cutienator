"""
QCss::BrushData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qcssparser_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QCss::BrushData to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QPalette

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QBrush
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBrush = WAIT['QBrush']


class BrushData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCss::BrushData: a plain Python object standing in
  front of one C++ QCss::BrushData.

  C++ hands a QCss::BrushData around as a copy, so every C++ QCss::BrushData
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QCss::BrushData yet. It can be made from Python, in 3
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCss::BrushData::~BrushData()': the destructor: Python removes its
    C++ QCss::BrushData by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QCss::BrushData is created at the first use, not by
    'QCss::BrushData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCss::BrushData back gives a copy the ritual made for
    Python, in a new cute QCss::BrushData.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCss::BrushData'

  #  Qt's '~QCss::BrushData()'. Naming it makes this a value class: Python
  #  owns every C++ QCss::BrushData behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN4QCss9BrushDataD1Ev'

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
    Notes what was given, for Qt's 'QCss::BrushData::BrushData()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcss-brushdata.html#BrushData
    """
    #  QCss::BrushData::BrushData()
    self._noteCreation(BrushData, lambda: Rituals.call(
        'ritual_ZN4QCss9BrushDataC1Ev',
    ))

  @overload(QBrush)
  def __init__(self, br: QBrush) -> None:
    """
    Notes what was given, for Qt's 'QCss::BrushData::BrushData(const QBrush
    &br)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcss-brushdata.html#BrushData

    Parameters
    ----------

    br : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  QCss::BrushData::BrushData(const QBrush &br)
    self._noteCreation(BrushData, lambda: Rituals.call(
        'ritual_ZN4QCss9BrushDataC1ERK6QBrush', self._valueOf(br),
    ))

  @overload(QPalette.ColorRole)
  def __init__(self, r: QPalette.ColorRole) -> None:
    """
    Notes what was given, for Qt's
    'QCss::BrushData::BrushData(QPalette::ColorRole r)', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcss-brushdata.html#BrushData

    Parameters
    ----------

    r : QPalette.ColorRole
      Passed on as its number.
    """
    #  QCss::BrushData::BrushData(QPalette::ColorRole r)
    self._noteCreation(BrushData, lambda: Rituals.call(
        'ritual_ZN4QCss9BrushDataC1EN8QPalette9ColorRoleE', r.value,
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
