"""
QSSGShaderKeyShadowSoftness binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershaderkeys_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGShaderKeyShadowSoftness to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSSGShaderKeyShadowSoftness(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGShaderKeyShadowSoftness: a plain Python object
  standing in front of one C++ QSSGShaderKeyShadowSoftness.

  C++ hands a QSSGShaderKeyShadowSoftness around as a copy, so every C++
  QSSGShaderKeyShadowSoftness behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  No function of Qt's QSSGShaderKeyShadowSoftness yet. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    QSSGShaderKeyShadowSoftness::setShadowSoftness(QSSGDataRef<quint32>
    inKeySet, QSSGRenderLight::SoftShadowQuality inQuality)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QSSGRenderLight::SoftShadowQuality
    QSSGShaderKeyShadowSoftness::getShadowSoftness(QSSGDataView<quint32>
    inKeySet) const': takes a type Python has no way to hand over yet.
  - Qt's 'void QSSGShaderKeyShadowSoftness::toString(QByteArray &ioStr,
    QSSGDataView<quint32> inKeySet) const': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QSSGShaderKeyShadowSoftness::fromString(const QByteArray
    &ioStr, QSSGDataRef<quint32> inKeySet)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QSSGShaderKeyShadowSoftness::~QSSGShaderKeyShadowSoftness()': the
    destructor: Python removes its C++ QSSGShaderKeyShadowSoftness by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QSSGShaderKeyShadowSoftness is created at the first use, not by
    'QSSGShaderKeyShadowSoftness(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGShaderKeyShadowSoftness back gives a copy the
    ritual made for Python, in a new cute QSSGShaderKeyShadowSoftness.
  - Each name of Qt's QSSGShaderKeyShadowSoftness that has no cute function
    yet, 'fromString', 'getShadowSoftness', 'setShadowSoftness', 'toString',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGShaderKeyShadowSoftness'

  #  Qt's '~QSSGShaderKeyShadowSoftness()'. Naming it makes this a value
  #  class: Python owns every C++ QSSGShaderKeyShadowSoftness behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN27QSSGShaderKeyShadowSoftnessD1Ev'

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

  @overload(str)
  @overload(NoneType)
  def __init__(self, inName: Optional[str]) -> None:
    """
    Notes what was given, for Qt's
    'QSSGShaderKeyShadowSoftness::QSSGShaderKeyShadowSoftness(const char
    *inName)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderkeyshadowsoftness.html

    Parameters
    ----------

    inName : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  QSSGShaderKeyShadowSoftness::QSSGShaderKeyShadowSoftness(const char
    #      *inName)
    self._noteCreation(QSSGShaderKeyShadowSoftness, lambda: Rituals.call(
        'ritual_ZN27QSSGShaderKeyShadowSoftnessC1EPKc',
        self._bytesOf(inName),
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
    Qt's 'void QSSGShaderKeyShadowSoftness::fromString(const QByteArray
    &ioStr, QSSGDataRef<quint32> inKeySet)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderKeyShadowSoftness.fromString' has no cute function yet. "
        "Qt's 'void QSSGShaderKeyShadowSoftness::fromString(const "
        "QByteArray &ioStr, QSSGDataRef<quint32> inKeySet)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def getShadowSoftness(*__, **_) -> Never:
    """
    Qt's 'QSSGRenderLight::SoftShadowQuality
    QSSGShaderKeyShadowSoftness::getShadowSoftness(QSSGDataView<quint32>
    inKeySet) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderKeyShadowSoftness.getShadowSoftness' has no cute "
        "function yet. Qt's 'QSSGRenderLight::SoftShadowQuality "
        "QSSGShaderKeyShadowSoftness::getShadowSoftness(QSSGDataView<quint32"
        "> inKeySet) const': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def setShadowSoftness(*__, **_) -> Never:
    """
    Qt's 'void
    QSSGShaderKeyShadowSoftness::setShadowSoftness(QSSGDataRef<quint32>
    inKeySet, QSSGRenderLight::SoftShadowQuality inQuality)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderKeyShadowSoftness.setShadowSoftness' has no cute "
        "function yet. Qt's 'void "
        "QSSGShaderKeyShadowSoftness::setShadowSoftness(QSSGDataRef<quint32>"
        " inKeySet, QSSGRenderLight::SoftShadowQuality inQuality)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def toString(*__, **_) -> Never:
    """
    Qt's 'void QSSGShaderKeyShadowSoftness::toString(QByteArray &ioStr,
    QSSGDataView<quint32> inKeySet) const': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderKeyShadowSoftness.toString' has no cute function yet. "
        "Qt's 'void QSSGShaderKeyShadowSoftness::toString(QByteArray "
        "&ioStr, QSSGDataView<quint32> inKeySet) const': takes a type "
        "Python has no way to hand over yet.")
