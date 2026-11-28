"""
QDesignerDialogGuiInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/abstractdialoggui_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QDesignerDialogGuiInterface to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..QtCore import QStringList
from ..QtWidgets import QFileDialog, QMessageBox

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QString
  from ..QtWidgets import QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QString = WAIT['QString']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerDialogGuiInterface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDesignerDialogGuiInterface: a plain Python object
  standing in front of one C++ QDesignerDialogGuiInterface.

  What exists
  -----------

  Every function of Qt's QDesignerDialogGuiInterface that has a ritual and
  that Python can call so far, 7 names in all: 'message',
  'getExistingDirectory', 'getOpenFileName', 'getOpenImageFileName',
  'getOpenFileNames', 'getOpenImageFileNames', 'getSaveFileName'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDesignerDialogGuiInterface::~QDesignerDialogGuiInterface()': the
    destructor: Python never removes a C++ QDesignerDialogGuiInterface.

  What has no ritual
  ------------------

  5 of the 15 functions Qt declares: 4 forbidden; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QDesignerDialogGuiInterface is created at the first use, not by
    'QDesignerDialogGuiInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDesignerDialogGuiInterface.
  - Each name of Qt's QDesignerDialogGuiInterface that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QDesignerDialogGuiInterface, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Message(CuteNum):
    """
    The enum 'QDesignerDialogGuiInterface::Message' of Qt, with the 14 names
    Qt gives in it.
    """

    FormLoadFailureMessage = Kee[int](0)
    UiVersionMismatchMessage = Kee[int](1)
    ResourceLoadFailureMessage = Kee[int](2)
    TopLevelSpacerMessage = Kee[int](3)
    PropertyEditorMessage = Kee[int](4)
    SignalSlotEditorMessage = Kee[int](5)
    FormEditorMessage = Kee[int](6)
    PreviewFailureMessage = Kee[int](7)
    PromotionErrorMessage = Kee[int](8)
    ResourceEditorMessage = Kee[int](9)
    ScriptDialogMessage = Kee[int](10)
    SignalSlotDialogMessage = Kee[int](11)
    OtherMessage = Kee[int](12)
    FileChangedMessage = Kee[int](13)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesignerDialogGuiInterface'

  #  A C++ QDesignerDialogGuiInterface Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDesignerDialogGuiInterface'

  #  The functions Qt calls itself that QDesignerDialogGuiInterface is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'getOpenFileNames': (
          'QStringList '
          'QDesignerDialogGuiInterface::getOpenFileNames(QWidget *, const '
          'QString &, const QString &, const QString &, QString *, '
          'QFileDialog::Options)',
      ),
      'getOpenImageFileNames': (
          'QStringList '
          'QDesignerDialogGuiInterface::getOpenImageFileNames(QWidget *, '
          'const QString &, const QString &, const QString &, QString *, '
          'QFileDialog::Options)',
      ),
  }

  #  The functions Qt calls itself that QDesignerDialogGuiInterface is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'message': (
          ('_ZN27QDesignerDialogGuiInterface7messageEP7QWidgetNS_7MessageEN'
           '11QMessageBox4IconERK7QStringS7_6QFlagsINS3_14StandardButtonEES'
           '9_',
           ('int', 'enum', 'QtWidgets:QMessageBox.StandardButton'),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
               ('int', 'enum',
                'QtDesigner:QDesignerDialogGuiInterface.Message'),
               ('int', 'enum', 'QtWidgets:QMessageBox.Icon'),
               ('address', 'text', ''),
               ('address', 'text', ''),
               ('int', 'flags', 'QtWidgets:QMessageBox.StandardButton'),
               ('int', 'enum', 'QtWidgets:QMessageBox.StandardButton'),
           )),
          ('_ZN27QDesignerDialogGuiInterface7messageEP7QWidgetNS_7MessageEN'
           '11QMessageBox4IconERK7QStringS7_S7_6QFlagsINS3_14StandardButton'
           'EES9_',
           ('int', 'enum', 'QtWidgets:QMessageBox.StandardButton'),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
               ('int', 'enum',
                'QtDesigner:QDesignerDialogGuiInterface.Message'),
               ('int', 'enum', 'QtWidgets:QMessageBox.Icon'),
               ('address', 'text', ''),
               ('address', 'text', ''),
               ('address', 'text', ''),
               ('int', 'flags', 'QtWidgets:QMessageBox.StandardButton'),
               ('int', 'enum', 'QtWidgets:QMessageBox.StandardButton'),
           )),
          ('_ZN27QDesignerDialogGuiInterface7messageEP7QWidgetNS_7MessageEN'
           '11QMessageBox4IconERK7QStringS7_S7_S7_6QFlagsINS3_14StandardBut'
           'tonEES9_',
           ('int', 'enum', 'QtWidgets:QMessageBox.StandardButton'),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
               ('int', 'enum',
                'QtDesigner:QDesignerDialogGuiInterface.Message'),
               ('int', 'enum', 'QtWidgets:QMessageBox.Icon'),
               ('address', 'text', ''),
               ('address', 'text', ''),
               ('address', 'text', ''),
               ('address', 'text', ''),
               ('int', 'flags', 'QtWidgets:QMessageBox.StandardButton'),
               ('int', 'enum', 'QtWidgets:QMessageBox.StandardButton'),
           )),
      ),
      'getExistingDirectory': (
          ('_ZN27QDesignerDialogGuiInterface20getExistingDirectoryEP7QWidge'
           'tRK7QStringS4_6QFlagsIN11QFileDialog6OptionEE',
           ('address', 'text', ''),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
               ('address', 'text', ''),
               ('address', 'text', ''),
               ('int', 'flags', 'QtWidgets:QFileDialog.Option'),
           )),
      ),
      'getOpenFileName': (
          ('_ZN27QDesignerDialogGuiInterface15getOpenFileNameEP7QWidgetRK7Q'
           'StringS4_S4_PS2_6QFlagsIN11QFileDialog6OptionEE',
           ('address', 'text', ''),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
               ('address', 'text', ''),
               ('address', 'text', ''),
               ('address', 'text', ''),
               ('address', 'address', 'QtCore:QString'),
               ('int', 'flags', 'QtWidgets:QFileDialog.Option'),
           )),
      ),
      'getOpenImageFileName': (
          ('_ZN27QDesignerDialogGuiInterface20getOpenImageFileNameEP7QWidge'
           'tRK7QStringS4_S4_PS2_6QFlagsIN11QFileDialog6OptionEE',
           ('address', 'text', ''),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
               ('address', 'text', ''),
               ('address', 'text', ''),
               ('address', 'text', ''),
               ('address', 'address', 'QtCore:QString'),
               ('int', 'flags', 'QtWidgets:QFileDialog.Option'),
           )),
      ),
      'getSaveFileName': (
          ('_ZN27QDesignerDialogGuiInterface15getSaveFileNameEP7QWidgetRK7Q'
           'StringS4_S4_PS2_6QFlagsIN11QFileDialog6OptionEE',
           ('address', 'text', ''),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
               ('address', 'text', ''),
               ('address', 'text', ''),
               ('address', 'text', ''),
               ('address', 'address', 'QtCore:QString'),
               ('int', 'flags', 'QtWidgets:QFileDialog.Option'),
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
    Qt's 'QDesignerDialogGuiInterface::QDesignerDialogGuiInterface()': the
    class is abstract, so C++ cannot make one, and the C++ class of ours does
    not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QDesignerDialogGuiInterface.__init__' has no cute function yet. "
        "Qt's 'QDesignerDialogGuiInterface::QDesignerDialogGuiInterface()': "
        "the class is abstract, so C++ cannot make one, and the C++ class "
        "of ours does not fill in every function it leaves open.")

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

  @overload(QWidget, Message, QMessageBox.Icon, str, str)
  @overload(NoneType, Message, QMessageBox.Icon, str, str)
  @overload(
      QWidget, Message, QMessageBox.Icon, str, str,
      QMessageBox.StandardButtons,
  )
  @overload(
      NoneType, Message, QMessageBox.Icon, str, str,
      QMessageBox.StandardButtons,
  )
  @overload(
      QWidget, Message, QMessageBox.Icon, str, str,
      QMessageBox.StandardButtons, QMessageBox.StandardButton,
  )
  @overload(
      NoneType, Message, QMessageBox.Icon, str, str,
      QMessageBox.StandardButtons, QMessageBox.StandardButton,
  )
  def message(
      self,
      parent: Optional[QWidget],
      context: Message,
      icon: QMessageBox.Icon,
      title: str,
      text: str,
      buttons: QMessageBox.StandardButtons = QMessageBox.StandardButtons.Ok,
      defaultButton: QMessageBox.StandardButton = (
          QMessageBox.StandardButton.NoButton),
  ) -> QMessageBox.StandardButton:
    """
    Calls Qt's 'QMessageBox::StandardButton
    QDesignerDialogGuiInterface::message(QWidget *parent, Message context,
    QMessageBox::Icon icon, const QString &title, const QString &text,
    QMessageBox::StandardButtons buttons, QMessageBox::StandardButton
    defaultButton)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerdialogguiinterface.html#message

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    context : Message
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
    #      QDesignerDialogGuiInterface::message(QWidget *parent, Message
    #      context, QMessageBox::Icon icon, const QString &title, const
    #      QString &text, QMessageBox::StandardButtons buttons,
    #      QMessageBox::StandardButton defaultButton)
    return QMessageBox.StandardButton(self.uglySide.call(
        'ritual_ZN27QDesignerDialogGuiInterface7messageEP7QWidgetNS_7Messag'
        'eEN11QMessageBox4IconERK7QStringS7_6QFlagsINS3_14StandardButtonEES'
        '9_',
        self._addressOf(parent), context.value, icon.value, title, text,
        buttons.value, defaultButton.value,
    ))

  @overload(QWidget, Message, QMessageBox.Icon, str, str, str)
  @overload(NoneType, Message, QMessageBox.Icon, str, str, str)
  @overload(
      QWidget, Message, QMessageBox.Icon, str, str, str,
      QMessageBox.StandardButtons,
  )
  @overload(
      NoneType, Message, QMessageBox.Icon, str, str, str,
      QMessageBox.StandardButtons,
  )
  @overload(
      QWidget, Message, QMessageBox.Icon, str, str, str,
      QMessageBox.StandardButtons, QMessageBox.StandardButton,
  )
  @overload(
      NoneType, Message, QMessageBox.Icon, str, str, str,
      QMessageBox.StandardButtons, QMessageBox.StandardButton,
  )
  def message(
      self,
      parent: Optional[QWidget],
      context: Message,
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
    QDesignerDialogGuiInterface::message(QWidget *parent, Message context,
    QMessageBox::Icon icon, const QString &title, const QString &text, const
    QString &informativeText, QMessageBox::StandardButtons buttons,
    QMessageBox::StandardButton defaultButton)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerdialogguiinterface.html#message

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    context : Message
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
    #      QDesignerDialogGuiInterface::message(QWidget *parent, Message
    #      context, QMessageBox::Icon icon, const QString &title, const
    #      QString &text, const QString &informativeText,
    #      QMessageBox::StandardButtons buttons, QMessageBox::StandardButton
    #      defaultButton)
    return QMessageBox.StandardButton(self.uglySide.call(
        'ritual_ZN27QDesignerDialogGuiInterface7messageEP7QWidgetNS_7Messag'
        'eEN11QMessageBox4IconERK7QStringS7_S7_6QFlagsINS3_14StandardButton'
        'EES9_',
        self._addressOf(parent), context.value, icon.value, title, text,
        informativeText, buttons.value, defaultButton.value,
    ))

  @overload(QWidget, Message, QMessageBox.Icon, str, str, str, str)
  @overload(NoneType, Message, QMessageBox.Icon, str, str, str, str)
  @overload(
      QWidget, Message, QMessageBox.Icon, str, str, str, str,
      QMessageBox.StandardButtons,
  )
  @overload(
      NoneType, Message, QMessageBox.Icon, str, str, str, str,
      QMessageBox.StandardButtons,
  )
  @overload(
      QWidget, Message, QMessageBox.Icon, str, str, str, str,
      QMessageBox.StandardButtons, QMessageBox.StandardButton,
  )
  @overload(
      NoneType, Message, QMessageBox.Icon, str, str, str, str,
      QMessageBox.StandardButtons, QMessageBox.StandardButton,
  )
  def message(
      self,
      parent: Optional[QWidget],
      context: Message,
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
    QDesignerDialogGuiInterface::message(QWidget *parent, Message context,
    QMessageBox::Icon icon, const QString &title, const QString &text, const
    QString &informativeText, const QString &detailedText,
    QMessageBox::StandardButtons buttons, QMessageBox::StandardButton
    defaultButton)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerdialogguiinterface.html#message

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    context : Message
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
    #      QDesignerDialogGuiInterface::message(QWidget *parent, Message
    #      context, QMessageBox::Icon icon, const QString &title, const
    #      QString &text, const QString &informativeText, const QString
    #      &detailedText, QMessageBox::StandardButtons buttons,
    #      QMessageBox::StandardButton defaultButton)
    return QMessageBox.StandardButton(self.uglySide.call(
        'ritual_ZN27QDesignerDialogGuiInterface7messageEP7QWidgetNS_7Messag'
        'eEN11QMessageBox4IconERK7QStringS7_S7_S7_6QFlagsINS3_14StandardBut'
        'tonEES9_',
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
    QDesignerDialogGuiInterface::getExistingDirectory(QWidget *parent, const
    QString &caption, const QString &dir, QFileDialog::Options options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerdialogguiinterface.html

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
    #  QString QDesignerDialogGuiInterface::getExistingDirectory(QWidget
    #      *parent, const QString &caption, const QString &dir,
    #      QFileDialog::Options options)
    return self.uglySide.call(
        'ritual_ZN27QDesignerDialogGuiInterface20getExistingDirectoryEP7QWi'
        'dgetRK7QStringS4_6QFlagsIN11QFileDialog6OptionEE',
        self._addressOf(parent), caption, dir, options.value,
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
    Calls Qt's 'QString QDesignerDialogGuiInterface::getOpenFileName(QWidget
    *parent, const QString &caption, const QString &dir, const QString
    &filter, QString *selectedFilter, QFileDialog::Options options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerdialogguiinterface.html#getOpenFileName

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
    #  QString QDesignerDialogGuiInterface::getOpenFileName(QWidget *parent,
    #      const QString &caption, const QString &dir, const QString &filter,
    #      QString *selectedFilter, QFileDialog::Options options)
    return self.uglySide.call(
        'ritual_ZN27QDesignerDialogGuiInterface15getOpenFileNameEP7QWidgetR'
        'K7QStringS4_S4_PS2_6QFlagsIN11QFileDialog6OptionEE',
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
    QDesignerDialogGuiInterface::getOpenImageFileName(QWidget *parent, const
    QString &caption, const QString &dir, const QString &filter, QString
    *selectedFilter, QFileDialog::Options options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerdialogguiinterface.html

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
    #  QString QDesignerDialogGuiInterface::getOpenImageFileName(QWidget
    #      *parent, const QString &caption, const QString &dir, const QString
    #      &filter, QString *selectedFilter, QFileDialog::Options options)
    ritual = (
        'ritual_ZN27QDesignerDialogGuiInterface20getOpenImageFileNameEP7QWi'
        'dgetRK7QStringS4_S4_PS2_6QFlagsIN11QFileDialog6OptionEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QDesignerDialogGuiInterface20getOpenImageFileName'
          'EP7QWidgetRK7QStringS4_S4_PS2_6QFlagsIN11QFileDialog6OptionEE')
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
    QDesignerDialogGuiInterface::getOpenFileNames(QWidget *parent, const
    QString &caption, const QString &dir, const QString &filter, QString
    *selectedFilter, QFileDialog::Options options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerdialogguiinterface.html#getOpenFileNames

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
    #  QStringList QDesignerDialogGuiInterface::getOpenFileNames(QWidget
    #      *parent, const QString &caption, const QString &dir, const QString
    #      &filter, QString *selectedFilter, QFileDialog::Options options)
    address = self.uglySide.call(
        'ritual_ZN27QDesignerDialogGuiInterface16getOpenFileNamesEP7QWidget'
        'RK7QStringS4_S4_PS2_6QFlagsIN11QFileDialog6OptionEE',
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
    QDesignerDialogGuiInterface::getOpenImageFileNames(QWidget *parent, const
    QString &caption, const QString &dir, const QString &filter, QString
    *selectedFilter, QFileDialog::Options options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerdialogguiinterface.html

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
    #  QStringList QDesignerDialogGuiInterface::getOpenImageFileNames(QWidget
    #      *parent, const QString &caption, const QString &dir, const QString
    #      &filter, QString *selectedFilter, QFileDialog::Options options)
    address = self.uglySide.call(
        'ritual_ZN27QDesignerDialogGuiInterface21getOpenImageFileNamesEP7QW'
        'idgetRK7QStringS4_S4_PS2_6QFlagsIN11QFileDialog6OptionEE',
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
    Calls Qt's 'QString QDesignerDialogGuiInterface::getSaveFileName(QWidget
    *parent, const QString &caption, const QString &dir, const QString
    &filter, QString *selectedFilter, QFileDialog::Options options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerdialogguiinterface.html#getSaveFileName

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
    #  QString QDesignerDialogGuiInterface::getSaveFileName(QWidget *parent,
    #      const QString &caption, const QString &dir, const QString &filter,
    #      QString *selectedFilter, QFileDialog::Options options)
    return self.uglySide.call(
        'ritual_ZN27QDesignerDialogGuiInterface15getSaveFileNameEP7QWidgetR'
        'K7QStringS4_S4_PS2_6QFlagsIN11QFileDialog6OptionEE',
        self._addressOf(parent), caption, dir, filter,
        self._addressOf(selectedFilter), options.value,
    )
