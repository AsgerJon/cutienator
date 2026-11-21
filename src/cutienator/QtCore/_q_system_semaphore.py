"""
QSystemSemaphore binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qsystemsemaphore.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from . import QSystemSemaphoreAccessMode
from . import QSystemSemaphoreSystemSemaphoreError

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSystemSemaphore(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSystemSemaphore: a plain Python object standing in
  front of one C++ QSystemSemaphore.

  What exists
  -----------

  Every function of Qt's QSystemSemaphore that has a ritual and that Python
  can call so far, 7 names in all: 'tr', 'setKey', 'key', 'acquire',
  'release', 'error', 'errorString'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSystemSemaphore::QSystemSemaphore(const QNativeIpcKey &key, int
    initialValue, AccessMode a2)': names 'QNativeIpcKey', which has no cute
    class yet.
  - Qt's 'QSystemSemaphore::~QSystemSemaphore()': the destructor: Python
    never removes a C++ QSystemSemaphore.
  - Qt's 'void QSystemSemaphore::setNativeKey(const QNativeIpcKey &key, int
    initialValue, AccessMode a2)': names 'QNativeIpcKey', which has no cute
    class yet.
  - Qt's 'void QSystemSemaphore::setNativeKey(const QString &key, int
    initialValue, AccessMode mode, QNativeIpcKey::Type type)': names the enum
    'QNativeIpcKey::Type', whose class cannot be named here.
  - Qt's 'QNativeIpcKey QSystemSemaphore::nativeIpcKey() const': gives
    'QNativeIpcKey', which has no cute class yet.
  - Qt's 'bool QSystemSemaphore::isKeyTypeSupported(QNativeIpcKey::Type
    type)': names the enum 'QNativeIpcKey::Type', whose class cannot be named
    here.
  - Qt's 'QNativeIpcKey QSystemSemaphore::platformSafeKey(const QString &key,
    QNativeIpcKey::Type type)': names the enum 'QNativeIpcKey::Type', whose
    class cannot be named here.
  - Qt's 'QNativeIpcKey QSystemSemaphore::legacyNativeKey(const QString &key,
    QNativeIpcKey::Type type)': names the enum 'QNativeIpcKey::Type', whose
    class cannot be named here.

  What has no ritual
  ------------------

  5 of the 21 functions Qt declares: 2 forbidden; 1 declared and nowhere to
  be found; 1 a template; 1 private.

  What to expect
  --------------

  - The C++ QSystemSemaphore is created at the first use, not by
    'QSystemSemaphore(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSystemSemaphore.
  """

  #  The enums Qt writes inside QSystemSemaphore, and the names Qt has for
  #  the combinations of its flags enums.
  AccessMode = QSystemSemaphoreAccessMode
  SystemSemaphoreError = QSystemSemaphoreSystemSemaphoreError

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
  def tr(
      sourceText: Optional[str],
      disambiguation: Optional[str] = None,
      n: int = -1,
  ) -> str:
    """
    Calls Qt's 'QString QSystemSemaphore::tr(const char *sourceText, const
    char *disambiguation, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsystemsemaphore.html#tr

    Parameters
    ----------

    sourceText : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    disambiguation : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSystemSemaphore::tr(const char *sourceText, const char
    #      *disambiguation, int n)
    return Rituals.call(
        'ritual_ZN16QSystemSemaphore2trEPKcS1_i',
        CuteMixin._bytesOf(sourceText), CuteMixin._bytesOf(disambiguation),
        n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSystemSemaphore'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def key(self) -> str:
    """
    Calls Qt's 'QString QSystemSemaphore::key() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsystemsemaphore.html#key

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSystemSemaphore::key() const
    return self.uglySide.call('ritual_ZNK16QSystemSemaphore3keyEv')

  def error(self) -> SystemSemaphoreError:
    """
    Calls Qt's 'SystemSemaphoreError QSystemSemaphore::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsystemsemaphore.html#error

    Returns
    -------

    SystemSemaphoreError
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'SystemSemaphoreError(number)' gives.
    """
    #  SystemSemaphoreError QSystemSemaphore::error() const
    return QSystemSemaphore.SystemSemaphoreError(self.uglySide.call(
        'ritual_ZNK16QSystemSemaphore5errorEv',
    ))

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QSystemSemaphore::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsystemsemaphore.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSystemSemaphore::errorString() const
    return self.uglySide.call('ritual_ZNK16QSystemSemaphore11errorStringEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  @overload(str, int)
  @overload(str, int, AccessMode)
  def setKey(
      self,
      key: str,
      initialValue: int = 0,
      mode: AccessMode = AccessMode.Open,
  ) -> None:
    """
    Calls Qt's 'void QSystemSemaphore::setKey(const QString &key, int
    initialValue, AccessMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qsystemsemaphore.html#setKey

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    initialValue : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    mode : AccessMode
      Passed on as its number. May be left out, as in Qt: it is then
      AccessMode.Open.
    """
    #  void QSystemSemaphore::setKey(const QString &key, int initialValue,
    #      AccessMode mode)
    self.uglySide.call(
        'ritual_ZN16QSystemSemaphore6setKeyERK7QStringiNS_10AccessModeE',
        key, initialValue, mode.value,
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

  @overload(str)
  @overload(str, int)
  @overload(str, int, AccessMode)
  def __init__(
      self,
      key: str,
      initialValue: int = 0,
      mode: AccessMode = AccessMode.Open,
  ) -> None:
    """
    Notes what was given, for Qt's 'QSystemSemaphore::QSystemSemaphore(const
    QString &key, int initialValue, AccessMode mode)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsystemsemaphore.html#QSystemSemaphore

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    initialValue : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    mode : AccessMode
      Passed on as its number. May be left out, as in Qt: it is then
      AccessMode.Open.
    """
    #  QSystemSemaphore::QSystemSemaphore(const QString &key, int
    #      initialValue, AccessMode mode)
    self._noteCreation(QSystemSemaphore, lambda: Rituals.call(
        'ritual_ZN16QSystemSemaphoreC1ERK7QStringiNS_10AccessModeE',
        key, initialValue, mode.value,
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

  def acquire(self) -> bool:
    """
    Calls Qt's 'bool QSystemSemaphore::acquire()'.

    Qt's own words: https://doc.qt.io/qt-6/qsystemsemaphore.html#acquire
    """
    #  bool QSystemSemaphore::acquire()
    return self.uglySide.call('ritual_ZN16QSystemSemaphore7acquireEv')

  @overload()
  @overload(int)
  def release(self, n: int = 1) -> bool:
    """
    Calls Qt's 'bool QSystemSemaphore::release(int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsystemsemaphore.html#release

    Parameters
    ----------

    n : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  bool QSystemSemaphore::release(int n)
    return self.uglySide.call('ritual_ZN16QSystemSemaphore7releaseEi', n)
