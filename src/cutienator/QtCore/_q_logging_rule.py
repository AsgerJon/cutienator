"""
QLoggingRule binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qloggingregistry_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QLoggingRule to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute
from ..occult import Rituals
from . import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QLoggingRule(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QLoggingRule: a plain Python object standing in front
  of one C++ QLoggingRule.

  C++ hands a QLoggingRule around as a copy, so every C++ QLoggingRule behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLoggingRule that has a ritual and that Python can
  call so far, 1 name in all: 'parse'. It can be made from Python, in 2 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'int QLoggingRule::pass(QLatin1StringView categoryName, QtMsgType
    type) const': names the enum 'QtMsgType', whose class cannot be named
    here.
  - Qt's 'QLoggingRule::~QLoggingRule()': the destructor: Python removes its
    C++ QLoggingRule by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QLoggingRule is created at the first use, not by
    'QLoggingRule(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLoggingRule back gives a copy the ritual made for
    Python, in a new cute QLoggingRule.
  - Each name of Qt's QLoggingRule that has no cute function yet, 'pass_',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QLoggingRule, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class PatternFlag(CuteFlags):
    """
    The flags enum 'QLoggingRule::PatternFlag' of Qt, with the 4 names Qt
    gives in it. Qt names the type of its combinations
    'QLoggingRule::PatternFlags'.
    """

    FullText = 0x1
    LeftFilter = 0x2
    RightFilter = 0x4
    MidFilter = 0x6

  PatternFlags = PatternFlag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLoggingRule'

  #  Qt's '~QLoggingRule()'. Naming it makes this a value class: Python owns
  #  every C++ QLoggingRule behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QLoggingRuleD1Ev'

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
    Notes what was given, for Qt's 'QLoggingRule::QLoggingRule()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qloggingrule.html#QLoggingRule
    """
    #  QLoggingRule::QLoggingRule()
    self._noteCreation(QLoggingRule, lambda: Rituals.call(
        'ritual_ZN12QLoggingRuleC1Ev',
    ))

  @overload(str, bool)
  def __init__(self, pattern: str, enabled: bool) -> None:
    """
    Notes what was given, for Qt's 'QLoggingRule::QLoggingRule(QStringView
    pattern, bool enabled)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qloggingrule.html#QLoggingRule

    Parameters
    ----------

    pattern : str
      Passed on as it is: a QString is made of it for the call.

    enabled : bool
      Passed on as it is.
    """
    #  QLoggingRule::QLoggingRule(QStringView pattern, bool enabled)
    self._noteCreation(QLoggingRule, lambda: Rituals.call(
        'ritual_ZN12QLoggingRuleC1E11QStringViewb', pattern, enabled,
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

  @overload(str)
  def parse(self, pattern: str) -> None:
    """
    Calls Qt's 'void QLoggingRule::parse(QStringView pattern)'.

    Qt's own words: https://doc.qt.io/qt-6/qloggingrule.html#parse

    Parameters
    ----------

    pattern : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QLoggingRule::parse(QStringView pattern)
    self.uglySide.call(
        'ritual_ZN12QLoggingRule5parseE11QStringView', pattern,
    )

  @staticmethod
  def pass_(*__, **_) -> Never:
    """
    Qt's 'int QLoggingRule::pass(QLatin1StringView categoryName, QtMsgType
    type) const': names the enum 'QtMsgType', whose class cannot be named
    here.
    """
    raise NotImplementedError(
        "'QLoggingRule.pass_' has no cute function yet. Qt's 'int "
        "QLoggingRule::pass(QLatin1StringView categoryName, QtMsgType type) "
        "const': names the enum 'QtMsgType', whose class cannot be named "
        "here.")


#  Qt's 'QList<QLoggingRule>': the list of QLoggingRule, which
#  'QList[QLoggingRule]' gives. It is made here, so that there is one as soon
#  as there can be a QLoggingRule.
QList.createKind(
    QLoggingRule, 'value',
    make='ritual_list_make_QLoggingRule',
    add='ritual_list_add_QLoggingRule',
    size='ritual_list_size_QLoggingRule',
    at='ritual_list_at_QLoggingRule',
    drop='ritual_list_drop_QLoggingRule',
)
