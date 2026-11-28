"""
QSpiApplicationAdaptor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qspiapplicationadaptor_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSpiApplicationAdaptor to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject
  from . import QKeyEvent
  from ..QtDBus import QDBusError, QDBusMessage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDBusError = WAIT['QDBusError']
  QDBusMessage = WAIT['QDBusMessage']
  QEvent = WAIT['QEvent']
  QKeyEvent = WAIT['QKeyEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSpiApplicationAdaptor(QObject):
  """
  The cute side of Qt's QSpiApplicationAdaptor: a plain Python object
  standing in front of one C++ QSpiApplicationAdaptor.

  It is built on the cute 'QObject', as Qt's QSpiApplicationAdaptor is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSpiApplicationAdaptor that has a ritual and that
  Python can call so far, 7 names in all: 'metaObject', 'sendEvents',
  'windowActivated', 'eventFilter', 'notifyKeyboardListenerCallback',
  'notifyKeyboardListenerError', 'copyKeyEvent'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSpiApplicationAdaptor::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QSpiApplicationAdaptor::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QSpiApplicationAdaptor::~QSpiApplicationAdaptor()': the destructor:
    Python never removes a C++ QSpiApplicationAdaptor.

  What has no ritual
  ------------------

  4 of the 14 functions Qt declares: 2 not a gap; 2 leans on
  'QSpiApplicationAdaptor.

  What to expect
  --------------

  - The C++ QSpiApplicationAdaptor is created at the first use, not by
    'QSpiApplicationAdaptor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSpiApplicationAdaptor.
  - Qt tells when it has removed the C++ QSpiApplicationAdaptor. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QSpiApplicationAdaptor that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QKeyEvent)
  @overload(NoneType)
  def copyKeyEvent(a0: Optional[QKeyEvent]) -> Optional[QKeyEvent]:
    """
    Calls Qt's 'QKeyEvent *QSpiApplicationAdaptor::copyKeyEvent(QKeyEvent
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspiapplicationadaptor.html#copyKeyEvent

    Parameters
    ----------

    a0 : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QKeyEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QKeyEvent *QSpiApplicationAdaptor::copyKeyEvent(QKeyEvent *a0)
    address = Rituals.call(
        'ritual_ZN22QSpiApplicationAdaptor12copyKeyEventEP9QKeyEvent',
        CuteMixin._addressOf(a0),
    )
    from . import QKeyEvent
    return QKeyEvent._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSpiApplicationAdaptor'

  #  A C++ QSpiApplicationAdaptor Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSpiApplicationAdaptor'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSpiApplicationAdaptor::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspiapplicationadaptor.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSpiApplicationAdaptor::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QSpiApplicationAdaptor10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Qt's 'QSpiApplicationAdaptor::QSpiApplicationAdaptor(const
    QDBusConnection &connection, QObject *parent)': leans on
    'QSpiApplicationAdaptor::qt_metacall(QMetaObject::Call, int, void**)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QSpiApplicationAdaptor.__init__' has no cute function yet. Qt's "
        "'QSpiApplicationAdaptor::QSpiApplicationAdaptor(const "
        "QDBusConnection &connection, QObject *parent)': leans on "
        "'QSpiApplicationAdaptor::qt_metacall(QMetaObject::Call, int, "
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

  @overload(bool)
  def sendEvents(self, active: bool) -> None:
    """
    Calls Qt's 'void QSpiApplicationAdaptor::sendEvents(bool active)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspiapplicationadaptor.html#sendEvents

    Parameters
    ----------

    active : bool
      Passed on as it is.
    """
    #  void QSpiApplicationAdaptor::sendEvents(bool active)
    self.uglySide.call(
        'ritual_ZN22QSpiApplicationAdaptor10sendEventsEb', active,
    )

  @overload(QObject, bool)
  @overload(NoneType, bool)
  def windowActivated(self, window: Optional[QObject], active: bool) -> None:
    """
    Calls Qt's 'void QSpiApplicationAdaptor::windowActivated(QObject *window,
    bool active)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspiapplicationadaptor.html#windowActivated

    Parameters
    ----------

    window : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    active : bool
      Passed on as it is.
    """
    #  void QSpiApplicationAdaptor::windowActivated(QObject *window, bool
    #      active)
    self.uglySide.call(
        'ritual_ZN22QSpiApplicationAdaptor15windowActivatedEP7QObjectb',
        self._addressOf(window, 'QObject'), active,
    )

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def eventFilter(
      self,
      obj: Optional[QObject],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QSpiApplicationAdaptor::eventFilter(QObject *obj, QEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspiapplicationadaptor.html#eventFilter

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSpiApplicationAdaptor::eventFilter(QObject *obj, QEvent *event)
    return self.uglySide.call(
        'ritual_ZN22QSpiApplicationAdaptor11eventFilterEP7QObjectP6QEvent',
        self._addressOf(obj, 'QObject'), self._addressOf(event),
    )

  @overload(QDBusMessage)
  def notifyKeyboardListenerCallback(self, message: QDBusMessage) -> None:
    """
    Calls Qt's 'void
    QSpiApplicationAdaptor::notifyKeyboardListenerCallback(const QDBusMessage
    &message)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspiapplicationadaptor.html

    Parameters
    ----------

    message : QDBusMessage
      Passed on as a value: Qt reads the C++ QDBusMessage, which stays
      Python's own.
    """
    #  void QSpiApplicationAdaptor::notifyKeyboardListenerCallback(const
    #      QDBusMessage &message)
    self.uglySide.call(
        'ritual_ZN22QSpiApplicationAdaptor30notifyKeyboardListenerCallbackE'
        'RK12QDBusMessage',
        self._valueOf(message),
    )

  @overload(QDBusError, QDBusMessage)
  def notifyKeyboardListenerError(
      self,
      error: QDBusError,
      message: QDBusMessage,
  ) -> None:
    """
    Calls Qt's 'void
    QSpiApplicationAdaptor::notifyKeyboardListenerError(const QDBusError
    &error, const QDBusMessage &message)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspiapplicationadaptor.html

    Parameters
    ----------

    error : QDBusError
      Passed on as a value: Qt reads the C++ QDBusError, which stays Python's
      own.

    message : QDBusMessage
      Passed on as a value: Qt reads the C++ QDBusMessage, which stays
      Python's own.
    """
    #  void QSpiApplicationAdaptor::notifyKeyboardListenerError(const
    #      QDBusError &error, const QDBusMessage &message)
    self.uglySide.call(
        'ritual_ZN22QSpiApplicationAdaptor27notifyKeyboardListenerErrorERK1'
        '0QDBusErrorRK12QDBusMessage',
        self._valueOf(error), self._valueOf(message),
    )
