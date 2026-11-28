"""
QPlatformSessionManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qplatformsessionmanager.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QStringList
from . import QSessionManager


class QPlatformSessionManager(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPlatformSessionManager: a plain Python object
  standing in front of one C++ QPlatformSessionManager.

  What exists
  -----------

  Every function of Qt's QPlatformSessionManager that has a ritual and that
  Python can call so far, 17 names in all: 'sessionId', 'sessionKey',
  'allowsInteraction', 'allowsErrorInteraction', 'release', 'cancel',
  'setRestartHint', 'restartHint', 'setRestartCommand', 'restartCommand',
  'setDiscardCommand', 'discardCommand', 'setManagerProperty', 'isPhase2',
  'requestPhase2', 'appCommitData', 'appSaveState'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlatformSessionManager::~QPlatformSessionManager()': the
    destructor: Python never removes a C++ QPlatformSessionManager.

  What has no ritual
  ------------------

  4 of the 24 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QPlatformSessionManager is created at the first use, not by
    'QPlatformSessionManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformSessionManager.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformSessionManager'

  #  A C++ QPlatformSessionManager Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlatformSessionManager'

  #  The functions Qt calls itself that QPlatformSessionManager is the first
  #  to declare and that cannot be handed to Python yet, each as Qt declares
  #  it. A class of a program that writes one of them anew is refused, since
  #  Qt would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'setRestartCommand': (
          'void QPlatformSessionManager::setRestartCommand(const '
          'QStringList &)',
      ),
      'restartCommand': (
          'QStringList QPlatformSessionManager::restartCommand() const',
      ),
      'setDiscardCommand': (
          'void QPlatformSessionManager::setDiscardCommand(const '
          'QStringList &)',
      ),
      'discardCommand': (
          'QStringList QPlatformSessionManager::discardCommand() const',
      ),
  }

  #  The functions Qt calls itself that QPlatformSessionManager is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'sessionId': (
          ('_ZNK23QPlatformSessionManager9sessionIdEv',
           ('address', 'text', ''),
           ()),
      ),
      'sessionKey': (
          ('_ZNK23QPlatformSessionManager10sessionKeyEv',
           ('address', 'text', ''),
           ()),
      ),
      'allowsInteraction': (
          ('_ZN23QPlatformSessionManager17allowsInteractionEv',
           ('bool', 'number', ''),
           ()),
      ),
      'allowsErrorInteraction': (
          ('_ZN23QPlatformSessionManager22allowsErrorInteractionEv',
           ('bool', 'number', ''),
           ()),
      ),
      'release': (
          ('_ZN23QPlatformSessionManager7releaseEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'cancel': (
          ('_ZN23QPlatformSessionManager6cancelEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'setRestartHint': (
          ('_ZN23QPlatformSessionManager14setRestartHintEN15QSessionManager'
           '11RestartHintE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtGui:QSessionManager.RestartHint'),
           )),
      ),
      'restartHint': (
          ('_ZNK23QPlatformSessionManager11restartHintEv',
           ('int', 'enum', 'QtGui:QSessionManager.RestartHint'),
           ()),
      ),
      'setManagerProperty': (
          ('_ZN23QPlatformSessionManager18setManagerPropertyERK7QStringS2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
               ('address', 'text', ''),
           )),
      ),
      'isPhase2': (
          ('_ZNK23QPlatformSessionManager8isPhase2Ev',
           ('bool', 'number', ''),
           ()),
      ),
      'requestPhase2': (
          ('_ZN23QPlatformSessionManager13requestPhase2Ev',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def sessionId(self) -> str:
    """
    Calls Qt's 'QString QPlatformSessionManager::sessionId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsessionmanager.html#sessionId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlatformSessionManager::sessionId() const
    ritual = 'ritual_ZNK23QPlatformSessionManager9sessionIdEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QPlatformSessionManager9sessionIdEv'
    return self.uglySide.call(ritual)

  def sessionKey(self) -> str:
    """
    Calls Qt's 'QString QPlatformSessionManager::sessionKey() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsessionmanager.html#sessionKey

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlatformSessionManager::sessionKey() const
    ritual = 'ritual_ZNK23QPlatformSessionManager10sessionKeyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QPlatformSessionManager10sessionKeyEv'
    return self.uglySide.call(ritual)

  def restartHint(self) -> QSessionManager.RestartHint:
    """
    Calls Qt's 'QSessionManager::RestartHint
    QPlatformSessionManager::restartHint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsessionmanager.html#restartHint

    Returns
    -------

    QSessionManager.RestartHint
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSessionManager.RestartHint(number)' gives.
    """
    #  QSessionManager::RestartHint QPlatformSessionManager::restartHint()
    #      const
    ritual = 'ritual_ZNK23QPlatformSessionManager11restartHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QPlatformSessionManager11restartHintEv'
    return QSessionManager.RestartHint(self.uglySide.call(ritual))

  def restartCommand(self) -> QStringList:
    """
    Calls Qt's 'QStringList QPlatformSessionManager::restartCommand() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsessionmanager.html#restartCommand

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QPlatformSessionManager::restartCommand() const
    address = self.uglySide.call(
        'ritual_ZNK23QPlatformSessionManager14restartCommandEv',
    )
    return QStringList._cuteOwning(address)

  def discardCommand(self) -> QStringList:
    """
    Calls Qt's 'QStringList QPlatformSessionManager::discardCommand() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsessionmanager.html#discardCommand

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QPlatformSessionManager::discardCommand() const
    address = self.uglySide.call(
        'ritual_ZNK23QPlatformSessionManager14discardCommandEv',
    )
    return QStringList._cuteOwning(address)

  def isPhase2(self) -> bool:
    """
    Calls Qt's 'bool QPlatformSessionManager::isPhase2() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsessionmanager.html#isPhase2
    """
    #  bool QPlatformSessionManager::isPhase2() const
    ritual = 'ritual_ZNK23QPlatformSessionManager8isPhase2Ev'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QPlatformSessionManager8isPhase2Ev'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSessionManager.RestartHint)
  def setRestartHint(self, restartHint: QSessionManager.RestartHint) -> None:
    """
    Calls Qt's 'void
    QPlatformSessionManager::setRestartHint(QSessionManager::RestartHint
    restartHint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsessionmanager.html#setRestartHint

    Parameters
    ----------

    restartHint : QSessionManager.RestartHint
      Passed on as its number.
    """
    #  void QPlatformSessionManager::setRestartHint(QSessionManager::
    #      RestartHint restartHint)
    ritual = (
        'ritual_ZN23QPlatformSessionManager14setRestartHintEN15QSessionMana'
        'ger11RestartHintE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QPlatformSessionManager14setRestartHintEN15QSessi'
          'onManager11RestartHintE')
    self.uglySide.call(ritual, restartHint.value)

  @overload(QStringList)
  def setRestartCommand(self, command: QStringList) -> None:
    """
    Calls Qt's 'void QPlatformSessionManager::setRestartCommand(const
    QStringList &command)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsessionmanager.html#setRestartCommand

    Parameters
    ----------

    command : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QPlatformSessionManager::setRestartCommand(const QStringList
    #      &command)
    self.uglySide.call(
        'ritual_ZN23QPlatformSessionManager17setRestartCommandERK5QListI7QS'
        'tringE',
        self._valueOf(command),
    )

  @overload(QStringList)
  def setDiscardCommand(self, command: QStringList) -> None:
    """
    Calls Qt's 'void QPlatformSessionManager::setDiscardCommand(const
    QStringList &command)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsessionmanager.html#setDiscardCommand

    Parameters
    ----------

    command : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QPlatformSessionManager::setDiscardCommand(const QStringList
    #      &command)
    self.uglySide.call(
        'ritual_ZN23QPlatformSessionManager17setDiscardCommandERK5QListI7QS'
        'tringE',
        self._valueOf(command),
    )

  @overload(str, str)
  def setManagerProperty(self, name: str, value: str) -> None:
    """
    Calls Qt's 'void QPlatformSessionManager::setManagerProperty(const
    QString &name, const QString &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsessionmanager.html#setManagerProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlatformSessionManager::setManagerProperty(const QString &name,
    #      const QString &value)
    ritual = (
        'ritual_ZN23QPlatformSessionManager18setManagerPropertyERK7QStringS'
        '2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QPlatformSessionManager18setManagerPropertyERK7QS'
          'tringS2_')
    self.uglySide.call(ritual, name, value)

  @overload(str, QStringList)
  def setManagerProperty(self, name: str, value: QStringList) -> None:
    """
    Calls Qt's 'void QPlatformSessionManager::setManagerProperty(const
    QString &name, const QStringList &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsessionmanager.html#setManagerProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QPlatformSessionManager::setManagerProperty(const QString &name,
    #      const QStringList &value)
    self.uglySide.call(
        'ritual_ZN23QPlatformSessionManager18setManagerPropertyERK7QStringR'
        'K5QListIS0_E',
        name, self._valueOf(value),
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

  @overload(str, str)
  def __init__(self, id: str, key: str) -> None:
    """
    Notes what was given, for Qt's
    'QPlatformSessionManager::QPlatformSessionManager(const QString &id,
    const QString &key)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsessionmanager.html

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.

    key : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QPlatformSessionManager::QPlatformSessionManager(const QString &id,
    #      const QString &key)
    self._noteCreation(QPlatformSessionManager, lambda: Rituals.call(
        'ritual_ZN23QPlatformSessionManagerC1ERK7QStringS2_', id, key,
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

  def allowsInteraction(self) -> bool:
    """
    Calls Qt's 'bool QPlatformSessionManager::allowsInteraction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsessionmanager.html#allowsInteraction
    """
    #  bool QPlatformSessionManager::allowsInteraction()
    ritual = 'ritual_ZN23QPlatformSessionManager17allowsInteractionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QPlatformSessionManager17allowsInteractionEv'
    return self.uglySide.call(ritual)

  def allowsErrorInteraction(self) -> bool:
    """
    Calls Qt's 'bool QPlatformSessionManager::allowsErrorInteraction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsessionmanager.html
    """
    #  bool QPlatformSessionManager::allowsErrorInteraction()
    ritual = 'ritual_ZN23QPlatformSessionManager22allowsErrorInteractionEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QPlatformSessionManager22allowsErrorInteractionEv')
    return self.uglySide.call(ritual)

  def release(self) -> None:
    """
    Calls Qt's 'void QPlatformSessionManager::release()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsessionmanager.html#release
    """
    #  void QPlatformSessionManager::release()
    ritual = 'ritual_ZN23QPlatformSessionManager7releaseEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QPlatformSessionManager7releaseEv'
    self.uglySide.call(ritual)

  def cancel(self) -> None:
    """
    Calls Qt's 'void QPlatformSessionManager::cancel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsessionmanager.html#cancel
    """
    #  void QPlatformSessionManager::cancel()
    ritual = 'ritual_ZN23QPlatformSessionManager6cancelEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QPlatformSessionManager6cancelEv'
    self.uglySide.call(ritual)

  def requestPhase2(self) -> None:
    """
    Calls Qt's 'void QPlatformSessionManager::requestPhase2()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsessionmanager.html#requestPhase2
    """
    #  void QPlatformSessionManager::requestPhase2()
    ritual = 'ritual_ZN23QPlatformSessionManager13requestPhase2Ev'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QPlatformSessionManager13requestPhase2Ev'
    self.uglySide.call(ritual)

  def appCommitData(self) -> None:
    """
    Calls Qt's 'void QPlatformSessionManager::appCommitData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsessionmanager.html#appCommitData
    """
    #  void QPlatformSessionManager::appCommitData()
    self.uglySide.call('ritual_ZN23QPlatformSessionManager13appCommitDataEv')

  def appSaveState(self) -> None:
    """
    Calls Qt's 'void QPlatformSessionManager::appSaveState()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsessionmanager.html#appSaveState
    """
    #  void QPlatformSessionManager::appSaveState()
    self.uglySide.call('ritual_ZN23QPlatformSessionManager12appSaveStateEv')
