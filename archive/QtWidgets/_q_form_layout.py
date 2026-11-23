"""
QFormLayout binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qformlayout.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QLayout, QLayoutItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRect, QSize
  from . import QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRect = WAIT['QRect']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFormLayout(QLayout):
  """
  The cute side of Qt's QFormLayout: a plain Python object standing in front
  of one C++ QFormLayout.

  It is built on the cute 'QLayout', as Qt's QFormLayout is built on Qt's
  QLayout, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QFormLayout that has a ritual and that Python can
  call so far, 42 names in all: 'metaObject', 'tr', 'setFieldGrowthPolicy',
  'fieldGrowthPolicy', 'setRowWrapPolicy', 'rowWrapPolicy',
  'setLabelAlignment', 'labelAlignment', 'setFormAlignment', 'formAlignment',
  'setHorizontalSpacing', 'horizontalSpacing', 'setVerticalSpacing',
  'verticalSpacing', 'spacing', 'setSpacing', 'addRow', 'insertRow',
  'removeRow', 'takeRow', 'setItem', 'setWidget', 'setLayout',
  'setRowVisible', 'isRowVisible', 'itemAt', 'labelForField', 'addItem',
  'takeAt', 'setGeometry', 'minimumSize', 'sizeHint', 'invalidate',
  'hasHeightForWidth', 'heightForWidth', 'expandingDirections', 'count',
  'rowCount', 'resetFieldGrowthPolicy', 'resetRowWrapPolicy',
  'resetLabelAlignment', 'resetFormAlignment'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFormLayout::~QFormLayout()': the destructor: Python never removes
    a C++ QFormLayout.

  What has no ritual
  ------------------

  9 of the 73 functions Qt declares: 7 takes or gives a type that cannot be
  passed yet; 1 a template; 1 declared and nowhere to be found.

  What to expect
  --------------

  - The C++ QFormLayout is created at the first use, not by
    'QFormLayout(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QFormLayout.
  - Qt tells when it has removed the C++ QFormLayout. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QFormLayout, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class FieldGrowthPolicy(CuteNum):
    """
    The enum 'QFormLayout::FieldGrowthPolicy' of Qt, with the 3 names Qt
    gives in it.
    """

    FieldsStayAtSizeHint = Kee[int](0)
    ExpandingFieldsGrow = Kee[int](1)
    AllNonFixedFieldsGrow = Kee[int](2)

  class ItemRole(CuteNum):
    """
    The enum 'QFormLayout::ItemRole' of Qt, with the 3 names Qt gives in it.
    """

    LabelRole = Kee[int](0)
    FieldRole = Kee[int](1)
    SpanningRole = Kee[int](2)

  class RowWrapPolicy(CuteNum):
    """
    The enum 'QFormLayout::RowWrapPolicy' of Qt, with the 3 names Qt gives in
    it.
    """

    DontWrapRows = Kee[int](0)
    WrapLongRows = Kee[int](1)
    WrapAllRows = Kee[int](2)

  #  The classes Qt writes inside QFormLayout, each a class in here as in
  #  C++.

  class TakeRowResult(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QFormLayout::TakeRowResult: a plain Python object
    standing in front of one C++ QFormLayout::TakeRowResult.

    C++ hands a QFormLayout::TakeRowResult around as a copy, so every C++
    QFormLayout::TakeRowResult behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QFormLayout::TakeRowResult yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QFormLayout::TakeRowResult::~TakeRowResult()': the destructor:
      Python removes its C++ QFormLayout::TakeRowResult by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QFormLayout::TakeRowResult is created at the first use, not by
      'QFormLayout::TakeRowResult(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QFormLayout::TakeRowResult back gives a copy the
      ritual made for Python, in a new cute QFormLayout::TakeRowResult.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QFormLayout::TakeRowResult'

    #  Qt's '~QFormLayout::TakeRowResult()'. Naming it makes this a value
    #  class: Python owns every C++ QFormLayout::TakeRowResult behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN11QFormLayout13TakeRowResultD1Ev'

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
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QFormLayout::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFormLayout::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QFormLayout2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFormLayout'

  #  A C++ QFormLayout Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QFormLayout'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QFormLayout::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QFormLayout::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QFormLayout10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def fieldGrowthPolicy(self) -> FieldGrowthPolicy:
    """
    Calls Qt's 'FieldGrowthPolicy QFormLayout::fieldGrowthPolicy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#fieldGrowthPolicy

    Returns
    -------

    FieldGrowthPolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'FieldGrowthPolicy(number)' gives.
    """
    #  FieldGrowthPolicy QFormLayout::fieldGrowthPolicy() const
    return QFormLayout.FieldGrowthPolicy(self.uglySide.call(
        'ritual_ZNK11QFormLayout17fieldGrowthPolicyEv',
    ))

  def rowWrapPolicy(self) -> RowWrapPolicy:
    """
    Calls Qt's 'RowWrapPolicy QFormLayout::rowWrapPolicy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#rowWrapPolicy

    Returns
    -------

    RowWrapPolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'RowWrapPolicy(number)'
      gives.
    """
    #  RowWrapPolicy QFormLayout::rowWrapPolicy() const
    return QFormLayout.RowWrapPolicy(self.uglySide.call(
        'ritual_ZNK11QFormLayout13rowWrapPolicyEv',
    ))

  def labelAlignment(self) -> Qt.Alignment:
    """
    Calls Qt's 'Qt::Alignment QFormLayout::labelAlignment() const'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#labelAlignment

    Returns
    -------

    Qt.Alignment
      The value standing for the combination Qt gave back.
    """
    #  Qt::Alignment QFormLayout::labelAlignment() const
    return Qt.Alignment(self.uglySide.call(
        'ritual_ZNK11QFormLayout14labelAlignmentEv',
    ))

  def formAlignment(self) -> Qt.Alignment:
    """
    Calls Qt's 'Qt::Alignment QFormLayout::formAlignment() const'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#formAlignment

    Returns
    -------

    Qt.Alignment
      The value standing for the combination Qt gave back.
    """
    #  Qt::Alignment QFormLayout::formAlignment() const
    return Qt.Alignment(self.uglySide.call(
        'ritual_ZNK11QFormLayout13formAlignmentEv',
    ))

  def horizontalSpacing(self) -> int:
    """
    Calls Qt's 'int QFormLayout::horizontalSpacing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#horizontalSpacing
    """
    #  int QFormLayout::horizontalSpacing() const
    return self.uglySide.call('ritual_ZNK11QFormLayout17horizontalSpacingEv')

  def verticalSpacing(self) -> int:
    """
    Calls Qt's 'int QFormLayout::verticalSpacing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#verticalSpacing
    """
    #  int QFormLayout::verticalSpacing() const
    return self.uglySide.call('ritual_ZNK11QFormLayout15verticalSpacingEv')

  def spacing(self) -> int:
    """
    Calls Qt's 'int QFormLayout::spacing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#spacing
    """
    #  int QFormLayout::spacing() const
    ritual = 'ritual_ZNK11QFormLayout7spacingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QFormLayout7spacingEv'
    return self.uglySide.call(ritual)

  @overload(int)
  def isRowVisible(self, row: int) -> bool:
    """
    Calls Qt's 'bool QFormLayout::isRowVisible(int row) const'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#isRowVisible

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  bool QFormLayout::isRowVisible(int row) const
    return self.uglySide.call('ritual_ZNK11QFormLayout12isRowVisibleEi', row)

  @overload(QWidget)
  @overload(NoneType)
  def isRowVisible(self, widget: Optional[QWidget]) -> bool:
    """
    Calls Qt's 'bool QFormLayout::isRowVisible(QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#isRowVisible

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QFormLayout::isRowVisible(QWidget *widget) const
    return self.uglySide.call(
        'ritual_ZNK11QFormLayout12isRowVisibleEP7QWidget',
        self._addressOf(widget),
    )

  @overload(QLayout)
  def isRowVisible(self, layout: Optional[QLayout]) -> bool:
    """
    Calls Qt's 'bool QFormLayout::isRowVisible(QLayout *layout) const'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#isRowVisible

    Parameters
    ----------

    layout : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QFormLayout::isRowVisible(QLayout *layout) const
    return self.uglySide.call(
        'ritual_ZNK11QFormLayout12isRowVisibleEP7QLayout',
        self._addressOf(layout),
    )

  @overload(int, ItemRole)
  def itemAt(self, row: int, role: ItemRole) -> Optional[QLayoutItem]:
    """
    Calls Qt's 'QLayoutItem *QFormLayout::itemAt(int row, ItemRole role)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#itemAt

    Parameters
    ----------

    row : int
      Passed on as it is.

    role : ItemRole
      Passed on as its number.

    Returns
    -------

    Optional[QLayoutItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLayoutItem *QFormLayout::itemAt(int row, ItemRole role) const
    address = self.uglySide.call(
        'ritual_ZNK11QFormLayout6itemAtEiNS_8ItemRoleE', row, role.value,
    )
    return QLayoutItem._cuteAt(address)

  @overload(int)
  def itemAt(self, index: int) -> Optional[QLayoutItem]:
    """
    Calls Qt's 'QLayoutItem *QFormLayout::itemAt(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#itemAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QLayoutItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLayoutItem *QFormLayout::itemAt(int index) const
    ritual = 'ritual_ZNK11QFormLayout6itemAtEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QFormLayout6itemAtEi'
    address = self.uglySide.call(ritual, index)
    return QLayoutItem._cuteAt(address)

  @overload(QWidget)
  @overload(NoneType)
  def labelForField(self, field: Optional[QWidget]) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QFormLayout::labelForField(QWidget *field) const'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#labelForField

    Parameters
    ----------

    field : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QFormLayout::labelForField(QWidget *field) const
    address = self.uglySide.call(
        'ritual_ZNK11QFormLayout13labelForFieldEP7QWidget',
        self._addressOf(field),
    )
    from . import QWidget
    return QWidget._cuteAt(address)

  @overload(QLayout)
  def labelForField(self, field: Optional[QLayout]) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QFormLayout::labelForField(QLayout *field) const'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#labelForField

    Parameters
    ----------

    field : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QFormLayout::labelForField(QLayout *field) const
    address = self.uglySide.call(
        'ritual_ZNK11QFormLayout13labelForFieldEP7QLayout',
        self._addressOf(field),
    )
    from . import QWidget
    return QWidget._cuteAt(address)

  def minimumSize(self) -> QSize:
    """
    Calls Qt's 'QSize QFormLayout::minimumSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#minimumSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QFormLayout::minimumSize() const
    ritual = 'ritual_ZNK11QFormLayout11minimumSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QFormLayout11minimumSizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QFormLayout::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QFormLayout::sizeHint() const
    ritual = 'ritual_ZNK11QFormLayout8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QFormLayout8sizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def hasHeightForWidth(self) -> bool:
    """
    Calls Qt's 'bool QFormLayout::hasHeightForWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#hasHeightForWidth
    """
    #  bool QFormLayout::hasHeightForWidth() const
    ritual = 'ritual_ZNK11QFormLayout17hasHeightForWidthEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QFormLayout17hasHeightForWidthEv'
    return self.uglySide.call(ritual)

  @overload(int)
  def heightForWidth(self, width: int) -> int:
    """
    Calls Qt's 'int QFormLayout::heightForWidth(int width) const'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#heightForWidth

    Parameters
    ----------

    width : int
      Passed on as it is.
    """
    #  int QFormLayout::heightForWidth(int width) const
    ritual = 'ritual_ZNK11QFormLayout14heightForWidthEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QFormLayout14heightForWidthEi'
    return self.uglySide.call(ritual, width)

  def expandingDirections(self) -> Qt.Orientations:
    """
    Calls Qt's 'Qt::Orientations QFormLayout::expandingDirections() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformlayout.html#expandingDirections

    Returns
    -------

    Qt.Orientations
      The value standing for the combination Qt gave back.
    """
    #  Qt::Orientations QFormLayout::expandingDirections() const
    ritual = 'ritual_ZNK11QFormLayout19expandingDirectionsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QFormLayout19expandingDirectionsEv'
    return Qt.Orientations(self.uglySide.call(ritual))

  def count(self) -> int:
    """
    Calls Qt's 'int QFormLayout::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#count
    """
    #  int QFormLayout::count() const
    ritual = 'ritual_ZNK11QFormLayout5countEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QFormLayout5countEv'
    return self.uglySide.call(ritual)

  def rowCount(self) -> int:
    """
    Calls Qt's 'int QFormLayout::rowCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#rowCount
    """
    #  int QFormLayout::rowCount() const
    return self.uglySide.call('ritual_ZNK11QFormLayout8rowCountEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(FieldGrowthPolicy)
  def setFieldGrowthPolicy(self, policy: FieldGrowthPolicy) -> None:
    """
    Calls Qt's 'void QFormLayout::setFieldGrowthPolicy(FieldGrowthPolicy
    policy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformlayout.html#setFieldGrowthPolicy

    Parameters
    ----------

    policy : FieldGrowthPolicy
      Passed on as its number.
    """
    #  void QFormLayout::setFieldGrowthPolicy(FieldGrowthPolicy policy)
    self.uglySide.call(
        'ritual_ZN11QFormLayout20setFieldGrowthPolicyENS_17FieldGrowthPolic'
        'yE',
        policy.value,
    )

  @overload(RowWrapPolicy)
  def setRowWrapPolicy(self, policy: RowWrapPolicy) -> None:
    """
    Calls Qt's 'void QFormLayout::setRowWrapPolicy(RowWrapPolicy policy)'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#setRowWrapPolicy

    Parameters
    ----------

    policy : RowWrapPolicy
      Passed on as its number.
    """
    #  void QFormLayout::setRowWrapPolicy(RowWrapPolicy policy)
    self.uglySide.call(
        'ritual_ZN11QFormLayout16setRowWrapPolicyENS_13RowWrapPolicyE',
        policy.value,
    )

  @overload(Qt.Alignment)
  def setLabelAlignment(self, alignment: Qt.Alignment) -> None:
    """
    Calls Qt's 'void QFormLayout::setLabelAlignment(Qt::Alignment
    alignment)'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#setLabelAlignment

    Parameters
    ----------

    alignment : Qt.Alignment
      Passed on as its number.
    """
    #  void QFormLayout::setLabelAlignment(Qt::Alignment alignment)
    self.uglySide.call(
        'ritual_ZN11QFormLayout17setLabelAlignmentE6QFlagsIN2Qt13AlignmentF'
        'lagEE',
        alignment.value,
    )

  @overload(Qt.Alignment)
  def setFormAlignment(self, alignment: Qt.Alignment) -> None:
    """
    Calls Qt's 'void QFormLayout::setFormAlignment(Qt::Alignment alignment)'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#setFormAlignment

    Parameters
    ----------

    alignment : Qt.Alignment
      Passed on as its number.
    """
    #  void QFormLayout::setFormAlignment(Qt::Alignment alignment)
    self.uglySide.call(
        'ritual_ZN11QFormLayout16setFormAlignmentE6QFlagsIN2Qt13AlignmentFl'
        'agEE',
        alignment.value,
    )

  @overload(int)
  def setHorizontalSpacing(self, spacing: int) -> None:
    """
    Calls Qt's 'void QFormLayout::setHorizontalSpacing(int spacing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformlayout.html#setHorizontalSpacing

    Parameters
    ----------

    spacing : int
      Passed on as it is.
    """
    #  void QFormLayout::setHorizontalSpacing(int spacing)
    self.uglySide.call(
        'ritual_ZN11QFormLayout20setHorizontalSpacingEi', spacing,
    )

  @overload(int)
  def setVerticalSpacing(self, spacing: int) -> None:
    """
    Calls Qt's 'void QFormLayout::setVerticalSpacing(int spacing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformlayout.html#setVerticalSpacing

    Parameters
    ----------

    spacing : int
      Passed on as it is.
    """
    #  void QFormLayout::setVerticalSpacing(int spacing)
    self.uglySide.call(
        'ritual_ZN11QFormLayout18setVerticalSpacingEi', spacing,
    )

  @overload(int)
  def setSpacing(self, a0: int) -> None:
    """
    Calls Qt's 'void QFormLayout::setSpacing(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#setSpacing

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QFormLayout::setSpacing(int a0)
    ritual = 'ritual_ZN11QFormLayout10setSpacingEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QFormLayout10setSpacingEi'
    self.uglySide.call(ritual, a0)

  @overload(int, ItemRole, QLayoutItem)
  @overload(int, ItemRole, NoneType)
  def setItem(
      self,
      row: int,
      role: ItemRole,
      item: Optional[QLayoutItem],
  ) -> None:
    """
    Calls Qt's 'void QFormLayout::setItem(int row, ItemRole role, QLayoutItem
    *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#setItem

    Parameters
    ----------

    row : int
      Passed on as it is.

    role : ItemRole
      Passed on as its number.

    item : Optional[QLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFormLayout::setItem(int row, ItemRole role, QLayoutItem *item)
    self.uglySide.call(
        'ritual_ZN11QFormLayout7setItemEiNS_8ItemRoleEP11QLayoutItem',
        row, role.value, self._addressOf(item, 'QLayoutItem'),
    )

  @overload(int, ItemRole, QWidget)
  @overload(int, ItemRole, NoneType)
  def setWidget(
      self,
      row: int,
      role: ItemRole,
      widget: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void QFormLayout::setWidget(int row, ItemRole role, QWidget
    *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#setWidget

    Parameters
    ----------

    row : int
      Passed on as it is.

    role : ItemRole
      Passed on as its number.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFormLayout::setWidget(int row, ItemRole role, QWidget *widget)
    self.uglySide.call(
        'ritual_ZN11QFormLayout9setWidgetEiNS_8ItemRoleEP7QWidget',
        row, role.value, self._addressOf(widget),
    )

  @overload(int, ItemRole, QLayout)
  @overload(int, ItemRole, NoneType)
  def setLayout(
      self,
      row: int,
      role: ItemRole,
      layout: Optional[QLayout],
  ) -> None:
    """
    Calls Qt's 'void QFormLayout::setLayout(int row, ItemRole role, QLayout
    *layout)'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#setLayout

    Parameters
    ----------

    row : int
      Passed on as it is.

    role : ItemRole
      Passed on as its number.

    layout : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFormLayout::setLayout(int row, ItemRole role, QLayout *layout)
    self.uglySide.call(
        'ritual_ZN11QFormLayout9setLayoutEiNS_8ItemRoleEP7QLayout',
        row, role.value, self._addressOf(layout),
    )

  @overload(int, bool)
  def setRowVisible(self, row: int, on: bool) -> None:
    """
    Calls Qt's 'void QFormLayout::setRowVisible(int row, bool on)'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#setRowVisible

    Parameters
    ----------

    row : int
      Passed on as it is.

    on : bool
      Passed on as it is.
    """
    #  void QFormLayout::setRowVisible(int row, bool on)
    self.uglySide.call('ritual_ZN11QFormLayout13setRowVisibleEib', row, on)

  @overload(QWidget, bool)
  @overload(NoneType, bool)
  def setRowVisible(self, widget: Optional[QWidget], on: bool) -> None:
    """
    Calls Qt's 'void QFormLayout::setRowVisible(QWidget *widget, bool on)'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#setRowVisible

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    on : bool
      Passed on as it is.
    """
    #  void QFormLayout::setRowVisible(QWidget *widget, bool on)
    self.uglySide.call(
        'ritual_ZN11QFormLayout13setRowVisibleEP7QWidgetb',
        self._addressOf(widget), on,
    )

  @overload(QLayout, bool)
  def setRowVisible(self, layout: Optional[QLayout], on: bool) -> None:
    """
    Calls Qt's 'void QFormLayout::setRowVisible(QLayout *layout, bool on)'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#setRowVisible

    Parameters
    ----------

    layout : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    on : bool
      Passed on as it is.
    """
    #  void QFormLayout::setRowVisible(QLayout *layout, bool on)
    self.uglySide.call(
        'ritual_ZN11QFormLayout13setRowVisibleEP7QLayoutb',
        self._addressOf(layout), on,
    )

  @overload(QRect)
  def setGeometry(self, rect: QRect) -> None:
    """
    Calls Qt's 'void QFormLayout::setGeometry(const QRect &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#setGeometry

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QFormLayout::setGeometry(const QRect &rect)
    ritual = 'ritual_ZN11QFormLayout11setGeometryERK5QRect'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QFormLayout11setGeometryERK5QRect'
    self.uglySide.call(ritual, self._valueOf(rect))

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
  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's 'QFormLayout::QFormLayout(QWidget
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#QFormLayout

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QFormLayout::QFormLayout(QWidget *parent)
    self._noteCreation(QFormLayout, lambda: Rituals.call(
        'ritual_ZN11QFormLayoutC1EP7QWidget', self._addressOf(parent),
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

  @overload(QWidget, QWidget)
  @overload(QWidget, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def addRow(
      self,
      label: Optional[QWidget],
      field: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void QFormLayout::addRow(QWidget *label, QWidget *field)'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#addRow

    Parameters
    ----------

    label : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    field : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFormLayout::addRow(QWidget *label, QWidget *field)
    self.uglySide.call(
        'ritual_ZN11QFormLayout6addRowEP7QWidgetS1_',
        self._addressOf(label), self._addressOf(field),
    )

  @overload(QWidget, QLayout)
  @overload(NoneType, QLayout)
  def addRow(
      self,
      label: Optional[QWidget],
      field: Optional[QLayout],
  ) -> None:
    """
    Calls Qt's 'void QFormLayout::addRow(QWidget *label, QLayout *field)'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#addRow

    Parameters
    ----------

    label : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    field : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFormLayout::addRow(QWidget *label, QLayout *field)
    self.uglySide.call(
        'ritual_ZN11QFormLayout6addRowEP7QWidgetP7QLayout',
        self._addressOf(label), self._addressOf(field),
    )

  @overload(str, QWidget)
  @overload(str, NoneType)
  def addRow(self, labelText: str, field: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QFormLayout::addRow(const QString &labelText, QWidget
    *field)'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#addRow

    Parameters
    ----------

    labelText : str
      Passed on as it is: a QString is made of it for the call.

    field : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFormLayout::addRow(const QString &labelText, QWidget *field)
    self.uglySide.call(
        'ritual_ZN11QFormLayout6addRowERK7QStringP7QWidget',
        labelText, self._addressOf(field),
    )

  @overload(str, QLayout)
  def addRow(self, labelText: str, field: Optional[QLayout]) -> None:
    """
    Calls Qt's 'void QFormLayout::addRow(const QString &labelText, QLayout
    *field)'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#addRow

    Parameters
    ----------

    labelText : str
      Passed on as it is: a QString is made of it for the call.

    field : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFormLayout::addRow(const QString &labelText, QLayout *field)
    self.uglySide.call(
        'ritual_ZN11QFormLayout6addRowERK7QStringP7QLayout',
        labelText, self._addressOf(field),
    )

  @overload(QWidget)
  @overload(NoneType)
  def addRow(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QFormLayout::addRow(QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#addRow

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFormLayout::addRow(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN11QFormLayout6addRowEP7QWidget', self._addressOf(widget),
    )

  @overload(QLayout)
  def addRow(self, layout: Optional[QLayout]) -> None:
    """
    Calls Qt's 'void QFormLayout::addRow(QLayout *layout)'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#addRow

    Parameters
    ----------

    layout : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFormLayout::addRow(QLayout *layout)
    self.uglySide.call(
        'ritual_ZN11QFormLayout6addRowEP7QLayout', self._addressOf(layout),
    )

  @overload(int, QWidget, QWidget)
  @overload(int, QWidget, NoneType)
  @overload(int, NoneType, QWidget)
  @overload(int, NoneType, NoneType)
  def insertRow(
      self,
      row: int,
      label: Optional[QWidget],
      field: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void QFormLayout::insertRow(int row, QWidget *label, QWidget
    *field)'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#insertRow

    Parameters
    ----------

    row : int
      Passed on as it is.

    label : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    field : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFormLayout::insertRow(int row, QWidget *label, QWidget *field)
    self.uglySide.call(
        'ritual_ZN11QFormLayout9insertRowEiP7QWidgetS1_',
        row, self._addressOf(label), self._addressOf(field),
    )

  @overload(int, QWidget, QLayout)
  @overload(int, NoneType, QLayout)
  def insertRow(
      self,
      row: int,
      label: Optional[QWidget],
      field: Optional[QLayout],
  ) -> None:
    """
    Calls Qt's 'void QFormLayout::insertRow(int row, QWidget *label, QLayout
    *field)'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#insertRow

    Parameters
    ----------

    row : int
      Passed on as it is.

    label : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    field : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFormLayout::insertRow(int row, QWidget *label, QLayout *field)
    self.uglySide.call(
        'ritual_ZN11QFormLayout9insertRowEiP7QWidgetP7QLayout',
        row, self._addressOf(label), self._addressOf(field),
    )

  @overload(int, str, QWidget)
  @overload(int, str, NoneType)
  def insertRow(
      self,
      row: int,
      labelText: str,
      field: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void QFormLayout::insertRow(int row, const QString
    &labelText, QWidget *field)'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#insertRow

    Parameters
    ----------

    row : int
      Passed on as it is.

    labelText : str
      Passed on as it is: a QString is made of it for the call.

    field : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFormLayout::insertRow(int row, const QString &labelText, QWidget
    #      *field)
    self.uglySide.call(
        'ritual_ZN11QFormLayout9insertRowEiRK7QStringP7QWidget',
        row, labelText, self._addressOf(field),
    )

  @overload(int, str, QLayout)
  def insertRow(
      self,
      row: int,
      labelText: str,
      field: Optional[QLayout],
  ) -> None:
    """
    Calls Qt's 'void QFormLayout::insertRow(int row, const QString
    &labelText, QLayout *field)'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#insertRow

    Parameters
    ----------

    row : int
      Passed on as it is.

    labelText : str
      Passed on as it is: a QString is made of it for the call.

    field : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFormLayout::insertRow(int row, const QString &labelText, QLayout
    #      *field)
    self.uglySide.call(
        'ritual_ZN11QFormLayout9insertRowEiRK7QStringP7QLayout',
        row, labelText, self._addressOf(field),
    )

  @overload(int, QWidget)
  @overload(int, NoneType)
  def insertRow(self, row: int, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QFormLayout::insertRow(int row, QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#insertRow

    Parameters
    ----------

    row : int
      Passed on as it is.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFormLayout::insertRow(int row, QWidget *widget)
    self.uglySide.call(
        'ritual_ZN11QFormLayout9insertRowEiP7QWidget',
        row, self._addressOf(widget),
    )

  @overload(int, QLayout)
  def insertRow(self, row: int, layout: Optional[QLayout]) -> None:
    """
    Calls Qt's 'void QFormLayout::insertRow(int row, QLayout *layout)'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#insertRow

    Parameters
    ----------

    row : int
      Passed on as it is.

    layout : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFormLayout::insertRow(int row, QLayout *layout)
    self.uglySide.call(
        'ritual_ZN11QFormLayout9insertRowEiP7QLayout',
        row, self._addressOf(layout),
    )

  @overload(int)
  def removeRow(self, row: int) -> None:
    """
    Calls Qt's 'void QFormLayout::removeRow(int row)'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#removeRow

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  void QFormLayout::removeRow(int row)
    self.uglySide.call('ritual_ZN11QFormLayout9removeRowEi', row)

  @overload(QWidget)
  @overload(NoneType)
  def removeRow(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QFormLayout::removeRow(QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#removeRow

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFormLayout::removeRow(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN11QFormLayout9removeRowEP7QWidget',
        self._addressOf(widget),
    )

  @overload(QLayout)
  def removeRow(self, layout: Optional[QLayout]) -> None:
    """
    Calls Qt's 'void QFormLayout::removeRow(QLayout *layout)'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#removeRow

    Parameters
    ----------

    layout : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFormLayout::removeRow(QLayout *layout)
    self.uglySide.call(
        'ritual_ZN11QFormLayout9removeRowEP7QLayout',
        self._addressOf(layout),
    )

  @overload(int)
  def takeRow(self, row: int) -> TakeRowResult:
    """
    Calls Qt's 'TakeRowResult QFormLayout::takeRow(int row)'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#takeRow

    Parameters
    ----------

    row : int
      Passed on as it is.

    Returns
    -------

    TakeRowResult
      A new cute QFormLayout::TakeRowResult around the copy Qt gave back.
      Python owns it.
    """
    #  TakeRowResult QFormLayout::takeRow(int row)
    address = self.uglySide.call('ritual_ZN11QFormLayout7takeRowEi', row)
    return QFormLayout.TakeRowResult._cuteOwning(address)

  @overload(QWidget)
  @overload(NoneType)
  def takeRow(self, widget: Optional[QWidget]) -> TakeRowResult:
    """
    Calls Qt's 'TakeRowResult QFormLayout::takeRow(QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#takeRow

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    TakeRowResult
      A new cute QFormLayout::TakeRowResult around the copy Qt gave back.
      Python owns it.
    """
    #  TakeRowResult QFormLayout::takeRow(QWidget *widget)
    address = self.uglySide.call(
        'ritual_ZN11QFormLayout7takeRowEP7QWidget', self._addressOf(widget),
    )
    return QFormLayout.TakeRowResult._cuteOwning(address)

  @overload(QLayout)
  def takeRow(self, layout: Optional[QLayout]) -> TakeRowResult:
    """
    Calls Qt's 'TakeRowResult QFormLayout::takeRow(QLayout *layout)'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#takeRow

    Parameters
    ----------

    layout : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    TakeRowResult
      A new cute QFormLayout::TakeRowResult around the copy Qt gave back.
      Python owns it.
    """
    #  TakeRowResult QFormLayout::takeRow(QLayout *layout)
    address = self.uglySide.call(
        'ritual_ZN11QFormLayout7takeRowEP7QLayout', self._addressOf(layout),
    )
    return QFormLayout.TakeRowResult._cuteOwning(address)

  @overload(QLayoutItem)
  @overload(NoneType)
  def addItem(self, item: Optional[QLayoutItem]) -> None:
    """
    Calls Qt's 'void QFormLayout::addItem(QLayoutItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#addItem

    Parameters
    ----------

    item : Optional[QLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFormLayout::addItem(QLayoutItem *item)
    ritual = 'ritual_ZN11QFormLayout7addItemEP11QLayoutItem'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QFormLayout7addItemEP11QLayoutItem'
    self.uglySide.call(ritual, self._addressOf(item, 'QLayoutItem'))

  @overload(int)
  def takeAt(self, index: int) -> Optional[QLayoutItem]:
    """
    Calls Qt's 'QLayoutItem *QFormLayout::takeAt(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#takeAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QLayoutItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLayoutItem *QFormLayout::takeAt(int index)
    ritual = 'ritual_ZN11QFormLayout6takeAtEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QFormLayout6takeAtEi'
    address = self.uglySide.call(ritual, index)
    return QLayoutItem._cuteAt(address)

  def invalidate(self) -> None:
    """
    Calls Qt's 'void QFormLayout::invalidate()'.

    Qt's own words: https://doc.qt.io/qt-6/qformlayout.html#invalidate
    """
    #  void QFormLayout::invalidate()
    ritual = 'ritual_ZN11QFormLayout10invalidateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QFormLayout10invalidateEv'
    self.uglySide.call(ritual)

  def resetFieldGrowthPolicy(self) -> None:
    """
    Calls Qt's 'void QFormLayout::resetFieldGrowthPolicy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformlayout.html#resetFieldGrowthPolicy
    """
    #  void QFormLayout::resetFieldGrowthPolicy()
    self.uglySide.call('ritual_ZN11QFormLayout22resetFieldGrowthPolicyEv')

  def resetRowWrapPolicy(self) -> None:
    """
    Calls Qt's 'void QFormLayout::resetRowWrapPolicy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformlayout.html#resetRowWrapPolicy
    """
    #  void QFormLayout::resetRowWrapPolicy()
    self.uglySide.call('ritual_ZN11QFormLayout18resetRowWrapPolicyEv')

  def resetLabelAlignment(self) -> None:
    """
    Calls Qt's 'void QFormLayout::resetLabelAlignment()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformlayout.html#resetLabelAlignment
    """
    #  void QFormLayout::resetLabelAlignment()
    self.uglySide.call('ritual_ZN11QFormLayout19resetLabelAlignmentEv')

  def resetFormAlignment(self) -> None:
    """
    Calls Qt's 'void QFormLayout::resetFormAlignment()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qformlayout.html#resetFormAlignment
    """
    #  void QFormLayout::resetFormAlignment()
    self.uglySide.call('ritual_ZN11QFormLayout18resetFormAlignmentEv')
