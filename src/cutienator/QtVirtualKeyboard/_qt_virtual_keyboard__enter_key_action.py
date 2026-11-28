"""
QtVirtualKeyboard::EnterKeyAction binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/enterkeyaction_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QtVirtualKeyboard::EnterKeyAction to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QtVirtualKeyboard

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class EnterKeyAction(QObject):
  """
  The cute side of Qt's QtVirtualKeyboard::EnterKeyAction: a plain Python
  object standing in front of one C++ QtVirtualKeyboard::EnterKeyAction.

  It is built on the cute 'QObject', as Qt's
  QtVirtualKeyboard::EnterKeyAction is built on Qt's QObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QtVirtualKeyboard::EnterKeyAction that has a ritual
  and that Python can call so far, 3 names in all: 'metaObject', 'tr',
  'qmlAttachedProperties'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QtVirtualKeyboard::EnterKeyAction::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QtVirtualKeyboard::EnterKeyAction::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void
    QtVirtualKeyboard::EnterKeyAction::qt_qmlMarker_uncreatable()': one of
    Qt's own inner workings.
  - Qt's 'void QtVirtualKeyboard::EnterKeyAction::qt_qmlMarker_attached()':
    one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 9 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QtVirtualKeyboard::EnterKeyAction is created at the first use,
    not by 'QtVirtualKeyboard::EnterKeyAction(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtVirtualKeyboard::EnterKeyAction.
  - Qt tells when it has removed the C++ QtVirtualKeyboard::EnterKeyAction.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QtVirtualKeyboard::EnterKeyAction, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class Id(CuteNum):
    """
    The enum 'QtVirtualKeyboard::EnterKeyAction::Id' of Qt, with the 6 names
    Qt gives in it.
    """

    NULL = Kee[int](0)
    Go = Kee[int](1)
    Search = Kee[int](2)
    Send = Kee[int](3)
    Next = Kee[int](4)
    Done = Kee[int](5)

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
    Calls Qt's 'QString QtVirtualKeyboard::EnterKeyAction::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-enterkeyaction.html#tr

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
    #  QString QtVirtualKeyboard::EnterKeyAction::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN17QtVirtualKeyboard14EnterKeyAction2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def qmlAttachedProperties(
      object: Optional[QObject],
  ) -> Optional[QtVirtualKeyboard.EnterKeyActionAttachedType]:
    """
    Calls Qt's 'EnterKeyActionAttachedType
    *QtVirtualKeyboard::EnterKeyAction::qmlAttachedProperties(QObject
    *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-enterkeyaction.html

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QtVirtualKeyboard.EnterKeyActionAttachedType]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  EnterKeyActionAttachedType
    #      *QtVirtualKeyboard::EnterKeyAction::qmlAttachedProperties(QObject
    #      *object)
    address = Rituals.call(
        'ritual_ZN17QtVirtualKeyboard14EnterKeyAction21qmlAttachedPropertie'
        'sEP7QObject',
        CuteMixin._addressOf(object, 'QObject'),
    )
    return QtVirtualKeyboard.EnterKeyActionAttachedType._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtVirtualKeyboard::EnterKeyAction'

  #  A C++ QtVirtualKeyboard::EnterKeyAction Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtVirtualKeyboard_EnterKeyAction'

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
    *QtVirtualKeyboard::EnterKeyAction::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-enterkeyaction.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QtVirtualKeyboard::EnterKeyAction::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard14EnterKeyAction10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
