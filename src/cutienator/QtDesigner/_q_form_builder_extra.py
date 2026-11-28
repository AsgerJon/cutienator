"""
QFormBuilderExtra binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/formbuilderextra_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QFormBuilderExtra to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from ..QtGui import QPalette

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QIODevice, QObject, QVariant
  from ..QtGui import QBrush
  from ..QtWidgets import QBoxLayout, QGridLayout, QLabel, QWidget
  from . import DomBrush, DomButtonGroups, DomColorGroup, DomCustomWidget
  from . import DomPalette, DomProperty, DomUI, QResourceBuilder
  from . import QTextBuilder
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  DomBrush = WAIT['DomBrush']
  DomButtonGroups = WAIT['DomButtonGroups']
  DomColorGroup = WAIT['DomColorGroup']
  DomCustomWidget = WAIT['DomCustomWidget']
  DomPalette = WAIT['DomPalette']
  DomProperty = WAIT['DomProperty']
  QBoxLayout = WAIT['QBoxLayout']
  QBrush = WAIT['QBrush']
  QGridLayout = WAIT['QGridLayout']
  QIODevice = WAIT['QIODevice']
  QLabel = WAIT['QLabel']
  QObject = WAIT['QObject']
  QResourceBuilder = WAIT['QResourceBuilder']
  QTextBuilder = WAIT['QTextBuilder']
  QVariant = WAIT['QVariant']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFormBuilderExtra(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QFormBuilderExtra: a plain Python object standing in
  front of one C++ QFormBuilderExtra.

  What exists
  -----------

  Every function of Qt's QFormBuilderExtra that has a ritual and that Python
  can call so far, 43 names in all: 'clear', 'readUi', 'msgInvalidUiFile',
  'applyPropertyInternally', 'applyInternalProperties', 'applyBuddy',
  'parentWidgetIsSet', 'setProcessingLayoutWidget', 'processingLayoutWidget',
  'setResourceBuilder', 'resourceBuilder', 'setTextBuilder', 'textBuilder',
  'storeCustomWidgetData', 'customWidgetAddPageMethod',
  'customWidgetBaseClass', 'isCustomWidgetContainer', 'registerButtonGroups',
  'boxLayoutStretch', 'setBoxLayoutStretch', 'clearBoxLayoutStretch',
  'gridLayoutRowStretch', 'setGridLayoutRowStretch',
  'clearGridLayoutRowStretch', 'gridLayoutColumnStretch',
  'setGridLayoutColumnStretch', 'clearGridLayoutColumnStretch',
  'gridLayoutRowMinimumHeight', 'setGridLayoutRowMinimumHeight',
  'clearGridLayoutRowMinimumHeight', 'gridLayoutColumnMinimumWidth',
  'setGridLayoutColumnMinimumWidth', 'clearGridLayoutColumnMinimumWidth',
  'loadPalette', 'setupColorGroup', 'saveColorGroup', 'savePalette',
  'setupBrush', 'saveBrush', 'propertyByName', 'isQFontComboBox',
  'clearResourceBuilder', 'clearTextBuilder'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFormBuilderExtra::~QFormBuilderExtra()': the destructor: Python
    never removes a C++ QFormBuilderExtra.
  - Qt's 'const QPointer<QWidget> &QFormBuilderExtra::parentWidget() const':
    gives a type Python has no way to take yet.
  - Qt's 'void QFormBuilderExtra::setParentWidget(const QPointer<QWidget>
    &w)': takes a type Python has no way to hand over yet.
  - Qt's 'const ButtonGroupHash &QFormBuilderExtra::buttonGroups() const':
    gives a type Python has no way to take yet.
  - Qt's 'ButtonGroupHash &QFormBuilderExtra::buttonGroups()': gives a type
    Python has no way to take yet.
  - Qt's 'void QFormBuilderExtra::getLayoutMargins(const QList<DomProperty *>
    &properties, int *left, int *top, int *right, int *bottom)': takes a
    number to change where it is.
  - Qt's 'void QFormBuilderExtra::setPixmapProperty(DomProperty *p, const
    std::pair<QString, QString> &ip)': takes a type Python has no way to hand
    over yet.

  What has no ritual
  ------------------

  4 of the 55 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QFormBuilderExtra is created at the first use, not by
    'QFormBuilderExtra(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QFormBuilderExtra.
  - Each name of Qt's QFormBuilderExtra that has no cute function yet,
    'buttonGroups', 'getLayoutMargins', 'parentWidget', 'setParentWidget',
    'setPixmapProperty', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QFormBuilderExtra, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class BuddyMode(CuteNum):
    """
    The enum 'QFormBuilderExtra::BuddyMode' of Qt, with the 2 names Qt gives
    in it.
    """

    BuddyApplyAll = Kee[int](0)
    BuddyApplyVisibleOnly = Kee[int](1)

  #  The classes Qt writes inside QFormBuilderExtra, each a class in here as
  #  in C++.

  class CustomWidgetData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QFormBuilderExtra::CustomWidgetData: a plain Python
    object standing in front of one C++ QFormBuilderExtra::CustomWidgetData.

    C++ hands a QFormBuilderExtra::CustomWidgetData around as a copy, so
    every C++ QFormBuilderExtra::CustomWidgetData behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QFormBuilderExtra::CustomWidgetData yet. It can be
    made from Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QFormBuilderExtra::CustomWidgetData::~CustomWidgetData()': the
      destructor: Python removes its C++ QFormBuilderExtra::CustomWidgetData
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QFormBuilderExtra::CustomWidgetData is created at the first
      use, not by 'QFormBuilderExtra::CustomWidgetData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QFormBuilderExtra::CustomWidgetData back gives a
      copy the ritual made for Python, in a new cute
      QFormBuilderExtra::CustomWidgetData.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      DomCustomWidget = WAIT['DomCustomWidget']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QFormBuilderExtra::CustomWidgetData'

    #  Qt's '~QFormBuilderExtra::CustomWidgetData()'. Naming it makes this a
    #  value class: Python owns every C++ QFormBuilderExtra::CustomWidgetData
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN17QFormBuilderExtra16CustomWidgetDataD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QFormBuilderExtra::CustomWidgetData::CustomWidgetData()', which is
      called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qformbuilderextra-customwidgetdata.html
      """
      #  QFormBuilderExtra::CustomWidgetData::CustomWidgetData()
      self._noteCreation(
          QFormBuilderExtra.CustomWidgetData, lambda: Rituals.call(
              'ritual_ZN17QFormBuilderExtra16CustomWidgetDataC1Ev',
          ))

    @overload(DomCustomWidget)
    @overload(NoneType)
    def __init__(self, dc: Optional[DomCustomWidget]) -> None:
      """
      Notes what was given, for Qt's
      'QFormBuilderExtra::CustomWidgetData::CustomWidgetData(const
      DomCustomWidget *dc)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qformbuilderextra-customwidgetdata.html

      Parameters
      ----------

      dc : Optional[DomCustomWidget]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  QFormBuilderExtra::CustomWidgetData::CustomWidgetData(const
      #      DomCustomWidget *dc)
      self._noteCreation(
          QFormBuilderExtra.CustomWidgetData, lambda: Rituals.call(
              'ritual_ZN17QFormBuilderExtra16CustomWidgetDataC1EPK15DomCust'
              'omWidget',
              self._addressOf(dc),
          ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def msgInvalidUiFile() -> str:
    """
    Calls Qt's 'QString QFormBuilderExtra::msgInvalidUiFile()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformbuilderextra.html#msgInvalidUiFile

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFormBuilderExtra::msgInvalidUiFile()
    return Rituals.call('ritual_ZN17QFormBuilderExtra16msgInvalidUiFileEv')

  @staticmethod
  @overload(str, BuddyMode, QLabel)
  @overload(str, BuddyMode, NoneType)
  def applyBuddy(
      buddyName: str,
      applyMode: BuddyMode,
      label: Optional[QLabel],
  ) -> bool:
    """
    Calls Qt's 'bool QFormBuilderExtra::applyBuddy(const QString &buddyName,
    BuddyMode applyMode, QLabel *label)'.

    Qt's own words: https://doc.qt.io/qt-6/qformbuilderextra.html#applyBuddy

    Parameters
    ----------

    buddyName : str
      Passed on as it is: a QString is made of it for the call.

    applyMode : BuddyMode
      Passed on as its number.

    label : Optional[QLabel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QFormBuilderExtra::applyBuddy(const QString &buddyName, BuddyMode
    #      applyMode, QLabel *label)
    return Rituals.call(
        'ritual_ZN17QFormBuilderExtra10applyBuddyERK7QStringNS_9BuddyModeEP'
        '6QLabel',
        buddyName, applyMode.value, CuteMixin._addressOf(label),
    )

  @staticmethod
  @overload(QBoxLayout)
  @overload(NoneType)
  def boxLayoutStretch(a0: Optional[QBoxLayout]) -> str:
    """
    Calls Qt's 'QString QFormBuilderExtra::boxLayoutStretch(const QBoxLayout
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformbuilderextra.html#boxLayoutStretch

    Parameters
    ----------

    a0 : Optional[QBoxLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFormBuilderExtra::boxLayoutStretch(const QBoxLayout *a0)
    return Rituals.call(
        'ritual_ZN17QFormBuilderExtra16boxLayoutStretchEPK10QBoxLayout',
        CuteMixin._addressOf(a0),
    )

  @staticmethod
  @overload(str, QBoxLayout)
  @overload(str, NoneType)
  def setBoxLayoutStretch(a0: str, a1: Optional[QBoxLayout]) -> bool:
    """
    Calls Qt's 'bool QFormBuilderExtra::setBoxLayoutStretch(const QString
    &a0, QBoxLayout *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformbuilderextra.html#setBoxLayoutStretch

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.

    a1 : Optional[QBoxLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QFormBuilderExtra::setBoxLayoutStretch(const QString &a0,
    #      QBoxLayout *a1)
    return Rituals.call(
        'ritual_ZN17QFormBuilderExtra19setBoxLayoutStretchERK7QStringP10QBo'
        'xLayout',
        a0, CuteMixin._addressOf(a1),
    )

  @staticmethod
  @overload(QBoxLayout)
  @overload(NoneType)
  def clearBoxLayoutStretch(a0: Optional[QBoxLayout]) -> None:
    """
    Calls Qt's 'void QFormBuilderExtra::clearBoxLayoutStretch(QBoxLayout
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformbuilderextra.html#clearBoxLayoutStretch

    Parameters
    ----------

    a0 : Optional[QBoxLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFormBuilderExtra::clearBoxLayoutStretch(QBoxLayout *a0)
    Rituals.call(
        'ritual_ZN17QFormBuilderExtra21clearBoxLayoutStretchEP10QBoxLayout',
        CuteMixin._addressOf(a0),
    )

  @staticmethod
  @overload(QGridLayout)
  @overload(NoneType)
  def gridLayoutRowStretch(a0: Optional[QGridLayout]) -> str:
    """
    Calls Qt's 'QString QFormBuilderExtra::gridLayoutRowStretch(const
    QGridLayout *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformbuilderextra.html#gridLayoutRowStretch

    Parameters
    ----------

    a0 : Optional[QGridLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFormBuilderExtra::gridLayoutRowStretch(const QGridLayout *a0)
    return Rituals.call(
        'ritual_ZN17QFormBuilderExtra20gridLayoutRowStretchEPK11QGridLayout',
        CuteMixin._addressOf(a0),
    )

  @staticmethod
  @overload(str, QGridLayout)
  @overload(str, NoneType)
  def setGridLayoutRowStretch(a0: str, a1: Optional[QGridLayout]) -> bool:
    """
    Calls Qt's 'bool QFormBuilderExtra::setGridLayoutRowStretch(const QString
    &a0, QGridLayout *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformbuilderextra.html#setGridLayoutRowStretch

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.

    a1 : Optional[QGridLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QFormBuilderExtra::setGridLayoutRowStretch(const QString &a0,
    #      QGridLayout *a1)
    return Rituals.call(
        'ritual_ZN17QFormBuilderExtra23setGridLayoutRowStretchERK7QStringP1'
        '1QGridLayout',
        a0, CuteMixin._addressOf(a1),
    )

  @staticmethod
  @overload(QGridLayout)
  @overload(NoneType)
  def clearGridLayoutRowStretch(a0: Optional[QGridLayout]) -> None:
    """
    Calls Qt's 'void QFormBuilderExtra::clearGridLayoutRowStretch(QGridLayout
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformbuilderextra.html#clearGridLayoutRowStretch

    Parameters
    ----------

    a0 : Optional[QGridLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFormBuilderExtra::clearGridLayoutRowStretch(QGridLayout *a0)
    Rituals.call(
        'ritual_ZN17QFormBuilderExtra25clearGridLayoutRowStretchEP11QGridLa'
        'yout',
        CuteMixin._addressOf(a0),
    )

  @staticmethod
  @overload(QGridLayout)
  @overload(NoneType)
  def gridLayoutColumnStretch(a0: Optional[QGridLayout]) -> str:
    """
    Calls Qt's 'QString QFormBuilderExtra::gridLayoutColumnStretch(const
    QGridLayout *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformbuilderextra.html#gridLayoutColumnStretch

    Parameters
    ----------

    a0 : Optional[QGridLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFormBuilderExtra::gridLayoutColumnStretch(const QGridLayout
    #      *a0)
    return Rituals.call(
        'ritual_ZN17QFormBuilderExtra23gridLayoutColumnStretchEPK11QGridLay'
        'out',
        CuteMixin._addressOf(a0),
    )

  @staticmethod
  @overload(str, QGridLayout)
  @overload(str, NoneType)
  def setGridLayoutColumnStretch(a0: str, a1: Optional[QGridLayout]) -> bool:
    """
    Calls Qt's 'bool QFormBuilderExtra::setGridLayoutColumnStretch(const
    QString &a0, QGridLayout *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformbuilderextra.html#setGridLayoutColumnStretch

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.

    a1 : Optional[QGridLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QFormBuilderExtra::setGridLayoutColumnStretch(const QString &a0,
    #      QGridLayout *a1)
    return Rituals.call(
        'ritual_ZN17QFormBuilderExtra26setGridLayoutColumnStretchERK7QStrin'
        'gP11QGridLayout',
        a0, CuteMixin._addressOf(a1),
    )

  @staticmethod
  @overload(QGridLayout)
  @overload(NoneType)
  def clearGridLayoutColumnStretch(a0: Optional[QGridLayout]) -> None:
    """
    Calls Qt's 'void
    QFormBuilderExtra::clearGridLayoutColumnStretch(QGridLayout *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformbuilderextra.html

    Parameters
    ----------

    a0 : Optional[QGridLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFormBuilderExtra::clearGridLayoutColumnStretch(QGridLayout *a0)
    Rituals.call(
        'ritual_ZN17QFormBuilderExtra28clearGridLayoutColumnStretchEP11QGri'
        'dLayout',
        CuteMixin._addressOf(a0),
    )

  @staticmethod
  @overload(QGridLayout)
  @overload(NoneType)
  def gridLayoutRowMinimumHeight(a0: Optional[QGridLayout]) -> str:
    """
    Calls Qt's 'QString QFormBuilderExtra::gridLayoutRowMinimumHeight(const
    QGridLayout *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformbuilderextra.html#gridLayoutRowMinimumHeight

    Parameters
    ----------

    a0 : Optional[QGridLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFormBuilderExtra::gridLayoutRowMinimumHeight(const
    #      QGridLayout *a0)
    return Rituals.call(
        'ritual_ZN17QFormBuilderExtra26gridLayoutRowMinimumHeightEPK11QGrid'
        'Layout',
        CuteMixin._addressOf(a0),
    )

  @staticmethod
  @overload(str, QGridLayout)
  @overload(str, NoneType)
  def setGridLayoutRowMinimumHeight(
      a0: str,
      a1: Optional[QGridLayout],
  ) -> bool:
    """
    Calls Qt's 'bool QFormBuilderExtra::setGridLayoutRowMinimumHeight(const
    QString &a0, QGridLayout *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformbuilderextra.html

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.

    a1 : Optional[QGridLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QFormBuilderExtra::setGridLayoutRowMinimumHeight(const QString
    #      &a0, QGridLayout *a1)
    return Rituals.call(
        'ritual_ZN17QFormBuilderExtra29setGridLayoutRowMinimumHeightERK7QSt'
        'ringP11QGridLayout',
        a0, CuteMixin._addressOf(a1),
    )

  @staticmethod
  @overload(QGridLayout)
  @overload(NoneType)
  def clearGridLayoutRowMinimumHeight(a0: Optional[QGridLayout]) -> None:
    """
    Calls Qt's 'void
    QFormBuilderExtra::clearGridLayoutRowMinimumHeight(QGridLayout *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformbuilderextra.html

    Parameters
    ----------

    a0 : Optional[QGridLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFormBuilderExtra::clearGridLayoutRowMinimumHeight(QGridLayout
    #      *a0)
    Rituals.call(
        'ritual_ZN17QFormBuilderExtra31clearGridLayoutRowMinimumHeightEP11Q'
        'GridLayout',
        CuteMixin._addressOf(a0),
    )

  @staticmethod
  @overload(QGridLayout)
  @overload(NoneType)
  def gridLayoutColumnMinimumWidth(a0: Optional[QGridLayout]) -> str:
    """
    Calls Qt's 'QString QFormBuilderExtra::gridLayoutColumnMinimumWidth(const
    QGridLayout *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformbuilderextra.html

    Parameters
    ----------

    a0 : Optional[QGridLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFormBuilderExtra::gridLayoutColumnMinimumWidth(const
    #      QGridLayout *a0)
    return Rituals.call(
        'ritual_ZN17QFormBuilderExtra28gridLayoutColumnMinimumWidthEPK11QGr'
        'idLayout',
        CuteMixin._addressOf(a0),
    )

  @staticmethod
  @overload(str, QGridLayout)
  @overload(str, NoneType)
  def setGridLayoutColumnMinimumWidth(
      a0: str,
      a1: Optional[QGridLayout],
  ) -> bool:
    """
    Calls Qt's 'bool QFormBuilderExtra::setGridLayoutColumnMinimumWidth(const
    QString &a0, QGridLayout *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformbuilderextra.html

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.

    a1 : Optional[QGridLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QFormBuilderExtra::setGridLayoutColumnMinimumWidth(const QString
    #      &a0, QGridLayout *a1)
    return Rituals.call(
        'ritual_ZN17QFormBuilderExtra31setGridLayoutColumnMinimumWidthERK7Q'
        'StringP11QGridLayout',
        a0, CuteMixin._addressOf(a1),
    )

  @staticmethod
  @overload(QGridLayout)
  @overload(NoneType)
  def clearGridLayoutColumnMinimumWidth(a0: Optional[QGridLayout]) -> None:
    """
    Calls Qt's 'void
    QFormBuilderExtra::clearGridLayoutColumnMinimumWidth(QGridLayout *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformbuilderextra.html

    Parameters
    ----------

    a0 : Optional[QGridLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFormBuilderExtra::clearGridLayoutColumnMinimumWidth(QGridLayout
    #      *a0)
    Rituals.call(
        'ritual_ZN17QFormBuilderExtra33clearGridLayoutColumnMinimumWidthEP1'
        '1QGridLayout',
        CuteMixin._addressOf(a0),
    )

  @staticmethod
  @overload(DomPalette)
  @overload(NoneType)
  def loadPalette(dom: Optional[DomPalette]) -> QPalette:
    """
    Calls Qt's 'QPalette QFormBuilderExtra::loadPalette(const DomPalette
    *dom)'.

    Qt's own words: https://doc.qt.io/qt-6/qformbuilderextra.html#loadPalette

    Parameters
    ----------

    dom : Optional[DomPalette]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  QPalette QFormBuilderExtra::loadPalette(const DomPalette *dom)
    address = Rituals.call(
        'ritual_ZN17QFormBuilderExtra11loadPaletteEPK10DomPalette',
        CuteMixin._addressOf(dom),
    )
    return QPalette._cuteOwning(address)

  @staticmethod
  @overload(QPalette, QPalette.ColorGroup, DomColorGroup)
  @overload(QPalette, QPalette.ColorGroup, NoneType)
  @overload(NoneType, QPalette.ColorGroup, DomColorGroup)
  @overload(NoneType, QPalette.ColorGroup, NoneType)
  def setupColorGroup(
      palette: Optional[QPalette],
      colorGroup: QPalette.ColorGroup,
      group: Optional[DomColorGroup],
  ) -> None:
    """
    Calls Qt's 'void QFormBuilderExtra::setupColorGroup(QPalette *palette,
    QPalette::ColorGroup colorGroup, const DomColorGroup *group)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformbuilderextra.html#setupColorGroup

    Parameters
    ----------

    palette : Optional[QPalette]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    colorGroup : QPalette.ColorGroup
      Passed on as its number.

    group : Optional[DomColorGroup]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFormBuilderExtra::setupColorGroup(QPalette *palette,
    #      QPalette::ColorGroup colorGroup, const DomColorGroup *group)
    Rituals.call(
        'ritual_ZN17QFormBuilderExtra15setupColorGroupEP8QPaletteNS0_10Colo'
        'rGroupEPK13DomColorGroup',
        CuteMixin._addressOf(palette), colorGroup.value,
        CuteMixin._addressOf(group),
    )

  @staticmethod
  @overload(QPalette, QPalette.ColorGroup)
  def saveColorGroup(
      palette: QPalette,
      colorGroup: QPalette.ColorGroup,
  ) -> Optional[DomColorGroup]:
    """
    Calls Qt's 'DomColorGroup *QFormBuilderExtra::saveColorGroup(const
    QPalette &palette, QPalette::ColorGroup colorGroup)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformbuilderextra.html#saveColorGroup

    Parameters
    ----------

    palette : QPalette
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own.

    colorGroup : QPalette.ColorGroup
      Passed on as its number.

    Returns
    -------

    Optional[DomColorGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomColorGroup *QFormBuilderExtra::saveColorGroup(const QPalette
    #      &palette, QPalette::ColorGroup colorGroup)
    address = Rituals.call(
        'ritual_ZN17QFormBuilderExtra14saveColorGroupERK8QPaletteNS0_10Colo'
        'rGroupE',
        CuteMixin._valueOf(palette), colorGroup.value,
    )
    from . import DomColorGroup
    return DomColorGroup._cuteAt(address)

  @staticmethod
  @overload(QPalette)
  def savePalette(palette: QPalette) -> Optional[DomPalette]:
    """
    Calls Qt's 'DomPalette *QFormBuilderExtra::savePalette(const QPalette
    &palette)'.

    Qt's own words: https://doc.qt.io/qt-6/qformbuilderextra.html#savePalette

    Parameters
    ----------

    palette : QPalette
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own.

    Returns
    -------

    Optional[DomPalette]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomPalette *QFormBuilderExtra::savePalette(const QPalette &palette)
    address = Rituals.call(
        'ritual_ZN17QFormBuilderExtra11savePaletteERK8QPalette',
        CuteMixin._valueOf(palette),
    )
    from . import DomPalette
    return DomPalette._cuteAt(address)

  @staticmethod
  @overload(DomBrush)
  @overload(NoneType)
  def setupBrush(brush: Optional[DomBrush]) -> QBrush:
    """
    Calls Qt's 'QBrush QFormBuilderExtra::setupBrush(const DomBrush *brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qformbuilderextra.html#setupBrush

    Parameters
    ----------

    brush : Optional[DomBrush]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QFormBuilderExtra::setupBrush(const DomBrush *brush)
    address = Rituals.call(
        'ritual_ZN17QFormBuilderExtra10setupBrushEPK8DomBrush',
        CuteMixin._addressOf(brush),
    )
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  @staticmethod
  @overload(QBrush)
  def saveBrush(br: QBrush) -> Optional[DomBrush]:
    """
    Calls Qt's 'DomBrush *QFormBuilderExtra::saveBrush(const QBrush &br)'.

    Qt's own words: https://doc.qt.io/qt-6/qformbuilderextra.html#saveBrush

    Parameters
    ----------

    br : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.

    Returns
    -------

    Optional[DomBrush]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomBrush *QFormBuilderExtra::saveBrush(const QBrush &br)
    address = Rituals.call(
        'ritual_ZN17QFormBuilderExtra9saveBrushERK6QBrush',
        CuteMixin._valueOf(br),
    )
    from . import DomBrush
    return DomBrush._cuteAt(address)

  @staticmethod
  @overload(QList[DomProperty], str)
  def propertyByName(
      properties: QList[DomProperty],
      needle: str,
  ) -> Optional[DomProperty]:
    """
    Calls Qt's 'DomProperty *QFormBuilderExtra::propertyByName(const
    QList<DomProperty *> &properties, QAnyStringView needle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformbuilderextra.html#propertyByName

    Parameters
    ----------

    properties : QList[DomProperty]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    needle : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[DomProperty]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomProperty *QFormBuilderExtra::propertyByName(const QList<DomProperty
    #      *> &properties, QAnyStringView needle)
    address = Rituals.call(
        'ritual_ZN17QFormBuilderExtra14propertyByNameERK5QListIP11DomProper'
        'tyE14QAnyStringView',
        CuteMixin._valueOf(properties), needle,
    )
    from . import DomProperty
    return DomProperty._cuteAt(address)

  @staticmethod
  @overload(QWidget)
  @overload(NoneType)
  def isQFontComboBox(w: Optional[QWidget]) -> bool:
    """
    Calls Qt's 'bool QFormBuilderExtra::isQFontComboBox(const QWidget *w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformbuilderextra.html#isQFontComboBox

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QFormBuilderExtra::isQFontComboBox(const QWidget *w)
    return Rituals.call(
        'ritual_ZN17QFormBuilderExtra15isQFontComboBoxEPK7QWidget',
        CuteMixin._addressOf(w),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFormBuilderExtra'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def parentWidgetIsSet(self) -> bool:
    """
    Calls Qt's 'bool QFormBuilderExtra::parentWidgetIsSet() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformbuilderextra.html#parentWidgetIsSet
    """
    #  bool QFormBuilderExtra::parentWidgetIsSet() const
    return self.uglySide.call(
        'ritual_ZNK17QFormBuilderExtra17parentWidgetIsSetEv',
    )

  def processingLayoutWidget(self) -> bool:
    """
    Calls Qt's 'bool QFormBuilderExtra::processingLayoutWidget() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformbuilderextra.html#processingLayoutWidget
    """
    #  bool QFormBuilderExtra::processingLayoutWidget() const
    return self.uglySide.call(
        'ritual_ZNK17QFormBuilderExtra22processingLayoutWidgetEv',
    )

  def resourceBuilder(self) -> Optional[QResourceBuilder]:
    """
    Calls Qt's 'QResourceBuilder *QFormBuilderExtra::resourceBuilder()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformbuilderextra.html#resourceBuilder

    Returns
    -------

    Optional[QResourceBuilder]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QResourceBuilder *QFormBuilderExtra::resourceBuilder() const
    address = self.uglySide.call(
        'ritual_ZNK17QFormBuilderExtra15resourceBuilderEv',
    )
    from . import QResourceBuilder
    return QResourceBuilder._cuteAt(address)

  def textBuilder(self) -> Optional[QTextBuilder]:
    """
    Calls Qt's 'QTextBuilder *QFormBuilderExtra::textBuilder() const'.

    Qt's own words: https://doc.qt.io/qt-6/qformbuilderextra.html#textBuilder

    Returns
    -------

    Optional[QTextBuilder]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextBuilder *QFormBuilderExtra::textBuilder() const
    address = self.uglySide.call(
        'ritual_ZNK17QFormBuilderExtra11textBuilderEv',
    )
    from . import QTextBuilder
    return QTextBuilder._cuteAt(address)

  @overload(str)
  def customWidgetAddPageMethod(self, className: str) -> str:
    """
    Calls Qt's 'QString QFormBuilderExtra::customWidgetAddPageMethod(const
    QString &className) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformbuilderextra.html#customWidgetAddPageMethod

    Parameters
    ----------

    className : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFormBuilderExtra::customWidgetAddPageMethod(const QString
    #      &className) const
    return self.uglySide.call(
        'ritual_ZNK17QFormBuilderExtra25customWidgetAddPageMethodERK7QStrin'
        'g',
        className,
    )

  @overload(str)
  def customWidgetBaseClass(self, className: str) -> str:
    """
    Calls Qt's 'QString QFormBuilderExtra::customWidgetBaseClass(const
    QString &className) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformbuilderextra.html#customWidgetBaseClass

    Parameters
    ----------

    className : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFormBuilderExtra::customWidgetBaseClass(const QString
    #      &className) const
    return self.uglySide.call(
        'ritual_ZNK17QFormBuilderExtra21customWidgetBaseClassERK7QString',
        className,
    )

  @overload(str)
  def isCustomWidgetContainer(self, className: str) -> bool:
    """
    Calls Qt's 'bool QFormBuilderExtra::isCustomWidgetContainer(const QString
    &className) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformbuilderextra.html#isCustomWidgetContainer

    Parameters
    ----------

    className : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QFormBuilderExtra::isCustomWidgetContainer(const QString
    #      &className) const
    return self.uglySide.call(
        'ritual_ZNK17QFormBuilderExtra23isCustomWidgetContainerERK7QString',
        className,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setProcessingLayoutWidget(self, processing: bool) -> None:
    """
    Calls Qt's 'void QFormBuilderExtra::setProcessingLayoutWidget(bool
    processing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformbuilderextra.html#setProcessingLayoutWidget

    Parameters
    ----------

    processing : bool
      Passed on as it is.
    """
    #  void QFormBuilderExtra::setProcessingLayoutWidget(bool processing)
    self.uglySide.call(
        'ritual_ZN17QFormBuilderExtra25setProcessingLayoutWidgetEb',
        processing,
    )

  @overload(QResourceBuilder)
  @overload(NoneType)
  def setResourceBuilder(self, builder: Optional[QResourceBuilder]) -> None:
    """
    Calls Qt's 'void QFormBuilderExtra::setResourceBuilder(QResourceBuilder
    *builder)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformbuilderextra.html#setResourceBuilder

    Parameters
    ----------

    builder : Optional[QResourceBuilder]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFormBuilderExtra::setResourceBuilder(QResourceBuilder *builder)
    self.uglySide.call(
        'ritual_ZN17QFormBuilderExtra18setResourceBuilderEP16QResourceBuild'
        'er',
        self._addressOf(builder),
    )

  @overload(QTextBuilder)
  @overload(NoneType)
  def setTextBuilder(self, builder: Optional[QTextBuilder]) -> None:
    """
    Calls Qt's 'void QFormBuilderExtra::setTextBuilder(QTextBuilder
    *builder)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformbuilderextra.html#setTextBuilder

    Parameters
    ----------

    builder : Optional[QTextBuilder]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFormBuilderExtra::setTextBuilder(QTextBuilder *builder)
    self.uglySide.call(
        'ritual_ZN17QFormBuilderExtra14setTextBuilderEP12QTextBuilder',
        self._addressOf(builder),
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
    Notes what was given, for Qt's 'QFormBuilderExtra::QFormBuilderExtra()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qformbuilderextra.html#QFormBuilderExtra
    """
    #  QFormBuilderExtra::QFormBuilderExtra()
    self._noteCreation(QFormBuilderExtra, lambda: Rituals.call(
        'ritual_ZN17QFormBuilderExtraC1Ev',
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

  def clear(self) -> None:
    """
    Calls Qt's 'void QFormBuilderExtra::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qformbuilderextra.html#clear
    """
    #  void QFormBuilderExtra::clear()
    self.uglySide.call('ritual_ZN17QFormBuilderExtra5clearEv')

  @overload(QIODevice)
  @overload(NoneType)
  def readUi(self, dev: Optional[QIODevice]) -> Optional[DomUI]:
    """
    Calls Qt's 'DomUI *QFormBuilderExtra::readUi(QIODevice *dev)'.

    Qt's own words: https://doc.qt.io/qt-6/qformbuilderextra.html#readUi

    Parameters
    ----------

    dev : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[DomUI]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomUI *QFormBuilderExtra::readUi(QIODevice *dev)
    address = self.uglySide.call(
        'ritual_ZN17QFormBuilderExtra6readUiEP9QIODevice',
        self._addressOf(dev),
    )
    from . import DomUI
    return DomUI._cuteAt(address)

  @overload(QObject, str, QVariant)
  @overload(NoneType, str, QVariant)
  def applyPropertyInternally(
      self,
      o: Optional[QObject],
      propertyName: str,
      value: QVariant,
  ) -> bool:
    """
    Calls Qt's 'bool QFormBuilderExtra::applyPropertyInternally(QObject *o,
    const QString &propertyName, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformbuilderextra.html#applyPropertyInternally

    Parameters
    ----------

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    propertyName : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  bool QFormBuilderExtra::applyPropertyInternally(QObject *o, const
    #      QString &propertyName, const QVariant &value)
    return self.uglySide.call(
        'ritual_ZN17QFormBuilderExtra23applyPropertyInternallyEP7QObjectRK7'
        'QStringRK8QVariant',
        self._addressOf(o, 'QObject'), propertyName, self._valueOf(value),
    )

  def applyInternalProperties(self) -> None:
    """
    Calls Qt's 'void QFormBuilderExtra::applyInternalProperties() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformbuilderextra.html#applyInternalProperties
    """
    #  void QFormBuilderExtra::applyInternalProperties() const
    self.uglySide.call(
        'ritual_ZNK17QFormBuilderExtra23applyInternalPropertiesEv',
    )

  @overload(str, DomCustomWidget)
  @overload(str, NoneType)
  def storeCustomWidgetData(
      self,
      className: str,
      d: Optional[DomCustomWidget],
  ) -> None:
    """
    Calls Qt's 'void QFormBuilderExtra::storeCustomWidgetData(const QString
    &className, const DomCustomWidget *d)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformbuilderextra.html#storeCustomWidgetData

    Parameters
    ----------

    className : str
      Passed on as it is: a QString is made of it for the call.

    d : Optional[DomCustomWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFormBuilderExtra::storeCustomWidgetData(const QString
    #      &className, const DomCustomWidget *d)
    self.uglySide.call(
        'ritual_ZN17QFormBuilderExtra21storeCustomWidgetDataERK7QStringPK15'
        'DomCustomWidget',
        className, self._addressOf(d),
    )

  @overload(DomButtonGroups)
  @overload(NoneType)
  def registerButtonGroups(self, groups: Optional[DomButtonGroups]) -> None:
    """
    Calls Qt's 'void QFormBuilderExtra::registerButtonGroups(const
    DomButtonGroups *groups)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformbuilderextra.html#registerButtonGroups

    Parameters
    ----------

    groups : Optional[DomButtonGroups]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFormBuilderExtra::registerButtonGroups(const DomButtonGroups
    #      *groups)
    self.uglySide.call(
        'ritual_ZN17QFormBuilderExtra20registerButtonGroupsEPK15DomButtonGr'
        'oups',
        self._addressOf(groups),
    )

  def clearResourceBuilder(self) -> None:
    """
    Calls Qt's 'void QFormBuilderExtra::clearResourceBuilder()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformbuilderextra.html#clearResourceBuilder
    """
    #  void QFormBuilderExtra::clearResourceBuilder()
    self.uglySide.call(
        'ritual_ZN17QFormBuilderExtra20clearResourceBuilderEv',
    )

  def clearTextBuilder(self) -> None:
    """
    Calls Qt's 'void QFormBuilderExtra::clearTextBuilder()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformbuilderextra.html#clearTextBuilder
    """
    #  void QFormBuilderExtra::clearTextBuilder()
    self.uglySide.call('ritual_ZN17QFormBuilderExtra16clearTextBuilderEv')

  @staticmethod
  def buttonGroups(*__, **_) -> Never:
    """
    - Qt's 'const ButtonGroupHash &QFormBuilderExtra::buttonGroups() const':
      gives a type Python has no way to take yet.
    - Qt's 'ButtonGroupHash &QFormBuilderExtra::buttonGroups()': gives a type
      Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QFormBuilderExtra.buttonGroups' has no cute function yet. Qt's "
        "'const ButtonGroupHash &QFormBuilderExtra::buttonGroups() const': "
        "gives a type Python has no way to take yet. Qt's 'ButtonGroupHash "
        "&QFormBuilderExtra::buttonGroups()': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def getLayoutMargins(*__, **_) -> Never:
    """
    Qt's 'void QFormBuilderExtra::getLayoutMargins(const QList<DomProperty *>
    &properties, int *left, int *top, int *right, int *bottom)': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QFormBuilderExtra.getLayoutMargins' has no cute function yet. "
        "Qt's 'void QFormBuilderExtra::getLayoutMargins(const "
        "QList<DomProperty *> &properties, int *left, int *top, int *right, "
        "int *bottom)': takes a number to change where it is.")

  @staticmethod
  def parentWidget(*__, **_) -> Never:
    """
    Qt's 'const QPointer<QWidget> &QFormBuilderExtra::parentWidget() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QFormBuilderExtra.parentWidget' has no cute function yet. Qt's "
        "'const QPointer<QWidget> &QFormBuilderExtra::parentWidget() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def setParentWidget(*__, **_) -> Never:
    """
    Qt's 'void QFormBuilderExtra::setParentWidget(const QPointer<QWidget>
    &w)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QFormBuilderExtra.setParentWidget' has no cute function yet. Qt's "
        "'void QFormBuilderExtra::setParentWidget(const QPointer<QWidget> "
        "&w)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setPixmapProperty(*__, **_) -> Never:
    """
    Qt's 'void QFormBuilderExtra::setPixmapProperty(DomProperty *p, const
    std::pair<QString, QString> &ip)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QFormBuilderExtra.setPixmapProperty' has no cute function yet. "
        "Qt's 'void QFormBuilderExtra::setPixmapProperty(DomProperty *p, "
        "const std::pair<QString, QString> &ip)': takes a type Python has "
        "no way to hand over yet.")
