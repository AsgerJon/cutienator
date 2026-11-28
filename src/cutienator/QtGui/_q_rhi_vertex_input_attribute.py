"""
QRhiVertexInputAttribute binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals


class QRhiVertexInputAttribute(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRhiVertexInputAttribute: a plain Python object
  standing in front of one C++ QRhiVertexInputAttribute.

  C++ hands a QRhiVertexInputAttribute around as a copy, so every C++
  QRhiVertexInputAttribute behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QRhiVertexInputAttribute that has a ritual and that
  Python can call so far, 12 names in all: 'binding', 'setBinding',
  'location', 'setLocation', 'format', 'setFormat', 'offset', 'setOffset',
  'matrixSlice', 'setMatrixSlice', '__eq__', '__ne__'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRhiVertexInputAttribute::~QRhiVertexInputAttribute()': the
    destructor: Python removes its C++ QRhiVertexInputAttribute by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QRhiVertexInputAttribute is created at the first use, not by
    'QRhiVertexInputAttribute(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QRhiVertexInputAttribute back gives a copy the ritual
    made for Python, in a new cute QRhiVertexInputAttribute.
  """

  #  The enums Qt writes inside QRhiVertexInputAttribute, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Format(CuteNum):
    """
    The enum 'QRhiVertexInputAttribute::Format' of Qt, with the 27 names Qt
    gives in it.
    """

    Float4 = Kee[int](0)
    Float3 = Kee[int](1)
    Float2 = Kee[int](2)
    Float = Kee[int](3)
    UNormByte4 = Kee[int](4)
    UNormByte2 = Kee[int](5)
    UNormByte = Kee[int](6)
    UInt4 = Kee[int](7)
    UInt3 = Kee[int](8)
    UInt2 = Kee[int](9)
    UInt = Kee[int](10)
    SInt4 = Kee[int](11)
    SInt3 = Kee[int](12)
    SInt2 = Kee[int](13)
    SInt = Kee[int](14)
    Half4 = Kee[int](15)
    Half3 = Kee[int](16)
    Half2 = Kee[int](17)
    Half = Kee[int](18)
    UShort4 = Kee[int](19)
    UShort3 = Kee[int](20)
    UShort2 = Kee[int](21)
    UShort = Kee[int](22)
    SShort4 = Kee[int](23)
    SShort3 = Kee[int](24)
    SShort2 = Kee[int](25)
    SShort = Kee[int](26)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRhiVertexInputAttribute'

  #  Qt's '~QRhiVertexInputAttribute()'. Naming it makes this a value class:
  #  Python owns every C++ QRhiVertexInputAttribute behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QRhiVertexInputAttributeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def binding(self) -> int:
    """
    Calls Qt's 'int QRhiVertexInputAttribute::binding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivertexinputattribute.html#binding
    """
    #  int QRhiVertexInputAttribute::binding() const
    return self.uglySide.call(
        'ritual_ZNK24QRhiVertexInputAttribute7bindingEv',
    )

  def location(self) -> int:
    """
    Calls Qt's 'int QRhiVertexInputAttribute::location() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivertexinputattribute.html#location
    """
    #  int QRhiVertexInputAttribute::location() const
    return self.uglySide.call(
        'ritual_ZNK24QRhiVertexInputAttribute8locationEv',
    )

  def format(self) -> Format:
    """
    Calls Qt's 'Format QRhiVertexInputAttribute::format() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivertexinputattribute.html#format

    Returns
    -------

    Format
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Format(number)' gives.
    """
    #  Format QRhiVertexInputAttribute::format() const
    return QRhiVertexInputAttribute.Format(self.uglySide.call(
        'ritual_ZNK24QRhiVertexInputAttribute6formatEv',
    ))

  def offset(self) -> int:
    """
    Calls Qt's 'quint32 QRhiVertexInputAttribute::offset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivertexinputattribute.html#offset
    """
    #  quint32 QRhiVertexInputAttribute::offset() const
    return self.uglySide.call(
        'ritual_ZNK24QRhiVertexInputAttribute6offsetEv',
    )

  def matrixSlice(self) -> int:
    """
    Calls Qt's 'int QRhiVertexInputAttribute::matrixSlice() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivertexinputattribute.html#matrixSlice
    """
    #  int QRhiVertexInputAttribute::matrixSlice() const
    return self.uglySide.call(
        'ritual_ZNK24QRhiVertexInputAttribute11matrixSliceEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setBinding(self, b: int) -> None:
    """
    Calls Qt's 'void QRhiVertexInputAttribute::setBinding(int b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivertexinputattribute.html#setBinding

    Parameters
    ----------

    b : int
      Passed on as it is.
    """
    #  void QRhiVertexInputAttribute::setBinding(int b)
    self.uglySide.call(
        'ritual_ZN24QRhiVertexInputAttribute10setBindingEi', b,
    )

  @overload(int)
  def setLocation(self, loc: int) -> None:
    """
    Calls Qt's 'void QRhiVertexInputAttribute::setLocation(int loc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivertexinputattribute.html#setLocation

    Parameters
    ----------

    loc : int
      Passed on as it is.
    """
    #  void QRhiVertexInputAttribute::setLocation(int loc)
    self.uglySide.call(
        'ritual_ZN24QRhiVertexInputAttribute11setLocationEi', loc,
    )

  @overload(Format)
  def setFormat(self, f: Format) -> None:
    """
    Calls Qt's 'void QRhiVertexInputAttribute::setFormat(Format f)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivertexinputattribute.html#setFormat

    Parameters
    ----------

    f : Format
      Passed on as its number.
    """
    #  void QRhiVertexInputAttribute::setFormat(Format f)
    self.uglySide.call(
        'ritual_ZN24QRhiVertexInputAttribute9setFormatENS_6FormatE', f.value,
    )

  @overload(int)
  def setOffset(self, ofs: int) -> None:
    """
    Calls Qt's 'void QRhiVertexInputAttribute::setOffset(quint32 ofs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivertexinputattribute.html#setOffset

    Parameters
    ----------

    ofs : int
      Passed on as it is.
    """
    #  void QRhiVertexInputAttribute::setOffset(quint32 ofs)
    self.uglySide.call(
        'ritual_ZN24QRhiVertexInputAttribute9setOffsetEj', ofs,
    )

  @overload(int)
  def setMatrixSlice(self, slice: int) -> None:
    """
    Calls Qt's 'void QRhiVertexInputAttribute::setMatrixSlice(int slice)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivertexinputattribute.html#setMatrixSlice

    Parameters
    ----------

    slice : int
      Passed on as it is.
    """
    #  void QRhiVertexInputAttribute::setMatrixSlice(int slice)
    self.uglySide.call(
        'ritual_ZN24QRhiVertexInputAttribute14setMatrixSliceEi', slice,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, b: QRhiVertexInputAttribute) -> bool:
    """
    Calls Qt's 'bool operator==(const QRhiVertexInputAttribute &a, const
    QRhiVertexInputAttribute &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivertexinputattribute.html#operator==

    Parameters
    ----------

    b : QRhiVertexInputAttribute
      Passed on as a value: Qt reads the C++ QRhiVertexInputAttribute, which
      stays Python's own.
    """
    #  bool operator==(const QRhiVertexInputAttribute &a, const
    #      QRhiVertexInputAttribute &b)
    return Rituals.call(
        'ritual_ZeqRK24QRhiVertexInputAttributeS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(b),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, b: QRhiVertexInputAttribute) -> bool:
    """
    Calls Qt's 'bool operator!=(const QRhiVertexInputAttribute &a, const
    QRhiVertexInputAttribute &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivertexinputattribute.html#operator!=

    Parameters
    ----------

    b : QRhiVertexInputAttribute
      Passed on as a value: Qt reads the C++ QRhiVertexInputAttribute, which
      stays Python's own.
    """
    #  bool operator!=(const QRhiVertexInputAttribute &a, const
    #      QRhiVertexInputAttribute &b)
    return Rituals.call(
        'ritual_ZneRK24QRhiVertexInputAttributeS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(b),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QRhiVertexInputAttribute::QRhiVertexInputAttribute()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivertexinputattribute.html
    """
    #  QRhiVertexInputAttribute::QRhiVertexInputAttribute()
    self._noteCreation(QRhiVertexInputAttribute, lambda: Rituals.call(
        'ritual_ZN24QRhiVertexInputAttributeC1Ev',
    ))

  @overload(int, int, Format, int)
  @overload(int, int, Format, int, int)
  def __init__(
      self,
      binding: int,
      location: int,
      format: Format,
      offset: int,
      matrixSlice: int = -1,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QRhiVertexInputAttribute::QRhiVertexInputAttribute(int binding, int
    location, Format format, quint32 offset, int matrixSlice)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivertexinputattribute.html

    Parameters
    ----------

    binding : int
      Passed on as it is.

    location : int
      Passed on as it is.

    format : Format
      Passed on as its number.

    offset : int
      Passed on as it is.

    matrixSlice : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  QRhiVertexInputAttribute::QRhiVertexInputAttribute(int binding, int
    #      location, Format format, quint32 offset, int matrixSlice)
    self._noteCreation(QRhiVertexInputAttribute, lambda: Rituals.call(
        'ritual_ZN24QRhiVertexInputAttributeC1EiiNS_6FormatEji',
        binding, location, format.value, offset, matrixSlice,
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
