"""
QSessionManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qsessionmanager.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum
from ..occult import Rituals
from ..QtCore import QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSessionManager(QObject):
  """
  The cute side of Qt's QSessionManager: a plain Python object standing in
  front of one C++ QSessionManager.

  It is built on the cute 'QObject', as Qt's QSessionManager is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSessionManager that has a ritual and that Python
  can call so far, 17 names in all: 'metaObject', 'tr', 'sessionId',
  'sessionKey', 'allowsInteraction', 'allowsErrorInteraction', 'release',
  'cancel', 'setRestartHint', 'restartHint', 'setRestartCommand',
  'restartCommand', 'setDiscardCommand', 'discardCommand',
  'setManagerProperty', 'isPhase2', 'requestPhase2'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSessionManager::~QSessionManager()': the destructor: Python never
    removes a C++ QSessionManager.

  What has no ritual
  ------------------

  7 of the 26 functions Qt declares: 5 takes or gives a type that cannot be
  passed yet; 1 a template; 1 declared and nowhere to be found.

  What to expect
  --------------

  - The C++ QSessionManager is created at the first use, not by
    'QSessionManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSessionManager.
  - Qt tells when it has removed the C++ QSessionManager. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QSessionManager, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class RestartHint(CuteNum):
    """
    The enum 'QSessionManager::RestartHint' of Qt, with the 4 names Qt gives
    in it.
    """

    RestartIfRunning = Kee[int](0)
    RestartAnyway = Kee[int](1)
    RestartImmediately = Kee[int](2)
    RestartNever = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QSessionManager::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsessionmanager.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSessionManager::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QSessionManager2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSessionManager'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSessionManager::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsessionmanager.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSessionManager::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QSessionManager10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def sessionId(self) -> str:
    """
    Calls Qt's 'QString QSessionManager::sessionId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsessionmanager.html#sessionId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSessionManager::sessionId() const
    return self.uglySide.call('ritual_ZNK15QSessionManager9sessionIdEv')

  def sessionKey(self) -> str:
    """
    Calls Qt's 'QString QSessionManager::sessionKey() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsessionmanager.html#sessionKey

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSessionManager::sessionKey() const
    return self.uglySide.call('ritual_ZNK15QSessionManager10sessionKeyEv')

  def restartHint(self) -> RestartHint:
    """
    Calls Qt's 'RestartHint QSessionManager::restartHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsessionmanager.html#restartHint

    Returns
    -------

    RestartHint
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'RestartHint(number)'
      gives.
    """
    #  RestartHint QSessionManager::restartHint() const
    return QSessionManager.RestartHint(self.uglySide.call(
        'ritual_ZNK15QSessionManager11restartHintEv',
    ))

  def restartCommand(self) -> QStringList:
    """
    Calls Qt's 'QStringList QSessionManager::restartCommand() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsessionmanager.html#restartCommand

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QSessionManager::restartCommand() const
    address = self.uglySide.call(
        'ritual_ZNK15QSessionManager14restartCommandEv',
    )
    return QStringList._cuteOwning(address)

  def discardCommand(self) -> QStringList:
    """
    Calls Qt's 'QStringList QSessionManager::discardCommand() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsessionmanager.html#discardCommand

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QSessionManager::discardCommand() const
    address = self.uglySide.call(
        'ritual_ZNK15QSessionManager14discardCommandEv',
    )
    return QStringList._cuteOwning(address)

  def isPhase2(self) -> bool:
    """
    Calls Qt's 'bool QSessionManager::isPhase2() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsessionmanager.html#isPhase2
    """
    #  bool QSessionManager::isPhase2() const
    return self.uglySide.call('ritual_ZNK15QSessionManager8isPhase2Ev')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(RestartHint)
  def setRestartHint(self, a0: RestartHint) -> None:
    """
    Calls Qt's 'void QSessionManager::setRestartHint(RestartHint a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsessionmanager.html#setRestartHint

    Parameters
    ----------

    a0 : RestartHint
      Passed on as its number.
    """
    #  void QSessionManager::setRestartHint(RestartHint a0)
    self.uglySide.call(
        'ritual_ZN15QSessionManager14setRestartHintENS_11RestartHintE',
        a0.value,
    )

  @overload(QStringList)
  def setRestartCommand(self, a0: QStringList) -> None:
    """
    Calls Qt's 'void QSessionManager::setRestartCommand(const QStringList
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsessionmanager.html#setRestartCommand

    Parameters
    ----------

    a0 : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QSessionManager::setRestartCommand(const QStringList &a0)
    self.uglySide.call(
        'ritual_ZN15QSessionManager17setRestartCommandERK5QListI7QStringE',
        self._valueOf(a0),
    )

  @overload(QStringList)
  def setDiscardCommand(self, a0: QStringList) -> None:
    """
    Calls Qt's 'void QSessionManager::setDiscardCommand(const QStringList
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsessionmanager.html#setDiscardCommand

    Parameters
    ----------

    a0 : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QSessionManager::setDiscardCommand(const QStringList &a0)
    self.uglySide.call(
        'ritual_ZN15QSessionManager17setDiscardCommandERK5QListI7QStringE',
        self._valueOf(a0),
    )

  @overload(str, str)
  def setManagerProperty(self, name: str, value: str) -> None:
    """
    Calls Qt's 'void QSessionManager::setManagerProperty(const QString &name,
    const QString &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsessionmanager.html#setManagerProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSessionManager::setManagerProperty(const QString &name, const
    #      QString &value)
    self.uglySide.call(
        'ritual_ZN15QSessionManager18setManagerPropertyERK7QStringS2_',
        name, value,
    )

  @overload(str, QStringList)
  def setManagerProperty(self, name: str, value: QStringList) -> None:
    """
    Calls Qt's 'void QSessionManager::setManagerProperty(const QString &name,
    const QStringList &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsessionmanager.html#setManagerProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QSessionManager::setManagerProperty(const QString &name, const
    #      QStringList &value)
    self.uglySide.call(
        'ritual_ZN15QSessionManager18setManagerPropertyERK7QStringRK5QListI'
        'S0_E',
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
    Calls Qt's 'bool QSessionManager::allowsInteraction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsessionmanager.html#allowsInteraction
    """
    #  bool QSessionManager::allowsInteraction()
    return self.uglySide.call(
        'ritual_ZN15QSessionManager17allowsInteractionEv',
    )

  def allowsErrorInteraction(self) -> bool:
    """
    Calls Qt's 'bool QSessionManager::allowsErrorInteraction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsessionmanager.html#allowsErrorInteraction
    """
    #  bool QSessionManager::allowsErrorInteraction()
    return self.uglySide.call(
        'ritual_ZN15QSessionManager22allowsErrorInteractionEv',
    )

  def release(self) -> None:
    """
    Calls Qt's 'void QSessionManager::release()'.

    Qt's own words: https://doc.qt.io/qt-6/qsessionmanager.html#release
    """
    #  void QSessionManager::release()
    self.uglySide.call('ritual_ZN15QSessionManager7releaseEv')

  def cancel(self) -> None:
    """
    Calls Qt's 'void QSessionManager::cancel()'.

    Qt's own words: https://doc.qt.io/qt-6/qsessionmanager.html#cancel
    """
    #  void QSessionManager::cancel()
    self.uglySide.call('ritual_ZN15QSessionManager6cancelEv')

  def requestPhase2(self) -> None:
    """
    Calls Qt's 'void QSessionManager::requestPhase2()'.

    Qt's own words: https://doc.qt.io/qt-6/qsessionmanager.html#requestPhase2
    """
    #  void QSessionManager::requestPhase2()
    self.uglySide.call('ritual_ZN15QSessionManager13requestPhase2Ev')
