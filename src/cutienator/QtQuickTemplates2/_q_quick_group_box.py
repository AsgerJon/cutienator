"""
QQuickGroupBox binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickgroupbox_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickGroupBox to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtGui import QAccessible
from ..QtQuick import QQuickItem
from . import QQuickFrame

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QFont

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickGroupBox(QQuickFrame):
  """
  The cute side of Qt's QQuickGroupBox: a plain Python object standing in
  front of one C++ QQuickGroupBox.

  It is built on the cute 'QQuickFrame', as Qt's QQuickGroupBox is built on
  Qt's QQuickFrame, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickGroupBox that has a ritual and that Python can
  call so far, 16 names in all: 'metaObject', 'tr', 'title', 'setTitle',
  'label', 'setLabel', 'implicitLabelWidth', 'implicitLabelHeight',
  'titleChanged', 'labelChanged', 'implicitLabelWidthChanged',
  'implicitLabelHeightChanged', 'componentComplete', 'defaultFont',
  'accessibleRole', 'accessibilityActiveChanged'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickGroupBox::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickGroupBox::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickGroupBox::~QQuickGroupBox()': the destructor: Python never
    removes a C++ QQuickGroupBox.
  - Qt's 'QQuickGroupBoxPrivate *QQuickGroupBox::d_func()': gives
    'QQuickGroupBoxPrivate', which has no cute class yet.
  - Qt's 'const QQuickGroupBoxPrivate *QQuickGroupBox::d_func() const': gives
    'QQuickGroupBoxPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 26 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickGroupBox is created at the first use, not by
    'QQuickGroupBox(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickGroupBox.
  - Qt tells when it has removed the C++ QQuickGroupBox. Every call on the
    cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickGroupBox::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgroupbox.html#tr

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
    #  QString QQuickGroupBox::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QQuickGroupBox2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickGroupBox'

  #  A C++ QQuickGroupBox Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickGroupBox'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickGroupBox::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgroupbox.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickGroupBox::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQuickGroupBox10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def title(self) -> str:
    """
    Calls Qt's 'QString QQuickGroupBox::title() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgroupbox.html#title

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickGroupBox::title() const
    return self.uglySide.call('ritual_ZNK14QQuickGroupBox5titleEv')

  def label(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickGroupBox::label() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgroupbox.html#label

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickGroupBox::label() const
    address = self.uglySide.call('ritual_ZNK14QQuickGroupBox5labelEv')
    return QQuickItem._cuteAt(address)

  def implicitLabelWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickGroupBox::implicitLabelWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgroupbox.html#implicitLabelWidth
    """
    #  qreal QQuickGroupBox::implicitLabelWidth() const
    return self.uglySide.call(
        'ritual_ZNK14QQuickGroupBox18implicitLabelWidthEv',
    )

  def implicitLabelHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickGroupBox::implicitLabelHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgroupbox.html#implicitLabelHeight
    """
    #  qreal QQuickGroupBox::implicitLabelHeight() const
    return self.uglySide.call(
        'ritual_ZNK14QQuickGroupBox19implicitLabelHeightEv',
    )

  def defaultFont(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickGroupBox::defaultFont() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgroupbox.html#defaultFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickGroupBox::defaultFont() const
    ritual = 'ritual_ZNK14QQuickGroupBox11defaultFontEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QQuickGroupBox11defaultFontEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def accessibleRole(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QQuickGroupBox::accessibleRole() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgroupbox.html#accessibleRole

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QQuickGroupBox::accessibleRole() const
    ritual = 'ritual_ZNK14QQuickGroupBox14accessibleRoleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QQuickGroupBox14accessibleRoleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setTitle(self, title: str) -> None:
    """
    Calls Qt's 'void QQuickGroupBox::setTitle(const QString &title)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgroupbox.html#setTitle

    Parameters
    ----------

    title : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickGroupBox::setTitle(const QString &title)
    self.uglySide.call(
        'ritual_ZN14QQuickGroupBox8setTitleERK7QString', title,
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setLabel(self, label: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickGroupBox::setLabel(QQuickItem *label)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgroupbox.html#setLabel

    Parameters
    ----------

    label : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGroupBox::setLabel(QQuickItem *label)
    self.uglySide.call(
        'ritual_ZN14QQuickGroupBox8setLabelEP10QQuickItem',
        self._addressOf(label),
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
    Notes what was given, for Qt's 'QQuickGroupBox::QQuickGroupBox(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickgroupbox.html#QQuickGroupBox

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickGroupBox::QQuickGroupBox(QQuickItem *parent)
    self._noteCreation(QQuickGroupBox, lambda: Rituals.call(
        'ritual_ZN14QQuickGroupBoxC1EP10QQuickItem', self._addressOf(parent),
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

  def titleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGroupBox::titleChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgroupbox.html#titleChanged
    """
    #  void QQuickGroupBox::titleChanged()
    self.uglySide.call('ritual_ZN14QQuickGroupBox12titleChangedEv')

  def labelChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGroupBox::labelChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgroupbox.html#labelChanged
    """
    #  void QQuickGroupBox::labelChanged()
    self.uglySide.call('ritual_ZN14QQuickGroupBox12labelChangedEv')

  def implicitLabelWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGroupBox::implicitLabelWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgroupbox.html#implicitLabelWidthChanged
    """
    #  void QQuickGroupBox::implicitLabelWidthChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickGroupBox25implicitLabelWidthChangedEv',
    )

  def implicitLabelHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGroupBox::implicitLabelHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgroupbox.html#implicitLabelHeightChanged
    """
    #  void QQuickGroupBox::implicitLabelHeightChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickGroupBox26implicitLabelHeightChangedEv',
    )

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickGroupBox::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgroupbox.html#componentComplete
    """
    #  void QQuickGroupBox::componentComplete()
    ritual = 'ritual_ZN14QQuickGroupBox17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickGroupBox17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(bool)
  def accessibilityActiveChanged(self, active: bool) -> None:
    """
    Calls Qt's 'void QQuickGroupBox::accessibilityActiveChanged(bool
    active)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgroupbox.html#accessibilityActiveChanged

    Parameters
    ----------

    active : bool
      Passed on as it is.
    """
    #  void QQuickGroupBox::accessibilityActiveChanged(bool active)
    ritual = 'ritual_ZN14QQuickGroupBox26accessibilityActiveChangedEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickGroupBox26accessibilityActiveChangedEb'
    self.uglySide.call(ritual, active)
