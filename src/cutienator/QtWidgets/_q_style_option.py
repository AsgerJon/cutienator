"""
QStyleOption binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ._q_widget import QWidget
from ._q_style_option_option_type import OptionType
from ._q_style_option_style_option_type import StyleOptionType
from ._q_style_option_style_option_version import StyleOptionVersion

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QStyleOption(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QStyleOption: a plain Python object standing in front
  of one C++ QStyleOption.

  C++ hands a QStyleOption around as a copy, so every C++ QStyleOption behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QStyleOption that has a ritual and that Python can
  call so far, 1 name in all: 'initFrom'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStyleOption::~QStyleOption()': the destructor: Python removes its
    C++ QStyleOption by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 5 functions Qt declares: 1 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QStyleOption is created at the first use, not by
    'QStyleOption(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QStyleOption back gives a copy the ritual made for
    Python, in a new cute QStyleOption.
  """

  #  The enums Qt writes inside QStyleOption, and the names Qt has for the
  #  combinations of its flags enums.
  OptionType = OptionType
  StyleOptionType = StyleOptionType
  StyleOptionVersion = StyleOptionVersion

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStyleOption'

  #  Qt's '~QStyleOption()'. Naming it makes this a value class: Python owns
  #  every C++ QStyleOption behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QStyleOptionD1Ev'

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
  @overload(int)
  @overload(int, int)
  def __init__(self, version: int = 1, type: int = 0) -> None:
    """
    Notes what was given, for Qt's 'QStyleOption::QStyleOption(int version,
    int type)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstyleoption.html#QStyleOption

    Parameters
    ----------

    version : int
      Passed on as it is. May be left out, as in Qt: it is then 1.

    type : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  QStyleOption::QStyleOption(int version, int type)
    self._noteCreation(QStyleOption, lambda: Rituals.call(
        'ritual_ZN12QStyleOptionC1Eii', version, type,
    ))

  @overload(THIS)
  def __init__(self, other: QStyleOption) -> None:
    """
    Notes what was given, for Qt's 'QStyleOption::QStyleOption(const
    QStyleOption &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstyleoption.html#QStyleOption

    Parameters
    ----------

    other : QStyleOption
      Passed on as a value: Qt reads the C++ QStyleOption, which stays
      Python's own.
    """
    #  QStyleOption::QStyleOption(const QStyleOption &other)
    self._noteCreation(QStyleOption, lambda: Rituals.call(
        'ritual_ZN12QStyleOptionC1ERKS_', self._valueOf(other),
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

  @overload(QWidget)
  @overload(NoneType)
  def initFrom(self, w: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QStyleOption::initFrom(const QWidget *w)'.

    Qt's own words: https://doc.qt.io/qt-6/qstyleoption.html#initFrom

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStyleOption::initFrom(const QWidget *w)
    self.uglySide.call(
        'ritual_ZN12QStyleOption8initFromEPK7QWidget', self._addressOf(w),
    )
