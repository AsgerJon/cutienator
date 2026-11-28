"""
QMqttTopicName binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMqtt/qmqtttopicname.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QLatin1String
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLatin1String = WAIT['QLatin1String']


class QMqttTopicName(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMqttTopicName: a plain Python object standing in
  front of one C++ QMqttTopicName.

  C++ hands a QMqttTopicName around as a copy, so every C++ QMqttTopicName
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QMqttTopicName that has a ritual and that Python can
  call so far, 8 names in all: 'name', 'setName', 'isValid', 'levelCount',
  'levels', '__eq__', '__ne__', '__lt__'. It can be made from Python, in 3
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMqttTopicName::~QMqttTopicName()': the destructor: Python removes
    its C++ QMqttTopicName by it, and has no other use for it.
  - Qt's 'QMqttTopicName &QMqttTopicName::operator=(const QMqttTopicName
    &name)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QMqttTopicName &QMqttTopicName::operator=(QMqttTopicName &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QMqttTopicName::swap(QMqttTopicName &other)': takes a type
    Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QMqttTopicName is created at the first use, not by
    'QMqttTopicName(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMqttTopicName back gives a copy the ritual made for
    Python, in a new cute QMqttTopicName.
  - Each name of Qt's QMqttTopicName that has no cute function yet, 'swap',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMqttTopicName'

  #  Qt's '~QMqttTopicName()'. Naming it makes this a value class: Python
  #  owns every C++ QMqttTopicName behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QMqttTopicNameD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> str:
    """
    Calls Qt's 'QString QMqttTopicName::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqtttopicname.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMqttTopicName::name() const
    return self.uglySide.call('ritual_ZNK14QMqttTopicName4nameEv')

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QMqttTopicName::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqtttopicname.html#isValid
    """
    #  bool QMqttTopicName::isValid() const
    return self.uglySide.call('ritual_ZNK14QMqttTopicName7isValidEv')

  def levelCount(self) -> int:
    """
    Calls Qt's 'int QMqttTopicName::levelCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqtttopicname.html#levelCount
    """
    #  int QMqttTopicName::levelCount() const
    return self.uglySide.call('ritual_ZNK14QMqttTopicName10levelCountEv')

  def levels(self) -> QStringList:
    """
    Calls Qt's 'QStringList QMqttTopicName::levels() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqtttopicname.html#levels

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QMqttTopicName::levels() const
    address = self.uglySide.call('ritual_ZNK14QMqttTopicName6levelsEv')
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QMqttTopicName::setName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqtttopicname.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMqttTopicName::setName(const QString &name)
    self.uglySide.call('ritual_ZN14QMqttTopicName7setNameERK7QString', name)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QMqttTopicName) -> bool:
    """
    Calls Qt's 'bool operator==(const QMqttTopicName &lhs, const
    QMqttTopicName &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqtttopicname.html#operator==

    Parameters
    ----------

    rhs : QMqttTopicName
      Passed on as a value: Qt reads the C++ QMqttTopicName, which stays
      Python's own.
    """
    #  bool operator==(const QMqttTopicName &lhs, const QMqttTopicName &rhs)
    return Rituals.call(
        'ritual_ZeqRK14QMqttTopicNameS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: QMqttTopicName) -> bool:
    """
    Calls Qt's 'bool operator!=(const QMqttTopicName &lhs, const
    QMqttTopicName &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqtttopicname.html#operator!=

    Parameters
    ----------

    rhs : QMqttTopicName
      Passed on as a value: Qt reads the C++ QMqttTopicName, which stays
      Python's own.
    """
    #  bool operator!=(const QMqttTopicName &lhs, const QMqttTopicName &rhs)
    return Rituals.call(
        'ritual_ZneRK14QMqttTopicNameS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __lt__(self, rhs: QMqttTopicName) -> bool:
    """
    Calls Qt's 'bool operator<(const QMqttTopicName &lhs, const
    QMqttTopicName &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqtttopicname.html#operator<

    Parameters
    ----------

    rhs : QMqttTopicName
      Passed on as a value: Qt reads the C++ QMqttTopicName, which stays
      Python's own.
    """
    #  bool operator<(const QMqttTopicName &lhs, const QMqttTopicName &rhs)
    return Rituals.call(
        'ritual_ZltRK14QMqttTopicNameS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __lt__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(str)
  def __init__(self, name: str = '') -> None:
    """
    Notes what was given, for Qt's 'QMqttTopicName::QMqttTopicName(const
    QString &name)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmqtttopicname.html#QMqttTopicName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  QMqttTopicName::QMqttTopicName(const QString &name)
    self._noteCreation(QMqttTopicName, lambda: Rituals.call(
        'ritual_ZN14QMqttTopicNameC1ERK7QString', name,
    ))

  @overload(QLatin1String)
  def __init__(self, name: QLatin1String) -> None:
    """
    Notes what was given, for Qt's 'QMqttTopicName::QMqttTopicName(const
    QLatin1String &name)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmqtttopicname.html#QMqttTopicName

    Parameters
    ----------

    name : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.
    """
    #  QMqttTopicName::QMqttTopicName(const QLatin1String &name)
    self._noteCreation(QMqttTopicName, lambda: Rituals.call(
        'ritual_ZN14QMqttTopicNameC1ERK13QLatin1String', self._valueOf(name),
    ))

  @overload(THIS)
  def __init__(self, name: QMqttTopicName) -> None:
    """
    Notes what was given, for Qt's 'QMqttTopicName::QMqttTopicName(const
    QMqttTopicName &name)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmqtttopicname.html#QMqttTopicName

    Parameters
    ----------

    name : QMqttTopicName
      Passed on as a value: Qt reads the C++ QMqttTopicName, which stays
      Python's own.
    """
    #  QMqttTopicName::QMqttTopicName(const QMqttTopicName &name)
    self._noteCreation(QMqttTopicName, lambda: Rituals.call(
        'ritual_ZN14QMqttTopicNameC1ERKS_', self._valueOf(name),
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

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QMqttTopicName::swap(QMqttTopicName &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QMqttTopicName.swap' has no cute function yet. Qt's 'void "
        "QMqttTopicName::swap(QMqttTopicName &other)': takes a type Python "
        "has no way to hand over yet.")
