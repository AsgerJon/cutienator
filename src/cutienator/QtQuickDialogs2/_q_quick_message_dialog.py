"""
QQuickMessageDialog binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickDialogs2/6.12.0/QtQuickDialogs2/private/qquickmessagedialog_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickMessageDialog to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject
from ..QtGui import QPlatformDialogHelper
from . import QQuickAbstractDialog

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickMessageDialog(QQuickAbstractDialog):
  """
  The cute side of Qt's QQuickMessageDialog: a plain Python object standing
  in front of one C++ QQuickMessageDialog.

  It is built on the cute 'QQuickAbstractDialog', as Qt's QQuickMessageDialog
  is built on Qt's QQuickAbstractDialog, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickMessageDialog that has a ritual and that
  Python can call so far, 20 names in all: 'metaObject', 'tr',
  'qmlExtendedNamespace', 'text', 'setText', 'informativeText',
  'setInformativeText', 'detailedText', 'setDetailedText', 'buttons',
  'setButtons', 'textChanged', 'informativeTextChanged',
  'detailedTextChanged', 'buttonsChanged', 'buttonClicked', 'handleClick',
  'onCreate', 'onShow', 'dialogCode'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickMessageDialog::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickMessageDialog::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickMessageDialog::qt_qmlMarker_extendedNamespace()': one of
    Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 26 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickMessageDialog is created at the first use, not by
    'QQuickMessageDialog(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickMessageDialog.
  - Qt tells when it has removed the C++ QQuickMessageDialog. Every call on
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
    Calls Qt's 'QString QQuickMessageDialog::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmessagedialog.html#tr

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
    #  QString QQuickMessageDialog::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QQuickMessageDialog2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def qmlExtendedNamespace() -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QQuickMessageDialog::qmlExtendedNamespace()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmessagedialog.html#qmlExtendedNamespace

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickMessageDialog::qmlExtendedNamespace()
    address = Rituals.call(
        'ritual_ZN19QQuickMessageDialog20qmlExtendedNamespaceEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickMessageDialog'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickMessageDialog::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmessagedialog.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickMessageDialog::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickMessageDialog10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def text(self) -> str:
    """
    Calls Qt's 'QString QQuickMessageDialog::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmessagedialog.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickMessageDialog::text() const
    return self.uglySide.call('ritual_ZNK19QQuickMessageDialog4textEv')

  def informativeText(self) -> str:
    """
    Calls Qt's 'QString QQuickMessageDialog::informativeText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmessagedialog.html#informativeText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickMessageDialog::informativeText() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickMessageDialog15informativeTextEv',
    )

  def detailedText(self) -> str:
    """
    Calls Qt's 'QString QQuickMessageDialog::detailedText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmessagedialog.html#detailedText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickMessageDialog::detailedText() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickMessageDialog12detailedTextEv',
    )

  def buttons(self) -> QPlatformDialogHelper.StandardButtons:
    """
    Calls Qt's 'QPlatformDialogHelper::StandardButtons
    QQuickMessageDialog::buttons() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmessagedialog.html#buttons

    Returns
    -------

    QPlatformDialogHelper.StandardButtons
      The value standing for the combination Qt gave back.
    """
    #  QPlatformDialogHelper::StandardButtons QQuickMessageDialog::buttons()
    #      const
    return QPlatformDialogHelper.StandardButtons(self.uglySide.call(
        'ritual_ZNK19QQuickMessageDialog7buttonsEv',
    ))

  def dialogCode(self) -> int:
    """
    Calls Qt's 'int QQuickMessageDialog::dialogCode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmessagedialog.html#dialogCode
    """
    #  int QQuickMessageDialog::dialogCode() const
    ritual = 'ritual_ZNK19QQuickMessageDialog10dialogCodeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QQuickMessageDialog10dialogCodeEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setText(self, text: str) -> None:
    """
    Calls Qt's 'void QQuickMessageDialog::setText(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmessagedialog.html#setText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickMessageDialog::setText(const QString &text)
    self.uglySide.call(
        'ritual_ZN19QQuickMessageDialog7setTextERK7QString', text,
    )

  @overload(str)
  def setInformativeText(self, text: str) -> None:
    """
    Calls Qt's 'void QQuickMessageDialog::setInformativeText(const QString
    &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmessagedialog.html#setInformativeText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickMessageDialog::setInformativeText(const QString &text)
    self.uglySide.call(
        'ritual_ZN19QQuickMessageDialog18setInformativeTextERK7QString',
        text,
    )

  @overload(str)
  def setDetailedText(self, text: str) -> None:
    """
    Calls Qt's 'void QQuickMessageDialog::setDetailedText(const QString
    &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmessagedialog.html#setDetailedText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickMessageDialog::setDetailedText(const QString &text)
    self.uglySide.call(
        'ritual_ZN19QQuickMessageDialog15setDetailedTextERK7QString', text,
    )

  @overload(QPlatformDialogHelper.StandardButtons)
  def setButtons(
      self,
      buttons: QPlatformDialogHelper.StandardButtons,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickMessageDialog::setButtons(QPlatformDialogHelper::StandardButtons
    buttons)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmessagedialog.html#setButtons

    Parameters
    ----------

    buttons : QPlatformDialogHelper.StandardButtons
      Passed on as its number.
    """
    #  void QQuickMessageDialog::setButtons(QPlatformDialogHelper::
    #      StandardButtons buttons)
    self.uglySide.call(
        'ritual_ZN19QQuickMessageDialog10setButtonsE6QFlagsIN21QPlatformDia'
        'logHelper14StandardButtonEE',
        buttons.value,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickMessageDialog::QQuickMessageDialog(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmessagedialog.html#QQuickMessageDialog

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickMessageDialog::QQuickMessageDialog(QObject *parent)
    self._noteCreation(QQuickMessageDialog, lambda: Rituals.call(
        'ritual_ZN19QQuickMessageDialogC1EP7QObject',
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

  def textChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMessageDialog::textChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmessagedialog.html#textChanged
    """
    #  void QQuickMessageDialog::textChanged()
    self.uglySide.call('ritual_ZN19QQuickMessageDialog11textChangedEv')

  def informativeTextChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMessageDialog::informativeTextChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmessagedialog.html#informativeTextChanged
    """
    #  void QQuickMessageDialog::informativeTextChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickMessageDialog22informativeTextChangedEv',
    )

  def detailedTextChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMessageDialog::detailedTextChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmessagedialog.html#detailedTextChanged
    """
    #  void QQuickMessageDialog::detailedTextChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickMessageDialog19detailedTextChangedEv',
    )

  def buttonsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMessageDialog::buttonsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmessagedialog.html#buttonsChanged
    """
    #  void QQuickMessageDialog::buttonsChanged()
    self.uglySide.call('ritual_ZN19QQuickMessageDialog14buttonsChangedEv')

  @overload(
      QPlatformDialogHelper.StandardButton, QPlatformDialogHelper.ButtonRole,
  )
  def buttonClicked(
      self,
      button: QPlatformDialogHelper.StandardButton,
      role: QPlatformDialogHelper.ButtonRole,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickMessageDialog::buttonClicked(QPlatformDialogHelper::StandardButton
    button, QPlatformDialogHelper::ButtonRole role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmessagedialog.html#buttonClicked

    Parameters
    ----------

    button : QPlatformDialogHelper.StandardButton
      Passed on as its number.

    role : QPlatformDialogHelper.ButtonRole
      Passed on as its number.
    """
    #  void QQuickMessageDialog::buttonClicked(QPlatformDialogHelper::
    #      StandardButton button, QPlatformDialogHelper::ButtonRole role)
    self.uglySide.call(
        'ritual_ZN19QQuickMessageDialog13buttonClickedEN21QPlatformDialogHe'
        'lper14StandardButtonENS0_10ButtonRoleE',
        button.value, role.value,
    )

  @overload(
      QPlatformDialogHelper.StandardButton, QPlatformDialogHelper.ButtonRole,
  )
  def handleClick(
      self,
      button: QPlatformDialogHelper.StandardButton,
      role: QPlatformDialogHelper.ButtonRole,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickMessageDialog::handleClick(QPlatformDialogHelper::StandardButton
    button, QPlatformDialogHelper::ButtonRole role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmessagedialog.html#handleClick

    Parameters
    ----------

    button : QPlatformDialogHelper.StandardButton
      Passed on as its number.

    role : QPlatformDialogHelper.ButtonRole
      Passed on as its number.
    """
    #  void QQuickMessageDialog::handleClick(QPlatformDialogHelper::
    #      StandardButton button, QPlatformDialogHelper::ButtonRole role)
    self.uglySide.call(
        'ritual_ZN19QQuickMessageDialog11handleClickEN21QPlatformDialogHelp'
        'er14StandardButtonENS0_10ButtonRoleE',
        button.value, role.value,
    )

  @overload(QPlatformDialogHelper)
  @overload(NoneType)
  def onCreate(self, dialog: Optional[QPlatformDialogHelper]) -> None:
    """
    Calls Qt's 'void QQuickMessageDialog::onCreate(QPlatformDialogHelper
    *dialog)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmessagedialog.html#onCreate

    Parameters
    ----------

    dialog : Optional[QPlatformDialogHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMessageDialog::onCreate(QPlatformDialogHelper *dialog)
    ritual = (
        'ritual_ZN19QQuickMessageDialog8onCreateEP21QPlatformDialogHelper')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickMessageDialog8onCreateEP21QPlatformDialogHe'
          'lper')
    self.uglySide.call(ritual, self._addressOf(dialog))

  @overload(QPlatformDialogHelper)
  @overload(NoneType)
  def onShow(self, dialog: Optional[QPlatformDialogHelper]) -> None:
    """
    Calls Qt's 'void QQuickMessageDialog::onShow(QPlatformDialogHelper
    *dialog)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmessagedialog.html#onShow

    Parameters
    ----------

    dialog : Optional[QPlatformDialogHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMessageDialog::onShow(QPlatformDialogHelper *dialog)
    ritual = 'ritual_ZN19QQuickMessageDialog6onShowEP21QPlatformDialogHelper'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickMessageDialog6onShowEP21QPlatformDialogHelp'
          'er')
    self.uglySide.call(ritual, self._addressOf(dialog))
