"""
QV4::Heap::SyntaxErrorObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4errorobject_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::Heap::SyntaxErrorObject to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QV4


class SyntaxErrorObject(QV4.Heap.ErrorObject):
  """
  The cute side of Qt's QV4::Heap::SyntaxErrorObject: a plain Python object
  standing in front of one C++ QV4::Heap::SyntaxErrorObject.

  It is built on the cute 'QV4::Heap::ErrorObject', as Qt's
  QV4::Heap::SyntaxErrorObject is built on Qt's QV4::Heap::ErrorObject, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::Heap::SyntaxErrorObject that has a ritual and
  that Python can call so far, 1 name in all: 'init'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What to expect
  --------------

  - The C++ QV4::Heap::SyntaxErrorObject is created at the first use, not by
    'QV4::Heap::SyntaxErrorObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Heap::SyntaxErrorObject.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Heap::SyntaxErrorObject'

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

  @overload(WAIT['QV4.Value'])
  def init(self, message: QV4.Value) -> None:
    """
    Calls Qt's 'void QV4::Heap::SyntaxErrorObject::init(const Value
    &message)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-syntaxerrorobject.html#init

    Parameters
    ----------

    message : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  void QV4::Heap::SyntaxErrorObject::init(const Value &message)
    self.uglySide.call(
        'ritual_ZN3QV44Heap17SyntaxErrorObject4initERKNS_5ValueE',
        self._valueOf(message),
    )

  @overload(WAIT['QV4.Value'], str, int, int)
  def init(
      self,
      msg: QV4.Value,
      fileName: str,
      lineNumber: int,
      columnNumber: int,
  ) -> None:
    """
    Calls Qt's 'void QV4::Heap::SyntaxErrorObject::init(const Value &msg,
    const QString &fileName, int lineNumber, int columnNumber)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-syntaxerrorobject.html#init

    Parameters
    ----------

    msg : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    lineNumber : int
      Passed on as it is.

    columnNumber : int
      Passed on as it is.
    """
    #  void QV4::Heap::SyntaxErrorObject::init(const Value &msg, const
    #      QString &fileName, int lineNumber, int columnNumber)
    self.uglySide.call(
        'ritual_ZN3QV44Heap17SyntaxErrorObject4initERKNS_5ValueERK7QStringi'
        'i',
        self._valueOf(msg), fileName, lineNumber, columnNumber,
    )
