"""
QDesignerExtraInfoExtension binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/extrainfo.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtWidgets import QWidget
  from . import DomUI, DomWidget, QDesignerFormEditorInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  DomUI = WAIT['DomUI']
  DomWidget = WAIT['DomWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerExtraInfoExtension(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDesignerExtraInfoExtension: a plain Python object
  standing in front of one C++ QDesignerExtraInfoExtension.

  What exists
  -----------

  Every function of Qt's QDesignerExtraInfoExtension that has a ritual and
  that Python can call so far, 8 names in all: 'core', 'widget',
  'saveUiExtraInfo', 'loadUiExtraInfo', 'saveWidgetExtraInfo',
  'loadWidgetExtraInfo', 'workingDirectory', 'setWorkingDirectory'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDesignerExtraInfoExtension::~QDesignerExtraInfoExtension()': the
    destructor: Python never removes a C++ QDesignerExtraInfoExtension.

  What has no ritual
  ------------------

  4 of the 14 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QDesignerExtraInfoExtension is created at the first use, not by
    'QDesignerExtraInfoExtension(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDesignerExtraInfoExtension.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesignerExtraInfoExtension'

  #  A C++ QDesignerExtraInfoExtension Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDesignerExtraInfoExtension'

  #  The functions Qt calls itself that QDesignerExtraInfoExtension is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'core': (
          ('_ZNK27QDesignerExtraInfoExtension4coreEv',
           ('address', 'address', 'QtDesigner:QDesignerFormEditorInterface'),
           ()),
      ),
      'widget': (
          ('_ZNK27QDesignerExtraInfoExtension6widgetEv',
           ('address', 'address', 'QtWidgets:QWidget'),
           ()),
      ),
      'saveUiExtraInfo': (
          ('_ZN27QDesignerExtraInfoExtension15saveUiExtraInfoEP5DomUI',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtDesigner:DomUI'),
           )),
      ),
      'loadUiExtraInfo': (
          ('_ZN27QDesignerExtraInfoExtension15loadUiExtraInfoEP5DomUI',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtDesigner:DomUI'),
           )),
      ),
      'saveWidgetExtraInfo': (
          ('_ZN27QDesignerExtraInfoExtension19saveWidgetExtraInfoEP9DomWidg'
           'et',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtDesigner:DomWidget'),
           )),
      ),
      'loadWidgetExtraInfo': (
          ('_ZN27QDesignerExtraInfoExtension19loadWidgetExtraInfoEP9DomWidg'
           'et',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtDesigner:DomWidget'),
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

  def core(self) -> Optional[QDesignerFormEditorInterface]:
    """
    Calls Qt's 'QDesignerFormEditorInterface
    *QDesignerExtraInfoExtension::core() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerextrainfoextension.html#core

    Returns
    -------

    Optional[QDesignerFormEditorInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerFormEditorInterface *QDesignerExtraInfoExtension::core()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK27QDesignerExtraInfoExtension4coreEv',
    )
    from . import QDesignerFormEditorInterface
    return QDesignerFormEditorInterface._cuteAt(address)

  def widget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QDesignerExtraInfoExtension::widget() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerextrainfoextension.html#widget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QDesignerExtraInfoExtension::widget() const
    address = self.uglySide.call(
        'ritual_ZNK27QDesignerExtraInfoExtension6widgetEv',
    )
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  def workingDirectory(self) -> str:
    """
    Calls Qt's 'QString QDesignerExtraInfoExtension::workingDirectory()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerextrainfoextension.html#workingDirectory

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerExtraInfoExtension::workingDirectory() const
    return self.uglySide.call(
        'ritual_ZNK27QDesignerExtraInfoExtension16workingDirectoryEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setWorkingDirectory(self, workingDirectory: str) -> None:
    """
    Calls Qt's 'void QDesignerExtraInfoExtension::setWorkingDirectory(const
    QString &workingDirectory)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerextrainfoextension.html

    Parameters
    ----------

    workingDirectory : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesignerExtraInfoExtension::setWorkingDirectory(const QString
    #      &workingDirectory)
    self.uglySide.call(
        'ritual_ZN27QDesignerExtraInfoExtension19setWorkingDirectoryERK7QSt'
        'ring',
        workingDirectory,
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QDesignerExtraInfoExtension::QDesignerExtraInfoExtension()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerextrainfoextension.html
    """
    #  QDesignerExtraInfoExtension::QDesignerExtraInfoExtension()
    self._noteCreation(QDesignerExtraInfoExtension, lambda: Rituals.call(
        'ritual_ZN27QDesignerExtraInfoExtensionC1Ev',
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

  @overload(DomUI)
  @overload(NoneType)
  def saveUiExtraInfo(self, ui: Optional[DomUI]) -> bool:
    """
    Calls Qt's 'bool QDesignerExtraInfoExtension::saveUiExtraInfo(DomUI
    *ui)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerextrainfoextension.html#saveUiExtraInfo

    Parameters
    ----------

    ui : Optional[DomUI]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDesignerExtraInfoExtension::saveUiExtraInfo(DomUI *ui)
    return self.uglySide.call(
        'ritual_ZN27QDesignerExtraInfoExtension15saveUiExtraInfoEP5DomUI',
        self._addressOf(ui),
    )

  @overload(DomUI)
  @overload(NoneType)
  def loadUiExtraInfo(self, ui: Optional[DomUI]) -> bool:
    """
    Calls Qt's 'bool QDesignerExtraInfoExtension::loadUiExtraInfo(DomUI
    *ui)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerextrainfoextension.html#loadUiExtraInfo

    Parameters
    ----------

    ui : Optional[DomUI]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDesignerExtraInfoExtension::loadUiExtraInfo(DomUI *ui)
    return self.uglySide.call(
        'ritual_ZN27QDesignerExtraInfoExtension15loadUiExtraInfoEP5DomUI',
        self._addressOf(ui),
    )

  @overload(DomWidget)
  @overload(NoneType)
  def saveWidgetExtraInfo(self, ui_widget: Optional[DomWidget]) -> bool:
    """
    Calls Qt's 'bool
    QDesignerExtraInfoExtension::saveWidgetExtraInfo(DomWidget *ui_widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerextrainfoextension.html

    Parameters
    ----------

    ui_widget : Optional[DomWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDesignerExtraInfoExtension::saveWidgetExtraInfo(DomWidget
    #      *ui_widget)
    return self.uglySide.call(
        'ritual_ZN27QDesignerExtraInfoExtension19saveWidgetExtraInfoEP9DomW'
        'idget',
        self._addressOf(ui_widget),
    )

  @overload(DomWidget)
  @overload(NoneType)
  def loadWidgetExtraInfo(self, ui_widget: Optional[DomWidget]) -> bool:
    """
    Calls Qt's 'bool
    QDesignerExtraInfoExtension::loadWidgetExtraInfo(DomWidget *ui_widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerextrainfoextension.html

    Parameters
    ----------

    ui_widget : Optional[DomWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDesignerExtraInfoExtension::loadWidgetExtraInfo(DomWidget
    #      *ui_widget)
    return self.uglySide.call(
        'ritual_ZN27QDesignerExtraInfoExtension19loadWidgetExtraInfoEP9DomW'
        'idget',
        self._addressOf(ui_widget),
    )
