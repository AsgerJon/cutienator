"""
QTsciiCodec binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore5Compat/6.12.0/QtCore5Compat/private/qtsciicodec_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QTsciiCodec to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QTextCodec

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QByteArray


class QTsciiCodec(QTextCodec):
  """
  The cute side of Qt's QTsciiCodec: a plain Python object standing in front
  of one C++ QTsciiCodec.

  It is built on the cute 'QTextCodec', as Qt's QTsciiCodec is built on Qt's
  QTextCodec, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTsciiCodec that has a ritual and that Python can
  call so far, 2 names in all: 'name', 'mibEnum'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTsciiCodec::~QTsciiCodec()': the destructor: Python never removes
    a C++ QTsciiCodec.
  - Qt's 'QString QTsciiCodec::convertToUnicode(const char *a0, int a1,
    ConverterState *a2) const': names 'QTextCodec::ConverterState', which has
    no cute class yet.
  - Qt's 'QByteArray QTsciiCodec::convertFromUnicode(const QChar *a0, int a1,
    ConverterState *a2) const': names 'QTextCodec::ConverterState', which has
    no cute class yet.

  What to expect
  --------------

  - The C++ QTsciiCodec is created at the first use, not by
    'QTsciiCodec(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTsciiCodec.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTsciiCodec'

  #  A C++ QTsciiCodec Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTsciiCodec'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QTsciiCodec::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtsciicodec.html#name

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QTsciiCodec::name() const
    ritual = 'ritual_ZNK11QTsciiCodec4nameEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QTsciiCodec4nameEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def mibEnum(self) -> int:
    """
    Calls Qt's 'int QTsciiCodec::mibEnum() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtsciicodec.html#mibEnum
    """
    #  int QTsciiCodec::mibEnum() const
    ritual = 'ritual_ZNK11QTsciiCodec7mibEnumEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QTsciiCodec7mibEnumEv'
    return self.uglySide.call(ritual)

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
