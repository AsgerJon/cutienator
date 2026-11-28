"""
QNearFieldManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNfc/qnearfieldmanager.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QNearFieldTarget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QNearFieldManagerPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QNearFieldManagerPrivate = WAIT['QNearFieldManagerPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QNearFieldManager(QObject):
  """
  The cute side of Qt's QNearFieldManager: a plain Python object standing in
  front of one C++ QNearFieldManager.

  It is built on the cute 'QObject', as Qt's QNearFieldManager is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QNearFieldManager that has a ritual and that Python
  can call so far, 12 names in all: 'metaObject', 'tr', 'd_func',
  'isEnabled', 'isSupported', 'startTargetDetection', 'stopTargetDetection',
  'setUserInformation', 'adapterStateChanged', 'targetDetectionStopped',
  'targetDetected', 'targetLost'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QNearFieldManager::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QNearFieldManager::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QNearFieldManagerPrivate *QNearFieldManager::d_func() const':
    takes in Python what 'QNearFieldManagerPrivate
    *QNearFieldManager::d_func()' takes.
  - Qt's 'QNearFieldManager::~QNearFieldManager()': the destructor: Python
    never removes a C++ QNearFieldManager.

  What has no ritual
  ------------------

  2 of the 20 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QNearFieldManager is created at the first use, not by
    'QNearFieldManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNearFieldManager.
  - Qt tells when it has removed the C++ QNearFieldManager. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QNearFieldManager, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class AdapterState(CuteNum, scoped=True):
    """
    The enum 'QNearFieldManager::AdapterState' of Qt, with the 4 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Offline = Kee[int](1)
    TurningOn = Kee[int](2)
    Online = Kee[int](3)
    TurningOff = Kee[int](4)

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
    Calls Qt's 'QString QNearFieldManager::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qnearfieldmanager.html#tr

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
    #  QString QNearFieldManager::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QNearFieldManager2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNearFieldManager'

  #  A C++ QNearFieldManager Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNearFieldManager'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QNearFieldManager::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnearfieldmanager.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QNearFieldManager::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QNearFieldManager10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isEnabled(self) -> bool:
    """
    Calls Qt's 'bool QNearFieldManager::isEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnearfieldmanager.html#isEnabled
    """
    #  bool QNearFieldManager::isEnabled() const
    return self.uglySide.call('ritual_ZNK17QNearFieldManager9isEnabledEv')

  @overload()
  @overload(QNearFieldTarget.AccessMethod)
  def isSupported(
      self,
      accessMethod: QNearFieldTarget.AccessMethod = (
          QNearFieldTarget.AccessMethod.AnyAccess),
  ) -> bool:
    """
    Calls Qt's 'bool
    QNearFieldManager::isSupported(QNearFieldTarget::AccessMethod
    accessMethod) const'.

    Qt's own words: https://doc.qt.io/qt-6/qnearfieldmanager.html#isSupported

    Parameters
    ----------

    accessMethod : QNearFieldTarget.AccessMethod
      Passed on as its number. May be left out, as in Qt: it is then
      QNearFieldTarget.AccessMethod.AnyAccess.
    """
    #  bool QNearFieldManager::isSupported(QNearFieldTarget::AccessMethod
    #      accessMethod) const
    return self.uglySide.call(
        'ritual_ZNK17QNearFieldManager11isSupportedEN16QNearFieldTarget12Ac'
        'cessMethodE',
        accessMethod.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setUserInformation(self, message: str) -> None:
    """
    Calls Qt's 'void QNearFieldManager::setUserInformation(const QString
    &message)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnearfieldmanager.html#setUserInformation

    Parameters
    ----------

    message : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QNearFieldManager::setUserInformation(const QString &message)
    self.uglySide.call(
        'ritual_ZN17QNearFieldManager18setUserInformationERK7QString',
        message,
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

  @overload(QNearFieldManagerPrivate)
  @overload(QNearFieldManagerPrivate, QObject)
  @overload(QNearFieldManagerPrivate, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      backend: Optional[QNearFieldManagerPrivate],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QNearFieldManager::QNearFieldManager(QNearFieldManagerPrivate *backend,
    QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnearfieldmanager.html#QNearFieldManager

    Parameters
    ----------

    backend : Optional[QNearFieldManagerPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QNearFieldManager::QNearFieldManager(QNearFieldManagerPrivate
    #      *backend, QObject *parent)
    self._noteCreation(QNearFieldManager, lambda: Rituals.call(
        'ritual_ZN17QNearFieldManagerC1EP24QNearFieldManagerPrivateP7QObjec'
        't',
        self._addressOf(backend), self._addressOf(parent, 'QObject'),
    ))

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QNearFieldManager::QNearFieldManager(QObject *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnearfieldmanager.html#QNearFieldManager

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QNearFieldManager::QNearFieldManager(QObject *parent)
    self._noteCreation(QNearFieldManager, lambda: Rituals.call(
        'ritual_ZN17QNearFieldManagerC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def d_func(self) -> Optional[QNearFieldManagerPrivate]:
    """
    Calls Qt's 'QNearFieldManagerPrivate *QNearFieldManager::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qnearfieldmanager.html#d_func

    Returns
    -------

    Optional[QNearFieldManagerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNearFieldManagerPrivate *QNearFieldManager::d_func()
    address = self.uglySide.call('ritual_ZN17QNearFieldManager6d_funcEv')
    from . import QNearFieldManagerPrivate
    return QNearFieldManagerPrivate._cuteAt(address)

  @overload(QNearFieldTarget.AccessMethod)
  def startTargetDetection(
      self,
      accessMethod: QNearFieldTarget.AccessMethod,
  ) -> bool:
    """
    Calls Qt's 'bool
    QNearFieldManager::startTargetDetection(QNearFieldTarget::AccessMethod
    accessMethod)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnearfieldmanager.html#startTargetDetection

    Parameters
    ----------

    accessMethod : QNearFieldTarget.AccessMethod
      Passed on as its number.
    """
    #  bool QNearFieldManager::startTargetDetection(QNearFieldTarget::
    #      AccessMethod accessMethod)
    return self.uglySide.call(
        'ritual_ZN17QNearFieldManager20startTargetDetectionEN16QNearFieldTa'
        'rget12AccessMethodE',
        accessMethod.value,
    )

  @overload()
  @overload(str)
  def stopTargetDetection(self, errorMessage: str = '') -> None:
    """
    Calls Qt's 'void QNearFieldManager::stopTargetDetection(const QString
    &errorMessage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnearfieldmanager.html#stopTargetDetection

    Parameters
    ----------

    errorMessage : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QNearFieldManager::stopTargetDetection(const QString
    #      &errorMessage)
    self.uglySide.call(
        'ritual_ZN17QNearFieldManager19stopTargetDetectionERK7QString',
        errorMessage,
    )

  @overload(AdapterState)
  def adapterStateChanged(self, state: AdapterState) -> None:
    """
    Calls Qt's 'void
    QNearFieldManager::adapterStateChanged(QNearFieldManager::AdapterState
    state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnearfieldmanager.html#adapterStateChanged

    Parameters
    ----------

    state : AdapterState
      Passed on as its number.
    """
    #  void QNearFieldManager::adapterStateChanged(QNearFieldManager::
    #      AdapterState state)
    self.uglySide.call(
        'ritual_ZN17QNearFieldManager19adapterStateChangedENS_12AdapterStat'
        'eE',
        state.value,
    )

  def targetDetectionStopped(self) -> None:
    """
    Calls Qt's 'void QNearFieldManager::targetDetectionStopped()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnearfieldmanager.html#targetDetectionStopped
    """
    #  void QNearFieldManager::targetDetectionStopped()
    self.uglySide.call(
        'ritual_ZN17QNearFieldManager22targetDetectionStoppedEv',
    )

  @overload(QNearFieldTarget)
  @overload(NoneType)
  def targetDetected(self, target: Optional[QNearFieldTarget]) -> None:
    """
    Calls Qt's 'void QNearFieldManager::targetDetected(QNearFieldTarget
    *target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnearfieldmanager.html#targetDetected

    Parameters
    ----------

    target : Optional[QNearFieldTarget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QNearFieldManager::targetDetected(QNearFieldTarget *target)
    self.uglySide.call(
        'ritual_ZN17QNearFieldManager14targetDetectedEP16QNearFieldTarget',
        self._addressOf(target),
    )

  @overload(QNearFieldTarget)
  @overload(NoneType)
  def targetLost(self, target: Optional[QNearFieldTarget]) -> None:
    """
    Calls Qt's 'void QNearFieldManager::targetLost(QNearFieldTarget
    *target)'.

    Qt's own words: https://doc.qt.io/qt-6/qnearfieldmanager.html#targetLost

    Parameters
    ----------

    target : Optional[QNearFieldTarget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QNearFieldManager::targetLost(QNearFieldTarget *target)
    self.uglySide.call(
        'ritual_ZN17QNearFieldManager10targetLostEP16QNearFieldTarget',
        self._addressOf(target),
    )
