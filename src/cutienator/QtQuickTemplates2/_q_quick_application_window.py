"""
QQuickApplicationWindow binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickapplicationwindow_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickApplicationWindow to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtGui import QWindow
from ..QtQuick import QQuickWindowQmlImpl

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QLocale, QMetaObject
  from ..QtGui import QFont, QResizeEvent
  from ..QtQuick import QQuickItem
  from . import QQuickApplicationWindowAttached
  from . import QQuickApplicationWindowPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFont = WAIT['QFont']
  QLocale = WAIT['QLocale']
  QQuickItem = WAIT['QQuickItem']
  QResizeEvent = WAIT['QResizeEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickApplicationWindow(QQuickWindowQmlImpl):
  """
  The cute side of Qt's QQuickApplicationWindow: a plain Python object
  standing in front of one C++ QQuickApplicationWindow.

  It is built on the cute 'QQuickWindowQmlImpl', as Qt's
  QQuickApplicationWindow is built on Qt's QQuickWindowQmlImpl, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickApplicationWindow that has a ritual and that
  Python can call so far, 35 names in all: 'metaObject', 'tr',
  'qmlAttachedProperties', 'background', 'setBackground', 'contentItem',
  'activeFocusControl', 'header', 'setHeader', 'footer', 'setFooter', 'font',
  'setFont', 'resetFont', 'locale', 'setLocale', 'resetLocale', 'menuBar',
  'setMenuBar', 'backgroundChanged', 'activeFocusControlChanged',
  'headerChanged', 'footerChanged', 'fontChanged', 'localeChanged',
  'menuBarChanged', 'topPaddingChanged', 'leftPaddingChanged',
  'rightPaddingChanged', 'bottomPaddingChanged', 'isComponentComplete',
  'classBegin', 'componentComplete', 'resizeEvent', 'd_func'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickApplicationWindow::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickApplicationWindow::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickApplicationWindow::qt_qmlMarker_attached()': one of Qt's
    own inner workings.
  - Qt's 'QQuickApplicationWindow::~QQuickApplicationWindow()': the
    destructor: Python never removes a C++ QQuickApplicationWindow.
  - Qt's 'const QQuickApplicationWindowPrivate
    *QQuickApplicationWindow::d_func() const': takes in Python what
    'QQuickApplicationWindowPrivate *QQuickApplicationWindow::d_func()'
    takes.

  What has no ritual
  ------------------

  4 of the 45 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickApplicationWindow is created at the first use, not by
    'QQuickApplicationWindow(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickApplicationWindow.
  - Qt tells when it has removed the C++ QQuickApplicationWindow. Every call
    on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickApplicationWindow::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickapplicationwindow.html#tr

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
    #  QString QQuickApplicationWindow::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QQuickApplicationWindow2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def qmlAttachedProperties(
      object: Optional[QObject],
  ) -> Optional[QQuickApplicationWindowAttached]:
    """
    Calls Qt's 'QQuickApplicationWindowAttached
    *QQuickApplicationWindow::qmlAttachedProperties(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindow.html#qmlAttachedProperties

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickApplicationWindowAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickApplicationWindowAttached
    #      *QQuickApplicationWindow::qmlAttachedProperties(QObject *object)
    address = Rituals.call(
        'ritual_ZN23QQuickApplicationWindow21qmlAttachedPropertiesEP7QObjec'
        't',
        CuteMixin._addressOf(object, 'QObject'),
    )
    from . import QQuickApplicationWindowAttached
    return QQuickApplicationWindowAttached._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickApplicationWindow'

  #  A C++ QQuickApplicationWindow Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickApplicationWindow'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickApplicationWindow::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindow.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickApplicationWindow::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickApplicationWindow10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def background(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickApplicationWindow::background() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindow.html#background

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickApplicationWindow::background() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickApplicationWindow10backgroundEv',
    )
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  def contentItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickApplicationWindow::contentItem() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindow.html#contentItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickApplicationWindow::contentItem() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickApplicationWindow11contentItemEv',
    )
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  def activeFocusControl(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickApplicationWindow::activeFocusControl()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindow.html#activeFocusControl

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickApplicationWindow::activeFocusControl() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickApplicationWindow18activeFocusControlEv',
    )
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  def header(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickApplicationWindow::header() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindow.html#header

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickApplicationWindow::header() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickApplicationWindow6headerEv',
    )
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  def footer(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickApplicationWindow::footer() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindow.html#footer

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickApplicationWindow::footer() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickApplicationWindow6footerEv',
    )
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  def font(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickApplicationWindow::font() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickapplicationwindow.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickApplicationWindow::font() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickApplicationWindow4fontEv',
    )
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def locale(self) -> QLocale:
    """
    Calls Qt's 'QLocale QQuickApplicationWindow::locale() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindow.html#locale

    Returns
    -------

    QLocale
      A new cute QLocale around the copy Qt gave back. Python owns it.
    """
    #  QLocale QQuickApplicationWindow::locale() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickApplicationWindow6localeEv',
    )
    from ..QtCore import QLocale
    return QLocale._cuteOwning(address)

  def menuBar(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickApplicationWindow::menuBar() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindow.html#menuBar

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickApplicationWindow::menuBar() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickApplicationWindow7menuBarEv',
    )
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  def isComponentComplete(self) -> bool:
    """
    Calls Qt's 'bool QQuickApplicationWindow::isComponentComplete() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindow.html#isComponentComplete
    """
    #  bool QQuickApplicationWindow::isComponentComplete() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickApplicationWindow19isComponentCompleteEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickItem)
  @overload(NoneType)
  def setBackground(self, background: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickApplicationWindow::setBackground(QQuickItem
    *background)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindow.html#setBackground

    Parameters
    ----------

    background : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickApplicationWindow::setBackground(QQuickItem *background)
    self.uglySide.call(
        'ritual_ZN23QQuickApplicationWindow13setBackgroundEP10QQuickItem',
        self._addressOf(background),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setHeader(self, header: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickApplicationWindow::setHeader(QQuickItem *header)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindow.html#setHeader

    Parameters
    ----------

    header : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickApplicationWindow::setHeader(QQuickItem *header)
    self.uglySide.call(
        'ritual_ZN23QQuickApplicationWindow9setHeaderEP10QQuickItem',
        self._addressOf(header),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setFooter(self, footer: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickApplicationWindow::setFooter(QQuickItem *footer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindow.html#setFooter

    Parameters
    ----------

    footer : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickApplicationWindow::setFooter(QQuickItem *footer)
    self.uglySide.call(
        'ritual_ZN23QQuickApplicationWindow9setFooterEP10QQuickItem',
        self._addressOf(footer),
    )

  @overload(QFont)
  def setFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QQuickApplicationWindow::setFont(const QFont &font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindow.html#setFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QQuickApplicationWindow::setFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN23QQuickApplicationWindow7setFontERK5QFont',
        self._valueOf(font),
    )

  @overload(QLocale)
  def setLocale(self, locale: QLocale) -> None:
    """
    Calls Qt's 'void QQuickApplicationWindow::setLocale(const QLocale
    &locale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindow.html#setLocale

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  void QQuickApplicationWindow::setLocale(const QLocale &locale)
    self.uglySide.call(
        'ritual_ZN23QQuickApplicationWindow9setLocaleERK7QLocale',
        self._valueOf(locale),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setMenuBar(self, menuBar: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickApplicationWindow::setMenuBar(QQuickItem
    *menuBar)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindow.html#setMenuBar

    Parameters
    ----------

    menuBar : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickApplicationWindow::setMenuBar(QQuickItem *menuBar)
    self.uglySide.call(
        'ritual_ZN23QQuickApplicationWindow10setMenuBarEP10QQuickItem',
        self._addressOf(menuBar),
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
  @overload(QWindow)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWindow] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickApplicationWindow::QQuickApplicationWindow(QWindow *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindow.html

    Parameters
    ----------

    parent : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickApplicationWindow::QQuickApplicationWindow(QWindow *parent)
    self._noteCreation(QQuickApplicationWindow, lambda: Rituals.call(
        'ritual_ZN23QQuickApplicationWindowC1EP7QWindow',
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

  def resetFont(self) -> None:
    """
    Calls Qt's 'void QQuickApplicationWindow::resetFont()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindow.html#resetFont
    """
    #  void QQuickApplicationWindow::resetFont()
    self.uglySide.call('ritual_ZN23QQuickApplicationWindow9resetFontEv')

  def resetLocale(self) -> None:
    """
    Calls Qt's 'void QQuickApplicationWindow::resetLocale()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindow.html#resetLocale
    """
    #  void QQuickApplicationWindow::resetLocale()
    self.uglySide.call('ritual_ZN23QQuickApplicationWindow11resetLocaleEv')

  def backgroundChanged(self) -> None:
    """
    Calls Qt's 'void QQuickApplicationWindow::backgroundChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindow.html#backgroundChanged
    """
    #  void QQuickApplicationWindow::backgroundChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickApplicationWindow17backgroundChangedEv',
    )

  def activeFocusControlChanged(self) -> None:
    """
    Calls Qt's 'void QQuickApplicationWindow::activeFocusControlChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindow.html
    """
    #  void QQuickApplicationWindow::activeFocusControlChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickApplicationWindow25activeFocusControlChangedEv',
    )

  def headerChanged(self) -> None:
    """
    Calls Qt's 'void QQuickApplicationWindow::headerChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindow.html#headerChanged
    """
    #  void QQuickApplicationWindow::headerChanged()
    self.uglySide.call('ritual_ZN23QQuickApplicationWindow13headerChangedEv')

  def footerChanged(self) -> None:
    """
    Calls Qt's 'void QQuickApplicationWindow::footerChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindow.html#footerChanged
    """
    #  void QQuickApplicationWindow::footerChanged()
    self.uglySide.call('ritual_ZN23QQuickApplicationWindow13footerChangedEv')

  def fontChanged(self) -> None:
    """
    Calls Qt's 'void QQuickApplicationWindow::fontChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindow.html#fontChanged
    """
    #  void QQuickApplicationWindow::fontChanged()
    self.uglySide.call('ritual_ZN23QQuickApplicationWindow11fontChangedEv')

  def localeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickApplicationWindow::localeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindow.html#localeChanged
    """
    #  void QQuickApplicationWindow::localeChanged()
    self.uglySide.call('ritual_ZN23QQuickApplicationWindow13localeChangedEv')

  def menuBarChanged(self) -> None:
    """
    Calls Qt's 'void QQuickApplicationWindow::menuBarChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindow.html#menuBarChanged
    """
    #  void QQuickApplicationWindow::menuBarChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickApplicationWindow14menuBarChangedEv',
    )

  def topPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickApplicationWindow::topPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindow.html#topPaddingChanged
    """
    #  void QQuickApplicationWindow::topPaddingChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickApplicationWindow17topPaddingChangedEv',
    )

  def leftPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickApplicationWindow::leftPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindow.html#leftPaddingChanged
    """
    #  void QQuickApplicationWindow::leftPaddingChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickApplicationWindow18leftPaddingChangedEv',
    )

  def rightPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickApplicationWindow::rightPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindow.html#rightPaddingChanged
    """
    #  void QQuickApplicationWindow::rightPaddingChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickApplicationWindow19rightPaddingChangedEv',
    )

  def bottomPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickApplicationWindow::bottomPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindow.html#bottomPaddingChanged
    """
    #  void QQuickApplicationWindow::bottomPaddingChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickApplicationWindow20bottomPaddingChangedEv',
    )

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuickApplicationWindow::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindow.html#classBegin
    """
    #  void QQuickApplicationWindow::classBegin()
    ritual = 'ritual_ZN23QQuickApplicationWindow10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QQuickApplicationWindow10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickApplicationWindow::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindow.html#componentComplete
    """
    #  void QQuickApplicationWindow::componentComplete()
    ritual = 'ritual_ZN23QQuickApplicationWindow17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QQuickApplicationWindow17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QResizeEvent)
  @overload(NoneType)
  def resizeEvent(self, event: Optional[QResizeEvent]) -> None:
    """
    Calls Qt's 'void QQuickApplicationWindow::resizeEvent(QResizeEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindow.html#resizeEvent

    Parameters
    ----------

    event : Optional[QResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickApplicationWindow::resizeEvent(QResizeEvent *event)
    ritual = (
        'ritual_ZN23QQuickApplicationWindow11resizeEventEP12QResizeEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QQuickApplicationWindow11resizeEventEP12QResizeEv'
          'ent')
    self.uglySide.call(ritual, self._addressOf(event))

  def d_func(self) -> Optional[QQuickApplicationWindowPrivate]:
    """
    Calls Qt's 'QQuickApplicationWindowPrivate
    *QQuickApplicationWindow::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindow.html#d_func

    Returns
    -------

    Optional[QQuickApplicationWindowPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickApplicationWindowPrivate *QQuickApplicationWindow::d_func()
    address = self.uglySide.call(
        'ritual_ZN23QQuickApplicationWindow6d_funcEv',
    )
    from . import QQuickApplicationWindowPrivate
    return QQuickApplicationWindowPrivate._cuteAt(address)
