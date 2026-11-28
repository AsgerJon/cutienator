"""
QInternalMessageLogContext binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qlogging_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QInternalMessageLogContext to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QMessageLogContext

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QInternalMessageLogContext(QMessageLogContext):
  """
  The cute side of Qt's QInternalMessageLogContext: a plain Python object
  standing in front of one C++ QInternalMessageLogContext.

  It is built on the cute 'QMessageLogContext', as Qt's
  QInternalMessageLogContext is built on Qt's QMessageLogContext, and has
  everything that class has.

  What exists
  -----------

  No function of Qt's QInternalMessageLogContext yet. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has no ritual
  ------------------

  4 of the 4 functions Qt declares: 2 leans on 'QInternalMessageLogContext; 1
  cannot be called and cannot be called through the meta-object and cannot be
  copied; 1 Qt's library has no name for it, and its code in Qt's source does
  not compile apart from its file.

  What to expect
  --------------

  - The C++ QInternalMessageLogContext is created at the first use, not by
    'QInternalMessageLogContext(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QInternalMessageLogContext.
  - Each name of Qt's QInternalMessageLogContext that has no cute function
    yet, '__init__', 'initFrom', 'populateBacktrace', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QInternalMessageLogContext'

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    - Qt's 'QInternalMessageLogContext::QInternalMessageLogContext(const
      QMessageLogContext &logContext)': leans on
      'QInternalMessageLogContext::populateBacktrace(int)', which Qt's source
      does not mark for use from outside Qt and has no code for that could be
      taken.
    - Qt's 'QInternalMessageLogContext::QInternalMessageLogContext(const
      QMessageLogContext &logContext, const QLoggingCategory
      &categoryOverride)': leans on
      'QInternalMessageLogContext::populateBacktrace(int)', which Qt's source
      does not mark for use from outside Qt and has no code for that could be
      taken.
    """
    raise NotImplementedError(
        "'QInternalMessageLogContext.__init__' has no cute function yet. "
        "Qt's 'QInternalMessageLogContext::QInternalMessageLogContext(const "
        "QMessageLogContext &logContext)': leans on "
        "'QInternalMessageLogContext::populateBacktrace(int)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken. Qt's "
        "'QInternalMessageLogContext::QInternalMessageLogContext(const "
        "QMessageLogContext &logContext, const QLoggingCategory "
        "&categoryOverride)': leans on "
        "'QInternalMessageLogContext::populateBacktrace(int)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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
  def initFrom(*__, **_) -> Never:
    """
    Qt's 'int QInternalMessageLogContext::initFrom(const QMessageLogContext
    &logContext)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'qMessagePattern'; did you mean 'QOpenGLBuffer::UsagePattern'?.
    """
    raise NotImplementedError(
        "'QInternalMessageLogContext.initFrom' has no cute function yet. "
        "Qt's 'int QInternalMessageLogContext::initFrom(const "
        "QMessageLogContext &logContext)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "use of undeclared identifier 'qMessagePattern'; did you mean "
        "'QOpenGLBuffer::UsagePattern'?.")

  @staticmethod
  def populateBacktrace(*__, **_) -> Never:
    """
    Qt's 'void QInternalMessageLogContext::populateBacktrace(int
    frameCount)': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QInternalMessageLogContext.populateBacktrace' has no cute "
        "function yet. Qt's 'void "
        "QInternalMessageLogContext::populateBacktrace(int frameCount)': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")
