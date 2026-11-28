"""
QSimpleTextCodec binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore5Compat/6.12.0/QtCore5Compat/private/qsimplecodec_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSimpleTextCodec to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..QtCore import QList
from . import QTextCodec

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray


class QSimpleTextCodec(QTextCodec):
  """
  The cute side of Qt's QSimpleTextCodec: a plain Python object standing in
  front of one C++ QSimpleTextCodec.

  It is built on the cute 'QTextCodec', as Qt's QSimpleTextCodec is built on
  Qt's QTextCodec, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSimpleTextCodec that has a ritual and that Python
  can call so far, 3 names in all: 'name', 'aliases', 'mibEnum'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSimpleTextCodec::~QSimpleTextCodec()': the destructor: Python
    never removes a C++ QSimpleTextCodec.
  - Qt's 'QString QSimpleTextCodec::convertToUnicode(const char *a0, int a1,
    ConverterState *a2) const': names 'QTextCodec::ConverterState', which has
    no cute class yet.
  - Qt's 'QByteArray QSimpleTextCodec::convertFromUnicode(const QChar *a0,
    int a1, ConverterState *a2) const': names 'QTextCodec::ConverterState',
    which has no cute class yet.

  What has no ritual
  ------------------

  1 of the 7 functions Qt declares: 1 leans on 'QSimpleTextCodec.

  What to expect
  --------------

  - The C++ QSimpleTextCodec is created at the first use, not by
    'QSimpleTextCodec(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSimpleTextCodec.
  - Each name of Qt's QSimpleTextCodec that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
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
  __qt_class__ = 'QSimpleTextCodec'

  #  A C++ QSimpleTextCodec Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSimpleTextCodec'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QSimpleTextCodec::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsimpletextcodec.html#name

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QSimpleTextCodec::name() const
    address = self.uglySide.call('ritual_ZNK16QSimpleTextCodec4nameEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def aliases(self) -> QList[QByteArray]:
    """
    Calls Qt's 'QList<QByteArray> QSimpleTextCodec::aliases() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsimpletextcodec.html#aliases

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QByteArray> QSimpleTextCodec::aliases() const
    address = self.uglySide.call('ritual_ZNK16QSimpleTextCodec7aliasesEv')
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  def mibEnum(self) -> int:
    """
    Calls Qt's 'int QSimpleTextCodec::mibEnum() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsimpletextcodec.html#mibEnum
    """
    #  int QSimpleTextCodec::mibEnum() const
    return self.uglySide.call('ritual_ZNK16QSimpleTextCodec7mibEnumEv')

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
    Qt's 'QSimpleTextCodec::QSimpleTextCodec(int a0)': leans on
    'QSimpleTextCodec::convertToUnicode(char const*, int,
    QStringConverterBase::State*) const', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSimpleTextCodec.__init__' has no cute function yet. Qt's "
        "'QSimpleTextCodec::QSimpleTextCodec(int a0)': leans on "
        "'QSimpleTextCodec::convertToUnicode(char const*, int, "
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
