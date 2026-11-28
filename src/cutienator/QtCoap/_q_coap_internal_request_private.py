"""
QCoapInternalRequestPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCoap/6.12.0/QtCoap/private/qcoapinternalrequest_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QCoapInternalRequestPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QCoapInternalMessagePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QCoapInternalRequest


class QCoapInternalRequestPrivate(QCoapInternalMessagePrivate):
  """
  The cute side of Qt's QCoapInternalRequestPrivate: a plain Python object
  standing in front of one C++ QCoapInternalRequestPrivate.

  It is built on the cute 'QCoapInternalMessagePrivate', as Qt's
  QCoapInternalRequestPrivate is built on Qt's QCoapInternalMessagePrivate,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCoapInternalRequestPrivate that has a ritual and
  that Python can call so far, 1 name in all: 'q_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QCoapInternalRequest *QCoapInternalRequestPrivate::q_func()
    const': takes in Python what 'QCoapInternalRequest
    *QCoapInternalRequestPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QCoapInternalRequestPrivate is created at the first use, not by
    'QCoapInternalRequestPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCoapInternalRequestPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCoapInternalRequestPrivate'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QCoapInternalRequestPrivate::QCoapInternalRequestPrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapinternalrequestprivate.html
    """
    #  QCoapInternalRequestPrivate::QCoapInternalRequestPrivate()
    self._noteCreation(QCoapInternalRequestPrivate, lambda: Rituals.call(
        'ritual_ZN27QCoapInternalRequestPrivateC1Ev',
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

  def q_func(self) -> Optional[QCoapInternalRequest]:
    """
    Calls Qt's 'QCoapInternalRequest *QCoapInternalRequestPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapinternalrequestprivate.html#q_func

    Returns
    -------

    Optional[QCoapInternalRequest]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoapInternalRequest *QCoapInternalRequestPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN27QCoapInternalRequestPrivate6q_funcEv',
    )
    from . import QCoapInternalRequest
    return QCoapInternalRequest._cuteAt(address)
