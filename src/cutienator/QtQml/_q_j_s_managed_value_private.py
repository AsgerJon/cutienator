"""
QJSManagedValuePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qjsmanagedvalue_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QJSManagedValuePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QJSManagedValue
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJSManagedValue = WAIT['QJSManagedValue']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QJSManagedValuePrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QJSManagedValuePrivate: a plain Python object
  standing in front of one C++ QJSManagedValuePrivate.

  C++ hands a QJSManagedValuePrivate around as a copy, so every C++
  QJSManagedValuePrivate behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QJSManagedValuePrivate that has a ritual and that
  Python can call so far, 1 name in all: 'member'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QJSManagedValue QJSManagedValuePrivate::create(QV4::ExecutionEngine
    *engine, const QV4::Value &value)': gives a type Python has no way to
    take yet.
  - Qt's 'QJSManagedValue QJSManagedValuePrivate::create(const QV4::Managed
    &managed)': takes a type Python has no way to hand over yet.
  - Qt's 'QJSManagedValuePrivate::~QJSManagedValuePrivate()': the destructor:
    Python removes its C++ QJSManagedValuePrivate by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QJSManagedValuePrivate is created at the first use, not by
    'QJSManagedValuePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QJSManagedValuePrivate back gives a copy the ritual
    made for Python, in a new cute QJSManagedValuePrivate.
  - Each name of Qt's QJSManagedValuePrivate that has no cute function yet,
    'create', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QJSManagedValue)
  @overload(NoneType)
  def member(jsmv: Optional[QJSManagedValue]) -> Optional[QV4.Value]:
    """
    Calls Qt's 'QV4::Value *QJSManagedValuePrivate::member(const
    QJSManagedValue *jsmv)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsmanagedvalueprivate.html#member

    Parameters
    ----------

    jsmv : Optional[QJSManagedValue]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Value]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Value *QJSManagedValuePrivate::member(const QJSManagedValue
    #      *jsmv)
    address = Rituals.call(
        'ritual_ZN22QJSManagedValuePrivate6memberEPK15QJSManagedValue',
        CuteMixin._addressOf(jsmv),
    )
    return QV4.Value._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QJSManagedValuePrivate'

  #  Qt's '~QJSManagedValuePrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QJSManagedValuePrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QJSManagedValuePrivateD1Ev'

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
  def create(*__, **_) -> Never:
    """
    - Qt's 'QJSManagedValue
      QJSManagedValuePrivate::create(QV4::ExecutionEngine *engine, const
      QV4::Value &value)': gives a type Python has no way to take yet.
    - Qt's 'QJSManagedValue QJSManagedValuePrivate::create(const QV4::Managed
      &managed)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QJSManagedValuePrivate.create' has no cute function yet. Qt's "
        "'QJSManagedValue "
        "QJSManagedValuePrivate::create(QV4::ExecutionEngine *engine, const "
        "QV4::Value &value)': gives a type Python has no way to take yet. "
        "Qt's 'QJSManagedValue QJSManagedValuePrivate::create(const "
        "QV4::Managed &managed)': takes a type Python has no way to hand "
        "over yet.")
