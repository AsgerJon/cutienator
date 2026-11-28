"""
QLayoutWidget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qlayout_widget_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QLayoutWidget to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtWidgets import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject
  from ..QtGui import QPaintEvent
  from . import QDesignerFormWindowInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerFormWindowInterface = WAIT['QDesignerFormWindowInterface']
  QEvent = WAIT['QEvent']
  QPaintEvent = WAIT['QPaintEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLayoutWidget(QWidget):
  """
  The cute side of Qt's QLayoutWidget: a plain Python object standing in
  front of one C++ QLayoutWidget.

  It is built on the cute 'QWidget', as Qt's QLayoutWidget is built on Qt's
  QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QLayoutWidget that has a ritual and that Python can
  call so far, 13 names in all: 'metaObject', 'tr', 'layoutLeftMargin',
  'setLayoutLeftMargin', 'layoutTopMargin', 'setLayoutTopMargin',
  'layoutRightMargin', 'setLayoutRightMargin', 'layoutBottomMargin',
  'setLayoutBottomMargin', 'formWindow', 'event', 'paintEvent'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QLayoutWidget::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QLayoutWidget::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 18 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QLayoutWidget is created at the first use, not by
    'QLayoutWidget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QLayoutWidget.
  - Qt tells when it has removed the C++ QLayoutWidget. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QLayoutWidget::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qlayoutwidget.html#tr

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
    #  QString QLayoutWidget::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QLayoutWidget2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLayoutWidget'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QLayoutWidget::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayoutwidget.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QLayoutWidget::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QLayoutWidget10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def layoutLeftMargin(self) -> int:
    """
    Calls Qt's 'int QLayoutWidget::layoutLeftMargin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlayoutwidget.html#layoutLeftMargin
    """
    #  int QLayoutWidget::layoutLeftMargin() const
    return self.uglySide.call(
        'ritual_ZNK13QLayoutWidget16layoutLeftMarginEv',
    )

  def layoutTopMargin(self) -> int:
    """
    Calls Qt's 'int QLayoutWidget::layoutTopMargin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayoutwidget.html#layoutTopMargin
    """
    #  int QLayoutWidget::layoutTopMargin() const
    return self.uglySide.call('ritual_ZNK13QLayoutWidget15layoutTopMarginEv')

  def layoutRightMargin(self) -> int:
    """
    Calls Qt's 'int QLayoutWidget::layoutRightMargin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlayoutwidget.html#layoutRightMargin
    """
    #  int QLayoutWidget::layoutRightMargin() const
    return self.uglySide.call(
        'ritual_ZNK13QLayoutWidget17layoutRightMarginEv',
    )

  def layoutBottomMargin(self) -> int:
    """
    Calls Qt's 'int QLayoutWidget::layoutBottomMargin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlayoutwidget.html#layoutBottomMargin
    """
    #  int QLayoutWidget::layoutBottomMargin() const
    return self.uglySide.call(
        'ritual_ZNK13QLayoutWidget18layoutBottomMarginEv',
    )

  def formWindow(self) -> Optional[QDesignerFormWindowInterface]:
    """
    Calls Qt's 'QDesignerFormWindowInterface *QLayoutWidget::formWindow()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayoutwidget.html#formWindow

    Returns
    -------

    Optional[QDesignerFormWindowInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerFormWindowInterface *QLayoutWidget::formWindow() const
    address = self.uglySide.call('ritual_ZNK13QLayoutWidget10formWindowEv')
    from . import QDesignerFormWindowInterface
    return QDesignerFormWindowInterface._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setLayoutLeftMargin(self, layoutMargin: int) -> None:
    """
    Calls Qt's 'void QLayoutWidget::setLayoutLeftMargin(int layoutMargin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlayoutwidget.html#setLayoutLeftMargin

    Parameters
    ----------

    layoutMargin : int
      Passed on as it is.
    """
    #  void QLayoutWidget::setLayoutLeftMargin(int layoutMargin)
    self.uglySide.call(
        'ritual_ZN13QLayoutWidget19setLayoutLeftMarginEi', layoutMargin,
    )

  @overload(int)
  def setLayoutTopMargin(self, layoutMargin: int) -> None:
    """
    Calls Qt's 'void QLayoutWidget::setLayoutTopMargin(int layoutMargin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlayoutwidget.html#setLayoutTopMargin

    Parameters
    ----------

    layoutMargin : int
      Passed on as it is.
    """
    #  void QLayoutWidget::setLayoutTopMargin(int layoutMargin)
    self.uglySide.call(
        'ritual_ZN13QLayoutWidget18setLayoutTopMarginEi', layoutMargin,
    )

  @overload(int)
  def setLayoutRightMargin(self, layoutMargin: int) -> None:
    """
    Calls Qt's 'void QLayoutWidget::setLayoutRightMargin(int layoutMargin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlayoutwidget.html#setLayoutRightMargin

    Parameters
    ----------

    layoutMargin : int
      Passed on as it is.
    """
    #  void QLayoutWidget::setLayoutRightMargin(int layoutMargin)
    self.uglySide.call(
        'ritual_ZN13QLayoutWidget20setLayoutRightMarginEi', layoutMargin,
    )

  @overload(int)
  def setLayoutBottomMargin(self, layoutMargin: int) -> None:
    """
    Calls Qt's 'void QLayoutWidget::setLayoutBottomMargin(int layoutMargin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlayoutwidget.html#setLayoutBottomMargin

    Parameters
    ----------

    layoutMargin : int
      Passed on as it is.
    """
    #  void QLayoutWidget::setLayoutBottomMargin(int layoutMargin)
    self.uglySide.call(
        'ritual_ZN13QLayoutWidget21setLayoutBottomMarginEi', layoutMargin,
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

  @overload(QDesignerFormWindowInterface)
  @overload(NoneType)
  @overload(QDesignerFormWindowInterface, QWidget)
  @overload(QDesignerFormWindowInterface, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      formWindow: Optional[QDesignerFormWindowInterface],
      parent: Optional[QWidget] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QLayoutWidget::QLayoutWidget(QDesignerFormWindowInterface *formWindow,
    QWidget *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlayoutwidget.html#QLayoutWidget

    Parameters
    ----------

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QLayoutWidget::QLayoutWidget(QDesignerFormWindowInterface *formWindow,
    #      QWidget *parent)
    self._noteCreation(QLayoutWidget, lambda: Rituals.call(
        'ritual_ZN13QLayoutWidgetC1EP28QDesignerFormWindowInterfaceP7QWidge'
        't',
        self._addressOf(formWindow), self._addressOf(parent),
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

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QLayoutWidget::event(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qlayoutwidget.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QLayoutWidget::event(QEvent *e)
    ritual = 'ritual_ZN13QLayoutWidget5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QLayoutWidget5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(e))

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, e: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QLayoutWidget::paintEvent(QPaintEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qlayoutwidget.html#paintEvent

    Parameters
    ----------

    e : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLayoutWidget::paintEvent(QPaintEvent *e)
    ritual = 'ritual_ZN13QLayoutWidget10paintEventEP11QPaintEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QLayoutWidget10paintEventEP11QPaintEvent'
    self.uglySide.call(ritual, self._addressOf(e))
