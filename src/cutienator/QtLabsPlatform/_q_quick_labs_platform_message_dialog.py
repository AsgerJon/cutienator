"""
QQuickLabsPlatformMessageDialog binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsPlatform/6.12.0/QtLabsPlatform/private/qquicklabsplatformmessagedialog_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickLabsPlatformMessageDialog to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QQuickLabsPlatformDialog
from ..QtGui import QPlatformDialogHelper

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickLabsPlatformMessageDialog(QQuickLabsPlatformDialog):
  """
  The cute side of Qt's QQuickLabsPlatformMessageDialog: a plain Python
  object standing in front of one C++ QQuickLabsPlatformMessageDialog.

  It is built on the cute 'QQuickLabsPlatformDialog', as Qt's
  QQuickLabsPlatformMessageDialog is built on Qt's QQuickLabsPlatformDialog,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickLabsPlatformMessageDialog that has a ritual
  and that Python can call so far, 32 names in all: 'metaObject',
  'qmlExtendedNamespace', 'text', 'informativeText', 'detailedText',
  'buttons', 'textChanged', 'informativeTextChanged', 'detailedTextChanged',
  'buttonsChanged', 'clicked', 'okClicked', 'saveClicked', 'saveAllClicked',
  'openClicked', 'yesClicked', 'yesToAllClicked', 'noClicked',
  'noToAllClicked', 'abortClicked', 'retryClicked', 'ignoreClicked',
  'closeClicked', 'cancelClicked', 'discardClicked', 'helpClicked',
  'applyClicked', 'resetClicked', 'restoreDefaultsClicked', 'onCreate',
  'onShow', 'handleClick'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickLabsPlatformMessageDialog::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QQuickLabsPlatformMessageDialog::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void
    QQuickLabsPlatformMessageDialog::qt_qmlMarker_extendedNamespace()': one
    of Qt's own inner workings.

  What has no ritual
  ------------------

  8 of the 43 functions Qt declares: 5 leans on
  'QQuickLabsPlatformMessageDialog; 2 not a gap; 1 leans on 'vtable for
  QQuickLabsPlatformMessageDialog', which Qt's source does not mark for use
  from outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QQuickLabsPlatformMessageDialog is created at the first use, not
    by 'QQuickLabsPlatformMessageDialog(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickLabsPlatformMessageDialog.
  - Qt tells when it has removed the C++ QQuickLabsPlatformMessageDialog.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickLabsPlatformMessageDialog that has no cute
    function yet, '__init__', 'setButtons', 'setDetailedText',
    'setInformativeText', 'setText', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def qmlExtendedNamespace() -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QQuickLabsPlatformMessageDialog::qmlExtendedNamespace()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmessagedialog.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *QQuickLabsPlatformMessageDialog::qmlExtendedNamespace()
    address = Rituals.call(
        'ritual_ZN31QQuickLabsPlatformMessageDialog20qmlExtendedNamespaceEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickLabsPlatformMessageDialog'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QQuickLabsPlatformMessageDialog::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmessagedialog.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickLabsPlatformMessageDialog::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK31QQuickLabsPlatformMessageDialog10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def text(self) -> str:
    """
    Calls Qt's 'QString QQuickLabsPlatformMessageDialog::text() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmessagedialog.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickLabsPlatformMessageDialog::text() const
    return self.uglySide.call(
        'ritual_ZNK31QQuickLabsPlatformMessageDialog4textEv',
    )

  def informativeText(self) -> str:
    """
    Calls Qt's 'QString QQuickLabsPlatformMessageDialog::informativeText()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmessagedialog.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickLabsPlatformMessageDialog::informativeText() const
    return self.uglySide.call(
        'ritual_ZNK31QQuickLabsPlatformMessageDialog15informativeTextEv',
    )

  def detailedText(self) -> str:
    """
    Calls Qt's 'QString QQuickLabsPlatformMessageDialog::detailedText()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmessagedialog.html#detailedText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickLabsPlatformMessageDialog::detailedText() const
    return self.uglySide.call(
        'ritual_ZNK31QQuickLabsPlatformMessageDialog12detailedTextEv',
    )

  def buttons(self) -> QPlatformDialogHelper.StandardButtons:
    """
    Calls Qt's 'QPlatformDialogHelper::StandardButtons
    QQuickLabsPlatformMessageDialog::buttons() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmessagedialog.html#buttons

    Returns
    -------

    QPlatformDialogHelper.StandardButtons
      The value standing for the combination Qt gave back.
    """
    #  QPlatformDialogHelper::StandardButtons
    #      QQuickLabsPlatformMessageDialog::buttons() const
    return QPlatformDialogHelper.StandardButtons(self.uglySide.call(
        'ritual_ZNK31QQuickLabsPlatformMessageDialog7buttonsEv',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's
    'QQuickLabsPlatformMessageDialog::QQuickLabsPlatformMessageDialog(QObject
    *parent)': leans on 'vtable for QQuickLabsPlatformMessageDialog', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMessageDialog.__init__' has no cute function "
        "yet. Qt's "
        "'QQuickLabsPlatformMessageDialog::QQuickLabsPlatformMessageDialog(Q"
        "Object *parent)': leans on 'vtable for "
        "QQuickLabsPlatformMessageDialog', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

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
    Calls Qt's 'void QQuickLabsPlatformMessageDialog::textChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmessagedialog.html#textChanged
    """
    #  void QQuickLabsPlatformMessageDialog::textChanged()
    self.uglySide.call(
        'ritual_ZN31QQuickLabsPlatformMessageDialog11textChangedEv',
    )

  def informativeTextChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickLabsPlatformMessageDialog::informativeTextChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmessagedialog.html
    """
    #  void QQuickLabsPlatformMessageDialog::informativeTextChanged()
    self.uglySide.call(
        'ritual_ZN31QQuickLabsPlatformMessageDialog22informativeTextChanged'
        'Ev',
    )

  def detailedTextChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMessageDialog::detailedTextChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmessagedialog.html
    """
    #  void QQuickLabsPlatformMessageDialog::detailedTextChanged()
    self.uglySide.call(
        'ritual_ZN31QQuickLabsPlatformMessageDialog19detailedTextChangedEv',
    )

  def buttonsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMessageDialog::buttonsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmessagedialog.html
    """
    #  void QQuickLabsPlatformMessageDialog::buttonsChanged()
    self.uglySide.call(
        'ritual_ZN31QQuickLabsPlatformMessageDialog14buttonsChangedEv',
    )

  @overload(QPlatformDialogHelper.StandardButton)
  def clicked(self, button: QPlatformDialogHelper.StandardButton) -> None:
    """
    Calls Qt's 'void
    QQuickLabsPlatformMessageDialog::clicked(QPlatformDialogHelper::
    StandardButton button)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmessagedialog.html#clicked

    Parameters
    ----------

    button : QPlatformDialogHelper.StandardButton
      Passed on as its number.
    """
    #  void QQuickLabsPlatformMessageDialog::clicked(QPlatformDialogHelper::
    #      StandardButton button)
    self.uglySide.call(
        'ritual_ZN31QQuickLabsPlatformMessageDialog7clickedEN21QPlatformDia'
        'logHelper14StandardButtonE',
        button.value,
    )

  def okClicked(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMessageDialog::okClicked()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmessagedialog.html#okClicked
    """
    #  void QQuickLabsPlatformMessageDialog::okClicked()
    self.uglySide.call(
        'ritual_ZN31QQuickLabsPlatformMessageDialog9okClickedEv',
    )

  def saveClicked(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMessageDialog::saveClicked()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmessagedialog.html#saveClicked
    """
    #  void QQuickLabsPlatformMessageDialog::saveClicked()
    self.uglySide.call(
        'ritual_ZN31QQuickLabsPlatformMessageDialog11saveClickedEv',
    )

  def saveAllClicked(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMessageDialog::saveAllClicked()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmessagedialog.html
    """
    #  void QQuickLabsPlatformMessageDialog::saveAllClicked()
    self.uglySide.call(
        'ritual_ZN31QQuickLabsPlatformMessageDialog14saveAllClickedEv',
    )

  def openClicked(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMessageDialog::openClicked()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmessagedialog.html#openClicked
    """
    #  void QQuickLabsPlatformMessageDialog::openClicked()
    self.uglySide.call(
        'ritual_ZN31QQuickLabsPlatformMessageDialog11openClickedEv',
    )

  def yesClicked(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMessageDialog::yesClicked()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmessagedialog.html#yesClicked
    """
    #  void QQuickLabsPlatformMessageDialog::yesClicked()
    self.uglySide.call(
        'ritual_ZN31QQuickLabsPlatformMessageDialog10yesClickedEv',
    )

  def yesToAllClicked(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMessageDialog::yesToAllClicked()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmessagedialog.html
    """
    #  void QQuickLabsPlatformMessageDialog::yesToAllClicked()
    self.uglySide.call(
        'ritual_ZN31QQuickLabsPlatformMessageDialog15yesToAllClickedEv',
    )

  def noClicked(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMessageDialog::noClicked()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmessagedialog.html#noClicked
    """
    #  void QQuickLabsPlatformMessageDialog::noClicked()
    self.uglySide.call(
        'ritual_ZN31QQuickLabsPlatformMessageDialog9noClickedEv',
    )

  def noToAllClicked(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMessageDialog::noToAllClicked()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmessagedialog.html
    """
    #  void QQuickLabsPlatformMessageDialog::noToAllClicked()
    self.uglySide.call(
        'ritual_ZN31QQuickLabsPlatformMessageDialog14noToAllClickedEv',
    )

  def abortClicked(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMessageDialog::abortClicked()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmessagedialog.html#abortClicked
    """
    #  void QQuickLabsPlatformMessageDialog::abortClicked()
    self.uglySide.call(
        'ritual_ZN31QQuickLabsPlatformMessageDialog12abortClickedEv',
    )

  def retryClicked(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMessageDialog::retryClicked()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmessagedialog.html#retryClicked
    """
    #  void QQuickLabsPlatformMessageDialog::retryClicked()
    self.uglySide.call(
        'ritual_ZN31QQuickLabsPlatformMessageDialog12retryClickedEv',
    )

  def ignoreClicked(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMessageDialog::ignoreClicked()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmessagedialog.html#ignoreClicked
    """
    #  void QQuickLabsPlatformMessageDialog::ignoreClicked()
    self.uglySide.call(
        'ritual_ZN31QQuickLabsPlatformMessageDialog13ignoreClickedEv',
    )

  def closeClicked(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMessageDialog::closeClicked()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmessagedialog.html#closeClicked
    """
    #  void QQuickLabsPlatformMessageDialog::closeClicked()
    self.uglySide.call(
        'ritual_ZN31QQuickLabsPlatformMessageDialog12closeClickedEv',
    )

  def cancelClicked(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMessageDialog::cancelClicked()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmessagedialog.html#cancelClicked
    """
    #  void QQuickLabsPlatformMessageDialog::cancelClicked()
    self.uglySide.call(
        'ritual_ZN31QQuickLabsPlatformMessageDialog13cancelClickedEv',
    )

  def discardClicked(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMessageDialog::discardClicked()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmessagedialog.html
    """
    #  void QQuickLabsPlatformMessageDialog::discardClicked()
    self.uglySide.call(
        'ritual_ZN31QQuickLabsPlatformMessageDialog14discardClickedEv',
    )

  def helpClicked(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMessageDialog::helpClicked()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmessagedialog.html#helpClicked
    """
    #  void QQuickLabsPlatformMessageDialog::helpClicked()
    self.uglySide.call(
        'ritual_ZN31QQuickLabsPlatformMessageDialog11helpClickedEv',
    )

  def applyClicked(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMessageDialog::applyClicked()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmessagedialog.html#applyClicked
    """
    #  void QQuickLabsPlatformMessageDialog::applyClicked()
    self.uglySide.call(
        'ritual_ZN31QQuickLabsPlatformMessageDialog12applyClickedEv',
    )

  def resetClicked(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformMessageDialog::resetClicked()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmessagedialog.html#resetClicked
    """
    #  void QQuickLabsPlatformMessageDialog::resetClicked()
    self.uglySide.call(
        'ritual_ZN31QQuickLabsPlatformMessageDialog12resetClickedEv',
    )

  def restoreDefaultsClicked(self) -> None:
    """
    Calls Qt's 'void
    QQuickLabsPlatformMessageDialog::restoreDefaultsClicked()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmessagedialog.html
    """
    #  void QQuickLabsPlatformMessageDialog::restoreDefaultsClicked()
    self.uglySide.call(
        'ritual_ZN31QQuickLabsPlatformMessageDialog22restoreDefaultsClicked'
        'Ev',
    )

  @overload(QPlatformDialogHelper)
  @overload(NoneType)
  def onCreate(self, dialog: Optional[QPlatformDialogHelper]) -> None:
    """
    Calls Qt's 'void
    QQuickLabsPlatformMessageDialog::onCreate(QPlatformDialogHelper
    *dialog)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmessagedialog.html#onCreate

    Parameters
    ----------

    dialog : Optional[QPlatformDialogHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickLabsPlatformMessageDialog::onCreate(QPlatformDialogHelper
    #      *dialog)
    self.uglySide.call(
        'ritual_ZN31QQuickLabsPlatformMessageDialog8onCreateEP21QPlatformDi'
        'alogHelper',
        self._addressOf(dialog),
    )

  @overload(QPlatformDialogHelper)
  @overload(NoneType)
  def onShow(self, dialog: Optional[QPlatformDialogHelper]) -> None:
    """
    Calls Qt's 'void
    QQuickLabsPlatformMessageDialog::onShow(QPlatformDialogHelper *dialog)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmessagedialog.html#onShow

    Parameters
    ----------

    dialog : Optional[QPlatformDialogHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickLabsPlatformMessageDialog::onShow(QPlatformDialogHelper
    #      *dialog)
    ritual = (
        'ritual_ZN31QQuickLabsPlatformMessageDialog6onShowEP21QPlatformDial'
        'ogHelper')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN31QQuickLabsPlatformMessageDialog6onShowEP21QPlatfo'
          'rmDialogHelper')
    self.uglySide.call(ritual, self._addressOf(dialog))

  @overload(QPlatformDialogHelper.StandardButton)
  def handleClick(
      self,
      button: QPlatformDialogHelper.StandardButton,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickLabsPlatformMessageDialog::handleClick(QPlatformDialogHelper::
    StandardButton button)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformmessagedialog.html#handleClick

    Parameters
    ----------

    button : QPlatformDialogHelper.StandardButton
      Passed on as its number.
    """
    #  void QQuickLabsPlatformMessageDialog::handleClick(
    #      QPlatformDialogHelper::StandardButton button)
    self.uglySide.call(
        'ritual_ZN31QQuickLabsPlatformMessageDialog11handleClickEN21QPlatfo'
        'rmDialogHelper14StandardButtonE',
        button.value,
    )

  @staticmethod
  def setButtons(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickLabsPlatformMessageDialog::setButtons(QPlatformDialogHelper::
    StandardButtons buttons)': leans on
    'QQuickLabsPlatformMessageDialog::buttonsChanged()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMessageDialog.setButtons' has no cute function "
        "yet. Qt's 'void "
        "QQuickLabsPlatformMessageDialog::setButtons(QPlatformDialogHelper::"
        "StandardButtons buttons)': leans on "
        "'QQuickLabsPlatformMessageDialog::buttonsChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setDetailedText(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformMessageDialog::setDetailedText(const QString
    &text)': leans on
    'QQuickLabsPlatformMessageDialog::detailedTextChanged()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMessageDialog.setDetailedText' has no cute "
        "function yet. Qt's 'void "
        "QQuickLabsPlatformMessageDialog::setDetailedText(const QString "
        "&text)': leans on "
        "'QQuickLabsPlatformMessageDialog::detailedTextChanged()', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def setInformativeText(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformMessageDialog::setInformativeText(const
    QString &text)': leans on
    'QQuickLabsPlatformMessageDialog::informativeTextChanged()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMessageDialog.setInformativeText' has no cute "
        "function yet. Qt's 'void "
        "QQuickLabsPlatformMessageDialog::setInformativeText(const QString "
        "&text)': leans on "
        "'QQuickLabsPlatformMessageDialog::informativeTextChanged()', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def setText(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformMessageDialog::setText(const QString
    &text)': leans on 'QQuickLabsPlatformMessageDialog::textChanged()', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformMessageDialog.setText' has no cute function "
        "yet. Qt's 'void QQuickLabsPlatformMessageDialog::setText(const "
        "QString &text)': leans on "
        "'QQuickLabsPlatformMessageDialog::textChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
