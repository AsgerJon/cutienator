"""
QCoapPrivateKey binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCoap/qcoapsecurityconfiguration.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtNetwork import QSsl

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QCoapPrivateKey(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCoapPrivateKey: a plain Python object standing in
  front of one C++ QCoapPrivateKey.

  C++ hands a QCoapPrivateKey around as a copy, so every C++ QCoapPrivateKey
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCoapPrivateKey that has a ritual and that Python
  can call so far, 5 names in all: 'isNull', 'key', 'algorithm',
  'encodingFormat', 'passPhrase'. It can be made from Python, in 3 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCoapPrivateKey::QCoapPrivateKey(const Qt::HANDLE &handle)': takes
    a type Python has no way to hand over yet.
  - Qt's 'QCoapPrivateKey::QCoapPrivateKey(QCoapPrivateKey &&other)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QCoapPrivateKey::~QCoapPrivateKey()': the destructor: Python
    removes its C++ QCoapPrivateKey by it, and has no other use for it.
  - Qt's 'QCoapPrivateKey &QCoapPrivateKey::operator=(QCoapPrivateKey
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QCoapPrivateKey &QCoapPrivateKey::operator=(const QCoapPrivateKey
    &other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'void QCoapPrivateKey::swap(QCoapPrivateKey &other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'Qt::HANDLE QCoapPrivateKey::handle() const': gives 'void', which
    has no cute class yet.

  What to expect
  --------------

  - The C++ QCoapPrivateKey is created at the first use, not by
    'QCoapPrivateKey(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCoapPrivateKey back gives a copy the ritual made for
    Python, in a new cute QCoapPrivateKey.
  - Each name of Qt's QCoapPrivateKey that has no cute function yet,
    'handle', 'swap', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCoapPrivateKey'

  #  Qt's '~QCoapPrivateKey()'. Naming it makes this a value class: Python
  #  owns every C++ QCoapPrivateKey behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QCoapPrivateKeyD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QCoapPrivateKey::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapprivatekey.html#isNull
    """
    #  bool QCoapPrivateKey::isNull() const
    return self.uglySide.call('ritual_ZNK15QCoapPrivateKey6isNullEv')

  def key(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QCoapPrivateKey::key() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapprivatekey.html#key

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QCoapPrivateKey::key() const
    address = self.uglySide.call('ritual_ZNK15QCoapPrivateKey3keyEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def algorithm(self) -> QSsl.KeyAlgorithm:
    """
    Calls Qt's 'QSsl::KeyAlgorithm QCoapPrivateKey::algorithm() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapprivatekey.html#algorithm

    Returns
    -------

    QSsl.KeyAlgorithm
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSsl.KeyAlgorithm(number)' gives.
    """
    #  QSsl::KeyAlgorithm QCoapPrivateKey::algorithm() const
    return QSsl.KeyAlgorithm(self.uglySide.call(
        'ritual_ZNK15QCoapPrivateKey9algorithmEv',
    ))

  def encodingFormat(self) -> QSsl.EncodingFormat:
    """
    Calls Qt's 'QSsl::EncodingFormat QCoapPrivateKey::encodingFormat()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapprivatekey.html#encodingFormat

    Returns
    -------

    QSsl.EncodingFormat
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSsl.EncodingFormat(number)' gives.
    """
    #  QSsl::EncodingFormat QCoapPrivateKey::encodingFormat() const
    return QSsl.EncodingFormat(self.uglySide.call(
        'ritual_ZNK15QCoapPrivateKey14encodingFormatEv',
    ))

  def passPhrase(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QCoapPrivateKey::passPhrase() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapprivatekey.html#passPhrase

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QCoapPrivateKey::passPhrase() const
    address = self.uglySide.call('ritual_ZNK15QCoapPrivateKey10passPhraseEv')
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QCoapPrivateKey::QCoapPrivateKey()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapprivatekey.html#QCoapPrivateKey
    """
    #  QCoapPrivateKey::QCoapPrivateKey()
    self._noteCreation(QCoapPrivateKey, lambda: Rituals.call(
        'ritual_ZN15QCoapPrivateKeyC1Ev',
    ))

  @overload(QByteArray, QSsl.KeyAlgorithm)
  @overload(QByteArray, QSsl.KeyAlgorithm, QSsl.EncodingFormat)
  @overload(QByteArray, QSsl.KeyAlgorithm, QSsl.EncodingFormat, QByteArray)
  def __init__(
      self,
      key: QByteArray,
      algorithm: QSsl.KeyAlgorithm,
      format: QSsl.EncodingFormat = QSsl.EncodingFormat.Pem,
      passPhrase: Optional[QByteArray] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QCoapPrivateKey::QCoapPrivateKey(const
    QByteArray &key, QSsl::KeyAlgorithm algorithm, QSsl::EncodingFormat
    format, const QByteArray &passPhrase)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapprivatekey.html#QCoapPrivateKey

    Parameters
    ----------

    key : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    algorithm : QSsl.KeyAlgorithm
      Passed on as its number.

    format : QSsl.EncodingFormat
      Passed on as its number. May be left out, as in Qt: it is then
      QSsl.EncodingFormat.Pem.

    passPhrase : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.
    """
    #  QCoapPrivateKey::QCoapPrivateKey(const QByteArray &key,
    #      QSsl::KeyAlgorithm algorithm, QSsl::EncodingFormat format, const
    #      QByteArray &passPhrase)
    if passPhrase is None:
      from ..QtCore import QByteArray
      passPhrase = QByteArray()
    self._noteCreation(QCoapPrivateKey, lambda: Rituals.call(
        'ritual_ZN15QCoapPrivateKeyC1ERK10QByteArrayN4QSsl12KeyAlgorithmENS'
        '3_14EncodingFormatES2_',
        self._valueOf(key), algorithm.value, format.value,
        self._valueOf(passPhrase),
    ))

  @overload(THIS)
  def __init__(self, other: QCoapPrivateKey) -> None:
    """
    Notes what was given, for Qt's 'QCoapPrivateKey::QCoapPrivateKey(const
    QCoapPrivateKey &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapprivatekey.html#QCoapPrivateKey

    Parameters
    ----------

    other : QCoapPrivateKey
      Passed on as a value: Qt reads the C++ QCoapPrivateKey, which stays
      Python's own.
    """
    #  QCoapPrivateKey::QCoapPrivateKey(const QCoapPrivateKey &other)
    self._noteCreation(QCoapPrivateKey, lambda: Rituals.call(
        'ritual_ZN15QCoapPrivateKeyC1ERKS_', self._valueOf(other),
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
  def handle(*__, **_) -> Never:
    """
    Qt's 'Qt::HANDLE QCoapPrivateKey::handle() const': gives 'void', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QCoapPrivateKey.handle' has no cute function yet. Qt's "
        "'Qt::HANDLE QCoapPrivateKey::handle() const': gives 'void', which "
        "has no cute class yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QCoapPrivateKey::swap(QCoapPrivateKey &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCoapPrivateKey.swap' has no cute function yet. Qt's 'void "
        "QCoapPrivateKey::swap(QCoapPrivateKey &other)': takes a type "
        "Python has no way to hand over yet.")
