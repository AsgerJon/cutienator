"""
QMqttAuthenticationProperties binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMqtt/qmqttauthenticationproperties.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QByteArray
  from . import QMqttUserProperties
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QMqttUserProperties = WAIT['QMqttUserProperties']


class QMqttAuthenticationProperties(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMqttAuthenticationProperties: a plain Python object
  standing in front of one C++ QMqttAuthenticationProperties.

  C++ hands a QMqttAuthenticationProperties around as a copy, so every C++
  QMqttAuthenticationProperties behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QMqttAuthenticationProperties that has a ritual and
  that Python can call so far, 8 names in all: 'authenticationMethod',
  'setAuthenticationMethod', 'authenticationData', 'setAuthenticationData',
  'reason', 'setReason', 'userProperties', 'setUserProperties'. It can be
  made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMqttAuthenticationProperties
    &QMqttAuthenticationProperties::operator=(const
    QMqttAuthenticationProperties &a0)': assignment: Python binds a name and
    has no operator for it.
  - Qt's 'QMqttAuthenticationProperties::~QMqttAuthenticationProperties()':
    the destructor: Python removes its C++ QMqttAuthenticationProperties by
    it, and has no other use for it.

  What to expect
  --------------

  - The C++ QMqttAuthenticationProperties is created at the first use, not by
    'QMqttAuthenticationProperties(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMqttAuthenticationProperties back gives a copy the
    ritual made for Python, in a new cute QMqttAuthenticationProperties.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMqttAuthenticationProperties'

  #  Qt's '~QMqttAuthenticationProperties()'. Naming it makes this a value
  #  class: Python owns every C++ QMqttAuthenticationProperties behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN29QMqttAuthenticationPropertiesD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def authenticationMethod(self) -> str:
    """
    Calls Qt's 'QString QMqttAuthenticationProperties::authenticationMethod()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttauthenticationproperties.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMqttAuthenticationProperties::authenticationMethod() const
    return self.uglySide.call(
        'ritual_ZNK29QMqttAuthenticationProperties20authenticationMethodEv',
    )

  def authenticationData(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray
    QMqttAuthenticationProperties::authenticationData() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttauthenticationproperties.html

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QMqttAuthenticationProperties::authenticationData() const
    address = self.uglySide.call(
        'ritual_ZNK29QMqttAuthenticationProperties18authenticationDataEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def reason(self) -> str:
    """
    Calls Qt's 'QString QMqttAuthenticationProperties::reason() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttauthenticationproperties.html#reason

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMqttAuthenticationProperties::reason() const
    return self.uglySide.call(
        'ritual_ZNK29QMqttAuthenticationProperties6reasonEv',
    )

  def userProperties(self) -> QMqttUserProperties:
    """
    Calls Qt's 'QMqttUserProperties
    QMqttAuthenticationProperties::userProperties() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttauthenticationproperties.html#userProperties

    Returns
    -------

    QMqttUserProperties
      A new cute QMqttUserProperties around the copy Qt gave back. Python
      owns it.
    """
    #  QMqttUserProperties QMqttAuthenticationProperties::userProperties()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK29QMqttAuthenticationProperties14userPropertiesEv',
    )
    from . import QMqttUserProperties
    return QMqttUserProperties._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setAuthenticationMethod(self, method: str) -> None:
    """
    Calls Qt's 'void
    QMqttAuthenticationProperties::setAuthenticationMethod(const QString
    &method)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttauthenticationproperties.html

    Parameters
    ----------

    method : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMqttAuthenticationProperties::setAuthenticationMethod(const
    #      QString &method)
    self.uglySide.call(
        'ritual_ZN29QMqttAuthenticationProperties23setAuthenticationMethodE'
        'RK7QString',
        method,
    )

  @overload(QByteArray)
  def setAuthenticationData(self, adata: QByteArray) -> None:
    """
    Calls Qt's 'void
    QMqttAuthenticationProperties::setAuthenticationData(const QByteArray
    &adata)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttauthenticationproperties.html

    Parameters
    ----------

    adata : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QMqttAuthenticationProperties::setAuthenticationData(const
    #      QByteArray &adata)
    self.uglySide.call(
        'ritual_ZN29QMqttAuthenticationProperties21setAuthenticationDataERK'
        '10QByteArray',
        self._valueOf(adata),
    )

  @overload(str)
  def setReason(self, r: str) -> None:
    """
    Calls Qt's 'void QMqttAuthenticationProperties::setReason(const QString
    &r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttauthenticationproperties.html#setReason

    Parameters
    ----------

    r : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMqttAuthenticationProperties::setReason(const QString &r)
    self.uglySide.call(
        'ritual_ZN29QMqttAuthenticationProperties9setReasonERK7QString', r,
    )

  @overload(QMqttUserProperties)
  def setUserProperties(self, user: QMqttUserProperties) -> None:
    """
    Calls Qt's 'void QMqttAuthenticationProperties::setUserProperties(const
    QMqttUserProperties &user)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttauthenticationproperties.html

    Parameters
    ----------

    user : QMqttUserProperties
      Passed on as a value: Qt reads the C++ QMqttUserProperties, which stays
      Python's own.
    """
    #  void QMqttAuthenticationProperties::setUserProperties(const
    #      QMqttUserProperties &user)
    self.uglySide.call(
        'ritual_ZN29QMqttAuthenticationProperties17setUserPropertiesERK19QM'
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
    'QMqttAuthenticationProperties::QMqttAuthenticationProperties()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttauthenticationproperties.html
    """
    #  QMqttAuthenticationProperties::QMqttAuthenticationProperties()
    self._noteCreation(QMqttAuthenticationProperties, lambda: Rituals.call(
        'ritual_ZN29QMqttAuthenticationPropertiesC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QMqttAuthenticationProperties) -> None:
    """
    Notes what was given, for Qt's
    'QMqttAuthenticationProperties::QMqttAuthenticationProperties(const
    QMqttAuthenticationProperties &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttauthenticationproperties.html

    Parameters
    ----------

    a0 : QMqttAuthenticationProperties
      Passed on as a value: Qt reads the C++ QMqttAuthenticationProperties,
      which stays Python's own.
    """
    #  QMqttAuthenticationProperties::QMqttAuthenticationProperties(const
    #      QMqttAuthenticationProperties &a0)
    self._noteCreation(QMqttAuthenticationProperties, lambda: Rituals.call(
        'ritual_ZN29QMqttAuthenticationPropertiesC1ERKS_', self._valueOf(a0),
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
