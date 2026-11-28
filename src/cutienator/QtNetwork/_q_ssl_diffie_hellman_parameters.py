"""
QSslDiffieHellmanParameters binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qssldiffiehellmanparameters.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QSsl

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QDebug, QIODevice
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QDebug = WAIT['QDebug']
  QIODevice = WAIT['QIODevice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSslDiffieHellmanParameters(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSslDiffieHellmanParameters: a plain Python object
  standing in front of one C++ QSslDiffieHellmanParameters.

  C++ hands a QSslDiffieHellmanParameters around as a copy, so every C++
  QSslDiffieHellmanParameters behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QSslDiffieHellmanParameters that has a ritual and
  that Python can call so far, 10 names in all: 'defaultParameters',
  'fromEncoded', 'isEmpty', 'isValid', 'error', 'errorString', 'isEqual',
  '__eq__', '__ne__', '__rlshift__'. It can be made from Python, in 2 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSslDiffieHellmanParameters::QSslDiffieHellmanParameters(
    QSslDiffieHellmanParameters &&other)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QSslDiffieHellmanParameters::~QSslDiffieHellmanParameters()': the
    destructor: Python removes its C++ QSslDiffieHellmanParameters by it, and
    has no other use for it.
  - Qt's 'QSslDiffieHellmanParameters
    &QSslDiffieHellmanParameters::operator=(const QSslDiffieHellmanParameters
    &other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QSslDiffieHellmanParameters
    &QSslDiffieHellmanParameters::operator=(QSslDiffieHellmanParameters
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'void QSslDiffieHellmanParameters::swap(QSslDiffieHellmanParameters
    &other)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QSslDiffieHellmanParameters is created at the first use, not by
    'QSslDiffieHellmanParameters(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSslDiffieHellmanParameters back gives a copy the
    ritual made for Python, in a new cute QSslDiffieHellmanParameters.
  - Each name of Qt's QSslDiffieHellmanParameters that has no cute function
    yet, 'swap', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QSslDiffieHellmanParameters, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Error(CuteNum):
    """
    The enum 'QSslDiffieHellmanParameters::Error' of Qt, with the 3 names Qt
    gives in it.
    """

    NoError = Kee[int](0)
    InvalidInputDataError = Kee[int](1)
    UnsafeParametersError = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def defaultParameters() -> QSslDiffieHellmanParameters:
    """
    Calls Qt's 'QSslDiffieHellmanParameters
    QSslDiffieHellmanParameters::defaultParameters()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssldiffiehellmanparameters.html#defaultParameters

    Returns
    -------

    QSslDiffieHellmanParameters
      A new cute QSslDiffieHellmanParameters around the copy Qt gave back.
      Python owns it.
    """
    #  QSslDiffieHellmanParameters
    #      QSslDiffieHellmanParameters::defaultParameters()
    address = Rituals.call(
        'ritual_ZN27QSslDiffieHellmanParameters17defaultParametersEv',
    )
    return QSslDiffieHellmanParameters._cuteOwning(address)

  @staticmethod
  @overload(QByteArray)
  @overload(QByteArray, QSsl.EncodingFormat)
  def fromEncoded(
      encoded: QByteArray,
      format: QSsl.EncodingFormat = QSsl.EncodingFormat.Pem,
  ) -> QSslDiffieHellmanParameters:
    """
    Calls Qt's 'QSslDiffieHellmanParameters
    QSslDiffieHellmanParameters::fromEncoded(const QByteArray &encoded,
    QSsl::EncodingFormat format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssldiffiehellmanparameters.html#fromEncoded

    Parameters
    ----------

    encoded : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    format : QSsl.EncodingFormat
      Passed on as its number. May be left out, as in Qt: it is then
      QSsl.EncodingFormat.Pem.

    Returns
    -------

    QSslDiffieHellmanParameters
      A new cute QSslDiffieHellmanParameters around the copy Qt gave back.
      Python owns it.
    """
    #  QSslDiffieHellmanParameters
    #      QSslDiffieHellmanParameters::fromEncoded(const QByteArray
    #      &encoded, QSsl::EncodingFormat format)
    address = Rituals.call(
        'ritual_ZN27QSslDiffieHellmanParameters11fromEncodedERK10QByteArray'
        'N4QSsl14EncodingFormatE',
        CuteMixin._valueOf(encoded), format.value,
    )
    return QSslDiffieHellmanParameters._cuteOwning(address)

  @staticmethod
  @overload(QIODevice)
  @overload(NoneType)
  @overload(QIODevice, QSsl.EncodingFormat)
  @overload(NoneType, QSsl.EncodingFormat)
  def fromEncoded(
      device: Optional[QIODevice],
      format: QSsl.EncodingFormat = QSsl.EncodingFormat.Pem,
  ) -> QSslDiffieHellmanParameters:
    """
    Calls Qt's 'QSslDiffieHellmanParameters
    QSslDiffieHellmanParameters::fromEncoded(QIODevice *device,
    QSsl::EncodingFormat format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssldiffiehellmanparameters.html#fromEncoded

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    format : QSsl.EncodingFormat
      Passed on as its number. May be left out, as in Qt: it is then
      QSsl.EncodingFormat.Pem.

    Returns
    -------

    QSslDiffieHellmanParameters
      A new cute QSslDiffieHellmanParameters around the copy Qt gave back.
      Python owns it.
    """
    #  QSslDiffieHellmanParameters
    #      QSslDiffieHellmanParameters::fromEncoded(QIODevice *device,
    #      QSsl::EncodingFormat format)
    address = Rituals.call(
        'ritual_ZN27QSslDiffieHellmanParameters11fromEncodedEP9QIODeviceN4Q'
        'Ssl14EncodingFormatE',
        CuteMixin._addressOf(device), format.value,
    )
    return QSslDiffieHellmanParameters._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSslDiffieHellmanParameters'

  #  Qt's '~QSslDiffieHellmanParameters()'. Naming it makes this a value
  #  class: Python owns every C++ QSslDiffieHellmanParameters behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN27QSslDiffieHellmanParametersD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QSslDiffieHellmanParameters::isEmpty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssldiffiehellmanparameters.html#isEmpty
    """
    #  bool QSslDiffieHellmanParameters::isEmpty() const
    return self.uglySide.call(
        'ritual_ZNK27QSslDiffieHellmanParameters7isEmptyEv',
    )

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QSslDiffieHellmanParameters::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssldiffiehellmanparameters.html#isValid
    """
    #  bool QSslDiffieHellmanParameters::isValid() const
    return self.uglySide.call(
        'ritual_ZNK27QSslDiffieHellmanParameters7isValidEv',
    )

  def error(self) -> Error:
    """
    Calls Qt's 'Error QSslDiffieHellmanParameters::error() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssldiffiehellmanparameters.html#error

    Returns
    -------

    Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Error(number)' gives.
    """
    #  Error QSslDiffieHellmanParameters::error() const
    return QSslDiffieHellmanParameters.Error(self.uglySide.call(
        'ritual_ZNK27QSslDiffieHellmanParameters5errorEv',
    ))

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QSslDiffieHellmanParameters::errorString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssldiffiehellmanparameters.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSslDiffieHellmanParameters::errorString() const
    return self.uglySide.call(
        'ritual_ZNK27QSslDiffieHellmanParameters11errorStringEv',
    )

  @overload(THIS)
  def isEqual(self, other: QSslDiffieHellmanParameters) -> bool:
    """
    Calls Qt's 'bool QSslDiffieHellmanParameters::isEqual(const
    QSslDiffieHellmanParameters &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssldiffiehellmanparameters.html#isEqual

    Parameters
    ----------

    other : QSslDiffieHellmanParameters
      Passed on as a value: Qt reads the C++ QSslDiffieHellmanParameters,
      which stays Python's own.
    """
    #  bool QSslDiffieHellmanParameters::isEqual(const
    #      QSslDiffieHellmanParameters &other) const
    return self.uglySide.call(
        'ritual_ZNK27QSslDiffieHellmanParameters7isEqualERKS_',
        self._valueOf(other),
    )

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
  def __eq__(self, rhs: QSslDiffieHellmanParameters) -> bool:
    """
    Calls Qt's 'bool operator==(const QSslDiffieHellmanParameters &lhs, const
    QSslDiffieHellmanParameters &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssldiffiehellmanparameters.html#operator==

    Parameters
    ----------

    rhs : QSslDiffieHellmanParameters
      Passed on as a value: Qt reads the C++ QSslDiffieHellmanParameters,
      which stays Python's own.
    """
    #  bool operator==(const QSslDiffieHellmanParameters &lhs, const
    #      QSslDiffieHellmanParameters &rhs)
    return Rituals.call(
        'ritual_ZeqRK27QSslDiffieHellmanParametersS1_',
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
  def __ne__(self, rhs: QSslDiffieHellmanParameters) -> bool:
    """
    Calls Qt's 'bool operator!=(const QSslDiffieHellmanParameters &lhs, const
    QSslDiffieHellmanParameters &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssldiffiehellmanparameters.html#operator!=

    Parameters
    ----------

    rhs : QSslDiffieHellmanParameters
      Passed on as a value: Qt reads the C++ QSslDiffieHellmanParameters,
      which stays Python's own.
    """
    #  bool operator!=(const QSslDiffieHellmanParameters &lhs, const
    #      QSslDiffieHellmanParameters &rhs)
    return Rituals.call(
        'ritual_ZneRK27QSslDiffieHellmanParametersS1_',
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
    Calls Qt's 'QDebug operator<<(QDebug debug, const
    QSslDiffieHellmanParameters &dhparam)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssldiffiehellmanparameters.html#operator<<

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
    #  QDebug operator<<(QDebug debug, const QSslDiffieHellmanParameters
    #      &dhparam)
    address = Rituals.call(
        'ritual_Zls6QDebugRK27QSslDiffieHellmanParameters',
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
    'QSslDiffieHellmanParameters::QSslDiffieHellmanParameters()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssldiffiehellmanparameters.html
    """
    #  QSslDiffieHellmanParameters::QSslDiffieHellmanParameters()
    self._noteCreation(QSslDiffieHellmanParameters, lambda: Rituals.call(
        'ritual_ZN27QSslDiffieHellmanParametersC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QSslDiffieHellmanParameters) -> None:
    """
    Notes what was given, for Qt's
    'QSslDiffieHellmanParameters::QSslDiffieHellmanParameters(const
    QSslDiffieHellmanParameters &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssldiffiehellmanparameters.html

    Parameters
    ----------

    other : QSslDiffieHellmanParameters
      Passed on as a value: Qt reads the C++ QSslDiffieHellmanParameters,
      which stays Python's own.
    """
    #  QSslDiffieHellmanParameters::QSslDiffieHellmanParameters(const
    #      QSslDiffieHellmanParameters &other)
    self._noteCreation(QSslDiffieHellmanParameters, lambda: Rituals.call(
        'ritual_ZN27QSslDiffieHellmanParametersC1ERKS_',
        self._valueOf(other),
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
    Qt's 'void QSslDiffieHellmanParameters::swap(QSslDiffieHellmanParameters
    &other)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSslDiffieHellmanParameters.swap' has no cute function yet. Qt's "
        "'void "
        "QSslDiffieHellmanParameters::swap(QSslDiffieHellmanParameters "
        "&other)': takes a type Python has no way to hand over yet.")
