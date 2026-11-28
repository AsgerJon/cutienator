"""
QQuickPage binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickpage_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickPage to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtGui import QAccessible
from ..QtQuick import QQuickItem
from . import QQuickPane

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQuickPagePrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPage(QQuickPane):
  """
  The cute side of Qt's QQuickPage: a plain Python object standing in front
  of one C++ QQuickPage.

  It is built on the cute 'QQuickPane', as Qt's QQuickPage is built on Qt's
  QQuickPane, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPage that has a ritual and that Python can
  call so far, 25 names in all: 'metaObject', 'tr', 'title', 'setTitle',
  'resetTitle', 'header', 'setHeader', 'footer', 'setFooter',
  'implicitHeaderWidth', 'implicitHeaderHeight', 'implicitFooterWidth',
  'implicitFooterHeight', 'titleChanged', 'headerChanged', 'footerChanged',
  'implicitHeaderWidthChanged', 'implicitHeaderHeightChanged',
  'implicitFooterWidthChanged', 'implicitFooterHeightChanged',
  'componentComplete', 'spacingChange', 'accessibleRole',
  'accessibilityActiveChanged', 'd_func'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickPage::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickPage::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickPage::~QQuickPage()': the destructor: Python never removes a
    C++ QQuickPage.
  - Qt's 'QQuickPage::QQuickPage(QQuickPagePrivate &dd, QQuickItem *parent)':
    takes a type Python has no way to hand over yet.
  - Qt's 'const QQuickPagePrivate *QQuickPage::d_func() const': takes in
    Python what 'QQuickPagePrivate *QQuickPage::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 35 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickPage is created at the first use, not by 'QQuickPage(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPage.
  - Qt tells when it has removed the C++ QQuickPage. Every call on the cute
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
    Calls Qt's 'QString QQuickPage::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpage.html#tr

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
    #  QString QQuickPage::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QQuickPage2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPage'

  #  A C++ QQuickPage Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickPage'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickPage::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpage.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickPage::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QQuickPage10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def title(self) -> str:
    """
    Calls Qt's 'QString QQuickPage::title() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpage.html#title

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickPage::title() const
    return self.uglySide.call('ritual_ZNK10QQuickPage5titleEv')

  def header(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickPage::header() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpage.html#header

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickPage::header() const
    address = self.uglySide.call('ritual_ZNK10QQuickPage6headerEv')
    return QQuickItem._cuteAt(address)

  def footer(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickPage::footer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpage.html#footer

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickPage::footer() const
    address = self.uglySide.call('ritual_ZNK10QQuickPage6footerEv')
    return QQuickItem._cuteAt(address)

  def implicitHeaderWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickPage::implicitHeaderWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpage.html#implicitHeaderWidth
    """
    #  qreal QQuickPage::implicitHeaderWidth() const
    return self.uglySide.call(
        'ritual_ZNK10QQuickPage19implicitHeaderWidthEv',
    )

  def implicitHeaderHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickPage::implicitHeaderHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpage.html#implicitHeaderHeight
    """
    #  qreal QQuickPage::implicitHeaderHeight() const
    return self.uglySide.call(
        'ritual_ZNK10QQuickPage20implicitHeaderHeightEv',
    )

  def implicitFooterWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickPage::implicitFooterWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpage.html#implicitFooterWidth
    """
    #  qreal QQuickPage::implicitFooterWidth() const
    return self.uglySide.call(
        'ritual_ZNK10QQuickPage19implicitFooterWidthEv',
    )

  def implicitFooterHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickPage::implicitFooterHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpage.html#implicitFooterHeight
    """
    #  qreal QQuickPage::implicitFooterHeight() const
    return self.uglySide.call(
        'ritual_ZNK10QQuickPage20implicitFooterHeightEv',
    )

  def accessibleRole(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QQuickPage::accessibleRole() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpage.html#accessibleRole

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QQuickPage::accessibleRole() const
    ritual = 'ritual_ZNK10QQuickPage14accessibleRoleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QQuickPage14accessibleRoleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setTitle(self, title: str) -> None:
    """
    Calls Qt's 'void QQuickPage::setTitle(const QString &title)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpage.html#setTitle

    Parameters
    ----------

    title : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickPage::setTitle(const QString &title)
    self.uglySide.call('ritual_ZN10QQuickPage8setTitleERK7QString', title)

  @overload(QQuickItem)
  @overload(NoneType)
  def setHeader(self, header: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickPage::setHeader(QQuickItem *header)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpage.html#setHeader

    Parameters
    ----------

    header : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPage::setHeader(QQuickItem *header)
    self.uglySide.call(
        'ritual_ZN10QQuickPage9setHeaderEP10QQuickItem',
        self._addressOf(header),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setFooter(self, footer: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickPage::setFooter(QQuickItem *footer)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpage.html#setFooter

    Parameters
    ----------

    footer : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPage::setFooter(QQuickItem *footer)
    self.uglySide.call(
        'ritual_ZN10QQuickPage9setFooterEP10QQuickItem',
        self._addressOf(footer),
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
    Notes what was given, for Qt's 'QQuickPage::QQuickPage(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickpage.html#QQuickPage

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickPage::QQuickPage(QQuickItem *parent)
    self._noteCreation(QQuickPage, lambda: Rituals.call(
        'ritual_ZN10QQuickPageC1EP10QQuickItem', self._addressOf(parent),
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

  def resetTitle(self) -> None:
    """
    Calls Qt's 'void QQuickPage::resetTitle()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpage.html#resetTitle
    """
    #  void QQuickPage::resetTitle()
    self.uglySide.call('ritual_ZN10QQuickPage10resetTitleEv')

  def titleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPage::titleChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpage.html#titleChanged
    """
    #  void QQuickPage::titleChanged()
    self.uglySide.call('ritual_ZN10QQuickPage12titleChangedEv')

  def headerChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPage::headerChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpage.html#headerChanged
    """
    #  void QQuickPage::headerChanged()
    self.uglySide.call('ritual_ZN10QQuickPage13headerChangedEv')

  def footerChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPage::footerChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpage.html#footerChanged
    """
    #  void QQuickPage::footerChanged()
    self.uglySide.call('ritual_ZN10QQuickPage13footerChangedEv')

  def implicitHeaderWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPage::implicitHeaderWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpage.html#implicitHeaderWidthChanged
    """
    #  void QQuickPage::implicitHeaderWidthChanged()
    self.uglySide.call('ritual_ZN10QQuickPage26implicitHeaderWidthChangedEv')

  def implicitHeaderHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPage::implicitHeaderHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpage.html#implicitHeaderHeightChanged
    """
    #  void QQuickPage::implicitHeaderHeightChanged()
    self.uglySide.call(
        'ritual_ZN10QQuickPage27implicitHeaderHeightChangedEv',
    )

  def implicitFooterWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPage::implicitFooterWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpage.html#implicitFooterWidthChanged
    """
    #  void QQuickPage::implicitFooterWidthChanged()
    self.uglySide.call('ritual_ZN10QQuickPage26implicitFooterWidthChangedEv')

  def implicitFooterHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPage::implicitFooterHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpage.html#implicitFooterHeightChanged
    """
    #  void QQuickPage::implicitFooterHeightChanged()
    self.uglySide.call(
        'ritual_ZN10QQuickPage27implicitFooterHeightChangedEv',
    )

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickPage::componentComplete()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpage.html#componentComplete
    """
    #  void QQuickPage::componentComplete()
    ritual = 'ritual_ZN10QQuickPage17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickPage17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(float, float)
  def spacingChange(self, newSpacing: float, oldSpacing: float) -> None:
    """
    Calls Qt's 'void QQuickPage::spacingChange(qreal newSpacing, qreal
    oldSpacing)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpage.html#spacingChange

    Parameters
    ----------

    newSpacing : float
      Passed on as it is.

    oldSpacing : float
      Passed on as it is.
    """
    #  void QQuickPage::spacingChange(qreal newSpacing, qreal oldSpacing)
    ritual = 'ritual_ZN10QQuickPage13spacingChangeEdd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickPage13spacingChangeEdd'
    self.uglySide.call(ritual, newSpacing, oldSpacing)

  @overload(bool)
  def accessibilityActiveChanged(self, active: bool) -> None:
    """
    Calls Qt's 'void QQuickPage::accessibilityActiveChanged(bool active)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpage.html#accessibilityActiveChanged

    Parameters
    ----------

    active : bool
      Passed on as it is.
    """
    #  void QQuickPage::accessibilityActiveChanged(bool active)
    ritual = 'ritual_ZN10QQuickPage26accessibilityActiveChangedEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickPage26accessibilityActiveChangedEb'
    self.uglySide.call(ritual, active)

  def d_func(self) -> Optional[QQuickPagePrivate]:
    """
    Calls Qt's 'QQuickPagePrivate *QQuickPage::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpage.html#d_func

    Returns
    -------

    Optional[QQuickPagePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPagePrivate *QQuickPage::d_func()
    address = self.uglySide.call('ritual_ZN10QQuickPage6d_funcEv')
    from . import QQuickPagePrivate
    return QQuickPagePrivate._cuteAt(address)
