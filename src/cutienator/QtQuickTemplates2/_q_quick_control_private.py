"""
QQuickControlPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickcontrol_p_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickControlPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtGui import QAccessible
from ..QtQuick import QQuickItemPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QLocale, QMarginsF, QObject, QPointF, QRectF
  from ..QtGui import QEventPoint, QFont, QPalette
  from ..QtQuick import QQuickAccessibleAttached, QQuickGeometryChange
  from ..QtQuick import QQuickItem, QQuickItemChangeListener
  from . import QQuickControl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEventPoint = WAIT['QEventPoint']
  QFont = WAIT['QFont']
  QLocale = WAIT['QLocale']
  QObject = WAIT['QObject']
  QPointF = WAIT['QPointF']
  QQuickControl = WAIT['QQuickControl']
  QQuickGeometryChange = WAIT['QQuickGeometryChange']
  QQuickItem = WAIT['QQuickItem']
  QQuickItemChangeListener = WAIT['QQuickItemChangeListener']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickControlPrivate(QQuickItemPrivate):
  """
  The cute side of Qt's QQuickControlPrivate: a plain Python object standing
  in front of one C++ QQuickControlPrivate.

  It is built on the cute 'QQuickItemPrivate', as Qt's QQuickControlPrivate
  is built on Qt's QQuickItemPrivate, and has everything that class has. Qt's
  QQuickControlPrivate is built on Qt's
  QSafeQuickItemChangeListener<QQuickControlPrivate> as well, which is not
  reflected. Qt's QQuickControlPrivate is built on Qt's
  QAccessible::ActivationObserver as well, which is not reflected.

  What exists
  -----------

  Every function of Qt's QQuickControlPrivate that has a ritual and that
  Python can call so far, 72 names in all: 'q_func', 'get', 'init',
  'acceptTouch', 'handlePress', 'handleMove', 'handleRelease',
  'handleUngrab', 'mirrorChange', 'getPadding', 'getTopPadding',
  'getLeftPadding', 'getRightPadding', 'getBottomPadding',
  'getHorizontalPadding', 'getVerticalPadding', 'setTopPadding',
  'setLeftPadding', 'setRightPadding', 'setBottomPadding',
  'setHorizontalPadding', 'setVerticalPadding', 'getInset', 'getTopInset',
  'getLeftInset', 'getRightInset', 'getBottomInset', 'setTopInset',
  'setLeftInset', 'setRightInset', 'setBottomInset', 'resizeBackground',
  'resizeContent', 'getContentItem', 'setContentItem_helper',
  'accessibilityActiveChanged', 'accessibleRole', 'accessibleAttached',
  'resolveFont', 'inheritFont', 'updateFont', 'updateFontRecur',
  'setFont_helper', 'parentFont', 'updateLocale', 'updateLocaleRecur',
  'calcLocale', 'updateHoverEnabled', 'updateHoverEnabledRecur',
  'calcHoverEnabled', 'warnIfCustomizationNotSupported', 'cancelContentItem',
  'executeContentItem', 'cancelBackground', 'executeBackground',
  'hideOldItem', 'unhideOldItem', 'updateBaselineOffset',
  'addImplicitSizeListener', 'removeImplicitSizeListener',
  'itemImplicitWidthChanged', 'itemImplicitHeightChanged',
  'itemGeometryChanged', 'itemDestroyed', 'itemFocusChanged',
  'setLastFocusChangeReason', 'getContentWidth', 'getContentHeight',
  'updateImplicitContentWidth', 'updateImplicitContentHeight',
  'updateImplicitContentSize', 'defaultPalette'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickControl *QQuickControlPrivate::q_func() const': takes
    in Python what 'QQuickControl *QQuickControlPrivate::q_func()' takes.
  - Qt's 'QQuickControlPrivate::~QQuickControlPrivate()': the destructor:
    Python never removes a C++ QQuickControlPrivate.

  What to expect
  --------------

  - The C++ QQuickControlPrivate is created at the first use, not by
    'QQuickControlPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickControlPrivate.
  """

  #  The enums Qt writes inside QQuickControlPrivate, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class UnhideVisibility(CuteNum, scoped=True):
    """
    The enum 'QQuickControlPrivate::UnhideVisibility' of Qt, with the 2 names
    Qt gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Show = Kee[int](0)
    Hide = Kee[int](1)

  #  The classes Qt writes inside QQuickControlPrivate, each a class in here
  #  as in C++.

  class ExtraData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuickControlPrivate::ExtraData: a plain Python
    object standing in front of one C++ QQuickControlPrivate::ExtraData.

    C++ hands a QQuickControlPrivate::ExtraData around as a copy, so every
    C++ QQuickControlPrivate::ExtraData behind a cute one is Python's own: it
    is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QQuickControlPrivate::ExtraData yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuickControlPrivate::ExtraData::~ExtraData()': the destructor:
      Python removes its C++ QQuickControlPrivate::ExtraData by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ QQuickControlPrivate::ExtraData is created at the first use,
      not by 'QQuickControlPrivate::ExtraData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuickControlPrivate::ExtraData back gives a copy
      the ritual made for Python, in a new cute
      QQuickControlPrivate::ExtraData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuickControlPrivate::ExtraData'

    #  Qt's '~QQuickControlPrivate::ExtraData()'. Naming it makes this a
    #  value class: Python owns every C++ QQuickControlPrivate::ExtraData
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN20QQuickControlPrivate9ExtraDataD1Ev'

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
  @overload(QQuickControl)
  @overload(NoneType)
  def get(
      control: Optional[QQuickControl],
  ) -> Optional[QQuickControlPrivate]:
    """
    Calls Qt's 'QQuickControlPrivate *QQuickControlPrivate::get(QQuickControl
    *control)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrolprivate.html#get

    Parameters
    ----------

    control : Optional[QQuickControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickControlPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickControlPrivate *QQuickControlPrivate::get(QQuickControl
    #      *control)
    address = Rituals.call(
        'ritual_ZN20QQuickControlPrivate3getEP13QQuickControl',
        CuteMixin._addressOf(control),
    )
    return QQuickControlPrivate._cuteAt(address)

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def accessibleAttached(
      object: Optional[QObject],
  ) -> Optional[QQuickAccessibleAttached]:
    """
    Calls Qt's 'QQuickAccessibleAttached
    *QQuickControlPrivate::accessibleAttached(const QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#accessibleAttached

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickAccessibleAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAccessibleAttached
    #      *QQuickControlPrivate::accessibleAttached(const QObject *object)
    address = Rituals.call(
        'ritual_ZN20QQuickControlPrivate18accessibleAttachedEPK7QObject',
        CuteMixin._addressOf(object, 'QObject'),
    )
    from ..QtQuick import QQuickAccessibleAttached
    return QQuickAccessibleAttached._cuteAt(address)

  @staticmethod
  @overload(QQuickItem, QFont)
  @overload(NoneType, QFont)
  def updateFontRecur(item: Optional[QQuickItem], font: QFont) -> None:
    """
    Calls Qt's 'void QQuickControlPrivate::updateFontRecur(QQuickItem *item,
    const QFont &font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#updateFontRecur

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QQuickControlPrivate::updateFontRecur(QQuickItem *item, const
    #      QFont &font)
    Rituals.call(
        'ritual_ZN20QQuickControlPrivate15updateFontRecurEP10QQuickItemRK5Q'
        'Font',
        CuteMixin._addressOf(item), CuteMixin._valueOf(font),
    )

  @staticmethod
  @overload(QQuickItem)
  @overload(NoneType)
  def parentFont(item: Optional[QQuickItem]) -> QFont:
    """
    Calls Qt's 'QFont QQuickControlPrivate::parentFont(const QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#parentFont

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickControlPrivate::parentFont(const QQuickItem *item)
    address = Rituals.call(
        'ritual_ZN20QQuickControlPrivate10parentFontEPK10QQuickItem',
        CuteMixin._addressOf(item),
    )
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  @staticmethod
  @overload(QQuickItem, QLocale)
  @overload(NoneType, QLocale)
  def updateLocaleRecur(item: Optional[QQuickItem], l: QLocale) -> None:
    """
    Calls Qt's 'void QQuickControlPrivate::updateLocaleRecur(QQuickItem
    *item, const QLocale &l)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#updateLocaleRecur

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    l : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  void QQuickControlPrivate::updateLocaleRecur(QQuickItem *item, const
    #      QLocale &l)
    Rituals.call(
        'ritual_ZN20QQuickControlPrivate17updateLocaleRecurEP10QQuickItemRK'
        '7QLocale',
        CuteMixin._addressOf(item), CuteMixin._valueOf(l),
    )

  @staticmethod
  @overload(QQuickItem)
  @overload(NoneType)
  def calcLocale(item: Optional[QQuickItem]) -> QLocale:
    """
    Calls Qt's 'QLocale QQuickControlPrivate::calcLocale(const QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#calcLocale

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QLocale
      A new cute QLocale around the copy Qt gave back. Python owns it.
    """
    #  QLocale QQuickControlPrivate::calcLocale(const QQuickItem *item)
    address = Rituals.call(
        'ritual_ZN20QQuickControlPrivate10calcLocaleEPK10QQuickItem',
        CuteMixin._addressOf(item),
    )
    from ..QtCore import QLocale
    return QLocale._cuteOwning(address)

  @staticmethod
  @overload(QQuickItem, bool)
  @overload(NoneType, bool)
  def updateHoverEnabledRecur(
      item: Optional[QQuickItem],
      enabled: bool,
  ) -> None:
    """
    Calls Qt's 'void QQuickControlPrivate::updateHoverEnabledRecur(QQuickItem
    *item, bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#updateHoverEnabledRecur

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickControlPrivate::updateHoverEnabledRecur(QQuickItem *item,
    #      bool enabled)
    Rituals.call(
        'ritual_ZN20QQuickControlPrivate23updateHoverEnabledRecurEP10QQuick'
        'Itemb',
        CuteMixin._addressOf(item), enabled,
    )

  @staticmethod
  @overload(QQuickItem)
  @overload(NoneType)
  def calcHoverEnabled(item: Optional[QQuickItem]) -> bool:
    """
    Calls Qt's 'bool QQuickControlPrivate::calcHoverEnabled(const QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#calcHoverEnabled

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickControlPrivate::calcHoverEnabled(const QQuickItem *item)
    return Rituals.call(
        'ritual_ZN20QQuickControlPrivate16calcHoverEnabledEPK10QQuickItem',
        CuteMixin._addressOf(item),
    )

  @staticmethod
  @overload(QObject, QQuickItem, str)
  @overload(QObject, NoneType, str)
  @overload(NoneType, QQuickItem, str)
  @overload(NoneType, NoneType, str)
  def warnIfCustomizationNotSupported(
      control: Optional[QObject],
      item: Optional[QQuickItem],
      propertyName: str,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickControlPrivate::warnIfCustomizationNotSupported(QObject *control,
    QQuickItem *item, const QString &propertyName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html

    Parameters
    ----------

    control : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    propertyName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickControlPrivate::warnIfCustomizationNotSupported(QObject
    #      *control, QQuickItem *item, const QString &propertyName)
    Rituals.call(
        'ritual_ZN20QQuickControlPrivate31warnIfCustomizationNotSupportedEP'
        '7QObjectP10QQuickItemRK7QString',
        CuteMixin._addressOf(control, 'QObject'), CuteMixin._addressOf(item),
        propertyName,
    )

  @staticmethod
  @overload(QQuickItem)
  @overload(NoneType)
  def hideOldItem(item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickControlPrivate::hideOldItem(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#hideOldItem

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickControlPrivate::hideOldItem(QQuickItem *item)
    Rituals.call(
        'ritual_ZN20QQuickControlPrivate11hideOldItemEP10QQuickItem',
        CuteMixin._addressOf(item),
    )

  @staticmethod
  @overload(QQuickControl, QQuickItem)
  @overload(QQuickControl, NoneType)
  @overload(NoneType, QQuickItem)
  @overload(NoneType, NoneType)
  @overload(QQuickControl, QQuickItem, UnhideVisibility)
  @overload(QQuickControl, NoneType, UnhideVisibility)
  @overload(NoneType, QQuickItem, UnhideVisibility)
  @overload(NoneType, NoneType, UnhideVisibility)
  def unhideOldItem(
      control: Optional[QQuickControl],
      item: Optional[QQuickItem],
      visibility: UnhideVisibility = UnhideVisibility.Show,
  ) -> None:
    """
    Calls Qt's 'void QQuickControlPrivate::unhideOldItem(QQuickControl
    *control, QQuickItem *item, UnhideVisibility visibility)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#unhideOldItem

    Parameters
    ----------

    control : Optional[QQuickControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    visibility : UnhideVisibility
      Passed on as its number. May be left out, as in Qt: it is then
      UnhideVisibility.Show.
    """
    #  void QQuickControlPrivate::unhideOldItem(QQuickControl *control,
    #      QQuickItem *item, UnhideVisibility visibility)
    Rituals.call(
        'ritual_ZN20QQuickControlPrivate13unhideOldItemEP13QQuickControlP10'
        'QQuickItemNS_16UnhideVisibilityE',
        CuteMixin._addressOf(control), CuteMixin._addressOf(item),
        visibility.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickControlPrivate'

  #  A C++ QQuickControlPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickControlPrivate'

  #  The functions Qt calls itself that QQuickControlPrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'acceptTouch': (
          ('_ZN20QQuickControlPrivate11acceptTouchERK11QEventPoint',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtGui:QEventPoint'),
           )),
      ),
      'handlePress': (
          ('_ZN20QQuickControlPrivate11handlePressERK7QPointFm',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore:QPointF'),
               ('unsigned long', 'number', ''),
           )),
      ),
      'handleMove': (
          ('_ZN20QQuickControlPrivate10handleMoveERK7QPointFm',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore:QPointF'),
               ('unsigned long', 'number', ''),
           )),
      ),
      'handleRelease': (
          ('_ZN20QQuickControlPrivate13handleReleaseERK7QPointFm',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore:QPointF'),
               ('unsigned long', 'number', ''),
           )),
      ),
      'handleUngrab': (
          ('_ZN20QQuickControlPrivate12handleUngrabEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'resizeBackground': (
          ('_ZN20QQuickControlPrivate16resizeBackgroundEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'resizeContent': (
          ('_ZN20QQuickControlPrivate13resizeContentEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'getContentItem': (
          ('_ZN20QQuickControlPrivate14getContentItemEv',
           ('address', 'address', 'QtQuick:QQuickItem'),
           ()),
      ),
      'resolveFont': (
          ('_ZN20QQuickControlPrivate11resolveFontEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'cancelContentItem': (
          ('_ZN20QQuickControlPrivate17cancelContentItemEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'executeContentItem': (
          ('_ZN20QQuickControlPrivate18executeContentItemEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'cancelBackground': (
          ('_ZN20QQuickControlPrivate16cancelBackgroundEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'executeBackground': (
          ('_ZN20QQuickControlPrivate17executeBackgroundEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'itemImplicitWidthChanged': (
          ('_ZN20QQuickControlPrivate24itemImplicitWidthChangedEP10QQuickIt'
           'em',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'itemImplicitHeightChanged': (
          ('_ZN20QQuickControlPrivate25itemImplicitHeightChangedEP10QQuickI'
           'tem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'itemGeometryChanged': (
          ('_ZN20QQuickControlPrivate19itemGeometryChangedEP10QQuickItem20Q'
           'QuickGeometryChangeRK6QRectF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('address', 'value', 'QtQuick:QQuickGeometryChange'),
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'itemDestroyed': (
          ('_ZN20QQuickControlPrivate13itemDestroyedEP10QQuickItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'itemFocusChanged': (
          ('_ZN20QQuickControlPrivate16itemFocusChangedEP10QQuickItemN2Qt11'
           'FocusReasonE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('int', 'enum', 'QtCore:Qt.FocusReason'),
           )),
      ),
      'getContentWidth': (
          ('_ZNK20QQuickControlPrivate15getContentWidthEv',
           ('double', 'number', ''),
           ()),
      ),
      'getContentHeight': (
          ('_ZNK20QQuickControlPrivate16getContentHeightEv',
           ('double', 'number', ''),
           ()),
      ),
      'defaultPalette': (
          ('_ZNK20QQuickControlPrivate14defaultPaletteEv',
           ('address', 'value', 'QtGui:QPalette'),
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

  def getPadding(self) -> QMarginsF:
    """
    Calls Qt's 'QMarginsF QQuickControlPrivate::getPadding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#getPadding

    Returns
    -------

    QMarginsF
      A new cute QMarginsF around the copy Qt gave back. Python owns it.
    """
    #  QMarginsF QQuickControlPrivate::getPadding() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickControlPrivate10getPaddingEv',
    )
    from ..QtCore import QMarginsF
    return QMarginsF._cuteOwning(address)

  def getTopPadding(self) -> float:
    """
    Calls Qt's 'qreal QQuickControlPrivate::getTopPadding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#getTopPadding
    """
    #  qreal QQuickControlPrivate::getTopPadding() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickControlPrivate13getTopPaddingEv',
    )

  def getLeftPadding(self) -> float:
    """
    Calls Qt's 'qreal QQuickControlPrivate::getLeftPadding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#getLeftPadding
    """
    #  qreal QQuickControlPrivate::getLeftPadding() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickControlPrivate14getLeftPaddingEv',
    )

  def getRightPadding(self) -> float:
    """
    Calls Qt's 'qreal QQuickControlPrivate::getRightPadding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#getRightPadding
    """
    #  qreal QQuickControlPrivate::getRightPadding() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickControlPrivate15getRightPaddingEv',
    )

  def getBottomPadding(self) -> float:
    """
    Calls Qt's 'qreal QQuickControlPrivate::getBottomPadding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#getBottomPadding
    """
    #  qreal QQuickControlPrivate::getBottomPadding() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickControlPrivate16getBottomPaddingEv',
    )

  def getHorizontalPadding(self) -> float:
    """
    Calls Qt's 'qreal QQuickControlPrivate::getHorizontalPadding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#getHorizontalPadding
    """
    #  qreal QQuickControlPrivate::getHorizontalPadding() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickControlPrivate20getHorizontalPaddingEv',
    )

  def getVerticalPadding(self) -> float:
    """
    Calls Qt's 'qreal QQuickControlPrivate::getVerticalPadding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#getVerticalPadding
    """
    #  qreal QQuickControlPrivate::getVerticalPadding() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickControlPrivate18getVerticalPaddingEv',
    )

  def getInset(self) -> QMarginsF:
    """
    Calls Qt's 'QMarginsF QQuickControlPrivate::getInset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrolprivate.html#getInset

    Returns
    -------

    QMarginsF
      A new cute QMarginsF around the copy Qt gave back. Python owns it.
    """
    #  QMarginsF QQuickControlPrivate::getInset() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickControlPrivate8getInsetEv',
    )
    from ..QtCore import QMarginsF
    return QMarginsF._cuteOwning(address)

  def getTopInset(self) -> float:
    """
    Calls Qt's 'qreal QQuickControlPrivate::getTopInset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#getTopInset
    """
    #  qreal QQuickControlPrivate::getTopInset() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickControlPrivate11getTopInsetEv',
    )

  def getLeftInset(self) -> float:
    """
    Calls Qt's 'qreal QQuickControlPrivate::getLeftInset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#getLeftInset
    """
    #  qreal QQuickControlPrivate::getLeftInset() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickControlPrivate12getLeftInsetEv',
    )

  def getRightInset(self) -> float:
    """
    Calls Qt's 'qreal QQuickControlPrivate::getRightInset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#getRightInset
    """
    #  qreal QQuickControlPrivate::getRightInset() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickControlPrivate13getRightInsetEv',
    )

  def getBottomInset(self) -> float:
    """
    Calls Qt's 'qreal QQuickControlPrivate::getBottomInset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#getBottomInset
    """
    #  qreal QQuickControlPrivate::getBottomInset() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickControlPrivate14getBottomInsetEv',
    )

  def accessibleRole(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QQuickControlPrivate::accessibleRole()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#accessibleRole

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QQuickControlPrivate::accessibleRole() const
    ritual = 'ritual_ZNK20QQuickControlPrivate14accessibleRoleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QQuickControlPrivate14accessibleRoleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  def getContentWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickControlPrivate::getContentWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#getContentWidth
    """
    #  qreal QQuickControlPrivate::getContentWidth() const
    ritual = 'ritual_ZNK20QQuickControlPrivate15getContentWidthEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QQuickControlPrivate15getContentWidthEv'
    return self.uglySide.call(ritual)

  def getContentHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickControlPrivate::getContentHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#getContentHeight
    """
    #  qreal QQuickControlPrivate::getContentHeight() const
    ritual = 'ritual_ZNK20QQuickControlPrivate16getContentHeightEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QQuickControlPrivate16getContentHeightEv'
    return self.uglySide.call(ritual)

  def defaultPalette(self) -> QPalette:
    """
    Calls Qt's 'QPalette QQuickControlPrivate::defaultPalette() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#defaultPalette

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  QPalette QQuickControlPrivate::defaultPalette() const
    ritual = 'ritual_ZNK20QQuickControlPrivate14defaultPaletteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QQuickControlPrivate14defaultPaletteEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPalette
    return QPalette._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  @overload(float, bool)
  def setTopPadding(self, value: float, reset: bool = False) -> None:
    """
    Calls Qt's 'void QQuickControlPrivate::setTopPadding(qreal value, bool
    reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#setTopPadding

    Parameters
    ----------

    value : float
      Passed on as it is.

    reset : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickControlPrivate::setTopPadding(qreal value, bool reset)
    self.uglySide.call(
        'ritual_ZN20QQuickControlPrivate13setTopPaddingEdb', value, reset,
    )

  @overload(float)
  @overload(float, bool)
  def setLeftPadding(self, value: float, reset: bool = False) -> None:
    """
    Calls Qt's 'void QQuickControlPrivate::setLeftPadding(qreal value, bool
    reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#setLeftPadding

    Parameters
    ----------

    value : float
      Passed on as it is.

    reset : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickControlPrivate::setLeftPadding(qreal value, bool reset)
    self.uglySide.call(
        'ritual_ZN20QQuickControlPrivate14setLeftPaddingEdb', value, reset,
    )

  @overload(float)
  @overload(float, bool)
  def setRightPadding(self, value: float, reset: bool = False) -> None:
    """
    Calls Qt's 'void QQuickControlPrivate::setRightPadding(qreal value, bool
    reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#setRightPadding

    Parameters
    ----------

    value : float
      Passed on as it is.

    reset : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickControlPrivate::setRightPadding(qreal value, bool reset)
    self.uglySide.call(
        'ritual_ZN20QQuickControlPrivate15setRightPaddingEdb', value, reset,
    )

  @overload(float)
  @overload(float, bool)
  def setBottomPadding(self, value: float, reset: bool = False) -> None:
    """
    Calls Qt's 'void QQuickControlPrivate::setBottomPadding(qreal value, bool
    reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#setBottomPadding

    Parameters
    ----------

    value : float
      Passed on as it is.

    reset : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickControlPrivate::setBottomPadding(qreal value, bool reset)
    self.uglySide.call(
        'ritual_ZN20QQuickControlPrivate16setBottomPaddingEdb', value, reset,
    )

  @overload(float)
  @overload(float, bool)
  def setHorizontalPadding(self, value: float, reset: bool = False) -> None:
    """
    Calls Qt's 'void QQuickControlPrivate::setHorizontalPadding(qreal value,
    bool reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#setHorizontalPadding

    Parameters
    ----------

    value : float
      Passed on as it is.

    reset : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickControlPrivate::setHorizontalPadding(qreal value, bool
    #      reset)
    self.uglySide.call(
        'ritual_ZN20QQuickControlPrivate20setHorizontalPaddingEdb',
        value, reset,
    )

  @overload(float)
  @overload(float, bool)
  def setVerticalPadding(self, value: float, reset: bool = False) -> None:
    """
    Calls Qt's 'void QQuickControlPrivate::setVerticalPadding(qreal value,
    bool reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#setVerticalPadding

    Parameters
    ----------

    value : float
      Passed on as it is.

    reset : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickControlPrivate::setVerticalPadding(qreal value, bool reset)
    self.uglySide.call(
        'ritual_ZN20QQuickControlPrivate18setVerticalPaddingEdb',
        value, reset,
    )

  @overload(float)
  @overload(float, bool)
  def setTopInset(self, value: float, reset: bool = False) -> None:
    """
    Calls Qt's 'void QQuickControlPrivate::setTopInset(qreal value, bool
    reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#setTopInset

    Parameters
    ----------

    value : float
      Passed on as it is.

    reset : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickControlPrivate::setTopInset(qreal value, bool reset)
    self.uglySide.call(
        'ritual_ZN20QQuickControlPrivate11setTopInsetEdb', value, reset,
    )

  @overload(float)
  @overload(float, bool)
  def setLeftInset(self, value: float, reset: bool = False) -> None:
    """
    Calls Qt's 'void QQuickControlPrivate::setLeftInset(qreal value, bool
    reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#setLeftInset

    Parameters
    ----------

    value : float
      Passed on as it is.

    reset : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickControlPrivate::setLeftInset(qreal value, bool reset)
    self.uglySide.call(
        'ritual_ZN20QQuickControlPrivate12setLeftInsetEdb', value, reset,
    )

  @overload(float)
  @overload(float, bool)
  def setRightInset(self, value: float, reset: bool = False) -> None:
    """
    Calls Qt's 'void QQuickControlPrivate::setRightInset(qreal value, bool
    reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#setRightInset

    Parameters
    ----------

    value : float
      Passed on as it is.

    reset : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickControlPrivate::setRightInset(qreal value, bool reset)
    self.uglySide.call(
        'ritual_ZN20QQuickControlPrivate13setRightInsetEdb', value, reset,
    )

  @overload(float)
  @overload(float, bool)
  def setBottomInset(self, value: float, reset: bool = False) -> None:
    """
    Calls Qt's 'void QQuickControlPrivate::setBottomInset(qreal value, bool
    reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#setBottomInset

    Parameters
    ----------

    value : float
      Passed on as it is.

    reset : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickControlPrivate::setBottomInset(qreal value, bool reset)
    self.uglySide.call(
        'ritual_ZN20QQuickControlPrivate14setBottomInsetEdb', value, reset,
    )

  @overload(QQuickItem)
  @overload(NoneType)
  @overload(QQuickItem, bool)
  @overload(NoneType, bool)
  def setContentItem_helper(
      self,
      item: Optional[QQuickItem],
      notify: bool = True,
  ) -> None:
    """
    Calls Qt's 'void QQuickControlPrivate::setContentItem_helper(QQuickItem
    *item, bool notify)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#setContentItem_helper

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    notify : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QQuickControlPrivate::setContentItem_helper(QQuickItem *item,
    #      bool notify)
    self.uglySide.call(
        'ritual_ZN20QQuickControlPrivate21setContentItem_helperEP10QQuickIt'
        'emb',
        self._addressOf(item), notify,
    )

  @overload(QFont)
  def setFont_helper(self, font: QFont) -> None:
    """
    Calls Qt's 'void QQuickControlPrivate::setFont_helper(const QFont
    &font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#setFont_helper

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QQuickControlPrivate::setFont_helper(const QFont &font)
    self.uglySide.call(
        'ritual_ZN20QQuickControlPrivate14setFont_helperERK5QFont',
        self._valueOf(font),
    )

  @overload(Qt.FocusReason)
  def setLastFocusChangeReason(self, a0: Qt.FocusReason) -> bool:
    """
    Calls Qt's 'bool
    QQuickControlPrivate::setLastFocusChangeReason(Qt::FocusReason a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#setLastFocusChangeReason

    Parameters
    ----------

    a0 : Qt.FocusReason
      Passed on as its number.
    """
    #  bool QQuickControlPrivate::setLastFocusChangeReason(Qt::FocusReason
    #      a0)
    ritual = (
        'ritual_ZN20QQuickControlPrivate24setLastFocusChangeReasonEN2Qt11Fo'
        'cusReasonE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickControlPrivate24setLastFocusChangeReasonEN2'
          'Qt11FocusReasonE')
    return self.uglySide.call(ritual, a0.value)

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
    'QQuickControlPrivate::QQuickControlPrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#QQuickControlPrivate
    """
    #  QQuickControlPrivate::QQuickControlPrivate()
    self._noteCreation(QQuickControlPrivate, lambda: Rituals.call(
        'ritual_ZN20QQuickControlPrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickControl]:
    """
    Calls Qt's 'QQuickControl *QQuickControlPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrolprivate.html#q_func

    Returns
    -------

    Optional[QQuickControl]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickControl *QQuickControlPrivate::q_func()
    address = self.uglySide.call('ritual_ZN20QQuickControlPrivate6q_funcEv')
    from . import QQuickControl
    return QQuickControl._cuteAt(address)

  def init(self) -> None:
    """
    Calls Qt's 'void QQuickControlPrivate::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrolprivate.html#init
    """
    #  void QQuickControlPrivate::init()
    self.uglySide.call('ritual_ZN20QQuickControlPrivate4initEv')

  @overload(QEventPoint)
  def acceptTouch(self, point: QEventPoint) -> bool:
    """
    Calls Qt's 'bool QQuickControlPrivate::acceptTouch(const
    QTouchEvent::TouchPoint &point)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#acceptTouch

    Parameters
    ----------

    point : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.
    """
    #  bool QQuickControlPrivate::acceptTouch(const QTouchEvent::TouchPoint
    #      &point)
    ritual = 'ritual_ZN20QQuickControlPrivate11acceptTouchERK11QEventPoint'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickControlPrivate11acceptTouchERK11QEventPoint')
    return self.uglySide.call(ritual, self._valueOf(point))

  @overload(QPointF, int)
  def handlePress(self, point: QPointF, timestamp: int) -> bool:
    """
    Calls Qt's 'bool QQuickControlPrivate::handlePress(const QPointF &point,
    ulong timestamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#handlePress

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    timestamp : int
      Passed on as it is.
    """
    #  bool QQuickControlPrivate::handlePress(const QPointF &point, ulong
    #      timestamp)
    ritual = 'ritual_ZN20QQuickControlPrivate11handlePressERK7QPointFm'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickControlPrivate11handlePressERK7QPointFm'
    return self.uglySide.call(
        ritual, self._valueOf(point, 'QPointF'), timestamp,
    )

  @overload(QPointF, int)
  def handleMove(self, point: QPointF, timestamp: int) -> bool:
    """
    Calls Qt's 'bool QQuickControlPrivate::handleMove(const QPointF &point,
    ulong timestamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#handleMove

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    timestamp : int
      Passed on as it is.
    """
    #  bool QQuickControlPrivate::handleMove(const QPointF &point, ulong
    #      timestamp)
    ritual = 'ritual_ZN20QQuickControlPrivate10handleMoveERK7QPointFm'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickControlPrivate10handleMoveERK7QPointFm'
    return self.uglySide.call(
        ritual, self._valueOf(point, 'QPointF'), timestamp,
    )

  @overload(QPointF, int)
  def handleRelease(self, point: QPointF, timestamp: int) -> bool:
    """
    Calls Qt's 'bool QQuickControlPrivate::handleRelease(const QPointF
    &point, ulong timestamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#handleRelease

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    timestamp : int
      Passed on as it is.
    """
    #  bool QQuickControlPrivate::handleRelease(const QPointF &point, ulong
    #      timestamp)
    ritual = 'ritual_ZN20QQuickControlPrivate13handleReleaseERK7QPointFm'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickControlPrivate13handleReleaseERK7QPointFm')
    return self.uglySide.call(
        ritual, self._valueOf(point, 'QPointF'), timestamp,
    )

  def handleUngrab(self) -> None:
    """
    Calls Qt's 'void QQuickControlPrivate::handleUngrab()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#handleUngrab
    """
    #  void QQuickControlPrivate::handleUngrab()
    ritual = 'ritual_ZN20QQuickControlPrivate12handleUngrabEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickControlPrivate12handleUngrabEv'
    self.uglySide.call(ritual)

  def mirrorChange(self) -> None:
    """
    Calls Qt's 'void QQuickControlPrivate::mirrorChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#mirrorChange
    """
    #  void QQuickControlPrivate::mirrorChange()
    ritual = 'ritual_ZN20QQuickControlPrivate12mirrorChangeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickControlPrivate12mirrorChangeEv'
    self.uglySide.call(ritual)

  def resizeBackground(self) -> None:
    """
    Calls Qt's 'void QQuickControlPrivate::resizeBackground()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#resizeBackground
    """
    #  void QQuickControlPrivate::resizeBackground()
    ritual = 'ritual_ZN20QQuickControlPrivate16resizeBackgroundEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickControlPrivate16resizeBackgroundEv'
    self.uglySide.call(ritual)

  def resizeContent(self) -> None:
    """
    Calls Qt's 'void QQuickControlPrivate::resizeContent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#resizeContent
    """
    #  void QQuickControlPrivate::resizeContent()
    ritual = 'ritual_ZN20QQuickControlPrivate13resizeContentEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickControlPrivate13resizeContentEv'
    self.uglySide.call(ritual)

  def getContentItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickControlPrivate::getContentItem()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#getContentItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickControlPrivate::getContentItem()
    ritual = 'ritual_ZN20QQuickControlPrivate14getContentItemEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickControlPrivate14getContentItemEv'
    address = self.uglySide.call(ritual)
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  @overload(bool)
  def accessibilityActiveChanged(self, active: bool) -> None:
    """
    Calls Qt's 'void QQuickControlPrivate::accessibilityActiveChanged(bool
    active)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html

    Parameters
    ----------

    active : bool
      Passed on as it is.
    """
    #  void QQuickControlPrivate::accessibilityActiveChanged(bool active)
    ritual = 'ritual_ZN20QQuickControlPrivate26accessibilityActiveChangedEb'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickControlPrivate26accessibilityActiveChangedE'
          'b')
    self.uglySide.call(ritual, active)

  def resolveFont(self) -> None:
    """
    Calls Qt's 'void QQuickControlPrivate::resolveFont()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#resolveFont
    """
    #  void QQuickControlPrivate::resolveFont()
    ritual = 'ritual_ZN20QQuickControlPrivate11resolveFontEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickControlPrivate11resolveFontEv'
    self.uglySide.call(ritual)

  @overload(QFont)
  def inheritFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QQuickControlPrivate::inheritFont(const QFont &font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#inheritFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QQuickControlPrivate::inheritFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN20QQuickControlPrivate11inheritFontERK5QFont',
        self._valueOf(font),
    )

  @overload(QFont)
  def updateFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QQuickControlPrivate::updateFont(const QFont &font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#updateFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QQuickControlPrivate::updateFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN20QQuickControlPrivate10updateFontERK5QFont',
        self._valueOf(font),
    )

  @overload(QLocale, bool)
  def updateLocale(self, l: QLocale, e: bool) -> None:
    """
    Calls Qt's 'void QQuickControlPrivate::updateLocale(const QLocale &l,
    bool e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#updateLocale

    Parameters
    ----------

    l : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.

    e : bool
      Passed on as it is.
    """
    #  void QQuickControlPrivate::updateLocale(const QLocale &l, bool e)
    self.uglySide.call(
        'ritual_ZN20QQuickControlPrivate12updateLocaleERK7QLocaleb',
        self._valueOf(l), e,
    )

  @overload(bool, bool)
  def updateHoverEnabled(self, enabled: bool, xplicit: bool) -> None:
    """
    Calls Qt's 'void QQuickControlPrivate::updateHoverEnabled(bool enabled,
    bool xplicit)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#updateHoverEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.

    xplicit : bool
      Passed on as it is.
    """
    #  void QQuickControlPrivate::updateHoverEnabled(bool enabled, bool
    #      xplicit)
    self.uglySide.call(
        'ritual_ZN20QQuickControlPrivate18updateHoverEnabledEbb',
        enabled, xplicit,
    )

  def cancelContentItem(self) -> None:
    """
    Calls Qt's 'void QQuickControlPrivate::cancelContentItem()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#cancelContentItem
    """
    #  void QQuickControlPrivate::cancelContentItem()
    ritual = 'ritual_ZN20QQuickControlPrivate17cancelContentItemEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickControlPrivate17cancelContentItemEv'
    self.uglySide.call(ritual)

  @overload()
  @overload(bool)
  def executeContentItem(self, complete: bool = False) -> None:
    """
    Calls Qt's 'void QQuickControlPrivate::executeContentItem(bool
    complete)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#executeContentItem

    Parameters
    ----------

    complete : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickControlPrivate::executeContentItem(bool complete)
    ritual = 'ritual_ZN20QQuickControlPrivate18executeContentItemEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickControlPrivate18executeContentItemEb'
    self.uglySide.call(ritual, complete)

  def cancelBackground(self) -> None:
    """
    Calls Qt's 'void QQuickControlPrivate::cancelBackground()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#cancelBackground
    """
    #  void QQuickControlPrivate::cancelBackground()
    ritual = 'ritual_ZN20QQuickControlPrivate16cancelBackgroundEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickControlPrivate16cancelBackgroundEv'
    self.uglySide.call(ritual)

  @overload()
  @overload(bool)
  def executeBackground(self, complete: bool = False) -> None:
    """
    Calls Qt's 'void QQuickControlPrivate::executeBackground(bool complete)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#executeBackground

    Parameters
    ----------

    complete : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickControlPrivate::executeBackground(bool complete)
    ritual = 'ritual_ZN20QQuickControlPrivate17executeBackgroundEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickControlPrivate17executeBackgroundEb'
    self.uglySide.call(ritual, complete)

  def updateBaselineOffset(self) -> None:
    """
    Calls Qt's 'void QQuickControlPrivate::updateBaselineOffset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#updateBaselineOffset
    """
    #  void QQuickControlPrivate::updateBaselineOffset()
    self.uglySide.call(
        'ritual_ZN20QQuickControlPrivate20updateBaselineOffsetEv',
    )

  @overload(QQuickItem, QQuickItemPrivate.ChangeTypes)
  @overload(NoneType, QQuickItemPrivate.ChangeTypes)
  def addImplicitSizeListener(
      self,
      item: Optional[QQuickItem],
      changes: QQuickItemPrivate.ChangeTypes,
  ) -> None:
    """
    Calls Qt's 'void QQuickControlPrivate::addImplicitSizeListener(QQuickItem
    *item, ChangeTypes changes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#addImplicitSizeListener

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    changes : QQuickItemPrivate.ChangeTypes
      Passed on as its number.
    """
    #  void QQuickControlPrivate::addImplicitSizeListener(QQuickItem *item,
    #      ChangeTypes changes)
    self.uglySide.call(
        'ritual_ZN20QQuickControlPrivate23addImplicitSizeListenerEP10QQuick'
        'Item6QFlagsIN17QQuickItemPrivate10ChangeTypeEE',
        self._addressOf(item), changes.value,
    )

  @staticmethod
  @overload(
      QQuickItem, QQuickItemChangeListener, QQuickItemPrivate.ChangeTypes,
  )
  @overload(QQuickItem, NoneType, QQuickItemPrivate.ChangeTypes)
  @overload(
      NoneType, QQuickItemChangeListener, QQuickItemPrivate.ChangeTypes,
  )
  @overload(NoneType, NoneType, QQuickItemPrivate.ChangeTypes)
  def addImplicitSizeListener(
      item: Optional[QQuickItem],
      listener: Optional[QQuickItemChangeListener],
      changes: QQuickItemPrivate.ChangeTypes,
  ) -> None:
    """
    Calls Qt's 'void QQuickControlPrivate::addImplicitSizeListener(QQuickItem
    *item, QQuickItemChangeListener *listener, ChangeTypes changes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#addImplicitSizeListener

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    listener : Optional[QQuickItemChangeListener]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    changes : QQuickItemPrivate.ChangeTypes
      Passed on as its number.
    """
    #  void QQuickControlPrivate::addImplicitSizeListener(QQuickItem *item,
    #      QQuickItemChangeListener *listener, ChangeTypes changes)
    Rituals.call(
        'ritual_ZN20QQuickControlPrivate23addImplicitSizeListenerEP10QQuick'
        'ItemP24QQuickItemChangeListener6QFlagsIN17QQuickItemPrivate10Chang'
        'eTypeEE',
        CuteMixin._addressOf(item), CuteMixin._addressOf(listener,
        'QQuickItemChangeListener'), changes.value,
    )

  @overload(QQuickItem, QQuickItemPrivate.ChangeTypes)
  @overload(NoneType, QQuickItemPrivate.ChangeTypes)
  def removeImplicitSizeListener(
      self,
      item: Optional[QQuickItem],
      changes: QQuickItemPrivate.ChangeTypes,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickControlPrivate::removeImplicitSizeListener(QQuickItem *item,
    ChangeTypes changes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    changes : QQuickItemPrivate.ChangeTypes
      Passed on as its number.
    """
    #  void QQuickControlPrivate::removeImplicitSizeListener(QQuickItem
    #      *item, ChangeTypes changes)
    self.uglySide.call(
        'ritual_ZN20QQuickControlPrivate26removeImplicitSizeListenerEP10QQu'
        'ickItem6QFlagsIN17QQuickItemPrivate10ChangeTypeEE',
        self._addressOf(item), changes.value,
    )

  @staticmethod
  @overload(
      QQuickItem, QQuickItemChangeListener, QQuickItemPrivate.ChangeTypes,
  )
  @overload(QQuickItem, NoneType, QQuickItemPrivate.ChangeTypes)
  @overload(
      NoneType, QQuickItemChangeListener, QQuickItemPrivate.ChangeTypes,
  )
  @overload(NoneType, NoneType, QQuickItemPrivate.ChangeTypes)
  def removeImplicitSizeListener(
      item: Optional[QQuickItem],
      listener: Optional[QQuickItemChangeListener],
      changes: QQuickItemPrivate.ChangeTypes,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickControlPrivate::removeImplicitSizeListener(QQuickItem *item,
    QQuickItemChangeListener *listener, ChangeTypes changes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    listener : Optional[QQuickItemChangeListener]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    changes : QQuickItemPrivate.ChangeTypes
      Passed on as its number.
    """
    #  void QQuickControlPrivate::removeImplicitSizeListener(QQuickItem
    #      *item, QQuickItemChangeListener *listener, ChangeTypes changes)
    Rituals.call(
        'ritual_ZN20QQuickControlPrivate26removeImplicitSizeListenerEP10QQu'
        'ickItemP24QQuickItemChangeListener6QFlagsIN17QQuickItemPrivate10Ch'
        'angeTypeEE',
        CuteMixin._addressOf(item), CuteMixin._addressOf(listener,
        'QQuickItemChangeListener'), changes.value,
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def itemImplicitWidthChanged(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void
    QQuickControlPrivate::itemImplicitWidthChanged(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#itemImplicitWidthChanged

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickControlPrivate::itemImplicitWidthChanged(QQuickItem *item)
    ritual = (
        'ritual_ZN20QQuickControlPrivate24itemImplicitWidthChangedEP10QQuic'
        'kItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickControlPrivate24itemImplicitWidthChangedEP1'
          '0QQuickItem')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QQuickItem)
  @overload(NoneType)
  def itemImplicitHeightChanged(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void
    QQuickControlPrivate::itemImplicitHeightChanged(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickControlPrivate::itemImplicitHeightChanged(QQuickItem *item)
    ritual = (
        'ritual_ZN20QQuickControlPrivate25itemImplicitHeightChangedEP10QQui'
        'ckItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickControlPrivate25itemImplicitHeightChangedEP'
          '10QQuickItem')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QQuickItem, QQuickGeometryChange, QRectF)
  @overload(NoneType, QQuickGeometryChange, QRectF)
  def itemGeometryChanged(
      self,
      item: Optional[QQuickItem],
      change: QQuickGeometryChange,
      diff: QRectF,
  ) -> None:
    """
    Calls Qt's 'void QQuickControlPrivate::itemGeometryChanged(QQuickItem
    *item, QQuickGeometryChange change, const QRectF &diff)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#itemGeometryChanged

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    change : QQuickGeometryChange
      Passed on as a value: Qt reads the C++ QQuickGeometryChange, which
      stays Python's own.

    diff : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickControlPrivate::itemGeometryChanged(QQuickItem *item,
    #      QQuickGeometryChange change, const QRectF &diff)
    ritual = (
        'ritual_ZN20QQuickControlPrivate19itemGeometryChangedEP10QQuickItem'
        '20QQuickGeometryChangeRK6QRectF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickControlPrivate19itemGeometryChangedEP10QQui'
          'ckItem20QQuickGeometryChangeRK6QRectF')
    self.uglySide.call(
        ritual,
        self._addressOf(item), self._valueOf(change), self._valueOf(diff),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def itemDestroyed(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickControlPrivate::itemDestroyed(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#itemDestroyed

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickControlPrivate::itemDestroyed(QQuickItem *item)
    ritual = 'ritual_ZN20QQuickControlPrivate13itemDestroyedEP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickControlPrivate13itemDestroyedEP10QQuickItem')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QQuickItem, Qt.FocusReason)
  @overload(NoneType, Qt.FocusReason)
  def itemFocusChanged(
      self,
      item: Optional[QQuickItem],
      reason: Qt.FocusReason,
  ) -> None:
    """
    Calls Qt's 'void QQuickControlPrivate::itemFocusChanged(QQuickItem *item,
    Qt::FocusReason reason)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html#itemFocusChanged

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    reason : Qt.FocusReason
      Passed on as its number.
    """
    #  void QQuickControlPrivate::itemFocusChanged(QQuickItem *item,
    #      Qt::FocusReason reason)
    ritual = (
        'ritual_ZN20QQuickControlPrivate16itemFocusChangedEP10QQuickItemN2Q'
        't11FocusReasonE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickControlPrivate16itemFocusChangedEP10QQuickI'
          'temN2Qt11FocusReasonE')
    self.uglySide.call(ritual, self._addressOf(item), reason.value)

  def updateImplicitContentWidth(self) -> None:
    """
    Calls Qt's 'void QQuickControlPrivate::updateImplicitContentWidth()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html
    """
    #  void QQuickControlPrivate::updateImplicitContentWidth()
    self.uglySide.call(
        'ritual_ZN20QQuickControlPrivate26updateImplicitContentWidthEv',
    )

  def updateImplicitContentHeight(self) -> None:
    """
    Calls Qt's 'void QQuickControlPrivate::updateImplicitContentHeight()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html
    """
    #  void QQuickControlPrivate::updateImplicitContentHeight()
    self.uglySide.call(
        'ritual_ZN20QQuickControlPrivate27updateImplicitContentHeightEv',
    )

  def updateImplicitContentSize(self) -> None:
    """
    Calls Qt's 'void QQuickControlPrivate::updateImplicitContentSize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrolprivate.html
    """
    #  void QQuickControlPrivate::updateImplicitContentSize()
    self.uglySide.call(
        'ritual_ZN20QQuickControlPrivate25updateImplicitContentSizeEv',
    )
