"""
QMetaCallEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qobject_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QMetaCallEvent to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QAbstractMetaCallEvent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMetaCallEvent(QAbstractMetaCallEvent):
  """
  The cute side of Qt's QMetaCallEvent: a plain Python object standing in
  front of one C++ QMetaCallEvent.

  It is built on the cute 'QAbstractMetaCallEvent', as Qt's QMetaCallEvent is
  built on Qt's QAbstractMetaCallEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QMetaCallEvent that has a ritual and that Python can
  call so far, 2 names in all: 'placeMetaCall', 'id'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMetaCallEvent::QMetaCallEvent(ushort method_offset, ushort
    method_relative, QObjectPrivate::StaticMetaCallFunction callFunction,
    const QObject *sender, int signalId, void **args, QLatch *latch)': takes
    a type Python has no way to hand over yet.
  - Qt's 'QMetaCallEvent::QMetaCallEvent(QtPrivate::QSlotObjectBase *slotObj,
    const QObject *sender, int signalId, void **args, QLatch *latch)': takes
    a type Python has no way to hand over yet.
  - Qt's 'QMetaCallEvent::QMetaCallEvent(const QObject *sender, int signalId,
    Data &&data)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  1 of the 6 functions Qt declares: 1 the compiler refuses its ritual as it
  would be written here.

  What to expect
  --------------

  - The C++ QMetaCallEvent is created at the first use, not by
    'QMetaCallEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMetaCallEvent.
  - Each name of Qt's QMetaCallEvent that has no cute function yet,
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
  __qt_class__ = 'QMetaCallEvent'

  #  A C++ QMetaCallEvent Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QMetaCallEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def id(self) -> int:
    """
    Calls Qt's 'int QMetaCallEvent::id() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetacallevent.html#id
    """
    #  int QMetaCallEvent::id() const
    return self.uglySide.call('ritual_ZNK14QMetaCallEvent2idEv')

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
    - Qt's 'QMetaCallEvent::QMetaCallEvent(ushort method_offset, ushort
      method_relative, QObjectPrivate::StaticMetaCallFunction callFunction,
      const QObject *sender, int signalId, void **args, QLatch *latch)':
      takes a type Python has no way to hand over yet.
    - Qt's 'QMetaCallEvent::QMetaCallEvent(QtPrivate::QSlotObjectBase
      *slotObj, const QObject *sender, int signalId, void **args, QLatch
      *latch)': takes a type Python has no way to hand over yet.
    - Qt's 'QMetaCallEvent::QMetaCallEvent(const QObject *sender, int
      signalId, Data &&data)': takes a type Python has no way to hand over
      yet.
    - Qt's 'QMetaCallEvent::QMetaCallEvent(QtPrivate::SlotObjUniquePtr
      slotObj, const QObject *sender, int signalId, void **args, QLatch
      *latch)': the compiler refuses its ritual as it would be written here:
      call to deleted constructor of 'QtPrivate::SlotObjUniquePtr' (aka
      'std::unique_ptr<QSlotObjectBase, QSlotObjectBase::Deleter>').
    """
    raise NotImplementedError(
        "'QMetaCallEvent.__init__' has no cute function yet. Qt's "
        "'QMetaCallEvent::QMetaCallEvent(ushort method_offset, ushort "
        "method_relative, QObjectPrivate::StaticMetaCallFunction "
        "callFunction, const QObject *sender, int signalId, void **args, "
        "QLatch *latch)': takes a type Python has no way to hand over yet. "
        "Qt's 'QMetaCallEvent::QMetaCallEvent(QtPrivate::QSlotObjectBase "
        "*slotObj, const QObject *sender, int signalId, void **args, QLatch "
        "*latch)': takes a type Python has no way to hand over yet. Qt's "
        "'QMetaCallEvent::QMetaCallEvent(const QObject *sender, int "
        "signalId, Data &&data)': takes a type Python has no way to hand "
        "over yet. Qt's "
        "'QMetaCallEvent::QMetaCallEvent(QtPrivate::SlotObjUniquePtr "
        "slotObj, const QObject *sender, int signalId, void **args, QLatch "
        "*latch)': the compiler refuses its ritual as it would be written "
        "here: call to deleted constructor of 'QtPrivate::SlotObjUniquePtr' "
        "(aka 'std::unique_ptr<QSlotObjectBase, QSlotObjectBase::Deleter>')."
    )

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

  @overload(QObject)
  @overload(NoneType)
  def placeMetaCall(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QMetaCallEvent::placeMetaCall(QObject *object)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetacallevent.html#placeMetaCall

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMetaCallEvent::placeMetaCall(QObject *object)
    ritual = 'ritual_ZN14QMetaCallEvent13placeMetaCallEP7QObject'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QMetaCallEvent13placeMetaCallEP7QObject'
    self.uglySide.call(ritual, self._addressOf(object, 'QObject'))
