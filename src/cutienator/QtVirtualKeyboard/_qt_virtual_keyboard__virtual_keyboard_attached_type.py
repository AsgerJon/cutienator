"""
QtVirtualKeyboard::VirtualKeyboardAttachedType binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/virtualkeyboardattachedtype_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QtVirtualKeyboard::VirtualKeyboardAttachedType to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class VirtualKeyboardAttachedType(QObject):
  """
  The cute side of Qt's QtVirtualKeyboard::VirtualKeyboardAttachedType: a
  plain Python object standing in front of one C++
  QtVirtualKeyboard::VirtualKeyboardAttachedType.

  It is built on the cute 'QObject', as Qt's
  QtVirtualKeyboard::VirtualKeyboardAttachedType is built on Qt's QObject,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QtVirtualKeyboard::VirtualKeyboardAttachedType that
  has a ritual and that Python can call so far, 5 names in all: 'metaObject',
  'tr', 'extraDictionaries', 'setExtraDictionaries',
  'extraDictionariesChanged'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    *QtVirtualKeyboard::VirtualKeyboardAttachedType::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QtVirtualKeyboard::VirtualKeyboardAttachedType::qt_metacall(
    QMetaObject::Call a0, int a1, void **a2)': one of Qt's own inner
    workings.
  - Qt's 'void
    QtVirtualKeyboard::VirtualKeyboardAttachedType::qt_qmlMarker_anonymous(
    )': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QtVirtualKeyboard::VirtualKeyboardAttachedType is created at the
    first use, not by 'QtVirtualKeyboard::VirtualKeyboardAttachedType(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    QtVirtualKeyboard::VirtualKeyboardAttachedType.
  - Qt tells when it has removed the C++
    QtVirtualKeyboard::VirtualKeyboardAttachedType. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString
    QtVirtualKeyboard::VirtualKeyboardAttachedType::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-virtualkeyboardattachedtype.html

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtVirtualKeyboard::VirtualKeyboardAttachedType::tr(const char
    #      *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QtVirtualKeyboard27VirtualKeyboardAttachedType2trEPKcS2'
        '_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtVirtualKeyboard::VirtualKeyboardAttachedType'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QtVirtualKeyboard::VirtualKeyboardAttachedType::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-virtualkeyboardattachedtype.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *QtVirtualKeyboard::VirtualKeyboardAttachedType::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard27VirtualKeyboardAttachedType10metaOb'
        'jectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def extraDictionaries(self) -> QStringList:
    """
    Calls Qt's 'QStringList
    QtVirtualKeyboard::VirtualKeyboardAttachedType::extraDictionaries()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-virtualkeyboardattachedtype.html

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList
    #      QtVirtualKeyboard::VirtualKeyboardAttachedType::extraDictionaries(
    #      ) const
    address = self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard27VirtualKeyboardAttachedType17extraD'
        'ictionariesEv',
    )
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QStringList)
  def setExtraDictionaries(self, dictionaries: QStringList) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::VirtualKeyboardAttachedType::setExtraDictionaries(
    const QStringList &dictionaries)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-virtualkeyboardattachedtype.html

    Parameters
    ----------

    dictionaries : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QtVirtualKeyboard::VirtualKeyboardAttachedType::
    #      setExtraDictionaries(const QStringList &dictionaries)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard27VirtualKeyboardAttachedType20setExtr'
        'aDictionariesERK5QListI7QStringE',
        self._valueOf(dictionaries),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's
    'QtVirtualKeyboard::VirtualKeyboardAttachedType::
    VirtualKeyboardAttachedType(QObject *parent)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-virtualkeyboardattachedtype.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QtVirtualKeyboard::VirtualKeyboardAttachedType::
    #      VirtualKeyboardAttachedType(QObject *parent)
    self._noteCreation(VirtualKeyboardAttachedType, lambda: Rituals.call(
        'ritual_ZN17QtVirtualKeyboard27VirtualKeyboardAttachedTypeC1EP7QObj'
        'ect',
        self._addressOf(parent, 'QObject'),
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

  def extraDictionariesChanged(self) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::VirtualKeyboardAttachedType::extraDictionariesChanged(
    )'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-virtualkeyboardattachedtype.html
    """
    #  void QtVirtualKeyboard::VirtualKeyboardAttachedType::
    #      extraDictionariesChanged()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard27VirtualKeyboardAttachedType24extraDi'
        'ctionariesChangedEv',
    )
