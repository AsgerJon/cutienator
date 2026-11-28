"""
qdesigner_internal::LayoutInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/layoutinfo_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means qdesigner_internal::LayoutInfo to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtWidgets import QLayout, QLayoutItem, QWidget
  from . import QDesignerFormEditorInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerFormEditorInterface = WAIT['QDesignerFormEditorInterface']
  QLayout = WAIT['QLayout']
  QLayoutItem = WAIT['QLayoutItem']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class LayoutInfo(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's qdesigner_internal::LayoutInfo: a plain Python object
  standing in front of one C++ qdesigner_internal::LayoutInfo.

  C++ hands a qdesigner_internal::LayoutInfo around as a copy, so every C++
  qdesigner_internal::LayoutInfo behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::LayoutInfo that has a ritual and
  that Python can call so far, 8 names in all: 'deleteLayout', 'layoutType',
  'layoutName', 'layoutParent', 'isWidgetLaidout', 'managedLayout',
  'internalLayout', 'isEmptyItem'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Type qdesigner_internal::LayoutInfo::managedLayoutType(const
    QDesignerFormEditorInterface *core, const QWidget *w, QLayout **layout)':
    takes a type Python has no way to hand over yet.
  - Qt's 'Type qdesigner_internal::LayoutInfo::laidoutWidgetType(const
    QDesignerFormEditorInterface *core, QWidget *widget, bool *isManaged,
    QLayout **layout)': takes a number to change where it is.
  - Qt's 'qdesigner_internal::LayoutInfo::~LayoutInfo()': the destructor:
    Python removes its C++ qdesigner_internal::LayoutInfo by it, and has no
    other use for it.

  What to expect
  --------------

  - The C++ qdesigner_internal::LayoutInfo is created at the first use, not
    by 'qdesigner_internal::LayoutInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a qdesigner_internal::LayoutInfo back gives a copy the
    ritual made for Python, in a new cute qdesigner_internal::LayoutInfo.
  - Each name of Qt's qdesigner_internal::LayoutInfo that has no cute
    function yet, 'laidoutWidgetType', 'managedLayoutType', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside qdesigner_internal::LayoutInfo, each a class
  #  in here as in C++, and the names Qt has for the combinations of its
  #  flags enums.

  class Type(CuteNum):
    """
    The enum 'qdesigner_internal::LayoutInfo::Type' of Qt, with the 8 names
    Qt gives in it.
    """

    NoLayout = Kee[int](0)
    HSplitter = Kee[int](1)
    VSplitter = Kee[int](2)
    HBox = Kee[int](3)
    VBox = Kee[int](4)
    Grid = Kee[int](5)
    Form = Kee[int](6)
    UnknownLayout = Kee[int](7)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QDesignerFormEditorInterface, QWidget)
  @overload(QDesignerFormEditorInterface, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def deleteLayout(
      core: Optional[QDesignerFormEditorInterface],
      widget: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void qdesigner_internal::LayoutInfo::deleteLayout(const
    QDesignerFormEditorInterface *core, QWidget *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layoutinfo.html#deleteLayout

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::LayoutInfo::deleteLayout(const
    #      QDesignerFormEditorInterface *core, QWidget *widget)
    Rituals.call(
        'ritual_ZN18qdesigner_internal10LayoutInfo12deleteLayoutEPK28QDesig'
        'nerFormEditorInterfaceP7QWidget',
        CuteMixin._addressOf(core), CuteMixin._addressOf(widget),
    )

  @staticmethod
  @overload(QDesignerFormEditorInterface, QWidget)
  @overload(QDesignerFormEditorInterface, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def layoutType(
      core: Optional[QDesignerFormEditorInterface],
      w: Optional[QWidget],
  ) -> Type:
    """
    Calls Qt's 'Type qdesigner_internal::LayoutInfo::layoutType(const
    QDesignerFormEditorInterface *core, const QWidget *w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layoutinfo.html#layoutType

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type qdesigner_internal::LayoutInfo::layoutType(const
    #      QDesignerFormEditorInterface *core, const QWidget *w)
    return LayoutInfo.Type(Rituals.call(
        'ritual_ZN18qdesigner_internal10LayoutInfo10layoutTypeEPK28QDesigne'
        'rFormEditorInterfacePK7QWidget',
        CuteMixin._addressOf(core), CuteMixin._addressOf(w),
    ))

  @staticmethod
  @overload(QDesignerFormEditorInterface, QLayout)
  @overload(NoneType, QLayout)
  def layoutType(
      core: Optional[QDesignerFormEditorInterface],
      layout: Optional[QLayout],
  ) -> Type:
    """
    Calls Qt's 'Type qdesigner_internal::LayoutInfo::layoutType(const
    QDesignerFormEditorInterface *core, const QLayout *layout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layoutinfo.html#layoutType

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    layout : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type qdesigner_internal::LayoutInfo::layoutType(const
    #      QDesignerFormEditorInterface *core, const QLayout *layout)
    return LayoutInfo.Type(Rituals.call(
        'ritual_ZN18qdesigner_internal10LayoutInfo10layoutTypeEPK28QDesigne'
        'rFormEditorInterfacePK7QLayout',
        CuteMixin._addressOf(core), CuteMixin._addressOf(layout),
    ))

  @staticmethod
  @overload(str)
  def layoutType(typeName: str) -> Type:
    """
    Calls Qt's 'Type qdesigner_internal::LayoutInfo::layoutType(const QString
    &typeName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layoutinfo.html#layoutType

    Parameters
    ----------

    typeName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type qdesigner_internal::LayoutInfo::layoutType(const QString
    #      &typeName)
    return LayoutInfo.Type(Rituals.call(
        'ritual_ZN18qdesigner_internal10LayoutInfo10layoutTypeERK7QString',
        typeName,
    ))

  @staticmethod
  @overload(Type)
  def layoutName(t: Type) -> str:
    """
    Calls Qt's 'QString qdesigner_internal::LayoutInfo::layoutName(Type t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layoutinfo.html#layoutName

    Parameters
    ----------

    t : Type
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::LayoutInfo::layoutName(Type t)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal10LayoutInfo10layoutNameENS0_4TypeE',
        t.value,
    )

  @staticmethod
  @overload(QDesignerFormEditorInterface, QLayout)
  @overload(QDesignerFormEditorInterface, NoneType)
  @overload(NoneType, QLayout)
  @overload(NoneType, NoneType)
  def layoutParent(
      core: Optional[QDesignerFormEditorInterface],
      layout: Optional[QLayout],
  ) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *qdesigner_internal::LayoutInfo::layoutParent(const
    QDesignerFormEditorInterface *core, QLayout *layout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layoutinfo.html#layoutParent

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    layout : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *qdesigner_internal::LayoutInfo::layoutParent(const
    #      QDesignerFormEditorInterface *core, QLayout *layout)
    address = Rituals.call(
        'ritual_ZN18qdesigner_internal10LayoutInfo12layoutParentEPK28QDesig'
        'nerFormEditorInterfaceP7QLayout',
        CuteMixin._addressOf(core), CuteMixin._addressOf(layout),
    )
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  @staticmethod
  @overload(QDesignerFormEditorInterface, QWidget)
  @overload(QDesignerFormEditorInterface, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def isWidgetLaidout(
      core: Optional[QDesignerFormEditorInterface],
      widget: Optional[QWidget],
  ) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::LayoutInfo::isWidgetLaidout(const
    QDesignerFormEditorInterface *core, QWidget *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layoutinfo.html#isWidgetLaidout

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool qdesigner_internal::LayoutInfo::isWidgetLaidout(const
    #      QDesignerFormEditorInterface *core, QWidget *widget)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal10LayoutInfo15isWidgetLaidoutEPK28QDe'
        'signerFormEditorInterfaceP7QWidget',
        CuteMixin._addressOf(core), CuteMixin._addressOf(widget),
    )

  @staticmethod
  @overload(QDesignerFormEditorInterface, QWidget)
  @overload(QDesignerFormEditorInterface, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def managedLayout(
      core: Optional[QDesignerFormEditorInterface],
      widget: Optional[QWidget],
  ) -> Optional[QLayout]:
    """
    Calls Qt's 'QLayout *qdesigner_internal::LayoutInfo::managedLayout(const
    QDesignerFormEditorInterface *core, const QWidget *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layoutinfo.html#managedLayout

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QLayout]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLayout *qdesigner_internal::LayoutInfo::managedLayout(const
    #      QDesignerFormEditorInterface *core, const QWidget *widget)
    address = Rituals.call(
        'ritual_ZN18qdesigner_internal10LayoutInfo13managedLayoutEPK28QDesi'
        'gnerFormEditorInterfacePK7QWidget',
        CuteMixin._addressOf(core), CuteMixin._addressOf(widget),
    )
    from ..QtWidgets import QLayout
    return QLayout._cuteAt(address)

  @staticmethod
  @overload(QDesignerFormEditorInterface, QLayout)
  @overload(NoneType, QLayout)
  def managedLayout(
      core: Optional[QDesignerFormEditorInterface],
      layout: Optional[QLayout],
  ) -> Optional[QLayout]:
    """
    Calls Qt's 'QLayout *qdesigner_internal::LayoutInfo::managedLayout(const
    QDesignerFormEditorInterface *core, QLayout *layout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layoutinfo.html#managedLayout

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    layout : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QLayout]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLayout *qdesigner_internal::LayoutInfo::managedLayout(const
    #      QDesignerFormEditorInterface *core, QLayout *layout)
    address = Rituals.call(
        'ritual_ZN18qdesigner_internal10LayoutInfo13managedLayoutEPK28QDesi'
        'gnerFormEditorInterfaceP7QLayout',
        CuteMixin._addressOf(core), CuteMixin._addressOf(layout),
    )
    from ..QtWidgets import QLayout
    return QLayout._cuteAt(address)

  @staticmethod
  @overload(QWidget)
  @overload(NoneType)
  def internalLayout(widget: Optional[QWidget]) -> Optional[QLayout]:
    """
    Calls Qt's 'QLayout *qdesigner_internal::LayoutInfo::internalLayout(const
    QWidget *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layoutinfo.html#internalLayout

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QLayout]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLayout *qdesigner_internal::LayoutInfo::internalLayout(const QWidget
    #      *widget)
    address = Rituals.call(
        'ritual_ZN18qdesigner_internal10LayoutInfo14internalLayoutEPK7QWidg'
        'et',
        CuteMixin._addressOf(widget),
    )
    from ..QtWidgets import QLayout
    return QLayout._cuteAt(address)

  @staticmethod
  @overload(QLayoutItem)
  @overload(NoneType)
  def isEmptyItem(item: Optional[QLayoutItem]) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::LayoutInfo::isEmptyItem(QLayoutItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layoutinfo.html#isEmptyItem

    Parameters
    ----------

    item : Optional[QLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool qdesigner_internal::LayoutInfo::isEmptyItem(QLayoutItem *item)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal10LayoutInfo11isEmptyItemEP11QLayoutI'
        'tem',
        CuteMixin._addressOf(item, 'QLayoutItem'),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::LayoutInfo'

  #  Qt's '~qdesigner_internal::LayoutInfo()'. Naming it makes this a value
  #  class: Python owns every C++ qdesigner_internal::LayoutInfo behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN18qdesigner_internal10LayoutInfoD1Ev'

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

  @staticmethod
  def laidoutWidgetType(*__, **_) -> Never:
    """
    Qt's 'Type qdesigner_internal::LayoutInfo::laidoutWidgetType(const
    QDesignerFormEditorInterface *core, QWidget *widget, bool *isManaged,
    QLayout **layout)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'qdesigner_internal.LayoutInfo.laidoutWidgetType' has no cute "
        "function yet. Qt's 'Type "
        "qdesigner_internal::LayoutInfo::laidoutWidgetType(const "
        "QDesignerFormEditorInterface *core, QWidget *widget, bool "
        "*isManaged, QLayout **layout)': takes a number to change where it "
        "is.")

  @staticmethod
  def managedLayoutType(*__, **_) -> Never:
    """
    Qt's 'Type qdesigner_internal::LayoutInfo::managedLayoutType(const
    QDesignerFormEditorInterface *core, const QWidget *w, QLayout **layout)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'qdesigner_internal.LayoutInfo.managedLayoutType' has no cute "
        "function yet. Qt's 'Type "
        "qdesigner_internal::LayoutInfo::managedLayoutType(const "
        "QDesignerFormEditorInterface *core, const QWidget *w, QLayout "
        "**layout)': takes a type Python has no way to hand over yet.")
