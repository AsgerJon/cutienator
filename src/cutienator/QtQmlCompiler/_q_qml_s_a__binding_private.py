"""
QQmlSA::BindingPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmlsa_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQmlSA::BindingPrivate to be private: it declares the class in a
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
  from typing import Never, Optional

  from . import QQmlJSMetaPropertyBinding
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlJSMetaPropertyBinding = WAIT['QQmlJSMetaPropertyBinding']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class BindingPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlSA::BindingPrivate: a plain Python object
  standing in front of one C++ QQmlSA::BindingPrivate.

  C++ hands a QQmlSA::BindingPrivate around as a copy, so every C++
  QQmlSA::BindingPrivate behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlSA::BindingPrivate that has a ritual and that
  Python can call so far, 8 names in all: 'q_func', 'get', 'createBinding',
  'setPropertyName', 'bindingScope', 'setBindingScope', 'isAttached',
  'setIsAttached'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const Binding *QQmlSA::BindingPrivate::q_func() const': takes in
    Python what 'Binding *QQmlSA::BindingPrivate::q_func()' takes.
  - Qt's 'const BindingPrivate *QQmlSA::BindingPrivate::get(const Binding
    *binding)': takes in Python what 'BindingPrivate
    *QQmlSA::BindingPrivate::get(Binding *binding)' takes.
  - Qt's 'QQmlSA::BindingPrivate::~BindingPrivate()': the destructor: Python
    removes its C++ QQmlSA::BindingPrivate by it, and has no other use for
    it.

  What has no ritual
  ------------------

  2 of the 15 functions Qt declares: 2 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QQmlSA::BindingPrivate is created at the first use, not by
    'QQmlSA::BindingPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlSA::BindingPrivate back gives a copy the ritual
    made for Python, in a new cute QQmlSA::BindingPrivate.
  - Each name of Qt's QQmlSA::BindingPrivate that has no cute function yet,
    'binding', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QQmlSA.Binding'])
  @overload(NoneType)
  def get(binding: Optional[QQmlSA.Binding]) -> Optional[BindingPrivate]:
    """
    Calls Qt's 'BindingPrivate *QQmlSA::BindingPrivate::get(Binding
    *binding)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-bindingprivate.html#get

    Parameters
    ----------

    binding : Optional[QQmlSA.Binding]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[BindingPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  BindingPrivate *QQmlSA::BindingPrivate::get(Binding *binding)
    address = Rituals.call(
        'ritual_ZN6QQmlSA14BindingPrivate3getEPNS_7BindingE',
        CuteMixin._addressOf(binding),
    )
    return BindingPrivate._cuteAt(address)

  @staticmethod
  @overload(QQmlJSMetaPropertyBinding)
  def createBinding(a0: QQmlJSMetaPropertyBinding) -> QQmlSA.Binding:
    """
    Calls Qt's 'QQmlSA::Binding QQmlSA::BindingPrivate::createBinding(const
    QQmlJSMetaPropertyBinding &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-bindingprivate.html#createBinding

    Parameters
    ----------

    a0 : QQmlJSMetaPropertyBinding
      Passed on as a value: Qt reads the C++ QQmlJSMetaPropertyBinding, which
      stays Python's own.

    Returns
    -------

    QQmlSA.Binding
      A new cute QQmlSA::Binding around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlSA::Binding QQmlSA::BindingPrivate::createBinding(const
    #      QQmlJSMetaPropertyBinding &a0)
    address = Rituals.call(
        'ritual_ZN6QQmlSA14BindingPrivate13createBindingERK25QQmlJSMetaProp'
        'ertyBinding',
        CuteMixin._valueOf(a0),
    )
    return QQmlSA.Binding._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlSA::BindingPrivate'

  #  Qt's '~QQmlSA::BindingPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QQmlSA::BindingPrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN6QQmlSA14BindingPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def bindingScope(self) -> QQmlSA.Element:
    """
    Calls Qt's 'Element QQmlSA::BindingPrivate::bindingScope() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-bindingprivate.html#bindingScope

    Returns
    -------

    QQmlSA.Element
      A new cute QQmlSA::Element around the copy Qt gave back. Python owns
      it.
    """
    #  Element QQmlSA::BindingPrivate::bindingScope() const
    address = self.uglySide.call(
        'ritual_ZNK6QQmlSA14BindingPrivate12bindingScopeEv',
    )
    return QQmlSA.Element._cuteOwning(address)

  def isAttached(self) -> bool:
    """
    Calls Qt's 'bool QQmlSA::BindingPrivate::isAttached() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-bindingprivate.html#isAttached
    """
    #  bool QQmlSA::BindingPrivate::isAttached() const
    return self.uglySide.call(
        'ritual_ZNK6QQmlSA14BindingPrivate10isAttachedEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setPropertyName(self, name: str) -> None:
    """
    Calls Qt's 'void QQmlSA::BindingPrivate::setPropertyName(QString name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-bindingprivate.html#setPropertyName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlSA::BindingPrivate::setPropertyName(QString name)
    self.uglySide.call(
        'ritual_ZN6QQmlSA14BindingPrivate15setPropertyNameE7QString', name,
    )

  @overload(WAIT['QQmlSA.Element'])
  def setBindingScope(self, bindingScope: QQmlSA.Element) -> None:
    """
    Calls Qt's 'void QQmlSA::BindingPrivate::setBindingScope(Element
    bindingScope)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-bindingprivate.html#setBindingScope

    Parameters
    ----------

    bindingScope : QQmlSA.Element
      Passed on as a value: Qt reads the C++ QQmlSA::Element, which stays
      Python's own.
    """
    #  void QQmlSA::BindingPrivate::setBindingScope(Element bindingScope)
    self.uglySide.call(
        'ritual_ZN6QQmlSA14BindingPrivate15setBindingScopeENS_7ElementE',
        self._valueOf(bindingScope),
    )

  @overload(bool)
  def setIsAttached(self, isAttached: bool) -> None:
    """
    Calls Qt's 'void QQmlSA::BindingPrivate::setIsAttached(bool isAttached)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-bindingprivate.html#setIsAttached

    Parameters
    ----------

    isAttached : bool
      Passed on as it is.
    """
    #  void QQmlSA::BindingPrivate::setIsAttached(bool isAttached)
    self.uglySide.call(
        'ritual_ZN6QQmlSA14BindingPrivate13setIsAttachedEb', isAttached,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['QQmlSA.Binding'])
  @overload(NoneType)
  def __init__(self, a0: Optional[QQmlSA.Binding]) -> None:
    """
    Notes what was given, for Qt's
    'QQmlSA::BindingPrivate::BindingPrivate(Binding *a0)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-bindingprivate.html#BindingPrivate

    Parameters
    ----------

    a0 : Optional[QQmlSA.Binding]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlSA::BindingPrivate::BindingPrivate(Binding *a0)
    self._noteCreation(BindingPrivate, lambda: Rituals.call(
        'ritual_ZN6QQmlSA14BindingPrivateC1EPNS_7BindingE',
        self._addressOf(a0),
    ))

  @overload(WAIT['QQmlSA.Binding'], THIS)
  @overload(NoneType, THIS)
  def __init__(
      self,
      a0: Optional[QQmlSA.Binding],
      a1: BindingPrivate,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlSA::BindingPrivate::BindingPrivate(Binding *a0, const BindingPrivate
    &a1)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-bindingprivate.html#BindingPrivate

    Parameters
    ----------

    a0 : Optional[QQmlSA.Binding]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : BindingPrivate
      Passed on as a value: Qt reads the C++ QQmlSA::BindingPrivate, which
      stays Python's own.
    """
    #  QQmlSA::BindingPrivate::BindingPrivate(Binding *a0, const
    #      BindingPrivate &a1)
    self._noteCreation(BindingPrivate, lambda: Rituals.call(
        'ritual_ZN6QQmlSA14BindingPrivateC1EPNS_7BindingERKS0_',
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

  def q_func(self) -> Optional[QQmlSA.Binding]:
    """
    Calls Qt's 'Binding *QQmlSA::BindingPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-bindingprivate.html#q_func

    Returns
    -------

    Optional[QQmlSA.Binding]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Binding *QQmlSA::BindingPrivate::q_func()
    address = self.uglySide.call('ritual_ZN6QQmlSA14BindingPrivate6q_funcEv')
    return QQmlSA.Binding._cuteAt(address)

  @staticmethod
  def binding(*__, **_) -> Never:
    """
    - Qt's 'QQmlJSMetaPropertyBinding
      QQmlSA::BindingPrivate::binding(QQmlSA::Binding &binding)': cannot be
      called and cannot be called through the meta-object and cannot be
      copied: no header file has its code, Qt's source does not mark it or
      its class for use from outside Qt or writes it 'inline' or nowhere, and
      it is no signal, slot or invokable function giving back nothing, of a
      class built on QObject, and Qt's source has no code for it that could
      be told from the rest.
    - Qt's 'const QQmlJSMetaPropertyBinding
      QQmlSA::BindingPrivate::binding(const QQmlSA::Binding &binding)':
      cannot be called and cannot be called through the meta-object and
      cannot be copied: no header file has its code, Qt's source does not
      mark it or its class for use from outside Qt or writes it 'inline' or
      nowhere, and it is no signal, slot or invokable function giving back
      nothing, of a class built on QObject, and Qt's source has no code for
      it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QQmlSA.BindingPrivate.binding' has no cute function yet. Qt's "
        "'QQmlJSMetaPropertyBinding "
        "QQmlSA::BindingPrivate::binding(QQmlSA::Binding &binding)': cannot "
        "be called and cannot be called through the meta-object and cannot "
        "be copied: no header file has its code, Qt's source does not mark "
        "it or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest. Qt's 'const "
        "QQmlJSMetaPropertyBinding QQmlSA::BindingPrivate::binding(const "
        "QQmlSA::Binding &binding)': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest.")
