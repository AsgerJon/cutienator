"""
QSystemSemaphorePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qsystemsemaphore_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSystemSemaphorePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QNativeIpcKey, QSystemSemaphore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QLatin1String
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLatin1String = WAIT['QLatin1String']


class QSystemSemaphorePrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSystemSemaphorePrivate: a plain Python object
  standing in front of one C++ QSystemSemaphorePrivate.

  What exists
  -----------

  Every function of Qt's QSystemSemaphorePrivate that has a ritual and that
  Python can call so far, 7 names in all: 'setUnixErrorString', 'setError',
  'clearError', 'constructBackend', 'destructBackend', 'handle',
  'cleanHandle'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSystemSemaphorePrivate::~QSystemSemaphorePrivate()': the
    destructor: Python never removes a C++ QSystemSemaphorePrivate.

  What has no ritual
  ------------------

  3 of the 12 functions Qt declares: 1 a template; 1 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file; 1
  leans on 'QSystemSemaphoreSystemV.

  What to expect
  --------------

  - The C++ QSystemSemaphorePrivate is created at the first use, not by
    'QSystemSemaphorePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSystemSemaphorePrivate.
  - Each name of Qt's QSystemSemaphorePrivate that has no cute function yet,
    'modifySemaphore', 'setWindowsErrorString', 'visit', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QSystemSemaphorePrivate, each a class in
  #  here as in C++.

  class Backend(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSystemSemaphorePrivate::Backend: a plain Python
    object standing in front of one C++ QSystemSemaphorePrivate::Backend.

    What exists
    -----------

    No function of Qt's QSystemSemaphorePrivate::Backend yet. It can be made
    from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSystemSemaphorePrivate::Backend::~Backend()': the destructor:
      Python never removes a C++ QSystemSemaphorePrivate::Backend.

    What to expect
    --------------

    - The C++ QSystemSemaphorePrivate::Backend is created at the first use,
      not by 'QSystemSemaphorePrivate::Backend(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++ QSystemSemaphorePrivate::Backend.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSystemSemaphorePrivate::Backend'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QSystemSemaphorePrivate::Backend::Backend()', which is called at the
      first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qsystemsemaphoreprivate-backend.html#Backend
      """
      #  QSystemSemaphorePrivate::Backend::Backend()
      self._noteCreation(
          QSystemSemaphorePrivate.Backend, lambda: Rituals.call(
              'ritual_ZN23QSystemSemaphorePrivate7BackendC1Ev',
          ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSystemSemaphorePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QLatin1String)
  def setUnixErrorString(self, function: QLatin1String) -> None:
    """
    Calls Qt's 'void
    QSystemSemaphorePrivate::setUnixErrorString(QLatin1StringView function)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsystemsemaphoreprivate.html#setUnixErrorString

    Parameters
    ----------

    function : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.
    """
    #  void QSystemSemaphorePrivate::setUnixErrorString(QLatin1StringView
    #      function)
    self.uglySide.call(
        'ritual_ZN23QSystemSemaphorePrivate18setUnixErrorStringE13QLatin1St'
        'ring',
        self._valueOf(function),
    )

  @overload(QSystemSemaphore.SystemSemaphoreError, str)
  def setError(
      self,
      e: QSystemSemaphore.SystemSemaphoreError,
      message: str,
  ) -> None:
    """
    Calls Qt's 'void
    QSystemSemaphorePrivate::setError(QSystemSemaphore::SystemSemaphoreError
    e, const QString &message)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsystemsemaphoreprivate.html#setError

    Parameters
    ----------

    e : QSystemSemaphore.SystemSemaphoreError
      Passed on as its number.

    message : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSystemSemaphorePrivate::setError(QSystemSemaphore::
    #      SystemSemaphoreError e, const QString &message)
    self.uglySide.call(
        'ritual_ZN23QSystemSemaphorePrivate8setErrorEN16QSystemSemaphore20S'
        'ystemSemaphoreErrorERK7QString',
        e.value, message,
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

  @overload(QNativeIpcKey.Type)
  def __init__(self, type: QNativeIpcKey.Type) -> None:
    """
    Notes what was given, for Qt's
    'QSystemSemaphorePrivate::QSystemSemaphorePrivate(QNativeIpcKey::Type
    type)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsystemsemaphoreprivate.html

    Parameters
    ----------

    type : QNativeIpcKey.Type
      Passed on as its number.
    """
    #  QSystemSemaphorePrivate::QSystemSemaphorePrivate(QNativeIpcKey::Type
    #      type)
    self._noteCreation(QSystemSemaphorePrivate, lambda: Rituals.call(
        'ritual_ZN23QSystemSemaphorePrivateC1EN13QNativeIpcKey4TypeE',
        type.value,
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

  def clearError(self) -> None:
    """
    Calls Qt's 'void QSystemSemaphorePrivate::clearError()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsystemsemaphoreprivate.html#clearError
    """
    #  void QSystemSemaphorePrivate::clearError()
    self.uglySide.call('ritual_ZN23QSystemSemaphorePrivate10clearErrorEv')

  def constructBackend(self) -> None:
    """
    Calls Qt's 'void QSystemSemaphorePrivate::constructBackend()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsystemsemaphoreprivate.html#constructBackend
    """
    #  void QSystemSemaphorePrivate::constructBackend()
    self.uglySide.call(
        'ritual_ZN23QSystemSemaphorePrivate16constructBackendEv',
    )

  def destructBackend(self) -> None:
    """
    Calls Qt's 'void QSystemSemaphorePrivate::destructBackend()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsystemsemaphoreprivate.html#destructBackend
    """
    #  void QSystemSemaphorePrivate::destructBackend()
    self.uglySide.call(
        'ritual_ZN23QSystemSemaphorePrivate15destructBackendEv',
    )

  @overload(QSystemSemaphore.AccessMode)
  def handle(self, mode: QSystemSemaphore.AccessMode) -> None:
    """
    Calls Qt's 'void
    QSystemSemaphorePrivate::handle(QSystemSemaphore::AccessMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsystemsemaphoreprivate.html#handle

    Parameters
    ----------

    mode : QSystemSemaphore.AccessMode
      Passed on as its number.
    """
    #  void QSystemSemaphorePrivate::handle(QSystemSemaphore::AccessMode
    #      mode)
    self.uglySide.call(
        'ritual_ZN23QSystemSemaphorePrivate6handleEN16QSystemSemaphore10Acc'
        'essModeE',
        mode.value,
    )

  def cleanHandle(self) -> None:
    """
    Calls Qt's 'void QSystemSemaphorePrivate::cleanHandle()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsystemsemaphoreprivate.html#cleanHandle
    """
    #  void QSystemSemaphorePrivate::cleanHandle()
    self.uglySide.call('ritual_ZN23QSystemSemaphorePrivate11cleanHandleEv')

  @staticmethod
  def modifySemaphore(*__, **_) -> Never:
    """
    Qt's 'bool QSystemSemaphorePrivate::modifySemaphore(int count)': leans on
    'QSystemSemaphoreSystemV::modifySemaphore(QSystemSemaphorePrivate*,
    int)', which Qt's source does not mark for use from outside Qt and has no
    code for that could be taken.
    """
    raise NotImplementedError(
        "'QSystemSemaphorePrivate.modifySemaphore' has no cute function "
        "yet. Qt's 'bool QSystemSemaphorePrivate::modifySemaphore(int "
        "count)': leans on "
        "'QSystemSemaphoreSystemV::modifySemaphore(QSystemSemaphorePrivate*,"
        " int)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def setWindowsErrorString(*__, **_) -> Never:
    """
    Qt's 'void
    QSystemSemaphorePrivate::setWindowsErrorString(QLatin1StringView
    function)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: unknown type name 'BOOL'.
    """
    raise NotImplementedError(
        "'QSystemSemaphorePrivate.setWindowsErrorString' has no cute "
        "function yet. Qt's 'void "
        "QSystemSemaphorePrivate::setWindowsErrorString(QLatin1StringView "
        "function)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: unknown type name "
        "'BOOL'.")

  @staticmethod
  def visit(*__, **_) -> Never:
    """
    Qt's 'QSystemSemaphorePrivate::visit': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QSystemSemaphorePrivate.visit' has no cute function yet. Qt's "
        "'QSystemSemaphorePrivate::visit': a template: a pattern and no "
        "single function.")
