"""
QDockWidgetLayout binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qdockwidget_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QDockWidgetLayout to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
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
  QSize = WAIT['QSize']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDockWidgetLayout(QLayout):
  """
  The cute side of Qt's QDockWidgetLayout: a plain Python object standing in
  front of one C++ QDockWidgetLayout.

  It is built on the cute 'QLayout', as Qt's QDockWidgetLayout is built on
  Qt's QLayout, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDockWidgetLayout that has a ritual and that Python
  can call so far, 20 names in all: 'metaObject', 'tr', 'addItem', 'itemAt',
  'takeAt', 'count', 'maximumSize', 'minimumSize', 'sizeHint',
  'sizeFromContent', 'setGeometry', 'widgetForRole', 'setWidgetForRole',
  'itemForRole', 'titleArea', 'minimumTitleWidth', 'titleHeight',
  'wmSupportsNativeWindowDeco', 'nativeWindowDeco', 'setVerticalTitleBar'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDockWidgetLayout::~QDockWidgetLayout()': the destructor: Python
    never removes a C++ QDockWidgetLayout.

  What has no ritual
  ------------------

  5 of the 28 functions Qt declares: 2 takes or gives a type that cannot be
  passed yet; 2 declared and nowhere to be found; 1 a template.

  What to expect
  --------------

  - The C++ QDockWidgetLayout is created at the first use, not by
    'QDockWidgetLayout(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDockWidgetLayout.
  - Qt tells when it has removed the C++ QDockWidgetLayout. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QDockWidgetLayout, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Role(CuteNum):
    """
    The enum 'QDockWidgetLayout::Role' of Qt, with the 5 names Qt gives in
    it.
    """

    Content = Kee[int](0)
    CloseButton = Kee[int](1)
    FloatButton = Kee[int](2)
    TitleBar = Kee[int](3)
    RoleCount = Kee[int](4)

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
    Calls Qt's 'QString QDockWidgetLayout::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qdockwidgetlayout.html#tr

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
    #  QString QDockWidgetLayout::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QDockWidgetLayout2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def wmSupportsNativeWindowDeco() -> bool:
    """
    Calls Qt's 'bool QDockWidgetLayout::wmSupportsNativeWindowDeco()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockwidgetlayout.html#wmSupportsNativeWindowDeco
    """
    #  bool QDockWidgetLayout::wmSupportsNativeWindowDeco()
    return Rituals.call(
        'ritual_ZN17QDockWidgetLayout26wmSupportsNativeWindowDecoEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDockWidgetLayout'

  #  A C++ QDockWidgetLayout Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDockWidgetLayout'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDockWidgetLayout::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdockwidgetlayout.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDockWidgetLayout::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QDockWidgetLayout10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(int)
  def itemAt(self, index: int) -> Optional[QLayoutItem]:
    """
    Calls Qt's 'QLayoutItem *QDockWidgetLayout::itemAt(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdockwidgetlayout.html#itemAt

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
    #  QLayoutItem *QDockWidgetLayout::itemAt(int index) const
    ritual = 'ritual_ZNK17QDockWidgetLayout6itemAtEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QDockWidgetLayout6itemAtEi'
    address = self.uglySide.call(ritual, index)
    return QLayoutItem._cuteAt(address)

  def count(self) -> int:
    """
    Calls Qt's 'int QDockWidgetLayout::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdockwidgetlayout.html#count
    """
    #  int QDockWidgetLayout::count() const
    ritual = 'ritual_ZNK17QDockWidgetLayout5countEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QDockWidgetLayout5countEv'
    return self.uglySide.call(ritual)

  def maximumSize(self) -> QSize:
    """
    Calls Qt's 'QSize QDockWidgetLayout::maximumSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdockwidgetlayout.html#maximumSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QDockWidgetLayout::maximumSize() const
    ritual = 'ritual_ZNK17QDockWidgetLayout11maximumSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QDockWidgetLayout11maximumSizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def minimumSize(self) -> QSize:
    """
    Calls Qt's 'QSize QDockWidgetLayout::minimumSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdockwidgetlayout.html#minimumSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QDockWidgetLayout::minimumSize() const
    ritual = 'ritual_ZNK17QDockWidgetLayout11minimumSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QDockWidgetLayout11minimumSizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QDockWidgetLayout::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdockwidgetlayout.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QDockWidgetLayout::sizeHint() const
    ritual = 'ritual_ZNK17QDockWidgetLayout8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QDockWidgetLayout8sizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(QSize, bool)
  def sizeFromContent(self, content: QSize, floating: bool) -> QSize:
    """
    Calls Qt's 'QSize QDockWidgetLayout::sizeFromContent(const QSize
    &content, bool floating) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockwidgetlayout.html#sizeFromContent

    Parameters
    ----------

    content : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    floating : bool
      Passed on as it is.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QDockWidgetLayout::sizeFromContent(const QSize &content, bool
    #      floating) const
    address = self.uglySide.call(
        'ritual_ZNK17QDockWidgetLayout15sizeFromContentERK5QSizeb',
        self._valueOf(content), floating,
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(Role)
  def widgetForRole(self, r: Role) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QDockWidgetLayout::widgetForRole(Role r) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockwidgetlayout.html#widgetForRole

    Parameters
    ----------

    r : Role
      Passed on as its number.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QDockWidgetLayout::widgetForRole(Role r) const
    address = self.uglySide.call(
        'ritual_ZNK17QDockWidgetLayout13widgetForRoleENS_4RoleE', r.value,
    )
    from . import QWidget
    return QWidget._cuteAt(address)

  @overload(Role)
  def itemForRole(self, r: Role) -> Optional[QLayoutItem]:
    """
    Calls Qt's 'QLayoutItem *QDockWidgetLayout::itemForRole(Role r) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdockwidgetlayout.html#itemForRole

    Parameters
    ----------

    r : Role
      Passed on as its number.

    Returns
    -------

    Optional[QLayoutItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLayoutItem *QDockWidgetLayout::itemForRole(Role r) const
    address = self.uglySide.call(
        'ritual_ZNK17QDockWidgetLayout11itemForRoleENS_4RoleE', r.value,
    )
    return QLayoutItem._cuteAt(address)

  def titleArea(self) -> QRect:
    """
    Calls Qt's 'QRect QDockWidgetLayout::titleArea() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdockwidgetlayout.html#titleArea

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QDockWidgetLayout::titleArea() const
    address = self.uglySide.call('ritual_ZNK17QDockWidgetLayout9titleAreaEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def minimumTitleWidth(self) -> int:
    """
    Calls Qt's 'int QDockWidgetLayout::minimumTitleWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockwidgetlayout.html#minimumTitleWidth
    """
    #  int QDockWidgetLayout::minimumTitleWidth() const
    return self.uglySide.call(
        'ritual_ZNK17QDockWidgetLayout17minimumTitleWidthEv',
    )

  def titleHeight(self) -> int:
    """
    Calls Qt's 'int QDockWidgetLayout::titleHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdockwidgetlayout.html#titleHeight
    """
    #  int QDockWidgetLayout::titleHeight() const
    return self.uglySide.call('ritual_ZNK17QDockWidgetLayout11titleHeightEv')

  @overload()
  def nativeWindowDeco(self) -> bool:
    """
    Calls Qt's 'bool QDockWidgetLayout::nativeWindowDeco() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockwidgetlayout.html#nativeWindowDeco
    """
    #  bool QDockWidgetLayout::nativeWindowDeco() const
    return self.uglySide.call(
        'ritual_ZNK17QDockWidgetLayout16nativeWindowDecoEv',
    )

  @overload(bool)
  def nativeWindowDeco(self, floating: bool) -> bool:
    """
    Calls Qt's 'bool QDockWidgetLayout::nativeWindowDeco(bool floating)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockwidgetlayout.html#nativeWindowDeco

    Parameters
    ----------

    floating : bool
      Passed on as it is.
    """
    #  bool QDockWidgetLayout::nativeWindowDeco(bool floating) const
    return self.uglySide.call(
        'ritual_ZNK17QDockWidgetLayout16nativeWindowDecoEb', floating,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRect)
  def setGeometry(self, r: QRect) -> None:
    """
    Calls Qt's 'void QDockWidgetLayout::setGeometry(const QRect &r)'.

    Qt's own words: https://doc.qt.io/qt-6/qdockwidgetlayout.html#setGeometry

    Parameters
    ----------

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QDockWidgetLayout::setGeometry(const QRect &r)
    ritual = 'ritual_ZN17QDockWidgetLayout11setGeometryERK5QRect'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QDockWidgetLayout11setGeometryERK5QRect'
    self.uglySide.call(ritual, self._valueOf(r))

  @overload(Role, QWidget)
  @overload(Role, NoneType)
  def setWidgetForRole(self, r: Role, w: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QDockWidgetLayout::setWidgetForRole(Role r, QWidget
    *w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockwidgetlayout.html#setWidgetForRole

    Parameters
    ----------

    r : Role
      Passed on as its number.

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDockWidgetLayout::setWidgetForRole(Role r, QWidget *w)
    self.uglySide.call(
        'ritual_ZN17QDockWidgetLayout16setWidgetForRoleENS_4RoleEP7QWidget',
        r.value, self._addressOf(w),
    )

  @overload(bool)
  def setVerticalTitleBar(self, b: bool) -> None:
    """
    Calls Qt's 'void QDockWidgetLayout::setVerticalTitleBar(bool b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockwidgetlayout.html#setVerticalTitleBar

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QDockWidgetLayout::setVerticalTitleBar(bool b)
    self.uglySide.call(
        'ritual_ZN17QDockWidgetLayout19setVerticalTitleBarEb', b,
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
  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's
    'QDockWidgetLayout::QDockWidgetLayout(QWidget *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockwidgetlayout.html#QDockWidgetLayout

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDockWidgetLayout::QDockWidgetLayout(QWidget *parent)
    self._noteCreation(QDockWidgetLayout, lambda: Rituals.call(
        'ritual_ZN17QDockWidgetLayoutC1EP7QWidget', self._addressOf(parent),
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

  @overload(QLayoutItem)
  @overload(NoneType)
  def addItem(self, item: Optional[QLayoutItem]) -> None:
    """
    Calls Qt's 'void QDockWidgetLayout::addItem(QLayoutItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qdockwidgetlayout.html#addItem

    Parameters
    ----------

    item : Optional[QLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDockWidgetLayout::addItem(QLayoutItem *item)
    ritual = 'ritual_ZN17QDockWidgetLayout7addItemEP11QLayoutItem'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QDockWidgetLayout7addItemEP11QLayoutItem'
    self.uglySide.call(ritual, self._addressOf(item, 'QLayoutItem'))

  @overload(int)
  def takeAt(self, index: int) -> Optional[QLayoutItem]:
    """
    Calls Qt's 'QLayoutItem *QDockWidgetLayout::takeAt(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qdockwidgetlayout.html#takeAt

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
    #  QLayoutItem *QDockWidgetLayout::takeAt(int index)
    ritual = 'ritual_ZN17QDockWidgetLayout6takeAtEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QDockWidgetLayout6takeAtEi'
    address = self.uglySide.call(ritual, index)
    return QLayoutItem._cuteAt(address)
