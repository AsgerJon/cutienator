"""
QQStyleKitControls binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitcontrols_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQStyleKitControls to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QQStyleKitControl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQStyleKitControl = WAIT['QQStyleKitControl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQStyleKitControls(QObject):
  """
  The cute side of Qt's QQStyleKitControls: a plain Python object standing in
  front of one C++ QQStyleKitControls.

  It is built on the cute 'QObject', as Qt's QQStyleKitControls is built on
  Qt's QObject, and has everything that class has. Qt's QQStyleKitControls is
  built on Qt's QQmlParserStatus as well, which is not reflected.

  What exists
  -----------

  Every function of Qt's QQStyleKitControls that has a ritual and that Python
  can call so far, 100 names in all: 'metaObject', 'set_applicationWindow',
  'set_abstractButton', 'set_control', 'set_busyIndicator', 'set_button',
  'set_checkBox', 'set_checkDelegate', 'set_comboBox', 'set_delayButton',
  'set_dial', 'set_dialog', 'set_dialogButtonBox', 'set_flatButton',
  'set_progressBar', 'set_scrollBar', 'set_scrollIndicator',
  'set_scrollView', 'set_searchField', 'set_slider', 'set_spinBox',
  'set_tabBar', 'set_tabButton', 'set_textField', 'set_textInput',
  'set_toolBar', 'set_toolButton', 'set_toolSeparator', 'set_swipeDelegate',
  'set_switchControl', 'set_switchDelegate', 'set_radioButton',
  'set_radioDelegate', 'set_roundButton', 'set_itemDelegate', 'set_popup',
  'set_pane', 'set_page', 'set_pageIndicator', 'set_frame', 'set_label',
  'set_groupBox', 'set_textArea', 'set_menu', 'set_menuBar',
  'set_menuBarItem', 'set_menuItem', 'set_menuSeparator', 'getControlStyle',
  'children', 'dataChanged', 'applicationWindowChanged',
  'abstractButtonChanged', 'controlChanged', 'busyIndicatorChanged',
  'buttonChanged', 'checkBoxChanged', 'checkDelegateChanged',
  'comboBoxChanged', 'delayButtonChanged', 'dialChanged', 'dialogChanged',
  'dialogButtonBoxChanged', 'flatButtonChanged', 'progressBarChanged',
  'scrollBarChanged', 'scrollIndicatorChanged', 'scrollViewChanged',
  'searchFieldChanged', 'sliderChanged', 'spinBoxChanged', 'tabBarChanged',
  'tabButtonChanged', 'textFieldChanged', 'textInputChanged',
  'toolBarChanged', 'toolButtonChanged', 'toolSeparatorChanged',
  'swipeDelegateChanged', 'switchControlChanged', 'switchDelegateChanged',
  'radioButtonChanged', 'radioDelegateChanged', 'roundButtonChanged',
  'itemDelegateChanged', 'popupChanged', 'paneChanged', 'pageChanged',
  'pageIndicatorChanged', 'frameChanged', 'labelChanged', 'groupBoxChanged',
  'textAreaChanged', 'menuChanged', 'menuBarChanged', 'menuBarItemChanged',
  'menuItemChanged', 'menuSeparatorChanged', 'classBegin',
  'componentComplete'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQStyleKitControls::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQStyleKitControls::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQStyleKitControls::qt_qmlMarker_uncreatable()': one of Qt's
    own inner workings.
  - Qt's 'QQmlListProperty<QObject> QQStyleKitControls::data()': gives a type
    Python has no way to take yet.

  What has no ritual
  ------------------

  53 of the 157 functions Qt declares: 48 leans on 'QQStyleKitControls; 2 not
  a gap; 2 forbidden; 1 leans on 'vtable for QQStyleKitControls', which Qt's
  source does not mark for use from outside Qt and has no code for that could
  be taken.

  What to expect
  --------------

  - The C++ QQStyleKitControls is created at the first use, not by
    'QQStyleKitControls(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQStyleKitControls.
  - Qt tells when it has removed the C++ QQStyleKitControls. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQStyleKitControls that has no cute function yet,
    '__init__', 'abstractButton', 'applicationWindow', 'busyIndicator',
    'button', 'checkBox', 'checkDelegate', 'comboBox', 'control', 'data',
    'delayButton', 'dial', 'dialog', 'dialogButtonBox', 'flatButton',
    'frame', 'groupBox', 'itemDelegate', 'label', 'menu', 'menuBar',
    'menuBarItem', 'menuItem', 'menuSeparator', 'page', 'pageIndicator',
    'pane', 'popup', 'progressBar', 'radioButton', 'radioDelegate',
    'roundButton', 'scrollBar', 'scrollIndicator', 'scrollView',
    'searchField', 'slider', 'spinBox', 'swipeDelegate', 'switchControl',
    'switchDelegate', 'tabBar', 'tabButton', 'textArea', 'textField',
    'textInput', 'toolBar', 'toolButton', 'toolSeparator', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQStyleKitControls'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQStyleKitControls::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitcontrols.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQStyleKitControls::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QQStyleKitControls10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(int)
  def getControlStyle(self, controlType: int) -> Optional[QQStyleKitControl]:
    """
    Calls Qt's 'QQStyleKitControl
    *QQStyleKitControls::getControlStyle(QQStyleKitExtendableControlType
    controlType) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#getControlStyle

    Parameters
    ----------

    controlType : int
      Passed on as it is.

    Returns
    -------

    Optional[QQStyleKitControl]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQStyleKitControl *QQStyleKitControls::getControlStyle(
    #      QQStyleKitExtendableControlType controlType) const
    address = self.uglySide.call(
        'ritual_ZNK18QQStyleKitControls15getControlStyleEj', controlType,
    )
    from . import QQStyleKitControl
    return QQStyleKitControl._cuteAt(address)

  def children(self) -> QList[QObject]:
    """
    Calls Qt's 'const QList<QObject *> QQStyleKitControls::children() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitcontrols.html#children

    Returns
    -------

    QList[QObject]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QList<QObject *> QQStyleKitControls::children() const
    address = self.uglySide.call('ritual_ZNK18QQStyleKitControls8childrenEv')
    return QList[QObject]._cuteOwning(address)

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
    Qt's 'QQStyleKitControls::QQStyleKitControls(QObject *parent)': leans on
    'vtable for QQStyleKitControls', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.__init__' has no cute function yet. Qt's "
        "'QQStyleKitControls::QQStyleKitControls(QObject *parent)': leans "
        "on 'vtable for QQStyleKitControls', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

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

  @overload(QQStyleKitControl)
  @overload(NoneType)
  def set_applicationWindow(
      self,
      control: Optional[QQStyleKitControl],
  ) -> None:
    """
    Calls Qt's 'void
    QQStyleKitControls::set_applicationWindow(QQStyleKitControl *control)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#set_applicationWindow

    Parameters
    ----------

    control : Optional[QQStyleKitControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControls::set_applicationWindow(QQStyleKitControl
    #      *control)
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls21set_applicationWindowEP17QQStyleKit'
        'Control',
        self._addressOf(control),
    )

  @overload(QQStyleKitControl)
  @overload(NoneType)
  def set_abstractButton(self, control: Optional[QQStyleKitControl]) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::set_abstractButton(QQStyleKitControl
    *control)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#set_abstractButton

    Parameters
    ----------

    control : Optional[QQStyleKitControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControls::set_abstractButton(QQStyleKitControl
    #      *control)
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls18set_abstractButtonEP17QQStyleKitCon'
        'trol',
        self._addressOf(control),
    )

  @overload(QQStyleKitControl)
  @overload(NoneType)
  def set_control(self, control: Optional[QQStyleKitControl]) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::set_control(QQStyleKitControl
    *control)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#set_control

    Parameters
    ----------

    control : Optional[QQStyleKitControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControls::set_control(QQStyleKitControl *control)
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls11set_controlEP17QQStyleKitControl',
        self._addressOf(control),
    )

  @overload(QQStyleKitControl)
  @overload(NoneType)
  def set_busyIndicator(self, control: Optional[QQStyleKitControl]) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::set_busyIndicator(QQStyleKitControl
    *control)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#set_busyIndicator

    Parameters
    ----------

    control : Optional[QQStyleKitControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControls::set_busyIndicator(QQStyleKitControl *control)
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls17set_busyIndicatorEP17QQStyleKitCont'
        'rol',
        self._addressOf(control),
    )

  @overload(QQStyleKitControl)
  @overload(NoneType)
  def set_button(self, control: Optional[QQStyleKitControl]) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::set_button(QQStyleKitControl
    *control)'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitcontrols.html#set_button

    Parameters
    ----------

    control : Optional[QQStyleKitControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControls::set_button(QQStyleKitControl *control)
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls10set_buttonEP17QQStyleKitControl',
        self._addressOf(control),
    )

  @overload(QQStyleKitControl)
  @overload(NoneType)
  def set_checkBox(self, control: Optional[QQStyleKitControl]) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::set_checkBox(QQStyleKitControl
    *control)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#set_checkBox

    Parameters
    ----------

    control : Optional[QQStyleKitControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControls::set_checkBox(QQStyleKitControl *control)
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls12set_checkBoxEP17QQStyleKitControl',
        self._addressOf(control),
    )

  @overload(QQStyleKitControl)
  @overload(NoneType)
  def set_checkDelegate(self, control: Optional[QQStyleKitControl]) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::set_checkDelegate(QQStyleKitControl
    *control)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#set_checkDelegate

    Parameters
    ----------

    control : Optional[QQStyleKitControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControls::set_checkDelegate(QQStyleKitControl *control)
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls17set_checkDelegateEP17QQStyleKitCont'
        'rol',
        self._addressOf(control),
    )

  @overload(QQStyleKitControl)
  @overload(NoneType)
  def set_comboBox(self, control: Optional[QQStyleKitControl]) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::set_comboBox(QQStyleKitControl
    *control)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#set_comboBox

    Parameters
    ----------

    control : Optional[QQStyleKitControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControls::set_comboBox(QQStyleKitControl *control)
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls12set_comboBoxEP17QQStyleKitControl',
        self._addressOf(control),
    )

  @overload(QQStyleKitControl)
  @overload(NoneType)
  def set_delayButton(self, control: Optional[QQStyleKitControl]) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::set_delayButton(QQStyleKitControl
    *control)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#set_delayButton

    Parameters
    ----------

    control : Optional[QQStyleKitControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControls::set_delayButton(QQStyleKitControl *control)
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls15set_delayButtonEP17QQStyleKitContro'
        'l',
        self._addressOf(control),
    )

  @overload(QQStyleKitControl)
  @overload(NoneType)
  def set_dial(self, control: Optional[QQStyleKitControl]) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::set_dial(QQStyleKitControl
    *control)'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitcontrols.html#set_dial

    Parameters
    ----------

    control : Optional[QQStyleKitControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControls::set_dial(QQStyleKitControl *control)
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls8set_dialEP17QQStyleKitControl',
        self._addressOf(control),
    )

  @overload(QQStyleKitControl)
  @overload(NoneType)
  def set_dialog(self, control: Optional[QQStyleKitControl]) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::set_dialog(QQStyleKitControl
    *control)'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitcontrols.html#set_dialog

    Parameters
    ----------

    control : Optional[QQStyleKitControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControls::set_dialog(QQStyleKitControl *control)
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls10set_dialogEP17QQStyleKitControl',
        self._addressOf(control),
    )

  @overload(QQStyleKitControl)
  @overload(NoneType)
  def set_dialogButtonBox(
      self,
      control: Optional[QQStyleKitControl],
  ) -> None:
    """
    Calls Qt's 'void
    QQStyleKitControls::set_dialogButtonBox(QQStyleKitControl *control)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#set_dialogButtonBox

    Parameters
    ----------

    control : Optional[QQStyleKitControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControls::set_dialogButtonBox(QQStyleKitControl
    #      *control)
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls19set_dialogButtonBoxEP17QQStyleKitCo'
        'ntrol',
        self._addressOf(control),
    )

  @overload(QQStyleKitControl)
  @overload(NoneType)
  def set_flatButton(self, control: Optional[QQStyleKitControl]) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::set_flatButton(QQStyleKitControl
    *control)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#set_flatButton

    Parameters
    ----------

    control : Optional[QQStyleKitControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControls::set_flatButton(QQStyleKitControl *control)
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls14set_flatButtonEP17QQStyleKitControl',
        self._addressOf(control),
    )

  @overload(QQStyleKitControl)
  @overload(NoneType)
  def set_progressBar(self, control: Optional[QQStyleKitControl]) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::set_progressBar(QQStyleKitControl
    *control)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#set_progressBar

    Parameters
    ----------

    control : Optional[QQStyleKitControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControls::set_progressBar(QQStyleKitControl *control)
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls15set_progressBarEP17QQStyleKitContro'
        'l',
        self._addressOf(control),
    )

  @overload(QQStyleKitControl)
  @overload(NoneType)
  def set_scrollBar(self, control: Optional[QQStyleKitControl]) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::set_scrollBar(QQStyleKitControl
    *control)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#set_scrollBar

    Parameters
    ----------

    control : Optional[QQStyleKitControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControls::set_scrollBar(QQStyleKitControl *control)
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls13set_scrollBarEP17QQStyleKitControl',
        self._addressOf(control),
    )

  @overload(QQStyleKitControl)
  @overload(NoneType)
  def set_scrollIndicator(
      self,
      control: Optional[QQStyleKitControl],
  ) -> None:
    """
    Calls Qt's 'void
    QQStyleKitControls::set_scrollIndicator(QQStyleKitControl *control)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#set_scrollIndicator

    Parameters
    ----------

    control : Optional[QQStyleKitControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControls::set_scrollIndicator(QQStyleKitControl
    #      *control)
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls19set_scrollIndicatorEP17QQStyleKitCo'
        'ntrol',
        self._addressOf(control),
    )

  @overload(QQStyleKitControl)
  @overload(NoneType)
  def set_scrollView(self, control: Optional[QQStyleKitControl]) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::set_scrollView(QQStyleKitControl
    *control)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#set_scrollView

    Parameters
    ----------

    control : Optional[QQStyleKitControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControls::set_scrollView(QQStyleKitControl *control)
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls14set_scrollViewEP17QQStyleKitControl',
        self._addressOf(control),
    )

  @overload(QQStyleKitControl)
  @overload(NoneType)
  def set_searchField(self, control: Optional[QQStyleKitControl]) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::set_searchField(QQStyleKitControl
    *control)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#set_searchField

    Parameters
    ----------

    control : Optional[QQStyleKitControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControls::set_searchField(QQStyleKitControl *control)
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls15set_searchFieldEP17QQStyleKitContro'
        'l',
        self._addressOf(control),
    )

  @overload(QQStyleKitControl)
  @overload(NoneType)
  def set_slider(self, control: Optional[QQStyleKitControl]) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::set_slider(QQStyleKitControl
    *control)'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitcontrols.html#set_slider

    Parameters
    ----------

    control : Optional[QQStyleKitControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControls::set_slider(QQStyleKitControl *control)
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls10set_sliderEP17QQStyleKitControl',
        self._addressOf(control),
    )

  @overload(QQStyleKitControl)
  @overload(NoneType)
  def set_spinBox(self, control: Optional[QQStyleKitControl]) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::set_spinBox(QQStyleKitControl
    *control)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#set_spinBox

    Parameters
    ----------

    control : Optional[QQStyleKitControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControls::set_spinBox(QQStyleKitControl *control)
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls11set_spinBoxEP17QQStyleKitControl',
        self._addressOf(control),
    )

  @overload(QQStyleKitControl)
  @overload(NoneType)
  def set_tabBar(self, control: Optional[QQStyleKitControl]) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::set_tabBar(QQStyleKitControl
    *control)'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitcontrols.html#set_tabBar

    Parameters
    ----------

    control : Optional[QQStyleKitControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControls::set_tabBar(QQStyleKitControl *control)
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls10set_tabBarEP17QQStyleKitControl',
        self._addressOf(control),
    )

  @overload(QQStyleKitControl)
  @overload(NoneType)
  def set_tabButton(self, control: Optional[QQStyleKitControl]) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::set_tabButton(QQStyleKitControl
    *control)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#set_tabButton

    Parameters
    ----------

    control : Optional[QQStyleKitControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControls::set_tabButton(QQStyleKitControl *control)
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls13set_tabButtonEP17QQStyleKitControl',
        self._addressOf(control),
    )

  @overload(QQStyleKitControl)
  @overload(NoneType)
  def set_textField(self, control: Optional[QQStyleKitControl]) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::set_textField(QQStyleKitControl
    *control)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#set_textField

    Parameters
    ----------

    control : Optional[QQStyleKitControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControls::set_textField(QQStyleKitControl *control)
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls13set_textFieldEP17QQStyleKitControl',
        self._addressOf(control),
    )

  @overload(QQStyleKitControl)
  @overload(NoneType)
  def set_textInput(self, control: Optional[QQStyleKitControl]) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::set_textInput(QQStyleKitControl
    *control)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#set_textInput

    Parameters
    ----------

    control : Optional[QQStyleKitControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControls::set_textInput(QQStyleKitControl *control)
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls13set_textInputEP17QQStyleKitControl',
        self._addressOf(control),
    )

  @overload(QQStyleKitControl)
  @overload(NoneType)
  def set_toolBar(self, control: Optional[QQStyleKitControl]) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::set_toolBar(QQStyleKitControl
    *control)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#set_toolBar

    Parameters
    ----------

    control : Optional[QQStyleKitControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControls::set_toolBar(QQStyleKitControl *control)
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls11set_toolBarEP17QQStyleKitControl',
        self._addressOf(control),
    )

  @overload(QQStyleKitControl)
  @overload(NoneType)
  def set_toolButton(self, control: Optional[QQStyleKitControl]) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::set_toolButton(QQStyleKitControl
    *control)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#set_toolButton

    Parameters
    ----------

    control : Optional[QQStyleKitControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControls::set_toolButton(QQStyleKitControl *control)
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls14set_toolButtonEP17QQStyleKitControl',
        self._addressOf(control),
    )

  @overload(QQStyleKitControl)
  @overload(NoneType)
  def set_toolSeparator(self, control: Optional[QQStyleKitControl]) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::set_toolSeparator(QQStyleKitControl
    *control)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#set_toolSeparator

    Parameters
    ----------

    control : Optional[QQStyleKitControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControls::set_toolSeparator(QQStyleKitControl *control)
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls17set_toolSeparatorEP17QQStyleKitCont'
        'rol',
        self._addressOf(control),
    )

  @overload(QQStyleKitControl)
  @overload(NoneType)
  def set_swipeDelegate(self, control: Optional[QQStyleKitControl]) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::set_swipeDelegate(QQStyleKitControl
    *control)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#set_swipeDelegate

    Parameters
    ----------

    control : Optional[QQStyleKitControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControls::set_swipeDelegate(QQStyleKitControl *control)
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls17set_swipeDelegateEP17QQStyleKitCont'
        'rol',
        self._addressOf(control),
    )

  @overload(QQStyleKitControl)
  @overload(NoneType)
  def set_switchControl(self, control: Optional[QQStyleKitControl]) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::set_switchControl(QQStyleKitControl
    *control)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#set_switchControl

    Parameters
    ----------

    control : Optional[QQStyleKitControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControls::set_switchControl(QQStyleKitControl *control)
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls17set_switchControlEP17QQStyleKitCont'
        'rol',
        self._addressOf(control),
    )

  @overload(QQStyleKitControl)
  @overload(NoneType)
  def set_switchDelegate(self, control: Optional[QQStyleKitControl]) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::set_switchDelegate(QQStyleKitControl
    *control)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#set_switchDelegate

    Parameters
    ----------

    control : Optional[QQStyleKitControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControls::set_switchDelegate(QQStyleKitControl
    #      *control)
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls18set_switchDelegateEP17QQStyleKitCon'
        'trol',
        self._addressOf(control),
    )

  @overload(QQStyleKitControl)
  @overload(NoneType)
  def set_radioButton(self, control: Optional[QQStyleKitControl]) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::set_radioButton(QQStyleKitControl
    *control)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#set_radioButton

    Parameters
    ----------

    control : Optional[QQStyleKitControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControls::set_radioButton(QQStyleKitControl *control)
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls15set_radioButtonEP17QQStyleKitContro'
        'l',
        self._addressOf(control),
    )

  @overload(QQStyleKitControl)
  @overload(NoneType)
  def set_radioDelegate(self, control: Optional[QQStyleKitControl]) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::set_radioDelegate(QQStyleKitControl
    *control)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#set_radioDelegate

    Parameters
    ----------

    control : Optional[QQStyleKitControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControls::set_radioDelegate(QQStyleKitControl *control)
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls17set_radioDelegateEP17QQStyleKitCont'
        'rol',
        self._addressOf(control),
    )

  @overload(QQStyleKitControl)
  @overload(NoneType)
  def set_roundButton(self, control: Optional[QQStyleKitControl]) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::set_roundButton(QQStyleKitControl
    *control)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#set_roundButton

    Parameters
    ----------

    control : Optional[QQStyleKitControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControls::set_roundButton(QQStyleKitControl *control)
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls15set_roundButtonEP17QQStyleKitContro'
        'l',
        self._addressOf(control),
    )

  @overload(QQStyleKitControl)
  @overload(NoneType)
  def set_itemDelegate(self, control: Optional[QQStyleKitControl]) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::set_itemDelegate(QQStyleKitControl
    *control)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#set_itemDelegate

    Parameters
    ----------

    control : Optional[QQStyleKitControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControls::set_itemDelegate(QQStyleKitControl *control)
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls16set_itemDelegateEP17QQStyleKitContr'
        'ol',
        self._addressOf(control),
    )

  @overload(QQStyleKitControl)
  @overload(NoneType)
  def set_popup(self, control: Optional[QQStyleKitControl]) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::set_popup(QQStyleKitControl
    *control)'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitcontrols.html#set_popup

    Parameters
    ----------

    control : Optional[QQStyleKitControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControls::set_popup(QQStyleKitControl *control)
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls9set_popupEP17QQStyleKitControl',
        self._addressOf(control),
    )

  @overload(QQStyleKitControl)
  @overload(NoneType)
  def set_pane(self, control: Optional[QQStyleKitControl]) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::set_pane(QQStyleKitControl
    *control)'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitcontrols.html#set_pane

    Parameters
    ----------

    control : Optional[QQStyleKitControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControls::set_pane(QQStyleKitControl *control)
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls8set_paneEP17QQStyleKitControl',
        self._addressOf(control),
    )

  @overload(QQStyleKitControl)
  @overload(NoneType)
  def set_page(self, control: Optional[QQStyleKitControl]) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::set_page(QQStyleKitControl
    *control)'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitcontrols.html#set_page

    Parameters
    ----------

    control : Optional[QQStyleKitControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControls::set_page(QQStyleKitControl *control)
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls8set_pageEP17QQStyleKitControl',
        self._addressOf(control),
    )

  @overload(QQStyleKitControl)
  @overload(NoneType)
  def set_pageIndicator(self, control: Optional[QQStyleKitControl]) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::set_pageIndicator(QQStyleKitControl
    *control)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#set_pageIndicator

    Parameters
    ----------

    control : Optional[QQStyleKitControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControls::set_pageIndicator(QQStyleKitControl *control)
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls17set_pageIndicatorEP17QQStyleKitCont'
        'rol',
        self._addressOf(control),
    )

  @overload(QQStyleKitControl)
  @overload(NoneType)
  def set_frame(self, control: Optional[QQStyleKitControl]) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::set_frame(QQStyleKitControl
    *control)'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitcontrols.html#set_frame

    Parameters
    ----------

    control : Optional[QQStyleKitControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControls::set_frame(QQStyleKitControl *control)
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls9set_frameEP17QQStyleKitControl',
        self._addressOf(control),
    )

  @overload(QQStyleKitControl)
  @overload(NoneType)
  def set_label(self, control: Optional[QQStyleKitControl]) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::set_label(QQStyleKitControl
    *control)'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitcontrols.html#set_label

    Parameters
    ----------

    control : Optional[QQStyleKitControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControls::set_label(QQStyleKitControl *control)
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls9set_labelEP17QQStyleKitControl',
        self._addressOf(control),
    )

  @overload(QQStyleKitControl)
  @overload(NoneType)
  def set_groupBox(self, control: Optional[QQStyleKitControl]) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::set_groupBox(QQStyleKitControl
    *control)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#set_groupBox

    Parameters
    ----------

    control : Optional[QQStyleKitControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControls::set_groupBox(QQStyleKitControl *control)
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls12set_groupBoxEP17QQStyleKitControl',
        self._addressOf(control),
    )

  @overload(QQStyleKitControl)
  @overload(NoneType)
  def set_textArea(self, control: Optional[QQStyleKitControl]) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::set_textArea(QQStyleKitControl
    *control)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#set_textArea

    Parameters
    ----------

    control : Optional[QQStyleKitControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControls::set_textArea(QQStyleKitControl *control)
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls12set_textAreaEP17QQStyleKitControl',
        self._addressOf(control),
    )

  @overload(QQStyleKitControl)
  @overload(NoneType)
  def set_menu(self, control: Optional[QQStyleKitControl]) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::set_menu(QQStyleKitControl
    *control)'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitcontrols.html#set_menu

    Parameters
    ----------

    control : Optional[QQStyleKitControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControls::set_menu(QQStyleKitControl *control)
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls8set_menuEP17QQStyleKitControl',
        self._addressOf(control),
    )

  @overload(QQStyleKitControl)
  @overload(NoneType)
  def set_menuBar(self, control: Optional[QQStyleKitControl]) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::set_menuBar(QQStyleKitControl
    *control)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#set_menuBar

    Parameters
    ----------

    control : Optional[QQStyleKitControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControls::set_menuBar(QQStyleKitControl *control)
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls11set_menuBarEP17QQStyleKitControl',
        self._addressOf(control),
    )

  @overload(QQStyleKitControl)
  @overload(NoneType)
  def set_menuBarItem(self, control: Optional[QQStyleKitControl]) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::set_menuBarItem(QQStyleKitControl
    *control)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#set_menuBarItem

    Parameters
    ----------

    control : Optional[QQStyleKitControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControls::set_menuBarItem(QQStyleKitControl *control)
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls15set_menuBarItemEP17QQStyleKitContro'
        'l',
        self._addressOf(control),
    )

  @overload(QQStyleKitControl)
  @overload(NoneType)
  def set_menuItem(self, control: Optional[QQStyleKitControl]) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::set_menuItem(QQStyleKitControl
    *control)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#set_menuItem

    Parameters
    ----------

    control : Optional[QQStyleKitControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControls::set_menuItem(QQStyleKitControl *control)
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls12set_menuItemEP17QQStyleKitControl',
        self._addressOf(control),
    )

  @overload(QQStyleKitControl)
  @overload(NoneType)
  def set_menuSeparator(self, control: Optional[QQStyleKitControl]) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::set_menuSeparator(QQStyleKitControl
    *control)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#set_menuSeparator

    Parameters
    ----------

    control : Optional[QQStyleKitControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControls::set_menuSeparator(QQStyleKitControl *control)
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls17set_menuSeparatorEP17QQStyleKitCont'
        'rol',
        self._addressOf(control),
    )

  def dataChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::dataChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#dataChanged
    """
    #  void QQStyleKitControls::dataChanged()
    self.uglySide.call('ritual_ZN18QQStyleKitControls11dataChangedEv')

  def applicationWindowChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::applicationWindowChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#applicationWindowChanged
    """
    #  void QQStyleKitControls::applicationWindowChanged()
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls24applicationWindowChangedEv',
    )

  def abstractButtonChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::abstractButtonChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#abstractButtonChanged
    """
    #  void QQStyleKitControls::abstractButtonChanged()
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls21abstractButtonChangedEv',
    )

  def controlChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::controlChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#controlChanged
    """
    #  void QQStyleKitControls::controlChanged()
    self.uglySide.call('ritual_ZN18QQStyleKitControls14controlChangedEv')

  def busyIndicatorChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::busyIndicatorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#busyIndicatorChanged
    """
    #  void QQStyleKitControls::busyIndicatorChanged()
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls20busyIndicatorChangedEv',
    )

  def buttonChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::buttonChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#buttonChanged
    """
    #  void QQStyleKitControls::buttonChanged()
    self.uglySide.call('ritual_ZN18QQStyleKitControls13buttonChangedEv')

  def checkBoxChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::checkBoxChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#checkBoxChanged
    """
    #  void QQStyleKitControls::checkBoxChanged()
    self.uglySide.call('ritual_ZN18QQStyleKitControls15checkBoxChangedEv')

  def checkDelegateChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::checkDelegateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#checkDelegateChanged
    """
    #  void QQStyleKitControls::checkDelegateChanged()
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls20checkDelegateChangedEv',
    )

  def comboBoxChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::comboBoxChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#comboBoxChanged
    """
    #  void QQStyleKitControls::comboBoxChanged()
    self.uglySide.call('ritual_ZN18QQStyleKitControls15comboBoxChangedEv')

  def delayButtonChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::delayButtonChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#delayButtonChanged
    """
    #  void QQStyleKitControls::delayButtonChanged()
    self.uglySide.call('ritual_ZN18QQStyleKitControls18delayButtonChangedEv')

  def dialChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::dialChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#dialChanged
    """
    #  void QQStyleKitControls::dialChanged()
    self.uglySide.call('ritual_ZN18QQStyleKitControls11dialChangedEv')

  def dialogChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::dialogChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#dialogChanged
    """
    #  void QQStyleKitControls::dialogChanged()
    self.uglySide.call('ritual_ZN18QQStyleKitControls13dialogChangedEv')

  def dialogButtonBoxChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::dialogButtonBoxChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#dialogButtonBoxChanged
    """
    #  void QQStyleKitControls::dialogButtonBoxChanged()
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls22dialogButtonBoxChangedEv',
    )

  def flatButtonChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::flatButtonChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#flatButtonChanged
    """
    #  void QQStyleKitControls::flatButtonChanged()
    self.uglySide.call('ritual_ZN18QQStyleKitControls17flatButtonChangedEv')

  def progressBarChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::progressBarChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#progressBarChanged
    """
    #  void QQStyleKitControls::progressBarChanged()
    self.uglySide.call('ritual_ZN18QQStyleKitControls18progressBarChangedEv')

  def scrollBarChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::scrollBarChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#scrollBarChanged
    """
    #  void QQStyleKitControls::scrollBarChanged()
    self.uglySide.call('ritual_ZN18QQStyleKitControls16scrollBarChangedEv')

  def scrollIndicatorChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::scrollIndicatorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#scrollIndicatorChanged
    """
    #  void QQStyleKitControls::scrollIndicatorChanged()
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls22scrollIndicatorChangedEv',
    )

  def scrollViewChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::scrollViewChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#scrollViewChanged
    """
    #  void QQStyleKitControls::scrollViewChanged()
    self.uglySide.call('ritual_ZN18QQStyleKitControls17scrollViewChangedEv')

  def searchFieldChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::searchFieldChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#searchFieldChanged
    """
    #  void QQStyleKitControls::searchFieldChanged()
    self.uglySide.call('ritual_ZN18QQStyleKitControls18searchFieldChangedEv')

  def sliderChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::sliderChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#sliderChanged
    """
    #  void QQStyleKitControls::sliderChanged()
    self.uglySide.call('ritual_ZN18QQStyleKitControls13sliderChangedEv')

  def spinBoxChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::spinBoxChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#spinBoxChanged
    """
    #  void QQStyleKitControls::spinBoxChanged()
    self.uglySide.call('ritual_ZN18QQStyleKitControls14spinBoxChangedEv')

  def tabBarChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::tabBarChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#tabBarChanged
    """
    #  void QQStyleKitControls::tabBarChanged()
    self.uglySide.call('ritual_ZN18QQStyleKitControls13tabBarChangedEv')

  def tabButtonChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::tabButtonChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#tabButtonChanged
    """
    #  void QQStyleKitControls::tabButtonChanged()
    self.uglySide.call('ritual_ZN18QQStyleKitControls16tabButtonChangedEv')

  def textFieldChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::textFieldChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#textFieldChanged
    """
    #  void QQStyleKitControls::textFieldChanged()
    self.uglySide.call('ritual_ZN18QQStyleKitControls16textFieldChangedEv')

  def textInputChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::textInputChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#textInputChanged
    """
    #  void QQStyleKitControls::textInputChanged()
    self.uglySide.call('ritual_ZN18QQStyleKitControls16textInputChangedEv')

  def toolBarChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::toolBarChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#toolBarChanged
    """
    #  void QQStyleKitControls::toolBarChanged()
    self.uglySide.call('ritual_ZN18QQStyleKitControls14toolBarChangedEv')

  def toolButtonChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::toolButtonChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#toolButtonChanged
    """
    #  void QQStyleKitControls::toolButtonChanged()
    self.uglySide.call('ritual_ZN18QQStyleKitControls17toolButtonChangedEv')

  def toolSeparatorChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::toolSeparatorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#toolSeparatorChanged
    """
    #  void QQStyleKitControls::toolSeparatorChanged()
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls20toolSeparatorChangedEv',
    )

  def swipeDelegateChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::swipeDelegateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#swipeDelegateChanged
    """
    #  void QQStyleKitControls::swipeDelegateChanged()
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls20swipeDelegateChangedEv',
    )

  def switchControlChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::switchControlChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#switchControlChanged
    """
    #  void QQStyleKitControls::switchControlChanged()
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls20switchControlChangedEv',
    )

  def switchDelegateChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::switchDelegateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#switchDelegateChanged
    """
    #  void QQStyleKitControls::switchDelegateChanged()
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls21switchDelegateChangedEv',
    )

  def radioButtonChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::radioButtonChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#radioButtonChanged
    """
    #  void QQStyleKitControls::radioButtonChanged()
    self.uglySide.call('ritual_ZN18QQStyleKitControls18radioButtonChangedEv')

  def radioDelegateChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::radioDelegateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#radioDelegateChanged
    """
    #  void QQStyleKitControls::radioDelegateChanged()
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls20radioDelegateChangedEv',
    )

  def roundButtonChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::roundButtonChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#roundButtonChanged
    """
    #  void QQStyleKitControls::roundButtonChanged()
    self.uglySide.call('ritual_ZN18QQStyleKitControls18roundButtonChangedEv')

  def itemDelegateChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::itemDelegateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#itemDelegateChanged
    """
    #  void QQStyleKitControls::itemDelegateChanged()
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls19itemDelegateChangedEv',
    )

  def popupChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::popupChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#popupChanged
    """
    #  void QQStyleKitControls::popupChanged()
    self.uglySide.call('ritual_ZN18QQStyleKitControls12popupChangedEv')

  def paneChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::paneChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#paneChanged
    """
    #  void QQStyleKitControls::paneChanged()
    self.uglySide.call('ritual_ZN18QQStyleKitControls11paneChangedEv')

  def pageChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::pageChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#pageChanged
    """
    #  void QQStyleKitControls::pageChanged()
    self.uglySide.call('ritual_ZN18QQStyleKitControls11pageChangedEv')

  def pageIndicatorChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::pageIndicatorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#pageIndicatorChanged
    """
    #  void QQStyleKitControls::pageIndicatorChanged()
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls20pageIndicatorChangedEv',
    )

  def frameChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::frameChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#frameChanged
    """
    #  void QQStyleKitControls::frameChanged()
    self.uglySide.call('ritual_ZN18QQStyleKitControls12frameChangedEv')

  def labelChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::labelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#labelChanged
    """
    #  void QQStyleKitControls::labelChanged()
    self.uglySide.call('ritual_ZN18QQStyleKitControls12labelChangedEv')

  def groupBoxChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::groupBoxChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#groupBoxChanged
    """
    #  void QQStyleKitControls::groupBoxChanged()
    self.uglySide.call('ritual_ZN18QQStyleKitControls15groupBoxChangedEv')

  def textAreaChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::textAreaChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#textAreaChanged
    """
    #  void QQStyleKitControls::textAreaChanged()
    self.uglySide.call('ritual_ZN18QQStyleKitControls15textAreaChangedEv')

  def menuChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::menuChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#menuChanged
    """
    #  void QQStyleKitControls::menuChanged()
    self.uglySide.call('ritual_ZN18QQStyleKitControls11menuChangedEv')

  def menuBarChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::menuBarChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#menuBarChanged
    """
    #  void QQStyleKitControls::menuBarChanged()
    self.uglySide.call('ritual_ZN18QQStyleKitControls14menuBarChangedEv')

  def menuBarItemChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::menuBarItemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#menuBarItemChanged
    """
    #  void QQStyleKitControls::menuBarItemChanged()
    self.uglySide.call('ritual_ZN18QQStyleKitControls18menuBarItemChangedEv')

  def menuItemChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::menuItemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#menuItemChanged
    """
    #  void QQStyleKitControls::menuItemChanged()
    self.uglySide.call('ritual_ZN18QQStyleKitControls15menuItemChangedEv')

  def menuSeparatorChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::menuSeparatorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#menuSeparatorChanged
    """
    #  void QQStyleKitControls::menuSeparatorChanged()
    self.uglySide.call(
        'ritual_ZN18QQStyleKitControls20menuSeparatorChangedEv',
    )

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::classBegin()'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitcontrols.html#classBegin
    """
    #  void QQStyleKitControls::classBegin()
    ritual = 'ritual_ZN18QQStyleKitControls10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQStyleKitControls10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControls::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrols.html#componentComplete
    """
    #  void QQStyleKitControls::componentComplete()
    self.uglySide.call('ritual_ZN18QQStyleKitControls17componentCompleteEv')

  @staticmethod
  def abstractButton(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControls::abstractButton() const':
    leans on 'QQStyleKitControls::abstractButton() const', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.abstractButton' has no cute function yet. Qt's "
        "'QQStyleKitControl *QQStyleKitControls::abstractButton() const': "
        "leans on 'QQStyleKitControls::abstractButton() const', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def applicationWindow(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControls::applicationWindow() const':
    leans on 'QQStyleKitControls::applicationWindow() const', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.applicationWindow' has no cute function yet. "
        "Qt's 'QQStyleKitControl *QQStyleKitControls::applicationWindow() "
        "const': leans on 'QQStyleKitControls::applicationWindow() const', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def busyIndicator(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControls::busyIndicator() const':
    leans on 'QQStyleKitControls::busyIndicator() const', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.busyIndicator' has no cute function yet. Qt's "
        "'QQStyleKitControl *QQStyleKitControls::busyIndicator() const': "
        "leans on 'QQStyleKitControls::busyIndicator() const', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def button(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControls::button() const': leans on
    'QQStyleKitControls::button() const', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.button' has no cute function yet. Qt's "
        "'QQStyleKitControl *QQStyleKitControls::button() const': leans on "
        "'QQStyleKitControls::button() const', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def checkBox(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControls::checkBox() const': leans on
    'QQStyleKitControls::checkBox() const', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.checkBox' has no cute function yet. Qt's "
        "'QQStyleKitControl *QQStyleKitControls::checkBox() const': leans "
        "on 'QQStyleKitControls::checkBox() const', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def checkDelegate(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControls::checkDelegate() const':
    leans on 'QQStyleKitControls::checkDelegate() const', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.checkDelegate' has no cute function yet. Qt's "
        "'QQStyleKitControl *QQStyleKitControls::checkDelegate() const': "
        "leans on 'QQStyleKitControls::checkDelegate() const', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def comboBox(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControls::comboBox() const': leans on
    'QQStyleKitControls::comboBox() const', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.comboBox' has no cute function yet. Qt's "
        "'QQStyleKitControl *QQStyleKitControls::comboBox() const': leans "
        "on 'QQStyleKitControls::comboBox() const', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def control(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControls::control() const': leans on
    'QQStyleKitControls::control() const', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.control' has no cute function yet. Qt's "
        "'QQStyleKitControl *QQStyleKitControls::control() const': leans on "
        "'QQStyleKitControls::control() const', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def data(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject> QQStyleKitControls::data()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.data' has no cute function yet. Qt's "
        "'QQmlListProperty<QObject> QQStyleKitControls::data()': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def delayButton(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControls::delayButton() const': leans
    on 'QQStyleKitControls::delayButton() const', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.delayButton' has no cute function yet. Qt's "
        "'QQStyleKitControl *QQStyleKitControls::delayButton() const': "
        "leans on 'QQStyleKitControls::delayButton() const', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def dial(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControls::dial() const': leans on
    'QQStyleKitControls::dial() const', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.dial' has no cute function yet. Qt's "
        "'QQStyleKitControl *QQStyleKitControls::dial() const': leans on "
        "'QQStyleKitControls::dial() const', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def dialog(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControls::dialog() const': leans on
    'QQStyleKitControls::dialog() const', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.dialog' has no cute function yet. Qt's "
        "'QQStyleKitControl *QQStyleKitControls::dialog() const': leans on "
        "'QQStyleKitControls::dialog() const', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def dialogButtonBox(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControls::dialogButtonBox() const':
    leans on 'QQStyleKitControls::dialogButtonBox() const', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.dialogButtonBox' has no cute function yet. "
        "Qt's 'QQStyleKitControl *QQStyleKitControls::dialogButtonBox() "
        "const': leans on 'QQStyleKitControls::dialogButtonBox() const', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def flatButton(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControls::flatButton() const': leans
    on 'QQStyleKitControls::flatButton() const', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.flatButton' has no cute function yet. Qt's "
        "'QQStyleKitControl *QQStyleKitControls::flatButton() const': leans "
        "on 'QQStyleKitControls::flatButton() const', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def frame(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControls::frame() const': leans on
    'QQStyleKitControls::frame() const', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.frame' has no cute function yet. Qt's "
        "'QQStyleKitControl *QQStyleKitControls::frame() const': leans on "
        "'QQStyleKitControls::frame() const', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def groupBox(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControls::groupBox() const': leans on
    'QQStyleKitControls::groupBox() const', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.groupBox' has no cute function yet. Qt's "
        "'QQStyleKitControl *QQStyleKitControls::groupBox() const': leans "
        "on 'QQStyleKitControls::groupBox() const', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def itemDelegate(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControls::itemDelegate() const': leans
    on 'QQStyleKitControls::itemDelegate() const', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.itemDelegate' has no cute function yet. Qt's "
        "'QQStyleKitControl *QQStyleKitControls::itemDelegate() const': "
        "leans on 'QQStyleKitControls::itemDelegate() const', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def label(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControls::label() const': leans on
    'QQStyleKitControls::label() const', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.label' has no cute function yet. Qt's "
        "'QQStyleKitControl *QQStyleKitControls::label() const': leans on "
        "'QQStyleKitControls::label() const', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def menu(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControls::menu() const': leans on
    'QQStyleKitControls::menu() const', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.menu' has no cute function yet. Qt's "
        "'QQStyleKitControl *QQStyleKitControls::menu() const': leans on "
        "'QQStyleKitControls::menu() const', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def menuBar(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControls::menuBar() const': leans on
    'QQStyleKitControls::menuBar() const', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.menuBar' has no cute function yet. Qt's "
        "'QQStyleKitControl *QQStyleKitControls::menuBar() const': leans on "
        "'QQStyleKitControls::menuBar() const', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def menuBarItem(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControls::menuBarItem() const': leans
    on 'QQStyleKitControls::menuBarItem() const', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.menuBarItem' has no cute function yet. Qt's "
        "'QQStyleKitControl *QQStyleKitControls::menuBarItem() const': "
        "leans on 'QQStyleKitControls::menuBarItem() const', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def menuItem(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControls::menuItem() const': leans on
    'QQStyleKitControls::menuItem() const', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.menuItem' has no cute function yet. Qt's "
        "'QQStyleKitControl *QQStyleKitControls::menuItem() const': leans "
        "on 'QQStyleKitControls::menuItem() const', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def menuSeparator(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControls::menuSeparator() const':
    leans on 'QQStyleKitControls::menuSeparator() const', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.menuSeparator' has no cute function yet. Qt's "
        "'QQStyleKitControl *QQStyleKitControls::menuSeparator() const': "
        "leans on 'QQStyleKitControls::menuSeparator() const', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def page(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControls::page() const': leans on
    'QQStyleKitControls::page() const', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.page' has no cute function yet. Qt's "
        "'QQStyleKitControl *QQStyleKitControls::page() const': leans on "
        "'QQStyleKitControls::page() const', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def pageIndicator(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControls::pageIndicator() const':
    leans on 'QQStyleKitControls::pageIndicator() const', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.pageIndicator' has no cute function yet. Qt's "
        "'QQStyleKitControl *QQStyleKitControls::pageIndicator() const': "
        "leans on 'QQStyleKitControls::pageIndicator() const', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def pane(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControls::pane() const': leans on
    'QQStyleKitControls::pane() const', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.pane' has no cute function yet. Qt's "
        "'QQStyleKitControl *QQStyleKitControls::pane() const': leans on "
        "'QQStyleKitControls::pane() const', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def popup(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControls::popup() const': leans on
    'QQStyleKitControls::popup() const', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.popup' has no cute function yet. Qt's "
        "'QQStyleKitControl *QQStyleKitControls::popup() const': leans on "
        "'QQStyleKitControls::popup() const', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def progressBar(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControls::progressBar() const': leans
    on 'QQStyleKitControls::progressBar() const', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.progressBar' has no cute function yet. Qt's "
        "'QQStyleKitControl *QQStyleKitControls::progressBar() const': "
        "leans on 'QQStyleKitControls::progressBar() const', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def radioButton(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControls::radioButton() const': leans
    on 'QQStyleKitControls::radioButton() const', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.radioButton' has no cute function yet. Qt's "
        "'QQStyleKitControl *QQStyleKitControls::radioButton() const': "
        "leans on 'QQStyleKitControls::radioButton() const', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def radioDelegate(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControls::radioDelegate() const':
    leans on 'QQStyleKitControls::radioDelegate() const', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.radioDelegate' has no cute function yet. Qt's "
        "'QQStyleKitControl *QQStyleKitControls::radioDelegate() const': "
        "leans on 'QQStyleKitControls::radioDelegate() const', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def roundButton(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControls::roundButton() const': leans
    on 'QQStyleKitControls::roundButton() const', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.roundButton' has no cute function yet. Qt's "
        "'QQStyleKitControl *QQStyleKitControls::roundButton() const': "
        "leans on 'QQStyleKitControls::roundButton() const', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def scrollBar(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControls::scrollBar() const': leans on
    'QQStyleKitControls::scrollBar() const', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.scrollBar' has no cute function yet. Qt's "
        "'QQStyleKitControl *QQStyleKitControls::scrollBar() const': leans "
        "on 'QQStyleKitControls::scrollBar() const', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def scrollIndicator(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControls::scrollIndicator() const':
    leans on 'QQStyleKitControls::scrollIndicator() const', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.scrollIndicator' has no cute function yet. "
        "Qt's 'QQStyleKitControl *QQStyleKitControls::scrollIndicator() "
        "const': leans on 'QQStyleKitControls::scrollIndicator() const', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def scrollView(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControls::scrollView() const': leans
    on 'QQStyleKitControls::scrollView() const', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.scrollView' has no cute function yet. Qt's "
        "'QQStyleKitControl *QQStyleKitControls::scrollView() const': leans "
        "on 'QQStyleKitControls::scrollView() const', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def searchField(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControls::searchField() const': leans
    on 'QQStyleKitControls::searchField() const', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.searchField' has no cute function yet. Qt's "
        "'QQStyleKitControl *QQStyleKitControls::searchField() const': "
        "leans on 'QQStyleKitControls::searchField() const', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def slider(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControls::slider() const': leans on
    'QQStyleKitControls::slider() const', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.slider' has no cute function yet. Qt's "
        "'QQStyleKitControl *QQStyleKitControls::slider() const': leans on "
        "'QQStyleKitControls::slider() const', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def spinBox(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControls::spinBox() const': leans on
    'QQStyleKitControls::spinBox() const', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.spinBox' has no cute function yet. Qt's "
        "'QQStyleKitControl *QQStyleKitControls::spinBox() const': leans on "
        "'QQStyleKitControls::spinBox() const', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def swipeDelegate(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControls::swipeDelegate() const':
    leans on 'QQStyleKitControls::swipeDelegate() const', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.swipeDelegate' has no cute function yet. Qt's "
        "'QQStyleKitControl *QQStyleKitControls::swipeDelegate() const': "
        "leans on 'QQStyleKitControls::swipeDelegate() const', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def switchControl(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControls::switchControl() const':
    leans on 'QQStyleKitControls::switchControl() const', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.switchControl' has no cute function yet. Qt's "
        "'QQStyleKitControl *QQStyleKitControls::switchControl() const': "
        "leans on 'QQStyleKitControls::switchControl() const', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def switchDelegate(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControls::switchDelegate() const':
    leans on 'QQStyleKitControls::switchDelegate() const', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.switchDelegate' has no cute function yet. Qt's "
        "'QQStyleKitControl *QQStyleKitControls::switchDelegate() const': "
        "leans on 'QQStyleKitControls::switchDelegate() const', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def tabBar(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControls::tabBar() const': leans on
    'QQStyleKitControls::tabBar() const', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.tabBar' has no cute function yet. Qt's "
        "'QQStyleKitControl *QQStyleKitControls::tabBar() const': leans on "
        "'QQStyleKitControls::tabBar() const', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def tabButton(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControls::tabButton() const': leans on
    'QQStyleKitControls::tabButton() const', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.tabButton' has no cute function yet. Qt's "
        "'QQStyleKitControl *QQStyleKitControls::tabButton() const': leans "
        "on 'QQStyleKitControls::tabButton() const', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def textArea(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControls::textArea() const': leans on
    'QQStyleKitControls::textArea() const', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.textArea' has no cute function yet. Qt's "
        "'QQStyleKitControl *QQStyleKitControls::textArea() const': leans "
        "on 'QQStyleKitControls::textArea() const', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def textField(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControls::textField() const': leans on
    'QQStyleKitControls::textField() const', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.textField' has no cute function yet. Qt's "
        "'QQStyleKitControl *QQStyleKitControls::textField() const': leans "
        "on 'QQStyleKitControls::textField() const', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def textInput(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControls::textInput() const': leans on
    'QQStyleKitControls::textInput() const', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.textInput' has no cute function yet. Qt's "
        "'QQStyleKitControl *QQStyleKitControls::textInput() const': leans "
        "on 'QQStyleKitControls::textInput() const', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def toolBar(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControls::toolBar() const': leans on
    'QQStyleKitControls::toolBar() const', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.toolBar' has no cute function yet. Qt's "
        "'QQStyleKitControl *QQStyleKitControls::toolBar() const': leans on "
        "'QQStyleKitControls::toolBar() const', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def toolButton(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControls::toolButton() const': leans
    on 'QQStyleKitControls::toolButton() const', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.toolButton' has no cute function yet. Qt's "
        "'QQStyleKitControl *QQStyleKitControls::toolButton() const': leans "
        "on 'QQStyleKitControls::toolButton() const', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def toolSeparator(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControl *QQStyleKitControls::toolSeparator() const':
    leans on 'QQStyleKitControls::toolSeparator() const', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControls.toolSeparator' has no cute function yet. Qt's "
        "'QQStyleKitControl *QQStyleKitControls::toolSeparator() const': "
        "leans on 'QQStyleKitControls::toolSeparator() const', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
