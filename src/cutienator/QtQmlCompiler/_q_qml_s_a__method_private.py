"""
QQmlSA::MethodPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmlsa_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQmlSA::MethodPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QQmlSA

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQmlJSMetaMethod
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlJSMetaMethod = WAIT['QQmlJSMetaMethod']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class MethodPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlSA::MethodPrivate: a plain Python object standing
  in front of one C++ QQmlSA::MethodPrivate.

  C++ hands a QQmlSA::MethodPrivate around as a copy, so every C++
  QQmlSA::MethodPrivate behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlSA::MethodPrivate that has a ritual and that
  Python can call so far, 6 names in all: 'q_func', 'methodName',
  'sourceLocation', 'methodType', 'createMethod', 'method'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const Method *QQmlSA::MethodPrivate::q_func() const': takes in
    Python what 'Method *QQmlSA::MethodPrivate::q_func()' takes.
  - Qt's 'QQmlSA::MethodPrivate::~MethodPrivate()': the destructor: Python
    removes its C++ QQmlSA::MethodPrivate by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQmlSA::MethodPrivate is created at the first use, not by
    'QQmlSA::MethodPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlSA::MethodPrivate back gives a copy the ritual
    made for Python, in a new cute QQmlSA::MethodPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQmlJSMetaMethod)
  def createMethod(a0: QQmlJSMetaMethod) -> QQmlSA.Method:
    """
    Calls Qt's 'QQmlSA::Method QQmlSA::MethodPrivate::createMethod(const
    QQmlJSMetaMethod &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-methodprivate.html#createMethod

    Parameters
    ----------

    a0 : QQmlJSMetaMethod
      Passed on as a value: Qt reads the C++ QQmlJSMetaMethod, which stays
      Python's own.

    Returns
    -------

    QQmlSA.Method
      A new cute QQmlSA::Method around the copy Qt gave back. Python owns it.
    """
    #  QQmlSA::Method QQmlSA::MethodPrivate::createMethod(const
    #      QQmlJSMetaMethod &a0)
    address = Rituals.call(
        'ritual_ZN6QQmlSA13MethodPrivate12createMethodERK16QQmlJSMetaMethod',
        CuteMixin._valueOf(a0),
    )
    return QQmlSA.Method._cuteOwning(address)

  @staticmethod
  @overload(WAIT['QQmlSA.Method'])
  def method(a0: QQmlSA.Method) -> QQmlJSMetaMethod:
    """
    Calls Qt's 'QQmlJSMetaMethod QQmlSA::MethodPrivate::method(const
    QQmlSA::Method &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-methodprivate.html#method

    Parameters
    ----------

    a0 : QQmlSA.Method
      Passed on as a value: Qt reads the C++ QQmlSA::Method, which stays
      Python's own.

    Returns
    -------

    QQmlJSMetaMethod
      A new cute QQmlJSMetaMethod around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlJSMetaMethod QQmlSA::MethodPrivate::method(const QQmlSA::Method
    #      &a0)
    address = Rituals.call(
        'ritual_ZN6QQmlSA13MethodPrivate6methodERKNS_6MethodE',
        CuteMixin._valueOf(a0),
    )
    from . import QQmlJSMetaMethod
    return QQmlJSMetaMethod._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlSA::MethodPrivate'

  #  Qt's '~QQmlSA::MethodPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QQmlSA::MethodPrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN6QQmlSA13MethodPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def methodName(self) -> str:
    """
    Calls Qt's 'QString QQmlSA::MethodPrivate::methodName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-methodprivate.html#methodName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlSA::MethodPrivate::methodName() const
    return self.uglySide.call(
        'ritual_ZNK6QQmlSA13MethodPrivate10methodNameEv',
    )

  def sourceLocation(self) -> QQmlSA.SourceLocation:
    """
    Calls Qt's 'QQmlSA::SourceLocation
    QQmlSA::MethodPrivate::sourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-methodprivate.html#sourceLocation

    Returns
    -------

    QQmlSA.SourceLocation
      A new cute QQmlSA::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlSA::SourceLocation QQmlSA::MethodPrivate::sourceLocation() const
    address = self.uglySide.call(
        'ritual_ZNK6QQmlSA13MethodPrivate14sourceLocationEv',
    )
    return QQmlSA.SourceLocation._cuteOwning(address)

  def methodType(self) -> QQmlSA.MethodType:
    """
    Calls Qt's 'MethodType QQmlSA::MethodPrivate::methodType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-methodprivate.html#methodType

    Returns
    -------

    QQmlSA.MethodType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQmlSA.MethodType(number)' gives.
    """
    #  MethodType QQmlSA::MethodPrivate::methodType() const
    return QQmlSA.MethodType(self.uglySide.call(
        'ritual_ZNK6QQmlSA13MethodPrivate10methodTypeEv',
    ))

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

  @overload(WAIT['QQmlSA.Method'])
  @overload(NoneType)
  def __init__(self, a0: Optional[QQmlSA.Method]) -> None:
    """
    Notes what was given, for Qt's
    'QQmlSA::MethodPrivate::MethodPrivate(Method *a0)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-methodprivate.html#MethodPrivate

    Parameters
    ----------

    a0 : Optional[QQmlSA.Method]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlSA::MethodPrivate::MethodPrivate(Method *a0)
    self._noteCreation(MethodPrivate, lambda: Rituals.call(
        'ritual_ZN6QQmlSA13MethodPrivateC1EPNS_6MethodE',
        self._addressOf(a0),
    ))

  @overload(WAIT['QQmlSA.Method'], THIS)
  @overload(NoneType, THIS)
  def __init__(self, a0: Optional[QQmlSA.Method], a1: MethodPrivate) -> None:
    """
    Notes what was given, for Qt's
    'QQmlSA::MethodPrivate::MethodPrivate(Method *a0, const MethodPrivate
    &a1)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-methodprivate.html#MethodPrivate

    Parameters
    ----------

    a0 : Optional[QQmlSA.Method]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : MethodPrivate
      Passed on as a value: Qt reads the C++ QQmlSA::MethodPrivate, which
      stays Python's own.
    """
    #  QQmlSA::MethodPrivate::MethodPrivate(Method *a0, const MethodPrivate
    #      &a1)
    self._noteCreation(MethodPrivate, lambda: Rituals.call(
        'ritual_ZN6QQmlSA13MethodPrivateC1EPNS_6MethodERKS0_',
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

  def q_func(self) -> Optional[QQmlSA.Method]:
    """
    Calls Qt's 'Method *QQmlSA::MethodPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-methodprivate.html#q_func

    Returns
    -------

    Optional[QQmlSA.Method]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Method *QQmlSA::MethodPrivate::q_func()
    address = self.uglySide.call('ritual_ZN6QQmlSA13MethodPrivate6q_funcEv')
    return QQmlSA.Method._cuteAt(address)
