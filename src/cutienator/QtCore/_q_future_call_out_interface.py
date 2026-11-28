"""
QFutureCallOutInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qfutureinterface_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QFutureCallOutInterface to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QFutureCallOutInterface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QFutureCallOutInterface: a plain Python object
  standing in front of one C++ QFutureCallOutInterface.

  What exists
  -----------

  Every function of Qt's QFutureCallOutInterface that has a ritual and that
  Python can call so far, 1 name in all: 'callOutInterfaceDisconnected'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFutureCallOutInterface::~QFutureCallOutInterface()': the
    destructor: Python never removes a C++ QFutureCallOutInterface.
  - Qt's 'void QFutureCallOutInterface::postCallOutEvent(const
    QFutureCallOutEvent &a0)': takes a type Python has no way to hand over
    yet.

  What to expect
  --------------

  - The C++ QFutureCallOutInterface is created at the first use, not by
    'QFutureCallOutInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QFutureCallOutInterface.
  - Each name of Qt's QFutureCallOutInterface that has no cute function yet,
    'postCallOutEvent', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFutureCallOutInterface'

  #  A C++ QFutureCallOutInterface Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QFutureCallOutInterface'

  #  The functions Qt calls itself that QFutureCallOutInterface is the first
  #  to declare and that cannot be handed to Python yet, each as Qt declares
  #  it. A class of a program that writes one of them anew is refused, since
  #  Qt would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'postCallOutEvent': (
          'void QFutureCallOutInterface::postCallOutEvent(const '
          'QFutureCallOutEvent &)',
      ),
  }

  #  The functions Qt calls itself that QFutureCallOutInterface is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'callOutInterfaceDisconnected': (
          ('_ZN23QFutureCallOutInterface28callOutInterfaceDisconnectedEv',
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

  def callOutInterfaceDisconnected(self) -> None:
    """
    Calls Qt's 'void
    QFutureCallOutInterface::callOutInterfaceDisconnected()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfuturecalloutinterface.html
    """
    #  void QFutureCallOutInterface::callOutInterfaceDisconnected()
    self._callAs(
        'QFutureCallOutInterface',
        'ritual_ZN23QFutureCallOutInterface28callOutInterfaceDisconnectedEv',
    )

  @staticmethod
  def postCallOutEvent(*__, **_) -> Never:
    """
    Qt's 'void QFutureCallOutInterface::postCallOutEvent(const
    QFutureCallOutEvent &a0)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QFutureCallOutInterface.postCallOutEvent' has no cute function "
        "yet. Qt's 'void QFutureCallOutInterface::postCallOutEvent(const "
        "QFutureCallOutEvent &a0)': takes a type Python has no way to hand "
        "over yet.")
