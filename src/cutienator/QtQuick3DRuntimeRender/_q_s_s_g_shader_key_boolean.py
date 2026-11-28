"""
QSSGShaderKeyBoolean binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershaderkeys_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGShaderKeyBoolean to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QSSGShaderKeyPropertyBase

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSSGShaderKeyBoolean(QSSGShaderKeyPropertyBase):
  """
  The cute side of Qt's QSSGShaderKeyBoolean: a plain Python object standing
  in front of one C++ QSSGShaderKeyBoolean.

  It is built on the cute 'QSSGShaderKeyPropertyBase', as Qt's
  QSSGShaderKeyBoolean is built on Qt's QSSGShaderKeyPropertyBase, and has
  everything that class has.

  C++ hands a QSSGShaderKeyBoolean around as a copy, so every C++
  QSSGShaderKeyBoolean behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSSGShaderKeyBoolean that has a ritual and that
  Python can call so far, 1 name in all: 'getMask'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QSSGShaderKeyBoolean::setValue(QSSGDataRef<quint32>
    inDataStore, bool inValue) const': takes a type Python has no way to hand
    over yet.
  - Qt's 'bool QSSGShaderKeyBoolean::getValue(QSSGDataView<quint32>
    inDataStore) const': takes a type Python has no way to hand over yet.
  - Qt's 'void QSSGShaderKeyBoolean::toString(QByteArray &ioStr,
    QSSGDataView<quint32> inKeySet) const': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QSSGShaderKeyBoolean::fromString(const QByteArray &ioStr,
    QSSGDataRef<quint32> inKeySet)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QSSGShaderKeyBoolean::~QSSGShaderKeyBoolean()': the destructor:
    Python removes its C++ QSSGShaderKeyBoolean by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QSSGShaderKeyBoolean is created at the first use, not by
    'QSSGShaderKeyBoolean(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGShaderKeyBoolean back gives a copy the ritual
    made for Python, in a new cute QSSGShaderKeyBoolean.
  - Each name of Qt's QSSGShaderKeyBoolean that has no cute function yet,
    'fromString', 'getValue', 'setValue', 'toString', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGShaderKeyBoolean'

  #  Qt's '~QSSGShaderKeyBoolean()'. Naming it makes this a value class:
  #  Python owns every C++ QSSGShaderKeyBoolean behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QSSGShaderKeyBooleanD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getMask(self) -> int:
    """
    Calls Qt's 'quint32 QSSGShaderKeyBoolean::getMask() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgshaderkeyboolean.html#getMask
    """
    #  quint32 QSSGShaderKeyBoolean::getMask() const
    return self.uglySide.call('ritual_ZNK20QSSGShaderKeyBoolean7getMaskEv')

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

  @overload(str)
  @overload(NoneType)
  def __init__(self, inName: Optional[str]) -> None:
    """
    Notes what was given, for Qt's
    'QSSGShaderKeyBoolean::QSSGShaderKeyBoolean(const char *inName)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderkeyboolean.html#QSSGShaderKeyBoolean

    Parameters
    ----------

    inName : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  QSSGShaderKeyBoolean::QSSGShaderKeyBoolean(const char *inName)
    self._noteCreation(QSSGShaderKeyBoolean, lambda: Rituals.call(
        'ritual_ZN20QSSGShaderKeyBooleanC1EPKc', self._bytesOf(inName),
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
  def fromString(*__, **_) -> Never:
    """
    Qt's 'void QSSGShaderKeyBoolean::fromString(const QByteArray &ioStr,
    QSSGDataRef<quint32> inKeySet)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderKeyBoolean.fromString' has no cute function yet. Qt's "
        "'void QSSGShaderKeyBoolean::fromString(const QByteArray &ioStr, "
        "QSSGDataRef<quint32> inKeySet)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def getValue(*__, **_) -> Never:
    """
    Qt's 'bool QSSGShaderKeyBoolean::getValue(QSSGDataView<quint32>
    inDataStore) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderKeyBoolean.getValue' has no cute function yet. Qt's "
        "'bool QSSGShaderKeyBoolean::getValue(QSSGDataView<quint32> "
        "inDataStore) const': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def setValue(*__, **_) -> Never:
    """
    Qt's 'void QSSGShaderKeyBoolean::setValue(QSSGDataRef<quint32>
    inDataStore, bool inValue) const': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderKeyBoolean.setValue' has no cute function yet. Qt's "
        "'void QSSGShaderKeyBoolean::setValue(QSSGDataRef<quint32> "
        "inDataStore, bool inValue) const': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def toString(*__, **_) -> Never:
    """
    Qt's 'void QSSGShaderKeyBoolean::toString(QByteArray &ioStr,
    QSSGDataView<quint32> inKeySet) const': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderKeyBoolean.toString' has no cute function yet. Qt's "
        "'void QSSGShaderKeyBoolean::toString(QByteArray &ioStr, "
        "QSSGDataView<quint32> inKeySet) const': takes a type Python has no "
        "way to hand over yet.")
