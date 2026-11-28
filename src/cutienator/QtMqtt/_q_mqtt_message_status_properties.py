"""
QMqttMessageStatusProperties binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMqtt/qmqttpublishproperties.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from . import QMqtt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QMqttUserProperties


class QMqttMessageStatusProperties(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMqttMessageStatusProperties: a plain Python object
  standing in front of one C++ QMqttMessageStatusProperties.

  C++ hands a QMqttMessageStatusProperties around as a copy, so every C++
  QMqttMessageStatusProperties behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QMqttMessageStatusProperties that has a ritual and
  that Python can call so far, 3 names in all: 'reasonCode', 'reason',
  'userProperties'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMqttMessageStatusProperties
    &QMqttMessageStatusProperties::operator=(const
    QMqttMessageStatusProperties &a0)': assignment: Python binds a name and
    has no operator for it.
  - Qt's 'QMqttMessageStatusProperties::~QMqttMessageStatusProperties()': the
    destructor: Python removes its C++ QMqttMessageStatusProperties by it,
    and has no other use for it.

  What to expect
  --------------

  - The C++ QMqttMessageStatusProperties is created at the first use, not by
    'QMqttMessageStatusProperties(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMqttMessageStatusProperties back gives a copy the
    ritual made for Python, in a new cute QMqttMessageStatusProperties.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMqttMessageStatusProperties'

  #  Qt's '~QMqttMessageStatusProperties()'. Naming it makes this a value
  #  class: Python owns every C++ QMqttMessageStatusProperties behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN28QMqttMessageStatusPropertiesD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def reasonCode(self) -> QMqtt.ReasonCode:
    """
    Calls Qt's 'QMqtt::ReasonCode QMqttMessageStatusProperties::reasonCode()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttmessagestatusproperties.html#reasonCode

    Returns
    -------

    QMqtt.ReasonCode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QMqtt.ReasonCode(number)'
      gives.
    """
    #  QMqtt::ReasonCode QMqttMessageStatusProperties::reasonCode() const
    return QMqtt.ReasonCode(self.uglySide.call(
        'ritual_ZNK28QMqttMessageStatusProperties10reasonCodeEv',
    ))

  def reason(self) -> str:
    """
    Calls Qt's 'QString QMqttMessageStatusProperties::reason() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttmessagestatusproperties.html#reason

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMqttMessageStatusProperties::reason() const
    return self.uglySide.call(
        'ritual_ZNK28QMqttMessageStatusProperties6reasonEv',
    )

  def userProperties(self) -> QMqttUserProperties:
    """
    Calls Qt's 'QMqttUserProperties
    QMqttMessageStatusProperties::userProperties() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttmessagestatusproperties.html#userProperties

    Returns
    -------

    QMqttUserProperties
      A new cute QMqttUserProperties around the copy Qt gave back. Python
      owns it.
    """
    #  QMqttUserProperties QMqttMessageStatusProperties::userProperties()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK28QMqttMessageStatusProperties14userPropertiesEv',
    )
    from . import QMqttUserProperties
    return QMqttUserProperties._cuteOwning(address)

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QMqttMessageStatusProperties::QMqttMessageStatusProperties()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttmessagestatusproperties.html
    """
    #  QMqttMessageStatusProperties::QMqttMessageStatusProperties()
    self._noteCreation(QMqttMessageStatusProperties, lambda: Rituals.call(
        'ritual_ZN28QMqttMessageStatusPropertiesC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QMqttMessageStatusProperties) -> None:
    """
    Notes what was given, for Qt's
    'QMqttMessageStatusProperties::QMqttMessageStatusProperties(const
    QMqttMessageStatusProperties &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttmessagestatusproperties.html

    Parameters
    ----------

    a0 : QMqttMessageStatusProperties
      Passed on as a value: Qt reads the C++ QMqttMessageStatusProperties,
      which stays Python's own.
    """
    #  QMqttMessageStatusProperties::QMqttMessageStatusProperties(const
    #      QMqttMessageStatusProperties &a0)
    self._noteCreation(QMqttMessageStatusProperties, lambda: Rituals.call(
        'ritual_ZN28QMqttMessageStatusPropertiesC1ERKS_', self._valueOf(a0),
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
