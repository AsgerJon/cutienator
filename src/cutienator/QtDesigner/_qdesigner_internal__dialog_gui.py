"""
qdesigner_internal::DialogGui binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/dialoggui_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means qdesigner_internal::DialogGui to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QStringList
from ..QtWidgets import QFileDialog, QMessageBox
from . import QDesignerDialogGuiInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QString
  from ..QtWidgets import QFileIconProvider, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QString = WAIT['QString']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class DialogGui(QDesignerDialogGuiInterface):
  """
  The cute side of Qt's qdesigner_internal::DialogGui: a plain Python object
  standing in front of one C++ qdesigner_internal::DialogGui.

  It is built on the cute 'QDesignerDialogGuiInterface', as Qt's
  qdesigner_internal::DialogGui is built on Qt's QDesignerDialogGuiInterface,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::DialogGui that has a ritual and
  that Python can call so far, 8 names in all: 'message',
  'getExistingDirectory', 'getOpenFileName', 'getOpenFileNames',
  'getSaveFileName', 'getOpenImageFileName', 'getOpenImageFileNames',
  'ensureIconProvider'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'qdesigner_internal::DialogGui::~DialogGui()': the destructor:
    Python never removes a C++ qdesigner_internal::DialogGui.
  - Qt's 'void
    qdesigner_internal::DialogGui::initializeImageFileDialog(QFileDialog &fd,
    QFileDialog::Options options, QFileDialog::FileMode a2)': takes a type
    Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ qdesigner_internal::DialogGui is created at the first use, not by
    'qdesigner_internal::DialogGui(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::DialogGui.
  - Each name of Qt's qdesigner_internal::DialogGui that has no cute function
    yet, 'initializeImageFileDialog', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::DialogGui'

  #  A C++ qdesigner_internal::DialogGui Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_qdesigner_internal_DialogGui'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::DialogGui::DialogGui()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-dialoggui.html#DialogGui
    """
    #  qdesigner_internal::DialogGui::DialogGui()
    self._noteCreation(DialogGui, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal9DialogGuiC1Ev',
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

  @overload(
      QWidget, QDesignerDialogGuiInterface.Message, QMessageBox.Icon, str,
      str,
  )
  @overload(
      NoneType, QDesignerDialogGuiInterface.Message, QMessageBox.Icon, str,
      str,
  )
  @overload(
      QWidget, QDesignerDialogGuiInterface.Message, QMessageBox.Icon, str,
      str, QMessageBox.StandardButtons,
  )
  @overload(
      NoneType, QDesignerDialogGuiInterface.Message, QMessageBox.Icon, str,
      str, QMessageBox.StandardButtons,
  )
  @overload(
      QWidget, QDesignerDialogGuiInterface.Message, QMessageBox.Icon, str,
      str, QMessageBox.StandardButtons, QMessageBox.StandardButton,
  )
  @overload(
      NoneType, QDesignerDialogGuiInterface.Message, QMessageBox.Icon, str,
      str, QMessageBox.StandardButtons, QMessageBox.StandardButton,
  )
  def message(
      self,
      parent: Optional[QWidget],
      context: QDesignerDialogGuiInterface.Message,
      icon: QMessageBox.Icon,
      title: str,
      text: str,
      buttons: QMessageBox.StandardButtons = QMessageBox.StandardButtons.Ok,
      defaultButton: QMessageBox.StandardButton = (
          QMessageBox.StandardButton.NoButton),
  ) -> QMessageBox.StandardButton:
    """
    Calls Qt's 'QMessageBox::StandardButton
    qdesigner_internal::DialogGui::message(QWidget *parent, Message context,
    QMessageBox::Icon icon, const QString &title, const QString &text,
    QMessageBox::StandardButtons buttons, QMessageBox::StandardButton
    defaultButton)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-dialoggui.html#message

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    context : QDesignerDialogGuiInterface.Message
      Passed on as its number.

    icon : QMessageBox.Icon
      Passed on as its number.

    title : str
      Passed on as it is: a QString is made of it for the call.

    text : str
      Passed on as it is: a QString is made of it for the call.

    buttons : QMessageBox.StandardButtons
      Passed on as its number. May be left out, as in Qt: it is then
      QMessageBox.StandardButtons.Ok.

    defaultButton : QMessageBox.StandardButton
      Passed on as its number. May be left out, as in Qt: it is then
      QMessageBox.StandardButton.NoButton.

    Returns
    -------

    QMessageBox.StandardButton
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QMessageBox.StandardButton(number)' gives.
    """
    #  QMessageBox::StandardButton
    #      qdesigner_internal::DialogGui::message(QWidget *parent, Message
    #      context, QMessageBox::Icon icon, const QString &title, const
    #      QString &text, QMessageBox::StandardButtons buttons,
    #      QMessageBox::StandardButton defaultButton)
    ritual = (
        'ritual_ZN18qdesigner_internal9DialogGui7messageEP7QWidgetN27QDesig'
        'nerDialogGuiInterface7MessageEN11QMessageBox4IconERK7QStringS9_6QF'
        'lagsINS5_14StandardButtonEESB_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal9DialogGui7messageEP7QWidgetN27'
          'QDesignerDialogGuiInterface7MessageEN11QMessageBox4IconERK7QStri'
          'ngS9_6QFlagsINS5_14StandardButtonEESB_')
    return QMessageBox.StandardButton(self.uglySide.call(
        ritual,
        self._addressOf(parent), context.value, icon.value, title, text,
        buttons.value, defaultButton.value,
    ))

  @overload(
      QWidget, QDesignerDialogGuiInterface.Message, QMessageBox.Icon, str,
      str, str,
  )
  @overload(
      NoneType, QDesignerDialogGuiInterface.Message, QMessageBox.Icon, str,
      str, str,
  )
  @overload(
      QWidget, QDesignerDialogGuiInterface.Message, QMessageBox.Icon, str,
      str, str, QMessageBox.StandardButtons,
  )
  @overload(
      NoneType, QDesignerDialogGuiInterface.Message, QMessageBox.Icon, str,
      str, str, QMessageBox.StandardButtons,
  )
  @overload(
      QWidget, QDesignerDialogGuiInterface.Message, QMessageBox.Icon, str,
      str, str, QMessageBox.StandardButtons, QMessageBox.StandardButton,
  )
  @overload(
      NoneType, QDesignerDialogGuiInterface.Message, QMessageBox.Icon, str,
      str, str, QMessageBox.StandardButtons, QMessageBox.StandardButton,
  )
  def message(
      self,
      parent: Optional[QWidget],
      context: QDesignerDialogGuiInterface.Message,
      icon: QMessageBox.Icon,
      title: str,
      text: str,
      informativeText: str,
      buttons: QMessageBox.StandardButtons = QMessageBox.StandardButtons.Ok,
      defaultButton: QMessageBox.StandardButton = (
          QMessageBox.StandardButton.NoButton),
  ) -> QMessageBox.StandardButton:
    """
    Calls Qt's 'QMessageBox::StandardButton
    qdesigner_internal::DialogGui::message(QWidget *parent, Message context,
    QMessageBox::Icon icon, const QString &title, const QString &text, const
    QString &informativeText, QMessageBox::StandardButtons buttons,
    QMessageBox::StandardButton defaultButton)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-dialoggui.html#message

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    context : QDesignerDialogGuiInterface.Message
      Passed on as its number.

    icon : QMessageBox.Icon
      Passed on as its number.

    title : str
      Passed on as it is: a QString is made of it for the call.

    text : str
      Passed on as it is: a QString is made of it for the call.

    informativeText : str
      Passed on as it is: a QString is made of it for the call.

    buttons : QMessageBox.StandardButtons
      Passed on as its number. May be left out, as in Qt: it is then
      QMessageBox.StandardButtons.Ok.

    defaultButton : QMessageBox.StandardButton
      Passed on as its number. May be left out, as in Qt: it is then
      QMessageBox.StandardButton.NoButton.

    Returns
    -------

    QMessageBox.StandardButton
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QMessageBox.StandardButton(number)' gives.
    """
    #  QMessageBox::StandardButton
    #      qdesigner_internal::DialogGui::message(QWidget *parent, Message
    #      context, QMessageBox::Icon icon, const QString &title, const
    #      QString &text, const QString &informativeText,
    #      QMessageBox::StandardButtons buttons, QMessageBox::StandardButton
    #      defaultButton)
    ritual = (
        'ritual_ZN18qdesigner_internal9DialogGui7messageEP7QWidgetN27QDesig'
        'nerDialogGuiInterface7MessageEN11QMessageBox4IconERK7QStringS9_S9_'
        '6QFlagsINS5_14StandardButtonEESB_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal9DialogGui7messageEP7QWidgetN27'
          'QDesignerDialogGuiInterface7MessageEN11QMessageBox4IconERK7QStri'
          'ngS9_S9_6QFlagsINS5_14StandardButtonEESB_')
    return QMessageBox.StandardButton(self.uglySide.call(
        ritual,
        self._addressOf(parent), context.value, icon.value, title, text,
        informativeText, buttons.value, defaultButton.value,
    ))

  @overload(
      QWidget, QDesignerDialogGuiInterface.Message, QMessageBox.Icon, str,
      str, str, str,
  )
  @overload(
      NoneType, QDesignerDialogGuiInterface.Message, QMessageBox.Icon, str,
      str, str, str,
  )
  @overload(
      QWidget, QDesignerDialogGuiInterface.Message, QMessageBox.Icon, str,
      str, str, str, QMessageBox.StandardButtons,
  )
  @overload(
      NoneType, QDesignerDialogGuiInterface.Message, QMessageBox.Icon, str,
      str, str, str, QMessageBox.StandardButtons,
  )
  @overload(
      QWidget, QDesignerDialogGuiInterface.Message, QMessageBox.Icon, str,
      str, str, str, QMessageBox.StandardButtons, QMessageBox.StandardButton,
  )
  @overload(
      NoneType, QDesignerDialogGuiInterface.Message, QMessageBox.Icon, str,
      str, str, str, QMessageBox.StandardButtons, QMessageBox.StandardButton,
  )
  def message(
      self,
      parent: Optional[QWidget],
      context: QDesignerDialogGuiInterface.Message,
      icon: QMessageBox.Icon,
      title: str,
      text: str,
      informativeText: str,
      detailedText: str,
      buttons: QMessageBox.StandardButtons = QMessageBox.StandardButtons.Ok,
      defaultButton: QMessageBox.StandardButton = (
          QMessageBox.StandardButton.NoButton),
  ) -> QMessageBox.StandardButton:
    """
    Calls Qt's 'QMessageBox::StandardButton
    qdesigner_internal::DialogGui::message(QWidget *parent, Message context,
    QMessageBox::Icon icon, const QString &title, const QString &text, const
    QString &informativeText, const QString &detailedText,
    QMessageBox::StandardButtons buttons, QMessageBox::StandardButton
    defaultButton)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-dialoggui.html#message

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    context : QDesignerDialogGuiInterface.Message
      Passed on as its number.

    icon : QMessageBox.Icon
      Passed on as its number.

    title : str
      Passed on as it is: a QString is made of it for the call.

    text : str
      Passed on as it is: a QString is made of it for the call.

    informativeText : str
      Passed on as it is: a QString is made of it for the call.

    detailedText : str
      Passed on as it is: a QString is made of it for the call.

    buttons : QMessageBox.StandardButtons
      Passed on as its number. May be left out, as in Qt: it is then
      QMessageBox.StandardButtons.Ok.

    defaultButton : QMessageBox.StandardButton
      Passed on as its number. May be left out, as in Qt: it is then
      QMessageBox.StandardButton.NoButton.

    Returns
    -------

    QMessageBox.StandardButton
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QMessageBox.StandardButton(number)' gives.
    """
    #  QMessageBox::StandardButton
    #      qdesigner_internal::DialogGui::message(QWidget *parent, Message
    #      context, QMessageBox::Icon icon, const QString &title, const
    #      QString &text, const QString &informativeText, const QString
    #      &detailedText, QMessageBox::StandardButtons buttons,
    #      QMessageBox::StandardButton defaultButton)
    ritual = (
        'ritual_ZN18qdesigner_internal9DialogGui7messageEP7QWidgetN27QDesig'
        'nerDialogGuiInterface7MessageEN11QMessageBox4IconERK7QStringS9_S9_'
        'S9_6QFlagsINS5_14StandardButtonEESB_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal9DialogGui7messageEP7QWidgetN27'
          'QDesignerDialogGuiInterface7MessageEN11QMessageBox4IconERK7QStri'
          'ngS9_S9_S9_6QFlagsINS5_14StandardButtonEESB_')
    return QMessageBox.StandardButton(self.uglySide.call(
        ritual,
        self._addressOf(parent), context.value, icon.value, title, text,
        informativeText, detailedText, buttons.value, defaultButton.value,
    ))

  @overload()
  @overload(QWidget)
  @overload(NoneType)
  @overload(QWidget, str)
  @overload(NoneType, str)
  @overload(QWidget, str, str)
  @overload(NoneType, str, str)
  @overload(QWidget, str, str, QFileDialog.Options)
  @overload(NoneType, str, str, QFileDialog.Options)
  def getExistingDirectory(
      self,
      parent: Optional[QWidget] = None,
      caption: str = '',
      dir: str = '',
      options: QFileDialog.Options = QFileDialog.Options.ShowDirsOnly,
  ) -> str:
    """
    Calls Qt's 'QString
    qdesigner_internal::DialogGui::getExistingDirectory(QWidget *parent,
    const QString &caption, const QString &dir, QFileDialog::Options
    options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-dialoggui.html

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    caption : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    dir : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    options : QFileDialog.Options
      Passed on as its number. May be left out, as in Qt: it is then
      QFileDialog.Options.ShowDirsOnly.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::DialogGui::getExistingDirectory(QWidget
    #      *parent, const QString &caption, const QString &dir,
    #      QFileDialog::Options options)
    ritual = (
        'ritual_ZN18qdesigner_internal9DialogGui20getExistingDirectoryEP7QW'
        'idgetRK7QStringS5_6QFlagsIN11QFileDialog6OptionEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal9DialogGui20getExistingDirector'
          'yEP7QWidgetRK7QStringS5_6QFlagsIN11QFileDialog6OptionEE')
    return self.uglySide.call(
        ritual, self._addressOf(parent), caption, dir, options.value,
    )

  @overload()
  @overload(QWidget)
  @overload(NoneType)
  @overload(QWidget, str)
  @overload(NoneType, str)
  @overload(QWidget, str, str)
  @overload(NoneType, str, str)
  @overload(QWidget, str, str, str)
  @overload(NoneType, str, str, str)
  @overload(QWidget, str, str, str, QString)
  @overload(QWidget, str, str, str, NoneType)
  @overload(NoneType, str, str, str, QString)
  @overload(NoneType, str, str, str, NoneType)
  @overload(QWidget, str, str, str, QString, QFileDialog.Options)
  @overload(QWidget, str, str, str, NoneType, QFileDialog.Options)
  @overload(NoneType, str, str, str, QString, QFileDialog.Options)
  @overload(NoneType, str, str, str, NoneType, QFileDialog.Options)
  def getOpenFileName(
      self,
      parent: Optional[QWidget] = None,
      caption: str = '',
      dir: str = '',
      filter: str = '',
      selectedFilter: Optional[QString] = None,
      options: QFileDialog.Options = QFileDialog.Options(),
  ) -> str:
    """
    Calls Qt's 'QString
    qdesigner_internal::DialogGui::getOpenFileName(QWidget *parent, const
    QString &caption, const QString &dir, const QString &filter, QString
    *selectedFilter, QFileDialog::Options options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-dialoggui.html#getOpenFileName

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    caption : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    dir : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    filter : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    selectedFilter : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    options : QFileDialog.Options
      Passed on as its number. May be left out, as in Qt: it is then
      QFileDialog.Options().

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::DialogGui::getOpenFileName(QWidget
    #      *parent, const QString &caption, const QString &dir, const QString
    #      &filter, QString *selectedFilter, QFileDialog::Options options)
    ritual = (
        'ritual_ZN18qdesigner_internal9DialogGui15getOpenFileNameEP7QWidget'
        'RK7QStringS5_S5_PS3_6QFlagsIN11QFileDialog6OptionEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal9DialogGui15getOpenFileNameEP7Q'
          'WidgetRK7QStringS5_S5_PS3_6QFlagsIN11QFileDialog6OptionEE')
    return self.uglySide.call(
        ritual,
        self._addressOf(parent), caption, dir, filter,
        self._addressOf(selectedFilter), options.value,
    )

  @overload()
  @overload(QWidget)
  @overload(NoneType)
  @overload(QWidget, str)
  @overload(NoneType, str)
  @overload(QWidget, str, str)
  @overload(NoneType, str, str)
  @overload(QWidget, str, str, str)
  @overload(NoneType, str, str, str)
  @overload(QWidget, str, str, str, QString)
  @overload(QWidget, str, str, str, NoneType)
  @overload(NoneType, str, str, str, QString)
  @overload(NoneType, str, str, str, NoneType)
  @overload(QWidget, str, str, str, QString, QFileDialog.Options)
  @overload(QWidget, str, str, str, NoneType, QFileDialog.Options)
  @overload(NoneType, str, str, str, QString, QFileDialog.Options)
  @overload(NoneType, str, str, str, NoneType, QFileDialog.Options)
  def getOpenFileNames(
      self,
      parent: Optional[QWidget] = None,
      caption: str = '',
      dir: str = '',
      filter: str = '',
      selectedFilter: Optional[QString] = None,
      options: QFileDialog.Options = QFileDialog.Options(),
  ) -> QStringList:
    """
    Calls Qt's 'QStringList
    qdesigner_internal::DialogGui::getOpenFileNames(QWidget *parent, const
    QString &caption, const QString &dir, const QString &filter, QString
    *selectedFilter, QFileDialog::Options options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-dialoggui.html#getOpenFileNames

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    caption : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    dir : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    filter : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    selectedFilter : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    options : QFileDialog.Options
      Passed on as its number. May be left out, as in Qt: it is then
      QFileDialog.Options().

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList qdesigner_internal::DialogGui::getOpenFileNames(QWidget
    #      *parent, const QString &caption, const QString &dir, const QString
    #      &filter, QString *selectedFilter, QFileDialog::Options options)
    address = self.uglySide.call(
        'ritual_ZN18qdesigner_internal9DialogGui16getOpenFileNamesEP7QWidge'
        'tRK7QStringS5_S5_PS3_6QFlagsIN11QFileDialog6OptionEE',
        self._addressOf(parent), caption, dir, filter,
        self._addressOf(selectedFilter), options.value,
    )
    return QStringList._cuteOwning(address)

  @overload()
  @overload(QWidget)
  @overload(NoneType)
  @overload(QWidget, str)
  @overload(NoneType, str)
  @overload(QWidget, str, str)
  @overload(NoneType, str, str)
  @overload(QWidget, str, str, str)
  @overload(NoneType, str, str, str)
  @overload(QWidget, str, str, str, QString)
  @overload(QWidget, str, str, str, NoneType)
  @overload(NoneType, str, str, str, QString)
  @overload(NoneType, str, str, str, NoneType)
  @overload(QWidget, str, str, str, QString, QFileDialog.Options)
  @overload(QWidget, str, str, str, NoneType, QFileDialog.Options)
  @overload(NoneType, str, str, str, QString, QFileDialog.Options)
  @overload(NoneType, str, str, str, NoneType, QFileDialog.Options)
  def getSaveFileName(
      self,
      parent: Optional[QWidget] = None,
      caption: str = '',
      dir: str = '',
      filter: str = '',
      selectedFilter: Optional[QString] = None,
      options: QFileDialog.Options = QFileDialog.Options(),
  ) -> str:
    """
    Calls Qt's 'QString
    qdesigner_internal::DialogGui::getSaveFileName(QWidget *parent, const
    QString &caption, const QString &dir, const QString &filter, QString
    *selectedFilter, QFileDialog::Options options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-dialoggui.html#getSaveFileName

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    caption : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    dir : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    filter : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    selectedFilter : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    options : QFileDialog.Options
      Passed on as its number. May be left out, as in Qt: it is then
      QFileDialog.Options().

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::DialogGui::getSaveFileName(QWidget
    #      *parent, const QString &caption, const QString &dir, const QString
    #      &filter, QString *selectedFilter, QFileDialog::Options options)
    ritual = (
        'ritual_ZN18qdesigner_internal9DialogGui15getSaveFileNameEP7QWidget'
        'RK7QStringS5_S5_PS3_6QFlagsIN11QFileDialog6OptionEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal9DialogGui15getSaveFileNameEP7Q'
          'WidgetRK7QStringS5_S5_PS3_6QFlagsIN11QFileDialog6OptionEE')
    return self.uglySide.call(
        ritual,
        self._addressOf(parent), caption, dir, filter,
        self._addressOf(selectedFilter), options.value,
    )

  @overload()
  @overload(QWidget)
  @overload(NoneType)
  @overload(QWidget, str)
  @overload(NoneType, str)
  @overload(QWidget, str, str)
  @overload(NoneType, str, str)
  @overload(QWidget, str, str, str)
  @overload(NoneType, str, str, str)
  @overload(QWidget, str, str, str, QString)
  @overload(QWidget, str, str, str, NoneType)
  @overload(NoneType, str, str, str, QString)
  @overload(NoneType, str, str, str, NoneType)
  @overload(QWidget, str, str, str, QString, QFileDialog.Options)
  @overload(QWidget, str, str, str, NoneType, QFileDialog.Options)
  @overload(NoneType, str, str, str, QString, QFileDialog.Options)
  @overload(NoneType, str, str, str, NoneType, QFileDialog.Options)
  def getOpenImageFileName(
      self,
      parent: Optional[QWidget] = None,
      caption: str = '',
      dir: str = '',
      filter: str = '',
      selectedFilter: Optional[QString] = None,
      options: QFileDialog.Options = QFileDialog.Options(),
  ) -> str:
    """
    Calls Qt's 'QString
    qdesigner_internal::DialogGui::getOpenImageFileName(QWidget *parent,
    const QString &caption, const QString &dir, const QString &filter,
    QString *selectedFilter, QFileDialog::Options options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-dialoggui.html

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    caption : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    dir : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    filter : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    selectedFilter : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    options : QFileDialog.Options
      Passed on as its number. May be left out, as in Qt: it is then
      QFileDialog.Options().

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::DialogGui::getOpenImageFileName(QWidget
    #      *parent, const QString &caption, const QString &dir, const QString
    #      &filter, QString *selectedFilter, QFileDialog::Options options)
    ritual = (
        'ritual_ZN18qdesigner_internal9DialogGui20getOpenImageFileNameEP7QW'
        'idgetRK7QStringS5_S5_PS3_6QFlagsIN11QFileDialog6OptionEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal9DialogGui20getOpenImageFileNam'
          'eEP7QWidgetRK7QStringS5_S5_PS3_6QFlagsIN11QFileDialog6OptionEE')
    return self.uglySide.call(
        ritual,
        self._addressOf(parent), caption, dir, filter,
        self._addressOf(selectedFilter), options.value,
    )

  @overload()
  @overload(QWidget)
  @overload(NoneType)
  @overload(QWidget, str)
  @overload(NoneType, str)
  @overload(QWidget, str, str)
  @overload(NoneType, str, str)
  @overload(QWidget, str, str, str)
  @overload(NoneType, str, str, str)
  @overload(QWidget, str, str, str, QString)
  @overload(QWidget, str, str, str, NoneType)
  @overload(NoneType, str, str, str, QString)
  @overload(NoneType, str, str, str, NoneType)
  @overload(QWidget, str, str, str, QString, QFileDialog.Options)
  @overload(QWidget, str, str, str, NoneType, QFileDialog.Options)
  @overload(NoneType, str, str, str, QString, QFileDialog.Options)
  @overload(NoneType, str, str, str, NoneType, QFileDialog.Options)
  def getOpenImageFileNames(
      self,
      parent: Optional[QWidget] = None,
      caption: str = '',
      dir: str = '',
      filter: str = '',
      selectedFilter: Optional[QString] = None,
      options: QFileDialog.Options = QFileDialog.Options(),
  ) -> QStringList:
    """
    Calls Qt's 'QStringList
    qdesigner_internal::DialogGui::getOpenImageFileNames(QWidget *parent,
    const QString &caption, const QString &dir, const QString &filter,
    QString *selectedFilter, QFileDialog::Options options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-dialoggui.html

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    caption : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    dir : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    filter : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    selectedFilter : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    options : QFileDialog.Options
      Passed on as its number. May be left out, as in Qt: it is then
      QFileDialog.Options().

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList
    #      qdesigner_internal::DialogGui::getOpenImageFileNames(QWidget
    #      *parent, const QString &caption, const QString &dir, const QString
    #      &filter, QString *selectedFilter, QFileDialog::Options options)
    address = self.uglySide.call(
        'ritual_ZN18qdesigner_internal9DialogGui21getOpenImageFileNamesEP7Q'
        'WidgetRK7QStringS5_S5_PS3_6QFlagsIN11QFileDialog6OptionEE',
        self._addressOf(parent), caption, dir, filter,
        self._addressOf(selectedFilter), options.value,
    )
    return QStringList._cuteOwning(address)

  def ensureIconProvider(self) -> Optional[QFileIconProvider]:
    """
    Calls Qt's 'QFileIconProvider
    *qdesigner_internal::DialogGui::ensureIconProvider()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-dialoggui.html

    Returns
    -------

    Optional[QFileIconProvider]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFileIconProvider *qdesigner_internal::DialogGui::ensureIconProvider()
    address = self.uglySide.call(
        'ritual_ZN18qdesigner_internal9DialogGui18ensureIconProviderEv',
    )
    from ..QtWidgets import QFileIconProvider
    return QFileIconProvider._cuteAt(address)

  @staticmethod
  def initializeImageFileDialog(*__, **_) -> Never:
    """
    Qt's 'void
    qdesigner_internal::DialogGui::initializeImageFileDialog(QFileDialog &fd,
    QFileDialog::Options options, QFileDialog::FileMode a2)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'qdesigner_internal.DialogGui.initializeImageFileDialog' has no "
        "cute function yet. Qt's 'void "
        "qdesigner_internal::DialogGui::initializeImageFileDialog(QFileDialo"
        "g &fd, QFileDialog::Options options, QFileDialog::FileMode a2)': "
        "takes a type Python has no way to hand over yet.")
