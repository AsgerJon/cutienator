"""
QSctpServerPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qsctpserver_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSctpServerPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QTcpServerPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QSctpServer


class QSctpServerPrivate(QTcpServerPrivate):
  """
  The cute side of Qt's QSctpServerPrivate: a plain Python object standing in
  front of one C++ QSctpServerPrivate.

  It is built on the cute 'QTcpServerPrivate', as Qt's QSctpServerPrivate is
  built on Qt's QTcpServerPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSctpServerPrivate that has a ritual and that Python
  can call so far, 2 names in all: 'q_func', 'configureCreatedSocket'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QSctpServer *QSctpServerPrivate::q_func() const': takes in
    Python what 'QSctpServer *QSctpServerPrivate::q_func()' takes.
  - Qt's 'QSctpServerPrivate::~QSctpServerPrivate()': the destructor: Python
    never removes a C++ QSctpServerPrivate.

  What to expect
  --------------

  - The C++ QSctpServerPrivate is created at the first use, not by
    'QSctpServerPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSctpServerPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSctpServerPrivate'

  #  A C++ QSctpServerPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSctpServerPrivate'

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
    'QSctpServerPrivate::QSctpServerPrivate()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsctpserverprivate.html#QSctpServerPrivate
    """
    #  QSctpServerPrivate::QSctpServerPrivate()
    self._noteCreation(QSctpServerPrivate, lambda: Rituals.call(
        'ritual_ZN18QSctpServerPrivateC1Ev',
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

  def q_func(self) -> Optional[QSctpServer]:
    """
    Calls Qt's 'QSctpServer *QSctpServerPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qsctpserverprivate.html#q_func

    Returns
    -------

    Optional[QSctpServer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSctpServer *QSctpServerPrivate::q_func()
    address = self.uglySide.call('ritual_ZN18QSctpServerPrivate6q_funcEv')
    from . import QSctpServer
    return QSctpServer._cuteAt(address)

  def configureCreatedSocket(self) -> None:
    """
    Calls Qt's 'void QSctpServerPrivate::configureCreatedSocket()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsctpserverprivate.html#configureCreatedSocket
    """
    #  void QSctpServerPrivate::configureCreatedSocket()
    ritual = 'ritual_ZN18QSctpServerPrivate22configureCreatedSocketEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QSctpServerPrivate22configureCreatedSocketEv'
    self.uglySide.call(ritual)
