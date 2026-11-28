"""
QSSGShaderKeyVertexAttribute binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershaderkeys_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGShaderKeyVertexAttribute to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSSGShaderKeyVertexAttribute(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGShaderKeyVertexAttribute: a plain Python object
  standing in front of one C++ QSSGShaderKeyVertexAttribute.

  C++ hands a QSSGShaderKeyVertexAttribute around as a copy, so every C++
  QSSGShaderKeyVertexAttribute behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  No function of Qt's QSSGShaderKeyVertexAttribute yet. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool QSSGShaderKeyVertexAttribute::getBitValue(VertexAttributeBits
    bit, QSSGDataView<quint32> inKeySet) const': takes a type Python has no
    way to hand over yet.
  - Qt's 'void QSSGShaderKeyVertexAttribute::setBitValue(VertexAttributeBits
    bit, QSSGDataRef<quint32> inKeySet, bool value) const': takes a type
    Python has no way to hand over yet.
  - Qt's 'void QSSGShaderKeyVertexAttribute::toString(QByteArray &ioStr,
    QSSGDataView<quint32> inKeySet) const': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QSSGShaderKeyVertexAttribute::fromString(const QByteArray
    &ioStr, QSSGDataRef<quint32> inKeySet)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QSSGShaderKeyVertexAttribute::~QSSGShaderKeyVertexAttribute()': the
    destructor: Python removes its C++ QSSGShaderKeyVertexAttribute by it,
    and has no other use for it.

  What to expect
  --------------

  - The C++ QSSGShaderKeyVertexAttribute is created at the first use, not by
    'QSSGShaderKeyVertexAttribute(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGShaderKeyVertexAttribute back gives a copy the
    ritual made for Python, in a new cute QSSGShaderKeyVertexAttribute.
  - Each name of Qt's QSSGShaderKeyVertexAttribute that has no cute function
    yet, 'fromString', 'getBitValue', 'setBitValue', 'toString', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QSSGShaderKeyVertexAttribute, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class VertexAttributeBits(CuteNum):
    """
    The enum 'QSSGShaderKeyVertexAttribute::VertexAttributeBits' of Qt, with
    the 9 names Qt gives in it.
    """

    Position = Kee[int](1)
    Normal = Kee[int](2)
    TexCoord0 = Kee[int](4)
    TexCoord1 = Kee[int](8)
    Tangent = Kee[int](16)
    Binormal = Kee[int](32)
    Color = Kee[int](64)
    JointAndWeight = Kee[int](128)
    TexCoordLightmap = Kee[int](256)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGShaderKeyVertexAttribute'

  #  Qt's '~QSSGShaderKeyVertexAttribute()'. Naming it makes this a value
  #  class: Python owns every C++ QSSGShaderKeyVertexAttribute behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN28QSSGShaderKeyVertexAttributeD1Ev'

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
    'QSSGShaderKeyVertexAttribute::QSSGShaderKeyVertexAttribute(const char
    *inName)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderkeyvertexattribute.html

    Parameters
    ----------

    inName : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  QSSGShaderKeyVertexAttribute::QSSGShaderKeyVertexAttribute(const char
    #      *inName)
    self._noteCreation(QSSGShaderKeyVertexAttribute, lambda: Rituals.call(
        'ritual_ZN28QSSGShaderKeyVertexAttributeC1EPKc',
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
    Qt's 'void QSSGShaderKeyVertexAttribute::fromString(const QByteArray
    &ioStr, QSSGDataRef<quint32> inKeySet)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderKeyVertexAttribute.fromString' has no cute function "
        "yet. Qt's 'void QSSGShaderKeyVertexAttribute::fromString(const "
        "QByteArray &ioStr, QSSGDataRef<quint32> inKeySet)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def getBitValue(*__, **_) -> Never:
    """
    Qt's 'bool QSSGShaderKeyVertexAttribute::getBitValue(VertexAttributeBits
    bit, QSSGDataView<quint32> inKeySet) const': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderKeyVertexAttribute.getBitValue' has no cute function "
        "yet. Qt's 'bool "
        "QSSGShaderKeyVertexAttribute::getBitValue(VertexAttributeBits bit, "
        "QSSGDataView<quint32> inKeySet) const': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def setBitValue(*__, **_) -> Never:
    """
    Qt's 'void QSSGShaderKeyVertexAttribute::setBitValue(VertexAttributeBits
    bit, QSSGDataRef<quint32> inKeySet, bool value) const': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderKeyVertexAttribute.setBitValue' has no cute function "
        "yet. Qt's 'void "
        "QSSGShaderKeyVertexAttribute::setBitValue(VertexAttributeBits bit, "
        "QSSGDataRef<quint32> inKeySet, bool value) const': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def toString(*__, **_) -> Never:
    """
    Qt's 'void QSSGShaderKeyVertexAttribute::toString(QByteArray &ioStr,
    QSSGDataView<quint32> inKeySet) const': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderKeyVertexAttribute.toString' has no cute function yet. "
        "Qt's 'void QSSGShaderKeyVertexAttribute::toString(QByteArray "
        "&ioStr, QSSGDataView<quint32> inKeySet) const': takes a type "
        "Python has no way to hand over yet.")
