"""
QTlsPrivate::TlsKey binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qtlsbackend_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QTlsPrivate::TlsKey to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from . import QSsl, QTlsPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class TlsKey(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTlsPrivate::TlsKey: a plain Python object standing
  in front of one C++ QTlsPrivate::TlsKey.

  What exists
  -----------

  Every function of Qt's QTlsPrivate::TlsKey that has a ritual and that
  Python can call so far, 13 names in all: 'decodeDer', 'decodePem', 'toPem',
  'isNull', 'type', 'algorithm', 'length', 'clear', 'isPkcs8', 'decrypt',
  'encrypt', 'pemHeader', 'pemFooter'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTlsPrivate::TlsKey::~TlsKey()': the destructor: Python never
    removes a C++ QTlsPrivate::TlsKey.
  - Qt's 'QByteArray QTlsPrivate::TlsKey::derFromPem(const QByteArray &pem,
    QMap<QByteArray, QByteArray> *headers) const': names 'QMap<QByteArray,
    QByteArray>', which has no cute class yet.
  - Qt's 'QByteArray QTlsPrivate::TlsKey::pemFromDer(const QByteArray &der,
    const QMap<QByteArray, QByteArray> &headers) const': takes a type Python
    has no way to hand over yet.
  - Qt's 'void QTlsPrivate::TlsKey::fromHandle(Qt::HANDLE handle, KeyType
    type)': names 'void', which has no cute class yet.
  - Qt's 'Qt::HANDLE QTlsPrivate::TlsKey::handle() const': gives 'void',
    which has no cute class yet.

  What has no ritual
  ------------------

  5 of the 23 functions Qt declares: 4 forbidden; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QTlsPrivate::TlsKey is created at the first use, not by
    'QTlsPrivate::TlsKey(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTlsPrivate::TlsKey.
  - Each name of Qt's QTlsPrivate::TlsKey that has no cute function yet,
    '__init__', 'derFromPem', 'fromHandle', 'handle', 'pemFromDer', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTlsPrivate::TlsKey'

  #  A C++ QTlsPrivate::TlsKey Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTlsPrivate_TlsKey'

  #  The functions Qt calls itself that QTlsPrivate::TlsKey is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'derFromPem': (
          'QByteArray QTlsPrivate::TlsKey::derFromPem(const QByteArray &, '
          'QMap<QByteArray, QByteArray> *) const',
      ),
      'pemFromDer': (
          'QByteArray QTlsPrivate::TlsKey::pemFromDer(const QByteArray &, '
          'const QMap<QByteArray, QByteArray> &) const',
      ),
      'fromHandle': (
          'void QTlsPrivate::TlsKey::fromHandle(Qt::HANDLE, KeyType)',
      ),
      'handle': (
          'Qt::HANDLE QTlsPrivate::TlsKey::handle() const',
      ),
  }

  #  The functions Qt calls itself that QTlsPrivate::TlsKey is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'decodeDer': (
          ('_ZN11QTlsPrivate6TlsKey9decodeDerEN4QSsl7KeyTypeENS1_12KeyAlgor'
           'ithmERK10QByteArrayS6_b',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtNetwork:QTlsPrivate.TlsKey.KeyType'),
               ('int', 'enum', 'QtNetwork:QTlsPrivate.TlsKey.KeyAlgorithm'),
               ('address', 'value', 'QtCore:QByteArray'),
               ('address', 'value', 'QtCore:QByteArray'),
               ('bool', 'number', ''),
           )),
      ),
      'decodePem': (
          ('_ZN11QTlsPrivate6TlsKey9decodePemEN4QSsl7KeyTypeENS1_12KeyAlgor'
           'ithmERK10QByteArrayS6_b',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtNetwork:QTlsPrivate.TlsKey.KeyType'),
               ('int', 'enum', 'QtNetwork:QTlsPrivate.TlsKey.KeyAlgorithm'),
               ('address', 'value', 'QtCore:QByteArray'),
               ('address', 'value', 'QtCore:QByteArray'),
               ('bool', 'number', ''),
           )),
      ),
      'toPem': (
          ('_ZNK11QTlsPrivate6TlsKey5toPemERK10QByteArray',
           ('address', 'value', 'QtCore:QByteArray'),
           (
               ('address', 'value', 'QtCore:QByteArray'),
           )),
      ),
      'isNull': (
          ('_ZNK11QTlsPrivate6TlsKey6isNullEv',
           ('bool', 'number', ''),
           ()),
      ),
      'type': (
          ('_ZNK11QTlsPrivate6TlsKey4typeEv',
           ('int', 'enum', 'QtNetwork:QTlsPrivate.TlsKey.KeyType'),
           ()),
      ),
      'algorithm': (
          ('_ZNK11QTlsPrivate6TlsKey9algorithmEv',
           ('int', 'enum', 'QtNetwork:QTlsPrivate.TlsKey.KeyAlgorithm'),
           ()),
      ),
      'length': (
          ('_ZNK11QTlsPrivate6TlsKey6lengthEv',
           ('int', 'number', ''),
           ()),
      ),
      'clear': (
          ('_ZN11QTlsPrivate6TlsKey5clearEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'isPkcs8': (
          ('_ZNK11QTlsPrivate6TlsKey7isPkcs8Ev',
           ('bool', 'number', ''),
           ()),
      ),
      'decrypt': (
          ('_ZNK11QTlsPrivate6TlsKey7decryptENS_6CipherERK10QByteArrayS4_S4'
           '_',
           ('address', 'value', 'QtCore:QByteArray'),
           (
               ('int', 'enum', 'QtNetwork:QTlsPrivate.Cipher'),
               ('address', 'value', 'QtCore:QByteArray'),
               ('address', 'value', 'QtCore:QByteArray'),
               ('address', 'value', 'QtCore:QByteArray'),
           )),
      ),
      'encrypt': (
          ('_ZNK11QTlsPrivate6TlsKey7encryptENS_6CipherERK10QByteArrayS4_S4'
           '_',
           ('address', 'value', 'QtCore:QByteArray'),
           (
               ('int', 'enum', 'QtNetwork:QTlsPrivate.Cipher'),
               ('address', 'value', 'QtCore:QByteArray'),
               ('address', 'value', 'QtCore:QByteArray'),
               ('address', 'value', 'QtCore:QByteArray'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QByteArray)
  def toPem(self, passPhrase: QByteArray) -> QByteArray:
    """
    Calls Qt's 'QByteArray QTlsPrivate::TlsKey::toPem(const QByteArray
    &passPhrase) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtlsprivate-tlskey.html#toPem

    Parameters
    ----------

    passPhrase : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QTlsPrivate::TlsKey::toPem(const QByteArray &passPhrase)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK11QTlsPrivate6TlsKey5toPemERK10QByteArray',
        self._valueOf(passPhrase),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QTlsPrivate::TlsKey::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtlsprivate-tlskey.html#isNull
    """
    #  bool QTlsPrivate::TlsKey::isNull() const
    return self.uglySide.call('ritual_ZNK11QTlsPrivate6TlsKey6isNullEv')

  def type(self) -> QSsl.KeyType:
    """
    Calls Qt's 'KeyType QTlsPrivate::TlsKey::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtlsprivate-tlskey.html#type

    Returns
    -------

    QSsl.KeyType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QSsl.KeyType(number)'
      gives.
    """
    #  KeyType QTlsPrivate::TlsKey::type() const
    return QSsl.KeyType(self.uglySide.call(
        'ritual_ZNK11QTlsPrivate6TlsKey4typeEv',
    ))

  def algorithm(self) -> QSsl.KeyAlgorithm:
    """
    Calls Qt's 'KeyAlgorithm QTlsPrivate::TlsKey::algorithm() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtlsprivate-tlskey.html#algorithm

    Returns
    -------

    QSsl.KeyAlgorithm
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSsl.KeyAlgorithm(number)' gives.
    """
    #  KeyAlgorithm QTlsPrivate::TlsKey::algorithm() const
    return QSsl.KeyAlgorithm(self.uglySide.call(
        'ritual_ZNK11QTlsPrivate6TlsKey9algorithmEv',
    ))

  def length(self) -> int:
    """
    Calls Qt's 'int QTlsPrivate::TlsKey::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtlsprivate-tlskey.html#length
    """
    #  int QTlsPrivate::TlsKey::length() const
    return self.uglySide.call('ritual_ZNK11QTlsPrivate6TlsKey6lengthEv')

  def isPkcs8(self) -> bool:
    """
    Calls Qt's 'bool QTlsPrivate::TlsKey::isPkcs8() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtlsprivate-tlskey.html#isPkcs8
    """
    #  bool QTlsPrivate::TlsKey::isPkcs8() const
    return self.uglySide.call('ritual_ZNK11QTlsPrivate6TlsKey7isPkcs8Ev')

  @overload(QTlsPrivate.Cipher, QByteArray, QByteArray, QByteArray)
  def decrypt(
      self,
      cipher: QTlsPrivate.Cipher,
      data: QByteArray,
      passPhrase: QByteArray,
      iv: QByteArray,
  ) -> QByteArray:
    """
    Calls Qt's 'QByteArray QTlsPrivate::TlsKey::decrypt(Cipher cipher, const
    QByteArray &data, const QByteArray &passPhrase, const QByteArray &iv)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtlsprivate-tlskey.html#decrypt

    Parameters
    ----------

    cipher : QTlsPrivate.Cipher
      Passed on as its number.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    passPhrase : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    iv : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QTlsPrivate::TlsKey::decrypt(Cipher cipher, const
    #      QByteArray &data, const QByteArray &passPhrase, const QByteArray
    #      &iv) const
    address = self.uglySide.call(
        'ritual_ZNK11QTlsPrivate6TlsKey7decryptENS_6CipherERK10QByteArrayS4'
        '_S4_',
        cipher.value, self._valueOf(data), self._valueOf(passPhrase),
        self._valueOf(iv),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(QTlsPrivate.Cipher, QByteArray, QByteArray, QByteArray)
  def encrypt(
      self,
      cipher: QTlsPrivate.Cipher,
      data: QByteArray,
      key: QByteArray,
      iv: QByteArray,
  ) -> QByteArray:
    """
    Calls Qt's 'QByteArray QTlsPrivate::TlsKey::encrypt(Cipher cipher, const
    QByteArray &data, const QByteArray &key, const QByteArray &iv) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtlsprivate-tlskey.html#encrypt

    Parameters
    ----------

    cipher : QTlsPrivate.Cipher
      Passed on as its number.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    key : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    iv : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QTlsPrivate::TlsKey::encrypt(Cipher cipher, const
    #      QByteArray &data, const QByteArray &key, const QByteArray &iv)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK11QTlsPrivate6TlsKey7encryptENS_6CipherERK10QByteArrayS4'
        '_S4_',
        cipher.value, self._valueOf(data), self._valueOf(key),
        self._valueOf(iv),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def pemHeader(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QTlsPrivate::TlsKey::pemHeader() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtlsprivate-tlskey.html#pemHeader

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QTlsPrivate::TlsKey::pemHeader() const
    address = self.uglySide.call(
        'ritual_ZNK11QTlsPrivate6TlsKey9pemHeaderEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def pemFooter(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QTlsPrivate::TlsKey::pemFooter() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtlsprivate-tlskey.html#pemFooter

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QTlsPrivate::TlsKey::pemFooter() const
    address = self.uglySide.call(
        'ritual_ZNK11QTlsPrivate6TlsKey9pemFooterEv',
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QTlsPrivate::TlsKey::TlsKey()': the class is abstract, so C++
    cannot make one, and the C++ class of ours does not fill in every
    function it leaves open.
    """
    raise NotImplementedError(
        "'QTlsPrivate.TlsKey.__init__' has no cute function yet. Qt's "
        "'QTlsPrivate::TlsKey::TlsKey()': the class is abstract, so C++ "
        "cannot make one, and the C++ class of ours does not fill in every "
        "function it leaves open.")

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

  @overload(QSsl.KeyType, QSsl.KeyAlgorithm, QByteArray, QByteArray, bool)
  def decodeDer(
      self,
      type: QSsl.KeyType,
      algorithm: QSsl.KeyAlgorithm,
      der: QByteArray,
      passPhrase: QByteArray,
      deepClear: bool,
  ) -> None:
    """
    Calls Qt's 'void QTlsPrivate::TlsKey::decodeDer(KeyType type,
    KeyAlgorithm algorithm, const QByteArray &der, const QByteArray
    &passPhrase, bool deepClear)'.

    Qt's own words: https://doc.qt.io/qt-6/qtlsprivate-tlskey.html#decodeDer

    Parameters
    ----------

    type : QSsl.KeyType
      Passed on as its number.

    algorithm : QSsl.KeyAlgorithm
      Passed on as its number.

    der : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    passPhrase : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    deepClear : bool
      Passed on as it is.
    """
    #  void QTlsPrivate::TlsKey::decodeDer(KeyType type, KeyAlgorithm
    #      algorithm, const QByteArray &der, const QByteArray &passPhrase,
    #      bool deepClear)
    self.uglySide.call(
        'ritual_ZN11QTlsPrivate6TlsKey9decodeDerEN4QSsl7KeyTypeENS1_12KeyAl'
        'gorithmERK10QByteArrayS6_b',
        type.value, algorithm.value, self._valueOf(der),
        self._valueOf(passPhrase), deepClear,
    )

  @overload(QSsl.KeyType, QSsl.KeyAlgorithm, QByteArray, QByteArray, bool)
  def decodePem(
      self,
      type: QSsl.KeyType,
      algorithm: QSsl.KeyAlgorithm,
      pem: QByteArray,
      passPhrase: QByteArray,
      deepClear: bool,
  ) -> None:
    """
    Calls Qt's 'void QTlsPrivate::TlsKey::decodePem(KeyType type,
    KeyAlgorithm algorithm, const QByteArray &pem, const QByteArray
    &passPhrase, bool deepClear)'.

    Qt's own words: https://doc.qt.io/qt-6/qtlsprivate-tlskey.html#decodePem

    Parameters
    ----------

    type : QSsl.KeyType
      Passed on as its number.

    algorithm : QSsl.KeyAlgorithm
      Passed on as its number.

    pem : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    passPhrase : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    deepClear : bool
      Passed on as it is.
    """
    #  void QTlsPrivate::TlsKey::decodePem(KeyType type, KeyAlgorithm
    #      algorithm, const QByteArray &pem, const QByteArray &passPhrase,
    #      bool deepClear)
    self.uglySide.call(
        'ritual_ZN11QTlsPrivate6TlsKey9decodePemEN4QSsl7KeyTypeENS1_12KeyAl'
        'gorithmERK10QByteArrayS6_b',
        type.value, algorithm.value, self._valueOf(pem),
        self._valueOf(passPhrase), deepClear,
    )

  @overload(bool)
  def clear(self, deepClear: bool) -> None:
    """
    Calls Qt's 'void QTlsPrivate::TlsKey::clear(bool deepClear)'.

    Qt's own words: https://doc.qt.io/qt-6/qtlsprivate-tlskey.html#clear

    Parameters
    ----------

    deepClear : bool
      Passed on as it is.
    """
    #  void QTlsPrivate::TlsKey::clear(bool deepClear)
    self.uglySide.call('ritual_ZN11QTlsPrivate6TlsKey5clearEb', deepClear)

  @staticmethod
  def derFromPem(*__, **_) -> Never:
    """
    Qt's 'QByteArray QTlsPrivate::TlsKey::derFromPem(const QByteArray &pem,
    QMap<QByteArray, QByteArray> *headers) const': names 'QMap<QByteArray,
    QByteArray>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QTlsPrivate.TlsKey.derFromPem' has no cute function yet. Qt's "
        "'QByteArray QTlsPrivate::TlsKey::derFromPem(const QByteArray &pem, "
        "QMap<QByteArray, QByteArray> *headers) const': names "
        "'QMap<QByteArray, QByteArray>', which has no cute class yet.")

  @staticmethod
  def fromHandle(*__, **_) -> Never:
    """
    Qt's 'void QTlsPrivate::TlsKey::fromHandle(Qt::HANDLE handle, KeyType
    type)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QTlsPrivate.TlsKey.fromHandle' has no cute function yet. Qt's "
        "'void QTlsPrivate::TlsKey::fromHandle(Qt::HANDLE handle, KeyType "
        "type)': names 'void', which has no cute class yet.")

  @staticmethod
  def handle(*__, **_) -> Never:
    """
    Qt's 'Qt::HANDLE QTlsPrivate::TlsKey::handle() const': gives 'void',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QTlsPrivate.TlsKey.handle' has no cute function yet. Qt's "
        "'Qt::HANDLE QTlsPrivate::TlsKey::handle() const': gives 'void', "
        "which has no cute class yet.")

  @staticmethod
  def pemFromDer(*__, **_) -> Never:
    """
    Qt's 'QByteArray QTlsPrivate::TlsKey::pemFromDer(const QByteArray &der,
    const QMap<QByteArray, QByteArray> &headers) const': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QTlsPrivate.TlsKey.pemFromDer' has no cute function yet. Qt's "
        "'QByteArray QTlsPrivate::TlsKey::pemFromDer(const QByteArray &der, "
        "const QMap<QByteArray, QByteArray> &headers) const': takes a type "
        "Python has no way to hand over yet.")
