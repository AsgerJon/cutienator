"""
QNfcNdefNotifier binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNfc/6.12.0/QtNfc/private/qiosndefnotifier_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QNfcNdefNotifier to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QNearFieldTarget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QNdefMessage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QNdefMessage = WAIT['QNdefMessage']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QNfcNdefNotifier(QObject):
  """
  The cute side of Qt's QNfcNdefNotifier: a plain Python object standing in
  front of one C++ QNfcNdefNotifier.

  It is built on the cute 'QObject', as Qt's QNfcNdefNotifier is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QNfcNdefNotifier that has a ritual and that Python
  can call so far, 6 names in all: 'metaObject', 'tr', 'invalidateWithError',
  'tagError', 'ndefMessageWritten', 'ndefMessageRead'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QNfcNdefNotifier::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QNfcNdefNotifier::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QNfcNdefNotifier::tagDetected(void *tag)': names 'void', which
    has no cute class yet.
  - Qt's 'void QNfcNdefNotifier::tagLost(void *tag)': names 'void', which has
    no cute class yet.

  What has no ritual
  ------------------

  6 of the 17 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ QNfcNdefNotifier is created at the first use, not by
    'QNfcNdefNotifier(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNfcNdefNotifier.
  - Qt tells when it has removed the C++ QNfcNdefNotifier. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QNfcNdefNotifier that has no cute function yet,
    'tagDetected', 'tagLost', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

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
    Calls Qt's 'QString QNfcNdefNotifier::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qnfcndefnotifier.html#tr

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
    #  QString QNfcNdefNotifier::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QNfcNdefNotifier2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNfcNdefNotifier'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QNfcNdefNotifier::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnfcndefnotifier.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QNfcNdefNotifier::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QNfcNdefNotifier10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
    Notes what was given, for Qt's 'QNfcNdefNotifier::QNfcNdefNotifier()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnfcndefnotifier.html#QNfcNdefNotifier
    """
    #  QNfcNdefNotifier::QNfcNdefNotifier()
    self._noteCreation(QNfcNdefNotifier, lambda: Rituals.call(
        'ritual_ZN16QNfcNdefNotifierC1Ev',
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

  @overload(bool)
  def invalidateWithError(self, restart: bool) -> None:
    """
    Calls Qt's 'void QNfcNdefNotifier::invalidateWithError(bool restart)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnfcndefnotifier.html#invalidateWithError

    Parameters
    ----------

    restart : bool
      Passed on as it is.
    """
    #  void QNfcNdefNotifier::invalidateWithError(bool restart)
    self.uglySide.call(
        'ritual_ZN16QNfcNdefNotifier19invalidateWithErrorEb', restart,
    )

  @overload(QNearFieldTarget.Error, QNearFieldTarget.RequestId)
  def tagError(
      self,
      code: QNearFieldTarget.Error,
      request: QNearFieldTarget.RequestId,
  ) -> None:
    """
    Calls Qt's 'void QNfcNdefNotifier::tagError(QNearFieldTarget::Error code,
    QNearFieldTarget::RequestId request)'.

    Qt's own words: https://doc.qt.io/qt-6/qnfcndefnotifier.html#tagError

    Parameters
    ----------

    code : QNearFieldTarget.Error
      Passed on as its number.

    request : QNearFieldTarget.RequestId
      Passed on as a value: Qt reads the C++ QNearFieldTarget::RequestId,
      which stays Python's own.
    """
    #  void QNfcNdefNotifier::tagError(QNearFieldTarget::Error code,
    #      QNearFieldTarget::RequestId request)
    self.uglySide.call(
        'ritual_ZN16QNfcNdefNotifier8tagErrorEN16QNearFieldTarget5ErrorENS0'
        '_9RequestIdE',
        code.value, self._valueOf(request),
    )

  @overload(QNearFieldTarget.RequestId)
  def ndefMessageWritten(self, request: QNearFieldTarget.RequestId) -> None:
    """
    Calls Qt's 'void
    QNfcNdefNotifier::ndefMessageWritten(QNearFieldTarget::RequestId
    request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnfcndefnotifier.html#ndefMessageWritten

    Parameters
    ----------

    request : QNearFieldTarget.RequestId
      Passed on as a value: Qt reads the C++ QNearFieldTarget::RequestId,
      which stays Python's own.
    """
    #  void QNfcNdefNotifier::ndefMessageWritten(QNearFieldTarget::RequestId
    #      request)
    self.uglySide.call(
        'ritual_ZN16QNfcNdefNotifier18ndefMessageWrittenEN16QNearFieldTarge'
        't9RequestIdE',
        self._valueOf(request),
    )

  @overload(QNdefMessage, QNearFieldTarget.RequestId)
  def ndefMessageRead(
      self,
      message: QNdefMessage,
      request: QNearFieldTarget.RequestId,
  ) -> None:
    """
    Calls Qt's 'void QNfcNdefNotifier::ndefMessageRead(const QNdefMessage
    &message, QNearFieldTarget::RequestId request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnfcndefnotifier.html#ndefMessageRead

    Parameters
    ----------

    message : QNdefMessage
      Passed on as a value: Qt reads the C++ QNdefMessage, which stays
      Python's own.

    request : QNearFieldTarget.RequestId
      Passed on as a value: Qt reads the C++ QNearFieldTarget::RequestId,
      which stays Python's own.
    """
    #  void QNfcNdefNotifier::ndefMessageRead(const QNdefMessage &message,
    #      QNearFieldTarget::RequestId request)
    self.uglySide.call(
        'ritual_ZN16QNfcNdefNotifier15ndefMessageReadERK12QNdefMessageN16QN'
        'earFieldTarget9RequestIdE',
        self._valueOf(message), self._valueOf(request),
    )

  @staticmethod
  def tagDetected(*__, **_) -> Never:
    """
    Qt's 'void QNfcNdefNotifier::tagDetected(void *tag)': names 'void', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QNfcNdefNotifier.tagDetected' has no cute function yet. Qt's "
        "'void QNfcNdefNotifier::tagDetected(void *tag)': names 'void', "
        "which has no cute class yet.")

  @staticmethod
  def tagLost(*__, **_) -> Never:
    """
    Qt's 'void QNfcNdefNotifier::tagLost(void *tag)': names 'void', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QNfcNdefNotifier.tagLost' has no cute function yet. Qt's 'void "
        "QNfcNdefNotifier::tagLost(void *tag)': names 'void', which has no "
        "cute class yet.")
