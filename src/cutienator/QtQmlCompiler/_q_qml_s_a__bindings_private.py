"""
QQmlSA::BindingsPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmlsa_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQmlSA::BindingsPrivate to be private: it declares the class in a
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


class BindingsPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlSA::BindingsPrivate: a plain Python object
  standing in front of one C++ QQmlSA::BindingsPrivate.

  C++ hands a QQmlSA::BindingsPrivate around as a copy, so every C++
  QQmlSA::BindingsPrivate behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlSA::BindingsPrivate that has a ritual and that
  Python can call so far, 1 name in all: 'q_func'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQmlSA::Binding::Bindings *QQmlSA::BindingsPrivate::q_func()
    const': takes in Python what 'QQmlSA::Binding::Bindings
    *QQmlSA::BindingsPrivate::q_func()' takes.
  - Qt's 'QQmlSA::BindingsPrivate::BindingsPrivate(QQmlSA::Binding::Bindings
    *a0, BindingsPrivate &&a1)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QQmlSA::BindingsPrivate::~BindingsPrivate()': the destructor:
    Python removes its C++ QQmlSA::BindingsPrivate by it, and has no other
    use for it.
  - Qt's 'QMultiHash<QString, Binding>::const_iterator
    QQmlSA::BindingsPrivate::constBegin() const': gives a type Python has no
    way to take yet.
  - Qt's 'QMultiHash<QString, Binding>::const_iterator
    QQmlSA::BindingsPrivate::constEnd() const': gives a type Python has no
    way to take yet.
  - Qt's 'QQmlSA::Binding::Bindings
    QQmlSA::BindingsPrivate::createBindings(const QMultiHash<QString,
    QQmlJSMetaPropertyBinding> &a0)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QQmlSA::Binding::Bindings
    QQmlSA::BindingsPrivate::createBindings(std::pair<QMultiHash<QString,
    QQmlJSMetaPropertyBinding>::const_iterator, QMultiHash<QString,
    QQmlJSMetaPropertyBinding>::const_iterator> a0)': takes a type Python has
    no way to hand over yet.

  What to expect
  --------------

  - The C++ QQmlSA::BindingsPrivate is created at the first use, not by
    'QQmlSA::BindingsPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlSA::BindingsPrivate back gives a copy the ritual
    made for Python, in a new cute QQmlSA::BindingsPrivate.
  - Each name of Qt's QQmlSA::BindingsPrivate that has no cute function yet,
    'constBegin', 'constEnd', 'createBindings', holds a function that raises
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
  __qt_class__ = 'QQmlSA::BindingsPrivate'

  #  Qt's '~QQmlSA::BindingsPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QQmlSA::BindingsPrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN6QQmlSA15BindingsPrivateD1Ev'

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

  @overload(QQmlSA.Binding.Bindings)
  @overload(NoneType)
  def __init__(self, a0: Optional[QQmlSA.Binding.Bindings]) -> None:
    """
    Notes what was given, for Qt's
    'QQmlSA::BindingsPrivate::BindingsPrivate(QQmlSA::Binding::Bindings
    *a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-bindingsprivate.html#BindingsPrivate

    Parameters
    ----------

    a0 : Optional[QQmlSA.Binding.Bindings]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlSA::BindingsPrivate::BindingsPrivate(QQmlSA::Binding::Bindings
    #      *a0)
    self._noteCreation(BindingsPrivate, lambda: Rituals.call(
        'ritual_ZN6QQmlSA15BindingsPrivateC1EPNS_7Binding8BindingsE',
        self._addressOf(a0),
    ))

  @overload(QQmlSA.Binding.Bindings, THIS)
  @overload(NoneType, THIS)
  def __init__(
      self,
      a0: Optional[QQmlSA.Binding.Bindings],
      a1: BindingsPrivate,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlSA::BindingsPrivate::BindingsPrivate(QQmlSA::Binding::Bindings *a0,
    const BindingsPrivate &a1)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-bindingsprivate.html#BindingsPrivate

    Parameters
    ----------

    a0 : Optional[QQmlSA.Binding.Bindings]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : BindingsPrivate
      Passed on as a value: Qt reads the C++ QQmlSA::BindingsPrivate, which
      stays Python's own.
    """
    #  QQmlSA::BindingsPrivate::BindingsPrivate(QQmlSA::Binding::Bindings
    #      *a0, const BindingsPrivate &a1)
    self._noteCreation(BindingsPrivate, lambda: Rituals.call(
        'ritual_ZN6QQmlSA15BindingsPrivateC1EPNS_7Binding8BindingsERKS0_',
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

  def q_func(self) -> Optional[QQmlSA.Binding.Bindings]:
    """
    Calls Qt's 'QQmlSA::Binding::Bindings
    *QQmlSA::BindingsPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-bindingsprivate.html#q_func

    Returns
    -------

    Optional[QQmlSA.Binding.Bindings]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlSA::Binding::Bindings *QQmlSA::BindingsPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN6QQmlSA15BindingsPrivate6q_funcEv',
    )
    return QQmlSA.Binding.Bindings._cuteAt(address)

  @staticmethod
  def constBegin(*__, **_) -> Never:
    """
    Qt's 'QMultiHash<QString, Binding>::const_iterator
    QQmlSA::BindingsPrivate::constBegin() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QQmlSA.BindingsPrivate.constBegin' has no cute function yet. Qt's "
        "'QMultiHash<QString, Binding>::const_iterator "
        "QQmlSA::BindingsPrivate::constBegin() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def constEnd(*__, **_) -> Never:
    """
    Qt's 'QMultiHash<QString, Binding>::const_iterator
    QQmlSA::BindingsPrivate::constEnd() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QQmlSA.BindingsPrivate.constEnd' has no cute function yet. Qt's "
        "'QMultiHash<QString, Binding>::const_iterator "
        "QQmlSA::BindingsPrivate::constEnd() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def createBindings(*__, **_) -> Never:
    """
    - Qt's 'QQmlSA::Binding::Bindings
      QQmlSA::BindingsPrivate::createBindings(const QMultiHash<QString,
      QQmlJSMetaPropertyBinding> &a0)': takes a type Python has no way to
      hand over yet.
    - Qt's 'QQmlSA::Binding::Bindings
      QQmlSA::BindingsPrivate::createBindings(std::pair<QMultiHash<QString,
      QQmlJSMetaPropertyBinding>::const_iterator, QMultiHash<QString,
      QQmlJSMetaPropertyBinding>::const_iterator> a0)': takes a type Python
      has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlSA.BindingsPrivate.createBindings' has no cute function yet. "
        "Qt's 'QQmlSA::Binding::Bindings "
        "QQmlSA::BindingsPrivate::createBindings(const QMultiHash<QString, "
        "QQmlJSMetaPropertyBinding> &a0)': takes a type Python has no way "
        "to hand over yet. Qt's 'QQmlSA::Binding::Bindings "
        "QQmlSA::BindingsPrivate::createBindings(std::pair<QMultiHash<QStrin"
        "g, QQmlJSMetaPropertyBinding>::const_iterator, QMultiHash<QString, "
        "QQmlJSMetaPropertyBinding>::const_iterator> a0)': takes a type "
        "Python has no way to hand over yet.")
