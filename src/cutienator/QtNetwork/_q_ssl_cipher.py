"""
QSslCipher binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qsslcipher.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QList
from . import QSsl

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QSslCipher(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSslCipher: a plain Python object standing in front
  of one C++ QSslCipher.

  C++ hands a QSslCipher around as a copy, so every C++ QSslCipher behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSslCipher that has a ritual and that Python can
  call so far, 11 names in all: '__eq__', '__ne__', 'isNull', 'name',
  'supportedBits', 'usedBits', 'keyExchangeMethod', 'authenticationMethod',
  'encryptionMethod', 'protocolString', 'protocol'. It can be made from
  Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSslCipher &QSslCipher::operator=(QSslCipher &&other)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'QSslCipher &QSslCipher::operator=(const QSslCipher &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QSslCipher::~QSslCipher()': the destructor: Python removes its C++
    QSslCipher by it, and has no other use for it.
  - Qt's 'void QSslCipher::swap(QSslCipher &other)': takes a type Python has
    no way to hand over yet.

  What to expect
  --------------

  - The C++ QSslCipher is created at the first use, not by 'QSslCipher(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSslCipher back gives a copy the ritual made for
    Python, in a new cute QSslCipher.
  - Each name of Qt's QSslCipher that has no cute function yet, 'swap', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSslCipher'

  #  Qt's '~QSslCipher()'. Naming it makes this a value class: Python owns
  #  every C++ QSslCipher behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10QSslCipherD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QSslCipher::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslcipher.html#isNull
    """
    #  bool QSslCipher::isNull() const
    return self.uglySide.call('ritual_ZNK10QSslCipher6isNullEv')

  def name(self) -> str:
    """
    Calls Qt's 'QString QSslCipher::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslcipher.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSslCipher::name() const
    return self.uglySide.call('ritual_ZNK10QSslCipher4nameEv')

  def supportedBits(self) -> int:
    """
    Calls Qt's 'int QSslCipher::supportedBits() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslcipher.html#supportedBits
    """
    #  int QSslCipher::supportedBits() const
    return self.uglySide.call('ritual_ZNK10QSslCipher13supportedBitsEv')

  def usedBits(self) -> int:
    """
    Calls Qt's 'int QSslCipher::usedBits() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslcipher.html#usedBits
    """
    #  int QSslCipher::usedBits() const
    return self.uglySide.call('ritual_ZNK10QSslCipher8usedBitsEv')

  def keyExchangeMethod(self) -> str:
    """
    Calls Qt's 'QString QSslCipher::keyExchangeMethod() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslcipher.html#keyExchangeMethod

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSslCipher::keyExchangeMethod() const
    return self.uglySide.call('ritual_ZNK10QSslCipher17keyExchangeMethodEv')

  def authenticationMethod(self) -> str:
    """
    Calls Qt's 'QString QSslCipher::authenticationMethod() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslcipher.html#authenticationMethod

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSslCipher::authenticationMethod() const
    return self.uglySide.call(
        'ritual_ZNK10QSslCipher20authenticationMethodEv',
    )

  def encryptionMethod(self) -> str:
    """
    Calls Qt's 'QString QSslCipher::encryptionMethod() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslcipher.html#encryptionMethod

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSslCipher::encryptionMethod() const
    return self.uglySide.call('ritual_ZNK10QSslCipher16encryptionMethodEv')

  def protocolString(self) -> str:
    """
    Calls Qt's 'QString QSslCipher::protocolString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslcipher.html#protocolString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSslCipher::protocolString() const
    return self.uglySide.call('ritual_ZNK10QSslCipher14protocolStringEv')

  def protocol(self) -> QSsl.SslProtocol:
    """
    Calls Qt's 'QSsl::SslProtocol QSslCipher::protocol() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslcipher.html#protocol

    Returns
    -------

    QSsl.SslProtocol
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QSsl.SslProtocol(number)'
      gives.
    """
    #  QSsl::SslProtocol QSslCipher::protocol() const
    return QSsl.SslProtocol(self.uglySide.call(
        'ritual_ZNK10QSslCipher8protocolEv',
    ))

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
  def __eq__(self, other: QSslCipher) -> bool:
    """
    Calls Qt's 'bool QSslCipher::operator==(const QSslCipher &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslcipher.html#operator==

    Parameters
    ----------

    other : QSslCipher
      Passed on as a value: Qt reads the C++ QSslCipher, which stays Python's
      own.
    """
    #  bool QSslCipher::operator==(const QSslCipher &other) const
    return self.uglySide.call(
        'ritual_ZNK10QSslCiphereqERKS_', self._valueOf(other),
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
  def __ne__(self, other: QSslCipher) -> bool:
    """
    Calls Qt's 'bool QSslCipher::operator!=(const QSslCipher &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslcipher.html#operator!=

    Parameters
    ----------

    other : QSslCipher
      Passed on as a value: Qt reads the C++ QSslCipher, which stays Python's
      own.
    """
    #  bool QSslCipher::operator!=(const QSslCipher &other) const
    return self.uglySide.call(
        'ritual_ZNK10QSslCipherneERKS_', self._valueOf(other),
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
    Notes what was given, for Qt's 'QSslCipher::QSslCipher()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsslcipher.html#QSslCipher
    """
    #  QSslCipher::QSslCipher()
    self._noteCreation(QSslCipher, lambda: Rituals.call(
        'ritual_ZN10QSslCipherC1Ev',
    ))

  @overload(str)
  def __init__(self, name: str) -> None:
    """
    Notes what was given, for Qt's 'QSslCipher::QSslCipher(const QString
    &name)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsslcipher.html#QSslCipher

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QSslCipher::QSslCipher(const QString &name)
    self._noteCreation(QSslCipher, lambda: Rituals.call(
        'ritual_ZN10QSslCipherC1ERK7QString', name,
    ))

  @overload(str, QSsl.SslProtocol)
  def __init__(self, name: str, protocol: QSsl.SslProtocol) -> None:
    """
    Notes what was given, for Qt's 'QSslCipher::QSslCipher(const QString
    &name, QSsl::SslProtocol protocol)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsslcipher.html#QSslCipher

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    protocol : QSsl.SslProtocol
      Passed on as its number.
    """
    #  QSslCipher::QSslCipher(const QString &name, QSsl::SslProtocol
    #      protocol)
    self._noteCreation(QSslCipher, lambda: Rituals.call(
        'ritual_ZN10QSslCipherC1ERK7QStringN4QSsl11SslProtocolE',
        name, protocol.value,
    ))

  @overload(THIS)
  def __init__(self, other: QSslCipher) -> None:
    """
    Notes what was given, for Qt's 'QSslCipher::QSslCipher(const QSslCipher
    &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsslcipher.html#QSslCipher

    Parameters
    ----------

    other : QSslCipher
      Passed on as a value: Qt reads the C++ QSslCipher, which stays Python's
      own.
    """
    #  QSslCipher::QSslCipher(const QSslCipher &other)
    self._noteCreation(QSslCipher, lambda: Rituals.call(
        'ritual_ZN10QSslCipherC1ERKS_', self._valueOf(other),
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
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QSslCipher::swap(QSslCipher &other)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSslCipher.swap' has no cute function yet. Qt's 'void "
        "QSslCipher::swap(QSslCipher &other)': takes a type Python has no "
        "way to hand over yet.")


#  Qt's 'QList<QSslCipher>': the list of QSslCipher, which
#  'QList[QSslCipher]' gives. It is made here, so that there is one as soon
#  as there can be a QSslCipher.
QList.createKind(
    QSslCipher, 'value',
    make='ritual_list_make_QSslCipher',
    add='ritual_list_add_QSslCipher',
    size='ritual_list_size_QSslCipher',
    at='ritual_list_at_QSslCipher',
    drop='ritual_list_drop_QSslCipher',
)
