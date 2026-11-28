"""
QtVirtualKeyboard::EnterKeyActionAttachedType binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/enterkeyactionattachedtype_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QtVirtualKeyboard::EnterKeyActionAttachedType to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class EnterKeyActionAttachedType(QObject):
  """
  The cute side of Qt's QtVirtualKeyboard::EnterKeyActionAttachedType: a
  plain Python object standing in front of one C++
  QtVirtualKeyboard::EnterKeyActionAttachedType.

  It is built on the cute 'QObject', as Qt's
  QtVirtualKeyboard::EnterKeyActionAttachedType is built on Qt's QObject, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QtVirtualKeyboard::EnterKeyActionAttachedType that
  has a ritual and that Python can call so far, 11 names in all:
  'metaObject', 'tr', 'actionId', 'setActionId', 'label', 'setLabel',
  'enabled', 'setEnabled', 'actionIdChanged', 'labelChanged',
  'enabledChanged'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    *QtVirtualKeyboard::EnterKeyActionAttachedType::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QtVirtualKeyboard::EnterKeyActionAttachedType::qt_metacall(QMetaObject::
    Call a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void
    QtVirtualKeyboard::EnterKeyActionAttachedType::qt_qmlMarker_anonymous()':
    one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QtVirtualKeyboard::EnterKeyActionAttachedType is created at the
    first use, not by 'QtVirtualKeyboard::EnterKeyActionAttachedType(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    QtVirtualKeyboard::EnterKeyActionAttachedType.
  - Qt tells when it has removed the C++
    QtVirtualKeyboard::EnterKeyActionAttachedType. Every call on the cute
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
    QtVirtualKeyboard::EnterKeyActionAttachedType::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-enterkeyactionattachedtype.html

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
    #  QString QtVirtualKeyboard::EnterKeyActionAttachedType::tr(const char
    #      *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QtVirtualKeyboard26EnterKeyActionAttachedType2trEPKcS2_'
        'i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtVirtualKeyboard::EnterKeyActionAttachedType'

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
    *QtVirtualKeyboard::EnterKeyActionAttachedType::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-enterkeyactionattachedtype.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *QtVirtualKeyboard::EnterKeyActionAttachedType::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard26EnterKeyActionAttachedType10metaObj'
        'ectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def actionId(self) -> int:
    """
    Calls Qt's 'int QtVirtualKeyboard::EnterKeyActionAttachedType::actionId()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-enterkeyactionattachedtype.html
    """
    #  int QtVirtualKeyboard::EnterKeyActionAttachedType::actionId() const
    return self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard26EnterKeyActionAttachedType8actionId'
        'Ev',
    )

  def label(self) -> str:
    """
    Calls Qt's 'QString
    QtVirtualKeyboard::EnterKeyActionAttachedType::label() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-enterkeyactionattachedtype.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtVirtualKeyboard::EnterKeyActionAttachedType::label() const
    return self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard26EnterKeyActionAttachedType5labelEv',
    )

  def enabled(self) -> bool:
    """
    Calls Qt's 'bool QtVirtualKeyboard::EnterKeyActionAttachedType::enabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-enterkeyactionattachedtype.html
    """
    #  bool QtVirtualKeyboard::EnterKeyActionAttachedType::enabled() const
    return self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard26EnterKeyActionAttachedType7enabledE'
        'v',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setActionId(self, actionId: int) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::EnterKeyActionAttachedType::setActionId(int
    actionId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-enterkeyactionattachedtype.html

    Parameters
    ----------

    actionId : int
      Passed on as it is.
    """
    #  void QtVirtualKeyboard::EnterKeyActionAttachedType::setActionId(int
    #      actionId)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard26EnterKeyActionAttachedType11setActio'
        'nIdEi',
        actionId,
    )

  @overload(str)
  def setLabel(self, label: str) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::EnterKeyActionAttachedType::setLabel(const QString
    &label)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-enterkeyactionattachedtype.html

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QtVirtualKeyboard::EnterKeyActionAttachedType::setLabel(const
    #      QString &label)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard26EnterKeyActionAttachedType8setLabelE'
        'RK7QString',
        label,
    )

  @overload(bool)
  def setEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::EnterKeyActionAttachedType::setEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-enterkeyactionattachedtype.html

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QtVirtualKeyboard::EnterKeyActionAttachedType::setEnabled(bool
    #      enabled)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard26EnterKeyActionAttachedType10setEnabl'
        'edEb',
        enabled,
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
    'QtVirtualKeyboard::EnterKeyActionAttachedType::
    EnterKeyActionAttachedType(QObject *parent)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-enterkeyactionattachedtype.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QtVirtualKeyboard::EnterKeyActionAttachedType::
    #      EnterKeyActionAttachedType(QObject *parent)
    self._noteCreation(EnterKeyActionAttachedType, lambda: Rituals.call(
        'ritual_ZN17QtVirtualKeyboard26EnterKeyActionAttachedTypeC1EP7QObje'
        'ct',
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

  def actionIdChanged(self) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::EnterKeyActionAttachedType::actionIdChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-enterkeyactionattachedtype.html
    """
    #  void QtVirtualKeyboard::EnterKeyActionAttachedType::actionIdChanged()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard26EnterKeyActionAttachedType15actionId'
        'ChangedEv',
    )

  def labelChanged(self) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::EnterKeyActionAttachedType::labelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-enterkeyactionattachedtype.html
    """
    #  void QtVirtualKeyboard::EnterKeyActionAttachedType::labelChanged()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard26EnterKeyActionAttachedType12labelCha'
        'ngedEv',
    )

  def enabledChanged(self) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::EnterKeyActionAttachedType::enabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-enterkeyactionattachedtype.html
    """
    #  void QtVirtualKeyboard::EnterKeyActionAttachedType::enabledChanged()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard26EnterKeyActionAttachedType14enabledC'
        'hangedEv',
    )
