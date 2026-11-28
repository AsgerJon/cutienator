"""
QQuickButton binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickbutton_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickButton to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtQuick import QQuickItem
from . import QQuickAbstractButton

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QFont
  from . import QQuickButtonPrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickButton(QQuickAbstractButton):
  """
  The cute side of Qt's QQuickButton: a plain Python object standing in front
  of one C++ QQuickButton.

  It is built on the cute 'QQuickAbstractButton', as Qt's QQuickButton is
  built on Qt's QQuickAbstractButton, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickButton that has a ritual and that Python can
  call so far, 10 names in all: 'metaObject', 'tr', 'isHighlighted',
  'setHighlighted', 'isFlat', 'setFlat', 'highlightedChanged', 'flatChanged',
  'defaultFont', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickButton::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickButton::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickButton::QQuickButton(QQuickButtonPrivate &dd, QQuickItem
    *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QQuickButtonPrivate *QQuickButton::d_func() const': takes in
    Python what 'QQuickButtonPrivate *QQuickButton::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 19 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickButton is created at the first use, not by
    'QQuickButton(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickButton.
  - Qt tells when it has removed the C++ QQuickButton. Every call on the cute
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
    Calls Qt's 'QString QQuickButton::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbutton.html#tr

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
    #  QString QQuickButton::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QQuickButton2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickButton'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickButton::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbutton.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickButton::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QQuickButton10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isHighlighted(self) -> bool:
    """
    Calls Qt's 'bool QQuickButton::isHighlighted() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbutton.html#isHighlighted
    """
    #  bool QQuickButton::isHighlighted() const
    return self.uglySide.call('ritual_ZNK12QQuickButton13isHighlightedEv')

  def isFlat(self) -> bool:
    """
    Calls Qt's 'bool QQuickButton::isFlat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbutton.html#isFlat
    """
    #  bool QQuickButton::isFlat() const
    return self.uglySide.call('ritual_ZNK12QQuickButton6isFlatEv')

  def defaultFont(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickButton::defaultFont() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbutton.html#defaultFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickButton::defaultFont() const
    ritual = 'ritual_ZNK12QQuickButton11defaultFontEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QQuickButton11defaultFontEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setHighlighted(self, highlighted: bool) -> None:
    """
    Calls Qt's 'void QQuickButton::setHighlighted(bool highlighted)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbutton.html#setHighlighted

    Parameters
    ----------

    highlighted : bool
      Passed on as it is.
    """
    #  void QQuickButton::setHighlighted(bool highlighted)
    self.uglySide.call(
        'ritual_ZN12QQuickButton14setHighlightedEb', highlighted,
    )

  @overload(bool)
  def setFlat(self, flat: bool) -> None:
    """
    Calls Qt's 'void QQuickButton::setFlat(bool flat)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbutton.html#setFlat

    Parameters
    ----------

    flat : bool
      Passed on as it is.
    """
    #  void QQuickButton::setFlat(bool flat)
    self.uglySide.call('ritual_ZN12QQuickButton7setFlatEb', flat)

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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's 'QQuickButton::QQuickButton(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickbutton.html#QQuickButton

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickButton::QQuickButton(QQuickItem *parent)
    self._noteCreation(QQuickButton, lambda: Rituals.call(
        'ritual_ZN12QQuickButtonC1EP10QQuickItem', self._addressOf(parent),
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

  def highlightedChanged(self) -> None:
    """
    Calls Qt's 'void QQuickButton::highlightedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbutton.html#highlightedChanged
    """
    #  void QQuickButton::highlightedChanged()
    self.uglySide.call('ritual_ZN12QQuickButton18highlightedChangedEv')

  def flatChanged(self) -> None:
    """
    Calls Qt's 'void QQuickButton::flatChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbutton.html#flatChanged
    """
    #  void QQuickButton::flatChanged()
    self.uglySide.call('ritual_ZN12QQuickButton11flatChangedEv')

  def d_func(self) -> Optional[QQuickButtonPrivate]:
    """
    Calls Qt's 'QQuickButtonPrivate *QQuickButton::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbutton.html#d_func

    Returns
    -------

    Optional[QQuickButtonPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickButtonPrivate *QQuickButton::d_func()
    address = self.uglySide.call('ritual_ZN12QQuickButton6d_funcEv')
    from . import QQuickButtonPrivate
    return QQuickButtonPrivate._cuteAt(address)
