"""
QCryptographicHash binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qcryptographichash.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QByteArray, QByteArrayView, QIODevice
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArrayView = WAIT['QByteArrayView']
  QIODevice = WAIT['QIODevice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCryptographicHash(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCryptographicHash: a plain Python object standing in
  front of one C++ QCryptographicHash.

  What exists
  -----------

  Every function of Qt's QCryptographicHash that has a ritual and that Python
  can call so far, 8 names in all: 'reset', 'algorithm', 'addData', 'result',
  'resultView', 'hash', 'hashLength', 'supportsAlgorithm'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCryptographicHash::QCryptographicHash(QCryptographicHash
    &&other)': takes a type Python has no way to hand over yet.
  - Qt's 'QCryptographicHash::~QCryptographicHash()': the destructor: Python
    never removes a C++ QCryptographicHash.
  - Qt's 'QCryptographicHash
    &QCryptographicHash::operator=(QCryptographicHash &&other)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'void QCryptographicHash::swap(QCryptographicHash &other)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QByteArrayView QCryptographicHash::hashInto(QSpan<char> buffer,
    QByteArrayView data, Algorithm method)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QByteArrayView QCryptographicHash::hashInto(QSpan<uchar> buffer,
    QByteArrayView data, Algorithm method)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QByteArrayView QCryptographicHash::hashInto(QSpan<std::byte>
    buffer, QByteArrayView data, Algorithm method)': takes a type Python has
    no way to hand over yet.
  - Qt's 'QByteArrayView QCryptographicHash::hashInto(QSpan<char> buffer,
    QSpan<const QByteArrayView> data, Algorithm method)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QByteArrayView QCryptographicHash::hashInto(QSpan<uchar> buffer,
    QSpan<const QByteArrayView> data, Algorithm method)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QByteArrayView QCryptographicHash::hashInto(QSpan<std::byte>
    buffer, QSpan<const QByteArrayView> data, Algorithm method)': takes a
    type Python has no way to hand over yet.

  What has no ritual
  ------------------

  5 of the 26 functions Qt declares: 3 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QCryptographicHash is created at the first use, not by
    'QCryptographicHash(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCryptographicHash.
  - Each name of Qt's QCryptographicHash that has no cute function yet,
    'hashInto', 'swap', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QCryptographicHash, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Algorithm(CuteNum):
    """
    The enum 'QCryptographicHash::Algorithm' of Qt, with the 28 names Qt
    gives in it.
    """

    Md4 = Kee[int](0)
    Md5 = Kee[int](1)
    Sha1 = Kee[int](2)
    Sha224 = Kee[int](3)
    Sha256 = Kee[int](4)
    Sha384 = Kee[int](5)
    Sha512 = Kee[int](6)
    Keccak_224 = Kee[int](7)
    Keccak_256 = Kee[int](8)
    Keccak_384 = Kee[int](9)
    Keccak_512 = Kee[int](10)
    RealSha3_224 = Kee[int](11)
    RealSha3_256 = Kee[int](12)
    RealSha3_384 = Kee[int](13)
    RealSha3_512 = Kee[int](14)
    Sha3_224 = Kee[int](11)
    Sha3_256 = Kee[int](12)
    Sha3_384 = Kee[int](13)
    Sha3_512 = Kee[int](14)
    Blake2b_160 = Kee[int](15)
    Blake2b_256 = Kee[int](16)
    Blake2b_384 = Kee[int](17)
    Blake2b_512 = Kee[int](18)
    Blake2s_128 = Kee[int](19)
    Blake2s_160 = Kee[int](20)
    Blake2s_224 = Kee[int](21)
    Blake2s_256 = Kee[int](22)
    NumAlgorithms = Kee[int](23)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QByteArrayView, Algorithm)
  def hash(data: QByteArrayView, method: Algorithm) -> QByteArray:
    """
    Calls Qt's 'QByteArray QCryptographicHash::hash(QByteArrayView data,
    Algorithm method)'.

    Qt's own words: https://doc.qt.io/qt-6/qcryptographichash.html#hash

    Parameters
    ----------

    data : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    method : Algorithm
      Passed on as its number.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QCryptographicHash::hash(QByteArrayView data, Algorithm
    #      method)
    address = Rituals.call(
        'ritual_ZN18QCryptographicHash4hashE14QByteArrayViewNS_9AlgorithmE',
        CuteMixin._valueOf(data), method.value,
    )
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  @staticmethod
  @overload(Algorithm)
  def hashLength(method: Algorithm) -> int:
    """
    Calls Qt's 'int QCryptographicHash::hashLength(Algorithm method)'.

    Qt's own words: https://doc.qt.io/qt-6/qcryptographichash.html#hashLength

    Parameters
    ----------

    method : Algorithm
      Passed on as its number.
    """
    #  int QCryptographicHash::hashLength(Algorithm method)
    return Rituals.call(
        'ritual_ZN18QCryptographicHash10hashLengthENS_9AlgorithmE',
        method.value,
    )

  @staticmethod
  @overload(Algorithm)
  def supportsAlgorithm(method: Algorithm) -> bool:
    """
    Calls Qt's 'bool QCryptographicHash::supportsAlgorithm(Algorithm
    method)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcryptographichash.html#supportsAlgorithm

    Parameters
    ----------

    method : Algorithm
      Passed on as its number.
    """
    #  bool QCryptographicHash::supportsAlgorithm(Algorithm method)
    return Rituals.call(
        'ritual_ZN18QCryptographicHash17supportsAlgorithmENS_9AlgorithmE',
        method.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCryptographicHash'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def algorithm(self) -> Algorithm:
    """
    Calls Qt's 'Algorithm QCryptographicHash::algorithm() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcryptographichash.html#algorithm

    Returns
    -------

    Algorithm
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Algorithm(number)' gives.
    """
    #  Algorithm QCryptographicHash::algorithm() const
    return QCryptographicHash.Algorithm(self.uglySide.call(
        'ritual_ZNK18QCryptographicHash9algorithmEv',
    ))

  def result(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QCryptographicHash::result() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcryptographichash.html#result

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QCryptographicHash::result() const
    address = self.uglySide.call('ritual_ZNK18QCryptographicHash6resultEv')
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  def resultView(self) -> QByteArrayView:
    """
    Calls Qt's 'QByteArrayView QCryptographicHash::resultView() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcryptographichash.html#resultView

    Returns
    -------

    QByteArrayView
      A new cute QByteArrayView around the copy Qt gave back. Python owns it.
    """
    #  QByteArrayView QCryptographicHash::resultView() const
    address = self.uglySide.call(
        'ritual_ZNK18QCryptographicHash10resultViewEv',
    )
    from . import QByteArrayView
    return QByteArrayView._cuteOwning(address)

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

  @overload(Algorithm)
  def __init__(self, method: Algorithm) -> None:
    """
    Notes what was given, for Qt's
    'QCryptographicHash::QCryptographicHash(Algorithm method)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcryptographichash.html#QCryptographicHash

    Parameters
    ----------

    method : Algorithm
      Passed on as its number.
    """
    #  QCryptographicHash::QCryptographicHash(Algorithm method)
    self._noteCreation(QCryptographicHash, lambda: Rituals.call(
        'ritual_ZN18QCryptographicHashC1ENS_9AlgorithmE', method.value,
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

  def reset(self) -> None:
    """
    Calls Qt's 'void QCryptographicHash::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qcryptographichash.html#reset
    """
    #  void QCryptographicHash::reset()
    self.uglySide.call('ritual_ZN18QCryptographicHash5resetEv')

  @overload(str, int)
  @overload(NoneType, int)
  def addData(self, data: Optional[str], length: int) -> None:
    """
    Calls Qt's 'void QCryptographicHash::addData(const char *data, qsizetype
    length)'.

    Qt's own words: https://doc.qt.io/qt-6/qcryptographichash.html#addData

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    length : int
      Passed on as it is.
    """
    #  void QCryptographicHash::addData(const char *data, qsizetype length)
    self.uglySide.call(
        'ritual_ZN18QCryptographicHash7addDataEPKcx',
        self._bytesOf(data), length,
    )

  @overload(QByteArrayView)
  def addData(self, data: QByteArrayView) -> None:
    """
    Calls Qt's 'void QCryptographicHash::addData(QByteArrayView data)'.

    Qt's own words: https://doc.qt.io/qt-6/qcryptographichash.html#addData

    Parameters
    ----------

    data : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  void QCryptographicHash::addData(QByteArrayView data)
    self.uglySide.call(
        'ritual_ZN18QCryptographicHash7addDataE14QByteArrayView',
        self._valueOf(data),
    )

  @overload(QIODevice)
  @overload(NoneType)
  def addData(self, device: Optional[QIODevice]) -> bool:
    """
    Calls Qt's 'bool QCryptographicHash::addData(QIODevice *device)'.

    Qt's own words: https://doc.qt.io/qt-6/qcryptographichash.html#addData

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCryptographicHash::addData(QIODevice *device)
    return self.uglySide.call(
        'ritual_ZN18QCryptographicHash7addDataEP9QIODevice',
        self._addressOf(device),
    )

  @staticmethod
  def hashInto(*__, **_) -> Never:
    """
    - Qt's 'QByteArrayView QCryptographicHash::hashInto(QSpan<char> buffer,
      QByteArrayView data, Algorithm method)': takes a type Python has no way
      to hand over yet.
    - Qt's 'QByteArrayView QCryptographicHash::hashInto(QSpan<uchar> buffer,
      QByteArrayView data, Algorithm method)': takes a type Python has no way
      to hand over yet.
    - Qt's 'QByteArrayView QCryptographicHash::hashInto(QSpan<std::byte>
      buffer, QByteArrayView data, Algorithm method)': takes a type Python
      has no way to hand over yet.
    - Qt's 'QByteArrayView QCryptographicHash::hashInto(QSpan<char> buffer,
      QSpan<const QByteArrayView> data, Algorithm method)': takes a type
      Python has no way to hand over yet.
    - Qt's 'QByteArrayView QCryptographicHash::hashInto(QSpan<uchar> buffer,
      QSpan<const QByteArrayView> data, Algorithm method)': takes a type
      Python has no way to hand over yet.
    - Qt's 'QByteArrayView QCryptographicHash::hashInto(QSpan<std::byte>
      buffer, QSpan<const QByteArrayView> data, Algorithm method)': takes a
      type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCryptographicHash.hashInto' has no cute function yet. Qt's "
        "'QByteArrayView QCryptographicHash::hashInto(QSpan<char> buffer, "
        "QByteArrayView data, Algorithm method)': takes a type Python has "
        "no way to hand over yet. Qt's 'QByteArrayView "
        "QCryptographicHash::hashInto(QSpan<uchar> buffer, QByteArrayView "
        "data, Algorithm method)': takes a type Python has no way to hand "
        "over yet. Qt's 'QByteArrayView "
        "QCryptographicHash::hashInto(QSpan<std::byte> buffer, "
        "QByteArrayView data, Algorithm method)': takes a type Python has "
        "no way to hand over yet. Qt's 'QByteArrayView "
        "QCryptographicHash::hashInto(QSpan<char> buffer, QSpan<const "
        "QByteArrayView> data, Algorithm method)': takes a type Python has "
        "no way to hand over yet. Qt's 'QByteArrayView "
        "QCryptographicHash::hashInto(QSpan<uchar> buffer, QSpan<const "
        "QByteArrayView> data, Algorithm method)': takes a type Python has "
        "no way to hand over yet. Qt's 'QByteArrayView "
        "QCryptographicHash::hashInto(QSpan<std::byte> buffer, QSpan<const "
        "QByteArrayView> data, Algorithm method)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QCryptographicHash::swap(QCryptographicHash &other)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCryptographicHash.swap' has no cute function yet. Qt's 'void "
        "QCryptographicHash::swap(QCryptographicHash &other)': takes a type "
        "Python has no way to hand over yet.")
