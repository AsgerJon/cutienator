"""
QDesignerLanguageExtension binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/abstractlanguage.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject, QString
  from ..QtWidgets import QDialog, QWidget
  from . import QDesignerFormEditorInterface, QDesignerFormWindowInterface
  from . import QDesignerResourceBrowserInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerFormEditorInterface = WAIT['QDesignerFormEditorInterface']
  QDesignerFormWindowInterface = WAIT['QDesignerFormWindowInterface']
  QObject = WAIT['QObject']
  QString = WAIT['QString']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerLanguageExtension(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDesignerLanguageExtension: a plain Python object
  standing in front of one C++ QDesignerLanguageExtension.

  What exists
  -----------

  Every function of Qt's QDesignerLanguageExtension that has a ritual and
  that Python can call so far, 9 names in all: 'name',
  'createFormWindowSettingsDialog', 'createResourceBrowser',
  'createPromotionDialog', 'isLanguageResource', 'classNameOf',
  'signalMatchesSlot', 'widgetBoxContents', 'uiExtension'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDesignerLanguageExtension::~QDesignerLanguageExtension()': the
    destructor: Python never removes a C++ QDesignerLanguageExtension.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QDesignerLanguageExtension is created at the first use, not by
    'QDesignerLanguageExtension(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDesignerLanguageExtension.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesignerLanguageExtension'

  #  A C++ QDesignerLanguageExtension Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDesignerLanguageExtension'

  #  The functions Qt calls itself that QDesignerLanguageExtension is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'name': (
          ('_ZNK26QDesignerLanguageExtension4nameEv',
           ('address', 'text', ''),
           ()),
      ),
      'createFormWindowSettingsDialog': (
          ('_ZN26QDesignerLanguageExtension30createFormWindowSettingsDialog'
           'EP28QDesignerFormWindowInterfaceP7QWidget',
           ('address', 'address', 'QtWidgets:QDialog'),
           (
               ('address', 'address',
                'QtDesigner:QDesignerFormWindowInterface'),
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'createResourceBrowser': (
          ('_ZN26QDesignerLanguageExtension21createResourceBrowserEP7QWidge'
           't',
           ('address', 'address',
            'QtDesigner:QDesignerResourceBrowserInterface'),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'createPromotionDialog': (
          ('_ZN26QDesignerLanguageExtension21createPromotionDialogEP28QDesi'
           'gnerFormEditorInterfaceP7QWidget',
           ('address', 'address', 'QtWidgets:QDialog'),
           (
               ('address', 'address',
                'QtDesigner:QDesignerFormEditorInterface'),
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
          ('_ZN26QDesignerLanguageExtension21createPromotionDialogEP28QDesi'
           'gnerFormEditorInterfaceRK7QStringPS2_P7QWidget',
           ('address', 'address', 'QtWidgets:QDialog'),
           (
               ('address', 'address',
                'QtDesigner:QDesignerFormEditorInterface'),
               ('address', 'text', ''),
               ('address', 'address', 'QtCore:QString'),
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'isLanguageResource': (
          ('_ZNK26QDesignerLanguageExtension18isLanguageResourceERK7QString',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'classNameOf': (
          ('_ZNK26QDesignerLanguageExtension11classNameOfEP7QObject',
           ('address', 'text', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'signalMatchesSlot': (
          ('_ZNK26QDesignerLanguageExtension17signalMatchesSlotERK7QStringS'
           '2_',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
               ('address', 'text', ''),
           )),
      ),
      'widgetBoxContents': (
          ('_ZNK26QDesignerLanguageExtension17widgetBoxContentsEv',
           ('address', 'text', ''),
           ()),
      ),
      'uiExtension': (
          ('_ZNK26QDesignerLanguageExtension11uiExtensionEv',
           ('address', 'text', ''),
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

  def name(self) -> str:
    """
    Calls Qt's 'QString QDesignerLanguageExtension::name() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerlanguageextension.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerLanguageExtension::name() const
    return self.uglySide.call(
        'ritual_ZNK26QDesignerLanguageExtension4nameEv',
    )

  @overload(str)
  def isLanguageResource(self, path: str) -> bool:
    """
    Calls Qt's 'bool QDesignerLanguageExtension::isLanguageResource(const
    QString &path) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerlanguageextension.html#isLanguageResource

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QDesignerLanguageExtension::isLanguageResource(const QString
    #      &path) const
    return self.uglySide.call(
        'ritual_ZNK26QDesignerLanguageExtension18isLanguageResourceERK7QStr'
        'ing',
        path,
    )

  @overload(QObject)
  @overload(NoneType)
  def classNameOf(self, object: Optional[QObject]) -> str:
    """
    Calls Qt's 'QString QDesignerLanguageExtension::classNameOf(QObject
    *object) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerlanguageextension.html#classNameOf

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerLanguageExtension::classNameOf(QObject *object) const
    return self.uglySide.call(
        'ritual_ZNK26QDesignerLanguageExtension11classNameOfEP7QObject',
        self._addressOf(object, 'QObject'),
    )

  @overload(str, str)
  def signalMatchesSlot(self, signal: str, slot: str) -> bool:
    """
    Calls Qt's 'bool QDesignerLanguageExtension::signalMatchesSlot(const
    QString &signal, const QString &slot) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerlanguageextension.html#signalMatchesSlot

    Parameters
    ----------

    signal : str
      Passed on as it is: a QString is made of it for the call.

    slot : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QDesignerLanguageExtension::signalMatchesSlot(const QString
    #      &signal, const QString &slot) const
    return self.uglySide.call(
        'ritual_ZNK26QDesignerLanguageExtension17signalMatchesSlotERK7QStri'
        'ngS2_',
        signal, slot,
    )

  def widgetBoxContents(self) -> str:
    """
    Calls Qt's 'QString QDesignerLanguageExtension::widgetBoxContents()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerlanguageextension.html#widgetBoxContents

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerLanguageExtension::widgetBoxContents() const
    return self.uglySide.call(
        'ritual_ZNK26QDesignerLanguageExtension17widgetBoxContentsEv',
    )

  def uiExtension(self) -> str:
    """
    Calls Qt's 'QString QDesignerLanguageExtension::uiExtension() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerlanguageextension.html#uiExtension

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerLanguageExtension::uiExtension() const
    return self.uglySide.call(
        'ritual_ZNK26QDesignerLanguageExtension11uiExtensionEv',
    )

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
    'QDesignerLanguageExtension::QDesignerLanguageExtension()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerlanguageextension.html
    """
    #  QDesignerLanguageExtension::QDesignerLanguageExtension()
    self._noteCreation(QDesignerLanguageExtension, lambda: Rituals.call(
        'ritual_ZN26QDesignerLanguageExtensionC1Ev',
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

  @overload(QDesignerFormWindowInterface, QWidget)
  @overload(QDesignerFormWindowInterface, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def createFormWindowSettingsDialog(
      self,
      formWindow: Optional[QDesignerFormWindowInterface],
      parentWidget: Optional[QWidget],
  ) -> Optional[QDialog]:
    """
    Calls Qt's 'QDialog
    *QDesignerLanguageExtension::createFormWindowSettingsDialog(
    QDesignerFormWindowInterface *formWindow, QWidget *parentWidget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerlanguageextension.html

    Parameters
    ----------

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parentWidget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QDialog]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDialog *QDesignerLanguageExtension::createFormWindowSettingsDialog(
    #      QDesignerFormWindowInterface *formWindow, QWidget *parentWidget)
    address = self.uglySide.call(
        'ritual_ZN26QDesignerLanguageExtension30createFormWindowSettingsDia'
        'logEP28QDesignerFormWindowInterfaceP7QWidget',
        self._addressOf(formWindow), self._addressOf(parentWidget),
    )
    from ..QtWidgets import QDialog
    return QDialog._cuteAt(address)

  @overload(QWidget)
  @overload(NoneType)
  def createResourceBrowser(
      self,
      parentWidget: Optional[QWidget],
  ) -> Optional[QDesignerResourceBrowserInterface]:
    """
    Calls Qt's 'QDesignerResourceBrowserInterface
    *QDesignerLanguageExtension::createResourceBrowser(QWidget
    *parentWidget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerlanguageextension.html

    Parameters
    ----------

    parentWidget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QDesignerResourceBrowserInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerResourceBrowserInterface
    #      *QDesignerLanguageExtension::createResourceBrowser(QWidget
    #      *parentWidget)
    address = self.uglySide.call(
        'ritual_ZN26QDesignerLanguageExtension21createResourceBrowserEP7QWi'
        'dget',
        self._addressOf(parentWidget),
    )
    from . import QDesignerResourceBrowserInterface
    return QDesignerResourceBrowserInterface._cuteAt(address)

  @overload(QDesignerFormEditorInterface)
  @overload(NoneType)
  @overload(QDesignerFormEditorInterface, QWidget)
  @overload(QDesignerFormEditorInterface, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def createPromotionDialog(
      self,
      formEditor: Optional[QDesignerFormEditorInterface],
      parentWidget: Optional[QWidget] = None,
  ) -> Optional[QDialog]:
    """
    Calls Qt's 'QDialog *QDesignerLanguageExtension::createPromotionDialog(
    QDesignerFormEditorInterface *formEditor, QWidget *parentWidget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerlanguageextension.html

    Parameters
    ----------

    formEditor : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parentWidget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QDialog]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDialog *QDesignerLanguageExtension::createPromotionDialog(
    #      QDesignerFormEditorInterface *formEditor, QWidget *parentWidget)
    address = self.uglySide.call(
        'ritual_ZN26QDesignerLanguageExtension21createPromotionDialogEP28QD'
        'esignerFormEditorInterfaceP7QWidget',
        self._addressOf(formEditor), self._addressOf(parentWidget),
    )
    from ..QtWidgets import QDialog
    return QDialog._cuteAt(address)

  @overload(QDesignerFormEditorInterface, str, QString)
  @overload(QDesignerFormEditorInterface, str, NoneType)
  @overload(NoneType, str, QString)
  @overload(NoneType, str, NoneType)
  @overload(QDesignerFormEditorInterface, str, QString, QWidget)
  @overload(QDesignerFormEditorInterface, str, QString, NoneType)
  @overload(QDesignerFormEditorInterface, str, NoneType, QWidget)
  @overload(QDesignerFormEditorInterface, str, NoneType, NoneType)
  @overload(NoneType, str, QString, QWidget)
  @overload(NoneType, str, QString, NoneType)
  @overload(NoneType, str, NoneType, QWidget)
  @overload(NoneType, str, NoneType, NoneType)
  def createPromotionDialog(
      self,
      formEditor: Optional[QDesignerFormEditorInterface],
      promotableWidgetClassName: str,
      promoteToClassName: Optional[QString],
      parentWidget: Optional[QWidget] = None,
  ) -> Optional[QDialog]:
    """
    Calls Qt's 'QDialog *QDesignerLanguageExtension::createPromotionDialog(
    QDesignerFormEditorInterface *formEditor, const QString
    &promotableWidgetClassName, QString *promoteToClassName, QWidget
    *parentWidget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerlanguageextension.html

    Parameters
    ----------

    formEditor : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    promotableWidgetClassName : str
      Passed on as it is: a QString is made of it for the call.

    promoteToClassName : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parentWidget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QDialog]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDialog *QDesignerLanguageExtension::createPromotionDialog(
    #      QDesignerFormEditorInterface *formEditor, const QString
    #      &promotableWidgetClassName, QString *promoteToClassName, QWidget
    #      *parentWidget)
    address = self.uglySide.call(
        'ritual_ZN26QDesignerLanguageExtension21createPromotionDialogEP28QD'
        'esignerFormEditorInterfaceRK7QStringPS2_P7QWidget',
        self._addressOf(formEditor), promotableWidgetClassName,
        self._addressOf(promoteToClassName), self._addressOf(parentWidget),
    )
    from ..QtWidgets import QDialog
    return QDialog._cuteAt(address)
