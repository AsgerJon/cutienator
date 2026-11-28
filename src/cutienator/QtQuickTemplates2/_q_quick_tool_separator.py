"""
QQuickToolSeparator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktoolseparator_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickToolSeparator to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import Qt
from ..QtGui import QAccessible
from ..QtQuick import QQuickItem
from . import QQuickControl

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QFont

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickToolSeparator(QQuickControl):
  """
  The cute side of Qt's QQuickToolSeparator: a plain Python object standing
  in front of one C++ QQuickToolSeparator.

  It is built on the cute 'QQuickControl', as Qt's QQuickToolSeparator is
  built on Qt's QQuickControl, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickToolSeparator that has a ritual and that
  Python can call so far, 9 names in all: 'metaObject', 'tr', 'orientation',
  'setOrientation', 'isHorizontal', 'isVertical', 'orientationChanged',
  'defaultFont', 'accessibleRole'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickToolSeparator::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickToolSeparator::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickToolSeparatorPrivate *QQuickToolSeparator::d_func()': gives
    'QQuickToolSeparatorPrivate', which has no cute class yet.
  - Qt's 'const QQuickToolSeparatorPrivate *QQuickToolSeparator::d_func()
    const': gives 'QQuickToolSeparatorPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 18 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickToolSeparator is created at the first use, not by
    'QQuickToolSeparator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickToolSeparator.
  - Qt tells when it has removed the C++ QQuickToolSeparator. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QQuickToolSeparator::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktoolseparator.html#tr

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
    #  QString QQuickToolSeparator::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QQuickToolSeparator2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickToolSeparator'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickToolSeparator::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktoolseparator.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickToolSeparator::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickToolSeparator10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def orientation(self) -> Qt.Orientation:
    """
    Calls Qt's 'Qt::Orientation QQuickToolSeparator::orientation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktoolseparator.html#orientation

    Returns
    -------

    Qt.Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Orientation(number)'
      gives.
    """
    #  Qt::Orientation QQuickToolSeparator::orientation() const
    return Qt.Orientation(self.uglySide.call(
        'ritual_ZNK19QQuickToolSeparator11orientationEv',
    ))

  def isHorizontal(self) -> bool:
    """
    Calls Qt's 'bool QQuickToolSeparator::isHorizontal() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktoolseparator.html#isHorizontal
    """
    #  bool QQuickToolSeparator::isHorizontal() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickToolSeparator12isHorizontalEv',
    )

  def isVertical(self) -> bool:
    """
    Calls Qt's 'bool QQuickToolSeparator::isVertical() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktoolseparator.html#isVertical
    """
    #  bool QQuickToolSeparator::isVertical() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickToolSeparator10isVerticalEv',
    )

  def defaultFont(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickToolSeparator::defaultFont() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktoolseparator.html#defaultFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickToolSeparator::defaultFont() const
    ritual = 'ritual_ZNK19QQuickToolSeparator11defaultFontEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QQuickToolSeparator11defaultFontEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def accessibleRole(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QQuickToolSeparator::accessibleRole()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktoolseparator.html#accessibleRole

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QQuickToolSeparator::accessibleRole() const
    ritual = 'ritual_ZNK19QQuickToolSeparator14accessibleRoleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QQuickToolSeparator14accessibleRoleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.Orientation)
  def setOrientation(self, orientation: Qt.Orientation) -> None:
    """
    Calls Qt's 'void QQuickToolSeparator::setOrientation(Qt::Orientation
    orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktoolseparator.html#setOrientation

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  void QQuickToolSeparator::setOrientation(Qt::Orientation orientation)
    self.uglySide.call(
        'ritual_ZN19QQuickToolSeparator14setOrientationEN2Qt11OrientationE',
        orientation.value,
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

  @overload()
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickToolSeparator::QQuickToolSeparator(QQuickItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktoolseparator.html#QQuickToolSeparator

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickToolSeparator::QQuickToolSeparator(QQuickItem *parent)
    self._noteCreation(QQuickToolSeparator, lambda: Rituals.call(
        'ritual_ZN19QQuickToolSeparatorC1EP10QQuickItem',
        self._addressOf(parent),
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

  def orientationChanged(self) -> None:
    """
    Calls Qt's 'void QQuickToolSeparator::orientationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktoolseparator.html#orientationChanged
    """
    #  void QQuickToolSeparator::orientationChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickToolSeparator18orientationChangedEv',
    )
