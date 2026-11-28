"""
QMessageAuthenticationCode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qmessageauthenticationcode.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QCryptographicHash

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


class QMessageAuthenticationCode(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMessageAuthenticationCode: a plain Python object
  standing in front of one C++ QMessageAuthenticationCode.

  What exists
  -----------

  Every function of Qt's QMessageAuthenticationCode that has a ritual and
  that Python can call so far, 6 names in all: 'reset', 'setKey', 'addData',
  'resultView', 'result', 'hash'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMessageAuthenticationCode::QMessageAuthenticationCode(
    QMessageAuthenticationCode &&other)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QMessageAuthenticationCode::~QMessageAuthenticationCode()': the
    destructor: Python never removes a C++ QMessageAuthenticationCode.
  - Qt's 'QMessageAuthenticationCode
    &QMessageAuthenticationCode::operator=(QMessageAuthenticationCode
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'void QMessageAuthenticationCode::swap(QMessageAuthenticationCode
    &other)': takes a type Python has no way to hand over yet.
  - Qt's 'QByteArrayView QMessageAuthenticationCode::hashInto(QSpan<char>
    buffer, QByteArrayView message, QByteArrayView key,
    QCryptographicHash::Algorithm method)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QByteArrayView QMessageAuthenticationCode::hashInto(QSpan<uchar>
    buffer, QByteArrayView message, QByteArrayView key,
    QCryptographicHash::Algorithm method)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QByteArrayView
    QMessageAuthenticationCode::hashInto(QSpan<std::byte> buffer,
    QByteArrayView message, QByteArrayView key, QCryptographicHash::Algorithm
    method)': takes a type Python has no way to hand over yet.
  - Qt's 'QByteArrayView QMessageAuthenticationCode::hashInto(QSpan<char>
    buffer, QSpan<const QByteArrayView> messageParts, QByteArrayView key,
    QCryptographicHash::Algorithm method)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QByteArrayView QMessageAuthenticationCode::hashInto(QSpan<uchar>
    buffer, QSpan<const QByteArrayView> messageParts, QByteArrayView key,
    QCryptographicHash::Algorithm method)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QByteArrayView
    QMessageAuthenticationCode::hashInto(QSpan<std::byte> buffer, QSpan<const
    QByteArrayView> message, QByteArrayView key,
    QCryptographicHash::Algorithm method)': takes a type Python has no way to
    hand over yet.

  What has no ritual
  ------------------

  2 of the 21 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QMessageAuthenticationCode is created at the first use, not by
    'QMessageAuthenticationCode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMessageAuthenticationCode.
  - Each name of Qt's QMessageAuthenticationCode that has no cute function
    yet, 'hashInto', 'swap', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QByteArrayView, QByteArrayView, QCryptographicHash.Algorithm)
  def hash(
      message: QByteArrayView,
      key: QByteArrayView,
      method: QCryptographicHash.Algorithm,
  ) -> QByteArray:
    """
    Calls Qt's 'QByteArray QMessageAuthenticationCode::hash(QByteArrayView
    message, QByteArrayView key, QCryptographicHash::Algorithm method)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmessageauthenticationcode.html#hash

    Parameters
    ----------

    message : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    key : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    method : QCryptographicHash.Algorithm
      Passed on as its number.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QMessageAuthenticationCode::hash(QByteArrayView message,
    #      QByteArrayView key, QCryptographicHash::Algorithm method)
    address = Rituals.call(
        'ritual_ZN26QMessageAuthenticationCode4hashE14QByteArrayViewS0_N18Q'
        'CryptographicHash9AlgorithmE',
        CuteMixin._valueOf(message), CuteMixin._valueOf(key), method.value,
    )
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMessageAuthenticationCode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def resultView(self) -> QByteArrayView:
    """
    Calls Qt's 'QByteArrayView QMessageAuthenticationCode::resultView()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmessageauthenticationcode.html#resultView

    Returns
    -------

    QByteArrayView
      A new cute QByteArrayView around the copy Qt gave back. Python owns it.
    """
    #  QByteArrayView QMessageAuthenticationCode::resultView() const
    address = self.uglySide.call(
        'ritual_ZNK26QMessageAuthenticationCode10resultViewEv',
    )
    from . import QByteArrayView
    return QByteArrayView._cuteOwning(address)

  def result(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QMessageAuthenticationCode::result() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmessageauthenticationcode.html#result

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QMessageAuthenticationCode::result() const
    address = self.uglySide.call(
        'ritual_ZNK26QMessageAuthenticationCode6resultEv',
    )
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QByteArrayView)
  def setKey(self, key: QByteArrayView) -> None:
    """
    Calls Qt's 'void QMessageAuthenticationCode::setKey(QByteArrayView key)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmessageauthenticationcode.html#setKey

    Parameters
    ----------

    key : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  void QMessageAuthenticationCode::setKey(QByteArrayView key)
    self.uglySide.call(
        'ritual_ZN26QMessageAuthenticationCode6setKeyE14QByteArrayView',
        self._valueOf(key),
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

  @overload(QCryptographicHash.Algorithm)
  @overload(QCryptographicHash.Algorithm, QByteArrayView)
  def __init__(
      self,
      method: QCryptographicHash.Algorithm,
      key: Optional[QByteArrayView] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QMessageAuthenticationCode::QMessageAuthenticationCode(
    QCryptographicHash::Algorithm method, QByteArrayView key)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmessageauthenticationcode.html

    Parameters
    ----------

    method : QCryptographicHash.Algorithm
      Passed on as its number.

    key : Optional[QByteArrayView]
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own. May be left out, as in Qt: a new 'QByteArrayView()' is
      then passed on.
    """
    #  QMessageAuthenticationCode::QMessageAuthenticationCode(
    #      QCryptographicHash::Algorithm method, QByteArrayView key)
    if key is None:
      from . import QByteArrayView
      key = QByteArrayView()
    self._noteCreation(QMessageAuthenticationCode, lambda: Rituals.call(
        'ritual_ZN26QMessageAuthenticationCodeC1EN18QCryptographicHash9Algo'
        'rithmE14QByteArrayView',
        method.value, self._valueOf(key),
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
    Calls Qt's 'void QMessageAuthenticationCode::reset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmessageauthenticationcode.html#reset
    """
    #  void QMessageAuthenticationCode::reset()
    self.uglySide.call('ritual_ZN26QMessageAuthenticationCode5resetEv')

  @overload(str, int)
  @overload(NoneType, int)
  def addData(self, data: Optional[str], length: int) -> None:
    """
    Calls Qt's 'void QMessageAuthenticationCode::addData(const char *data,
    qsizetype length)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmessageauthenticationcode.html#addData

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    length : int
      Passed on as it is.
    """
    #  void QMessageAuthenticationCode::addData(const char *data, qsizetype
    #      length)
    self.uglySide.call(
        'ritual_ZN26QMessageAuthenticationCode7addDataEPKcx',
        self._bytesOf(data), length,
    )

  @overload(QByteArrayView)
  def addData(self, data: QByteArrayView) -> None:
    """
    Calls Qt's 'void QMessageAuthenticationCode::addData(QByteArrayView
    data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmessageauthenticationcode.html#addData

    Parameters
    ----------

    data : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  void QMessageAuthenticationCode::addData(QByteArrayView data)
    self.uglySide.call(
        'ritual_ZN26QMessageAuthenticationCode7addDataE14QByteArrayView',
        self._valueOf(data),
    )

  @overload(QIODevice)
  @overload(NoneType)
  def addData(self, device: Optional[QIODevice]) -> bool:
    """
    Calls Qt's 'bool QMessageAuthenticationCode::addData(QIODevice *device)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmessageauthenticationcode.html#addData

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QMessageAuthenticationCode::addData(QIODevice *device)
    return self.uglySide.call(
        'ritual_ZN26QMessageAuthenticationCode7addDataEP9QIODevice',
        self._addressOf(device),
    )

  @staticmethod
  def hashInto(*__, **_) -> Never:
    """
    - Qt's 'QByteArrayView QMessageAuthenticationCode::hashInto(QSpan<char>
      buffer, QByteArrayView message, QByteArrayView key,
      QCryptographicHash::Algorithm method)': takes a type Python has no way
      to hand over yet.
    - Qt's 'QByteArrayView QMessageAuthenticationCode::hashInto(QSpan<uchar>
      buffer, QByteArrayView message, QByteArrayView key,
      QCryptographicHash::Algorithm method)': takes a type Python has no way
      to hand over yet.
    - Qt's 'QByteArrayView
      QMessageAuthenticationCode::hashInto(QSpan<std::byte> buffer,
      QByteArrayView message, QByteArrayView key,
      QCryptographicHash::Algorithm method)': takes a type Python has no way
      to hand over yet.
    - Qt's 'QByteArrayView QMessageAuthenticationCode::hashInto(QSpan<char>
      buffer, QSpan<const QByteArrayView> messageParts, QByteArrayView key,
      QCryptographicHash::Algorithm method)': takes a type Python has no way
      to hand over yet.
    - Qt's 'QByteArrayView QMessageAuthenticationCode::hashInto(QSpan<uchar>
      buffer, QSpan<const QByteArrayView> messageParts, QByteArrayView key,
      QCryptographicHash::Algorithm method)': takes a type Python has no way
      to hand over yet.
    - Qt's 'QByteArrayView
      QMessageAuthenticationCode::hashInto(QSpan<std::byte> buffer,
      QSpan<const QByteArrayView> message, QByteArrayView key,
      QCryptographicHash::Algorithm method)': takes a type Python has no way
      to hand over yet.
    """
    raise NotImplementedError(
        "'QMessageAuthenticationCode.hashInto' has no cute function yet. "
        "Qt's 'QByteArrayView "
        "QMessageAuthenticationCode::hashInto(QSpan<char> buffer, "
        "QByteArrayView message, QByteArrayView key, "
        "QCryptographicHash::Algorithm method)': takes a type Python has no "
        "way to hand over yet. Qt's 'QByteArrayView "
        "QMessageAuthenticationCode::hashInto(QSpan<uchar> buffer, "
        "QByteArrayView message, QByteArrayView key, "
        "QCryptographicHash::Algorithm method)': takes a type Python has no "
        "way to hand over yet. Qt's 'QByteArrayView "
        "QMessageAuthenticationCode::hashInto(QSpan<std::byte> buffer, "
        "QByteArrayView message, QByteArrayView key, "
        "QCryptographicHash::Algorithm method)': takes a type Python has no "
        "way to hand over yet. Qt's 'QByteArrayView "
        "QMessageAuthenticationCode::hashInto(QSpan<char> buffer, "
        "QSpan<const QByteArrayView> messageParts, QByteArrayView key, "
        "QCryptographicHash::Algorithm method)': takes a type Python has no "
        "way to hand over yet. Qt's 'QByteArrayView "
        "QMessageAuthenticationCode::hashInto(QSpan<uchar> buffer, "
        "QSpan<const QByteArrayView> messageParts, QByteArrayView key, "
        "QCryptographicHash::Algorithm method)': takes a type Python has no "
        "way to hand over yet. Qt's 'QByteArrayView "
        "QMessageAuthenticationCode::hashInto(QSpan<std::byte> buffer, "
        "QSpan<const QByteArrayView> message, QByteArrayView key, "
        "QCryptographicHash::Algorithm method)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QMessageAuthenticationCode::swap(QMessageAuthenticationCode
    &other)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QMessageAuthenticationCode.swap' has no cute function yet. Qt's "
        "'void QMessageAuthenticationCode::swap(QMessageAuthenticationCode "
        "&other)': takes a type Python has no way to hand over yet.")
