"""
QSslKey binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qsslkey.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QSsl

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QIODevice
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QIODevice = WAIT['QIODevice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSslKey(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSslKey: a plain Python object standing in front of
  one C++ QSslKey.

  C++ hands a QSslKey around as a copy, so every C++ QSslKey behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSslKey that has a ritual and that Python can call
  so far, 9 names in all: 'isNull', 'clear', 'length', 'type', 'algorithm',
  'toPem', 'toDer', '__eq__', '__ne__'. It can be made from Python, in 4
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSslKey::QSslKey(Qt::HANDLE handle, QSsl::KeyType type)': names
    'void', which has no cute class yet.
  - Qt's 'QSslKey::QSslKey(QSslKey &&other)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QSslKey &QSslKey::operator=(QSslKey &&other)': assignment: Python
    binds a name and has no operator for it.
  - Qt's 'QSslKey &QSslKey::operator=(const QSslKey &other)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'QSslKey::~QSslKey()': the destructor: Python removes its C++
    QSslKey by it, and has no other use for it.
  - Qt's 'void QSslKey::swap(QSslKey &other)': takes a type Python has no way
    to hand over yet.
  - Qt's 'Qt::HANDLE QSslKey::handle() const': gives 'void', which has no
    cute class yet.

  What to expect
  --------------

  - The C++ QSslKey is created at the first use, not by 'QSslKey(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSslKey back gives a copy the ritual made for Python,
    in a new cute QSslKey.
  - Each name of Qt's QSslKey that has no cute function yet, 'handle',
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
  __qt_class__ = 'QSslKey'

  #  Qt's '~QSslKey()'. Naming it makes this a value class: Python owns every
  #  C++ QSslKey behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN7QSslKeyD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QSslKey::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslkey.html#isNull
    """
    #  bool QSslKey::isNull() const
    return self.uglySide.call('ritual_ZNK7QSslKey6isNullEv')

  def length(self) -> int:
    """
    Calls Qt's 'int QSslKey::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslkey.html#length
    """
    #  int QSslKey::length() const
    return self.uglySide.call('ritual_ZNK7QSslKey6lengthEv')

  def type(self) -> QSsl.KeyType:
    """
    Calls Qt's 'QSsl::KeyType QSslKey::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslkey.html#type

    Returns
    -------

    QSsl.KeyType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QSsl.KeyType(number)'
      gives.
    """
    #  QSsl::KeyType QSslKey::type() const
    return QSsl.KeyType(self.uglySide.call('ritual_ZNK7QSslKey4typeEv'))

  def algorithm(self) -> QSsl.KeyAlgorithm:
    """
    Calls Qt's 'QSsl::KeyAlgorithm QSslKey::algorithm() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslkey.html#algorithm

    Returns
    -------

    QSsl.KeyAlgorithm
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSsl.KeyAlgorithm(number)' gives.
    """
    #  QSsl::KeyAlgorithm QSslKey::algorithm() const
    return QSsl.KeyAlgorithm(self.uglySide.call(
        'ritual_ZNK7QSslKey9algorithmEv',
    ))

  @overload()
  @overload(QByteArray)
  def toPem(self, passPhrase: Optional[QByteArray] = None) -> QByteArray:
    """
    Calls Qt's 'QByteArray QSslKey::toPem(const QByteArray &passPhrase)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslkey.html#toPem

    Parameters
    ----------

    passPhrase : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QSslKey::toPem(const QByteArray &passPhrase) const
    if passPhrase is None:
      from ..QtCore import QByteArray
      passPhrase = QByteArray()
    address = self.uglySide.call(
        'ritual_ZNK7QSslKey5toPemERK10QByteArray', self._valueOf(passPhrase),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload()
  @overload(QByteArray)
  def toDer(self, passPhrase: Optional[QByteArray] = None) -> QByteArray:
    """
    Calls Qt's 'QByteArray QSslKey::toDer(const QByteArray &passPhrase)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslkey.html#toDer

    Parameters
    ----------

    passPhrase : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QSslKey::toDer(const QByteArray &passPhrase) const
    if passPhrase is None:
      from ..QtCore import QByteArray
      passPhrase = QByteArray()
    address = self.uglySide.call(
        'ritual_ZNK7QSslKey5toDerERK10QByteArray', self._valueOf(passPhrase),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

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
  def __eq__(self, key: QSslKey) -> bool:
    """
    Calls Qt's 'bool QSslKey::operator==(const QSslKey &key) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslkey.html#operator==

    Parameters
    ----------

    key : QSslKey
      Passed on as a value: Qt reads the C++ QSslKey, which stays Python's
      own.
    """
    #  bool QSslKey::operator==(const QSslKey &key) const
    return self.uglySide.call(
        'ritual_ZNK7QSslKeyeqERKS_', self._valueOf(key),
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
  def __ne__(self, key: QSslKey) -> bool:
    """
    Calls Qt's 'bool QSslKey::operator!=(const QSslKey &key) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslkey.html#operator!=

    Parameters
    ----------

    key : QSslKey
      Passed on as a value: Qt reads the C++ QSslKey, which stays Python's
      own.
    """
    #  bool QSslKey::operator!=(const QSslKey &key) const
    return self.uglySide.call(
        'ritual_ZNK7QSslKeyneERKS_', self._valueOf(key),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
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
    Notes what was given, for Qt's 'QSslKey::QSslKey()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsslkey.html#QSslKey
    """
    #  QSslKey::QSslKey()
    self._noteCreation(QSslKey, lambda: Rituals.call(
        'ritual_ZN7QSslKeyC1Ev',
    ))

  @overload(QByteArray, QSsl.KeyAlgorithm)
  @overload(QByteArray, QSsl.KeyAlgorithm, QSsl.EncodingFormat)
  @overload(QByteArray, QSsl.KeyAlgorithm, QSsl.EncodingFormat, QSsl.KeyType)
  @overload(
      QByteArray, QSsl.KeyAlgorithm, QSsl.EncodingFormat, QSsl.KeyType,
      QByteArray,
  )
  def __init__(
      self,
      encoded: QByteArray,
      algorithm: QSsl.KeyAlgorithm,
      format: QSsl.EncodingFormat = QSsl.EncodingFormat.Pem,
      type: QSsl.KeyType = QSsl.KeyType.PrivateKey,
      passPhrase: Optional[QByteArray] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QSslKey::QSslKey(const QByteArray
    &encoded, QSsl::KeyAlgorithm algorithm, QSsl::EncodingFormat format,
    QSsl::KeyType type, const QByteArray &passPhrase)', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsslkey.html#QSslKey

    Parameters
    ----------

    encoded : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    algorithm : QSsl.KeyAlgorithm
      Passed on as its number.

    format : QSsl.EncodingFormat
      Passed on as its number. May be left out, as in Qt: it is then
      QSsl.EncodingFormat.Pem.

    type : QSsl.KeyType
      Passed on as its number. May be left out, as in Qt: it is then
      QSsl.KeyType.PrivateKey.

    passPhrase : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.
    """
    #  QSslKey::QSslKey(const QByteArray &encoded, QSsl::KeyAlgorithm
    #      algorithm, QSsl::EncodingFormat format, QSsl::KeyType type, const
    #      QByteArray &passPhrase)
    if passPhrase is None:
      from ..QtCore import QByteArray
      passPhrase = QByteArray()
    self._noteCreation(QSslKey, lambda: Rituals.call(
        'ritual_ZN7QSslKeyC1ERK10QByteArrayN4QSsl12KeyAlgorithmENS3_14Encod'
        'ingFormatENS3_7KeyTypeES2_',
        self._valueOf(encoded), algorithm.value, format.value, type.value,
        self._valueOf(passPhrase),
    ))

  @overload(QIODevice, QSsl.KeyAlgorithm)
  @overload(NoneType, QSsl.KeyAlgorithm)
  @overload(QIODevice, QSsl.KeyAlgorithm, QSsl.EncodingFormat)
  @overload(NoneType, QSsl.KeyAlgorithm, QSsl.EncodingFormat)
  @overload(QIODevice, QSsl.KeyAlgorithm, QSsl.EncodingFormat, QSsl.KeyType)
  @overload(NoneType, QSsl.KeyAlgorithm, QSsl.EncodingFormat, QSsl.KeyType)
  @overload(
      QIODevice, QSsl.KeyAlgorithm, QSsl.EncodingFormat, QSsl.KeyType,
      QByteArray,
  )
  @overload(
      NoneType, QSsl.KeyAlgorithm, QSsl.EncodingFormat, QSsl.KeyType,
      QByteArray,
  )
  def __init__(
      self,
      device: Optional[QIODevice],
      algorithm: QSsl.KeyAlgorithm,
      format: QSsl.EncodingFormat = QSsl.EncodingFormat.Pem,
      type: QSsl.KeyType = QSsl.KeyType.PrivateKey,
      passPhrase: Optional[QByteArray] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QSslKey::QSslKey(QIODevice *device,
    QSsl::KeyAlgorithm algorithm, QSsl::EncodingFormat format, QSsl::KeyType
    type, const QByteArray &passPhrase)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsslkey.html#QSslKey

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    algorithm : QSsl.KeyAlgorithm
      Passed on as its number.

    format : QSsl.EncodingFormat
      Passed on as its number. May be left out, as in Qt: it is then
      QSsl.EncodingFormat.Pem.

    type : QSsl.KeyType
      Passed on as its number. May be left out, as in Qt: it is then
      QSsl.KeyType.PrivateKey.

    passPhrase : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.
    """
    #  QSslKey::QSslKey(QIODevice *device, QSsl::KeyAlgorithm algorithm,
    #      QSsl::EncodingFormat format, QSsl::KeyType type, const QByteArray
    #      &passPhrase)
    if passPhrase is None:
      from ..QtCore import QByteArray
      passPhrase = QByteArray()
    self._noteCreation(QSslKey, lambda: Rituals.call(
        'ritual_ZN7QSslKeyC1EP9QIODeviceN4QSsl12KeyAlgorithmENS2_14Encoding'
        'FormatENS2_7KeyTypeERK10QByteArray',
        self._addressOf(device), algorithm.value, format.value, type.value,
        self._valueOf(passPhrase),
    ))

  @overload(THIS)
  def __init__(self, other: QSslKey) -> None:
    """
    Notes what was given, for Qt's 'QSslKey::QSslKey(const QSslKey &other)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsslkey.html#QSslKey

    Parameters
    ----------

    other : QSslKey
      Passed on as a value: Qt reads the C++ QSslKey, which stays Python's
      own.
    """
    #  QSslKey::QSslKey(const QSslKey &other)
    self._noteCreation(QSslKey, lambda: Rituals.call(
        'ritual_ZN7QSslKeyC1ERKS_', self._valueOf(other),
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

  def clear(self) -> None:
    """
    Calls Qt's 'void QSslKey::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qsslkey.html#clear
    """
    #  void QSslKey::clear()
    self.uglySide.call('ritual_ZN7QSslKey5clearEv')

  @staticmethod
  def handle(*__, **_) -> Never:
    """
    Qt's 'Qt::HANDLE QSslKey::handle() const': gives 'void', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QSslKey.handle' has no cute function yet. Qt's 'Qt::HANDLE "
        "QSslKey::handle() const': gives 'void', which has no cute class "
        "yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QSslKey::swap(QSslKey &other)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QSslKey.swap' has no cute function yet. Qt's 'void "
        "QSslKey::swap(QSslKey &other)': takes a type Python has no way to "
        "hand over yet.")
