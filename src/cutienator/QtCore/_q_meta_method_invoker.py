"""
QMetaMethodInvoker binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qmetaobject_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QMetaMethodInvoker to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.keenum import Kee

from ..cute import CuteNum
from . import QMetaMethod


class QMetaMethodInvoker(QMetaMethod):
  """
  The cute side of Qt's QMetaMethodInvoker: a plain Python object standing in
  front of one C++ QMetaMethodInvoker.

  It is built on the cute 'QMetaMethod', as Qt's QMetaMethodInvoker is built
  on Qt's QMetaMethod, and has everything that class has.

  C++ hands a QMetaMethodInvoker around as a copy, so every C++
  QMetaMethodInvoker behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QMetaMethodInvoker yet. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'InvokeFailReason QMetaMethodInvoker::invokeImpl(QMetaMethod self_,
    void *target, Qt::ConnectionType a2, qsizetype paramCount, const void
    *const *parameters, const char *const *typeNames, const
    QtPrivate::QMetaTypeInterface *const *metaTypes)': names 'void', which
    has no cute class yet.
  - Qt's 'QMetaMethodInvoker::~QMetaMethodInvoker()': the destructor: Python
    removes its C++ QMetaMethodInvoker by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 3 functions Qt declares: 1 forbidden.

  What to expect
  --------------

  - The C++ QMetaMethodInvoker is created at the first use, not by
    'QMetaMethodInvoker(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMetaMethodInvoker back gives a copy the ritual made
    for Python, in a new cute QMetaMethodInvoker.
  """

  #  The enums Qt writes inside QMetaMethodInvoker, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class InvokeFailReason(CuteNum, scoped=True):
    """
    The enum 'QMetaMethodInvoker::InvokeFailReason' of Qt, with the 10 names
    Qt gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    ReturnTypeMismatch = Kee[int](-1)
    DeadLockDetected = Kee[int](-2)
    CallViaVirtualFailed = Kee[int](-3)
    ConstructorCallOnObject = Kee[int](-4)
    ConstructorCallWithoutResult = Kee[int](-5)
    ConstructorCallFailed = Kee[int](-6)
    CouldNotQueueParameter = Kee[int](-4096)
    NULL = Kee[int](0)
    TooFewArguments = Kee[int](1)
    FormalParameterMismatch = Kee[int](4096)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMetaMethodInvoker'

  #  Qt's '~QMetaMethodInvoker()'. Naming it makes this a value class: Python
  #  owns every C++ QMetaMethodInvoker behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QMetaMethodInvokerD1Ev'

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
