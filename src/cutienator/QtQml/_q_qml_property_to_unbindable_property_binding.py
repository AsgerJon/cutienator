"""
QQmlPropertyToUnbindablePropertyBinding binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlpropertytopropertybinding_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlPropertyToUnbindablePropertyBinding to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QQmlAbstractBinding, QQmlPropertyData

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QMetaProperty, QObject
  from . import QQmlEngine, QQmlProperty
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaObject = WAIT['QMetaObject']
  QMetaProperty = WAIT['QMetaProperty']
  QQmlEngine = WAIT['QQmlEngine']
  QQmlProperty = WAIT['QQmlProperty']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlPropertyToUnbindablePropertyBinding(QQmlAbstractBinding):
  """
  The cute side of Qt's QQmlPropertyToUnbindablePropertyBinding: a plain
  Python object standing in front of one C++
  QQmlPropertyToUnbindablePropertyBinding.

  It is built on the cute 'QQmlAbstractBinding', as Qt's
  QQmlPropertyToUnbindablePropertyBinding is built on Qt's
  QQmlAbstractBinding, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlPropertyToUnbindablePropertyBinding that has a
  ritual and that Python can call so far, 5 names in all: 'kind',
  'setEnabled', 'update', 'source', 'captureProperty'. It can be made from
  Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QQmlPropertyToUnbindablePropertyBinding is created at the first
    use, not by 'QQmlPropertyToUnbindablePropertyBinding(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlPropertyToUnbindablePropertyBinding.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlPropertyToUnbindablePropertyBinding'

  #  A C++ QQmlPropertyToUnbindablePropertyBinding Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlPropertyToUnbindablePropertyBinding'

  #  The functions Qt calls itself that
  #  QQmlPropertyToUnbindablePropertyBinding is the first to declare. A class
  #  of a program built on it can write one anew, and Qt then calls that. For
  #  each name: the key C++ knows the function by, what it gives, and what it
  #  takes.
  __virtual_functions__ = {
      'captureProperty': (
          ('_ZN39QQmlPropertyToUnbindablePropertyBinding15capturePropertyEP'
           'K11QMetaObjectRK13QMetaProperty',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QMetaObject'),
               ('address', 'value', 'QtCore:QMetaProperty'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def kind(self) -> QQmlAbstractBinding.Kind:
    """
    Calls Qt's 'Kind QQmlPropertyToUnbindablePropertyBinding::kind() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertytounbindablepropertybinding.html#kind

    Returns
    -------

    QQmlAbstractBinding.Kind
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQmlAbstractBinding.Kind(number)' gives.
    """
    #  Kind QQmlPropertyToUnbindablePropertyBinding::kind() const
    return QQmlAbstractBinding.Kind(self._callAs(
        'QQmlPropertyToUnbindablePropertyBinding',
        'ritual_ZNK39QQmlPropertyToUnbindablePropertyBinding4kindEv',
    ))

  def source(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlPropertyToUnbindablePropertyBinding::source()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertytounbindablepropertybinding.html

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlPropertyToUnbindablePropertyBinding::source() const
    address = self._callAs(
        'QQmlPropertyToUnbindablePropertyBinding',
        'ritual_ZNK39QQmlPropertyToUnbindablePropertyBinding6sourceEv',
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool, QQmlPropertyData.WriteFlags)
  def setEnabled(self, e: bool, flags: QQmlPropertyData.WriteFlags) -> None:
    """
    Calls Qt's 'void QQmlPropertyToUnbindablePropertyBinding::setEnabled(bool
    e, QQmlPropertyData::WriteFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertytounbindablepropertybinding.html

    Parameters
    ----------

    e : bool
      Passed on as it is.

    flags : QQmlPropertyData.WriteFlags
      Passed on as its number.
    """
    #  void QQmlPropertyToUnbindablePropertyBinding::setEnabled(bool e,
    #      QQmlPropertyData::WriteFlags flags)
    self._callAs(
        'QQmlPropertyToUnbindablePropertyBinding',
        'ritual_ZN39QQmlPropertyToUnbindablePropertyBinding10setEnabledEb6Q'
        'FlagsIN16QQmlPropertyData9WriteFlagEE',
        e, flags.value,
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

  @overload(QQmlEngine, QQmlProperty, QQmlProperty)
  @overload(NoneType, QQmlProperty, QQmlProperty)
  def __init__(
      self,
      engine: Optional[QQmlEngine],
      source: QQmlProperty,
      target: QQmlProperty,
  ) -> None:
    """
    Notes what was given, for Qt's 'QQmlPropertyToUnbindablePropertyBinding::
    QQmlPropertyToUnbindablePropertyBinding(QQmlEngine *engine, const
    QQmlProperty &source, const QQmlProperty &target)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertytounbindablepropertybinding.html

    Parameters
    ----------

    engine : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    source : QQmlProperty
      Passed on as a value: Qt reads the C++ QQmlProperty, which stays
      Python's own.

    target : QQmlProperty
      Passed on as a value: Qt reads the C++ QQmlProperty, which stays
      Python's own.
    """
    #  QQmlPropertyToUnbindablePropertyBinding::
    #      QQmlPropertyToUnbindablePropertyBinding(QQmlEngine *engine, const
    #      QQmlProperty &source, const QQmlProperty &target)
    self._noteCreation(
        QQmlPropertyToUnbindablePropertyBinding, lambda: Rituals.call(
            'ritual_ZN39QQmlPropertyToUnbindablePropertyBindingC1EP10QQmlEn'
            'gineRK12QQmlPropertyS4_',
            self._addressOf(engine), self._valueOf(source),
            self._valueOf(target),
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

  @overload()
  @overload(QQmlPropertyData.WriteFlags)
  def update(
      self,
      flags: QQmlPropertyData.WriteFlags = (
          QQmlPropertyData.WriteFlags.DontRemoveBinding),
  ) -> None:
    """
    Calls Qt's 'void
    QQmlPropertyToUnbindablePropertyBinding::update(QQmlPropertyData::
    WriteFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertytounbindablepropertybinding.html

    Parameters
    ----------

    flags : QQmlPropertyData.WriteFlags
      Passed on as its number. May be left out, as in Qt: it is then
      QQmlPropertyData.WriteFlags.DontRemoveBinding.
    """
    #  void QQmlPropertyToUnbindablePropertyBinding::update(
    #      QQmlPropertyData::WriteFlags flags)
    self._callAs(
        'QQmlPropertyToUnbindablePropertyBinding',
        'ritual_ZN39QQmlPropertyToUnbindablePropertyBinding6updateE6QFlagsI'
        'N16QQmlPropertyData9WriteFlagEE',
        flags.value,
    )

  @overload(QMetaObject, QMetaProperty)
  @overload(NoneType, QMetaProperty)
  def captureProperty(
      self,
      sourceMetaObject: Optional[QMetaObject],
      sourceProperty: QMetaProperty,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlPropertyToUnbindablePropertyBinding::captureProperty(const
    QMetaObject *sourceMetaObject, const QMetaProperty &sourceProperty)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertytounbindablepropertybinding.html

    Parameters
    ----------

    sourceMetaObject : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    sourceProperty : QMetaProperty
      Passed on as a value: Qt reads the C++ QMetaProperty, which stays
      Python's own.
    """
    #  void QQmlPropertyToUnbindablePropertyBinding::captureProperty(const
    #      QMetaObject *sourceMetaObject, const QMetaProperty
    #      &sourceProperty)
    self._callAs(
        'QQmlPropertyToUnbindablePropertyBinding',
        'ritual_ZN39QQmlPropertyToUnbindablePropertyBinding15capturePropert'
        'yEPK11QMetaObjectRK13QMetaProperty',
        self._addressOf(sourceMetaObject, 'QMetaObject'),
        self._valueOf(sourceProperty),
    )
