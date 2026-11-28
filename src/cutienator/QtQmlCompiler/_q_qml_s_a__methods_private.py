"""
QQmlSA::MethodsPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmlsa_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQmlSA::MethodsPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from . import QQmlSA

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class MethodsPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlSA::MethodsPrivate: a plain Python object
  standing in front of one C++ QQmlSA::MethodsPrivate.

  C++ hands a QQmlSA::MethodsPrivate around as a copy, so every C++
  QQmlSA::MethodsPrivate behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlSA::MethodsPrivate that has a ritual and that
  Python can call so far, 1 name in all: 'q_func'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQmlSA::Method::Methods *QQmlSA::MethodsPrivate::q_func()
    const': takes in Python what 'QQmlSA::Method::Methods
    *QQmlSA::MethodsPrivate::q_func()' takes.
  - Qt's 'QQmlSA::MethodsPrivate::MethodsPrivate(QQmlSA::Method::Methods *a0,
    MethodsPrivate &&a1)': takes a type Python has no way to hand over yet.
  - Qt's 'QQmlSA::MethodsPrivate::~MethodsPrivate()': the destructor: Python
    removes its C++ QQmlSA::MethodsPrivate by it, and has no other use for
    it.
  - Qt's 'QMultiHash<QString, Method>::const_iterator
    QQmlSA::MethodsPrivate::constBegin() const': gives a type Python has no
    way to take yet.
  - Qt's 'QMultiHash<QString, Method>::const_iterator
    QQmlSA::MethodsPrivate::constEnd() const': gives a type Python has no way
    to take yet.
  - Qt's 'QQmlSA::Method::Methods QQmlSA::MethodsPrivate::createMethods(const
    QMultiHash<QString, QQmlJSMetaMethod> &a0)': takes a type Python has no
    way to hand over yet.

  What to expect
  --------------

  - The C++ QQmlSA::MethodsPrivate is created at the first use, not by
    'QQmlSA::MethodsPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlSA::MethodsPrivate back gives a copy the ritual
    made for Python, in a new cute QQmlSA::MethodsPrivate.
  - Each name of Qt's QQmlSA::MethodsPrivate that has no cute function yet,
    'constBegin', 'constEnd', 'createMethods', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlSA::MethodsPrivate'

  #  Qt's '~QQmlSA::MethodsPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QQmlSA::MethodsPrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN6QQmlSA14MethodsPrivateD1Ev'

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

  @overload(QQmlSA.Method.Methods)
  @overload(NoneType)
  def __init__(self, a0: Optional[QQmlSA.Method.Methods]) -> None:
    """
    Notes what was given, for Qt's
    'QQmlSA::MethodsPrivate::MethodsPrivate(QQmlSA::Method::Methods *a0)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-methodsprivate.html#MethodsPrivate

    Parameters
    ----------

    a0 : Optional[QQmlSA.Method.Methods]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlSA::MethodsPrivate::MethodsPrivate(QQmlSA::Method::Methods *a0)
    self._noteCreation(MethodsPrivate, lambda: Rituals.call(
        'ritual_ZN6QQmlSA14MethodsPrivateC1EPNS_6Method7MethodsE',
        self._addressOf(a0),
    ))

  @overload(QQmlSA.Method.Methods, THIS)
  @overload(NoneType, THIS)
  def __init__(
      self,
      a0: Optional[QQmlSA.Method.Methods],
      a1: MethodsPrivate,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlSA::MethodsPrivate::MethodsPrivate(QQmlSA::Method::Methods *a0,
    const MethodsPrivate &a1)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-methodsprivate.html#MethodsPrivate

    Parameters
    ----------

    a0 : Optional[QQmlSA.Method.Methods]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : MethodsPrivate
      Passed on as a value: Qt reads the C++ QQmlSA::MethodsPrivate, which
      stays Python's own.
    """
    #  QQmlSA::MethodsPrivate::MethodsPrivate(QQmlSA::Method::Methods *a0,
    #      const MethodsPrivate &a1)
    self._noteCreation(MethodsPrivate, lambda: Rituals.call(
        'ritual_ZN6QQmlSA14MethodsPrivateC1EPNS_6Method7MethodsERKS0_',
        self._addressOf(a0), self._valueOf(a1),
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

  def q_func(self) -> Optional[QQmlSA.Method.Methods]:
    """
    Calls Qt's 'QQmlSA::Method::Methods *QQmlSA::MethodsPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-methodsprivate.html#q_func

    Returns
    -------

    Optional[QQmlSA.Method.Methods]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlSA::Method::Methods *QQmlSA::MethodsPrivate::q_func()
    address = self.uglySide.call('ritual_ZN6QQmlSA14MethodsPrivate6q_funcEv')
    return QQmlSA.Method.Methods._cuteAt(address)

  @staticmethod
  def constBegin(*__, **_) -> Never:
    """
    Qt's 'QMultiHash<QString, Method>::const_iterator
    QQmlSA::MethodsPrivate::constBegin() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QQmlSA.MethodsPrivate.constBegin' has no cute function yet. Qt's "
        "'QMultiHash<QString, Method>::const_iterator "
        "QQmlSA::MethodsPrivate::constBegin() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def constEnd(*__, **_) -> Never:
    """
    Qt's 'QMultiHash<QString, Method>::const_iterator
    QQmlSA::MethodsPrivate::constEnd() const': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'QQmlSA.MethodsPrivate.constEnd' has no cute function yet. Qt's "
        "'QMultiHash<QString, Method>::const_iterator "
        "QQmlSA::MethodsPrivate::constEnd() const': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def createMethods(*__, **_) -> Never:
    """
    Qt's 'QQmlSA::Method::Methods QQmlSA::MethodsPrivate::createMethods(const
    QMultiHash<QString, QQmlJSMetaMethod> &a0)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlSA.MethodsPrivate.createMethods' has no cute function yet. "
        "Qt's 'QQmlSA::Method::Methods "
        "QQmlSA::MethodsPrivate::createMethods(const QMultiHash<QString, "
        "QQmlJSMetaMethod> &a0)': takes a type Python has no way to hand "
        "over yet.")
