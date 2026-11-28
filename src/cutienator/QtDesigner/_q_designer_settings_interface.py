"""
QDesignerSettingsInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/abstractsettings.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']


class QDesignerSettingsInterface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDesignerSettingsInterface: a plain Python object
  standing in front of one C++ QDesignerSettingsInterface.

  What exists
  -----------

  Every function of Qt's QDesignerSettingsInterface that has a ritual and
  that Python can call so far, 6 names in all: 'beginGroup', 'endGroup',
  'contains', 'setValue', 'value', 'remove'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDesignerSettingsInterface::~QDesignerSettingsInterface()': the
    destructor: Python never removes a C++ QDesignerSettingsInterface.

  What has no ritual
  ------------------

  4 of the 12 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QDesignerSettingsInterface is created at the first use, not by
    'QDesignerSettingsInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDesignerSettingsInterface.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesignerSettingsInterface'

  #  A C++ QDesignerSettingsInterface Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDesignerSettingsInterface'

  #  The functions Qt calls itself that QDesignerSettingsInterface is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'beginGroup': (
          ('_ZN26QDesignerSettingsInterface10beginGroupERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'endGroup': (
          ('_ZN26QDesignerSettingsInterface8endGroupEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'contains': (
          ('_ZNK26QDesignerSettingsInterface8containsERK7QString',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'setValue': (
          ('_ZN26QDesignerSettingsInterface8setValueERK7QStringRK8QVariant',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
      'value': (
          ('_ZNK26QDesignerSettingsInterface5valueERK7QStringRK8QVariant',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('address', 'text', ''),
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
      'remove': (
          ('_ZN26QDesignerSettingsInterface6removeERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
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

  @overload(str)
  def contains(self, key: str) -> bool:
    """
    Calls Qt's 'bool QDesignerSettingsInterface::contains(const QString &key)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignersettingsinterface.html#contains

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QDesignerSettingsInterface::contains(const QString &key) const
    return self.uglySide.call(
        'ritual_ZNK26QDesignerSettingsInterface8containsERK7QString', key,
    )

  @overload(str)
  @overload(str, QVariant)
  def value(
      self,
      key: str,
      defaultValue: Optional[QVariant] = None,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant QDesignerSettingsInterface::value(const QString
    &key, const QVariant &defaultValue) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignersettingsinterface.html#value

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
    #  QVariant QDesignerSettingsInterface::value(const QString &key, const
    #      QVariant &defaultValue) const
    if defaultValue is None:
      from ..QtCore import QVariant
      defaultValue = QVariant()
    address = self.uglySide.call(
        'ritual_ZNK26QDesignerSettingsInterface5valueERK7QStringRK8QVariant',
        key, self._valueOf(defaultValue),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str, QVariant)
  def setValue(self, key: str, value: QVariant) -> None:
    """
    Calls Qt's 'void QDesignerSettingsInterface::setValue(const QString &key,
    const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignersettingsinterface.html#setValue

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QDesignerSettingsInterface::setValue(const QString &key, const
    #      QVariant &value)
    self.uglySide.call(
        'ritual_ZN26QDesignerSettingsInterface8setValueERK7QStringRK8QVaria'
        'nt',
        key, self._valueOf(value),
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
    'QDesignerSettingsInterface::QDesignerSettingsInterface()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignersettingsinterface.html
    """
    #  QDesignerSettingsInterface::QDesignerSettingsInterface()
    self._noteCreation(QDesignerSettingsInterface, lambda: Rituals.call(
        'ritual_ZN26QDesignerSettingsInterfaceC1Ev',
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
    Calls Qt's 'void QDesignerSettingsInterface::beginGroup(const QString
    &prefix)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignersettingsinterface.html#beginGroup

    Parameters
    ----------

    prefix : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesignerSettingsInterface::beginGroup(const QString &prefix)
    self.uglySide.call(
        'ritual_ZN26QDesignerSettingsInterface10beginGroupERK7QString',
        prefix,
    )

  def endGroup(self) -> None:
    """
    Calls Qt's 'void QDesignerSettingsInterface::endGroup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignersettingsinterface.html#endGroup
    """
    #  void QDesignerSettingsInterface::endGroup()
    self.uglySide.call('ritual_ZN26QDesignerSettingsInterface8endGroupEv')

  @overload(str)
  def remove(self, key: str) -> None:
    """
    Calls Qt's 'void QDesignerSettingsInterface::remove(const QString &key)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignersettingsinterface.html#remove

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesignerSettingsInterface::remove(const QString &key)
    self.uglySide.call(
        'ritual_ZN26QDesignerSettingsInterface6removeERK7QString', key,
    )
