"""
QGrpcHttp2Channel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGrpc/qgrpchttp2channel.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QAbstractGrpcChannel

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QUrl
  from . import QGrpcChannelOptions
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGrpcChannelOptions = WAIT['QGrpcChannelOptions']
  QUrl = WAIT['QUrl']


class QGrpcHttp2Channel(QAbstractGrpcChannel):
  """
  The cute side of Qt's QGrpcHttp2Channel: a plain Python object standing in
  front of one C++ QGrpcHttp2Channel.

  It is built on the cute 'QAbstractGrpcChannel', as Qt's QGrpcHttp2Channel
  is built on Qt's QAbstractGrpcChannel, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGrpcHttp2Channel that has a ritual and that Python
  can call so far, 1 name in all: 'hostUri'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGrpcHttp2Channel::~QGrpcHttp2Channel()': the destructor: Python
    never removes a C++ QGrpcHttp2Channel.
  - Qt's 'void QGrpcHttp2Channel::call(QGrpcOperationContext
    *operationContext, QByteArray &&messageData)': takes a type Python has no
    way to hand over yet.
  - Qt's 'void QGrpcHttp2Channel::serverStream(QGrpcOperationContext
    *operationContext, QByteArray &&messageData)': takes a type Python has no
    way to hand over yet.
  - Qt's 'void QGrpcHttp2Channel::clientStream(QGrpcOperationContext
    *operationContext, QByteArray &&messageData)': takes a type Python has no
    way to hand over yet.
  - Qt's 'void QGrpcHttp2Channel::bidiStream(QGrpcOperationContext
    *operationContext, QByteArray &&messageData)': takes a type Python has no
    way to hand over yet.
  - Qt's 'std::shared_ptr<QAbstractProtobufSerializer>
    QGrpcHttp2Channel::serializer() const': gives a type Python has no way to
    take yet.

  What has no ritual
  ------------------

  6 of the 15 functions Qt declares: 4 forbidden; 2 the compiler refuses its
  ritual as it would be written here.

  What to expect
  --------------

  - The C++ QGrpcHttp2Channel is created at the first use, not by
    'QGrpcHttp2Channel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGrpcHttp2Channel.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGrpcHttp2Channel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hostUri(self) -> QUrl:
    """
    Calls Qt's 'QUrl QGrpcHttp2Channel::hostUri() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgrpchttp2channel.html#hostUri

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QGrpcHttp2Channel::hostUri() const
    address = self.uglySide.call('ritual_ZNK17QGrpcHttp2Channel7hostUriEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

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

  @overload(QUrl)
  def __init__(self, hostUri: QUrl) -> None:
    """
    Notes what was given, for Qt's
    'QGrpcHttp2Channel::QGrpcHttp2Channel(const QUrl &hostUri)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpchttp2channel.html#QGrpcHttp2Channel

    Parameters
    ----------

    hostUri : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  QGrpcHttp2Channel::QGrpcHttp2Channel(const QUrl &hostUri)
    self._noteCreation(QGrpcHttp2Channel, lambda: Rituals.call(
        'ritual_ZN17QGrpcHttp2ChannelC1ERK4QUrl', self._valueOf(hostUri),
    ))

  @overload(QUrl, QGrpcChannelOptions)
  def __init__(self, hostUri: QUrl, options: QGrpcChannelOptions) -> None:
    """
    Notes what was given, for Qt's
    'QGrpcHttp2Channel::QGrpcHttp2Channel(const QUrl &hostUri, const
    QGrpcChannelOptions &options)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpchttp2channel.html#QGrpcHttp2Channel

    Parameters
    ----------

    hostUri : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    options : QGrpcChannelOptions
      Passed on as a value: Qt reads the C++ QGrpcChannelOptions, which stays
      Python's own.
    """
    #  QGrpcHttp2Channel::QGrpcHttp2Channel(const QUrl &hostUri, const
    #      QGrpcChannelOptions &options)
    self._noteCreation(QGrpcHttp2Channel, lambda: Rituals.call(
        'ritual_ZN17QGrpcHttp2ChannelC1ERK4QUrlRK19QGrpcChannelOptions',
        self._valueOf(hostUri), self._valueOf(options),
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
