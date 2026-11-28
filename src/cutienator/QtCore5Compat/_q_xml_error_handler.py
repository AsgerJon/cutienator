"""
QXmlErrorHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore5Compat/qxml.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QXmlParseException
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QXmlParseException = WAIT['QXmlParseException']


class QXmlErrorHandler(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QXmlErrorHandler: a plain Python object standing in
  front of one C++ QXmlErrorHandler.

  What exists
  -----------

  Every function of Qt's QXmlErrorHandler that has a ritual and that Python
  can call so far, 4 names in all: 'warning', 'error', 'fatalError',
  'errorString'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QXmlErrorHandler::~QXmlErrorHandler()': the destructor: Python
    never removes a C++ QXmlErrorHandler.

  What to expect
  --------------

  - The C++ QXmlErrorHandler is created at the first use, not by
    'QXmlErrorHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QXmlErrorHandler.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QXmlErrorHandler'

  #  A C++ QXmlErrorHandler Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QXmlErrorHandler'

  #  The functions Qt calls itself that QXmlErrorHandler is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'warning': (
          ('_ZN16QXmlErrorHandler7warningERK18QXmlParseException',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore5Compat:QXmlParseException'),
           )),
      ),
      'error': (
          ('_ZN16QXmlErrorHandler5errorERK18QXmlParseException',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore5Compat:QXmlParseException'),
           )),
      ),
      'fatalError': (
          ('_ZN16QXmlErrorHandler10fatalErrorERK18QXmlParseException',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore5Compat:QXmlParseException'),
           )),
      ),
      'errorString': (
          ('_ZNK16QXmlErrorHandler11errorStringEv',
           ('address', 'text', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QXmlErrorHandler::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlerrorhandler.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QXmlErrorHandler::errorString() const
    return self._callAs(
        'QXmlErrorHandler', 'ritual_ZNK16QXmlErrorHandler11errorStringEv',
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

  @overload(QXmlParseException)
  def warning(self, exception: QXmlParseException) -> bool:
    """
    Calls Qt's 'bool QXmlErrorHandler::warning(const QXmlParseException
    &exception)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlerrorhandler.html#warning

    Parameters
    ----------

    exception : QXmlParseException
      Passed on as a value: Qt reads the C++ QXmlParseException, which stays
      Python's own.
    """
    #  bool QXmlErrorHandler::warning(const QXmlParseException &exception)
    return self._callAs(
        'QXmlErrorHandler',
        'ritual_ZN16QXmlErrorHandler7warningERK18QXmlParseException',
        self._valueOf(exception),
    )

  @overload(QXmlParseException)
  def error(self, exception: QXmlParseException) -> bool:
    """
    Calls Qt's 'bool QXmlErrorHandler::error(const QXmlParseException
    &exception)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlerrorhandler.html#error

    Parameters
    ----------

    exception : QXmlParseException
      Passed on as a value: Qt reads the C++ QXmlParseException, which stays
      Python's own.
    """
    #  bool QXmlErrorHandler::error(const QXmlParseException &exception)
    return self._callAs(
        'QXmlErrorHandler',
        'ritual_ZN16QXmlErrorHandler5errorERK18QXmlParseException',
        self._valueOf(exception),
    )

  @overload(QXmlParseException)
  def fatalError(self, exception: QXmlParseException) -> bool:
    """
    Calls Qt's 'bool QXmlErrorHandler::fatalError(const QXmlParseException
    &exception)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlerrorhandler.html#fatalError

    Parameters
    ----------

    exception : QXmlParseException
      Passed on as a value: Qt reads the C++ QXmlParseException, which stays
      Python's own.
    """
    #  bool QXmlErrorHandler::fatalError(const QXmlParseException &exception)
    return self._callAs(
        'QXmlErrorHandler',
        'ritual_ZN16QXmlErrorHandler10fatalErrorERK18QXmlParseException',
        self._valueOf(exception),
    )
