"""
QMessageLogContext binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qlogging.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMessageLogContext(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMessageLogContext: a plain Python object standing in
  front of one C++ QMessageLogContext.

  What exists
  -----------

  No function of Qt's QMessageLogContext yet. It can be made from Python, in
  2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMessageLogContext &QMessageLogContext::copyContextFrom(const
    QMessageLogContext &logContext)': takes a type Python has no way to hand
    over yet.

  What has no ritual
  ------------------

  2 of the 5 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QMessageLogContext is created at the first use, not by
    'QMessageLogContext(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMessageLogContext.
  - Each name of Qt's QMessageLogContext that has no cute function yet,
    'copyContextFrom', holds a function that raises 'NotImplementedError',
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
  __qt_class__ = 'QMessageLogContext'

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
    Notes what was given, for Qt's
    'QMessageLogContext::QMessageLogContext()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmessagelogcontext.html#QMessageLogContext
    """
    #  QMessageLogContext::QMessageLogContext()
    self._noteCreation(QMessageLogContext, lambda: Rituals.call(
        'ritual_ZN18QMessageLogContextC1Ev',
    ))

  @overload(str, int, str, str)
  @overload(str, int, str, NoneType)
  @overload(str, int, NoneType, str)
  @overload(str, int, NoneType, NoneType)
  @overload(NoneType, int, str, str)
  @overload(NoneType, int, str, NoneType)
  @overload(NoneType, int, NoneType, str)
  @overload(NoneType, int, NoneType, NoneType)
  def __init__(
      self,
      fileName: Optional[str],
      lineNumber: int,
      functionName: Optional[str],
      categoryName: Optional[str],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QMessageLogContext::QMessageLogContext(const char *fileName, int
    lineNumber, const char *functionName, const char *categoryName)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmessagelogcontext.html#QMessageLogContext

    Parameters
    ----------

    fileName : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    lineNumber : int
      Passed on as it is.

    functionName : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    categoryName : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  QMessageLogContext::QMessageLogContext(const char *fileName, int
    #      lineNumber, const char *functionName, const char *categoryName)
    self._noteCreation(QMessageLogContext, lambda: Rituals.call(
        'ritual_ZN18QMessageLogContextC1EPKciS1_S1_',
        self._bytesOf(fileName), lineNumber, self._bytesOf(functionName),
        self._bytesOf(categoryName),
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

  @staticmethod
  def copyContextFrom(*__, **_) -> Never:
    """
    Qt's 'QMessageLogContext &QMessageLogContext::copyContextFrom(const
    QMessageLogContext &logContext)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QMessageLogContext.copyContextFrom' has no cute function yet. "
        "Qt's 'QMessageLogContext "
        "&QMessageLogContext::copyContextFrom(const QMessageLogContext "
        "&logContext)': takes a type Python has no way to hand over yet.")
