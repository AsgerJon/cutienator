"""
QLayout binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qlayout.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from . import QLayoutItem, QSizePolicy

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QChildEvent, QEvent, QMargins, QMetaObject, QRect
  from ..QtCore import QSize
  from . import QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QChildEvent = WAIT['QChildEvent']
  QEvent = WAIT['QEvent']
  QMargins = WAIT['QMargins']
  QRect = WAIT['QRect']
  QSize = WAIT['QSize']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLayout(QObject, QLayoutItem):
  """
  The cute side of Qt's QLayout: a plain Python object standing in front of
  one C++ QLayout.

  It is built on the cute 'QObject', as Qt's QLayout is built on Qt's
  QObject, and has everything that class has. It is built on the cute
  'QLayoutItem' as well, as Qt's QLayout is built on Qt's QLayoutItem too,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QLayout that has a ritual and that Python can call
  so far, 54 names in all: 'metaObject', 'tr', 'spacing', 'setSpacing',
  'setContentsMargins', 'unsetContentsMargins', 'contentsMargins',
  'contentsRect', 'setAlignment', 'setSizeConstraint', 'sizeConstraint',
  'setSizeConstraints', 'setHorizontalSizeConstraint',
  'horizontalSizeConstraint', 'setVerticalSizeConstraint',
  'verticalSizeConstraint', 'setMenuBar', 'menuBar', 'parentWidget',
  'invalidate', 'geometry', 'activate', 'update', 'addWidget', 'addItem',
  'removeWidget', 'removeItem', 'expandingDirections', 'minimumSize',
  'maximumSize', 'setGeometry', 'itemAt', 'takeAt', 'indexOf', 'count',
  'isEmpty', 'controlTypes', 'replaceWidget', 'totalMinimumHeightForWidth',
  'totalHeightForWidth', 'totalMinimumSize', 'totalMaximumSize',
  'totalSizeHint', 'layout', 'setEnabled', 'isEnabled',
  'closestAcceptableSize', 'widgetEvent', 'childEvent', 'addChildLayout',
  'addChildWidget', 'adoptLayout', 'alignmentRect',
  'activateRecursiveHelper'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QLayout::~QLayout()': the destructor: Python never removes a C++
    QLayout.
  - Qt's 'void QLayout::getContentsMargins(int *left, int *top, int *right,
    int *bottom) const': takes a number to change where it is.

  What has no ritual
  ------------------

  10 of the 69 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet; 2 the class is abstract, so C++ cannot make one; 2 forbidden; 1
  a template; 1 declared and nowhere to be found.

  What to expect
  --------------

  - The C++ QLayout is created at the first use, not by 'QLayout(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QLayout.
  - Qt tells when it has removed the C++ QLayout. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QLayout, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class SizeConstraint(CuteNum):
    """
    The enum 'QLayout::SizeConstraint' of Qt, with the 6 names Qt gives in
    it.
    """

    SetDefaultConstraint = Kee[int](0)
    SetNoConstraint = Kee[int](1)
    SetMinimumSize = Kee[int](2)
    SetFixedSize = Kee[int](3)
    SetMaximumSize = Kee[int](4)
    SetMinAndMaxSize = Kee[int](5)

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
    Calls Qt's 'QString QLayout::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#tr

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
    #  QString QLayout::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN7QLayout2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QWidget, QSize)
  @overload(NoneType, QSize)
  def closestAcceptableSize(w: Optional[QWidget], s: QSize) -> QSize:
    """
    Calls Qt's 'QSize QLayout::closestAcceptableSize(const QWidget *w, const
    QSize &s)'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#closestAcceptableSize

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    s : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QLayout::closestAcceptableSize(const QWidget *w, const QSize &s)
    address = Rituals.call(
        'ritual_ZN7QLayout21closestAcceptableSizeEPK7QWidgetRK5QSize',
        CuteMixin._addressOf(w), CuteMixin._valueOf(s),
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @staticmethod
  @overload(QLayoutItem)
  @overload(NoneType)
  def activateRecursiveHelper(item: Optional[QLayoutItem]) -> None:
    """
    Calls Qt's 'void QLayout::activateRecursiveHelper(QLayoutItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlayout.html#activateRecursiveHelper

    Parameters
    ----------

    item : Optional[QLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLayout::activateRecursiveHelper(QLayoutItem *item)
    Rituals.call(
        'ritual_ZN7QLayout23activateRecursiveHelperEP11QLayoutItem',
        CuteMixin._addressOf(item, 'QLayoutItem'),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLayout'

  #  Qt's QLayout is built on more than one class. The part of a C++ QLayout
  #  that belongs to a class after the first begins somewhere inside the
  #  object, and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QLayoutItem': 'ritual_cast_QLayout_QLayoutItem',
  }

  #  A C++ QLayout Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLayout'

  #  The functions Qt calls itself that QLayout is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'spacing': (
          ('_ZNK7QLayout7spacingEv',
           ('int', 'number', ''),
           ()),
      ),
      'setSpacing': (
          ('_ZN7QLayout10setSpacingEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'addItem': (
          ('_ZN7QLayout7addItemEP11QLayoutItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QLayoutItem'),
           )),
      ),
      'itemAt': (
          ('_ZNK7QLayout6itemAtEi',
           ('address', 'address', 'QtWidgets:QLayoutItem'),
           (
               ('int', 'number', ''),
           )),
      ),
      'takeAt': (
          ('_ZN7QLayout6takeAtEi',
           ('address', 'address', 'QtWidgets:QLayoutItem'),
           (
               ('int', 'number', ''),
           )),
      ),
      'indexOf': (
          ('_ZNK7QLayout7indexOfEPK7QWidget',
           ('int', 'number', ''),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
          ('_ZNK7QLayout7indexOfEPK11QLayoutItem',
           ('int', 'number', ''),
           (
               ('address', 'address', 'QtWidgets:QLayoutItem'),
           )),
      ),
      'count': (
          ('_ZNK7QLayout5countEv',
           ('int', 'number', ''),
           ()),
      ),
      'replaceWidget': (
          ('_ZN7QLayout13replaceWidgetEP7QWidgetS1_6QFlagsIN2Qt15FindChildO'
           'ptionEE',
           ('address', 'address', 'QtWidgets:QLayoutItem'),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
               ('address', 'address', 'QtWidgets:QWidget'),
               ('int', 'flags', 'QtCore:Qt.FindChildOption'),
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QLayout::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QLayout::metaObject() const
    address = self.uglySide.call('ritual_ZNK7QLayout10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def spacing(self) -> int:
    """
    Calls Qt's 'int QLayout::spacing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#spacing
    """
    #  int QLayout::spacing() const
    ritual = 'ritual_ZNK7QLayout7spacingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK7QLayout7spacingEv'
    return self.uglySide.call(ritual)

  def contentsMargins(self) -> QMargins:
    """
    Calls Qt's 'QMargins QLayout::contentsMargins() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#contentsMargins

    Returns
    -------

    QMargins
      A new cute QMargins around the copy Qt gave back. Python owns it.
    """
    #  QMargins QLayout::contentsMargins() const
    address = self.uglySide.call('ritual_ZNK7QLayout15contentsMarginsEv')
    from ..QtCore import QMargins
    return QMargins._cuteOwning(address)

  def contentsRect(self) -> QRect:
    """
    Calls Qt's 'QRect QLayout::contentsRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#contentsRect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QLayout::contentsRect() const
    address = self.uglySide.call('ritual_ZNK7QLayout12contentsRectEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def sizeConstraint(self) -> SizeConstraint:
    """
    Calls Qt's 'SizeConstraint QLayout::sizeConstraint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#sizeConstraint

    Returns
    -------

    SizeConstraint
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SizeConstraint(number)'
      gives.
    """
    #  SizeConstraint QLayout::sizeConstraint() const
    return QLayout.SizeConstraint(self.uglySide.call(
        'ritual_ZNK7QLayout14sizeConstraintEv',
    ))

  def horizontalSizeConstraint(self) -> SizeConstraint:
    """
    Calls Qt's 'SizeConstraint QLayout::horizontalSizeConstraint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlayout.html#horizontalSizeConstraint

    Returns
    -------

    SizeConstraint
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SizeConstraint(number)'
      gives.
    """
    #  SizeConstraint QLayout::horizontalSizeConstraint() const
    return QLayout.SizeConstraint(self.uglySide.call(
        'ritual_ZNK7QLayout24horizontalSizeConstraintEv',
    ))

  def verticalSizeConstraint(self) -> SizeConstraint:
    """
    Calls Qt's 'SizeConstraint QLayout::verticalSizeConstraint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlayout.html#verticalSizeConstraint

    Returns
    -------

    SizeConstraint
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SizeConstraint(number)'
      gives.
    """
    #  SizeConstraint QLayout::verticalSizeConstraint() const
    return QLayout.SizeConstraint(self.uglySide.call(
        'ritual_ZNK7QLayout22verticalSizeConstraintEv',
    ))

  def menuBar(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QLayout::menuBar() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#menuBar

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QLayout::menuBar() const
    address = self.uglySide.call('ritual_ZNK7QLayout7menuBarEv')
    from . import QWidget
    return QWidget._cuteAt(address)

  def parentWidget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QLayout::parentWidget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#parentWidget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QLayout::parentWidget() const
    address = self.uglySide.call('ritual_ZNK7QLayout12parentWidgetEv')
    from . import QWidget
    return QWidget._cuteAt(address)

  def geometry(self) -> QRect:
    """
    Calls Qt's 'QRect QLayout::geometry() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#geometry

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QLayout::geometry() const
    ritual = 'ritual_ZNK7QLayout8geometryEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK7QLayout8geometryEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def expandingDirections(self) -> Qt.Orientations:
    """
    Calls Qt's 'Qt::Orientations QLayout::expandingDirections() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#expandingDirections

    Returns
    -------

    Qt.Orientations
      The value standing for the combination Qt gave back.
    """
    #  Qt::Orientations QLayout::expandingDirections() const
    ritual = 'ritual_ZNK7QLayout19expandingDirectionsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK7QLayout19expandingDirectionsEv'
    return Qt.Orientations(self.uglySide.call(ritual))

  def minimumSize(self) -> QSize:
    """
    Calls Qt's 'QSize QLayout::minimumSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#minimumSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QLayout::minimumSize() const
    ritual = 'ritual_ZNK7QLayout11minimumSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK7QLayout11minimumSizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def maximumSize(self) -> QSize:
    """
    Calls Qt's 'QSize QLayout::maximumSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#maximumSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QLayout::maximumSize() const
    ritual = 'ritual_ZNK7QLayout11maximumSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK7QLayout11maximumSizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(int)
  def itemAt(self, index: int) -> Optional[QLayoutItem]:
    """
    Calls Qt's 'QLayoutItem *QLayout::itemAt(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#itemAt

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
    #  QLayoutItem *QLayout::itemAt(int index) const
    address = self.uglySide.call('ritual_ZNK7QLayout6itemAtEi', index)
    return QLayoutItem._cuteAt(address)

  @overload(QWidget)
  @overload(NoneType)
  def indexOf(self, a0: Optional[QWidget]) -> int:
    """
    Calls Qt's 'int QLayout::indexOf(const QWidget *a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#indexOf

    Parameters
    ----------

    a0 : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QLayout::indexOf(const QWidget *a0) const
    ritual = 'ritual_ZNK7QLayout7indexOfEPK7QWidget'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK7QLayout7indexOfEPK7QWidget'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QLayoutItem)
  def indexOf(self, a0: Optional[QLayoutItem]) -> int:
    """
    Calls Qt's 'int QLayout::indexOf(const QLayoutItem *a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#indexOf

    Parameters
    ----------

    a0 : Optional[QLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QLayout::indexOf(const QLayoutItem *a0) const
    ritual = 'ritual_ZNK7QLayout7indexOfEPK11QLayoutItem'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK7QLayout7indexOfEPK11QLayoutItem'
    return self.uglySide.call(ritual, self._addressOf(a0, 'QLayoutItem'))

  def count(self) -> int:
    """
    Calls Qt's 'int QLayout::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#count
    """
    #  int QLayout::count() const
    return self.uglySide.call('ritual_ZNK7QLayout5countEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QLayout::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#isEmpty
    """
    #  bool QLayout::isEmpty() const
    ritual = 'ritual_ZNK7QLayout7isEmptyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK7QLayout7isEmptyEv'
    return self.uglySide.call(ritual)

  def controlTypes(self) -> QSizePolicy.ControlTypes:
    """
    Calls Qt's 'QSizePolicy::ControlTypes QLayout::controlTypes() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#controlTypes

    Returns
    -------

    QSizePolicy.ControlTypes
      The value standing for the combination Qt gave back.
    """
    #  QSizePolicy::ControlTypes QLayout::controlTypes() const
    ritual = 'ritual_ZNK7QLayout12controlTypesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK7QLayout12controlTypesEv'
    return QSizePolicy.ControlTypes(self.uglySide.call(ritual))

  @overload(int)
  def totalMinimumHeightForWidth(self, w: int) -> int:
    """
    Calls Qt's 'int QLayout::totalMinimumHeightForWidth(int w) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlayout.html#totalMinimumHeightForWidth

    Parameters
    ----------

    w : int
      Passed on as it is.
    """
    #  int QLayout::totalMinimumHeightForWidth(int w) const
    return self.uglySide.call(
        'ritual_ZNK7QLayout26totalMinimumHeightForWidthEi', w,
    )

  @overload(int)
  def totalHeightForWidth(self, w: int) -> int:
    """
    Calls Qt's 'int QLayout::totalHeightForWidth(int w) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#totalHeightForWidth

    Parameters
    ----------

    w : int
      Passed on as it is.
    """
    #  int QLayout::totalHeightForWidth(int w) const
    return self.uglySide.call('ritual_ZNK7QLayout19totalHeightForWidthEi', w)

  def totalMinimumSize(self) -> QSize:
    """
    Calls Qt's 'QSize QLayout::totalMinimumSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#totalMinimumSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QLayout::totalMinimumSize() const
    address = self.uglySide.call('ritual_ZNK7QLayout16totalMinimumSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def totalMaximumSize(self) -> QSize:
    """
    Calls Qt's 'QSize QLayout::totalMaximumSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#totalMaximumSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QLayout::totalMaximumSize() const
    address = self.uglySide.call('ritual_ZNK7QLayout16totalMaximumSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def totalSizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QLayout::totalSizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#totalSizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QLayout::totalSizeHint() const
    address = self.uglySide.call('ritual_ZNK7QLayout13totalSizeHintEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def isEnabled(self) -> bool:
    """
    Calls Qt's 'bool QLayout::isEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#isEnabled
    """
    #  bool QLayout::isEnabled() const
    return self.uglySide.call('ritual_ZNK7QLayout9isEnabledEv')

  @overload(QRect)
  def alignmentRect(self, a0: QRect) -> QRect:
    """
    Calls Qt's 'QRect QLayout::alignmentRect(const QRect &a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#alignmentRect

    Parameters
    ----------

    a0 : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QLayout::alignmentRect(const QRect &a0) const
    address = self.uglySide.call(
        'ritual_ZNK7QLayout13alignmentRectERK5QRect', self._valueOf(a0),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setSpacing(self, a0: int) -> None:
    """
    Calls Qt's 'void QLayout::setSpacing(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#setSpacing

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QLayout::setSpacing(int a0)
    ritual = 'ritual_ZN7QLayout10setSpacingEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QLayout10setSpacingEi'
    self.uglySide.call(ritual, a0)

  @overload(int, int, int, int)
  def setContentsMargins(
      self,
      left: int,
      top: int,
      right: int,
      bottom: int,
  ) -> None:
    """
    Calls Qt's 'void QLayout::setContentsMargins(int left, int top, int
    right, int bottom)'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#setContentsMargins

    Parameters
    ----------

    left : int
      Passed on as it is.

    top : int
      Passed on as it is.

    right : int
      Passed on as it is.

    bottom : int
      Passed on as it is.
    """
    #  void QLayout::setContentsMargins(int left, int top, int right, int
    #      bottom)
    self.uglySide.call(
        'ritual_ZN7QLayout18setContentsMarginsEiiii',
        left, top, right, bottom,
    )

  @overload(QMargins)
  def setContentsMargins(self, margins: QMargins) -> None:
    """
    Calls Qt's 'void QLayout::setContentsMargins(const QMargins &margins)'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#setContentsMargins

    Parameters
    ----------

    margins : QMargins
      Passed on as a value: Qt reads the C++ QMargins, which stays Python's
      own.
    """
    #  void QLayout::setContentsMargins(const QMargins &margins)
    self.uglySide.call(
        'ritual_ZN7QLayout18setContentsMarginsERK8QMargins',
        self._valueOf(margins),
    )

  @overload(QWidget, Qt.Alignment)
  @overload(NoneType, Qt.Alignment)
  def setAlignment(
      self,
      w: Optional[QWidget],
      alignment: Qt.Alignment,
  ) -> bool:
    """
    Calls Qt's 'bool QLayout::setAlignment(QWidget *w, Qt::Alignment
    alignment)'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#setAlignment

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    alignment : Qt.Alignment
      Passed on as its number.
    """
    #  bool QLayout::setAlignment(QWidget *w, Qt::Alignment alignment)
    return self.uglySide.call(
        'ritual_ZN7QLayout12setAlignmentEP7QWidget6QFlagsIN2Qt13AlignmentFl'
        'agEE',
        self._addressOf(w), alignment.value,
    )

  @overload(THIS, Qt.Alignment)
  def setAlignment(
      self,
      l: Optional[QLayout],
      alignment: Qt.Alignment,
  ) -> bool:
    """
    Calls Qt's 'bool QLayout::setAlignment(QLayout *l, Qt::Alignment
    alignment)'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#setAlignment

    Parameters
    ----------

    l : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    alignment : Qt.Alignment
      Passed on as its number.
    """
    #  bool QLayout::setAlignment(QLayout *l, Qt::Alignment alignment)
    return self.uglySide.call(
        'ritual_ZN7QLayout12setAlignmentEPS_6QFlagsIN2Qt13AlignmentFlagEE',
        self._addressOf(l), alignment.value,
    )

  @overload(SizeConstraint)
  def setSizeConstraint(self, constraint: SizeConstraint) -> None:
    """
    Calls Qt's 'void QLayout::setSizeConstraint(SizeConstraint constraint)'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#setSizeConstraint

    Parameters
    ----------

    constraint : SizeConstraint
      Passed on as its number.
    """
    #  void QLayout::setSizeConstraint(SizeConstraint constraint)
    self.uglySide.call(
        'ritual_ZN7QLayout17setSizeConstraintENS_14SizeConstraintE',
        constraint.value,
    )

  @overload(SizeConstraint, SizeConstraint)
  def setSizeConstraints(
      self,
      horizontal: SizeConstraint,
      vertical: SizeConstraint,
  ) -> None:
    """
    Calls Qt's 'void QLayout::setSizeConstraints(SizeConstraint horizontal,
    SizeConstraint vertical)'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#setSizeConstraints

    Parameters
    ----------

    horizontal : SizeConstraint
      Passed on as its number.

    vertical : SizeConstraint
      Passed on as its number.
    """
    #  void QLayout::setSizeConstraints(SizeConstraint horizontal,
    #      SizeConstraint vertical)
    self.uglySide.call(
        'ritual_ZN7QLayout18setSizeConstraintsENS_14SizeConstraintES0_',
        horizontal.value, vertical.value,
    )

  @overload(SizeConstraint)
  def setHorizontalSizeConstraint(self, constraint: SizeConstraint) -> None:
    """
    Calls Qt's 'void QLayout::setHorizontalSizeConstraint(SizeConstraint
    constraint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlayout.html#setHorizontalSizeConstraint

    Parameters
    ----------

    constraint : SizeConstraint
      Passed on as its number.
    """
    #  void QLayout::setHorizontalSizeConstraint(SizeConstraint constraint)
    self.uglySide.call(
        'ritual_ZN7QLayout27setHorizontalSizeConstraintENS_14SizeConstraint'
        'E',
        constraint.value,
    )

  @overload(SizeConstraint)
  def setVerticalSizeConstraint(self, constraint: SizeConstraint) -> None:
    """
    Calls Qt's 'void QLayout::setVerticalSizeConstraint(SizeConstraint
    constraint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlayout.html#setVerticalSizeConstraint

    Parameters
    ----------

    constraint : SizeConstraint
      Passed on as its number.
    """
    #  void QLayout::setVerticalSizeConstraint(SizeConstraint constraint)
    self.uglySide.call(
        'ritual_ZN7QLayout25setVerticalSizeConstraintENS_14SizeConstraintE',
        constraint.value,
    )

  @overload(QWidget)
  @overload(NoneType)
  def setMenuBar(self, w: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QLayout::setMenuBar(QWidget *w)'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#setMenuBar

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLayout::setMenuBar(QWidget *w)
    self.uglySide.call(
        'ritual_ZN7QLayout10setMenuBarEP7QWidget', self._addressOf(w),
    )

  @overload(QRect)
  def setGeometry(self, a0: QRect) -> None:
    """
    Calls Qt's 'void QLayout::setGeometry(const QRect &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#setGeometry

    Parameters
    ----------

    a0 : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QLayout::setGeometry(const QRect &a0)
    ritual = 'ritual_ZN7QLayout11setGeometryERK5QRect'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QLayout11setGeometryERK5QRect'
    self.uglySide.call(ritual, self._valueOf(a0))

  @overload(bool)
  def setEnabled(self, a0: bool) -> None:
    """
    Calls Qt's 'void QLayout::setEnabled(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#setEnabled

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QLayout::setEnabled(bool a0)
    self.uglySide.call('ritual_ZN7QLayout10setEnabledEb', a0)

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

  def unsetContentsMargins(self) -> None:
    """
    Calls Qt's 'void QLayout::unsetContentsMargins()'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#unsetContentsMargins
    """
    #  void QLayout::unsetContentsMargins()
    self.uglySide.call('ritual_ZN7QLayout20unsetContentsMarginsEv')

  def invalidate(self) -> None:
    """
    Calls Qt's 'void QLayout::invalidate()'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#invalidate
    """
    #  void QLayout::invalidate()
    ritual = 'ritual_ZN7QLayout10invalidateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QLayout10invalidateEv'
    self.uglySide.call(ritual)

  def activate(self) -> bool:
    """
    Calls Qt's 'bool QLayout::activate()'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#activate
    """
    #  bool QLayout::activate()
    return self.uglySide.call('ritual_ZN7QLayout8activateEv')

  def update(self) -> None:
    """
    Calls Qt's 'void QLayout::update()'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#update
    """
    #  void QLayout::update()
    self.uglySide.call('ritual_ZN7QLayout6updateEv')

  @overload(QWidget)
  @overload(NoneType)
  def addWidget(self, w: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QLayout::addWidget(QWidget *w)'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#addWidget

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLayout::addWidget(QWidget *w)
    self.uglySide.call(
        'ritual_ZN7QLayout9addWidgetEP7QWidget', self._addressOf(w),
    )

  @overload(QLayoutItem)
  @overload(NoneType)
  def addItem(self, a0: Optional[QLayoutItem]) -> None:
    """
    Calls Qt's 'void QLayout::addItem(QLayoutItem *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#addItem

    Parameters
    ----------

    a0 : Optional[QLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLayout::addItem(QLayoutItem *a0)
    self.uglySide.call(
        'ritual_ZN7QLayout7addItemEP11QLayoutItem',
        self._addressOf(a0, 'QLayoutItem'),
    )

  @overload(QWidget)
  @overload(NoneType)
  def removeWidget(self, w: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QLayout::removeWidget(QWidget *w)'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#removeWidget

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLayout::removeWidget(QWidget *w)
    self.uglySide.call(
        'ritual_ZN7QLayout12removeWidgetEP7QWidget', self._addressOf(w),
    )

  @overload(QLayoutItem)
  @overload(NoneType)
  def removeItem(self, a0: Optional[QLayoutItem]) -> None:
    """
    Calls Qt's 'void QLayout::removeItem(QLayoutItem *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#removeItem

    Parameters
    ----------

    a0 : Optional[QLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLayout::removeItem(QLayoutItem *a0)
    self.uglySide.call(
        'ritual_ZN7QLayout10removeItemEP11QLayoutItem',
        self._addressOf(a0, 'QLayoutItem'),
    )

  @overload(int)
  def takeAt(self, index: int) -> Optional[QLayoutItem]:
    """
    Calls Qt's 'QLayoutItem *QLayout::takeAt(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#takeAt

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
    #  QLayoutItem *QLayout::takeAt(int index)
    address = self.uglySide.call('ritual_ZN7QLayout6takeAtEi', index)
    return QLayoutItem._cuteAt(address)

  @overload(QWidget, QWidget)
  @overload(QWidget, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  @overload(QWidget, QWidget, Qt.FindChildOptions)
  @overload(QWidget, NoneType, Qt.FindChildOptions)
  @overload(NoneType, QWidget, Qt.FindChildOptions)
  @overload(NoneType, NoneType, Qt.FindChildOptions)
  def replaceWidget(
      self,
      from_: Optional[QWidget],
      to: Optional[QWidget],
      options: Qt.FindChildOptions = (
          Qt.FindChildOptions.FindChildrenRecursively),
  ) -> Optional[QLayoutItem]:
    """
    Calls Qt's 'QLayoutItem *QLayout::replaceWidget(QWidget *from, QWidget
    *to, Qt::FindChildOptions options)'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#replaceWidget

    Parameters
    ----------

    from_ : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    to : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    options : Qt.FindChildOptions
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.FindChildOptions.FindChildrenRecursively.

    Returns
    -------

    Optional[QLayoutItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLayoutItem *QLayout::replaceWidget(QWidget *from, QWidget *to,
    #      Qt::FindChildOptions options)
    ritual = (
        'ritual_ZN7QLayout13replaceWidgetEP7QWidgetS1_6QFlagsIN2Qt15FindChi'
        'ldOptionEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN7QLayout13replaceWidgetEP7QWidgetS1_6QFlagsIN2Qt15F'
          'indChildOptionEE')
    address = self.uglySide.call(
        ritual, self._addressOf(from_), self._addressOf(to), options.value,
    )
    return QLayoutItem._cuteAt(address)

  def layout(self) -> Optional[QLayout]:
    """
    Calls Qt's 'QLayout *QLayout::layout()'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#layout

    Returns
    -------

    Optional[QLayout]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLayout *QLayout::layout()
    ritual = 'ritual_ZN7QLayout6layoutEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QLayout6layoutEv'
    address = self.uglySide.call(ritual)
    return QLayout._cuteAt(address)

  @overload(QEvent)
  @overload(NoneType)
  def widgetEvent(self, a0: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QLayout::widgetEvent(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#widgetEvent

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLayout::widgetEvent(QEvent *a0)
    self.uglySide.call(
        'ritual_ZN7QLayout11widgetEventEP6QEvent', self._addressOf(a0),
    )

  @overload(QChildEvent)
  @overload(NoneType)
  def childEvent(self, e: Optional[QChildEvent]) -> None:
    """
    Calls Qt's 'void QLayout::childEvent(QChildEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#childEvent

    Parameters
    ----------

    e : Optional[QChildEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLayout::childEvent(QChildEvent *e)
    ritual = 'ritual_ZN7QLayout10childEventEP11QChildEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QLayout10childEventEP11QChildEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(THIS)
  @overload(NoneType)
  def addChildLayout(self, l: Optional[QLayout]) -> None:
    """
    Calls Qt's 'void QLayout::addChildLayout(QLayout *l)'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#addChildLayout

    Parameters
    ----------

    l : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLayout::addChildLayout(QLayout *l)
    self.uglySide.call(
        'ritual_ZN7QLayout14addChildLayoutEPS_', self._addressOf(l),
    )

  @overload(QWidget)
  @overload(NoneType)
  def addChildWidget(self, w: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QLayout::addChildWidget(QWidget *w)'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#addChildWidget

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLayout::addChildWidget(QWidget *w)
    self.uglySide.call(
        'ritual_ZN7QLayout14addChildWidgetEP7QWidget', self._addressOf(w),
    )

  @overload(THIS)
  @overload(NoneType)
  def adoptLayout(self, layout: Optional[QLayout]) -> bool:
    """
    Calls Qt's 'bool QLayout::adoptLayout(QLayout *layout)'.

    Qt's own words: https://doc.qt.io/qt-6/qlayout.html#adoptLayout

    Parameters
    ----------

    layout : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QLayout::adoptLayout(QLayout *layout)
    return self.uglySide.call(
        'ritual_ZN7QLayout11adoptLayoutEPS_', self._addressOf(layout),
    )
