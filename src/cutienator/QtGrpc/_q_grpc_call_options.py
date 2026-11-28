"""
QGrpcCallOptions binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGrpc/qgrpccalloptions.h, Qt 6.12.0. Changes made here are lost.
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
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDebug = WAIT['QDebug']


class QGrpcCallOptions(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGrpcCallOptions: a plain Python object standing in
  front of one C++ QGrpcCallOptions.

  C++ hands a QGrpcCallOptions around as a copy, so every C++
  QGrpcCallOptions behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGrpcCallOptions that has a ritual and that Python
  can call so far, 3 names in all: '__eq__', '__ne__', '__rlshift__'. It can
  be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGrpcCallOptions::~QGrpcCallOptions()': the destructor: Python
    removes its C++ QGrpcCallOptions by it, and has no other use for it.
  - Qt's 'QGrpcCallOptions &QGrpcCallOptions::operator=(const
    QGrpcCallOptions &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QGrpcCallOptions::QGrpcCallOptions(QGrpcCallOptions &&other)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QGrpcCallOptions &QGrpcCallOptions::operator=(QGrpcCallOptions
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QVariant QGrpcCallOptions::operator QVariant() const': an operator
    Python has no name for.
  - Qt's 'void QGrpcCallOptions::swap(QGrpcCallOptions &other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'std::optional<std::chrono::milliseconds>
    QGrpcCallOptions::deadlineTimeout() const': gives a type Python has no
    way to take yet.
  - Qt's 'QGrpcCallOptions
    &QGrpcCallOptions::setDeadlineTimeout(std::chrono::milliseconds
    timeout)': takes a type Python has no way to hand over yet.
  - Qt's 'const QHash<QByteArray, QByteArray> &QGrpcCallOptions::metadata()
    const': gives a type Python has no way to take yet.
  - Qt's 'QGrpcCallOptions &QGrpcCallOptions::setMetadata(const
    QHash<QByteArray, QByteArray> &metadata)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QGrpcCallOptions &QGrpcCallOptions::setMetadata(QHash<QByteArray,
    QByteArray> &&metadata)': takes a type Python has no way to hand over
    yet.
  - Qt's 'const QMultiHash<QByteArray, QByteArray>
    &QGrpcCallOptions::metadata(QtGrpc::MultiValue_t a0) const': gives a type
    Python has no way to take yet.
  - Qt's 'QGrpcCallOptions &QGrpcCallOptions::setMetadata(const
    QMultiHash<QByteArray, QByteArray> &metadata)': takes a type Python has
    no way to hand over yet.
  - Qt's 'QGrpcCallOptions
    &QGrpcCallOptions::setMetadata(QMultiHash<QByteArray, QByteArray>
    &&metadata)': takes a type Python has no way to hand over yet.
  - Qt's 'QGrpcCallOptions
    &QGrpcCallOptions::setMetadata(std::initializer_list<std::
    pair<QByteArray, QByteArray>> list)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QGrpcCallOptions &QGrpcCallOptions::addMetadata(QByteArrayView key,
    QByteArrayView value)': gives a type Python has no way to take yet.
  - Qt's 'std::optional<bool> QGrpcCallOptions::filterServerMetadata()
    const': gives a type Python has no way to take yet.
  - Qt's 'QGrpcCallOptions &QGrpcCallOptions::setFilterServerMetadata(bool
    value)': gives a type Python has no way to take yet.
  - Qt's 'std::optional<quint64>
    QGrpcCallOptions::maximumReceiveMessageSize() const': gives a type Python
    has no way to take yet.
  - Qt's 'QGrpcCallOptions
    &QGrpcCallOptions::setMaximumReceiveMessageSize(quint64 size)': gives a
    type Python has no way to take yet.
  - Qt's 'std::optional<QtGrpc::CompressionAlgorithm>
    QGrpcCallOptions::requestCompression() const': gives a type Python has no
    way to take yet.
  - Qt's 'QGrpcCallOptions
    &QGrpcCallOptions::setRequestCompression(QtGrpc::CompressionAlgorithm
    algorithm)': gives a type Python has no way to take yet.
  - Qt's 'QGrpcCallOptionsPrivate *QGrpcCallOptions::d_func()': gives
    'QGrpcCallOptionsPrivate', which has no cute class yet.
  - Qt's 'const QGrpcCallOptionsPrivate *QGrpcCallOptions::d_func() const':
    gives 'QGrpcCallOptionsPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 33 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QGrpcCallOptions is created at the first use, not by
    'QGrpcCallOptions(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGrpcCallOptions back gives a copy the ritual made
    for Python, in a new cute QGrpcCallOptions.
  - Each name of Qt's QGrpcCallOptions that has no cute function yet,
    'addMetadata', 'd_func', 'deadlineTimeout', 'filterServerMetadata',
    'maximumReceiveMessageSize', 'metadata', 'requestCompression',
    'setDeadlineTimeout', 'setFilterServerMetadata',
    'setMaximumReceiveMessageSize', 'setMetadata', 'setRequestCompression',
    'swap', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGrpcCallOptions'

  #  Qt's '~QGrpcCallOptions()'. Naming it makes this a value class: Python
  #  owns every C++ QGrpcCallOptions behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QGrpcCallOptionsD1Ev'

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

  @overload(THIS)
  def __eq__(self, rhs: QGrpcCallOptions) -> bool:
    """
    Calls Qt's 'bool operator==(const QGrpcCallOptions &lhs, const
    QGrpcCallOptions &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qgrpccalloptions.html#operator==

    Parameters
    ----------

    rhs : QGrpcCallOptions
      Passed on as a value: Qt reads the C++ QGrpcCallOptions, which stays
      Python's own.
    """
    #  bool operator==(const QGrpcCallOptions &lhs, const QGrpcCallOptions
    #      &rhs)
    return Rituals.call(
        'ritual_ZeqRK16QGrpcCallOptionsS1_',
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
  def __ne__(self, rhs: QGrpcCallOptions) -> bool:
    """
    Calls Qt's 'bool operator!=(const QGrpcCallOptions &lhs, const
    QGrpcCallOptions &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qgrpccalloptions.html#operator!=

    Parameters
    ----------

    rhs : QGrpcCallOptions
      Passed on as a value: Qt reads the C++ QGrpcCallOptions, which stays
      Python's own.
    """
    #  bool operator!=(const QGrpcCallOptions &lhs, const QGrpcCallOptions
    #      &rhs)
    return Rituals.call(
        'ritual_ZneRK16QGrpcCallOptionsS1_',
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
    Calls Qt's 'QDebug operator<<(QDebug debug, const QGrpcCallOptions
    &callOpts)'.

    Qt's own words: https://doc.qt.io/qt-6/qgrpccalloptions.html#operator<<

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
    #  QDebug operator<<(QDebug debug, const QGrpcCallOptions &callOpts)
    address = Rituals.call(
        'ritual_Zls6QDebugRK16QGrpcCallOptions',
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
    Notes what was given, for Qt's 'QGrpcCallOptions::QGrpcCallOptions()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpccalloptions.html#QGrpcCallOptions
    """
    #  QGrpcCallOptions::QGrpcCallOptions()
    self._noteCreation(QGrpcCallOptions, lambda: Rituals.call(
        'ritual_ZN16QGrpcCallOptionsC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QGrpcCallOptions) -> None:
    """
    Notes what was given, for Qt's 'QGrpcCallOptions::QGrpcCallOptions(const
    QGrpcCallOptions &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpccalloptions.html#QGrpcCallOptions

    Parameters
    ----------

    other : QGrpcCallOptions
      Passed on as a value: Qt reads the C++ QGrpcCallOptions, which stays
      Python's own.
    """
    #  QGrpcCallOptions::QGrpcCallOptions(const QGrpcCallOptions &other)
    self._noteCreation(QGrpcCallOptions, lambda: Rituals.call(
        'ritual_ZN16QGrpcCallOptionsC1ERKS_', self._valueOf(other),
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
    Qt's 'QGrpcCallOptions &QGrpcCallOptions::addMetadata(QByteArrayView key,
    QByteArrayView value)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGrpcCallOptions.addMetadata' has no cute function yet. Qt's "
        "'QGrpcCallOptions &QGrpcCallOptions::addMetadata(QByteArrayView "
        "key, QByteArrayView value)': gives a type Python has no way to "
        "take yet.")

  @staticmethod
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'QGrpcCallOptionsPrivate *QGrpcCallOptions::d_func()': gives
      'QGrpcCallOptionsPrivate', which has no cute class yet.
    - Qt's 'const QGrpcCallOptionsPrivate *QGrpcCallOptions::d_func() const':
      gives 'QGrpcCallOptionsPrivate', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QGrpcCallOptions.d_func' has no cute function yet. Qt's "
        "'QGrpcCallOptionsPrivate *QGrpcCallOptions::d_func()': gives "
        "'QGrpcCallOptionsPrivate', which has no cute class yet. Qt's "
        "'const QGrpcCallOptionsPrivate *QGrpcCallOptions::d_func() const': "
        "gives 'QGrpcCallOptionsPrivate', which has no cute class yet.")

  @staticmethod
  def deadlineTimeout(*__, **_) -> Never:
    """
    Qt's 'std::optional<std::chrono::milliseconds>
    QGrpcCallOptions::deadlineTimeout() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QGrpcCallOptions.deadlineTimeout' has no cute function yet. Qt's "
        "'std::optional<std::chrono::milliseconds> "
        "QGrpcCallOptions::deadlineTimeout() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def filterServerMetadata(*__, **_) -> Never:
    """
    Qt's 'std::optional<bool> QGrpcCallOptions::filterServerMetadata()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGrpcCallOptions.filterServerMetadata' has no cute function yet. "
        "Qt's 'std::optional<bool> QGrpcCallOptions::filterServerMetadata() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def maximumReceiveMessageSize(*__, **_) -> Never:
    """
    Qt's 'std::optional<quint64>
    QGrpcCallOptions::maximumReceiveMessageSize() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QGrpcCallOptions.maximumReceiveMessageSize' has no cute function "
        "yet. Qt's 'std::optional<quint64> "
        "QGrpcCallOptions::maximumReceiveMessageSize() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def metadata(*__, **_) -> Never:
    """
    - Qt's 'const QHash<QByteArray, QByteArray> &QGrpcCallOptions::metadata()
      const': gives a type Python has no way to take yet.
    - Qt's 'const QMultiHash<QByteArray, QByteArray>
      &QGrpcCallOptions::metadata(QtGrpc::MultiValue_t a0) const': gives a
      type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGrpcCallOptions.metadata' has no cute function yet. Qt's 'const "
        "QHash<QByteArray, QByteArray> &QGrpcCallOptions::metadata() "
        "const': gives a type Python has no way to take yet. Qt's 'const "
        "QMultiHash<QByteArray, QByteArray> "
        "&QGrpcCallOptions::metadata(QtGrpc::MultiValue_t a0) const': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def requestCompression(*__, **_) -> Never:
    """
    Qt's 'std::optional<QtGrpc::CompressionAlgorithm>
    QGrpcCallOptions::requestCompression() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QGrpcCallOptions.requestCompression' has no cute function yet. "
        "Qt's 'std::optional<QtGrpc::CompressionAlgorithm> "
        "QGrpcCallOptions::requestCompression() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def setDeadlineTimeout(*__, **_) -> Never:
    """
    Qt's 'QGrpcCallOptions
    &QGrpcCallOptions::setDeadlineTimeout(std::chrono::milliseconds
    timeout)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGrpcCallOptions.setDeadlineTimeout' has no cute function yet. "
        "Qt's 'QGrpcCallOptions "
        "&QGrpcCallOptions::setDeadlineTimeout(std::chrono::milliseconds "
        "timeout)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setFilterServerMetadata(*__, **_) -> Never:
    """
    Qt's 'QGrpcCallOptions &QGrpcCallOptions::setFilterServerMetadata(bool
    value)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGrpcCallOptions.setFilterServerMetadata' has no cute function "
        "yet. Qt's 'QGrpcCallOptions "
        "&QGrpcCallOptions::setFilterServerMetadata(bool value)': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def setMaximumReceiveMessageSize(*__, **_) -> Never:
    """
    Qt's 'QGrpcCallOptions
    &QGrpcCallOptions::setMaximumReceiveMessageSize(quint64 size)': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGrpcCallOptions.setMaximumReceiveMessageSize' has no cute "
        "function yet. Qt's 'QGrpcCallOptions "
        "&QGrpcCallOptions::setMaximumReceiveMessageSize(quint64 size)': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def setMetadata(*__, **_) -> Never:
    """
    - Qt's 'QGrpcCallOptions &QGrpcCallOptions::setMetadata(const
      QHash<QByteArray, QByteArray> &metadata)': takes a type Python has no
      way to hand over yet.
    - Qt's 'QGrpcCallOptions &QGrpcCallOptions::setMetadata(QHash<QByteArray,
      QByteArray> &&metadata)': takes a type Python has no way to hand over
      yet.
    - Qt's 'QGrpcCallOptions &QGrpcCallOptions::setMetadata(const
      QMultiHash<QByteArray, QByteArray> &metadata)': takes a type Python has
      no way to hand over yet.
    - Qt's 'QGrpcCallOptions
      &QGrpcCallOptions::setMetadata(QMultiHash<QByteArray, QByteArray>
      &&metadata)': takes a type Python has no way to hand over yet.
    - Qt's 'QGrpcCallOptions
      &QGrpcCallOptions::setMetadata(std::initializer_list<std::
      pair<QByteArray, QByteArray>> list)': takes a type Python has no way to
      hand over yet.
    """
    raise NotImplementedError(
        "'QGrpcCallOptions.setMetadata' has no cute function yet. Qt's "
        "'QGrpcCallOptions &QGrpcCallOptions::setMetadata(const "
        "QHash<QByteArray, QByteArray> &metadata)': takes a type Python has "
        "no way to hand over yet. Qt's 'QGrpcCallOptions "
        "&QGrpcCallOptions::setMetadata(QHash<QByteArray, QByteArray> "
        "&&metadata)': takes a type Python has no way to hand over yet. "
        "Qt's 'QGrpcCallOptions &QGrpcCallOptions::setMetadata(const "
        "QMultiHash<QByteArray, QByteArray> &metadata)': takes a type "
        "Python has no way to hand over yet. Qt's 'QGrpcCallOptions "
        "&QGrpcCallOptions::setMetadata(QMultiHash<QByteArray, QByteArray> "
        "&&metadata)': takes a type Python has no way to hand over yet. "
        "Qt's 'QGrpcCallOptions "
        "&QGrpcCallOptions::setMetadata(std::initializer_list<std::pair<QByt"
        "eArray, QByteArray>> list)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def setRequestCompression(*__, **_) -> Never:
    """
    Qt's 'QGrpcCallOptions
    &QGrpcCallOptions::setRequestCompression(QtGrpc::CompressionAlgorithm
    algorithm)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGrpcCallOptions.setRequestCompression' has no cute function yet. "
        "Qt's 'QGrpcCallOptions "
        "&QGrpcCallOptions::setRequestCompression(QtGrpc::CompressionAlgorit"
        "hm algorithm)': gives a type Python has no way to take yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QGrpcCallOptions::swap(QGrpcCallOptions &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGrpcCallOptions.swap' has no cute function yet. Qt's 'void "
        "QGrpcCallOptions::swap(QGrpcCallOptions &other)': takes a type "
        "Python has no way to hand over yet.")
