"""
QOpcUaApplicationIdentity binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuaapplicationidentity.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from . import QOpcUaApplicationDescription


class QOpcUaApplicationIdentity(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaApplicationIdentity: a plain Python object
  standing in front of one C++ QOpcUaApplicationIdentity.

  C++ hands a QOpcUaApplicationIdentity around as a copy, so every C++
  QOpcUaApplicationIdentity behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaApplicationIdentity that has a ritual and that
  Python can call so far, 9 names in all: 'applicationUri',
  'setApplicationUri', 'applicationName', 'setApplicationName', 'productUri',
  'setProductUri', 'applicationType', 'setApplicationType', 'isValid'. It can
  be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaApplicationIdentity::~QOpcUaApplicationIdentity()': the
    destructor: Python removes its C++ QOpcUaApplicationIdentity by it, and
    has no other use for it.
  - Qt's 'QOpcUaApplicationIdentity
    &QOpcUaApplicationIdentity::operator=(const QOpcUaApplicationIdentity
    &rhs)': assignment: Python binds a name and has no operator for it.

  What to expect
  --------------

  - The C++ QOpcUaApplicationIdentity is created at the first use, not by
    'QOpcUaApplicationIdentity(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaApplicationIdentity back gives a copy the
    ritual made for Python, in a new cute QOpcUaApplicationIdentity.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaApplicationIdentity'

  #  Qt's '~QOpcUaApplicationIdentity()'. Naming it makes this a value class:
  #  Python owns every C++ QOpcUaApplicationIdentity behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN25QOpcUaApplicationIdentityD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def applicationUri(self) -> str:
    """
    Calls Qt's 'QString QOpcUaApplicationIdentity::applicationUri() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaapplicationidentity.html#applicationUri

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaApplicationIdentity::applicationUri() const
    return self.uglySide.call(
        'ritual_ZNK25QOpcUaApplicationIdentity14applicationUriEv',
    )

  def applicationName(self) -> str:
    """
    Calls Qt's 'QString QOpcUaApplicationIdentity::applicationName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaapplicationidentity.html#applicationName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaApplicationIdentity::applicationName() const
    return self.uglySide.call(
        'ritual_ZNK25QOpcUaApplicationIdentity15applicationNameEv',
    )

  def productUri(self) -> str:
    """
    Calls Qt's 'QString QOpcUaApplicationIdentity::productUri() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaapplicationidentity.html#productUri

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaApplicationIdentity::productUri() const
    return self.uglySide.call(
        'ritual_ZNK25QOpcUaApplicationIdentity10productUriEv',
    )

  def applicationType(self) -> QOpcUaApplicationDescription.ApplicationType:
    """
    Calls Qt's 'QOpcUaApplicationDescription::ApplicationType
    QOpcUaApplicationIdentity::applicationType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaapplicationidentity.html#applicationType

    Returns
    -------

    QOpcUaApplicationDescription.ApplicationType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QOpcUaApplicationDescription.ApplicationType(number)' gives.
    """
    #  QOpcUaApplicationDescription::ApplicationType
    #      QOpcUaApplicationIdentity::applicationType() const
    return QOpcUaApplicationDescription.ApplicationType(self.uglySide.call(
        'ritual_ZNK25QOpcUaApplicationIdentity15applicationTypeEv',
    ))

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaApplicationIdentity::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaapplicationidentity.html#isValid
    """
    #  bool QOpcUaApplicationIdentity::isValid() const
    return self.uglySide.call(
        'ritual_ZNK25QOpcUaApplicationIdentity7isValidEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setApplicationUri(self, value: str) -> None:
    """
    Calls Qt's 'void QOpcUaApplicationIdentity::setApplicationUri(const
    QString &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaapplicationidentity.html#setApplicationUri

    Parameters
    ----------

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaApplicationIdentity::setApplicationUri(const QString
    #      &value)
    self.uglySide.call(
        'ritual_ZN25QOpcUaApplicationIdentity17setApplicationUriERK7QString',
        value,
    )

  @overload(str)
  def setApplicationName(self, value: str) -> None:
    """
    Calls Qt's 'void QOpcUaApplicationIdentity::setApplicationName(const
    QString &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaapplicationidentity.html#setApplicationName

    Parameters
    ----------

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaApplicationIdentity::setApplicationName(const QString
    #      &value)
    self.uglySide.call(
        'ritual_ZN25QOpcUaApplicationIdentity18setApplicationNameERK7QStrin'
        'g',
        value,
    )

  @overload(str)
  def setProductUri(self, value: str) -> None:
    """
    Calls Qt's 'void QOpcUaApplicationIdentity::setProductUri(const QString
    &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaapplicationidentity.html#setProductUri

    Parameters
    ----------

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaApplicationIdentity::setProductUri(const QString &value)
    self.uglySide.call(
        'ritual_ZN25QOpcUaApplicationIdentity13setProductUriERK7QString',
        value,
    )

  @overload(QOpcUaApplicationDescription.ApplicationType)
  def setApplicationType(
      self,
      value: QOpcUaApplicationDescription.ApplicationType,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaApplicationIdentity::setApplicationType(
    QOpcUaApplicationDescription::ApplicationType value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaapplicationidentity.html#setApplicationType

    Parameters
    ----------

    value : QOpcUaApplicationDescription.ApplicationType
      Passed on as its number.
    """
    #  void QOpcUaApplicationIdentity::setApplicationType(
    #      QOpcUaApplicationDescription::ApplicationType value)
    self.uglySide.call(
        'ritual_ZN25QOpcUaApplicationIdentity18setApplicationTypeEN28QOpcUa'
        'ApplicationDescription15ApplicationTypeE',
        value.value,
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
    'QOpcUaApplicationIdentity::QOpcUaApplicationIdentity()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaapplicationidentity.html
    """
    #  QOpcUaApplicationIdentity::QOpcUaApplicationIdentity()
    self._noteCreation(QOpcUaApplicationIdentity, lambda: Rituals.call(
        'ritual_ZN25QOpcUaApplicationIdentityC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QOpcUaApplicationIdentity) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaApplicationIdentity::QOpcUaApplicationIdentity(const
    QOpcUaApplicationIdentity &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaapplicationidentity.html

    Parameters
    ----------

    other : QOpcUaApplicationIdentity
      Passed on as a value: Qt reads the C++ QOpcUaApplicationIdentity, which
      stays Python's own.
    """
    #  QOpcUaApplicationIdentity::QOpcUaApplicationIdentity(const
    #      QOpcUaApplicationIdentity &other)
    self._noteCreation(QOpcUaApplicationIdentity, lambda: Rituals.call(
        'ritual_ZN25QOpcUaApplicationIdentityC1ERKS_', self._valueOf(other),
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
