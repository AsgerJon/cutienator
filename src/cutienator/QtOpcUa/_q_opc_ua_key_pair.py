"""
QOpcUaKeyPair binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuakeypair.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpcUaKeyPair(QObject):
  """
  The cute side of Qt's QOpcUaKeyPair: a plain Python object standing in
  front of one C++ QOpcUaKeyPair.

  It is built on the cute 'QObject', as Qt's QOpcUaKeyPair is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QOpcUaKeyPair that has a ritual and that Python can
  call so far, 8 names in all: 'metaObject', 'tr', 'loadFromPemData',
  'publicKeyToByteArray', 'privateKeyToByteArray', 'type', 'hasPrivateKey',
  'generateRsaKey'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QOpcUaKeyPair::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QOpcUaKeyPair::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QOpcUaKeyPairPrivate *QOpcUaKeyPair::d_func()': gives
    'QOpcUaKeyPairPrivate', which has no cute class yet.
  - Qt's 'const QOpcUaKeyPairPrivate *QOpcUaKeyPair::d_func() const': gives
    'QOpcUaKeyPairPrivate', which has no cute class yet.
  - Qt's 'QOpcUaKeyPair::~QOpcUaKeyPair()': the destructor: Python never
    removes a C++ QOpcUaKeyPair.
  - Qt's 'void QOpcUaKeyPair::passphraseNeeded(QString &passphrase, int
    maximumLength, bool writeOperation)': takes a type Python has no way to
    hand over yet.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QOpcUaKeyPair is created at the first use, not by
    'QOpcUaKeyPair(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpcUaKeyPair.
  - Qt tells when it has removed the C++ QOpcUaKeyPair. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QOpcUaKeyPair that has no cute function yet,
    'passphraseNeeded', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QOpcUaKeyPair, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Cipher(CuteNum, scoped=True):
    """
    The enum 'QOpcUaKeyPair::Cipher' of Qt, with the 2 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    Aes128Cbc = Kee[int](0)
    Unencrypted = Kee[int](1)

  class KeyType(CuteNum, scoped=True):
    """
    The enum 'QOpcUaKeyPair::KeyType' of Qt, with the 3 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    Rsa = Kee[int](0)
    Empty = Kee[int](1)
    Unknown = Kee[int](2)

  class RsaKeyStrength(CuteNum, scoped=True):
    """
    The enum 'QOpcUaKeyPair::RsaKeyStrength' of Qt, with the 3 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Bits1024 = Kee[int](1024)
    Bits2048 = Kee[int](2048)
    Bits4096 = Kee[int](4096)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QOpcUaKeyPair::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuakeypair.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaKeyPair::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QOpcUaKeyPair2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaKeyPair'

  #  A C++ QOpcUaKeyPair Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QOpcUaKeyPair'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QOpcUaKeyPair::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuakeypair.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QOpcUaKeyPair::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QOpcUaKeyPair10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def publicKeyToByteArray(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QOpcUaKeyPair::publicKeyToByteArray() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuakeypair.html#publicKeyToByteArray

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QOpcUaKeyPair::publicKeyToByteArray() const
    address = self.uglySide.call(
        'ritual_ZNK13QOpcUaKeyPair20publicKeyToByteArrayEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(Cipher, str)
  def privateKeyToByteArray(
      self,
      cipher: Cipher,
      password: str,
  ) -> QByteArray:
    """
    Calls Qt's 'QByteArray QOpcUaKeyPair::privateKeyToByteArray(Cipher
    cipher, const QString &password) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuakeypair.html#privateKeyToByteArray

    Parameters
    ----------

    cipher : Cipher
      Passed on as its number.

    password : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QOpcUaKeyPair::privateKeyToByteArray(Cipher cipher, const
    #      QString &password) const
    address = self.uglySide.call(
        'ritual_ZNK13QOpcUaKeyPair21privateKeyToByteArrayENS_6CipherERK7QSt'
        'ring',
        cipher.value, password,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def type(self) -> KeyType:
    """
    Calls Qt's 'KeyType QOpcUaKeyPair::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuakeypair.html#type

    Returns
    -------

    KeyType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'KeyType(number)' gives.
    """
    #  KeyType QOpcUaKeyPair::type() const
    return QOpcUaKeyPair.KeyType(self.uglySide.call(
        'ritual_ZNK13QOpcUaKeyPair4typeEv',
    ))

  def hasPrivateKey(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaKeyPair::hasPrivateKey() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuakeypair.html#hasPrivateKey
    """
    #  bool QOpcUaKeyPair::hasPrivateKey() const
    return self.uglySide.call('ritual_ZNK13QOpcUaKeyPair13hasPrivateKeyEv')

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QOpcUaKeyPair::QOpcUaKeyPair(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qopcuakeypair.html#QOpcUaKeyPair

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QOpcUaKeyPair::QOpcUaKeyPair(QObject *parent)
    self._noteCreation(QOpcUaKeyPair, lambda: Rituals.call(
        'ritual_ZN13QOpcUaKeyPairC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  @overload(QByteArray)
  def loadFromPemData(self, data: QByteArray) -> bool:
    """
    Calls Qt's 'bool QOpcUaKeyPair::loadFromPemData(const QByteArray &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuakeypair.html#loadFromPemData

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool QOpcUaKeyPair::loadFromPemData(const QByteArray &data)
    return self.uglySide.call(
        'ritual_ZN13QOpcUaKeyPair15loadFromPemDataERK10QByteArray',
        self._valueOf(data),
    )

  @overload(RsaKeyStrength)
  def generateRsaKey(self, strength: RsaKeyStrength) -> None:
    """
    Calls Qt's 'void
    QOpcUaKeyPair::generateRsaKey(QOpcUaKeyPair::RsaKeyStrength strength)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuakeypair.html#generateRsaKey

    Parameters
    ----------

    strength : RsaKeyStrength
      Passed on as its number.
    """
    #  void QOpcUaKeyPair::generateRsaKey(QOpcUaKeyPair::RsaKeyStrength
    #      strength)
    self.uglySide.call(
        'ritual_ZN13QOpcUaKeyPair14generateRsaKeyENS_14RsaKeyStrengthE',
        strength.value,
    )

  @staticmethod
  def passphraseNeeded(*__, **_) -> Never:
    """
    Qt's 'void QOpcUaKeyPair::passphraseNeeded(QString &passphrase, int
    maximumLength, bool writeOperation)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QOpcUaKeyPair.passphraseNeeded' has no cute function yet. Qt's "
        "'void QOpcUaKeyPair::passphraseNeeded(QString &passphrase, int "
        "maximumLength, bool writeOperation)': takes a type Python has no "
        "way to hand over yet.")
