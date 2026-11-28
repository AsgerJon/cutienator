"""
QMqttSubscriptionProperties binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMqtt/qmqttsubscriptionproperties.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QMqttUserProperties
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMqttUserProperties = WAIT['QMqttUserProperties']


class QMqttSubscriptionProperties(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMqttSubscriptionProperties: a plain Python object
  standing in front of one C++ QMqttSubscriptionProperties.

  C++ hands a QMqttSubscriptionProperties around as a copy, so every C++
  QMqttSubscriptionProperties behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QMqttSubscriptionProperties that has a ritual and
  that Python can call so far, 6 names in all: 'userProperties',
  'setUserProperties', 'subscriptionIdentifier', 'setSubscriptionIdentifier',
  'noLocal', 'setNoLocal'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMqttSubscriptionProperties
    &QMqttSubscriptionProperties::operator=(const QMqttSubscriptionProperties
    &a0)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QMqttSubscriptionProperties::~QMqttSubscriptionProperties()': the
    destructor: Python removes its C++ QMqttSubscriptionProperties by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QMqttSubscriptionProperties is created at the first use, not by
    'QMqttSubscriptionProperties(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMqttSubscriptionProperties back gives a copy the
    ritual made for Python, in a new cute QMqttSubscriptionProperties.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMqttSubscriptionProperties'

  #  Qt's '~QMqttSubscriptionProperties()'. Naming it makes this a value
  #  class: Python owns every C++ QMqttSubscriptionProperties behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN27QMqttSubscriptionPropertiesD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def userProperties(self) -> QMqttUserProperties:
    """
    Calls Qt's 'QMqttUserProperties
    QMqttSubscriptionProperties::userProperties() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttsubscriptionproperties.html#userProperties

    Returns
    -------

    QMqttUserProperties
      A new cute QMqttUserProperties around the copy Qt gave back. Python
      owns it.
    """
    #  QMqttUserProperties QMqttSubscriptionProperties::userProperties()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK27QMqttSubscriptionProperties14userPropertiesEv',
    )
    from . import QMqttUserProperties
    return QMqttUserProperties._cuteOwning(address)

  def subscriptionIdentifier(self) -> int:
    """
    Calls Qt's 'quint32 QMqttSubscriptionProperties::subscriptionIdentifier()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttsubscriptionproperties.html
    """
    #  quint32 QMqttSubscriptionProperties::subscriptionIdentifier() const
    return self.uglySide.call(
        'ritual_ZNK27QMqttSubscriptionProperties22subscriptionIdentifierEv',
    )

  def noLocal(self) -> bool:
    """
    Calls Qt's 'bool QMqttSubscriptionProperties::noLocal() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttsubscriptionproperties.html#noLocal
    """
    #  bool QMqttSubscriptionProperties::noLocal() const
    return self.uglySide.call(
        'ritual_ZNK27QMqttSubscriptionProperties7noLocalEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QMqttUserProperties)
  def setUserProperties(self, user: QMqttUserProperties) -> None:
    """
    Calls Qt's 'void QMqttSubscriptionProperties::setUserProperties(const
    QMqttUserProperties &user)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttsubscriptionproperties.html#setUserProperties

    Parameters
    ----------

    user : QMqttUserProperties
      Passed on as a value: Qt reads the C++ QMqttUserProperties, which stays
      Python's own.
    """
    #  void QMqttSubscriptionProperties::setUserProperties(const
    #      QMqttUserProperties &user)
    self.uglySide.call(
        'ritual_ZN27QMqttSubscriptionProperties17setUserPropertiesERK19QMqt'
        'tUserProperties',
        self._valueOf(user),
    )

  @overload(int)
  def setSubscriptionIdentifier(self, id: int) -> None:
    """
    Calls Qt's 'void
    QMqttSubscriptionProperties::setSubscriptionIdentifier(quint32 id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttsubscriptionproperties.html

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  void QMqttSubscriptionProperties::setSubscriptionIdentifier(quint32
    #      id)
    self.uglySide.call(
        'ritual_ZN27QMqttSubscriptionProperties25setSubscriptionIdentifierE'
        'j',
        id,
    )

  @overload(bool)
  def setNoLocal(self, noloc: bool) -> None:
    """
    Calls Qt's 'void QMqttSubscriptionProperties::setNoLocal(bool noloc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttsubscriptionproperties.html#setNoLocal

    Parameters
    ----------

    noloc : bool
      Passed on as it is.
    """
    #  void QMqttSubscriptionProperties::setNoLocal(bool noloc)
    self.uglySide.call(
        'ritual_ZN27QMqttSubscriptionProperties10setNoLocalEb', noloc,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QMqttSubscriptionProperties::QMqttSubscriptionProperties()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttsubscriptionproperties.html
    """
    #  QMqttSubscriptionProperties::QMqttSubscriptionProperties()
    self._noteCreation(QMqttSubscriptionProperties, lambda: Rituals.call(
        'ritual_ZN27QMqttSubscriptionPropertiesC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QMqttSubscriptionProperties) -> None:
    """
    Notes what was given, for Qt's
    'QMqttSubscriptionProperties::QMqttSubscriptionProperties(const
    QMqttSubscriptionProperties &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttsubscriptionproperties.html

    Parameters
    ----------

    a0 : QMqttSubscriptionProperties
      Passed on as a value: Qt reads the C++ QMqttSubscriptionProperties,
      which stays Python's own.
    """
    #  QMqttSubscriptionProperties::QMqttSubscriptionProperties(const
    #      QMqttSubscriptionProperties &a0)
    self._noteCreation(QMqttSubscriptionProperties, lambda: Rituals.call(
        'ritual_ZN27QMqttSubscriptionPropertiesC1ERKS_', self._valueOf(a0),
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
