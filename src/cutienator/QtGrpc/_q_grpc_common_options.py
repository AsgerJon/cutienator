"""
QGrpcCommonOptions binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGrpc/6.12.0/QtGrpc/private/qgrpccommonoptions_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QGrpcCommonOptions to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QSharedData
from . import QtGrpc

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArrayView
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArrayView = WAIT['QByteArrayView']


class QGrpcCommonOptions(QSharedData):
  """
  The cute side of Qt's QGrpcCommonOptions: a plain Python object standing in
  front of one C++ QGrpcCommonOptions.

  It is built on the cute 'QSharedData', as Qt's QGrpcCommonOptions is built
  on Qt's QSharedData, and has everything that class has.

  C++ hands a QGrpcCommonOptions around as a copy, so every C++
  QGrpcCommonOptions behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGrpcCommonOptions that has a ritual and that Python
  can call so far, 4 names in all: 'containsMetadata',
  'setFilterServerMetadata', 'setMaximumReceiveMessageSize',
  'setRequestCompression'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGrpcCommonOptions::~QGrpcCommonOptions()': the destructor: Python
    removes its C++ QGrpcCommonOptions by it, and has no other use for it.
  - Qt's 'std::optional<std::chrono::milliseconds>
    QGrpcCommonOptions::deadlineTimeout() const': gives a type Python has no
    way to take yet.
  - Qt's 'void
    QGrpcCommonOptions::setDeadlineTimeout(std::chrono::milliseconds t)':
    takes a type Python has no way to hand over yet.
  - Qt's 'const QHash<QByteArray, QByteArray> &QGrpcCommonOptions::metadata()
    const': gives a type Python has no way to take yet.
  - Qt's 'void QGrpcCommonOptions::setMetadata(const QHash<QByteArray,
    QByteArray> &md)': takes a type Python has no way to hand over yet.
  - Qt's 'void QGrpcCommonOptions::setMetadata(QHash<QByteArray, QByteArray>
    &&md)': takes a type Python has no way to hand over yet.
  - Qt's 'const QMultiHash<QByteArray, QByteArray>
    &QGrpcCommonOptions::metadata(QtGrpc::MultiValue_t a0) const': gives a
    type Python has no way to take yet.
  - Qt's 'void QGrpcCommonOptions::setMetadata(const QMultiHash<QByteArray,
    QByteArray> &md)': takes a type Python has no way to hand over yet.
  - Qt's 'void QGrpcCommonOptions::setMetadata(QMultiHash<QByteArray,
    QByteArray> &&md)': takes a type Python has no way to hand over yet.
  - Qt's 'void QGrpcCommonOptions::addMetadata(QByteArray &&key, QByteArray
    &&value)': takes a type Python has no way to hand over yet.
  - Qt's 'std::optional<bool> QGrpcCommonOptions::filterServerMetadata()
    const': gives a type Python has no way to take yet.
  - Qt's 'std::optional<quint64>
    QGrpcCommonOptions::maximumReceiveMessageSize() const': gives a type
    Python has no way to take yet.
  - Qt's 'std::optional<QtGrpc::CompressionAlgorithm>
    QGrpcCommonOptions::requestCompression() const': gives a type Python has
    no way to take yet.

  What has no ritual
  ------------------

  2 of the 20 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QGrpcCommonOptions is created at the first use, not by
    'QGrpcCommonOptions(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGrpcCommonOptions back gives a copy the ritual made
    for Python, in a new cute QGrpcCommonOptions.
  - Each name of Qt's QGrpcCommonOptions that has no cute function yet,
    'addMetadata', 'deadlineTimeout', 'filterServerMetadata',
    'maximumReceiveMessageSize', 'metadata', 'requestCompression',
    'setDeadlineTimeout', 'setMetadata', holds a function that raises
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
  __qt_class__ = 'QGrpcCommonOptions'

  #  Qt's '~QGrpcCommonOptions()'. Naming it makes this a value class: Python
  #  owns every C++ QGrpcCommonOptions behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QGrpcCommonOptionsD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QByteArrayView, QByteArrayView)
  def containsMetadata(
      self,
      key: QByteArrayView,
      value: QByteArrayView,
  ) -> bool:
    """
    Calls Qt's 'bool QGrpcCommonOptions::containsMetadata(QByteArrayView key,
    QByteArrayView value) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpccommonoptions.html#containsMetadata

    Parameters
    ----------

    key : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    value : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  bool QGrpcCommonOptions::containsMetadata(QByteArrayView key,
    #      QByteArrayView value) const
    return self.uglySide.call(
        'ritual_ZNK18QGrpcCommonOptions16containsMetadataE14QByteArrayViewS'
        '0_',
        self._valueOf(key), self._valueOf(value),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setFilterServerMetadata(self, value: bool) -> None:
    """
    Calls Qt's 'void QGrpcCommonOptions::setFilterServerMetadata(bool
    value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpccommonoptions.html#setFilterServerMetadata

    Parameters
    ----------

    value : bool
      Passed on as it is.
    """
    #  void QGrpcCommonOptions::setFilterServerMetadata(bool value)
    self.uglySide.call(
        'ritual_ZN18QGrpcCommonOptions23setFilterServerMetadataEb', value,
    )

  @overload(int)
  def setMaximumReceiveMessageSize(self, size: int) -> None:
    """
    Calls Qt's 'void QGrpcCommonOptions::setMaximumReceiveMessageSize(quint64
    size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpccommonoptions.html

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QGrpcCommonOptions::setMaximumReceiveMessageSize(quint64 size)
    self.uglySide.call(
        'ritual_ZN18QGrpcCommonOptions28setMaximumReceiveMessageSizeEy',
        size,
    )

  @overload(QtGrpc.CompressionAlgorithm)
  def setRequestCompression(
      self,
      algorithm: QtGrpc.CompressionAlgorithm,
  ) -> None:
    """
    Calls Qt's 'void
    QGrpcCommonOptions::setRequestCompression(QtGrpc::CompressionAlgorithm
    algorithm)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpccommonoptions.html#setRequestCompression

    Parameters
    ----------

    algorithm : QtGrpc.CompressionAlgorithm
      Passed on as its number.
    """
    #  void QGrpcCommonOptions::setRequestCompression(QtGrpc::
    #      CompressionAlgorithm algorithm)
    self.uglySide.call(
        'ritual_ZN18QGrpcCommonOptions21setRequestCompressionEN6QtGrpc20Com'
        'pressionAlgorithmE',
        algorithm.value,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QGrpcCommonOptions::QGrpcCommonOptions()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpccommonoptions.html#QGrpcCommonOptions
    """
    #  QGrpcCommonOptions::QGrpcCommonOptions()
    self._noteCreation(QGrpcCommonOptions, lambda: Rituals.call(
        'ritual_ZN18QGrpcCommonOptionsC1Ev',
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
    Qt's 'void QGrpcCommonOptions::addMetadata(QByteArray &&key, QByteArray
    &&value)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGrpcCommonOptions.addMetadata' has no cute function yet. Qt's "
        "'void QGrpcCommonOptions::addMetadata(QByteArray &&key, QByteArray "
        "&&value)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def deadlineTimeout(*__, **_) -> Never:
    """
    Qt's 'std::optional<std::chrono::milliseconds>
    QGrpcCommonOptions::deadlineTimeout() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QGrpcCommonOptions.deadlineTimeout' has no cute function yet. "
        "Qt's 'std::optional<std::chrono::milliseconds> "
        "QGrpcCommonOptions::deadlineTimeout() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def filterServerMetadata(*__, **_) -> Never:
    """
    Qt's 'std::optional<bool> QGrpcCommonOptions::filterServerMetadata()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGrpcCommonOptions.filterServerMetadata' has no cute function "
        "yet. Qt's 'std::optional<bool> "
        "QGrpcCommonOptions::filterServerMetadata() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def maximumReceiveMessageSize(*__, **_) -> Never:
    """
    Qt's 'std::optional<quint64>
    QGrpcCommonOptions::maximumReceiveMessageSize() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGrpcCommonOptions.maximumReceiveMessageSize' has no cute "
        "function yet. Qt's 'std::optional<quint64> "
        "QGrpcCommonOptions::maximumReceiveMessageSize() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def metadata(*__, **_) -> Never:
    """
    - Qt's 'const QHash<QByteArray, QByteArray>
      &QGrpcCommonOptions::metadata() const': gives a type Python has no way
      to take yet.
    - Qt's 'const QMultiHash<QByteArray, QByteArray>
      &QGrpcCommonOptions::metadata(QtGrpc::MultiValue_t a0) const': gives a
      type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGrpcCommonOptions.metadata' has no cute function yet. Qt's "
        "'const QHash<QByteArray, QByteArray> "
        "&QGrpcCommonOptions::metadata() const': gives a type Python has no "
        "way to take yet. Qt's 'const QMultiHash<QByteArray, QByteArray> "
        "&QGrpcCommonOptions::metadata(QtGrpc::MultiValue_t a0) const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def requestCompression(*__, **_) -> Never:
    """
    Qt's 'std::optional<QtGrpc::CompressionAlgorithm>
    QGrpcCommonOptions::requestCompression() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QGrpcCommonOptions.requestCompression' has no cute function yet. "
        "Qt's 'std::optional<QtGrpc::CompressionAlgorithm> "
        "QGrpcCommonOptions::requestCompression() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def setDeadlineTimeout(*__, **_) -> Never:
    """
    Qt's 'void
    QGrpcCommonOptions::setDeadlineTimeout(std::chrono::milliseconds t)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGrpcCommonOptions.setDeadlineTimeout' has no cute function yet. "
        "Qt's 'void "
        "QGrpcCommonOptions::setDeadlineTimeout(std::chrono::milliseconds "
        "t)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setMetadata(*__, **_) -> Never:
    """
    - Qt's 'void QGrpcCommonOptions::setMetadata(const QHash<QByteArray,
      QByteArray> &md)': takes a type Python has no way to hand over yet.
    - Qt's 'void QGrpcCommonOptions::setMetadata(QHash<QByteArray,
      QByteArray> &&md)': takes a type Python has no way to hand over yet.
    - Qt's 'void QGrpcCommonOptions::setMetadata(const QMultiHash<QByteArray,
      QByteArray> &md)': takes a type Python has no way to hand over yet.
    - Qt's 'void QGrpcCommonOptions::setMetadata(QMultiHash<QByteArray,
      QByteArray> &&md)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGrpcCommonOptions.setMetadata' has no cute function yet. Qt's "
        "'void QGrpcCommonOptions::setMetadata(const QHash<QByteArray, "
        "QByteArray> &md)': takes a type Python has no way to hand over "
        "yet. Qt's 'void QGrpcCommonOptions::setMetadata(QHash<QByteArray, "
        "QByteArray> &&md)': takes a type Python has no way to hand over "
        "yet. Qt's 'void QGrpcCommonOptions::setMetadata(const "
        "QMultiHash<QByteArray, QByteArray> &md)': takes a type Python has "
        "no way to hand over yet. Qt's 'void "
        "QGrpcCommonOptions::setMetadata(QMultiHash<QByteArray, QByteArray> "
        "&&md)': takes a type Python has no way to hand over yet.")
