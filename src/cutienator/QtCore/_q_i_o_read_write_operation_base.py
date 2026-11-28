"""
QIOReadWriteOperationBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qiooperation_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QIOReadWriteOperationBase to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QIOOperation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QIOReadWriteOperationBase(QIOOperation):
  """
  The cute side of Qt's QIOReadWriteOperationBase: a plain Python object
  standing in front of one C++ QIOReadWriteOperationBase.

  It is built on the cute 'QIOOperation', as Qt's QIOReadWriteOperationBase
  is built on Qt's QIOOperation, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QIOReadWriteOperationBase that has a ritual and that
  Python can call so far, 2 names in all: 'offset', 'numBytesProcessed'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QIOReadWriteOperationBase::~QIOReadWriteOperationBase()': the
    destructor: Python never removes a C++ QIOReadWriteOperationBase.
  - Qt's
    'QIOReadWriteOperationBase::QIOReadWriteOperationBase(QIOOperationPrivate
    &dd, QObject *parent)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  5 of the 9 functions Qt declares: 5 forbidden.

  What to expect
  --------------

  - The C++ QIOReadWriteOperationBase is created at the first use, not by
    'QIOReadWriteOperationBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QIOReadWriteOperationBase.
  - Qt tells when it has removed the C++ QIOReadWriteOperationBase. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QIOReadWriteOperationBase that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QIOReadWriteOperationBase'

  #  A C++ QIOReadWriteOperationBase Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QIOReadWriteOperationBase'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def offset(self) -> int:
    """
    Calls Qt's 'qint64 QIOReadWriteOperationBase::offset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qioreadwriteoperationbase.html#offset
    """
    #  qint64 QIOReadWriteOperationBase::offset() const
    return self.uglySide.call(
        'ritual_ZNK25QIOReadWriteOperationBase6offsetEv',
    )

  def numBytesProcessed(self) -> int:
    """
    Calls Qt's 'qint64 QIOReadWriteOperationBase::numBytesProcessed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qioreadwriteoperationbase.html#numBytesProcessed
    """
    #  qint64 QIOReadWriteOperationBase::numBytesProcessed() const
    return self.uglySide.call(
        'ritual_ZNK25QIOReadWriteOperationBase17numBytesProcessedEv',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's
    'QIOReadWriteOperationBase::QIOReadWriteOperationBase(QIOOperationPrivate
    &dd, QObject *parent)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QIOReadWriteOperationBase.__init__' has no cute function yet. "
        "Qt's "
        "'QIOReadWriteOperationBase::QIOReadWriteOperationBase(QIOOperationP"
        "rivate &dd, QObject *parent)': takes a type Python has no way to "
        "hand over yet.")

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
