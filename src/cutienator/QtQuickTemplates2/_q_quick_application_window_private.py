"""
QQuickApplicationWindowPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickapplicationwindow_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickApplicationWindowPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtQuick import QQuickWindowQmlImplPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRectF
  from ..QtGui import QFont, QPalette
  from ..QtQuick import QQuickGeometryChange, QQuickItem
  from . import QQuickApplicationWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFont = WAIT['QFont']
  QPalette = WAIT['QPalette']
  QQuickApplicationWindow = WAIT['QQuickApplicationWindow']
  QQuickGeometryChange = WAIT['QQuickGeometryChange']
  QQuickItem = WAIT['QQuickItem']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickApplicationWindowPrivate(QQuickWindowQmlImplPrivate):
  """
  The cute side of Qt's QQuickApplicationWindowPrivate: a plain Python object
  standing in front of one C++ QQuickApplicationWindowPrivate.

  It is built on the cute 'QQuickWindowQmlImplPrivate', as Qt's
  QQuickApplicationWindowPrivate is built on Qt's QQuickWindowQmlImplPrivate,
  and has everything that class has. Qt's QQuickApplicationWindowPrivate is
  built on Qt's QSafeQuickItemChangeListener<QQuickApplicationWindowPrivate>
  as well, which is not reflected.

  What exists
  -----------

  Every function of Qt's QQuickApplicationWindowPrivate that has a ritual and
  that Python can call so far, 18 names in all: 'q_func', 'get',
  'updateHasBackgroundFlags', 'relayout', 'itemGeometryChanged',
  'itemVisibilityChanged', 'itemImplicitWidthChanged',
  'itemImplicitHeightChanged', 'windowPalette', 'updateFont',
  'setFont_helper', 'resolveFont', '_q_updateActiveFocus',
  'setActiveFocusControl', 'cancelBackground', 'executeBackground',
  'defaultPalette', 'updateChildrenPalettes'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickApplicationWindow
    *QQuickApplicationWindowPrivate::q_func() const': takes in Python what
    'QQuickApplicationWindow *QQuickApplicationWindowPrivate::q_func()'
    takes.
  - Qt's 'QQmlListProperty<QObject>
    QQuickApplicationWindowPrivate::contentData()': gives a type Python has
    no way to take yet.
  - Qt's 'void QQuickApplicationWindowPrivate::contentData_append(
    QQmlListProperty<QObject> *prop, QObject *obj)': names
    'QQmlListProperty<QObject>', which has no cute class yet.

  What to expect
  --------------

  - The C++ QQuickApplicationWindowPrivate is created at the first use, not
    by 'QQuickApplicationWindowPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickApplicationWindowPrivate.
  - Each name of Qt's QQuickApplicationWindowPrivate that has no cute
    function yet, 'contentData', 'contentData_append', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickApplicationWindow)
  @overload(NoneType)
  def get(
      window: Optional[QQuickApplicationWindow],
  ) -> Optional[QQuickApplicationWindowPrivate]:
    """
    Calls Qt's 'QQuickApplicationWindowPrivate
    *QQuickApplicationWindowPrivate::get(QQuickApplicationWindow *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindowprivate.html#get

    Parameters
    ----------

    window : Optional[QQuickApplicationWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickApplicationWindowPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickApplicationWindowPrivate
    #      *QQuickApplicationWindowPrivate::get(QQuickApplicationWindow
    #      *window)
    address = Rituals.call(
        'ritual_ZN30QQuickApplicationWindowPrivate3getEP23QQuickApplication'
        'Window',
        CuteMixin._addressOf(window),
    )
    return QQuickApplicationWindowPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickApplicationWindowPrivate'

  #  A C++ QQuickApplicationWindowPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickApplicationWindowPrivate'

  #  The functions Qt calls itself that QQuickApplicationWindowPrivate is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'itemGeometryChanged': (
          ('_ZN30QQuickApplicationWindowPrivate19itemGeometryChangedEP10QQu'
           'ickItem20QQuickGeometryChangeRK6QRectF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('address', 'value', 'QtQuick:QQuickGeometryChange'),
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'itemVisibilityChanged': (
          ('_ZN30QQuickApplicationWindowPrivate21itemVisibilityChangedEP10Q'
           'QuickItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'itemImplicitWidthChanged': (
          ('_ZN30QQuickApplicationWindowPrivate24itemImplicitWidthChangedEP'
           '10QQuickItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'itemImplicitHeightChanged': (
          ('_ZN30QQuickApplicationWindowPrivate25itemImplicitHeightChangedE'
           'P10QQuickItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'defaultPalette': (
          ('_ZNK30QQuickApplicationWindowPrivate14defaultPaletteEv',
           ('address', 'value', 'QtGui:QPalette'),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def windowPalette(self) -> QPalette:
    """
    Calls Qt's 'QPalette QQuickApplicationWindowPrivate::windowPalette()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindowprivate.html#windowPalette

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  QPalette QQuickApplicationWindowPrivate::windowPalette() const
    ritual = 'ritual_ZNK30QQuickApplicationWindowPrivate13windowPaletteEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK30QQuickApplicationWindowPrivate13windowPaletteEv')
    address = self.uglySide.call(ritual)
    from ..QtGui import QPalette
    return QPalette._cuteOwning(address)

  def defaultPalette(self) -> QPalette:
    """
    Calls Qt's 'QPalette QQuickApplicationWindowPrivate::defaultPalette()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindowprivate.html#defaultPalette

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  QPalette QQuickApplicationWindowPrivate::defaultPalette() const
    ritual = 'ritual_ZNK30QQuickApplicationWindowPrivate14defaultPaletteEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK30QQuickApplicationWindowPrivate14defaultPaletteEv')
    address = self.uglySide.call(ritual)
    from ..QtGui import QPalette
    return QPalette._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QFont)
  def setFont_helper(self, f: QFont) -> None:
    """
    Calls Qt's 'void QQuickApplicationWindowPrivate::setFont_helper(const
    QFont &f)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindowprivate.html#setFont_helper

    Parameters
    ----------

    f : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QQuickApplicationWindowPrivate::setFont_helper(const QFont &f)
    self.uglySide.call(
        'ritual_ZN30QQuickApplicationWindowPrivate14setFont_helperERK5QFont',
        self._valueOf(f),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setActiveFocusControl(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void
    QQuickApplicationWindowPrivate::setActiveFocusControl(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindowprivate.html

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickApplicationWindowPrivate::setActiveFocusControl(QQuickItem
    #      *item)
    self.uglySide.call(
        'ritual_ZN30QQuickApplicationWindowPrivate21setActiveFocusControlEP'
        '10QQuickItem',
        self._addressOf(item),
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

  def q_func(self) -> Optional[QQuickApplicationWindow]:
    """
    Calls Qt's 'QQuickApplicationWindow
    *QQuickApplicationWindowPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindowprivate.html#q_func

    Returns
    -------

    Optional[QQuickApplicationWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickApplicationWindow *QQuickApplicationWindowPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN30QQuickApplicationWindowPrivate6q_funcEv',
    )
    from . import QQuickApplicationWindow
    return QQuickApplicationWindow._cuteAt(address)

  def updateHasBackgroundFlags(self) -> None:
    """
    Calls Qt's 'void
    QQuickApplicationWindowPrivate::updateHasBackgroundFlags()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindowprivate.html
    """
    #  void QQuickApplicationWindowPrivate::updateHasBackgroundFlags()
    self.uglySide.call(
        'ritual_ZN30QQuickApplicationWindowPrivate24updateHasBackgroundFlag'
        'sEv',
    )

  def relayout(self) -> None:
    """
    Calls Qt's 'void QQuickApplicationWindowPrivate::relayout()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindowprivate.html#relayout
    """
    #  void QQuickApplicationWindowPrivate::relayout()
    self.uglySide.call(
        'ritual_ZN30QQuickApplicationWindowPrivate8relayoutEv',
    )

  @overload(QQuickItem, QQuickGeometryChange, QRectF)
  @overload(NoneType, QQuickGeometryChange, QRectF)
  def itemGeometryChanged(
      self,
      item: Optional[QQuickItem],
      change: QQuickGeometryChange,
      diff: QRectF,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickApplicationWindowPrivate::itemGeometryChanged(QQuickItem *item,
    QQuickGeometryChange change, const QRectF &diff)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindowprivate.html

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    change : QQuickGeometryChange
      Passed on as a value: Qt reads the C++ QQuickGeometryChange, which
      stays Python's own.

    diff : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickApplicationWindowPrivate::itemGeometryChanged(QQuickItem
    #      *item, QQuickGeometryChange change, const QRectF &diff)
    ritual = (
        'ritual_ZN30QQuickApplicationWindowPrivate19itemGeometryChangedEP10'
        'QQuickItem20QQuickGeometryChangeRK6QRectF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30QQuickApplicationWindowPrivate19itemGeometryChang'
          'edEP10QQuickItem20QQuickGeometryChangeRK6QRectF')
    self.uglySide.call(
        ritual,
        self._addressOf(item), self._valueOf(change), self._valueOf(diff),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def itemVisibilityChanged(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void
    QQuickApplicationWindowPrivate::itemVisibilityChanged(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindowprivate.html

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickApplicationWindowPrivate::itemVisibilityChanged(QQuickItem
    #      *item)
    ritual = (
        'ritual_ZN30QQuickApplicationWindowPrivate21itemVisibilityChangedEP'
        '10QQuickItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30QQuickApplicationWindowPrivate21itemVisibilityCha'
          'ngedEP10QQuickItem')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QQuickItem)
  @overload(NoneType)
  def itemImplicitWidthChanged(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void
    QQuickApplicationWindowPrivate::itemImplicitWidthChanged(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindowprivate.html

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickApplicationWindowPrivate::itemImplicitWidthChanged(
    #      QQuickItem *item)
    ritual = (
        'ritual_ZN30QQuickApplicationWindowPrivate24itemImplicitWidthChange'
        'dEP10QQuickItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30QQuickApplicationWindowPrivate24itemImplicitWidth'
          'ChangedEP10QQuickItem')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QQuickItem)
  @overload(NoneType)
  def itemImplicitHeightChanged(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void
    QQuickApplicationWindowPrivate::itemImplicitHeightChanged(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindowprivate.html

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickApplicationWindowPrivate::itemImplicitHeightChanged(
    #      QQuickItem *item)
    ritual = (
        'ritual_ZN30QQuickApplicationWindowPrivate25itemImplicitHeightChang'
        'edEP10QQuickItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30QQuickApplicationWindowPrivate25itemImplicitHeigh'
          'tChangedEP10QQuickItem')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QFont)
  def updateFont(self, f: QFont) -> None:
    """
    Calls Qt's 'void QQuickApplicationWindowPrivate::updateFont(const QFont
    &f)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindowprivate.html#updateFont

    Parameters
    ----------

    f : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QQuickApplicationWindowPrivate::updateFont(const QFont &f)
    self.uglySide.call(
        'ritual_ZN30QQuickApplicationWindowPrivate10updateFontERK5QFont',
        self._valueOf(f),
    )

  def resolveFont(self) -> None:
    """
    Calls Qt's 'void QQuickApplicationWindowPrivate::resolveFont()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindowprivate.html#resolveFont
    """
    #  void QQuickApplicationWindowPrivate::resolveFont()
    self.uglySide.call(
        'ritual_ZN30QQuickApplicationWindowPrivate11resolveFontEv',
    )

  def _q_updateActiveFocus(self) -> None:
    """
    Calls Qt's 'void QQuickApplicationWindowPrivate::_q_updateActiveFocus()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindowprivate.html
    """
    #  void QQuickApplicationWindowPrivate::_q_updateActiveFocus()
    self.uglySide.call(
        'ritual_ZN30QQuickApplicationWindowPrivate20_q_updateActiveFocusEv',
    )

  def cancelBackground(self) -> None:
    """
    Calls Qt's 'void QQuickApplicationWindowPrivate::cancelBackground()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindowprivate.html
    """
    #  void QQuickApplicationWindowPrivate::cancelBackground()
    self.uglySide.call(
        'ritual_ZN30QQuickApplicationWindowPrivate16cancelBackgroundEv',
    )

  @overload()
  @overload(bool)
  def executeBackground(self, complete: bool = False) -> None:
    """
    Calls Qt's 'void QQuickApplicationWindowPrivate::executeBackground(bool
    complete)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindowprivate.html

    Parameters
    ----------

    complete : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickApplicationWindowPrivate::executeBackground(bool complete)
    self.uglySide.call(
        'ritual_ZN30QQuickApplicationWindowPrivate17executeBackgroundEb',
        complete,
    )

  @overload(QPalette)
  def updateChildrenPalettes(self, parentPalette: QPalette) -> None:
    """
    Calls Qt's 'void
    QQuickApplicationWindowPrivate::updateChildrenPalettes(const QPalette
    &parentPalette)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindowprivate.html

    Parameters
    ----------

    parentPalette : QPalette
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own.
    """
    #  void QQuickApplicationWindowPrivate::updateChildrenPalettes(const
    #      QPalette &parentPalette)
    ritual = (
        'ritual_ZN30QQuickApplicationWindowPrivate22updateChildrenPalettesE'
        'RK8QPalette')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30QQuickApplicationWindowPrivate22updateChildrenPal'
          'ettesERK8QPalette')
    self.uglySide.call(ritual, self._valueOf(parentPalette))

  @staticmethod
  def contentData(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject>
    QQuickApplicationWindowPrivate::contentData()': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickApplicationWindowPrivate.contentData' has no cute function "
        "yet. Qt's 'QQmlListProperty<QObject> "
        "QQuickApplicationWindowPrivate::contentData()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def contentData_append(*__, **_) -> Never:
    """
    Qt's 'void QQuickApplicationWindowPrivate::contentData_append(
    QQmlListProperty<QObject> *prop, QObject *obj)': names
    'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickApplicationWindowPrivate.contentData_append' has no cute "
        "function yet. Qt's 'void "
        "QQuickApplicationWindowPrivate::contentData_append(QQmlListProperty"
        "<QObject> *prop, QObject *obj)': names "
        "'QQmlListProperty<QObject>', which has no cute class yet.")
