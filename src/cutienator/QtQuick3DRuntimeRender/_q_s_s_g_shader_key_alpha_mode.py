"""
QSSGShaderKeyAlphaMode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershaderkeys_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGShaderKeyAlphaMode to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
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


class QSSGShaderKeyAlphaMode(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGShaderKeyAlphaMode: a plain Python object
  standing in front of one C++ QSSGShaderKeyAlphaMode.

  C++ hands a QSSGShaderKeyAlphaMode around as a copy, so every C++
  QSSGShaderKeyAlphaMode behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QSSGShaderKeyAlphaMode yet. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QSSGShaderKeyAlphaMode::setAlphaMode(QSSGDataRef<quint32>
    inKeySet, QSSGRenderDefaultMaterial::MaterialAlphaMode inMode)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QSSGRenderDefaultMaterial::MaterialAlphaMode
    QSSGShaderKeyAlphaMode::getAlphaMode(QSSGDataView<quint32> inKeySet)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'void QSSGShaderKeyAlphaMode::toString(QByteArray &ioStr,
    QSSGDataView<quint32> inKeySet) const': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QSSGShaderKeyAlphaMode::fromString(const QByteArray &ioStr,
    QSSGDataRef<quint32> inKeySet)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QSSGShaderKeyAlphaMode::~QSSGShaderKeyAlphaMode()': the destructor:
    Python removes its C++ QSSGShaderKeyAlphaMode by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QSSGShaderKeyAlphaMode is created at the first use, not by
    'QSSGShaderKeyAlphaMode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGShaderKeyAlphaMode back gives a copy the ritual
    made for Python, in a new cute QSSGShaderKeyAlphaMode.
  - Each name of Qt's QSSGShaderKeyAlphaMode that has no cute function yet,
    'fromString', 'getAlphaMode', 'setAlphaMode', 'toString', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGShaderKeyAlphaMode'

  #  Qt's '~QSSGShaderKeyAlphaMode()'. Naming it makes this a value class:
  #  Python owns every C++ QSSGShaderKeyAlphaMode behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QSSGShaderKeyAlphaModeD1Ev'

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
    'QSSGShaderKeyAlphaMode::QSSGShaderKeyAlphaMode(const char *inName)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderkeyalphamode.html#QSSGShaderKeyAlphaMode

    Parameters
    ----------

    inName : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  QSSGShaderKeyAlphaMode::QSSGShaderKeyAlphaMode(const char *inName)
    self._noteCreation(QSSGShaderKeyAlphaMode, lambda: Rituals.call(
        'ritual_ZN22QSSGShaderKeyAlphaModeC1EPKc', self._bytesOf(inName),
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
    Qt's 'void QSSGShaderKeyAlphaMode::fromString(const QByteArray &ioStr,
    QSSGDataRef<quint32> inKeySet)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderKeyAlphaMode.fromString' has no cute function yet. Qt's "
        "'void QSSGShaderKeyAlphaMode::fromString(const QByteArray &ioStr, "
        "QSSGDataRef<quint32> inKeySet)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def getAlphaMode(*__, **_) -> Never:
    """
    Qt's 'QSSGRenderDefaultMaterial::MaterialAlphaMode
    QSSGShaderKeyAlphaMode::getAlphaMode(QSSGDataView<quint32> inKeySet)
    const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderKeyAlphaMode.getAlphaMode' has no cute function yet. "
        "Qt's 'QSSGRenderDefaultMaterial::MaterialAlphaMode "
        "QSSGShaderKeyAlphaMode::getAlphaMode(QSSGDataView<quint32> "
        "inKeySet) const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setAlphaMode(*__, **_) -> Never:
    """
    Qt's 'void QSSGShaderKeyAlphaMode::setAlphaMode(QSSGDataRef<quint32>
    inKeySet, QSSGRenderDefaultMaterial::MaterialAlphaMode inMode)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderKeyAlphaMode.setAlphaMode' has no cute function yet. "
        "Qt's 'void "
        "QSSGShaderKeyAlphaMode::setAlphaMode(QSSGDataRef<quint32> "
        "inKeySet, QSSGRenderDefaultMaterial::MaterialAlphaMode inMode)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def toString(*__, **_) -> Never:
    """
    Qt's 'void QSSGShaderKeyAlphaMode::toString(QByteArray &ioStr,
    QSSGDataView<quint32> inKeySet) const': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderKeyAlphaMode.toString' has no cute function yet. Qt's "
        "'void QSSGShaderKeyAlphaMode::toString(QByteArray &ioStr, "
        "QSSGDataView<quint32> inKeySet) const': takes a type Python has no "
        "way to hand over yet.")
