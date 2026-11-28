"""
QIcuCodec binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore5Compat/6.12.0/QtCore5Compat/private/qicucodec_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QIcuCodec to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtCore import QList
from . import QTextCodec

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QIcuCodec(QTextCodec):
  """
  The cute side of Qt's QIcuCodec: a plain Python object standing in front of
  one C++ QIcuCodec.

  It is built on the cute 'QTextCodec', as Qt's QIcuCodec is built on Qt's
  QTextCodec, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QIcuCodec that has a ritual and that Python can call
  so far, 4 names in all: 'availableCodecs', 'name', 'aliases', 'mibEnum'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QString QIcuCodec::convertToUnicode(const char *a0, int a1,
    ConverterState *a2) const': names 'QTextCodec::ConverterState', which has
    no cute class yet.
  - Qt's 'QByteArray QIcuCodec::convertFromUnicode(const QChar *a0, int a1,
    ConverterState *a2) const': names 'QTextCodec::ConverterState', which has
    no cute class yet.
  - Qt's 'QIcuCodec::~QIcuCodec()': the destructor: Python never removes a
    C++ QIcuCodec.
  - Qt's 'UConverter *QIcuCodec::getConverter(QTextCodec::ConverterState
    *state) const': names 'QTextCodec::ConverterState', which has no cute
    class yet.

  What has no ritual
  ------------------

  4 of the 13 functions Qt declares: 3 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'qTextCodecNameMatch(char const*, char const*)', which Qt's source does not
  mark for use from outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QIcuCodec is created at the first use, not by 'QIcuCodec(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QIcuCodec.
  - Each name of Qt's QIcuCodec that has no cute function yet,
    'codecForMibUnlocked', 'codecForNameUnlocked', 'defaultCodecUnlocked',
    'getConverter', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def availableCodecs() -> QList[QByteArray]:
    """
    Calls Qt's 'QList<QByteArray> QIcuCodec::availableCodecs()'.

    Qt's own words: https://doc.qt.io/qt-6/qicucodec.html#availableCodecs

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QByteArray> QIcuCodec::availableCodecs()
    address = Rituals.call('ritual_ZN9QIcuCodec15availableCodecsEv')
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QIcuCodec'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QIcuCodec::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qicucodec.html#name

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QIcuCodec::name() const
    ritual = 'ritual_ZNK9QIcuCodec4nameEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK9QIcuCodec4nameEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def aliases(self) -> QList[QByteArray]:
    """
    Calls Qt's 'QList<QByteArray> QIcuCodec::aliases() const'.

    Qt's own words: https://doc.qt.io/qt-6/qicucodec.html#aliases

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QByteArray> QIcuCodec::aliases() const
    address = self.uglySide.call('ritual_ZNK9QIcuCodec7aliasesEv')
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  def mibEnum(self) -> int:
    """
    Calls Qt's 'int QIcuCodec::mibEnum() const'.

    Qt's own words: https://doc.qt.io/qt-6/qicucodec.html#mibEnum
    """
    #  int QIcuCodec::mibEnum() const
    return self.uglySide.call('ritual_ZNK9QIcuCodec7mibEnumEv')

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
  def __init__(self, name: Optional[str]) -> None:
    """
    Notes what was given, for Qt's 'QIcuCodec::QIcuCodec(const char *name)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qicucodec.html#QIcuCodec

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  QIcuCodec::QIcuCodec(const char *name)
    self._noteCreation(QIcuCodec, lambda: Rituals.call(
        'ritual_ZN9QIcuCodecC1EPKc', self._bytesOf(name),
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
  def codecForMibUnlocked(*__, **_) -> Never:
    """
    Qt's 'QTextCodec *QIcuCodec::codecForMibUnlocked(int mib)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'mibToNameSize'.
    """
    raise NotImplementedError(
        "'QIcuCodec.codecForMibUnlocked' has no cute function yet. Qt's "
        "'QTextCodec *QIcuCodec::codecForMibUnlocked(int mib)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'mibToNameSize'.")

  @staticmethod
  def codecForNameUnlocked(*__, **_) -> Never:
    """
    Qt's 'QTextCodec *QIcuCodec::codecForNameUnlocked(const char *name)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier 'c'.
    """
    raise NotImplementedError(
        "'QIcuCodec.codecForNameUnlocked' has no cute function yet. Qt's "
        "'QTextCodec *QIcuCodec::codecForNameUnlocked(const char *name)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier 'c'.")

  @staticmethod
  def defaultCodecUnlocked(*__, **_) -> Never:
    """
    Qt's 'QTextCodec *QIcuCodec::defaultCodecUnlocked()': leans on
    'qTextCodecNameMatch(char const*, char const*)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QIcuCodec.defaultCodecUnlocked' has no cute function yet. Qt's "
        "'QTextCodec *QIcuCodec::defaultCodecUnlocked()': leans on "
        "'qTextCodecNameMatch(char const*, char const*)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def getConverter(*__, **_) -> Never:
    """
    Qt's 'UConverter *QIcuCodec::getConverter(QTextCodec::ConverterState
    *state) const': names 'QTextCodec::ConverterState', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QIcuCodec.getConverter' has no cute function yet. Qt's "
        "'UConverter *QIcuCodec::getConverter(QTextCodec::ConverterState "
        "*state) const': names 'QTextCodec::ConverterState', which has no "
        "cute class yet.")
