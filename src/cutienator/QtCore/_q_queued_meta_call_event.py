"""
QQueuedMetaCallEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qobject_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QQueuedMetaCallEvent to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QMetaCallEvent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QMetaType
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaType = WAIT['QMetaType']


class QQueuedMetaCallEvent(QMetaCallEvent):
  """
  The cute side of Qt's QQueuedMetaCallEvent: a plain Python object standing
  in front of one C++ QQueuedMetaCallEvent.

  It is built on the cute 'QMetaCallEvent', as Qt's QQueuedMetaCallEvent is
  built on Qt's QMetaCallEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQueuedMetaCallEvent that has a ritual and that
  Python can call so far, 2 names in all: 'allocArgs', 'typeFitsInPlace'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQueuedMetaCallEvent::QQueuedMetaCallEvent(ushort method_offset,
    ushort method_relative, QObjectPrivate::StaticMetaCallFunction
    callFunction, const QObject *sender, int signalId, int argCount, const
    QtPrivate::QMetaTypeInterface *const *argTypes, const void *const
    *argValues)': takes a type Python has no way to hand over yet.
  - Qt's
    'QQueuedMetaCallEvent::QQueuedMetaCallEvent(QtPrivate::QSlotObjectBase
    *slotObj, const QObject *sender, int signalId, int argCount, const
    QtPrivate::QMetaTypeInterface *const *argTypes, const void *const
    *argValues)': names 'QtPrivate::QMetaTypeInterface *const', which has no
    cute class yet.
  - Qt's 'QQueuedMetaCallEvent::~QQueuedMetaCallEvent()': the destructor:
    Python never removes a C++ QQueuedMetaCallEvent.
  - Qt's 'void QQueuedMetaCallEvent::copyArgValues(int argCount, const
    QtPrivate::QMetaTypeInterface *const *argTypes, const void *const
    *argValues)': names 'QtPrivate::QMetaTypeInterface *const', which has no
    cute class yet.

  What has no ritual
  ------------------

  1 of the 7 functions Qt declares: 1 the compiler refuses its ritual as it
  would be written here.

  What to expect
  --------------

  - The C++ QQueuedMetaCallEvent is created at the first use, not by
    'QQueuedMetaCallEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQueuedMetaCallEvent.
  - Each name of Qt's QQueuedMetaCallEvent that has no cute function yet,
    '__init__', 'copyArgValues', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QMetaType)
  def typeFitsInPlace(type: QMetaType) -> bool:
    """
    Calls Qt's 'bool QQueuedMetaCallEvent::typeFitsInPlace(const QMetaType
    type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqueuedmetacallevent.html#typeFitsInPlace

    Parameters
    ----------

    type : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.
    """
    #  bool QQueuedMetaCallEvent::typeFitsInPlace(const QMetaType type)
    return Rituals.call(
        'ritual_ZN20QQueuedMetaCallEvent15typeFitsInPlaceE9QMetaType',
        CuteMixin._valueOf(type),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQueuedMetaCallEvent'

  #  A C++ QQueuedMetaCallEvent Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQueuedMetaCallEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    - Qt's 'QQueuedMetaCallEvent::QQueuedMetaCallEvent(ushort method_offset,
      ushort method_relative, QObjectPrivate::StaticMetaCallFunction
      callFunction, const QObject *sender, int signalId, int argCount, const
      QtPrivate::QMetaTypeInterface *const *argTypes, const void *const
      *argValues)': takes a type Python has no way to hand over yet.
    - Qt's
      'QQueuedMetaCallEvent::QQueuedMetaCallEvent(QtPrivate::QSlotObjectBase
      *slotObj, const QObject *sender, int signalId, int argCount, const
      QtPrivate::QMetaTypeInterface *const *argTypes, const void *const
      *argValues)': names 'QtPrivate::QMetaTypeInterface *const', which has
      no cute class yet.
    - Qt's
      'QQueuedMetaCallEvent::QQueuedMetaCallEvent(QtPrivate::SlotObjUniquePtr
      slotObj, const QObject *sender, int signalId, int argCount, const
      QtPrivate::QMetaTypeInterface *const *argTypes, const void *const
      *argValues)': the compiler refuses its ritual as it would be written
      here: call to deleted constructor of 'QtPrivate::SlotObjUniquePtr' (aka
      'std::unique_ptr<QSlotObjectBase, QSlotObjectBase::Deleter>').
    """
    raise NotImplementedError(
        "'QQueuedMetaCallEvent.__init__' has no cute function yet. Qt's "
        "'QQueuedMetaCallEvent::QQueuedMetaCallEvent(ushort method_offset, "
        "ushort method_relative, QObjectPrivate::StaticMetaCallFunction "
        "callFunction, const QObject *sender, int signalId, int argCount, "
        "const QtPrivate::QMetaTypeInterface *const *argTypes, const void "
        "*const *argValues)': takes a type Python has no way to hand over "
        "yet. Qt's "
        "'QQueuedMetaCallEvent::QQueuedMetaCallEvent(QtPrivate::QSlotObjectB"
        "ase *slotObj, const QObject *sender, int signalId, int argCount, "
        "const QtPrivate::QMetaTypeInterface *const *argTypes, const void "
        "*const *argValues)': names 'QtPrivate::QMetaTypeInterface *const', "
        "which has no cute class yet. Qt's "
        "'QQueuedMetaCallEvent::QQueuedMetaCallEvent(QtPrivate::SlotObjUniqu"
        "ePtr slotObj, const QObject *sender, int signalId, int argCount, "
        "const QtPrivate::QMetaTypeInterface *const *argTypes, const void "
        "*const *argValues)': the compiler refuses its ritual as it would "
        "be written here: call to deleted constructor of "
        "'QtPrivate::SlotObjUniquePtr' (aka "
        "'std::unique_ptr<QSlotObjectBase, QSlotObjectBase::Deleter>').")

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

  def allocArgs(self) -> None:
    """
    Calls Qt's 'void QQueuedMetaCallEvent::allocArgs()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqueuedmetacallevent.html#allocArgs
    """
    #  void QQueuedMetaCallEvent::allocArgs()
    self.uglySide.call('ritual_ZN20QQueuedMetaCallEvent9allocArgsEv')

  @staticmethod
  def copyArgValues(*__, **_) -> Never:
    """
    Qt's 'void QQueuedMetaCallEvent::copyArgValues(int argCount, const
    QtPrivate::QMetaTypeInterface *const *argTypes, const void *const
    *argValues)': names 'QtPrivate::QMetaTypeInterface *const', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QQueuedMetaCallEvent.copyArgValues' has no cute function yet. "
        "Qt's 'void QQueuedMetaCallEvent::copyArgValues(int argCount, const "
        "QtPrivate::QMetaTypeInterface *const *argTypes, const void *const "
        "*argValues)': names 'QtPrivate::QMetaTypeInterface *const', which "
        "has no cute class yet.")
