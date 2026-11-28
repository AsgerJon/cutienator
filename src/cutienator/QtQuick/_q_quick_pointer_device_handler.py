"""
QQuickPointerDeviceHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickpointerdevicehandler_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickPointerDeviceHandler to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtGui import QInputDevice, QPointingDevice
from . import QQuickPointerHandler

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QPointerEvent
  from . import QQuickItem, QQuickPointerDeviceHandlerPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointerEvent = WAIT['QPointerEvent']
  QQuickItem = WAIT['QQuickItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPointerDeviceHandler(QQuickPointerHandler):
  """
  The cute side of Qt's QQuickPointerDeviceHandler: a plain Python object
  standing in front of one C++ QQuickPointerDeviceHandler.

  It is built on the cute 'QQuickPointerHandler', as Qt's
  QQuickPointerDeviceHandler is built on Qt's QQuickPointerHandler, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPointerDeviceHandler that has a ritual and
  that Python can call so far, 16 names in all: 'metaObject', 'tr',
  'acceptedDevices', 'acceptedPointerTypes', 'acceptedButtons',
  'acceptedModifiers', 'setAcceptedDevices', 'setAcceptedPointerTypes',
  'setAcceptedButtons', 'setAcceptedModifiers', 'acceptedDevicesChanged',
  'acceptedPointerTypesChanged', 'acceptedButtonsChanged',
  'acceptedModifiersChanged', 'wantsPointerEvent', 'd_func'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickPointerDeviceHandler::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuickPointerDeviceHandler::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickPointerDeviceHandler::QQuickPointerDeviceHandler(
    QQuickPointerDeviceHandlerPrivate &dd, QQuickItem *parent)': takes a type
    Python has no way to hand over yet.
  - Qt's 'const QQuickPointerDeviceHandlerPrivate
    *QQuickPointerDeviceHandler::d_func() const': takes in Python what
    'QQuickPointerDeviceHandlerPrivate *QQuickPointerDeviceHandler::d_func()'
    takes.

  What has no ritual
  ------------------

  2 of the 23 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickPointerDeviceHandler is created at the first use, not by
    'QQuickPointerDeviceHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPointerDeviceHandler.
  - Qt tells when it has removed the C++ QQuickPointerDeviceHandler. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

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
    Calls Qt's 'QString QQuickPointerDeviceHandler::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpointerdevicehandler.html#tr

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
    #  QString QQuickPointerDeviceHandler::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN26QQuickPointerDeviceHandler2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPointerDeviceHandler'

  #  A C++ QQuickPointerDeviceHandler Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickPointerDeviceHandler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickPointerDeviceHandler::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerdevicehandler.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickPointerDeviceHandler::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuickPointerDeviceHandler10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def acceptedDevices(self) -> QInputDevice.DeviceTypes:
    """
    Calls Qt's 'QInputDevice::DeviceTypes
    QQuickPointerDeviceHandler::acceptedDevices() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerdevicehandler.html#acceptedDevices

    Returns
    -------

    QInputDevice.DeviceTypes
      The value standing for the combination Qt gave back.
    """
    #  QInputDevice::DeviceTypes
    #      QQuickPointerDeviceHandler::acceptedDevices() const
    return QInputDevice.DeviceTypes(self.uglySide.call(
        'ritual_ZNK26QQuickPointerDeviceHandler15acceptedDevicesEv',
    ))

  def acceptedPointerTypes(self) -> QPointingDevice.PointerTypes:
    """
    Calls Qt's 'QPointingDevice::PointerTypes
    QQuickPointerDeviceHandler::acceptedPointerTypes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerdevicehandler.html

    Returns
    -------

    QPointingDevice.PointerTypes
      The value standing for the combination Qt gave back.
    """
    #  QPointingDevice::PointerTypes
    #      QQuickPointerDeviceHandler::acceptedPointerTypes() const
    return QPointingDevice.PointerTypes(self.uglySide.call(
        'ritual_ZNK26QQuickPointerDeviceHandler20acceptedPointerTypesEv',
    ))

  def acceptedButtons(self) -> Qt.MouseButtons:
    """
    Calls Qt's 'Qt::MouseButtons
    QQuickPointerDeviceHandler::acceptedButtons() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerdevicehandler.html#acceptedButtons

    Returns
    -------

    Qt.MouseButtons
      The value standing for the combination Qt gave back.
    """
    #  Qt::MouseButtons QQuickPointerDeviceHandler::acceptedButtons() const
    return Qt.MouseButtons(self.uglySide.call(
        'ritual_ZNK26QQuickPointerDeviceHandler15acceptedButtonsEv',
    ))

  def acceptedModifiers(self) -> Qt.KeyboardModifiers:
    """
    Calls Qt's 'Qt::KeyboardModifiers
    QQuickPointerDeviceHandler::acceptedModifiers() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerdevicehandler.html#acceptedModifiers

    Returns
    -------

    Qt.KeyboardModifiers
      The value standing for the combination Qt gave back.
    """
    #  Qt::KeyboardModifiers QQuickPointerDeviceHandler::acceptedModifiers()
    #      const
    return Qt.KeyboardModifiers(self.uglySide.call(
        'ritual_ZNK26QQuickPointerDeviceHandler17acceptedModifiersEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QInputDevice.DeviceTypes)
  def setAcceptedDevices(
      self,
      acceptedDevices: QInputDevice.DeviceTypes,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickPointerDeviceHandler::setAcceptedDevices(QInputDevice::DeviceTypes
    acceptedDevices)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerdevicehandler.html#setAcceptedDevices

    Parameters
    ----------

    acceptedDevices : QInputDevice.DeviceTypes
      Passed on as its number.
    """
    #  void QQuickPointerDeviceHandler::setAcceptedDevices(QInputDevice::
    #      DeviceTypes acceptedDevices)
    self.uglySide.call(
        'ritual_ZN26QQuickPointerDeviceHandler18setAcceptedDevicesE6QFlagsI'
        'N12QInputDevice10DeviceTypeEE',
        acceptedDevices.value,
    )

  @overload(QPointingDevice.PointerTypes)
  def setAcceptedPointerTypes(
      self,
      acceptedPointerTypes: QPointingDevice.PointerTypes,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickPointerDeviceHandler::setAcceptedPointerTypes(QPointingDevice::
    PointerTypes acceptedPointerTypes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerdevicehandler.html

    Parameters
    ----------

    acceptedPointerTypes : QPointingDevice.PointerTypes
      Passed on as its number.
    """
    #  void QQuickPointerDeviceHandler::setAcceptedPointerTypes(
    #      QPointingDevice::PointerTypes acceptedPointerTypes)
    self.uglySide.call(
        'ritual_ZN26QQuickPointerDeviceHandler23setAcceptedPointerTypesE6QF'
        'lagsIN15QPointingDevice11PointerTypeEE',
        acceptedPointerTypes.value,
    )

  @overload(Qt.MouseButtons)
  def setAcceptedButtons(self, buttons: Qt.MouseButtons) -> None:
    """
    Calls Qt's 'void
    QQuickPointerDeviceHandler::setAcceptedButtons(Qt::MouseButtons
    buttons)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerdevicehandler.html#setAcceptedButtons

    Parameters
    ----------

    buttons : Qt.MouseButtons
      Passed on as its number.
    """
    #  void QQuickPointerDeviceHandler::setAcceptedButtons(Qt::MouseButtons
    #      buttons)
    self.uglySide.call(
        'ritual_ZN26QQuickPointerDeviceHandler18setAcceptedButtonsE6QFlagsI'
        'N2Qt11MouseButtonEE',
        buttons.value,
    )

  @overload(Qt.KeyboardModifiers)
  def setAcceptedModifiers(
      self,
      acceptedModifiers: Qt.KeyboardModifiers,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickPointerDeviceHandler::setAcceptedModifiers(Qt::KeyboardModifiers
    acceptedModifiers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerdevicehandler.html

    Parameters
    ----------

    acceptedModifiers : Qt.KeyboardModifiers
      Passed on as its number.
    """
    #  void QQuickPointerDeviceHandler::setAcceptedModifiers(Qt::
    #      KeyboardModifiers acceptedModifiers)
    self.uglySide.call(
        'ritual_ZN26QQuickPointerDeviceHandler20setAcceptedModifiersE6QFlag'
        'sIN2Qt16KeyboardModifierEE',
        acceptedModifiers.value,
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickPointerDeviceHandler::QQuickPointerDeviceHandler(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerdevicehandler.html

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickPointerDeviceHandler::QQuickPointerDeviceHandler(QQuickItem
    #      *parent)
    self._noteCreation(QQuickPointerDeviceHandler, lambda: Rituals.call(
        'ritual_ZN26QQuickPointerDeviceHandlerC1EP10QQuickItem',
        self._addressOf(parent),
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

  def acceptedDevicesChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPointerDeviceHandler::acceptedDevicesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerdevicehandler.html
    """
    #  void QQuickPointerDeviceHandler::acceptedDevicesChanged()
    self.uglySide.call(
        'ritual_ZN26QQuickPointerDeviceHandler22acceptedDevicesChangedEv',
    )

  def acceptedPointerTypesChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickPointerDeviceHandler::acceptedPointerTypesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerdevicehandler.html
    """
    #  void QQuickPointerDeviceHandler::acceptedPointerTypesChanged()
    self.uglySide.call(
        'ritual_ZN26QQuickPointerDeviceHandler27acceptedPointerTypesChanged'
        'Ev',
    )

  def acceptedButtonsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPointerDeviceHandler::acceptedButtonsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerdevicehandler.html
    """
    #  void QQuickPointerDeviceHandler::acceptedButtonsChanged()
    self.uglySide.call(
        'ritual_ZN26QQuickPointerDeviceHandler22acceptedButtonsChangedEv',
    )

  def acceptedModifiersChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPointerDeviceHandler::acceptedModifiersChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerdevicehandler.html
    """
    #  void QQuickPointerDeviceHandler::acceptedModifiersChanged()
    self.uglySide.call(
        'ritual_ZN26QQuickPointerDeviceHandler24acceptedModifiersChangedEv',
    )

  @overload(QPointerEvent)
  @overload(NoneType)
  def wantsPointerEvent(self, event: Optional[QPointerEvent]) -> bool:
    """
    Calls Qt's 'bool
    QQuickPointerDeviceHandler::wantsPointerEvent(QPointerEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerdevicehandler.html#wantsPointerEvent

    Parameters
    ----------

    event : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickPointerDeviceHandler::wantsPointerEvent(QPointerEvent
    #      *event)
    ritual = (
        'ritual_ZN26QQuickPointerDeviceHandler17wantsPointerEventEP13QPoint'
        'erEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QQuickPointerDeviceHandler17wantsPointerEventEP13'
          'QPointerEvent')
    return self.uglySide.call(ritual, self._addressOf(event))

  def d_func(self) -> Optional[QQuickPointerDeviceHandlerPrivate]:
    """
    Calls Qt's 'QQuickPointerDeviceHandlerPrivate
    *QQuickPointerDeviceHandler::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointerdevicehandler.html#d_func

    Returns
    -------

    Optional[QQuickPointerDeviceHandlerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPointerDeviceHandlerPrivate
    #      *QQuickPointerDeviceHandler::d_func()
    address = self.uglySide.call(
        'ritual_ZN26QQuickPointerDeviceHandler6d_funcEv',
    )
    from . import QQuickPointerDeviceHandlerPrivate
    return QQuickPointerDeviceHandlerPrivate._cuteAt(address)
