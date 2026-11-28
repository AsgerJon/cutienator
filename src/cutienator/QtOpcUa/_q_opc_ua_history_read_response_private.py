"""
QOpcUaHistoryReadResponsePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/6.12.0/QtOpcUa/private/qopcuahistoryreadresponse_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QOpcUaHistoryReadResponsePrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QOpcUaHistoryReadResponse, QOpcUaHistoryReadResponseImpl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpcUaHistoryReadResponseImpl = WAIT['QOpcUaHistoryReadResponseImpl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpcUaHistoryReadResponsePrivate(QObjectPrivate):
  """
  The cute side of Qt's QOpcUaHistoryReadResponsePrivate: a plain Python
  object standing in front of one C++ QOpcUaHistoryReadResponsePrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  QOpcUaHistoryReadResponsePrivate is built on Qt's QObjectPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QOpcUaHistoryReadResponsePrivate that has a ritual
  and that Python can call so far, 1 name in all: 'q_func'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QOpcUaHistoryReadResponse
    *QOpcUaHistoryReadResponsePrivate::q_func() const': takes in Python what
    'QOpcUaHistoryReadResponse *QOpcUaHistoryReadResponsePrivate::q_func()'
    takes.
  - Qt's
    'QOpcUaHistoryReadResponsePrivate::~QOpcUaHistoryReadResponsePrivate()':
    the destructor: Python never removes a C++
    QOpcUaHistoryReadResponsePrivate.

  What to expect
  --------------

  - The C++ QOpcUaHistoryReadResponsePrivate is created at the first use, not
    by 'QOpcUaHistoryReadResponsePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpcUaHistoryReadResponsePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaHistoryReadResponsePrivate'

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

  @overload(QOpcUaHistoryReadResponseImpl)
  @overload(NoneType)
  def __init__(self, impl: Optional[QOpcUaHistoryReadResponseImpl]) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaHistoryReadResponsePrivate::QOpcUaHistoryReadResponsePrivate(
    QOpcUaHistoryReadResponseImpl *impl)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadresponseprivate.html

    Parameters
    ----------

    impl : Optional[QOpcUaHistoryReadResponseImpl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QOpcUaHistoryReadResponsePrivate::
    #      QOpcUaHistoryReadResponsePrivate(QOpcUaHistoryReadResponseImpl
    #      *impl)
    self._noteCreation(
        QOpcUaHistoryReadResponsePrivate, lambda: Rituals.call(
            'ritual_ZN32QOpcUaHistoryReadResponsePrivateC1EP29QOpcUaHistory'
            'ReadResponseImpl',
            self._addressOf(impl),
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

  def q_func(self) -> Optional[QOpcUaHistoryReadResponse]:
    """
    Calls Qt's 'QOpcUaHistoryReadResponse
    *QOpcUaHistoryReadResponsePrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuahistoryreadresponseprivate.html#q_func

    Returns
    -------

    Optional[QOpcUaHistoryReadResponse]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpcUaHistoryReadResponse *QOpcUaHistoryReadResponsePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN32QOpcUaHistoryReadResponsePrivate6q_funcEv',
    )
    from . import QOpcUaHistoryReadResponse
    return QOpcUaHistoryReadResponse._cuteAt(address)
