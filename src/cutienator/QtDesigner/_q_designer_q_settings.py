"""
QDesignerQSettings binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_qsettings_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QDesignerQSettings to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QDesignerSettingsInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']


class QDesignerQSettings(QDesignerSettingsInterface):
  """
  The cute side of Qt's QDesignerQSettings: a plain Python object standing in
  front of one C++ QDesignerQSettings.

  It is built on the cute 'QDesignerSettingsInterface', as Qt's
  QDesignerQSettings is built on Qt's QDesignerSettingsInterface, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QDesignerQSettings that has a ritual and that Python
  can call so far, 7 names in all: 'beginGroup', 'endGroup', 'contains',
  'setValue', 'value', 'remove', 'settingsApplicationName'. It can be made
  from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QDesignerQSettings is created at the first use, not by
    'QDesignerQSettings(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDesignerQSettings.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def settingsApplicationName() -> str:
    """
    Calls Qt's 'QString QDesignerQSettings::settingsApplicationName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerqsettings.html#settingsApplicationName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerQSettings::settingsApplicationName()
    return Rituals.call(
        'ritual_ZN18QDesignerQSettings23settingsApplicationNameEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesignerQSettings'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def contains(self, key: str) -> bool:
    """
    Calls Qt's 'bool QDesignerQSettings::contains(const QString &key) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignerqsettings.html#contains

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QDesignerQSettings::contains(const QString &key) const
    ritual = 'ritual_ZNK18QDesignerQSettings8containsERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QDesignerQSettings8containsERK7QString'
    return self.uglySide.call(ritual, key)

  @overload(str)
  @overload(str, QVariant)
  def value(
      self,
      key: str,
      defaultValue: Optional[QVariant] = None,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant QDesignerQSettings::value(const QString &key, const
    QVariant &defaultValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignerqsettings.html#value

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    defaultValue : Optional[QVariant]
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own. May be left out, as in Qt: a new 'QVariant()' is then passed on.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QDesignerQSettings::value(const QString &key, const QVariant
    #      &defaultValue) const
    if defaultValue is None:
      from ..QtCore import QVariant
      defaultValue = QVariant()
    ritual = 'ritual_ZNK18QDesignerQSettings5valueERK7QStringRK8QVariant'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18QDesignerQSettings5valueERK7QStringRK8QVariant')
    address = self.uglySide.call(ritual, key, self._valueOf(defaultValue))
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str, QVariant)
  def setValue(self, key: str, value: QVariant) -> None:
    """
    Calls Qt's 'void QDesignerQSettings::setValue(const QString &key, const
    QVariant &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignerqsettings.html#setValue

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QDesignerQSettings::setValue(const QString &key, const QVariant
    #      &value)
    ritual = 'ritual_ZN18QDesignerQSettings8setValueERK7QStringRK8QVariant'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QDesignerQSettings8setValueERK7QStringRK8QVariant')
    self.uglySide.call(ritual, key, self._valueOf(value))

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
    'QDesignerQSettings::QDesignerQSettings()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerqsettings.html#QDesignerQSettings
    """
    #  QDesignerQSettings::QDesignerQSettings()
    self._noteCreation(QDesignerQSettings, lambda: Rituals.call(
        'ritual_ZN18QDesignerQSettingsC1Ev',
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

  @overload(str)
  def beginGroup(self, prefix: str) -> None:
    """
    Calls Qt's 'void QDesignerQSettings::beginGroup(const QString &prefix)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignerqsettings.html#beginGroup

    Parameters
    ----------

    prefix : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesignerQSettings::beginGroup(const QString &prefix)
    ritual = 'ritual_ZN18QDesignerQSettings10beginGroupERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QDesignerQSettings10beginGroupERK7QString'
    self.uglySide.call(ritual, prefix)

  def endGroup(self) -> None:
    """
    Calls Qt's 'void QDesignerQSettings::endGroup()'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignerqsettings.html#endGroup
    """
    #  void QDesignerQSettings::endGroup()
    ritual = 'ritual_ZN18QDesignerQSettings8endGroupEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QDesignerQSettings8endGroupEv'
    self.uglySide.call(ritual)

  @overload(str)
  def remove(self, key: str) -> None:
    """
    Calls Qt's 'void QDesignerQSettings::remove(const QString &key)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignerqsettings.html#remove

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesignerQSettings::remove(const QString &key)
    ritual = 'ritual_ZN18QDesignerQSettings6removeERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QDesignerQSettings6removeERK7QString'
    self.uglySide.call(ritual, key)
