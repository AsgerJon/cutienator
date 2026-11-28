"""
QDesignerDockWidget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_dockwidget_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QDesignerDockWidget to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import Qt
from ..QtWidgets import QDockWidget, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtWidgets import QMainWindow
  from . import QDesignerFormWindowInterface

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerDockWidget(QDockWidget):
  """
  The cute side of Qt's QDesignerDockWidget: a plain Python object standing
  in front of one C++ QDesignerDockWidget.

  It is built on the cute 'QDockWidget', as Qt's QDesignerDockWidget is built
  on Qt's QDockWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDesignerDockWidget that has a ritual and that
  Python can call so far, 9 names in all: 'metaObject', 'tr', 'docked',
  'setDocked', 'dockWidgetArea', 'setDockWidgetArea', 'inMainWindow',
  'formWindow', 'findMainWindow'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDesignerDockWidget::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QDesignerDockWidget::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QDesignerDockWidget::~QDesignerDockWidget()': the destructor:
    Python never removes a C++ QDesignerDockWidget.

  What has no ritual
  ------------------

  2 of the 15 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QDesignerDockWidget is created at the first use, not by
    'QDesignerDockWidget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDesignerDockWidget.
  - Qt tells when it has removed the C++ QDesignerDockWidget. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QDesignerDockWidget::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignerdockwidget.html#tr

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
    #  QString QDesignerDockWidget::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QDesignerDockWidget2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesignerDockWidget'

  #  A C++ QDesignerDockWidget Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDesignerDockWidget'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDesignerDockWidget::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerdockwidget.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDesignerDockWidget::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QDesignerDockWidget10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def docked(self) -> bool:
    """
    Calls Qt's 'bool QDesignerDockWidget::docked() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignerdockwidget.html#docked
    """
    #  bool QDesignerDockWidget::docked() const
    return self.uglySide.call('ritual_ZNK19QDesignerDockWidget6dockedEv')

  def dockWidgetArea(self) -> Qt.DockWidgetArea:
    """
    Calls Qt's 'Qt::DockWidgetArea QDesignerDockWidget::dockWidgetArea()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerdockwidget.html#dockWidgetArea

    Returns
    -------

    Qt.DockWidgetArea
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.DockWidgetArea(number)' gives.
    """
    #  Qt::DockWidgetArea QDesignerDockWidget::dockWidgetArea() const
    return Qt.DockWidgetArea(self.uglySide.call(
        'ritual_ZNK19QDesignerDockWidget14dockWidgetAreaEv',
    ))

  def inMainWindow(self) -> bool:
    """
    Calls Qt's 'bool QDesignerDockWidget::inMainWindow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerdockwidget.html#inMainWindow
    """
    #  bool QDesignerDockWidget::inMainWindow() const
    return self.uglySide.call(
        'ritual_ZNK19QDesignerDockWidget12inMainWindowEv',
    )

  def formWindow(self) -> Optional[QDesignerFormWindowInterface]:
    """
    Calls Qt's 'QDesignerFormWindowInterface
    *QDesignerDockWidget::formWindow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerdockwidget.html#formWindow

    Returns
    -------

    Optional[QDesignerFormWindowInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerFormWindowInterface *QDesignerDockWidget::formWindow() const
    address = self.uglySide.call(
        'ritual_ZNK19QDesignerDockWidget10formWindowEv',
    )
    from . import QDesignerFormWindowInterface
    return QDesignerFormWindowInterface._cuteAt(address)

  def findMainWindow(self) -> Optional[QMainWindow]:
    """
    Calls Qt's 'QMainWindow *QDesignerDockWidget::findMainWindow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerdockwidget.html#findMainWindow

    Returns
    -------

    Optional[QMainWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMainWindow *QDesignerDockWidget::findMainWindow() const
    address = self.uglySide.call(
        'ritual_ZNK19QDesignerDockWidget14findMainWindowEv',
    )
    from ..QtWidgets import QMainWindow
    return QMainWindow._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setDocked(self, b: bool) -> None:
    """
    Calls Qt's 'void QDesignerDockWidget::setDocked(bool b)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignerdockwidget.html#setDocked

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QDesignerDockWidget::setDocked(bool b)
    self.uglySide.call('ritual_ZN19QDesignerDockWidget9setDockedEb', b)

  @overload(Qt.DockWidgetArea)
  def setDockWidgetArea(self, dockWidgetArea: Qt.DockWidgetArea) -> None:
    """
    Calls Qt's 'void
    QDesignerDockWidget::setDockWidgetArea(Qt::DockWidgetArea
    dockWidgetArea)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerdockwidget.html#setDockWidgetArea

    Parameters
    ----------

    dockWidgetArea : Qt.DockWidgetArea
      Passed on as its number.
    """
    #  void QDesignerDockWidget::setDockWidgetArea(Qt::DockWidgetArea
    #      dockWidgetArea)
    self.uglySide.call(
        'ritual_ZN19QDesignerDockWidget17setDockWidgetAreaEN2Qt14DockWidget'
        'AreaE',
        dockWidgetArea.value,
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
    'QDesignerDockWidget::QDesignerDockWidget(QWidget *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerdockwidget.html#QDesignerDockWidget

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDesignerDockWidget::QDesignerDockWidget(QWidget *parent)
    self._noteCreation(QDesignerDockWidget, lambda: Rituals.call(
        'ritual_ZN19QDesignerDockWidgetC1EP7QWidget',
        self._addressOf(parent),
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
