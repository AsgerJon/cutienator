"""
QNativeIpcKeyPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qtipccommon_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QNativeIpcKeyPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QNativeIpcKey
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QNativeIpcKey = WAIT['QNativeIpcKey']


class QNativeIpcKeyPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QNativeIpcKeyPrivate: a plain Python object standing
  in front of one C++ QNativeIpcKeyPrivate.

  C++ hands a QNativeIpcKeyPrivate around as a copy, so every C++
  QNativeIpcKeyPrivate behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QNativeIpcKeyPrivate that has a ritual and that
  Python can call so far, 1 name in all: 'legacyKey'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QNativeIpcKeyPrivate::setLegacyKey(QNativeIpcKey &key, const
    QString &legacyKey)': takes a type Python has no way to hand over yet.
  - Qt's 'void QNativeIpcKeyPrivate::setNativeAndLegacyKeys(QNativeIpcKey
    &key, const QString &nativeKey, const QString &legacyKey)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QNativeIpcKeyPrivate
    *QNativeIpcKeyPrivate::makeExtended(QNativeIpcKey &key)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QNativeIpcKeyPrivate::~QNativeIpcKeyPrivate()': the destructor:
    Python removes its C++ QNativeIpcKeyPrivate by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QNativeIpcKeyPrivate is created at the first use, not by
    'QNativeIpcKeyPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QNativeIpcKeyPrivate back gives a copy the ritual
    made for Python, in a new cute QNativeIpcKeyPrivate.
  - Each name of Qt's QNativeIpcKeyPrivate that has no cute function yet,
    'makeExtended', 'setLegacyKey', 'setNativeAndLegacyKeys', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QNativeIpcKey)
  def legacyKey(key: QNativeIpcKey) -> str:
    """
    Calls Qt's 'QString QNativeIpcKeyPrivate::legacyKey(const QNativeIpcKey
    &key)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnativeipckeyprivate.html#legacyKey

    Parameters
    ----------

    key : QNativeIpcKey
      Passed on as a value: Qt reads the C++ QNativeIpcKey, which stays
      Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QNativeIpcKeyPrivate::legacyKey(const QNativeIpcKey &key)
    return Rituals.call(
        'ritual_ZN20QNativeIpcKeyPrivate9legacyKeyERK13QNativeIpcKey',
        CuteMixin._valueOf(key),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNativeIpcKeyPrivate'

  #  Qt's '~QNativeIpcKeyPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QNativeIpcKeyPrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QNativeIpcKeyPrivateD1Ev'

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

  @staticmethod
  def makeExtended(*__, **_) -> Never:
    """
    Qt's 'QNativeIpcKeyPrivate
    *QNativeIpcKeyPrivate::makeExtended(QNativeIpcKey &key)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QNativeIpcKeyPrivate.makeExtended' has no cute function yet. Qt's "
        "'QNativeIpcKeyPrivate "
        "*QNativeIpcKeyPrivate::makeExtended(QNativeIpcKey &key)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def setLegacyKey(*__, **_) -> Never:
    """
    Qt's 'void QNativeIpcKeyPrivate::setLegacyKey(QNativeIpcKey &key, const
    QString &legacyKey)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QNativeIpcKeyPrivate.setLegacyKey' has no cute function yet. Qt's "
        "'void QNativeIpcKeyPrivate::setLegacyKey(QNativeIpcKey &key, const "
        "QString &legacyKey)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def setNativeAndLegacyKeys(*__, **_) -> Never:
    """
    Qt's 'void QNativeIpcKeyPrivate::setNativeAndLegacyKeys(QNativeIpcKey
    &key, const QString &nativeKey, const QString &legacyKey)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QNativeIpcKeyPrivate.setNativeAndLegacyKeys' has no cute function "
        "yet. Qt's 'void "
        "QNativeIpcKeyPrivate::setNativeAndLegacyKeys(QNativeIpcKey &key, "
        "const QString &nativeKey, const QString &legacyKey)': takes a type "
        "Python has no way to hand over yet.")
