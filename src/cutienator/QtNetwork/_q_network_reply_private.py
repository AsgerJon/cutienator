"""
QNetworkReplyPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qnetworkreply_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QNetworkReplyPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QIODevicePrivate
from . import QNetworkHeadersPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QNetworkAccessManager, QNetworkReply
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QNetworkAccessManager = WAIT['QNetworkAccessManager']
  QNetworkReply = WAIT['QNetworkReply']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QNetworkReplyPrivate(QIODevicePrivate, QNetworkHeadersPrivate):
  """
  The cute side of Qt's QNetworkReplyPrivate: a plain Python object standing
  in front of one C++ QNetworkReplyPrivate.

  It is built on the cute 'QIODevicePrivate', as Qt's QNetworkReplyPrivate is
  built on Qt's QIODevicePrivate, and has everything that class has. It is
  built on the cute 'QNetworkHeadersPrivate' as well, as Qt's
  QNetworkReplyPrivate is built on Qt's QNetworkHeadersPrivate too, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QNetworkReplyPrivate that has a ritual and that
  Python can call so far, 2 names in all: 'setManager', 'q_func'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QNetworkReply *QNetworkReplyPrivate::q_func() const': takes
    in Python what 'QNetworkReply *QNetworkReplyPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QNetworkReplyPrivate is created at the first use, not by
    'QNetworkReplyPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNetworkReplyPrivate.
  """

  #  The enums Qt writes inside QNetworkReplyPrivate, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class State(CuteNum):
    """
    The enum 'QNetworkReplyPrivate::State' of Qt, with the 5 names Qt gives
    in it.
    """

    Idle = Kee[int](0)
    Buffering = Kee[int](1)
    Working = Kee[int](2)
    Finished = Kee[int](3)
    Aborted = Kee[int](4)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QNetworkReply, QNetworkAccessManager)
  @overload(QNetworkReply, NoneType)
  @overload(NoneType, QNetworkAccessManager)
  @overload(NoneType, NoneType)
  def setManager(
      reply: Optional[QNetworkReply],
      manager: Optional[QNetworkAccessManager],
  ) -> None:
    """
    Calls Qt's 'void QNetworkReplyPrivate::setManager(QNetworkReply *reply,
    QNetworkAccessManager *manager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyprivate.html#setManager

    Parameters
    ----------

    reply : Optional[QNetworkReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    manager : Optional[QNetworkAccessManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QNetworkReplyPrivate::setManager(QNetworkReply *reply,
    #      QNetworkAccessManager *manager)
    Rituals.call(
        'ritual_ZN20QNetworkReplyPrivate10setManagerEP13QNetworkReplyP21QNe'
        'tworkAccessManager',
        CuteMixin._addressOf(reply), CuteMixin._addressOf(manager),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNetworkReplyPrivate'

  #  Qt's QNetworkReplyPrivate is built on more than one class. The part of a
  #  C++ QNetworkReplyPrivate that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QNetworkHeadersPrivate':
          'ritual_cast_QNetworkReplyPrivate_QNetworkHeadersPrivate',
  }

  #  A C++ QNetworkReplyPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNetworkReplyPrivate'

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
    'QNetworkReplyPrivate::QNetworkReplyPrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyprivate.html#QNetworkReplyPrivate
    """
    #  QNetworkReplyPrivate::QNetworkReplyPrivate()
    self._noteCreation(QNetworkReplyPrivate, lambda: Rituals.call(
        'ritual_ZN20QNetworkReplyPrivateC1Ev',
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

  def q_func(self) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QNetworkReplyPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreplyprivate.html#q_func

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QNetworkReplyPrivate::q_func()
    address = self.uglySide.call('ritual_ZN20QNetworkReplyPrivate6q_funcEv')
    from . import QNetworkReply
    return QNetworkReply._cuteAt(address)
