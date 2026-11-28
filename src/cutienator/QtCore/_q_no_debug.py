"""
QNoDebug binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtCore/qdebug.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QNoDebug(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QNoDebug: a plain Python object standing in front of
  one C++ QNoDebug.

  C++ hands a QNoDebug around as a copy, so every C++ QNoDebug behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QNoDebug yet. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNoDebug &QNoDebug::operator<<(QTextStreamFunction a0)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QNoDebug &QNoDebug::operator<<(QTextStreamManipulator a0)': gives a
    type Python has no way to take yet.
  - Qt's 'QNoDebug &QNoDebug::space()': gives a type Python has no way to
    take yet.
  - Qt's 'QNoDebug &QNoDebug::nospace()': gives a type Python has no way to
    take yet.
  - Qt's 'QNoDebug &QNoDebug::maybeSpace()': gives a type Python has no way
    to take yet.
  - Qt's 'QNoDebug &QNoDebug::quote()': gives a type Python has no way to
    take yet.
  - Qt's 'QNoDebug &QNoDebug::noquote()': gives a type Python has no way to
    take yet.
  - Qt's 'QNoDebug &QNoDebug::maybeQuote(const char a0)': takes a single
    letter as C has it.
  - Qt's 'QNoDebug &QNoDebug::verbosity(int a0)': gives a type Python has no
    way to take yet.
  - Qt's 'QNoDebug::~QNoDebug()': the destructor: Python removes its C++
    QNoDebug by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 11 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QNoDebug is created at the first use, not by 'QNoDebug(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QNoDebug back gives a copy the ritual made for
    Python, in a new cute QNoDebug.
  - Each name of Qt's QNoDebug that has no cute function yet, 'maybeQuote',
    'maybeSpace', 'noquote', 'nospace', 'quote', 'space', 'verbosity', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNoDebug'

  #  Qt's '~QNoDebug()'. Naming it makes this a value class: Python owns
  #  every C++ QNoDebug behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN8QNoDebugD1Ev'

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
  def maybeQuote(*__, **_) -> Never:
    """
    Qt's 'QNoDebug &QNoDebug::maybeQuote(const char a0)': takes a single
    letter as C has it.
    """
    raise NotImplementedError(
        "'QNoDebug.maybeQuote' has no cute function yet. Qt's 'QNoDebug "
        "&QNoDebug::maybeQuote(const char a0)': takes a single letter as C "
        "has it.")

  @staticmethod
  def maybeSpace(*__, **_) -> Never:
    """
    Qt's 'QNoDebug &QNoDebug::maybeSpace()': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'QNoDebug.maybeSpace' has no cute function yet. Qt's 'QNoDebug "
        "&QNoDebug::maybeSpace()': gives a type Python has no way to take "
        "yet.")

  @staticmethod
  def noquote(*__, **_) -> Never:
    """
    Qt's 'QNoDebug &QNoDebug::noquote()': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QNoDebug.noquote' has no cute function yet. Qt's 'QNoDebug "
        "&QNoDebug::noquote()': gives a type Python has no way to take yet.")

  @staticmethod
  def nospace(*__, **_) -> Never:
    """
    Qt's 'QNoDebug &QNoDebug::nospace()': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QNoDebug.nospace' has no cute function yet. Qt's 'QNoDebug "
        "&QNoDebug::nospace()': gives a type Python has no way to take yet.")

  @staticmethod
  def quote(*__, **_) -> Never:
    """
    Qt's 'QNoDebug &QNoDebug::quote()': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QNoDebug.quote' has no cute function yet. Qt's 'QNoDebug "
        "&QNoDebug::quote()': gives a type Python has no way to take yet.")

  @staticmethod
  def space(*__, **_) -> Never:
    """
    Qt's 'QNoDebug &QNoDebug::space()': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QNoDebug.space' has no cute function yet. Qt's 'QNoDebug "
        "&QNoDebug::space()': gives a type Python has no way to take yet.")

  @staticmethod
  def verbosity(*__, **_) -> Never:
    """
    Qt's 'QNoDebug &QNoDebug::verbosity(int a0)': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QNoDebug.verbosity' has no cute function yet. Qt's 'QNoDebug "
        "&QNoDebug::verbosity(int a0)': gives a type Python has no way to "
        "take yet.")
