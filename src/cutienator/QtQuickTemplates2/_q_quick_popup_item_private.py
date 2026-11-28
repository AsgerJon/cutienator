"""
QQuickPopupItemPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickpopupitem_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickPopupItemPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtQuick import QtPrivate
from . import QQuickPagePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QPalette
  from ..QtQuick import QQuickItem, QQuickPalette
  from . import QQuickPopup, QQuickPopupItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaObject = WAIT['QMetaObject']
  QPalette = WAIT['QPalette']
  QQuickPalette = WAIT['QQuickPalette']
  QQuickPopup = WAIT['QQuickPopup']
  QQuickPopupItem = WAIT['QQuickPopupItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPopupItemPrivate(QQuickPagePrivate):
  """
  The cute side of Qt's QQuickPopupItemPrivate: a plain Python object
  standing in front of one C++ QQuickPopupItemPrivate.

  It is built on the cute 'QQuickPagePrivate', as Qt's QQuickPopupItemPrivate
  is built on Qt's QQuickPagePrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPopupItemPrivate that has a ritual and that
  Python can call so far, 17 names in all: 'q_func', 'get',
  'implicitWidthChanged', 'implicitHeightChanged', 'resolveFont',
  'getContentItem', 'cancelContentItem', 'executeContentItem',
  'cancelBackground', 'executeBackground', 'palette', 'setPalette',
  'resetPalette', 'defaultPalette', 'providesPalette', 'parentPalette',
  'attachedPropertyPropagator_parent'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickPopupItem *QQuickPopupItemPrivate::q_func() const':
    takes in Python what 'QQuickPopupItem *QQuickPopupItemPrivate::q_func()'
    takes.

  What to expect
  --------------

  - The C++ QQuickPopupItemPrivate is created at the first use, not by
    'QQuickPopupItemPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPopupItemPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickPopupItem)
  @overload(NoneType)
  def get(
      popupItem: Optional[QQuickPopupItem],
  ) -> Optional[QQuickPopupItemPrivate]:
    """
    Calls Qt's 'QQuickPopupItemPrivate
    *QQuickPopupItemPrivate::get(QQuickPopupItem *popupItem)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopupitemprivate.html#get

    Parameters
    ----------

    popupItem : Optional[QQuickPopupItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickPopupItemPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPopupItemPrivate *QQuickPopupItemPrivate::get(QQuickPopupItem
    #      *popupItem)
    address = Rituals.call(
        'ritual_ZN22QQuickPopupItemPrivate3getEP15QQuickPopupItem',
        CuteMixin._addressOf(popupItem),
    )
    return QQuickPopupItemPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPopupItemPrivate'

  #  A C++ QQuickPopupItemPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickPopupItemPrivate'

  #  The functions Qt calls itself that QQuickPopupItemPrivate is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'palette': (
          ('_ZNK22QQuickPopupItemPrivate7paletteEv',
           ('address', 'address', 'QtQuick:QQuickPalette'),
           ()),
      ),
      'setPalette': (
          ('_ZN22QQuickPopupItemPrivate10setPaletteEP13QQuickPalette',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickPalette'),
           )),
      ),
      'resetPalette': (
          ('_ZN22QQuickPopupItemPrivate12resetPaletteEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'providesPalette': (
          ('_ZNK22QQuickPopupItemPrivate15providesPaletteEv',
           ('bool', 'number', ''),
           ()),
      ),
      'parentPalette': (
          ('_ZNK22QQuickPopupItemPrivate13parentPaletteERK8QPalette',
           ('address', 'value', 'QtGui:QPalette'),
           (
               ('address', 'value', 'QtGui:QPalette'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def palette(self) -> Optional[QQuickPalette]:
    """
    Calls Qt's 'QQuickPalette *QQuickPopupItemPrivate::palette() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupitemprivate.html#palette

    Returns
    -------

    Optional[QQuickPalette]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPalette *QQuickPopupItemPrivate::palette() const
    ritual = 'ritual_ZNK22QQuickPopupItemPrivate7paletteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QQuickPopupItemPrivate7paletteEv'
    address = self.uglySide.call(ritual)
    from ..QtQuick import QQuickPalette
    return QQuickPalette._cuteAt(address)

  def defaultPalette(self) -> QPalette:
    """
    Calls Qt's 'QPalette QQuickPopupItemPrivate::defaultPalette() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupitemprivate.html#defaultPalette

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  QPalette QQuickPopupItemPrivate::defaultPalette() const
    ritual = 'ritual_ZNK22QQuickPopupItemPrivate14defaultPaletteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QQuickPopupItemPrivate14defaultPaletteEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPalette
    return QPalette._cuteOwning(address)

  def providesPalette(self) -> bool:
    """
    Calls Qt's 'bool QQuickPopupItemPrivate::providesPalette() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupitemprivate.html#providesPalette
    """
    #  bool QQuickPopupItemPrivate::providesPalette() const
    ritual = 'ritual_ZNK22QQuickPopupItemPrivate15providesPaletteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QQuickPopupItemPrivate15providesPaletteEv'
    return self.uglySide.call(ritual)

  @overload(QPalette)
  def parentPalette(self, fallbackPalette: QPalette) -> QPalette:
    """
    Calls Qt's 'QPalette QQuickPopupItemPrivate::parentPalette(const QPalette
    &fallbackPalette) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupitemprivate.html#parentPalette

    Parameters
    ----------

    fallbackPalette : QPalette
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own.

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  QPalette QQuickPopupItemPrivate::parentPalette(const QPalette
    #      &fallbackPalette) const
    ritual = 'ritual_ZNK22QQuickPopupItemPrivate13parentPaletteERK8QPalette'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK22QQuickPopupItemPrivate13parentPaletteERK8QPalett'
          'e')
    address = self.uglySide.call(ritual, self._valueOf(fallbackPalette))
    from ..QtGui import QPalette
    return QPalette._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickPalette)
  @overload(NoneType)
  def setPalette(self, p: Optional[QQuickPalette]) -> None:
    """
    Calls Qt's 'void QQuickPopupItemPrivate::setPalette(QQuickPalette *p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupitemprivate.html#setPalette

    Parameters
    ----------

    p : Optional[QQuickPalette]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopupItemPrivate::setPalette(QQuickPalette *p)
    ritual = 'ritual_ZN22QQuickPopupItemPrivate10setPaletteEP13QQuickPalette'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickPopupItemPrivate10setPaletteEP13QQuickPalet'
          'te')
    self.uglySide.call(ritual, self._addressOf(p))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickPopup)
  @overload(NoneType)
  def __init__(self, popup: Optional[QQuickPopup]) -> None:
    """
    Notes what was given, for Qt's
    'QQuickPopupItemPrivate::QQuickPopupItemPrivate(QQuickPopup *popup)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupitemprivate.html#QQuickPopupItemPrivate

    Parameters
    ----------

    popup : Optional[QQuickPopup]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickPopupItemPrivate::QQuickPopupItemPrivate(QQuickPopup *popup)
    self._noteCreation(QQuickPopupItemPrivate, lambda: Rituals.call(
        'ritual_ZN22QQuickPopupItemPrivateC1EP11QQuickPopup',
        self._addressOf(popup),
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

  def q_func(self) -> Optional[QQuickPopupItem]:
    """
    Calls Qt's 'QQuickPopupItem *QQuickPopupItemPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopupitemprivate.html#q_func

    Returns
    -------

    Optional[QQuickPopupItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPopupItem *QQuickPopupItemPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN22QQuickPopupItemPrivate6q_funcEv',
    )
    from . import QQuickPopupItem
    return QQuickPopupItem._cuteAt(address)

  def implicitWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopupItemPrivate::implicitWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupitemprivate.html#implicitWidthChanged
    """
    #  void QQuickPopupItemPrivate::implicitWidthChanged()
    ritual = 'ritual_ZN22QQuickPopupItemPrivate20implicitWidthChangedEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickPopupItemPrivate20implicitWidthChangedEv')
    self.uglySide.call(ritual)

  def implicitHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopupItemPrivate::implicitHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupitemprivate.html#implicitHeightChanged
    """
    #  void QQuickPopupItemPrivate::implicitHeightChanged()
    ritual = 'ritual_ZN22QQuickPopupItemPrivate21implicitHeightChangedEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickPopupItemPrivate21implicitHeightChangedEv')
    self.uglySide.call(ritual)

  def resolveFont(self) -> None:
    """
    Calls Qt's 'void QQuickPopupItemPrivate::resolveFont()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupitemprivate.html#resolveFont
    """
    #  void QQuickPopupItemPrivate::resolveFont()
    ritual = 'ritual_ZN22QQuickPopupItemPrivate11resolveFontEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickPopupItemPrivate11resolveFontEv'
    self.uglySide.call(ritual)

  def getContentItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickPopupItemPrivate::getContentItem()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupitemprivate.html#getContentItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickPopupItemPrivate::getContentItem()
    ritual = 'ritual_ZN22QQuickPopupItemPrivate14getContentItemEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickPopupItemPrivate14getContentItemEv'
    address = self.uglySide.call(ritual)
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  def cancelContentItem(self) -> None:
    """
    Calls Qt's 'void QQuickPopupItemPrivate::cancelContentItem()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupitemprivate.html#cancelContentItem
    """
    #  void QQuickPopupItemPrivate::cancelContentItem()
    ritual = 'ritual_ZN22QQuickPopupItemPrivate17cancelContentItemEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickPopupItemPrivate17cancelContentItemEv'
    self.uglySide.call(ritual)

  @overload()
  @overload(bool)
  def executeContentItem(self, complete: bool = False) -> None:
    """
    Calls Qt's 'void QQuickPopupItemPrivate::executeContentItem(bool
    complete)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupitemprivate.html#executeContentItem

    Parameters
    ----------

    complete : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickPopupItemPrivate::executeContentItem(bool complete)
    ritual = 'ritual_ZN22QQuickPopupItemPrivate18executeContentItemEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickPopupItemPrivate18executeContentItemEb'
    self.uglySide.call(ritual, complete)

  def cancelBackground(self) -> None:
    """
    Calls Qt's 'void QQuickPopupItemPrivate::cancelBackground()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupitemprivate.html#cancelBackground
    """
    #  void QQuickPopupItemPrivate::cancelBackground()
    ritual = 'ritual_ZN22QQuickPopupItemPrivate16cancelBackgroundEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickPopupItemPrivate16cancelBackgroundEv'
    self.uglySide.call(ritual)

  @overload()
  @overload(bool)
  def executeBackground(self, complete: bool = False) -> None:
    """
    Calls Qt's 'void QQuickPopupItemPrivate::executeBackground(bool
    complete)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupitemprivate.html#executeBackground

    Parameters
    ----------

    complete : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickPopupItemPrivate::executeBackground(bool complete)
    ritual = 'ritual_ZN22QQuickPopupItemPrivate17executeBackgroundEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickPopupItemPrivate17executeBackgroundEb'
    self.uglySide.call(ritual, complete)

  def resetPalette(self) -> None:
    """
    Calls Qt's 'void QQuickPopupItemPrivate::resetPalette()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupitemprivate.html#resetPalette
    """
    #  void QQuickPopupItemPrivate::resetPalette()
    ritual = 'ritual_ZN22QQuickPopupItemPrivate12resetPaletteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickPopupItemPrivate12resetPaletteEv'
    self.uglySide.call(ritual)

  @overload(QMetaObject)
  @overload(NoneType)
  def attachedPropertyPropagator_parent(
      self,
      attachedType: Optional[QMetaObject],
  ) -> Optional[QtPrivate.QQuickAttachedPropertyPropagator]:
    """
    Calls Qt's 'QtPrivate::QQuickAttachedPropertyPropagator
    *QQuickPopupItemPrivate::attachedPropertyPropagator_parent(const
    QMetaObject *attachedType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupitemprivate.html

    Parameters
    ----------

    attachedType : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QtPrivate.QQuickAttachedPropertyPropagator]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QtPrivate::QQuickAttachedPropertyPropagator
    #      *QQuickPopupItemPrivate::attachedPropertyPropagator_parent(const
    #      QMetaObject *attachedType)
    ritual = (
        'ritual_ZN22QQuickPopupItemPrivate33attachedPropertyPropagator_pare'
        'ntEPK11QMetaObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickPopupItemPrivate33attachedPropertyPropagato'
          'r_parentEPK11QMetaObject')
    address = self.uglySide.call(
        ritual, self._addressOf(attachedType, 'QMetaObject'),
    )
    return QtPrivate.QQuickAttachedPropertyPropagator._cuteAt(address)
