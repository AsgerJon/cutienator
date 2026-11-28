"""
QCss::Scanner binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qcssparser_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QCss::Scanner to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class Scanner(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCss::Scanner: a plain Python object standing in
  front of one C++ QCss::Scanner.

  C++ hands a QCss::Scanner around as a copy, so every C++ QCss::Scanner
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QCss::Scanner yet. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QString QCss::Scanner::preprocess(const QString &input, bool
    *hasEscapeSequences)': takes a number to change where it is.
  - Qt's 'void QCss::Scanner::scan(const QString &preprocessedInput,
    QList<Symbol> *symbols)': names 'QList<QCss::Symbol>', which has no cute
    class yet.
  - Qt's 'QCss::Scanner::~Scanner()': the destructor: Python removes its C++
    QCss::Scanner by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QCss::Scanner is created at the first use, not by
    'QCss::Scanner(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCss::Scanner back gives a copy the ritual made for
    Python, in a new cute QCss::Scanner.
  - Each name of Qt's QCss::Scanner that has no cute function yet,
    'preprocess', 'scan', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCss::Scanner'

  #  Qt's '~QCss::Scanner()'. Naming it makes this a value class: Python owns
  #  every C++ QCss::Scanner behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN4QCss7ScannerD1Ev'

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
  def preprocess(*__, **_) -> Never:
    """
    Qt's 'QString QCss::Scanner::preprocess(const QString &input, bool
    *hasEscapeSequences)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QCss.Scanner.preprocess' has no cute function yet. Qt's 'QString "
        "QCss::Scanner::preprocess(const QString &input, bool "
        "*hasEscapeSequences)': takes a number to change where it is.")

  @staticmethod
  def scan(*__, **_) -> Never:
    """
    Qt's 'void QCss::Scanner::scan(const QString &preprocessedInput,
    QList<Symbol> *symbols)': names 'QList<QCss::Symbol>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QCss.Scanner.scan' has no cute function yet. Qt's 'void "
        "QCss::Scanner::scan(const QString &preprocessedInput, "
        "QList<Symbol> *symbols)': names 'QList<QCss::Symbol>', which has "
        "no cute class yet.")
