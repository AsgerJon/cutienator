"""
QQuickRow binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickpositioners_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickRow to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QQuickBasePositioner, QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QSizeF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSizeF = WAIT['QSizeF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickRow(QQuickBasePositioner):
  """
  The cute side of Qt's QQuickRow: a plain Python object standing in front of
  one C++ QQuickRow.

  It is built on the cute 'QQuickBasePositioner', as Qt's QQuickRow is built
  on Qt's QQuickBasePositioner, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickRow that has a ritual and that Python can call
  so far, 9 names in all: 'metaObject', 'tr', 'layoutDirection',
  'setLayoutDirection', 'effectiveLayoutDirection', 'layoutDirectionChanged',
  'effectiveLayoutDirectionChanged', 'doPositioning',
  'reportConflictingAnchors'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickRow::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickRow::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickRowPrivate *QQuickRow::d_func()': gives 'QQuickRowPrivate',
    which has no cute class yet.
  - Qt's 'const QQuickRowPrivate *QQuickRow::d_func() const': gives
    'QQuickRowPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickRow is created at the first use, not by 'QQuickRow(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickRow.
  - Qt tells when it has removed the C++ QQuickRow. Every call on the cute
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
    Calls Qt's 'QString QQuickRow::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrow.html#tr

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
    #  QString QQuickRow::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN9QQuickRow2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickRow'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickRow::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrow.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickRow::metaObject() const
    address = self.uglySide.call('ritual_ZNK9QQuickRow10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def layoutDirection(self) -> Qt.LayoutDirection:
    """
    Calls Qt's 'Qt::LayoutDirection QQuickRow::layoutDirection() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrow.html#layoutDirection

    Returns
    -------

    Qt.LayoutDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.LayoutDirection(number)' gives.
    """
    #  Qt::LayoutDirection QQuickRow::layoutDirection() const
    return Qt.LayoutDirection(self.uglySide.call(
        'ritual_ZNK9QQuickRow15layoutDirectionEv',
    ))

  def effectiveLayoutDirection(self) -> Qt.LayoutDirection:
    """
    Calls Qt's 'Qt::LayoutDirection QQuickRow::effectiveLayoutDirection()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrow.html#effectiveLayoutDirection

    Returns
    -------

    Qt.LayoutDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.LayoutDirection(number)' gives.
    """
    #  Qt::LayoutDirection QQuickRow::effectiveLayoutDirection() const
    return Qt.LayoutDirection(self.uglySide.call(
        'ritual_ZNK9QQuickRow24effectiveLayoutDirectionEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.LayoutDirection)
  def setLayoutDirection(self, a0: Qt.LayoutDirection) -> None:
    """
    Calls Qt's 'void QQuickRow::setLayoutDirection(Qt::LayoutDirection a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrow.html#setLayoutDirection

    Parameters
    ----------

    a0 : Qt.LayoutDirection
      Passed on as its number.
    """
    #  void QQuickRow::setLayoutDirection(Qt::LayoutDirection a0)
    self.uglySide.call(
        'ritual_ZN9QQuickRow18setLayoutDirectionEN2Qt15LayoutDirectionE',
        a0.value,
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
    Notes what was given, for Qt's 'QQuickRow::QQuickRow(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickrow.html#QQuickRow

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickRow::QQuickRow(QQuickItem *parent)
    self._noteCreation(QQuickRow, lambda: Rituals.call(
        'ritual_ZN9QQuickRowC1EP10QQuickItem', self._addressOf(parent),
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

  def layoutDirectionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRow::layoutDirectionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrow.html#layoutDirectionChanged
    """
    #  void QQuickRow::layoutDirectionChanged()
    self.uglySide.call('ritual_ZN9QQuickRow22layoutDirectionChangedEv')

  def effectiveLayoutDirectionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRow::effectiveLayoutDirectionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrow.html#effectiveLayoutDirectionChanged
    """
    #  void QQuickRow::effectiveLayoutDirectionChanged()
    self.uglySide.call(
        'ritual_ZN9QQuickRow31effectiveLayoutDirectionChangedEv',
    )

  @overload(QSizeF)
  @overload(NoneType)
  def doPositioning(self, contentSize: Optional[QSizeF]) -> None:
    """
    Calls Qt's 'void QQuickRow::doPositioning(QSizeF *contentSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrow.html#doPositioning

    Parameters
    ----------

    contentSize : Optional[QSizeF]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickRow::doPositioning(QSizeF *contentSize)
    ritual = 'ritual_ZN9QQuickRow13doPositioningEP6QSizeF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QQuickRow13doPositioningEP6QSizeF'
    self.uglySide.call(ritual, self._addressOf(contentSize))

  def reportConflictingAnchors(self) -> None:
    """
    Calls Qt's 'void QQuickRow::reportConflictingAnchors()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrow.html#reportConflictingAnchors
    """
    #  void QQuickRow::reportConflictingAnchors()
    ritual = 'ritual_ZN9QQuickRow24reportConflictingAnchorsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QQuickRow24reportConflictingAnchorsEv'
    self.uglySide.call(ritual)
