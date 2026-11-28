"""
QQuickDialogButtonBoxPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickdialogbuttonbox_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickDialogButtonBoxPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtGui import QPlatformDialogHelper
from . import QQuickContainerPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtQuick import QQuickItem
  from . import QQuickAbstractButton, QQuickDialogButtonBox
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickAbstractButton = WAIT['QQuickAbstractButton']
  QQuickDialogButtonBox = WAIT['QQuickDialogButtonBox']
  QQuickItem = WAIT['QQuickItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickDialogButtonBoxPrivate(QQuickContainerPrivate):
  """
  The cute side of Qt's QQuickDialogButtonBoxPrivate: a plain Python object
  standing in front of one C++ QQuickDialogButtonBoxPrivate.

  It is built on the cute 'QQuickContainerPrivate', as Qt's
  QQuickDialogButtonBoxPrivate is built on Qt's QQuickContainerPrivate, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickDialogButtonBoxPrivate that has a ritual and
  that Python can call so far, 15 names in all: 'q_func', 'get',
  'itemImplicitWidthChanged', 'itemImplicitHeightChanged', 'resizeContent',
  'updateLayout', 'updateFocus', 'getContentWidth', 'getContentHeight',
  'handleClick', 'buttonText', 'createStandardButton',
  'removeStandardButtons', 'updateLanguage', 'standardButton'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickDialogButtonBox *QQuickDialogButtonBoxPrivate::q_func()
    const': takes in Python what 'QQuickDialogButtonBox
    *QQuickDialogButtonBoxPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QQuickDialogButtonBoxPrivate is created at the first use, not by
    'QQuickDialogButtonBoxPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickDialogButtonBoxPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickDialogButtonBox)
  @overload(NoneType)
  def get(
      box: Optional[QQuickDialogButtonBox],
  ) -> Optional[QQuickDialogButtonBoxPrivate]:
    """
    Calls Qt's 'QQuickDialogButtonBoxPrivate
    *QQuickDialogButtonBoxPrivate::get(QQuickDialogButtonBox *box)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonboxprivate.html#get

    Parameters
    ----------

    box : Optional[QQuickDialogButtonBox]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickDialogButtonBoxPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDialogButtonBoxPrivate
    #      *QQuickDialogButtonBoxPrivate::get(QQuickDialogButtonBox *box)
    address = Rituals.call(
        'ritual_ZN28QQuickDialogButtonBoxPrivate3getEP21QQuickDialogButtonB'
        'ox',
        CuteMixin._addressOf(box),
    )
    return QQuickDialogButtonBoxPrivate._cuteAt(address)

  @staticmethod
  @overload(QPlatformDialogHelper.StandardButton)
  def buttonText(
      standardButton: QPlatformDialogHelper.StandardButton,
  ) -> str:
    """
    Calls Qt's 'QString
    QQuickDialogButtonBoxPrivate::buttonText(QPlatformDialogHelper::
    StandardButton standardButton)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonboxprivate.html#buttonText

    Parameters
    ----------

    standardButton : QPlatformDialogHelper.StandardButton
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString
    #      QQuickDialogButtonBoxPrivate::buttonText(QPlatformDialogHelper::
    #      StandardButton standardButton)
    return Rituals.call(
        'ritual_ZN28QQuickDialogButtonBoxPrivate10buttonTextEN21QPlatformDi'
        'alogHelper14StandardButtonE',
        standardButton.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickDialogButtonBoxPrivate'

  #  A C++ QQuickDialogButtonBoxPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickDialogButtonBoxPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getContentWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickDialogButtonBoxPrivate::getContentWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonboxprivate.html#getContentWidth
    """
    #  qreal QQuickDialogButtonBoxPrivate::getContentWidth() const
    ritual = 'ritual_ZNK28QQuickDialogButtonBoxPrivate15getContentWidthEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK28QQuickDialogButtonBoxPrivate15getContentWidthEv')
    return self.uglySide.call(ritual)

  def getContentHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickDialogButtonBoxPrivate::getContentHeight()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonboxprivate.html#getContentHeight
    """
    #  qreal QQuickDialogButtonBoxPrivate::getContentHeight() const
    ritual = 'ritual_ZNK28QQuickDialogButtonBoxPrivate16getContentHeightEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK28QQuickDialogButtonBoxPrivate16getContentHeightEv')
    return self.uglySide.call(ritual)

  @overload(QQuickAbstractButton)
  @overload(NoneType)
  def standardButton(
      self,
      button: Optional[QQuickAbstractButton],
  ) -> QPlatformDialogHelper.StandardButton:
    """
    Calls Qt's 'QPlatformDialogHelper::StandardButton
    QQuickDialogButtonBoxPrivate::standardButton(QQuickAbstractButton
    *button) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonboxprivate.html#standardButton

    Parameters
    ----------

    button : Optional[QQuickAbstractButton]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QPlatformDialogHelper.StandardButton
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QPlatformDialogHelper.StandardButton(number)' gives.
    """
    #  QPlatformDialogHelper::StandardButton
    #      QQuickDialogButtonBoxPrivate::standardButton(QQuickAbstractButton
    #      *button) const
    return QPlatformDialogHelper.StandardButton(self.uglySide.call(
        'ritual_ZNK28QQuickDialogButtonBoxPrivate14standardButtonEP20QQuick'
        'AbstractButton',
        self._addressOf(button),
    ))

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

  def q_func(self) -> Optional[QQuickDialogButtonBox]:
    """
    Calls Qt's 'QQuickDialogButtonBox
    *QQuickDialogButtonBoxPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonboxprivate.html#q_func

    Returns
    -------

    Optional[QQuickDialogButtonBox]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDialogButtonBox *QQuickDialogButtonBoxPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN28QQuickDialogButtonBoxPrivate6q_funcEv',
    )
    from . import QQuickDialogButtonBox
    return QQuickDialogButtonBox._cuteAt(address)

  @overload(QQuickItem)
  @overload(NoneType)
  def itemImplicitWidthChanged(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void
    QQuickDialogButtonBoxPrivate::itemImplicitWidthChanged(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonboxprivate.html

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDialogButtonBoxPrivate::itemImplicitWidthChanged(QQuickItem
    #      *item)
    ritual = (
        'ritual_ZN28QQuickDialogButtonBoxPrivate24itemImplicitWidthChangedE'
        'P10QQuickItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QQuickDialogButtonBoxPrivate24itemImplicitWidthCh'
          'angedEP10QQuickItem')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QQuickItem)
  @overload(NoneType)
  def itemImplicitHeightChanged(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void
    QQuickDialogButtonBoxPrivate::itemImplicitHeightChanged(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonboxprivate.html

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      QQuickDialogButtonBoxPrivate::itemImplicitHeightChanged(QQuickItem
    #      *item)
    ritual = (
        'ritual_ZN28QQuickDialogButtonBoxPrivate25itemImplicitHeightChanged'
        'EP10QQuickItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QQuickDialogButtonBoxPrivate25itemImplicitHeightC'
          'hangedEP10QQuickItem')
    self.uglySide.call(ritual, self._addressOf(item))

  def resizeContent(self) -> None:
    """
    Calls Qt's 'void QQuickDialogButtonBoxPrivate::resizeContent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonboxprivate.html#resizeContent
    """
    #  void QQuickDialogButtonBoxPrivate::resizeContent()
    ritual = 'ritual_ZN28QQuickDialogButtonBoxPrivate13resizeContentEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN28QQuickDialogButtonBoxPrivate13resizeContentEv'
    self.uglySide.call(ritual)

  def updateLayout(self) -> None:
    """
    Calls Qt's 'void QQuickDialogButtonBoxPrivate::updateLayout()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonboxprivate.html#updateLayout
    """
    #  void QQuickDialogButtonBoxPrivate::updateLayout()
    self.uglySide.call(
        'ritual_ZN28QQuickDialogButtonBoxPrivate12updateLayoutEv',
    )

  def updateFocus(self) -> None:
    """
    Calls Qt's 'void QQuickDialogButtonBoxPrivate::updateFocus()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonboxprivate.html#updateFocus
    """
    #  void QQuickDialogButtonBoxPrivate::updateFocus()
    self.uglySide.call(
        'ritual_ZN28QQuickDialogButtonBoxPrivate11updateFocusEv',
    )

  def handleClick(self) -> None:
    """
    Calls Qt's 'void QQuickDialogButtonBoxPrivate::handleClick()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonboxprivate.html#handleClick
    """
    #  void QQuickDialogButtonBoxPrivate::handleClick()
    self.uglySide.call(
        'ritual_ZN28QQuickDialogButtonBoxPrivate11handleClickEv',
    )

  @overload(QPlatformDialogHelper.StandardButton)
  def createStandardButton(
      self,
      button: QPlatformDialogHelper.StandardButton,
  ) -> Optional[QQuickAbstractButton]:
    """
    Calls Qt's 'QQuickAbstractButton
    *QQuickDialogButtonBoxPrivate::createStandardButton(
    QPlatformDialogHelper::StandardButton button)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonboxprivate.html

    Parameters
    ----------

    button : QPlatformDialogHelper.StandardButton
      Passed on as its number.

    Returns
    -------

    Optional[QQuickAbstractButton]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAbstractButton
    #      *QQuickDialogButtonBoxPrivate::createStandardButton(
    #      QPlatformDialogHelper::StandardButton button)
    address = self.uglySide.call(
        'ritual_ZN28QQuickDialogButtonBoxPrivate20createStandardButtonEN21Q'
        'PlatformDialogHelper14StandardButtonE',
        button.value,
    )
    from . import QQuickAbstractButton
    return QQuickAbstractButton._cuteAt(address)

  def removeStandardButtons(self) -> None:
    """
    Calls Qt's 'void QQuickDialogButtonBoxPrivate::removeStandardButtons()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonboxprivate.html
    """
    #  void QQuickDialogButtonBoxPrivate::removeStandardButtons()
    self.uglySide.call(
        'ritual_ZN28QQuickDialogButtonBoxPrivate21removeStandardButtonsEv',
    )

  def updateLanguage(self) -> None:
    """
    Calls Qt's 'void QQuickDialogButtonBoxPrivate::updateLanguage()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonboxprivate.html#updateLanguage
    """
    #  void QQuickDialogButtonBoxPrivate::updateLanguage()
    self.uglySide.call(
        'ritual_ZN28QQuickDialogButtonBoxPrivate14updateLanguageEv',
    )
