"""
QIsciiCodec binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore5Compat/6.12.0/QtCore5Compat/private/qisciicodec_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QIsciiCodec to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QTextCodec

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray


class QIsciiCodec(QTextCodec):
  """
  The cute side of Qt's QIsciiCodec: a plain Python object standing in front
  of one C++ QIsciiCodec.

  It is built on the cute 'QTextCodec', as Qt's QIsciiCodec is built on Qt's
  QTextCodec, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QIsciiCodec that has a ritual and that Python can
  call so far, 2 names in all: 'name', 'mibEnum'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QIsciiCodec::~QIsciiCodec()': the destructor: Python never removes
    a C++ QIsciiCodec.
  - Qt's 'QString QIsciiCodec::convertToUnicode(const char *a0, int a1,
    ConverterState *a2) const': names 'QTextCodec::ConverterState', which has
    no cute class yet.
  - Qt's 'QByteArray QIsciiCodec::convertFromUnicode(const QChar *a0, int a1,
    ConverterState *a2) const': names 'QTextCodec::ConverterState', which has
    no cute class yet.

  What has no ritual
  ------------------

  2 of the 7 functions Qt declares: 1 leans on 'qTextCodecNameMatch(char
  const*, char const*)', which Qt's source does not mark for use from outside
  Qt and has no code for that could be taken; 1 leans on 'QIsciiCodec.

  What to expect
  --------------

  - The C++ QIsciiCodec is created at the first use, not by
    'QIsciiCodec(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QIsciiCodec.
  - Each name of Qt's QIsciiCodec that has no cute function yet, '__init__',
    'create', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QIsciiCodec'

  #  A C++ QIsciiCodec Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QIsciiCodec'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QIsciiCodec::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qisciicodec.html#name

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QIsciiCodec::name() const
    ritual = 'ritual_ZNK11QIsciiCodec4nameEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QIsciiCodec4nameEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def mibEnum(self) -> int:
    """
    Calls Qt's 'int QIsciiCodec::mibEnum() const'.

    Qt's own words: https://doc.qt.io/qt-6/qisciicodec.html#mibEnum
    """
    #  int QIsciiCodec::mibEnum() const
    ritual = 'ritual_ZNK11QIsciiCodec7mibEnumEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QIsciiCodec7mibEnumEv'
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QIsciiCodec::QIsciiCodec(int i)': leans on
    'QIsciiCodec::convertFromUnicode(QChar const*, int,
    QStringConverterBase::State*) const', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QIsciiCodec.__init__' has no cute function yet. Qt's "
        "'QIsciiCodec::QIsciiCodec(int i)': leans on "
        "'QIsciiCodec::convertFromUnicode(QChar const*, int, "
        "QStringConverterBase::State*) const', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

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
  def create(*__, **_) -> Never:
    """
    Qt's 'QTextCodec *QIsciiCodec::create(const char *name)': leans on
    'qTextCodecNameMatch(char const*, char const*)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QIsciiCodec.create' has no cute function yet. Qt's 'QTextCodec "
        "*QIsciiCodec::create(const char *name)': leans on "
        "'qTextCodecNameMatch(char const*, char const*)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")
