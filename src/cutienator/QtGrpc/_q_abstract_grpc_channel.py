"""
QAbstractGrpcChannel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGrpc/qabstractgrpcchannel.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QAbstractGrpcChannelPrivate, QGrpcChannelOptions
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGrpcChannelOptions = WAIT['QGrpcChannelOptions']


class QAbstractGrpcChannel(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QAbstractGrpcChannel: a plain Python object standing
  in front of one C++ QAbstractGrpcChannel.

  What exists
  -----------

  Every function of Qt's QAbstractGrpcChannel that has a ritual and that
  Python can call so far, 3 names in all: 'channelOptions',
  'setChannelOptions', 'd_func'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAbstractGrpcChannel::~QAbstractGrpcChannel()': the destructor:
    Python never removes a C++ QAbstractGrpcChannel.
  - Qt's 'std::shared_ptr<QAbstractProtobufSerializer>
    QAbstractGrpcChannel::serializer() const': gives a type Python has no way
    to take yet.
  - Qt's 'void QAbstractGrpcChannel::setChannelOptions(QGrpcChannelOptions
    &&options)': takes a type Python has no way to hand over yet.
  - Qt's 'const QGrpcInterceptorChain
    &QAbstractGrpcChannel::interceptorChain() const': gives a type Python has
    no way to take yet.
  - Qt's 'void QAbstractGrpcChannel::call(QGrpcOperationContext
    *operationContext, QByteArray &&messageData)': takes a type Python has no
    way to hand over yet.
  - Qt's 'void QAbstractGrpcChannel::serverStream(QGrpcOperationContext
    *operationContext, QByteArray &&messageData)': takes a type Python has no
    way to hand over yet.
  - Qt's 'void QAbstractGrpcChannel::clientStream(QGrpcOperationContext
    *operationContext, QByteArray &&messageData)': takes a type Python has no
    way to hand over yet.
  - Qt's 'void QAbstractGrpcChannel::bidiStream(QGrpcOperationContext
    *operationContext, QByteArray &&messageData)': takes a type Python has no
    way to hand over yet.
  - Qt's 'const QAbstractGrpcChannelPrivate *QAbstractGrpcChannel::d_func()
    const': takes in Python what 'QAbstractGrpcChannelPrivate
    *QAbstractGrpcChannel::d_func()' takes.

  What has no ritual
  ------------------

  11 of the 23 functions Qt declares: 6 forbidden; 5 the class is abstract,
  so C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QAbstractGrpcChannel is created at the first use, not by
    'QAbstractGrpcChannel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractGrpcChannel.
  - Each name of Qt's QAbstractGrpcChannel that has no cute function yet,
    '__init__', 'bidiStream', 'call', 'clientStream', 'interceptorChain',
    'serializer', 'serverStream', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractGrpcChannel'

  #  The functions Qt calls itself that QAbstractGrpcChannel is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'serializer': (
          'std::shared_ptr<QAbstractProtobufSerializer> '
          'QAbstractGrpcChannel::serializer() const',
      ),
      'call': (
          'void QAbstractGrpcChannel::call(QGrpcOperationContext *, '
          'QByteArray &&)',
      ),
      'serverStream': (
          'void QAbstractGrpcChannel::serverStream(QGrpcOperationContext '
          '*, QByteArray &&)',
      ),
      'clientStream': (
          'void QAbstractGrpcChannel::clientStream(QGrpcOperationContext '
          '*, QByteArray &&)',
      ),
      'bidiStream': (
          'void QAbstractGrpcChannel::bidiStream(QGrpcOperationContext *, '
          'QByteArray &&)',
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def channelOptions(self) -> QGrpcChannelOptions:
    """
    Calls Qt's 'const QGrpcChannelOptions
    &QAbstractGrpcChannel::channelOptions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractgrpcchannel.html#channelOptions

    Returns
    -------

    QGrpcChannelOptions
      A new cute QGrpcChannelOptions around the copy Qt gave back. Python
      owns it.
    """
    #  const QGrpcChannelOptions &QAbstractGrpcChannel::channelOptions()
    #      const
    address = self.uglySide.call(
        'ritual_ZNKR20QAbstractGrpcChannel14channelOptionsEv',
    )
    from . import QGrpcChannelOptions
    return QGrpcChannelOptions._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QGrpcChannelOptions)
  def setChannelOptions(self, options: QGrpcChannelOptions) -> None:
    """
    Calls Qt's 'void QAbstractGrpcChannel::setChannelOptions(const
    QGrpcChannelOptions &options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractgrpcchannel.html#setChannelOptions

    Parameters
    ----------

    options : QGrpcChannelOptions
      Passed on as a value: Qt reads the C++ QGrpcChannelOptions, which stays
      Python's own.
    """
    #  void QAbstractGrpcChannel::setChannelOptions(const QGrpcChannelOptions
    #      &options)
    self.uglySide.call(
        'ritual_ZN20QAbstractGrpcChannel17setChannelOptionsERK19QGrpcChanne'
        'lOptions',
        self._valueOf(options),
    )

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
    - Qt's 'QAbstractGrpcChannel::QAbstractGrpcChannel()': the class is
      abstract, so C++ cannot make one, and the C++ class of ours does not
      fill in every function it leaves open.
    - Qt's
      'QAbstractGrpcChannel::QAbstractGrpcChannel(QAbstractGrpcChannelPrivate
      &dd)': the class is abstract, so C++ cannot make one, and the C++ class
      of ours does not fill in every function it leaves open.
    - Qt's 'QAbstractGrpcChannel::QAbstractGrpcChannel(const
      QGrpcChannelOptions &options)': the class is abstract, so C++ cannot
      make one, and the C++ class of ours does not fill in every function it
      leaves open.
    - Qt's 'QAbstractGrpcChannel::QAbstractGrpcChannel(QGrpcInterceptorChain
      interceptorChain)': the class is abstract, so C++ cannot make one, and
      the C++ class of ours does not fill in every function it leaves open.
    - Qt's 'QAbstractGrpcChannel::QAbstractGrpcChannel(const
      QGrpcChannelOptions &options, QGrpcInterceptorChain interceptorChain)':
      the class is abstract, so C++ cannot make one, and the C++ class of
      ours does not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QAbstractGrpcChannel.__init__' has no cute function yet. Qt's "
        "'QAbstractGrpcChannel::QAbstractGrpcChannel()': the class is "
        "abstract, so C++ cannot make one, and the C++ class of ours does "
        "not fill in every function it leaves open. Qt's "
        "'QAbstractGrpcChannel::QAbstractGrpcChannel(QAbstractGrpcChannelPri"
        "vate &dd)': the class is abstract, so C++ cannot make one, and the "
        "C++ class of ours does not fill in every function it leaves open. "
        "Qt's 'QAbstractGrpcChannel::QAbstractGrpcChannel(const "
        "QGrpcChannelOptions &options)': the class is abstract, so C++ "
        "cannot make one, and the C++ class of ours does not fill in every "
        "function it leaves open. Qt's "
        "'QAbstractGrpcChannel::QAbstractGrpcChannel(QGrpcInterceptorChain "
        "interceptorChain)': the class is abstract, so C++ cannot make one, "
        "and the C++ class of ours does not fill in every function it "
        "leaves open. Qt's "
        "'QAbstractGrpcChannel::QAbstractGrpcChannel(const "
        "QGrpcChannelOptions &options, QGrpcInterceptorChain "
        "interceptorChain)': the class is abstract, so C++ cannot make one, "
        "and the C++ class of ours does not fill in every function it "
        "leaves open.")

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

  def d_func(self) -> Optional[QAbstractGrpcChannelPrivate]:
    """
    Calls Qt's 'QAbstractGrpcChannelPrivate *QAbstractGrpcChannel::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractgrpcchannel.html#d_func

    Returns
    -------

    Optional[QAbstractGrpcChannelPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractGrpcChannelPrivate *QAbstractGrpcChannel::d_func()
    address = self.uglySide.call('ritual_ZN20QAbstractGrpcChannel6d_funcEv')
    from . import QAbstractGrpcChannelPrivate
    return QAbstractGrpcChannelPrivate._cuteAt(address)

  @staticmethod
  def bidiStream(*__, **_) -> Never:
    """
    Qt's 'void QAbstractGrpcChannel::bidiStream(QGrpcOperationContext
    *operationContext, QByteArray &&messageData)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractGrpcChannel.bidiStream' has no cute function yet. Qt's "
        "'void QAbstractGrpcChannel::bidiStream(QGrpcOperationContext "
        "*operationContext, QByteArray &&messageData)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def call(*__, **_) -> Never:
    """
    Qt's 'void QAbstractGrpcChannel::call(QGrpcOperationContext
    *operationContext, QByteArray &&messageData)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractGrpcChannel.call' has no cute function yet. Qt's 'void "
        "QAbstractGrpcChannel::call(QGrpcOperationContext "
        "*operationContext, QByteArray &&messageData)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def clientStream(*__, **_) -> Never:
    """
    Qt's 'void QAbstractGrpcChannel::clientStream(QGrpcOperationContext
    *operationContext, QByteArray &&messageData)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractGrpcChannel.clientStream' has no cute function yet. Qt's "
        "'void QAbstractGrpcChannel::clientStream(QGrpcOperationContext "
        "*operationContext, QByteArray &&messageData)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def interceptorChain(*__, **_) -> Never:
    """
    Qt's 'const QGrpcInterceptorChain
    &QAbstractGrpcChannel::interceptorChain() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QAbstractGrpcChannel.interceptorChain' has no cute function yet. "
        "Qt's 'const QGrpcInterceptorChain "
        "&QAbstractGrpcChannel::interceptorChain() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def serializer(*__, **_) -> Never:
    """
    Qt's 'std::shared_ptr<QAbstractProtobufSerializer>
    QAbstractGrpcChannel::serializer() const': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'QAbstractGrpcChannel.serializer' has no cute function yet. Qt's "
        "'std::shared_ptr<QAbstractProtobufSerializer> "
        "QAbstractGrpcChannel::serializer() const': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def serverStream(*__, **_) -> Never:
    """
    Qt's 'void QAbstractGrpcChannel::serverStream(QGrpcOperationContext
    *operationContext, QByteArray &&messageData)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractGrpcChannel.serverStream' has no cute function yet. Qt's "
        "'void QAbstractGrpcChannel::serverStream(QGrpcOperationContext "
        "*operationContext, QByteArray &&messageData)': takes a type Python "
        "has no way to hand over yet.")
