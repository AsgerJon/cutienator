"""
QHashedCStringRef binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qhashedstring_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QHashedCStringRef to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QChar
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QChar = WAIT['QChar']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHashedCStringRef(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QHashedCStringRef: a plain Python object standing in
  front of one C++ QHashedCStringRef.

  C++ hands a QHashedCStringRef around as a copy, so every C++
  QHashedCStringRef behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QHashedCStringRef that has a ritual and that Python
  can call so far, 7 names in all: 'hash', 'constData', 'length', 'toUtf16',
  'utf16length', 'writeUtf16', 'computeHash'. It can be made from Python, in
  4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QHashedCStringRef::writeUtf16(quint16 *a0) const': takes a
    number to change where it is.
  - Qt's 'QHashedCStringRef::~QHashedCStringRef()': the destructor: Python
    removes its C++ QHashedCStringRef by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QHashedCStringRef is created at the first use, not by
    'QHashedCStringRef(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QHashedCStringRef back gives a copy the ritual made
    for Python, in a new cute QHashedCStringRef.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHashedCStringRef'

  #  Qt's '~QHashedCStringRef()'. Naming it makes this a value class: Python
  #  owns every C++ QHashedCStringRef behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QHashedCStringRefD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hash(self) -> int:
    """
    Calls Qt's 'quint32 QHashedCStringRef::hash() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhashedcstringref.html#hash
    """
    #  quint32 QHashedCStringRef::hash() const
    return self.uglySide.call('ritual_ZNK17QHashedCStringRef4hashEv')

  def constData(self) -> Optional[str]:
    """
    Calls Qt's 'const char *QHashedCStringRef::constData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhashedcstringref.html#constData

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QHashedCStringRef::constData() const
    chars = self.uglySide.call('ritual_ZNK17QHashedCStringRef9constDataEv')
    return None if chars is None else chars.decode()

  def length(self) -> int:
    """
    Calls Qt's 'int QHashedCStringRef::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhashedcstringref.html#length
    """
    #  int QHashedCStringRef::length() const
    return self.uglySide.call('ritual_ZNK17QHashedCStringRef6lengthEv')

  def toUtf16(self) -> str:
    """
    Calls Qt's 'QString QHashedCStringRef::toUtf16() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhashedcstringref.html#toUtf16

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QHashedCStringRef::toUtf16() const
    return self.uglySide.call('ritual_ZNK17QHashedCStringRef7toUtf16Ev')

  def utf16length(self) -> int:
    """
    Calls Qt's 'int QHashedCStringRef::utf16length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhashedcstringref.html#utf16length
    """
    #  int QHashedCStringRef::utf16length() const
    return self.uglySide.call('ritual_ZNK17QHashedCStringRef11utf16lengthEv')

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QHashedCStringRef::QHashedCStringRef()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhashedcstringref.html#QHashedCStringRef
    """
    #  QHashedCStringRef::QHashedCStringRef()
    self._noteCreation(QHashedCStringRef, lambda: Rituals.call(
        'ritual_ZN17QHashedCStringRefC1Ev',
    ))

  @overload(str, int)
  @overload(NoneType, int)
  def __init__(self, a0: Optional[str], a1: int) -> None:
    """
    Notes what was given, for Qt's
    'QHashedCStringRef::QHashedCStringRef(const char *a0, int a1)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhashedcstringref.html#QHashedCStringRef

    Parameters
    ----------

    a0 : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    a1 : int
      Passed on as it is.
    """
    #  QHashedCStringRef::QHashedCStringRef(const char *a0, int a1)
    self._noteCreation(QHashedCStringRef, lambda: Rituals.call(
        'ritual_ZN17QHashedCStringRefC1EPKci', self._bytesOf(a0), a1,
    ))

  @overload(str, int, int)
  @overload(NoneType, int, int)
  def __init__(self, a0: Optional[str], a1: int, a2: int) -> None:
    """
    Notes what was given, for Qt's
    'QHashedCStringRef::QHashedCStringRef(const char *a0, int a1, quint32
    a2)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhashedcstringref.html#QHashedCStringRef

    Parameters
    ----------

    a0 : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    a1 : int
      Passed on as it is.

    a2 : int
      Passed on as it is.
    """
    #  QHashedCStringRef::QHashedCStringRef(const char *a0, int a1, quint32
    #      a2)
    self._noteCreation(QHashedCStringRef, lambda: Rituals.call(
        'ritual_ZN17QHashedCStringRefC1EPKcij', self._bytesOf(a0), a1, a2,
    ))

  @overload(THIS)
  def __init__(self, a0: QHashedCStringRef) -> None:
    """
    Notes what was given, for Qt's
    'QHashedCStringRef::QHashedCStringRef(const QHashedCStringRef &a0)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhashedcstringref.html#QHashedCStringRef

    Parameters
    ----------

    a0 : QHashedCStringRef
      Passed on as a value: Qt reads the C++ QHashedCStringRef, which stays
      Python's own.
    """
    #  QHashedCStringRef::QHashedCStringRef(const QHashedCStringRef &a0)
    self._noteCreation(QHashedCStringRef, lambda: Rituals.call(
        'ritual_ZN17QHashedCStringRefC1ERKS_', self._valueOf(a0),
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

  @overload(QChar)
  @overload(NoneType)
  def writeUtf16(self, a0: Optional[QChar]) -> None:
    """
    Calls Qt's 'void QHashedCStringRef::writeUtf16(QChar *a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhashedcstringref.html#writeUtf16

    Parameters
    ----------

    a0 : Optional[QChar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHashedCStringRef::writeUtf16(QChar *a0) const
    self.uglySide.call(
        'ritual_ZNK17QHashedCStringRef10writeUtf16EP5QChar',
        self._addressOf(a0),
    )

  def computeHash(self) -> None:
    """
    Calls Qt's 'void QHashedCStringRef::computeHash() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhashedcstringref.html#computeHash
    """
    #  void QHashedCStringRef::computeHash() const
    self.uglySide.call('ritual_ZNK17QHashedCStringRef11computeHashEv')
