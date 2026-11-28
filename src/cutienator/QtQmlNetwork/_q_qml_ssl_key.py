"""
QQmlSslKey binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlNetwork/6.12.0/QtQmlNetwork/private/qqmlsslkey_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlSslKey to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtNetwork import QSsl

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QByteArray
  from ..QtNetwork import QSslKey
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QQmlSslKey(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlSslKey: a plain Python object standing in front
  of one C++ QQmlSslKey.

  C++ hands a QQmlSslKey around as a copy, so every C++ QQmlSslKey behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlSslKey that has a ritual and that Python can
  call so far, 12 names in all: 'getSslKey', 'keyFile', 'keyAlgorithm',
  'keyFormat', 'keyPassPhrase', 'keyType', 'setKeyFile', 'setKeyAlgorithm',
  'setKeyFormat', 'setKeyPassPhrase', 'setKeyType', '__eq__'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlSslKey::~QQmlSslKey()': the destructor: Python removes its C++
    QQmlSslKey by it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 16 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QQmlSslKey is created at the first use, not by 'QQmlSslKey(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlSslKey back gives a copy the ritual made for
    Python, in a new cute QQmlSslKey.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlSslKey'

  #  Qt's '~QQmlSslKey()'. Naming it makes this a value class: Python owns
  #  every C++ QQmlSslKey behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10QQmlSslKeyD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getSslKey(self) -> QSslKey:
    """
    Calls Qt's 'QSslKey QQmlSslKey::getSslKey() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsslkey.html#getSslKey

    Returns
    -------

    QSslKey
      A new cute QSslKey around the copy Qt gave back. Python owns it.
    """
    #  QSslKey QQmlSslKey::getSslKey() const
    address = self.uglySide.call('ritual_ZNK10QQmlSslKey9getSslKeyEv')
    from ..QtNetwork import QSslKey
    return QSslKey._cuteOwning(address)

  def keyFile(self) -> str:
    """
    Calls Qt's 'QString QQmlSslKey::keyFile() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsslkey.html#keyFile

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlSslKey::keyFile() const
    return self.uglySide.call('ritual_ZNK10QQmlSslKey7keyFileEv')

  def keyAlgorithm(self) -> QSsl.KeyAlgorithm:
    """
    Calls Qt's 'QSsl::KeyAlgorithm QQmlSslKey::keyAlgorithm() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsslkey.html#keyAlgorithm

    Returns
    -------

    QSsl.KeyAlgorithm
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSsl.KeyAlgorithm(number)' gives.
    """
    #  QSsl::KeyAlgorithm QQmlSslKey::keyAlgorithm() const
    return QSsl.KeyAlgorithm(self.uglySide.call(
        'ritual_ZNK10QQmlSslKey12keyAlgorithmEv',
    ))

  def keyFormat(self) -> QSsl.EncodingFormat:
    """
    Calls Qt's 'QSsl::EncodingFormat QQmlSslKey::keyFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsslkey.html#keyFormat

    Returns
    -------

    QSsl.EncodingFormat
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSsl.EncodingFormat(number)' gives.
    """
    #  QSsl::EncodingFormat QQmlSslKey::keyFormat() const
    return QSsl.EncodingFormat(self.uglySide.call(
        'ritual_ZNK10QQmlSslKey9keyFormatEv',
    ))

  def keyPassPhrase(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QQmlSslKey::keyPassPhrase() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsslkey.html#keyPassPhrase

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QQmlSslKey::keyPassPhrase() const
    address = self.uglySide.call('ritual_ZNK10QQmlSslKey13keyPassPhraseEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def keyType(self) -> QSsl.KeyType:
    """
    Calls Qt's 'QSsl::KeyType QQmlSslKey::keyType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsslkey.html#keyType

    Returns
    -------

    QSsl.KeyType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QSsl.KeyType(number)'
      gives.
    """
    #  QSsl::KeyType QQmlSslKey::keyType() const
    return QSsl.KeyType(self.uglySide.call(
        'ritual_ZNK10QQmlSslKey7keyTypeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setKeyFile(self, key: str) -> None:
    """
    Calls Qt's 'void QQmlSslKey::setKeyFile(const QString &key)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsslkey.html#setKeyFile

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlSslKey::setKeyFile(const QString &key)
    self.uglySide.call('ritual_ZN10QQmlSslKey10setKeyFileERK7QString', key)

  @overload(QSsl.KeyAlgorithm)
  def setKeyAlgorithm(self, value: QSsl.KeyAlgorithm) -> None:
    """
    Calls Qt's 'void QQmlSslKey::setKeyAlgorithm(QSsl::KeyAlgorithm value)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsslkey.html#setKeyAlgorithm

    Parameters
    ----------

    value : QSsl.KeyAlgorithm
      Passed on as its number.
    """
    #  void QQmlSslKey::setKeyAlgorithm(QSsl::KeyAlgorithm value)
    self.uglySide.call(
        'ritual_ZN10QQmlSslKey15setKeyAlgorithmEN4QSsl12KeyAlgorithmE',
        value.value,
    )

  @overload(QSsl.EncodingFormat)
  def setKeyFormat(self, value: QSsl.EncodingFormat) -> None:
    """
    Calls Qt's 'void QQmlSslKey::setKeyFormat(QSsl::EncodingFormat value)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsslkey.html#setKeyFormat

    Parameters
    ----------

    value : QSsl.EncodingFormat
      Passed on as its number.
    """
    #  void QQmlSslKey::setKeyFormat(QSsl::EncodingFormat value)
    self.uglySide.call(
        'ritual_ZN10QQmlSslKey12setKeyFormatEN4QSsl14EncodingFormatE',
        value.value,
    )

  @overload(QByteArray)
  def setKeyPassPhrase(self, value: QByteArray) -> None:
    """
    Calls Qt's 'void QQmlSslKey::setKeyPassPhrase(const QByteArray &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsslkey.html#setKeyPassPhrase

    Parameters
    ----------

    value : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QQmlSslKey::setKeyPassPhrase(const QByteArray &value)
    self.uglySide.call(
        'ritual_ZN10QQmlSslKey16setKeyPassPhraseERK10QByteArray',
        self._valueOf(value),
    )

  @overload(QSsl.KeyType)
  def setKeyType(self, type: QSsl.KeyType) -> None:
    """
    Calls Qt's 'void QQmlSslKey::setKeyType(QSsl::KeyType type)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsslkey.html#setKeyType

    Parameters
    ----------

    type : QSsl.KeyType
      Passed on as its number.
    """
    #  void QQmlSslKey::setKeyType(QSsl::KeyType type)
    self.uglySide.call(
        'ritual_ZN10QQmlSslKey10setKeyTypeEN4QSsl7KeyTypeE', type.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rvalue: QQmlSslKey) -> bool:
    """
    Calls Qt's 'bool operator==(const QQmlSslKey &lvalue, const QQmlSslKey
    &rvalue)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsslkey.html#operator==

    Parameters
    ----------

    rvalue : QQmlSslKey
      Passed on as a value: Qt reads the C++ QQmlSslKey, which stays Python's
      own.
    """
    #  bool operator==(const QQmlSslKey &lvalue, const QQmlSslKey &rvalue)
    return Rituals.call(
        'ritual_ZeqRK10QQmlSslKeyS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rvalue),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
