"""
QMqttUnsubscriptionProperties binding of the Qt C++
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


class QMqttUnsubscriptionProperties(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMqttUnsubscriptionProperties: a plain Python object
  standing in front of one C++ QMqttUnsubscriptionProperties.

  C++ hands a QMqttUnsubscriptionProperties around as a copy, so every C++
  QMqttUnsubscriptionProperties behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QMqttUnsubscriptionProperties that has a ritual and
  that Python can call so far, 2 names in all: 'userProperties',
  'setUserProperties'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMqttUnsubscriptionProperties
    &QMqttUnsubscriptionProperties::operator=(const
    QMqttUnsubscriptionProperties &rhs)': assignment: Python binds a name and
    has no operator for it.
  - Qt's 'QMqttUnsubscriptionProperties::~QMqttUnsubscriptionProperties()':
    the destructor: Python removes its C++ QMqttUnsubscriptionProperties by
    it, and has no other use for it.

  What to expect
  --------------

  - The C++ QMqttUnsubscriptionProperties is created at the first use, not by
    'QMqttUnsubscriptionProperties(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMqttUnsubscriptionProperties back gives a copy the
    ritual made for Python, in a new cute QMqttUnsubscriptionProperties.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMqttUnsubscriptionProperties'

  #  Qt's '~QMqttUnsubscriptionProperties()'. Naming it makes this a value
  #  class: Python owns every C++ QMqttUnsubscriptionProperties behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN29QMqttUnsubscriptionPropertiesD1Ev'

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
    QMqttUnsubscriptionProperties::userProperties() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttunsubscriptionproperties.html#userProperties

    Returns
    -------

    QMqttUserProperties
      A new cute QMqttUserProperties around the copy Qt gave back. Python
      owns it.
    """
    #  QMqttUserProperties QMqttUnsubscriptionProperties::userProperties()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK29QMqttUnsubscriptionProperties14userPropertiesEv',
    )
    from . import QMqttUserProperties
    return QMqttUserProperties._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QMqttUserProperties)
  def setUserProperties(self, user: QMqttUserProperties) -> None:
    """
    Calls Qt's 'void QMqttUnsubscriptionProperties::setUserProperties(const
    QMqttUserProperties &user)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttunsubscriptionproperties.html

    Parameters
    ----------

    user : QMqttUserProperties
      Passed on as a value: Qt reads the C++ QMqttUserProperties, which stays
      Python's own.
    """
    #  void QMqttUnsubscriptionProperties::setUserProperties(const
    #      QMqttUserProperties &user)
    self.uglySide.call(
        'ritual_ZN29QMqttUnsubscriptionProperties17setUserPropertiesERK19QM'
        'qttUserProperties',
        self._valueOf(user),
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
    'QMqttUnsubscriptionProperties::QMqttUnsubscriptionProperties()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttunsubscriptionproperties.html
    """
    #  QMqttUnsubscriptionProperties::QMqttUnsubscriptionProperties()
    self._noteCreation(QMqttUnsubscriptionProperties, lambda: Rituals.call(
        'ritual_ZN29QMqttUnsubscriptionPropertiesC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QMqttUnsubscriptionProperties) -> None:
    """
    Notes what was given, for Qt's
    'QMqttUnsubscriptionProperties::QMqttUnsubscriptionProperties(const
    QMqttUnsubscriptionProperties &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttunsubscriptionproperties.html

    Parameters
    ----------

    a0 : QMqttUnsubscriptionProperties
      Passed on as a value: Qt reads the C++ QMqttUnsubscriptionProperties,
      which stays Python's own.
    """
    #  QMqttUnsubscriptionProperties::QMqttUnsubscriptionProperties(const
    #      QMqttUnsubscriptionProperties &a0)
    self._noteCreation(QMqttUnsubscriptionProperties, lambda: Rituals.call(
        'ritual_ZN29QMqttUnsubscriptionPropertiesC1ERKS_', self._valueOf(a0),
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
