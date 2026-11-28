"""
QCoapResourceDiscoveryReplyPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCoap/6.12.0/QtCoap/private/qcoapresourcediscoveryreply_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QCoapResourceDiscoveryReplyPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QtCoap, QCoapReplyPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray
  from ..QtNetwork import QHostAddress
  from . import QCoapMessage, QCoapResource, QCoapResourceDiscoveryReply
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QCoapMessage = WAIT['QCoapMessage']
  QHostAddress = WAIT['QHostAddress']


class QCoapResourceDiscoveryReplyPrivate(QCoapReplyPrivate):
  """
  The cute side of Qt's QCoapResourceDiscoveryReplyPrivate: a plain Python
  object standing in front of one C++ QCoapResourceDiscoveryReplyPrivate.

  It is built on the cute 'QCoapReplyPrivate', as Qt's
  QCoapResourceDiscoveryReplyPrivate is built on Qt's QCoapReplyPrivate, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QCoapResourceDiscoveryReplyPrivate that has a ritual
  and that Python can call so far, 3 names in all: '_q_setContent',
  'resourcesFromCoreLinkList', 'q_func'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QCoapResourceDiscoveryReply
    *QCoapResourceDiscoveryReplyPrivate::q_func() const': takes in Python
    what 'QCoapResourceDiscoveryReply
    *QCoapResourceDiscoveryReplyPrivate::q_func()' takes.

  What has no ritual
  ------------------

  1 of the 5 functions Qt declares: 1 leans on 'QCoapReplyPrivate.

  What to expect
  --------------

  - The C++ QCoapResourceDiscoveryReplyPrivate is created at the first use,
    not by 'QCoapResourceDiscoveryReplyPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCoapResourceDiscoveryReplyPrivate.
  - Each name of Qt's QCoapResourceDiscoveryReplyPrivate that has no cute
    function yet, '__init__', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QHostAddress, QByteArray)
  def resourcesFromCoreLinkList(
      sender: QHostAddress,
      data: QByteArray,
  ) -> QList[QCoapResource]:
    """
    Calls Qt's 'QList<QCoapResource>
    QCoapResourceDiscoveryReplyPrivate::resourcesFromCoreLinkList(const
    QHostAddress &sender, const QByteArray &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapresourcediscoveryreplyprivate.html

    Parameters
    ----------

    sender : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QList[QCoapResource]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QCoapResource>
    #      QCoapResourceDiscoveryReplyPrivate::resourcesFromCoreLinkList(
    #      const QHostAddress &sender, const QByteArray &data)
    address = Rituals.call(
        'ritual_ZN34QCoapResourceDiscoveryReplyPrivate25resourcesFromCoreLi'
        'nkListERK12QHostAddressRK10QByteArray',
        CuteMixin._valueOf(sender), CuteMixin._valueOf(data),
    )
    from . import QCoapResource
    return QList[QCoapResource]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCoapResourceDiscoveryReplyPrivate'

  #  A C++ QCoapResourceDiscoveryReplyPrivate Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCoapResourceDiscoveryReplyPrivate'

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
    Qt's
    'QCoapResourceDiscoveryReplyPrivate::QCoapResourceDiscoveryReplyPrivate(
    const QCoapRequest &request)': leans on
    'QCoapReplyPrivate::_q_setError(QtCoap::ResponseCode)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QCoapResourceDiscoveryReplyPrivate.__init__' has no cute function "
        "yet. Qt's "
        "'QCoapResourceDiscoveryReplyPrivate::QCoapResourceDiscoveryReplyPri"
        "vate(const QCoapRequest &request)': leans on "
        "'QCoapReplyPrivate::_q_setError(QtCoap::ResponseCode)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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

  @overload(QHostAddress, QCoapMessage, QtCoap.ResponseCode)
  def _q_setContent(
      self,
      sender: QHostAddress,
      a1: QCoapMessage,
      a2: QtCoap.ResponseCode,
  ) -> None:
    """
    Calls Qt's 'void QCoapResourceDiscoveryReplyPrivate::_q_setContent(const
    QHostAddress &sender, const QCoapMessage &a1, QtCoap::ResponseCode a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapresourcediscoveryreplyprivate.html

    Parameters
    ----------

    sender : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    a1 : QCoapMessage
      Passed on as a value: Qt reads the C++ QCoapMessage, which stays
      Python's own.

    a2 : QtCoap.ResponseCode
      Passed on as its number.
    """
    #  void QCoapResourceDiscoveryReplyPrivate::_q_setContent(const
    #      QHostAddress &sender, const QCoapMessage &a1, QtCoap::ResponseCode
    #      a2)
    self.uglySide.call(
        'ritual_ZN34QCoapResourceDiscoveryReplyPrivate13_q_setContentERK12Q'
        'HostAddressRK12QCoapMessageN6QtCoap12ResponseCodeE',
        self._valueOf(sender), self._valueOf(a1), a2.value,
    )

  def q_func(self) -> Optional[QCoapResourceDiscoveryReply]:
    """
    Calls Qt's 'QCoapResourceDiscoveryReply
    *QCoapResourceDiscoveryReplyPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapresourcediscoveryreplyprivate.html#q_func

    Returns
    -------

    Optional[QCoapResourceDiscoveryReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoapResourceDiscoveryReply
    #      *QCoapResourceDiscoveryReplyPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN34QCoapResourceDiscoveryReplyPrivate6q_funcEv',
    )
    from . import QCoapResourceDiscoveryReply
    return QCoapResourceDiscoveryReply._cuteAt(address)
