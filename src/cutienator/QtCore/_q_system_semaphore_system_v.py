"""
QSystemSemaphoreSystemV binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qsystemsemaphore_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSystemSemaphoreSystemV to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QNativeIpcKey, QSystemSemaphore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QSystemSemaphorePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSystemSemaphorePrivate = WAIT['QSystemSemaphorePrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSystemSemaphoreSystemV(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSystemSemaphoreSystemV: a plain Python object
  standing in front of one C++ QSystemSemaphoreSystemV.

  C++ hands a QSystemSemaphoreSystemV around as a copy, so every C++
  QSystemSemaphoreSystemV behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSystemSemaphoreSystemV that has a ritual and that
  Python can call so far, 3 names in all: 'supports', 'runtimeSupportCheck',
  'cleanHandle'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'key_t QSystemSemaphoreSystemV::handle(QSystemSemaphorePrivate
    *self_, QSystemSemaphore::AccessMode mode)': gives a type Python has no
    way to take yet.
  - Qt's 'QSystemSemaphoreSystemV::~QSystemSemaphoreSystemV()': the
    destructor: Python removes its C++ QSystemSemaphoreSystemV by it, and has
    no other use for it.

  What has no ritual
  ------------------

  1 of the 6 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QSystemSemaphoreSystemV is created at the first use, not by
    'QSystemSemaphoreSystemV(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSystemSemaphoreSystemV back gives a copy the ritual
    made for Python, in a new cute QSystemSemaphoreSystemV.
  - Each name of Qt's QSystemSemaphoreSystemV that has no cute function yet,
    'handle', 'modifySemaphore', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QNativeIpcKey.Type)
  def supports(type: QNativeIpcKey.Type) -> bool:
    """
    Calls Qt's 'bool QSystemSemaphoreSystemV::supports(QNativeIpcKey::Type
    type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsystemsemaphoresystemv.html#supports

    Parameters
    ----------

    type : QNativeIpcKey.Type
      Passed on as its number.
    """
    #  bool QSystemSemaphoreSystemV::supports(QNativeIpcKey::Type type)
    return Rituals.call(
        'ritual_ZN23QSystemSemaphoreSystemV8supportsEN13QNativeIpcKey4TypeE',
        type.value,
    )

  @staticmethod
  def runtimeSupportCheck() -> bool:
    """
    Calls Qt's 'bool QSystemSemaphoreSystemV::runtimeSupportCheck()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsystemsemaphoresystemv.html#runtimeSupportCheck
    """
    #  bool QSystemSemaphoreSystemV::runtimeSupportCheck()
    return Rituals.call(
        'ritual_ZN23QSystemSemaphoreSystemV19runtimeSupportCheckEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSystemSemaphoreSystemV'

  #  Qt's '~QSystemSemaphoreSystemV()'. Naming it makes this a value class:
  #  Python owns every C++ QSystemSemaphoreSystemV behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QSystemSemaphoreSystemVD1Ev'

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @overload(QSystemSemaphorePrivate)
  @overload(NoneType)
  def cleanHandle(self, self_: Optional[QSystemSemaphorePrivate]) -> None:
    """
    Calls Qt's 'void
    QSystemSemaphoreSystemV::cleanHandle(QSystemSemaphorePrivate *self_)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsystemsemaphoresystemv.html#cleanHandle

    Parameters
    ----------

    self_ : Optional[QSystemSemaphorePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSystemSemaphoreSystemV::cleanHandle(QSystemSemaphorePrivate
    #      *self_)
    self.uglySide.call(
        'ritual_ZN23QSystemSemaphoreSystemV11cleanHandleEP23QSystemSemaphor'
        'ePrivate',
        self._addressOf(self_),
    )

  @staticmethod
  def handle(*__, **_) -> Never:
    """
    Qt's 'key_t QSystemSemaphoreSystemV::handle(QSystemSemaphorePrivate
    *self_, QSystemSemaphore::AccessMode mode)': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QSystemSemaphoreSystemV.handle' has no cute function yet. Qt's "
        "'key_t QSystemSemaphoreSystemV::handle(QSystemSemaphorePrivate "
        "*self_, QSystemSemaphore::AccessMode mode)': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def modifySemaphore(*__, **_) -> Never:
    """
    Qt's 'bool
    QSystemSemaphoreSystemV::modifySemaphore(QSystemSemaphorePrivate *self_,
    int count)': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QSystemSemaphoreSystemV.modifySemaphore' has no cute function "
        "yet. Qt's 'bool "
        "QSystemSemaphoreSystemV::modifySemaphore(QSystemSemaphorePrivate "
        "*self_, int count)': cannot be called and cannot be called through "
        "the meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")
