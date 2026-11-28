"""
QCollatorPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qcollator_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QCollatorPrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QLocale
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLocale = WAIT['QLocale']


class QCollatorPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCollatorPrivate: a plain Python object standing in
  front of one C++ QCollatorPrivate.

  What exists
  -----------

  Every function of Qt's QCollatorPrivate that has a ritual and that Python
  can call so far, 1 name in all: 'isC'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCollatorSortKey QCollatorPrivate::sortKeyFromData(CollatorKeyType
    &&data)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  9 of the 12 functions Qt declares: 4 forbidden; 3 leans on
  'QCollatorPrivate; 2 cannot be called and cannot be called through the
  meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QCollatorPrivate is created at the first use, not by
    'QCollatorPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCollatorPrivate.
  - Each name of Qt's QCollatorPrivate that has no cute function yet,
    'cleanup', 'clear', 'ensureInitialized', 'init', 'sortKeyFromData', holds
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
  __qt_class__ = 'QCollatorPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isC(self) -> bool:
    """
    Calls Qt's 'bool QCollatorPrivate::isC() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcollatorprivate.html#isC
    """
    #  bool QCollatorPrivate::isC() const
    return self.uglySide.call('ritual_ZNK16QCollatorPrivate3isCEv')

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

  @overload(QLocale)
  def __init__(self, locale: QLocale) -> None:
    """
    Notes what was given, for Qt's 'QCollatorPrivate::QCollatorPrivate(const
    QLocale &locale)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcollatorprivate.html#QCollatorPrivate

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  QCollatorPrivate::QCollatorPrivate(const QLocale &locale)
    self._noteCreation(QCollatorPrivate, lambda: Rituals.call(
        'ritual_ZN16QCollatorPrivateC1ERK7QLocale', self._valueOf(locale),
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
  def cleanup(*__, **_) -> Never:
    """
    Qt's 'void QCollatorPrivate::cleanup()': cannot be called and cannot be
    called through the meta-object and cannot be copied: no header file has
    its code, Qt's source does not mark it or its class for use from outside
    Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QCollatorPrivate.cleanup' has no cute function yet. Qt's 'void "
        "QCollatorPrivate::cleanup()': cannot be called and cannot be "
        "called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")

  @staticmethod
  def clear(*__, **_) -> Never:
    """
    Qt's 'void QCollatorPrivate::clear()': leans on
    'QCollatorPrivate::cleanup()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCollatorPrivate.clear' has no cute function yet. Qt's 'void "
        "QCollatorPrivate::clear()': leans on "
        "'QCollatorPrivate::cleanup()', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def ensureInitialized(*__, **_) -> Never:
    """
    Qt's 'void QCollatorPrivate::ensureInitialized()': leans on
    'QCollatorPrivate::init()', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCollatorPrivate.ensureInitialized' has no cute function yet. "
        "Qt's 'void QCollatorPrivate::ensureInitialized()': leans on "
        "'QCollatorPrivate::init()', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def init(*__, **_) -> Never:
    """
    Qt's 'void QCollatorPrivate::init()': cannot be called and cannot be
    called through the meta-object and cannot be copied: no header file has
    its code, Qt's source does not mark it or its class for use from outside
    Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QCollatorPrivate.init' has no cute function yet. Qt's 'void "
        "QCollatorPrivate::init()': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def sortKeyFromData(*__, **_) -> Never:
    """
    Qt's 'QCollatorSortKey QCollatorPrivate::sortKeyFromData(CollatorKeyType
    &&data)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCollatorPrivate.sortKeyFromData' has no cute function yet. Qt's "
        "'QCollatorSortKey "
        "QCollatorPrivate::sortKeyFromData(CollatorKeyType &&data)': takes "
        "a type Python has no way to hand over yet.")
