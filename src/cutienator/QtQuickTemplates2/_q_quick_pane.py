"""
QQuickPane binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickpane_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickPane to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtGui import QAccessible
from ..QtQuick import QQuickItem
from . import QQuickControl

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QSizeF
  from . import QQuickPanePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSizeF = WAIT['QSizeF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPane(QQuickControl):
  """
  The cute side of Qt's QQuickPane: a plain Python object standing in front
  of one C++ QQuickPane.

  It is built on the cute 'QQuickControl', as Qt's QQuickPane is built on
  Qt's QQuickControl, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPane that has a ritual and that Python can
  call so far, 16 names in all: 'metaObject', 'tr', 'contentWidth',
  'setContentWidth', 'resetContentWidth', 'contentHeight',
  'setContentHeight', 'resetContentHeight', 'contentWidthChanged',
  'contentHeightChanged', 'contentChildrenChanged', 'componentComplete',
  'contentItemChange', 'contentSizeChange', 'accessibleRole', 'd_func'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickPane::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickPane::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickPane::~QQuickPane()': the destructor: Python never removes a
    C++ QQuickPane.
  - Qt's 'QQuickPane::QQuickPane(QQuickPanePrivate &dd, QQuickItem *parent)':
    takes a type Python has no way to hand over yet.
  - Qt's 'const QQuickPanePrivate *QQuickPane::d_func() const': takes in
    Python what 'QQuickPanePrivate *QQuickPane::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 26 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickPane is created at the first use, not by 'QQuickPane(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPane.
  - Qt tells when it has removed the C++ QQuickPane. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
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
    Calls Qt's 'QString QQuickPane::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpane.html#tr

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
    #  QString QQuickPane::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QQuickPane2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPane'

  #  A C++ QQuickPane Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickPane'

  #  The functions Qt calls itself that QQuickPane is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'contentSizeChange': (
          ('_ZN10QQuickPane17contentSizeChangeERK6QSizeFS2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QSizeF'),
               ('address', 'value', 'QtCore:QSizeF'),
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
    Calls Qt's 'const QMetaObject *QQuickPane::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpane.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickPane::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QQuickPane10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def contentWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickPane::contentWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpane.html#contentWidth
    """
    #  qreal QQuickPane::contentWidth() const
    return self.uglySide.call('ritual_ZNK10QQuickPane12contentWidthEv')

  def contentHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickPane::contentHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpane.html#contentHeight
    """
    #  qreal QQuickPane::contentHeight() const
    return self.uglySide.call('ritual_ZNK10QQuickPane13contentHeightEv')

  def accessibleRole(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QQuickPane::accessibleRole() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpane.html#accessibleRole

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QQuickPane::accessibleRole() const
    ritual = 'ritual_ZNK10QQuickPane14accessibleRoleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QQuickPane14accessibleRoleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setContentWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QQuickPane::setContentWidth(qreal width)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpane.html#setContentWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QQuickPane::setContentWidth(qreal width)
    self.uglySide.call('ritual_ZN10QQuickPane15setContentWidthEd', width)

  @overload(float)
  def setContentHeight(self, height: float) -> None:
    """
    Calls Qt's 'void QQuickPane::setContentHeight(qreal height)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpane.html#setContentHeight

    Parameters
    ----------

    height : float
      Passed on as it is.
    """
    #  void QQuickPane::setContentHeight(qreal height)
    self.uglySide.call('ritual_ZN10QQuickPane16setContentHeightEd', height)

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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's 'QQuickPane::QQuickPane(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickpane.html#QQuickPane

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickPane::QQuickPane(QQuickItem *parent)
    self._noteCreation(QQuickPane, lambda: Rituals.call(
        'ritual_ZN10QQuickPaneC1EP10QQuickItem', self._addressOf(parent),
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

  def resetContentWidth(self) -> None:
    """
    Calls Qt's 'void QQuickPane::resetContentWidth()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpane.html#resetContentWidth
    """
    #  void QQuickPane::resetContentWidth()
    self.uglySide.call('ritual_ZN10QQuickPane17resetContentWidthEv')

  def resetContentHeight(self) -> None:
    """
    Calls Qt's 'void QQuickPane::resetContentHeight()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpane.html#resetContentHeight
    """
    #  void QQuickPane::resetContentHeight()
    self.uglySide.call('ritual_ZN10QQuickPane18resetContentHeightEv')

  def contentWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPane::contentWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpane.html#contentWidthChanged
    """
    #  void QQuickPane::contentWidthChanged()
    self.uglySide.call('ritual_ZN10QQuickPane19contentWidthChangedEv')

  def contentHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPane::contentHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpane.html#contentHeightChanged
    """
    #  void QQuickPane::contentHeightChanged()
    self.uglySide.call('ritual_ZN10QQuickPane20contentHeightChangedEv')

  def contentChildrenChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPane::contentChildrenChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpane.html#contentChildrenChanged
    """
    #  void QQuickPane::contentChildrenChanged()
    self.uglySide.call('ritual_ZN10QQuickPane22contentChildrenChangedEv')

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickPane::componentComplete()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpane.html#componentComplete
    """
    #  void QQuickPane::componentComplete()
    ritual = 'ritual_ZN10QQuickPane17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickPane17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QQuickItem, QQuickItem)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QQuickItem)
  @overload(NoneType, NoneType)
  def contentItemChange(
      self,
      newItem: Optional[QQuickItem],
      oldItem: Optional[QQuickItem],
  ) -> None:
    """
    Calls Qt's 'void QQuickPane::contentItemChange(QQuickItem *newItem,
    QQuickItem *oldItem)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpane.html#contentItemChange

    Parameters
    ----------

    newItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    oldItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPane::contentItemChange(QQuickItem *newItem, QQuickItem
    #      *oldItem)
    ritual = 'ritual_ZN10QQuickPane17contentItemChangeEP10QQuickItemS1_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QQuickPane17contentItemChangeEP10QQuickItemS1_')
    self.uglySide.call(
        ritual, self._addressOf(newItem), self._addressOf(oldItem),
    )

  @overload(QSizeF, QSizeF)
  def contentSizeChange(self, newSize: QSizeF, oldSize: QSizeF) -> None:
    """
    Calls Qt's 'void QQuickPane::contentSizeChange(const QSizeF &newSize,
    const QSizeF &oldSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpane.html#contentSizeChange

    Parameters
    ----------

    newSize : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.

    oldSize : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QQuickPane::contentSizeChange(const QSizeF &newSize, const QSizeF
    #      &oldSize)
    ritual = 'ritual_ZN10QQuickPane17contentSizeChangeERK6QSizeFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickPane17contentSizeChangeERK6QSizeFS2_'
    self.uglySide.call(
        ritual, self._valueOf(newSize), self._valueOf(oldSize),
    )

  def d_func(self) -> Optional[QQuickPanePrivate]:
    """
    Calls Qt's 'QQuickPanePrivate *QQuickPane::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpane.html#d_func

    Returns
    -------

    Optional[QQuickPanePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPanePrivate *QQuickPane::d_func()
    address = self.uglySide.call('ritual_ZN10QQuickPane6d_funcEv')
    from . import QQuickPanePrivate
    return QQuickPanePrivate._cuteAt(address)
