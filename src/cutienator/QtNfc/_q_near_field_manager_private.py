"""
QNearFieldManagerPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNfc/6.12.0/QtNfc/private/qnearfieldmanager_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QNearFieldManagerPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..QtCore import QObject
from . import QNearFieldManager, QNearFieldTarget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QNearFieldManagerPrivate(QObject):
  """
  The cute side of Qt's QNearFieldManagerPrivate: a plain Python object
  standing in front of one C++ QNearFieldManagerPrivate.

  It is built on the cute 'QObject', as Qt's QNearFieldManagerPrivate is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QNearFieldManagerPrivate that has a ritual and that
  Python can call so far, 10 names in all: 'metaObject', 'isEnabled',
  'isSupported', 'startTargetDetection', 'stopTargetDetection',
  'setUserInformation', 'adapterStateChanged', 'targetDetectionStopped',
  'targetDetected', 'targetLost'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QNearFieldManagerPrivate::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QNearFieldManagerPrivate::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QNearFieldManagerPrivate::~QNearFieldManagerPrivate()': the
    destructor: Python never removes a C++ QNearFieldManagerPrivate.

  What has no ritual
  ------------------

  4 of the 17 functions Qt declares: 2 not a gap; 2 leans on
  'QNearFieldManagerPrivate.

  What to expect
  --------------

  - The C++ QNearFieldManagerPrivate is created at the first use, not by
    'QNearFieldManagerPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNearFieldManagerPrivate.
  - Qt tells when it has removed the C++ QNearFieldManagerPrivate. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QNearFieldManagerPrivate that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNearFieldManagerPrivate'

  #  A C++ QNearFieldManagerPrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNearFieldManagerPrivate'

  #  The functions Qt calls itself that QNearFieldManagerPrivate is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'isEnabled': (
          ('_ZNK24QNearFieldManagerPrivate9isEnabledEv',
           ('bool', 'number', ''),
           ()),
      ),
      'isSupported': (
          ('_ZNK24QNearFieldManagerPrivate11isSupportedEN16QNearFieldTarget'
           '12AccessMethodE',
           ('bool', 'number', ''),
           (
               ('int', 'enum', 'QtNfc:QNearFieldTarget.AccessMethod'),
           )),
      ),
      'startTargetDetection': (
          ('_ZN24QNearFieldManagerPrivate20startTargetDetectionEN16QNearFie'
           'ldTarget12AccessMethodE',
           ('bool', 'number', ''),
           (
               ('int', 'enum', 'QtNfc:QNearFieldTarget.AccessMethod'),
           )),
      ),
      'stopTargetDetection': (
          ('_ZN24QNearFieldManagerPrivate19stopTargetDetectionERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'setUserInformation': (
          ('_ZN24QNearFieldManagerPrivate18setUserInformationERK7QString',
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QNearFieldManagerPrivate::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnearfieldmanagerprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QNearFieldManagerPrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QNearFieldManagerPrivate10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isEnabled(self) -> bool:
    """
    Calls Qt's 'bool QNearFieldManagerPrivate::isEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnearfieldmanagerprivate.html#isEnabled
    """
    #  bool QNearFieldManagerPrivate::isEnabled() const
    ritual = 'ritual_ZNK24QNearFieldManagerPrivate9isEnabledEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QNearFieldManagerPrivate9isEnabledEv'
    return self.uglySide.call(ritual)

  @overload(QNearFieldTarget.AccessMethod)
  def isSupported(self, a0: QNearFieldTarget.AccessMethod) -> bool:
    """
    Calls Qt's 'bool
    QNearFieldManagerPrivate::isSupported(QNearFieldTarget::AccessMethod a0)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnearfieldmanagerprivate.html#isSupported

    Parameters
    ----------

    a0 : QNearFieldTarget.AccessMethod
      Passed on as its number.
    """
    #  bool QNearFieldManagerPrivate::isSupported(QNearFieldTarget::
    #      AccessMethod a0) const
    ritual = (
        'ritual_ZNK24QNearFieldManagerPrivate11isSupportedEN16QNearFieldTar'
        'get12AccessMethodE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QNearFieldManagerPrivate11isSupportedEN16QNearFi'
          'eldTarget12AccessMethodE')
    return self.uglySide.call(ritual, a0.value)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setUserInformation(self, a0: str) -> None:
    """
    Calls Qt's 'void QNearFieldManagerPrivate::setUserInformation(const
    QString &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnearfieldmanagerprivate.html#setUserInformation

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QNearFieldManagerPrivate::setUserInformation(const QString &a0)
    ritual = (
        'ritual_ZN24QNearFieldManagerPrivate18setUserInformationERK7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QNearFieldManagerPrivate18setUserInformationERK7Q'
          'String')
    self.uglySide.call(ritual, a0)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QNearFieldManagerPrivate::QNearFieldManagerPrivate(QObject
    *parent)': leans on
    'QNearFieldManagerPrivate::qt_metacall(QMetaObject::Call, int, void**)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QNearFieldManagerPrivate.__init__' has no cute function yet. Qt's "
        "'QNearFieldManagerPrivate::QNearFieldManagerPrivate(QObject "
        "*parent)': leans on "
        "'QNearFieldManagerPrivate::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  @overload(QNearFieldTarget.AccessMethod)
  def startTargetDetection(self, a0: QNearFieldTarget.AccessMethod) -> bool:
    """
    Calls Qt's 'bool
    QNearFieldManagerPrivate::startTargetDetection(QNearFieldTarget::
    AccessMethod a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnearfieldmanagerprivate.html#startTargetDetection

    Parameters
    ----------

    a0 : QNearFieldTarget.AccessMethod
      Passed on as its number.
    """
    #  bool QNearFieldManagerPrivate::startTargetDetection(QNearFieldTarget::
    #      AccessMethod a0)
    ritual = (
        'ritual_ZN24QNearFieldManagerPrivate20startTargetDetectionEN16QNear'
        'FieldTarget12AccessMethodE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QNearFieldManagerPrivate20startTargetDetectionEN1'
          '6QNearFieldTarget12AccessMethodE')
    return self.uglySide.call(ritual, a0.value)

  @overload(str)
  def stopTargetDetection(self, a0: str) -> None:
    """
    Calls Qt's 'void QNearFieldManagerPrivate::stopTargetDetection(const
    QString &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnearfieldmanagerprivate.html#stopTargetDetection

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QNearFieldManagerPrivate::stopTargetDetection(const QString &a0)
    ritual = (
        'ritual_ZN24QNearFieldManagerPrivate19stopTargetDetectionERK7QStrin'
        'g')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QNearFieldManagerPrivate19stopTargetDetectionERK7'
          'QString')
    self.uglySide.call(ritual, a0)

  @overload(QNearFieldManager.AdapterState)
  def adapterStateChanged(
      self,
      state: QNearFieldManager.AdapterState,
  ) -> None:
    """
    Calls Qt's 'void
    QNearFieldManagerPrivate::adapterStateChanged(QNearFieldManager::
    AdapterState state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnearfieldmanagerprivate.html#adapterStateChanged

    Parameters
    ----------

    state : QNearFieldManager.AdapterState
      Passed on as its number.
    """
    #  void QNearFieldManagerPrivate::adapterStateChanged(QNearFieldManager::
    #      AdapterState state)
    self.uglySide.call(
        'ritual_ZN24QNearFieldManagerPrivate19adapterStateChangedEN17QNearF'
        'ieldManager12AdapterStateE',
        state.value,
    )

  def targetDetectionStopped(self) -> None:
    """
    Calls Qt's 'void QNearFieldManagerPrivate::targetDetectionStopped()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnearfieldmanagerprivate.html
    """
    #  void QNearFieldManagerPrivate::targetDetectionStopped()
    self.uglySide.call(
        'ritual_ZN24QNearFieldManagerPrivate22targetDetectionStoppedEv',
    )

  @overload(QNearFieldTarget)
  @overload(NoneType)
  def targetDetected(self, target: Optional[QNearFieldTarget]) -> None:
    """
    Calls Qt's 'void
    QNearFieldManagerPrivate::targetDetected(QNearFieldTarget *target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnearfieldmanagerprivate.html#targetDetected

    Parameters
    ----------

    target : Optional[QNearFieldTarget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QNearFieldManagerPrivate::targetDetected(QNearFieldTarget
    #      *target)
    self.uglySide.call(
        'ritual_ZN24QNearFieldManagerPrivate14targetDetectedEP16QNearFieldT'
        'arget',
        self._addressOf(target),
    )

  @overload(QNearFieldTarget)
  @overload(NoneType)
  def targetLost(self, target: Optional[QNearFieldTarget]) -> None:
    """
    Calls Qt's 'void QNearFieldManagerPrivate::targetLost(QNearFieldTarget
    *target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnearfieldmanagerprivate.html#targetLost

    Parameters
    ----------

    target : Optional[QNearFieldTarget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QNearFieldManagerPrivate::targetLost(QNearFieldTarget *target)
    self.uglySide.call(
        'ritual_ZN24QNearFieldManagerPrivate10targetLostEP16QNearFieldTarge'
        't',
        self._addressOf(target),
    )
