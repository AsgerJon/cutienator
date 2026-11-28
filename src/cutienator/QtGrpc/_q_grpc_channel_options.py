"""
QGrpcChannelOptions binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGrpc/qgrpcchanneloptions.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QtGrpc

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QDebug
  from . import QGrpcSerializationFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDebug = WAIT['QDebug']


class QGrpcChannelOptions(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGrpcChannelOptions: a plain Python object standing
  in front of one C++ QGrpcChannelOptions.

  C++ hands a QGrpcChannelOptions around as a copy, so every C++
  QGrpcChannelOptions behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGrpcChannelOptions that has a ritual and that
  Python can call so far, 6 names in all: 'supportedCompressionAlgorithms',
  'acceptedCompressionAlgorithms', 'serializationFormat', '__eq__', '__ne__',
  '__rlshift__'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGrpcChannelOptions::~QGrpcChannelOptions()': the destructor:
    Python removes its C++ QGrpcChannelOptions by it, and has no other use
    for it.
  - Qt's 'QGrpcChannelOptions &QGrpcChannelOptions::operator=(const
    QGrpcChannelOptions &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QGrpcChannelOptions::QGrpcChannelOptions(QGrpcChannelOptions
    &&other)': takes a type Python has no way to hand over yet.
  - Qt's 'QGrpcChannelOptions
    &QGrpcChannelOptions::operator=(QGrpcChannelOptions &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QVariant QGrpcChannelOptions::operator QVariant() const': an
    operator Python has no name for.
  - Qt's 'void QGrpcChannelOptions::swap(QGrpcChannelOptions &other)': takes
    a type Python has no way to hand over yet.
  - Qt's 'std::optional<std::chrono::milliseconds>
    QGrpcChannelOptions::deadlineTimeout() const': gives a type Python has no
    way to take yet.
  - Qt's 'QGrpcChannelOptions
    &QGrpcChannelOptions::setDeadlineTimeout(std::chrono::milliseconds
    timeout)': takes a type Python has no way to hand over yet.
  - Qt's 'const QHash<QByteArray, QByteArray>
    &QGrpcChannelOptions::metadata() const': gives a type Python has no way
    to take yet.
  - Qt's 'QGrpcChannelOptions &QGrpcChannelOptions::setMetadata(const
    QHash<QByteArray, QByteArray> &metadata)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QGrpcChannelOptions
    &QGrpcChannelOptions::setMetadata(QHash<QByteArray, QByteArray>
    &&metadata)': takes a type Python has no way to hand over yet.
  - Qt's 'const QMultiHash<QByteArray, QByteArray>
    &QGrpcChannelOptions::metadata(QtGrpc::MultiValue_t a0) const': gives a
    type Python has no way to take yet.
  - Qt's 'QGrpcChannelOptions &QGrpcChannelOptions::setMetadata(const
    QMultiHash<QByteArray, QByteArray> &metadata)': takes a type Python has
    no way to hand over yet.
  - Qt's 'QGrpcChannelOptions
    &QGrpcChannelOptions::setMetadata(QMultiHash<QByteArray, QByteArray>
    &&metadata)': takes a type Python has no way to hand over yet.
  - Qt's 'QGrpcChannelOptions
    &QGrpcChannelOptions::setMetadata(std::initializer_list<std::
    pair<QByteArray, QByteArray>> list)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QGrpcChannelOptions
    &QGrpcChannelOptions::addMetadata(QByteArrayView key, QByteArrayView
    value)': gives a type Python has no way to take yet.
  - Qt's 'std::optional<bool> QGrpcChannelOptions::filterServerMetadata()
    const': gives a type Python has no way to take yet.
  - Qt's 'QGrpcChannelOptions
    &QGrpcChannelOptions::setFilterServerMetadata(bool value)': gives a type
    Python has no way to take yet.
  - Qt's 'std::optional<quint64>
    QGrpcChannelOptions::maximumReceiveMessageSize() const': gives a type
    Python has no way to take yet.
  - Qt's 'QGrpcChannelOptions
    &QGrpcChannelOptions::setMaximumReceiveMessageSize(quint64 size)': gives
    a type Python has no way to take yet.
  - Qt's 'std::optional<QtGrpc::CompressionAlgorithm>
    QGrpcChannelOptions::requestCompression() const': gives a type Python has
    no way to take yet.
  - Qt's 'QGrpcChannelOptions
    &QGrpcChannelOptions::setRequestCompression(QtGrpc::CompressionAlgorithm
    algorithm)': gives a type Python has no way to take yet.
  - Qt's 'QGrpcChannelOptions
    &QGrpcChannelOptions::setAcceptedCompressionAlgorithms(QtGrpc::
    CompressionAlgorithms algorithms)': gives a type Python has no way to
    take yet.
  - Qt's 'QGrpcChannelOptions
    &QGrpcChannelOptions::setSerializationFormat(const
    QGrpcSerializationFormat &format)': gives a type Python has no way to
    take yet.
  - Qt's 'std::optional<QSslConfiguration>
    QGrpcChannelOptions::sslConfiguration() const': gives a type Python has
    no way to take yet.
  - Qt's 'QGrpcChannelOptions &QGrpcChannelOptions::setSslConfiguration(const
    QSslConfiguration &sslConfiguration)': gives a type Python has no way to
    take yet.
  - Qt's 'QGrpcChannelOptionsPrivate *QGrpcChannelOptions::d_func()': gives
    'QGrpcChannelOptionsPrivate', which has no cute class yet.
  - Qt's 'const QGrpcChannelOptionsPrivate *QGrpcChannelOptions::d_func()
    const': gives 'QGrpcChannelOptionsPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 40 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QGrpcChannelOptions is created at the first use, not by
    'QGrpcChannelOptions(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGrpcChannelOptions back gives a copy the ritual made
    for Python, in a new cute QGrpcChannelOptions.
  - Each name of Qt's QGrpcChannelOptions that has no cute function yet,
    'addMetadata', 'd_func', 'deadlineTimeout', 'filterServerMetadata',
    'maximumReceiveMessageSize', 'metadata', 'requestCompression',
    'setAcceptedCompressionAlgorithms', 'setDeadlineTimeout',
    'setFilterServerMetadata', 'setMaximumReceiveMessageSize', 'setMetadata',
    'setRequestCompression', 'setSerializationFormat', 'setSslConfiguration',
    'sslConfiguration', 'swap', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def supportedCompressionAlgorithms() -> QtGrpc.CompressionAlgorithms:
    """
    Calls Qt's 'QtGrpc::CompressionAlgorithms
    QGrpcChannelOptions::supportedCompressionAlgorithms()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpcchanneloptions.html

    Returns
    -------

    QtGrpc.CompressionAlgorithms
      The value standing for the combination Qt gave back.
    """
    #  QtGrpc::CompressionAlgorithms
    #      QGrpcChannelOptions::supportedCompressionAlgorithms()
    return QtGrpc.CompressionAlgorithms(Rituals.call(
        'ritual_ZN19QGrpcChannelOptions30supportedCompressionAlgorithmsEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGrpcChannelOptions'

  #  Qt's '~QGrpcChannelOptions()'. Naming it makes this a value class:
  #  Python owns every C++ QGrpcChannelOptions behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QGrpcChannelOptionsD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def acceptedCompressionAlgorithms(self) -> QtGrpc.CompressionAlgorithms:
    """
    Calls Qt's 'QtGrpc::CompressionAlgorithms
    QGrpcChannelOptions::acceptedCompressionAlgorithms() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpcchanneloptions.html

    Returns
    -------

    QtGrpc.CompressionAlgorithms
      The value standing for the combination Qt gave back.
    """
    #  QtGrpc::CompressionAlgorithms
    #      QGrpcChannelOptions::acceptedCompressionAlgorithms() const
    return QtGrpc.CompressionAlgorithms(self.uglySide.call(
        'ritual_ZNK19QGrpcChannelOptions29acceptedCompressionAlgorithmsEv',
    ))

  def serializationFormat(self) -> QGrpcSerializationFormat:
    """
    Calls Qt's 'QGrpcSerializationFormat
    QGrpcChannelOptions::serializationFormat() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpcchanneloptions.html#serializationFormat

    Returns
    -------

    QGrpcSerializationFormat
      A new cute QGrpcSerializationFormat around the copy Qt gave back.
      Python owns it.
    """
    #  QGrpcSerializationFormat QGrpcChannelOptions::serializationFormat()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK19QGrpcChannelOptions19serializationFormatEv',
    )
    from . import QGrpcSerializationFormat
    return QGrpcSerializationFormat._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QGrpcChannelOptions) -> bool:
    """
    Calls Qt's 'bool operator==(const QGrpcChannelOptions &lhs, const
    QGrpcChannelOptions &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpcchanneloptions.html#operator==

    Parameters
    ----------

    rhs : QGrpcChannelOptions
      Passed on as a value: Qt reads the C++ QGrpcChannelOptions, which stays
      Python's own.
    """
    #  bool operator==(const QGrpcChannelOptions &lhs, const
    #      QGrpcChannelOptions &rhs)
    return Rituals.call(
        'ritual_ZeqRK19QGrpcChannelOptionsS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: QGrpcChannelOptions) -> bool:
    """
    Calls Qt's 'bool operator!=(const QGrpcChannelOptions &lhs, const
    QGrpcChannelOptions &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpcchanneloptions.html#operator!=

    Parameters
    ----------

    rhs : QGrpcChannelOptions
      Passed on as a value: Qt reads the C++ QGrpcChannelOptions, which stays
      Python's own.
    """
    #  bool operator!=(const QGrpcChannelOptions &lhs, const
    #      QGrpcChannelOptions &rhs)
    return Rituals.call(
        'ritual_ZneRK19QGrpcChannelOptionsS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(QDebug)
  def __rlshift__(self, debug: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug debug, const QGrpcChannelOptions
    &chOpts)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpcchanneloptions.html#operator<<

    Parameters
    ----------

    debug : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug debug, const QGrpcChannelOptions &chOpts)
    address = Rituals.call(
        'ritual_Zls6QDebugRK19QGrpcChannelOptions',
        CuteMixin._valueOf(debug), CuteMixin._valueOf(self),
    )
    from ..QtCore import QDebug
    return QDebug._cuteOwning(address)

  @overload.fallback
  def __rlshift__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QGrpcChannelOptions::QGrpcChannelOptions()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpcchanneloptions.html#QGrpcChannelOptions
    """
    #  QGrpcChannelOptions::QGrpcChannelOptions()
    self._noteCreation(QGrpcChannelOptions, lambda: Rituals.call(
        'ritual_ZN19QGrpcChannelOptionsC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QGrpcChannelOptions) -> None:
    """
    Notes what was given, for Qt's
    'QGrpcChannelOptions::QGrpcChannelOptions(const QGrpcChannelOptions
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpcchanneloptions.html#QGrpcChannelOptions

    Parameters
    ----------

    other : QGrpcChannelOptions
      Passed on as a value: Qt reads the C++ QGrpcChannelOptions, which stays
      Python's own.
    """
    #  QGrpcChannelOptions::QGrpcChannelOptions(const QGrpcChannelOptions
    #      &other)
    self._noteCreation(QGrpcChannelOptions, lambda: Rituals.call(
        'ritual_ZN19QGrpcChannelOptionsC1ERKS_', self._valueOf(other),
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

  @staticmethod
  def addMetadata(*__, **_) -> Never:
    """
    Qt's 'QGrpcChannelOptions
    &QGrpcChannelOptions::addMetadata(QByteArrayView key, QByteArrayView
    value)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGrpcChannelOptions.addMetadata' has no cute function yet. Qt's "
        "'QGrpcChannelOptions "
        "&QGrpcChannelOptions::addMetadata(QByteArrayView key, "
        "QByteArrayView value)': gives a type Python has no way to take yet."
    )

  @staticmethod
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'QGrpcChannelOptionsPrivate *QGrpcChannelOptions::d_func()': gives
      'QGrpcChannelOptionsPrivate', which has no cute class yet.
    - Qt's 'const QGrpcChannelOptionsPrivate *QGrpcChannelOptions::d_func()
      const': gives 'QGrpcChannelOptionsPrivate', which has no cute class
      yet.
    """
    raise NotImplementedError(
        "'QGrpcChannelOptions.d_func' has no cute function yet. Qt's "
        "'QGrpcChannelOptionsPrivate *QGrpcChannelOptions::d_func()': gives "
        "'QGrpcChannelOptionsPrivate', which has no cute class yet. Qt's "
        "'const QGrpcChannelOptionsPrivate *QGrpcChannelOptions::d_func() "
        "const': gives 'QGrpcChannelOptionsPrivate', which has no cute "
        "class yet.")

  @staticmethod
  def deadlineTimeout(*__, **_) -> Never:
    """
    Qt's 'std::optional<std::chrono::milliseconds>
    QGrpcChannelOptions::deadlineTimeout() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QGrpcChannelOptions.deadlineTimeout' has no cute function yet. "
        "Qt's 'std::optional<std::chrono::milliseconds> "
        "QGrpcChannelOptions::deadlineTimeout() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def filterServerMetadata(*__, **_) -> Never:
    """
    Qt's 'std::optional<bool> QGrpcChannelOptions::filterServerMetadata()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGrpcChannelOptions.filterServerMetadata' has no cute function "
        "yet. Qt's 'std::optional<bool> "
        "QGrpcChannelOptions::filterServerMetadata() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def maximumReceiveMessageSize(*__, **_) -> Never:
    """
    Qt's 'std::optional<quint64>
    QGrpcChannelOptions::maximumReceiveMessageSize() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGrpcChannelOptions.maximumReceiveMessageSize' has no cute "
        "function yet. Qt's 'std::optional<quint64> "
        "QGrpcChannelOptions::maximumReceiveMessageSize() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def metadata(*__, **_) -> Never:
    """
    - Qt's 'const QHash<QByteArray, QByteArray>
      &QGrpcChannelOptions::metadata() const': gives a type Python has no way
      to take yet.
    - Qt's 'const QMultiHash<QByteArray, QByteArray>
      &QGrpcChannelOptions::metadata(QtGrpc::MultiValue_t a0) const': gives a
      type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGrpcChannelOptions.metadata' has no cute function yet. Qt's "
        "'const QHash<QByteArray, QByteArray> "
        "&QGrpcChannelOptions::metadata() const': gives a type Python has "
        "no way to take yet. Qt's 'const QMultiHash<QByteArray, QByteArray> "
        "&QGrpcChannelOptions::metadata(QtGrpc::MultiValue_t a0) const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def requestCompression(*__, **_) -> Never:
    """
    Qt's 'std::optional<QtGrpc::CompressionAlgorithm>
    QGrpcChannelOptions::requestCompression() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QGrpcChannelOptions.requestCompression' has no cute function yet. "
        "Qt's 'std::optional<QtGrpc::CompressionAlgorithm> "
        "QGrpcChannelOptions::requestCompression() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def setAcceptedCompressionAlgorithms(*__, **_) -> Never:
    """
    Qt's 'QGrpcChannelOptions
    &QGrpcChannelOptions::setAcceptedCompressionAlgorithms(QtGrpc::
    CompressionAlgorithms algorithms)': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QGrpcChannelOptions.setAcceptedCompressionAlgorithms' has no cute "
        "function yet. Qt's 'QGrpcChannelOptions "
        "&QGrpcChannelOptions::setAcceptedCompressionAlgorithms(QtGrpc::Comp"
        "ressionAlgorithms algorithms)': gives a type Python has no way to "
        "take yet.")

  @staticmethod
  def setDeadlineTimeout(*__, **_) -> Never:
    """
    Qt's 'QGrpcChannelOptions
    &QGrpcChannelOptions::setDeadlineTimeout(std::chrono::milliseconds
    timeout)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGrpcChannelOptions.setDeadlineTimeout' has no cute function yet. "
        "Qt's 'QGrpcChannelOptions "
        "&QGrpcChannelOptions::setDeadlineTimeout(std::chrono::milliseconds "
        "timeout)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setFilterServerMetadata(*__, **_) -> Never:
    """
    Qt's 'QGrpcChannelOptions
    &QGrpcChannelOptions::setFilterServerMetadata(bool value)': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGrpcChannelOptions.setFilterServerMetadata' has no cute function "
        "yet. Qt's 'QGrpcChannelOptions "
        "&QGrpcChannelOptions::setFilterServerMetadata(bool value)': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def setMaximumReceiveMessageSize(*__, **_) -> Never:
    """
    Qt's 'QGrpcChannelOptions
    &QGrpcChannelOptions::setMaximumReceiveMessageSize(quint64 size)': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGrpcChannelOptions.setMaximumReceiveMessageSize' has no cute "
        "function yet. Qt's 'QGrpcChannelOptions "
        "&QGrpcChannelOptions::setMaximumReceiveMessageSize(quint64 size)': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def setMetadata(*__, **_) -> Never:
    """
    - Qt's 'QGrpcChannelOptions &QGrpcChannelOptions::setMetadata(const
      QHash<QByteArray, QByteArray> &metadata)': takes a type Python has no
      way to hand over yet.
    - Qt's 'QGrpcChannelOptions
      &QGrpcChannelOptions::setMetadata(QHash<QByteArray, QByteArray>
      &&metadata)': takes a type Python has no way to hand over yet.
    - Qt's 'QGrpcChannelOptions &QGrpcChannelOptions::setMetadata(const
      QMultiHash<QByteArray, QByteArray> &metadata)': takes a type Python has
      no way to hand over yet.
    - Qt's 'QGrpcChannelOptions
      &QGrpcChannelOptions::setMetadata(QMultiHash<QByteArray, QByteArray>
      &&metadata)': takes a type Python has no way to hand over yet.
    - Qt's 'QGrpcChannelOptions
      &QGrpcChannelOptions::setMetadata(std::initializer_list<std::
      pair<QByteArray, QByteArray>> list)': takes a type Python has no way to
      hand over yet.
    """
    raise NotImplementedError(
        "'QGrpcChannelOptions.setMetadata' has no cute function yet. Qt's "
        "'QGrpcChannelOptions &QGrpcChannelOptions::setMetadata(const "
        "QHash<QByteArray, QByteArray> &metadata)': takes a type Python has "
        "no way to hand over yet. Qt's 'QGrpcChannelOptions "
        "&QGrpcChannelOptions::setMetadata(QHash<QByteArray, QByteArray> "
        "&&metadata)': takes a type Python has no way to hand over yet. "
        "Qt's 'QGrpcChannelOptions &QGrpcChannelOptions::setMetadata(const "
        "QMultiHash<QByteArray, QByteArray> &metadata)': takes a type "
        "Python has no way to hand over yet. Qt's 'QGrpcChannelOptions "
        "&QGrpcChannelOptions::setMetadata(QMultiHash<QByteArray, "
        "QByteArray> &&metadata)': takes a type Python has no way to hand "
        "over yet. Qt's 'QGrpcChannelOptions "
        "&QGrpcChannelOptions::setMetadata(std::initializer_list<std::pair<Q"
        "ByteArray, QByteArray>> list)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def setRequestCompression(*__, **_) -> Never:
    """
    Qt's 'QGrpcChannelOptions
    &QGrpcChannelOptions::setRequestCompression(QtGrpc::CompressionAlgorithm
    algorithm)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGrpcChannelOptions.setRequestCompression' has no cute function "
        "yet. Qt's 'QGrpcChannelOptions "
        "&QGrpcChannelOptions::setRequestCompression(QtGrpc::CompressionAlgo"
        "rithm algorithm)': gives a type Python has no way to take yet.")

  @staticmethod
  def setSerializationFormat(*__, **_) -> Never:
    """
    Qt's 'QGrpcChannelOptions
    &QGrpcChannelOptions::setSerializationFormat(const
    QGrpcSerializationFormat &format)': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QGrpcChannelOptions.setSerializationFormat' has no cute function "
        "yet. Qt's 'QGrpcChannelOptions "
        "&QGrpcChannelOptions::setSerializationFormat(const "
        "QGrpcSerializationFormat &format)': gives a type Python has no way "
        "to take yet.")

  @staticmethod
  def setSslConfiguration(*__, **_) -> Never:
    """
    Qt's 'QGrpcChannelOptions &QGrpcChannelOptions::setSslConfiguration(const
    QSslConfiguration &sslConfiguration)': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QGrpcChannelOptions.setSslConfiguration' has no cute function "
        "yet. Qt's 'QGrpcChannelOptions "
        "&QGrpcChannelOptions::setSslConfiguration(const QSslConfiguration "
        "&sslConfiguration)': gives a type Python has no way to take yet.")

  @staticmethod
  def sslConfiguration(*__, **_) -> Never:
    """
    Qt's 'std::optional<QSslConfiguration>
    QGrpcChannelOptions::sslConfiguration() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QGrpcChannelOptions.sslConfiguration' has no cute function yet. "
        "Qt's 'std::optional<QSslConfiguration> "
        "QGrpcChannelOptions::sslConfiguration() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QGrpcChannelOptions::swap(QGrpcChannelOptions &other)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGrpcChannelOptions.swap' has no cute function yet. Qt's 'void "
        "QGrpcChannelOptions::swap(QGrpcChannelOptions &other)': takes a "
        "type Python has no way to hand over yet.")
