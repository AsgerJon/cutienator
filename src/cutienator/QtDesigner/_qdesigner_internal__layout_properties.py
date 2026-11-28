"""
qdesigner_internal::LayoutProperties binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qlayout_widget_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::LayoutProperties to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtWidgets import QLayout
  from . import QDesignerFormEditorInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerFormEditorInterface = WAIT['QDesignerFormEditorInterface']
  QLayout = WAIT['QLayout']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class LayoutProperties(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's qdesigner_internal::LayoutProperties: a plain Python
  object standing in front of one C++ qdesigner_internal::LayoutProperties.

  C++ hands a qdesigner_internal::LayoutProperties around as a copy, so every
  C++ qdesigner_internal::LayoutProperties behind a cute one is Python's own:
  it is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::LayoutProperties that has a
  ritual and that Python can call so far, 4 names in all: 'clear',
  'visibleProperties', 'fromPropertySheet', 'toPropertySheet'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'qdesigner_internal::LayoutProperties::~LayoutProperties()': the
    destructor: Python removes its C++ qdesigner_internal::LayoutProperties
    by it, and has no other use for it.

  What to expect
  --------------

  - The C++ qdesigner_internal::LayoutProperties is created at the first use,
    not by 'qdesigner_internal::LayoutProperties(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a qdesigner_internal::LayoutProperties back gives a
    copy the ritual made for Python, in a new cute
    qdesigner_internal::LayoutProperties.
  """

  #  The enums Qt writes inside qdesigner_internal::LayoutProperties, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class Margins(CuteNum):
    """
    The enum 'qdesigner_internal::LayoutProperties::Margins' of Qt, with the
    5 names Qt gives in it.
    """

    LeftMargin = Kee[int](0)
    TopMargin = Kee[int](1)
    RightMargin = Kee[int](2)
    BottomMargin = Kee[int](3)
    MarginCount = Kee[int](4)

  class PropertyMask(CuteNum):
    """
    The enum 'qdesigner_internal::LayoutProperties::PropertyMask' of Qt, with
    the 19 names Qt gives in it.
    """

    ObjectNameProperty = Kee[int](1)
    LeftMarginProperty = Kee[int](2)
    TopMarginProperty = Kee[int](4)
    RightMarginProperty = Kee[int](8)
    BottomMarginProperty = Kee[int](16)
    SpacingProperty = Kee[int](32)
    HorizSpacingProperty = Kee[int](64)
    VertSpacingProperty = Kee[int](128)
    SizeConstraintProperty = Kee[int](256)
    FieldGrowthPolicyProperty = Kee[int](1024)
    RowWrapPolicyProperty = Kee[int](2048)
    LabelAlignmentProperty = Kee[int](4096)
    FormAlignmentProperty = Kee[int](8192)
    BoxStretchProperty = Kee[int](16384)
    GridRowStretchProperty = Kee[int](32768)
    GridColumnStretchProperty = Kee[int](65536)
    GridRowMinimumHeightProperty = Kee[int](131072)
    GridColumnMinimumWidthProperty = Kee[int](262144)
    AllProperties = Kee[int](1048575)

  class Spacings(CuteNum):
    """
    The enum 'qdesigner_internal::LayoutProperties::Spacings' of Qt, with the
    4 names Qt gives in it.
    """

    Spacing = Kee[int](0)
    HorizSpacing = Kee[int](1)
    VertSpacing = Kee[int](2)
    SpacingsCount = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QLayout)
  @overload(NoneType)
  def visibleProperties(layout: Optional[QLayout]) -> int:
    """
    Calls Qt's 'int
    qdesigner_internal::LayoutProperties::visibleProperties(const QLayout
    *layout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layoutproperties.html

    Parameters
    ----------

    layout : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int qdesigner_internal::LayoutProperties::visibleProperties(const
    #      QLayout *layout)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal16LayoutProperties17visibleProperties'
        'EPK7QLayout',
        CuteMixin._addressOf(layout),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::LayoutProperties'

  #  Qt's '~qdesigner_internal::LayoutProperties()'. Naming it makes this a
  #  value class: Python owns every C++ qdesigner_internal::LayoutProperties
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN18qdesigner_internal16LayoutPropertiesD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDesignerFormEditorInterface, QLayout)
  @overload(QDesignerFormEditorInterface, NoneType)
  @overload(NoneType, QLayout)
  @overload(NoneType, NoneType)
  @overload(QDesignerFormEditorInterface, QLayout, int)
  @overload(QDesignerFormEditorInterface, NoneType, int)
  @overload(NoneType, QLayout, int)
  @overload(NoneType, NoneType, int)
  @overload(QDesignerFormEditorInterface, QLayout, int, bool)
  @overload(QDesignerFormEditorInterface, NoneType, int, bool)
  @overload(NoneType, QLayout, int, bool)
  @overload(NoneType, NoneType, int, bool)
  def toPropertySheet(
      self,
      core: Optional[QDesignerFormEditorInterface],
      l: Optional[QLayout],
      mask: int = 1048575,
      applyChanged: bool = True,
  ) -> int:
    """
    Calls Qt's 'int
    qdesigner_internal::LayoutProperties::toPropertySheet(const
    QDesignerFormEditorInterface *core, QLayout *l, int mask, bool
    applyChanged) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layoutproperties.html

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    l : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    mask : int
      Passed on as it is. May be left out, as in Qt: it is then 1048575.

    applyChanged : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  int qdesigner_internal::LayoutProperties::toPropertySheet(const
    #      QDesignerFormEditorInterface *core, QLayout *l, int mask, bool
    #      applyChanged) const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal16LayoutProperties15toPropertySheetE'
        'PK28QDesignerFormEditorInterfaceP7QLayoutib',
        self._addressOf(core), self._addressOf(l), mask, applyChanged,
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
    'qdesigner_internal::LayoutProperties::LayoutProperties()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layoutproperties.html
    """
    #  qdesigner_internal::LayoutProperties::LayoutProperties()
    self._noteCreation(LayoutProperties, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal16LayoutPropertiesC1Ev',
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
    Calls Qt's 'void qdesigner_internal::LayoutProperties::clear()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layoutproperties.html#clear
    """
    #  void qdesigner_internal::LayoutProperties::clear()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal16LayoutProperties5clearEv',
    )

  @overload(QDesignerFormEditorInterface, QLayout)
  @overload(QDesignerFormEditorInterface, NoneType)
  @overload(NoneType, QLayout)
  @overload(NoneType, NoneType)
  @overload(QDesignerFormEditorInterface, QLayout, int)
  @overload(QDesignerFormEditorInterface, NoneType, int)
  @overload(NoneType, QLayout, int)
  @overload(NoneType, NoneType, int)
  def fromPropertySheet(
      self,
      core: Optional[QDesignerFormEditorInterface],
      l: Optional[QLayout],
      mask: int = 1048575,
  ) -> int:
    """
    Calls Qt's 'int
    qdesigner_internal::LayoutProperties::fromPropertySheet(const
    QDesignerFormEditorInterface *core, QLayout *l, int mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layoutproperties.html

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    l : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    mask : int
      Passed on as it is. May be left out, as in Qt: it is then 1048575.
    """
    #  int qdesigner_internal::LayoutProperties::fromPropertySheet(const
    #      QDesignerFormEditorInterface *core, QLayout *l, int mask)
    return self.uglySide.call(
        'ritual_ZN18qdesigner_internal16LayoutProperties17fromPropertySheet'
        'EPK28QDesignerFormEditorInterfaceP7QLayouti',
        self._addressOf(core), self._addressOf(l), mask,
    )
