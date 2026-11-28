"""
QQmlSA::PropertyPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmlsa_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQmlSA::PropertyPrivate to be private: it declares the class in a
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

  from . import QQmlJSMetaProperty
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlJSMetaProperty = WAIT['QQmlJSMetaProperty']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class PropertyPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlSA::PropertyPrivate: a plain Python object
  standing in front of one C++ QQmlSA::PropertyPrivate.

  C++ hands a QQmlSA::PropertyPrivate around as a copy, so every C++
  QQmlSA::PropertyPrivate behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlSA::PropertyPrivate that has a ritual and that
  Python can call so far, 7 names in all: 'q_func', 'typeName', 'isValid',
  'isReadonly', 'type', 'property', 'createProperty'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQmlSA::Property *QQmlSA::PropertyPrivate::q_func() const':
    takes in Python what 'QQmlSA::Property
    *QQmlSA::PropertyPrivate::q_func()' takes.
  - Qt's 'QQmlSA::PropertyPrivate::PropertyPrivate(Property *a0,
    PropertyPrivate &&a1)': takes a type Python has no way to hand over yet.
  - Qt's 'QQmlSA::PropertyPrivate::~PropertyPrivate()': the destructor:
    Python removes its C++ QQmlSA::PropertyPrivate by it, and has no other
    use for it.

  What to expect
  --------------

  - The C++ QQmlSA::PropertyPrivate is created at the first use, not by
    'QQmlSA::PropertyPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlSA::PropertyPrivate back gives a copy the ritual
    made for Python, in a new cute QQmlSA::PropertyPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QQmlSA.Property'])
  def property(property: QQmlSA.Property) -> QQmlJSMetaProperty:
    """
    Calls Qt's 'QQmlJSMetaProperty QQmlSA::PropertyPrivate::property(const
    QQmlSA::Property &property)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-propertyprivate.html#property

    Parameters
    ----------

    property : QQmlSA.Property
      Passed on as a value: Qt reads the C++ QQmlSA::Property, which stays
      Python's own.

    Returns
    -------

    QQmlJSMetaProperty
      A new cute QQmlJSMetaProperty around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlJSMetaProperty QQmlSA::PropertyPrivate::property(const
    #      QQmlSA::Property &property)
    address = Rituals.call(
        'ritual_ZN6QQmlSA15PropertyPrivate8propertyERKNS_8PropertyE',
        CuteMixin._valueOf(property),
    )
    from . import QQmlJSMetaProperty
    return QQmlJSMetaProperty._cuteOwning(address)

  @staticmethod
  @overload(QQmlJSMetaProperty)
  def createProperty(a0: QQmlJSMetaProperty) -> QQmlSA.Property:
    """
    Calls Qt's 'QQmlSA::Property
    QQmlSA::PropertyPrivate::createProperty(const QQmlJSMetaProperty &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-propertyprivate.html#createProperty

    Parameters
    ----------

    a0 : QQmlJSMetaProperty
      Passed on as a value: Qt reads the C++ QQmlJSMetaProperty, which stays
      Python's own.

    Returns
    -------

    QQmlSA.Property
      A new cute QQmlSA::Property around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlSA::Property QQmlSA::PropertyPrivate::createProperty(const
    #      QQmlJSMetaProperty &a0)
    address = Rituals.call(
        'ritual_ZN6QQmlSA15PropertyPrivate14createPropertyERK18QQmlJSMetaPr'
        'operty',
        CuteMixin._valueOf(a0),
    )
    return QQmlSA.Property._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlSA::PropertyPrivate'

  #  Qt's '~QQmlSA::PropertyPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QQmlSA::PropertyPrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN6QQmlSA15PropertyPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def typeName(self) -> str:
    """
    Calls Qt's 'QString QQmlSA::PropertyPrivate::typeName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-propertyprivate.html#typeName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlSA::PropertyPrivate::typeName() const
    return self.uglySide.call(
        'ritual_ZNK6QQmlSA15PropertyPrivate8typeNameEv',
    )

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QQmlSA::PropertyPrivate::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-propertyprivate.html#isValid
    """
    #  bool QQmlSA::PropertyPrivate::isValid() const
    return self.uglySide.call('ritual_ZNK6QQmlSA15PropertyPrivate7isValidEv')

  def isReadonly(self) -> bool:
    """
    Calls Qt's 'bool QQmlSA::PropertyPrivate::isReadonly() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-propertyprivate.html#isReadonly
    """
    #  bool QQmlSA::PropertyPrivate::isReadonly() const
    return self.uglySide.call(
        'ritual_ZNK6QQmlSA15PropertyPrivate10isReadonlyEv',
    )

  def type(self) -> QQmlSA.Element:
    """
    Calls Qt's 'QQmlSA::Element QQmlSA::PropertyPrivate::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-propertyprivate.html#type

    Returns
    -------

    QQmlSA.Element
      A new cute QQmlSA::Element around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlSA::Element QQmlSA::PropertyPrivate::type() const
    address = self.uglySide.call('ritual_ZNK6QQmlSA15PropertyPrivate4typeEv')
    return QQmlSA.Element._cuteOwning(address)

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

  @overload(WAIT['QQmlSA.Property'])
  @overload(NoneType)
  def __init__(self, a0: Optional[QQmlSA.Property]) -> None:
    """
    Notes what was given, for Qt's
    'QQmlSA::PropertyPrivate::PropertyPrivate(Property *a0)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-propertyprivate.html#PropertyPrivate

    Parameters
    ----------

    a0 : Optional[QQmlSA.Property]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlSA::PropertyPrivate::PropertyPrivate(Property *a0)
    self._noteCreation(PropertyPrivate, lambda: Rituals.call(
        'ritual_ZN6QQmlSA15PropertyPrivateC1EPNS_8PropertyE',
        self._addressOf(a0),
    ))

  @overload(WAIT['QQmlSA.Property'], THIS)
  @overload(NoneType, THIS)
  def __init__(
      self,
      a0: Optional[QQmlSA.Property],
      a1: PropertyPrivate,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlSA::PropertyPrivate::PropertyPrivate(Property *a0, const
    PropertyPrivate &a1)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-propertyprivate.html#PropertyPrivate

    Parameters
    ----------

    a0 : Optional[QQmlSA.Property]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : PropertyPrivate
      Passed on as a value: Qt reads the C++ QQmlSA::PropertyPrivate, which
      stays Python's own.
    """
    #  QQmlSA::PropertyPrivate::PropertyPrivate(Property *a0, const
    #      PropertyPrivate &a1)
    self._noteCreation(PropertyPrivate, lambda: Rituals.call(
        'ritual_ZN6QQmlSA15PropertyPrivateC1EPNS_8PropertyERKS0_',
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

  def q_func(self) -> Optional[QQmlSA.Property]:
    """
    Calls Qt's 'QQmlSA::Property *QQmlSA::PropertyPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-propertyprivate.html#q_func

    Returns
    -------

    Optional[QQmlSA.Property]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlSA::Property *QQmlSA::PropertyPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN6QQmlSA15PropertyPrivate6q_funcEv',
    )
    return QQmlSA.Property._cuteAt(address)
