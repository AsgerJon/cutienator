"""
QAbstractMetaCallEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qobject_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QAbstractMetaCallEvent to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QEvent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QLatch, QObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLatch = WAIT['QLatch']
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractMetaCallEvent(QEvent):
  """
  The cute side of Qt's QAbstractMetaCallEvent: a plain Python object
  standing in front of one C++ QAbstractMetaCallEvent.

  It is built on the cute 'QEvent', as Qt's QAbstractMetaCallEvent is built
  on Qt's QEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractMetaCallEvent that has a ritual and that
  Python can call so far, 3 names in all: 'placeMetaCall', 'sender',
  'signalId'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAbstractMetaCallEvent::~QAbstractMetaCallEvent()': the destructor:
    Python never removes a C++ QAbstractMetaCallEvent.

  What to expect
  --------------

  - The C++ QAbstractMetaCallEvent is created at the first use, not by
    'QAbstractMetaCallEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractMetaCallEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractMetaCallEvent'

  #  A C++ QAbstractMetaCallEvent Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractMetaCallEvent'

  #  The functions Qt calls itself that QAbstractMetaCallEvent is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'placeMetaCall': (
          ('_ZN22QAbstractMetaCallEvent13placeMetaCallEP7QObject',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
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

  def sender(self) -> Optional[QObject]:
    """
    Calls Qt's 'const QObject *QAbstractMetaCallEvent::sender() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractmetacallevent.html#sender

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QObject *QAbstractMetaCallEvent::sender() const
    address = self.uglySide.call(
        'ritual_ZNK22QAbstractMetaCallEvent6senderEv',
    )
    from . import QObject
    return QObject._cuteAt(address)

  def signalId(self) -> int:
    """
    Calls Qt's 'int QAbstractMetaCallEvent::signalId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractmetacallevent.html#signalId
    """
    #  int QAbstractMetaCallEvent::signalId() const
    return self.uglySide.call(
        'ritual_ZNK22QAbstractMetaCallEvent8signalIdEv',
    )

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

  @overload(QObject, int)
  @overload(NoneType, int)
  @overload(QObject, int, QLatch)
  @overload(QObject, int, NoneType)
  @overload(NoneType, int, QLatch)
  @overload(NoneType, int, NoneType)
  def __init__(
      self,
      sender: Optional[QObject],
      signalId: int,
      latch: Optional[QLatch] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QAbstractMetaCallEvent::QAbstractMetaCallEvent(const QObject *sender,
    int signalId, QLatch *latch)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractmetacallevent.html#QAbstractMetaCallEvent

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    signalId : int
      Passed on as it is.

    latch : Optional[QLatch]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QAbstractMetaCallEvent::QAbstractMetaCallEvent(const QObject *sender,
    #      int signalId, QLatch *latch)
    self._noteCreation(QAbstractMetaCallEvent, lambda: Rituals.call(
        'ritual_ZN22QAbstractMetaCallEventC1EPK7QObjectiP6QLatch',
        self._addressOf(sender, 'QObject'), signalId, self._addressOf(latch),
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

  @overload(QObject)
  @overload(NoneType)
  def placeMetaCall(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QAbstractMetaCallEvent::placeMetaCall(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractmetacallevent.html#placeMetaCall

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractMetaCallEvent::placeMetaCall(QObject *object)
    self.uglySide.call(
        'ritual_ZN22QAbstractMetaCallEvent13placeMetaCallEP7QObject',
        self._addressOf(object, 'QObject'),
    )
