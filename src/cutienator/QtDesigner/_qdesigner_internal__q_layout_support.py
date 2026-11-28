"""
qdesigner_internal::QLayoutSupport binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qlayout_widget_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::QLayoutSupport to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList, QObject
from . import QDesignerLayoutDecorationExtension, qdesigner_internal

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPoint, QRect
  from ..QtWidgets import QFormLayout, QGridLayout, QLayout, QLayoutItem
  from ..QtWidgets import QWidget
  from . import QDesignerFormWindowInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerFormWindowInterface = WAIT['QDesignerFormWindowInterface']
  QFormLayout = WAIT['QFormLayout']
  QGridLayout = WAIT['QGridLayout']
  QLayout = WAIT['QLayout']
  QLayoutItem = WAIT['QLayoutItem']
  QPoint = WAIT['QPoint']
  QRect = WAIT['QRect']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLayoutSupport(QObject, QDesignerLayoutDecorationExtension):
  """
  The cute side of Qt's qdesigner_internal::QLayoutSupport: a plain Python
  object standing in front of one C++ qdesigner_internal::QLayoutSupport.

  It is built on the cute 'QObject', as Qt's
  qdesigner_internal::QLayoutSupport is built on Qt's QObject, and has
  everything that class has. It is built on the cute
  'QDesignerLayoutDecorationExtension' as well, as Qt's
  qdesigner_internal::QLayoutSupport is built on Qt's
  QDesignerLayoutDecorationExtension too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::QLayoutSupport that has a ritual
  and that Python can call so far, 23 names in all: 'metaObject', 'tr',
  'formWindow', 'helper', 'currentIndex', 'currentInsertMode', 'findItemAt',
  'indexOf', 'adjustIndicator', 'widgets', 'createEmptyCells',
  'removeEmptyCells', 'canSimplifyQuickCheck', 'createLayoutSupport',
  'setCurrentCellFromIndicatorOnEmptyCell', 'setCurrentCellFromIndicator',
  'extendedGeometry', 'supportsIndicatorOrientation', 'itemInfo', 'layout',
  'gridLayout', 'widget', 'setInsertMode'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *qdesigner_internal::QLayoutSupport::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    qdesigner_internal::QLayoutSupport::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'qdesigner_internal::QLayoutSupport::~QLayoutSupport()': the
    destructor: Python never removes a C++
    qdesigner_internal::QLayoutSupport.
  - Qt's 'std::pair<int, int>
    qdesigner_internal::QLayoutSupport::currentCell() const': gives a type
    Python has no way to take yet.
  - Qt's 'void qdesigner_internal::QLayoutSupport::setCurrentCell(const
    std::pair<int, int> &cell)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void qdesigner_internal::QLayoutSupport::hideIndicator(Indicator
    i)': names the enum 'qdesigner_internal::QLayoutSupport::Indicator',
    whose class cannot be named here.
  - Qt's 'void qdesigner_internal::QLayoutSupport::showIndicator(Indicator i,
    const QRect &geometry, const QPalette &a2)': names the enum
    'qdesigner_internal::QLayoutSupport::Indicator', whose class cannot be
    named here.

  What has no ritual
  ------------------

  3 of the 38 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ qdesigner_internal::QLayoutSupport is created at the first use,
    not by 'qdesigner_internal::QLayoutSupport(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::QLayoutSupport.
  - Qt tells when it has removed the C++ qdesigner_internal::QLayoutSupport.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's qdesigner_internal::QLayoutSupport that has no cute
    function yet, '__init__', 'hideIndicator', 'setCurrentCell',
    'showIndicator', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

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
    Calls Qt's 'QString qdesigner_internal::QLayoutSupport::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qlayoutsupport.html#tr

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
    #  QString qdesigner_internal::QLayoutSupport::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal14QLayoutSupport2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QGridLayout)
  @overload(NoneType)
  def createEmptyCells(gridLayout: Optional[QGridLayout]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QLayoutSupport::createEmptyCells(QGridLayout
    *gridLayout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qlayoutsupport.html

    Parameters
    ----------

    gridLayout : Optional[QGridLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::QLayoutSupport::createEmptyCells(QGridLayout
    #      *gridLayout)
    Rituals.call(
        'ritual_ZN18qdesigner_internal14QLayoutSupport16createEmptyCellsEP1'
        '1QGridLayout',
        CuteMixin._addressOf(gridLayout),
    )

  @staticmethod
  @overload(QFormLayout)
  def createEmptyCells(formLayout: Optional[QFormLayout]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QLayoutSupport::createEmptyCells(QFormLayout
    *formLayout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qlayoutsupport.html

    Parameters
    ----------

    formLayout : Optional[QFormLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::QLayoutSupport::createEmptyCells(QFormLayout
    #      *formLayout)
    Rituals.call(
        'ritual_ZN18qdesigner_internal14QLayoutSupport16createEmptyCellsEP1'
        '1QFormLayout',
        CuteMixin._addressOf(formLayout),
    )

  @staticmethod
  @overload(QGridLayout, QRect)
  @overload(NoneType, QRect)
  def removeEmptyCells(
      gridLayout: Optional[QGridLayout],
      area: QRect,
  ) -> bool:
    """
    Calls Qt's 'bool
    qdesigner_internal::QLayoutSupport::removeEmptyCells(QGridLayout
    *gridLayout, const QRect &area)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qlayoutsupport.html

    Parameters
    ----------

    gridLayout : Optional[QGridLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    area : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  bool qdesigner_internal::QLayoutSupport::removeEmptyCells(QGridLayout
    #      *gridLayout, const QRect &area)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal14QLayoutSupport16removeEmptyCellsEP1'
        '1QGridLayoutRK5QRect',
        CuteMixin._addressOf(gridLayout), CuteMixin._valueOf(area),
    )

  @staticmethod
  @overload(QFormLayout, QRect)
  def removeEmptyCells(
      formLayout: Optional[QFormLayout],
      area: QRect,
  ) -> bool:
    """
    Calls Qt's 'bool
    qdesigner_internal::QLayoutSupport::removeEmptyCells(QFormLayout
    *formLayout, const QRect &area)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qlayoutsupport.html

    Parameters
    ----------

    formLayout : Optional[QFormLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    area : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  bool qdesigner_internal::QLayoutSupport::removeEmptyCells(QFormLayout
    #      *formLayout, const QRect &area)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal14QLayoutSupport16removeEmptyCellsEP1'
        '1QFormLayoutRK5QRect',
        CuteMixin._addressOf(formLayout), CuteMixin._valueOf(area),
    )

  @staticmethod
  @overload(QGridLayout)
  @overload(NoneType)
  def canSimplifyQuickCheck(a0: Optional[QGridLayout]) -> bool:
    """
    Calls Qt's 'bool
    qdesigner_internal::QLayoutSupport::canSimplifyQuickCheck(const
    QGridLayout *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qlayoutsupport.html

    Parameters
    ----------

    a0 : Optional[QGridLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool qdesigner_internal::QLayoutSupport::canSimplifyQuickCheck(const
    #      QGridLayout *a0)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal14QLayoutSupport21canSimplifyQuickChe'
        'ckEPK11QGridLayout',
        CuteMixin._addressOf(a0),
    )

  @staticmethod
  @overload(QFormLayout)
  def canSimplifyQuickCheck(fl: Optional[QFormLayout]) -> bool:
    """
    Calls Qt's 'bool
    qdesigner_internal::QLayoutSupport::canSimplifyQuickCheck(const
    QFormLayout *fl)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qlayoutsupport.html

    Parameters
    ----------

    fl : Optional[QFormLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool qdesigner_internal::QLayoutSupport::canSimplifyQuickCheck(const
    #      QFormLayout *fl)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal14QLayoutSupport21canSimplifyQuickChe'
        'ckEPK11QFormLayout',
        CuteMixin._addressOf(fl),
    )

  @staticmethod
  @overload(QDesignerFormWindowInterface, QWidget)
  @overload(QDesignerFormWindowInterface, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  @overload(QDesignerFormWindowInterface, QWidget, QObject)
  @overload(QDesignerFormWindowInterface, QWidget, NoneType)
  @overload(QDesignerFormWindowInterface, NoneType, QObject)
  @overload(QDesignerFormWindowInterface, NoneType, NoneType)
  @overload(NoneType, QWidget, QObject)
  @overload(NoneType, QWidget, NoneType)
  @overload(NoneType, NoneType, QObject)
  @overload(NoneType, NoneType, NoneType)
  def createLayoutSupport(
      formWindow: Optional[QDesignerFormWindowInterface],
      widget: Optional[QWidget],
      parent: Optional[QObject] = None,
  ) -> Optional[QLayoutSupport]:
    """
    Calls Qt's 'QLayoutSupport
    *qdesigner_internal::QLayoutSupport::createLayoutSupport(
    QDesignerFormWindowInterface *formWindow, QWidget *widget, QObject
    *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qlayoutsupport.html

    Parameters
    ----------

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QLayoutSupport]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLayoutSupport
    #      *qdesigner_internal::QLayoutSupport::createLayoutSupport(
    #      QDesignerFormWindowInterface *formWindow, QWidget *widget, QObject
    #      *parent)
    address = Rituals.call(
        'ritual_ZN18qdesigner_internal14QLayoutSupport19createLayoutSupport'
        'EP28QDesignerFormWindowInterfaceP7QWidgetP7QObject',
        CuteMixin._addressOf(formWindow), CuteMixin._addressOf(widget),
        CuteMixin._addressOf(parent, 'QObject'),
    )
    return QLayoutSupport._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::QLayoutSupport'

  #  Qt's qdesigner_internal::QLayoutSupport is built on more than one class.
  #  The part of a C++ qdesigner_internal::QLayoutSupport that belongs to a
  #  class after the first begins somewhere inside the object, and the ritual
  #  named for that class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QDesignerLayoutDecorationExtension':
          'ritual_cast_qdesigner_internal_QLayoutSupport_QDesignerLayoutDecorationExtension',
  }

  #  A C++ qdesigner_internal::QLayoutSupport Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_qdesigner_internal_QLayoutSupport'

  #  The functions Qt calls itself that qdesigner_internal::QLayoutSupport is
  #  the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'setCurrentCellFromIndicatorOnEmptyCell': (
          ('_ZN18qdesigner_internal14QLayoutSupport38setCurrentCellFromIndi'
           'catorOnEmptyCellEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'setCurrentCellFromIndicator': (
          ('_ZN18qdesigner_internal14QLayoutSupport27setCurrentCellFromIndi'
           'catorEN2Qt11OrientationEii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtCore:Qt.Orientation'),
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'extendedGeometry': (
          ('_ZNK18qdesigner_internal14QLayoutSupport16extendedGeometryEi',
           ('address', 'value', 'QtCore:QRect'),
           (
               ('int', 'number', ''),
           )),
      ),
      'supportsIndicatorOrientation': (
          ('_ZNK18qdesigner_internal14QLayoutSupport28supportsIndicatorOrie'
           'ntationEN2Qt11OrientationE',
           ('bool', 'number', ''),
           (
               ('int', 'enum', 'QtCore:Qt.Orientation'),
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
    Calls Qt's 'const QMetaObject
    *qdesigner_internal::QLayoutSupport::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qlayoutsupport.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *qdesigner_internal::QLayoutSupport::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal14QLayoutSupport10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def formWindow(self) -> Optional[QDesignerFormWindowInterface]:
    """
    Calls Qt's 'QDesignerFormWindowInterface
    *qdesigner_internal::QLayoutSupport::formWindow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qlayoutsupport.html#formWindow

    Returns
    -------

    Optional[QDesignerFormWindowInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerFormWindowInterface
    #      *qdesigner_internal::QLayoutSupport::formWindow() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal14QLayoutSupport10formWindowEv',
    )
    from . import QDesignerFormWindowInterface
    return QDesignerFormWindowInterface._cuteAt(address)

  def helper(self) -> Optional[qdesigner_internal.LayoutHelper]:
    """
    Calls Qt's 'LayoutHelper *qdesigner_internal::QLayoutSupport::helper()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qlayoutsupport.html#helper

    Returns
    -------

    Optional[qdesigner_internal.LayoutHelper]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  LayoutHelper *qdesigner_internal::QLayoutSupport::helper() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal14QLayoutSupport6helperEv',
    )
    return qdesigner_internal.LayoutHelper._cuteAt(address)

  def currentIndex(self) -> int:
    """
    Calls Qt's 'int qdesigner_internal::QLayoutSupport::currentIndex()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qlayoutsupport.html
    """
    #  int qdesigner_internal::QLayoutSupport::currentIndex() const
    ritual = 'ritual_ZNK18qdesigner_internal14QLayoutSupport12currentIndexEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18qdesigner_internal14QLayoutSupport12currentIndex'
          'Ev')
    return self.uglySide.call(ritual)

  def currentInsertMode(
      self,
  ) -> QDesignerLayoutDecorationExtension.InsertMode:
    """
    Calls Qt's 'InsertMode
    qdesigner_internal::QLayoutSupport::currentInsertMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qlayoutsupport.html

    Returns
    -------

    QDesignerLayoutDecorationExtension.InsertMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QDesignerLayoutDecorationExtension.InsertMode(number)' gives.
    """
    #  InsertMode qdesigner_internal::QLayoutSupport::currentInsertMode()
    #      const
    ritual = (
        'ritual_ZNK18qdesigner_internal14QLayoutSupport17currentInsertModeE'
        'v')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18qdesigner_internal14QLayoutSupport17currentInser'
          'tModeEv')
    return QDesignerLayoutDecorationExtension.InsertMode(self.uglySide.call(
        ritual,
    ))

  @overload(QPoint)
  def findItemAt(self, pos: QPoint) -> int:
    """
    Calls Qt's 'int qdesigner_internal::QLayoutSupport::findItemAt(const
    QPoint &pos) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qlayoutsupport.html#findItemAt

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  int qdesigner_internal::QLayoutSupport::findItemAt(const QPoint &pos)
    #      const
    ritual = (
        'ritual_ZNK18qdesigner_internal14QLayoutSupport10findItemAtERK6QPoi'
        'nt')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18qdesigner_internal14QLayoutSupport10findItemAtER'
          'K6QPoint')
    return self.uglySide.call(ritual, self._valueOf(pos))

  @staticmethod
  @overload(QGridLayout, int, int)
  @overload(NoneType, int, int)
  def findItemAt(a0: Optional[QGridLayout], row: int, column: int) -> int:
    """
    Calls Qt's 'int
    qdesigner_internal::QLayoutSupport::findItemAt(QGridLayout *a0, int row,
    int column)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qlayoutsupport.html#findItemAt

    Parameters
    ----------

    a0 : Optional[QGridLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.
    """
    #  int qdesigner_internal::QLayoutSupport::findItemAt(QGridLayout *a0,
    #      int row, int column)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal14QLayoutSupport10findItemAtEP11QGrid'
        'Layoutii',
        CuteMixin._addressOf(a0), row, column,
    )

  @overload(QWidget)
  @overload(NoneType)
  def indexOf(self, widget: Optional[QWidget]) -> int:
    """
    Calls Qt's 'int qdesigner_internal::QLayoutSupport::indexOf(QWidget
    *widget) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qlayoutsupport.html#indexOf

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int qdesigner_internal::QLayoutSupport::indexOf(QWidget *widget) const
    ritual = (
        'ritual_ZNK18qdesigner_internal14QLayoutSupport7indexOfEP7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18qdesigner_internal14QLayoutSupport7indexOfEP7QWi'
          'dget')
    return self.uglySide.call(ritual, self._addressOf(widget))

  @overload(QLayoutItem)
  def indexOf(self, item: Optional[QLayoutItem]) -> int:
    """
    Calls Qt's 'int qdesigner_internal::QLayoutSupport::indexOf(QLayoutItem
    *item) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qlayoutsupport.html#indexOf

    Parameters
    ----------

    item : Optional[QLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int qdesigner_internal::QLayoutSupport::indexOf(QLayoutItem *item)
    #      const
    ritual = (
        'ritual_ZNK18qdesigner_internal14QLayoutSupport7indexOfEP11QLayoutI'
        'tem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18qdesigner_internal14QLayoutSupport7indexOfEP11QL'
          'ayoutItem')
    return self.uglySide.call(ritual, self._addressOf(item, 'QLayoutItem'))

  @overload(QLayout)
  @overload(NoneType)
  def widgets(self, layout: Optional[QLayout]) -> QList[QWidget]:
    """
    Calls Qt's 'QWidgetList
    qdesigner_internal::QLayoutSupport::widgets(QLayout *layout) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qlayoutsupport.html#widgets

    Parameters
    ----------

    layout : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QList[QWidget]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QWidgetList qdesigner_internal::QLayoutSupport::widgets(QLayout
    #      *layout) const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal14QLayoutSupport7widgetsEP7QLayout',
        self._addressOf(layout),
    )
    from ..QtWidgets import QWidget
    return QList[QWidget]._cuteOwning(address)

  @overload(int)
  def extendedGeometry(self, index: int) -> QRect:
    """
    Calls Qt's 'QRect
    qdesigner_internal::QLayoutSupport::extendedGeometry(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qlayoutsupport.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect qdesigner_internal::QLayoutSupport::extendedGeometry(int index)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal14QLayoutSupport16extendedGeometryEi',
        index,
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(Qt.Orientation)
  def supportsIndicatorOrientation(
      self,
      indicatorOrientation: Qt.Orientation,
  ) -> bool:
    """
    Calls Qt's 'bool
    qdesigner_internal::QLayoutSupport::supportsIndicatorOrientation(Qt::
    Orientation indicatorOrientation) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qlayoutsupport.html

    Parameters
    ----------

    indicatorOrientation : Qt.Orientation
      Passed on as its number.
    """
    #  bool qdesigner_internal::QLayoutSupport::supportsIndicatorOrientation(
    #      Qt::Orientation indicatorOrientation) const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal14QLayoutSupport28supportsIndicatorO'
        'rientationEN2Qt11OrientationE',
        indicatorOrientation.value,
    )

  @overload(int)
  def itemInfo(self, index: int) -> QRect:
    """
    Calls Qt's 'QRect qdesigner_internal::QLayoutSupport::itemInfo(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qlayoutsupport.html#itemInfo

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect qdesigner_internal::QLayoutSupport::itemInfo(int index) const
    ritual = 'ritual_ZNK18qdesigner_internal14QLayoutSupport8itemInfoEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18qdesigner_internal14QLayoutSupport8itemInfoEi')
    address = self.uglySide.call(ritual, index)
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def layout(self) -> Optional[QLayout]:
    """
    Calls Qt's 'QLayout *qdesigner_internal::QLayoutSupport::layout() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qlayoutsupport.html#layout

    Returns
    -------

    Optional[QLayout]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLayout *qdesigner_internal::QLayoutSupport::layout() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal14QLayoutSupport6layoutEv',
    )
    from ..QtWidgets import QLayout
    return QLayout._cuteAt(address)

  def gridLayout(self) -> Optional[QGridLayout]:
    """
    Calls Qt's 'QGridLayout *qdesigner_internal::QLayoutSupport::gridLayout()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qlayoutsupport.html#gridLayout

    Returns
    -------

    Optional[QGridLayout]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGridLayout *qdesigner_internal::QLayoutSupport::gridLayout() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal14QLayoutSupport10gridLayoutEv',
    )
    from ..QtWidgets import QGridLayout
    return QGridLayout._cuteAt(address)

  def widget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *qdesigner_internal::QLayoutSupport::widget() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qlayoutsupport.html#widget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *qdesigner_internal::QLayoutSupport::widget() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal14QLayoutSupport6widgetEv',
    )
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setCurrentCellFromIndicatorOnEmptyCell(self, index: int) -> None:
    """
    Calls Qt's 'void qdesigner_internal::QLayoutSupport::
    setCurrentCellFromIndicatorOnEmptyCell(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qlayoutsupport.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void qdesigner_internal::QLayoutSupport::
    #      setCurrentCellFromIndicatorOnEmptyCell(int index)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14QLayoutSupport38setCurrentCellFromI'
        'ndicatorOnEmptyCellEi',
        index,
    )

  @overload(Qt.Orientation, int, int)
  def setCurrentCellFromIndicator(
      self,
      indicatorOrientation: Qt.Orientation,
      index: int,
      increment: int,
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QLayoutSupport::setCurrentCellFromIndicator(Qt::
    Orientation indicatorOrientation, int index, int increment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qlayoutsupport.html

    Parameters
    ----------

    indicatorOrientation : Qt.Orientation
      Passed on as its number.

    index : int
      Passed on as it is.

    increment : int
      Passed on as it is.
    """
    #  void qdesigner_internal::QLayoutSupport::setCurrentCellFromIndicator(
    #      Qt::Orientation indicatorOrientation, int index, int increment)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14QLayoutSupport27setCurrentCellFromI'
        'ndicatorEN2Qt11OrientationEii',
        indicatorOrientation.value, index, increment,
    )

  @overload(QDesignerLayoutDecorationExtension.InsertMode)
  def setInsertMode(
      self,
      im: QDesignerLayoutDecorationExtension.InsertMode,
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QLayoutSupport::setInsertMode(InsertMode im)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qlayoutsupport.html

    Parameters
    ----------

    im : QDesignerLayoutDecorationExtension.InsertMode
      Passed on as its number.
    """
    #  void qdesigner_internal::QLayoutSupport::setInsertMode(InsertMode im)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14QLayoutSupport13setInsertModeEN34QD'
        'esignerLayoutDecorationExtension10InsertModeE',
        im.value,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'qdesigner_internal::QLayoutSupport::QLayoutSupport(
    QDesignerFormWindowInterface *formWindow, QWidget *widget, LayoutHelper
    *helper, QObject *parent)': the class is abstract, so C++ cannot make
    one, and the C++ class of ours does not fill in every function it leaves
    open.
    """
    raise NotImplementedError(
        "'qdesigner_internal.QLayoutSupport.__init__' has no cute function "
        "yet. Qt's "
        "'qdesigner_internal::QLayoutSupport::QLayoutSupport(QDesignerFormWi"
        "ndowInterface *formWindow, QWidget *widget, LayoutHelper *helper, "
        "QObject *parent)': the class is abstract, so C++ cannot make one, "
        "and the C++ class of ours does not fill in every function it "
        "leaves open.")

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

  @overload(QPoint, int)
  def adjustIndicator(self, pos: QPoint, index: int) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QLayoutSupport::adjustIndicator(const QPoint &pos,
    int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qlayoutsupport.html

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    index : int
      Passed on as it is.
    """
    #  void qdesigner_internal::QLayoutSupport::adjustIndicator(const QPoint
    #      &pos, int index)
    ritual = (
        'ritual_ZN18qdesigner_internal14QLayoutSupport15adjustIndicatorERK6'
        'QPointi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal14QLayoutSupport15adjustIndicat'
          'orERK6QPointi')
    self.uglySide.call(ritual, self._valueOf(pos), index)

  @staticmethod
  def hideIndicator(*__, **_) -> Never:
    """
    Qt's 'void qdesigner_internal::QLayoutSupport::hideIndicator(Indicator
    i)': names the enum 'qdesigner_internal::QLayoutSupport::Indicator',
    whose class cannot be named here.
    """
    raise NotImplementedError(
        "'qdesigner_internal.QLayoutSupport.hideIndicator' has no cute "
        "function yet. Qt's 'void "
        "qdesigner_internal::QLayoutSupport::hideIndicator(Indicator i)': "
        "names the enum 'qdesigner_internal::QLayoutSupport::Indicator', "
        "whose class cannot be named here.")

  @staticmethod
  def setCurrentCell(*__, **_) -> Never:
    """
    Qt's 'void qdesigner_internal::QLayoutSupport::setCurrentCell(const
    std::pair<int, int> &cell)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'qdesigner_internal.QLayoutSupport.setCurrentCell' has no cute "
        "function yet. Qt's 'void "
        "qdesigner_internal::QLayoutSupport::setCurrentCell(const "
        "std::pair<int, int> &cell)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def showIndicator(*__, **_) -> Never:
    """
    Qt's 'void qdesigner_internal::QLayoutSupport::showIndicator(Indicator i,
    const QRect &geometry, const QPalette &a2)': names the enum
    'qdesigner_internal::QLayoutSupport::Indicator', whose class cannot be
    named here.
    """
    raise NotImplementedError(
        "'qdesigner_internal.QLayoutSupport.showIndicator' has no cute "
        "function yet. Qt's 'void "
        "qdesigner_internal::QLayoutSupport::showIndicator(Indicator i, "
        "const QRect &geometry, const QPalette &a2)': names the enum "
        "'qdesigner_internal::QLayoutSupport::Indicator', whose class "
        "cannot be named here.")
