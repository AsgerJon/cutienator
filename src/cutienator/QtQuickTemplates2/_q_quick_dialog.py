"""
QQuickDialog binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickdialog_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickDialog to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum
from ..occult import Rituals
from ..QtCore import QObject
from ..QtGui import QAccessible, QPlatformDialogHelper
from ..QtQuick import QQuickItem
from . import QQuickPopup

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQuickAbstractButton, QQuickDialogPrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickDialog(QQuickPopup):
  """
  The cute side of Qt's QQuickDialog: a plain Python object standing in front
  of one C++ QQuickDialog.

  It is built on the cute 'QQuickPopup', as Qt's QQuickDialog is built on
  Qt's QQuickPopup, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickDialog that has a ritual and that Python can
  call so far, 41 names in all: 'metaObject', 'tr', 'qmlExtendedNamespace',
  'title', 'setTitle', 'header', 'setHeader', 'footer', 'setFooter',
  'standardButtons', 'setStandardButtons', 'standardButton', 'result',
  'setResult', 'implicitHeaderWidth', 'implicitHeaderHeight',
  'implicitFooterWidth', 'implicitFooterHeight', 'setOpacity', 'accept',
  'reject', 'done', 'accepted', 'rejected', 'titleChanged', 'headerChanged',
  'footerChanged', 'standardButtonsChanged', 'applied', 'reset', 'discarded',
  'helpRequested', 'resultChanged', 'implicitHeaderWidthChanged',
  'implicitHeaderHeightChanged', 'implicitFooterWidthChanged',
  'implicitFooterHeightChanged', 'itemChange', 'accessibleRole',
  'accessibilityActiveChanged', 'd_func'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickDialog::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickDialog::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickDialog::qt_qmlMarker_extendedNamespace()': one of Qt's
    own inner workings.
  - Qt's 'QQuickDialog::~QQuickDialog()': the destructor: Python never
    removes a C++ QQuickDialog.
  - Qt's 'QQuickDialog::QQuickDialog(QQuickDialogPrivate &dd, QObject
    *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QQuickDialogPrivate *QQuickDialog::d_func() const': takes in
    Python what 'QQuickDialogPrivate *QQuickDialog::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 52 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickDialog is created at the first use, not by
    'QQuickDialog(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickDialog.
  - Qt tells when it has removed the C++ QQuickDialog. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickDialog, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class StandardCode(CuteNum):
    """
    The enum 'QQuickDialog::StandardCode' of Qt, with the 2 names Qt gives in
    it.
    """

    Rejected = Kee[int](0)
    Accepted = Kee[int](1)

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
    Calls Qt's 'QString QQuickDialog::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdialog.html#tr

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
    #  QString QQuickDialog::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QQuickDialog2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def qmlExtendedNamespace() -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickDialog::qmlExtendedNamespace()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialog.html#qmlExtendedNamespace

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickDialog::qmlExtendedNamespace()
    address = Rituals.call('ritual_ZN12QQuickDialog20qmlExtendedNamespaceEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickDialog'

  #  A C++ QQuickDialog Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickDialog'

  #  The functions Qt calls itself that QQuickDialog is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'accept': (
          ('_ZN12QQuickDialog6acceptEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'reject': (
          ('_ZN12QQuickDialog6rejectEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'done': (
          ('_ZN12QQuickDialog4doneEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickDialog::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdialog.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickDialog::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QQuickDialog10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def title(self) -> str:
    """
    Calls Qt's 'QString QQuickDialog::title() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdialog.html#title

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickDialog::title() const
    return self.uglySide.call('ritual_ZNK12QQuickDialog5titleEv')

  def header(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickDialog::header() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdialog.html#header

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickDialog::header() const
    address = self.uglySide.call('ritual_ZNK12QQuickDialog6headerEv')
    return QQuickItem._cuteAt(address)

  def footer(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickDialog::footer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdialog.html#footer

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickDialog::footer() const
    address = self.uglySide.call('ritual_ZNK12QQuickDialog6footerEv')
    return QQuickItem._cuteAt(address)

  def standardButtons(self) -> QPlatformDialogHelper.StandardButtons:
    """
    Calls Qt's 'QPlatformDialogHelper::StandardButtons
    QQuickDialog::standardButtons() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdialog.html#standardButtons

    Returns
    -------

    QPlatformDialogHelper.StandardButtons
      The value standing for the combination Qt gave back.
    """
    #  QPlatformDialogHelper::StandardButtons QQuickDialog::standardButtons()
    #      const
    return QPlatformDialogHelper.StandardButtons(self.uglySide.call(
        'ritual_ZNK12QQuickDialog15standardButtonsEv',
    ))

  @overload(QPlatformDialogHelper.StandardButton)
  def standardButton(
      self,
      button: QPlatformDialogHelper.StandardButton,
  ) -> Optional[QQuickAbstractButton]:
    """
    Calls Qt's 'QQuickAbstractButton
    *QQuickDialog::standardButton(QPlatformDialogHelper::StandardButton
    button) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdialog.html#standardButton

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
    #      *QQuickDialog::standardButton(QPlatformDialogHelper::
    #      StandardButton button) const
    address = self.uglySide.call(
        'ritual_ZNK12QQuickDialog14standardButtonEN21QPlatformDialogHelper1'
        '4StandardButtonE',
        button.value,
    )
    from . import QQuickAbstractButton
    return QQuickAbstractButton._cuteAt(address)

  def result(self) -> int:
    """
    Calls Qt's 'int QQuickDialog::result() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdialog.html#result
    """
    #  int QQuickDialog::result() const
    return self.uglySide.call('ritual_ZNK12QQuickDialog6resultEv')

  def implicitHeaderWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickDialog::implicitHeaderWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialog.html#implicitHeaderWidth
    """
    #  qreal QQuickDialog::implicitHeaderWidth() const
    return self.uglySide.call(
        'ritual_ZNK12QQuickDialog19implicitHeaderWidthEv',
    )

  def implicitHeaderHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickDialog::implicitHeaderHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialog.html#implicitHeaderHeight
    """
    #  qreal QQuickDialog::implicitHeaderHeight() const
    return self.uglySide.call(
        'ritual_ZNK12QQuickDialog20implicitHeaderHeightEv',
    )

  def implicitFooterWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickDialog::implicitFooterWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialog.html#implicitFooterWidth
    """
    #  qreal QQuickDialog::implicitFooterWidth() const
    return self.uglySide.call(
        'ritual_ZNK12QQuickDialog19implicitFooterWidthEv',
    )

  def implicitFooterHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickDialog::implicitFooterHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialog.html#implicitFooterHeight
    """
    #  qreal QQuickDialog::implicitFooterHeight() const
    return self.uglySide.call(
        'ritual_ZNK12QQuickDialog20implicitFooterHeightEv',
    )

  def accessibleRole(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QQuickDialog::accessibleRole() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdialog.html#accessibleRole

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QQuickDialog::accessibleRole() const
    ritual = 'ritual_ZNK12QQuickDialog14accessibleRoleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QQuickDialog14accessibleRoleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setTitle(self, title: str) -> None:
    """
    Calls Qt's 'void QQuickDialog::setTitle(const QString &title)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdialog.html#setTitle

    Parameters
    ----------

    title : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickDialog::setTitle(const QString &title)
    self.uglySide.call('ritual_ZN12QQuickDialog8setTitleERK7QString', title)

  @overload(QQuickItem)
  @overload(NoneType)
  def setHeader(self, header: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickDialog::setHeader(QQuickItem *header)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdialog.html#setHeader

    Parameters
    ----------

    header : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDialog::setHeader(QQuickItem *header)
    self.uglySide.call(
        'ritual_ZN12QQuickDialog9setHeaderEP10QQuickItem',
        self._addressOf(header),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setFooter(self, footer: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickDialog::setFooter(QQuickItem *footer)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdialog.html#setFooter

    Parameters
    ----------

    footer : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDialog::setFooter(QQuickItem *footer)
    self.uglySide.call(
        'ritual_ZN12QQuickDialog9setFooterEP10QQuickItem',
        self._addressOf(footer),
    )

  @overload(QPlatformDialogHelper.StandardButtons)
  def setStandardButtons(
      self,
      buttons: QPlatformDialogHelper.StandardButtons,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickDialog::setStandardButtons(QPlatformDialogHelper::StandardButtons
    buttons)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialog.html#setStandardButtons

    Parameters
    ----------

    buttons : QPlatformDialogHelper.StandardButtons
      Passed on as its number.
    """
    #  void QQuickDialog::setStandardButtons(QPlatformDialogHelper::
    #      StandardButtons buttons)
    self.uglySide.call(
        'ritual_ZN12QQuickDialog18setStandardButtonsE6QFlagsIN21QPlatformDi'
        'alogHelper14StandardButtonEE',
        buttons.value,
    )

  @overload(int)
  def setResult(self, result: int) -> None:
    """
    Calls Qt's 'void QQuickDialog::setResult(int result)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdialog.html#setResult

    Parameters
    ----------

    result : int
      Passed on as it is.
    """
    #  void QQuickDialog::setResult(int result)
    self.uglySide.call('ritual_ZN12QQuickDialog9setResultEi', result)

  @overload(float)
  def setOpacity(self, opacity: float) -> None:
    """
    Calls Qt's 'void QQuickDialog::setOpacity(qreal opacity)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdialog.html#setOpacity

    Parameters
    ----------

    opacity : float
      Passed on as it is.
    """
    #  void QQuickDialog::setOpacity(qreal opacity)
    ritual = 'ritual_ZN12QQuickDialog10setOpacityEd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickDialog10setOpacityEd'
    self.uglySide.call(ritual, opacity)

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QQuickDialog::QQuickDialog(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickdialog.html#QQuickDialog

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickDialog::QQuickDialog(QObject *parent)
    self._noteCreation(QQuickDialog, lambda: Rituals.call(
        'ritual_ZN12QQuickDialogC1EP7QObject',
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

  def accept(self) -> None:
    """
    Calls Qt's 'void QQuickDialog::accept()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdialog.html#accept
    """
    #  void QQuickDialog::accept()
    ritual = 'ritual_ZN12QQuickDialog6acceptEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickDialog6acceptEv'
    self.uglySide.call(ritual)

  def reject(self) -> None:
    """
    Calls Qt's 'void QQuickDialog::reject()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdialog.html#reject
    """
    #  void QQuickDialog::reject()
    ritual = 'ritual_ZN12QQuickDialog6rejectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickDialog6rejectEv'
    self.uglySide.call(ritual)

  @overload(int)
  def done(self, result: int) -> None:
    """
    Calls Qt's 'void QQuickDialog::done(int result)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdialog.html#done

    Parameters
    ----------

    result : int
      Passed on as it is.
    """
    #  void QQuickDialog::done(int result)
    ritual = 'ritual_ZN12QQuickDialog4doneEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickDialog4doneEi'
    self.uglySide.call(ritual, result)

  def accepted(self) -> None:
    """
    Calls Qt's 'void QQuickDialog::accepted()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdialog.html#accepted
    """
    #  void QQuickDialog::accepted()
    self.uglySide.call('ritual_ZN12QQuickDialog8acceptedEv')

  def rejected(self) -> None:
    """
    Calls Qt's 'void QQuickDialog::rejected()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdialog.html#rejected
    """
    #  void QQuickDialog::rejected()
    self.uglySide.call('ritual_ZN12QQuickDialog8rejectedEv')

  def titleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDialog::titleChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdialog.html#titleChanged
    """
    #  void QQuickDialog::titleChanged()
    self.uglySide.call('ritual_ZN12QQuickDialog12titleChangedEv')

  def headerChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDialog::headerChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdialog.html#headerChanged
    """
    #  void QQuickDialog::headerChanged()
    self.uglySide.call('ritual_ZN12QQuickDialog13headerChangedEv')

  def footerChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDialog::footerChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdialog.html#footerChanged
    """
    #  void QQuickDialog::footerChanged()
    self.uglySide.call('ritual_ZN12QQuickDialog13footerChangedEv')

  def standardButtonsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDialog::standardButtonsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialog.html#standardButtonsChanged
    """
    #  void QQuickDialog::standardButtonsChanged()
    self.uglySide.call('ritual_ZN12QQuickDialog22standardButtonsChangedEv')

  def applied(self) -> None:
    """
    Calls Qt's 'void QQuickDialog::applied()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdialog.html#applied
    """
    #  void QQuickDialog::applied()
    self.uglySide.call('ritual_ZN12QQuickDialog7appliedEv')

  def reset(self) -> None:
    """
    Calls Qt's 'void QQuickDialog::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdialog.html#reset
    """
    #  void QQuickDialog::reset()
    self.uglySide.call('ritual_ZN12QQuickDialog5resetEv')

  def discarded(self) -> None:
    """
    Calls Qt's 'void QQuickDialog::discarded()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdialog.html#discarded
    """
    #  void QQuickDialog::discarded()
    self.uglySide.call('ritual_ZN12QQuickDialog9discardedEv')

  def helpRequested(self) -> None:
    """
    Calls Qt's 'void QQuickDialog::helpRequested()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdialog.html#helpRequested
    """
    #  void QQuickDialog::helpRequested()
    self.uglySide.call('ritual_ZN12QQuickDialog13helpRequestedEv')

  def resultChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDialog::resultChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdialog.html#resultChanged
    """
    #  void QQuickDialog::resultChanged()
    self.uglySide.call('ritual_ZN12QQuickDialog13resultChangedEv')

  def implicitHeaderWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDialog::implicitHeaderWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialog.html#implicitHeaderWidthChanged
    """
    #  void QQuickDialog::implicitHeaderWidthChanged()
    self.uglySide.call(
        'ritual_ZN12QQuickDialog26implicitHeaderWidthChangedEv',
    )

  def implicitHeaderHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDialog::implicitHeaderHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialog.html#implicitHeaderHeightChanged
    """
    #  void QQuickDialog::implicitHeaderHeightChanged()
    self.uglySide.call(
        'ritual_ZN12QQuickDialog27implicitHeaderHeightChangedEv',
    )

  def implicitFooterWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDialog::implicitFooterWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialog.html#implicitFooterWidthChanged
    """
    #  void QQuickDialog::implicitFooterWidthChanged()
    self.uglySide.call(
        'ritual_ZN12QQuickDialog26implicitFooterWidthChangedEv',
    )

  def implicitFooterHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDialog::implicitFooterHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialog.html#implicitFooterHeightChanged
    """
    #  void QQuickDialog::implicitFooterHeightChanged()
    self.uglySide.call(
        'ritual_ZN12QQuickDialog27implicitFooterHeightChangedEv',
    )

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      data: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickDialog::itemChange(QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdialog.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    data : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickDialog::itemChange(QQuickItem::ItemChange change, const
    #      QQuickItem::ItemChangeData &data)
    ritual = (
        'ritual_ZN12QQuickDialog10itemChangeEN10QQuickItem10ItemChangeERKNS'
        '0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QQuickDialog10itemChangeEN10QQuickItem10ItemChang'
          'eERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(data))

  @overload(bool)
  def accessibilityActiveChanged(self, active: bool) -> None:
    """
    Calls Qt's 'void QQuickDialog::accessibilityActiveChanged(bool active)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialog.html#accessibilityActiveChanged

    Parameters
    ----------

    active : bool
      Passed on as it is.
    """
    #  void QQuickDialog::accessibilityActiveChanged(bool active)
    ritual = 'ritual_ZN12QQuickDialog26accessibilityActiveChangedEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickDialog26accessibilityActiveChangedEb'
    self.uglySide.call(ritual, active)

  def d_func(self) -> Optional[QQuickDialogPrivate]:
    """
    Calls Qt's 'QQuickDialogPrivate *QQuickDialog::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdialog.html#d_func

    Returns
    -------

    Optional[QQuickDialogPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDialogPrivate *QQuickDialog::d_func()
    address = self.uglySide.call('ritual_ZN12QQuickDialog6d_funcEv')
    from . import QQuickDialogPrivate
    return QQuickDialogPrivate._cuteAt(address)
