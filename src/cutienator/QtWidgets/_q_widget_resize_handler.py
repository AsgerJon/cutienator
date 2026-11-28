"""
QWidgetResizeHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qwidgetresizehandler_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QWidgetResizeHandler to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject
  from ..QtGui import QMouseEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QMouseEvent = WAIT['QMouseEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWidgetResizeHandler(QObject):
  """
  The cute side of Qt's QWidgetResizeHandler: a plain Python object standing
  in front of one C++ QWidgetResizeHandler.

  It is built on the cute 'QObject', as Qt's QWidgetResizeHandler is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWidgetResizeHandler that has a ritual and that
  Python can call so far, 10 names in all: 'metaObject', 'setEnabled',
  'isEnabled', 'isButtonDown', 'setExtraHeight', 'setFrameWidth', 'activate',
  'eventFilter', 'mouseMoveEvent', 'isResizing'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWidgetResizeHandler::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QWidgetResizeHandler::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QWidgetResizeHandler::setMouseCursor(MousePosition m)': names
    the enum 'QWidgetResizeHandler::MousePosition', whose class cannot be
    named here.

  What has no ritual
  ------------------

  10 of the 23 functions Qt declares: 4 forbidden; 3 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file; 2
  not a gap; 1 leans on 'QWidgetResizeHandler.

  What to expect
  --------------

  - The C++ QWidgetResizeHandler is created at the first use, not by
    'QWidgetResizeHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWidgetResizeHandler.
  - Qt tells when it has removed the C++ QWidgetResizeHandler. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QWidgetResizeHandler that has no cute function yet,
    '__init__', 'doResize', 'keyPressEvent', 'setMouseCursor', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWidgetResizeHandler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWidgetResizeHandler::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetresizehandler.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWidgetResizeHandler::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QWidgetResizeHandler10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isEnabled(self) -> bool:
    """
    Calls Qt's 'bool QWidgetResizeHandler::isEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetresizehandler.html#isEnabled
    """
    #  bool QWidgetResizeHandler::isEnabled() const
    return self.uglySide.call('ritual_ZNK20QWidgetResizeHandler9isEnabledEv')

  def isButtonDown(self) -> bool:
    """
    Calls Qt's 'bool QWidgetResizeHandler::isButtonDown() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetresizehandler.html#isButtonDown
    """
    #  bool QWidgetResizeHandler::isButtonDown() const
    return self.uglySide.call(
        'ritual_ZNK20QWidgetResizeHandler12isButtonDownEv',
    )

  def isResizing(self) -> bool:
    """
    Calls Qt's 'bool QWidgetResizeHandler::isResizing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetresizehandler.html#isResizing
    """
    #  bool QWidgetResizeHandler::isResizing() const
    return self.uglySide.call(
        'ritual_ZNK20QWidgetResizeHandler10isResizingEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setEnabled(self, b: bool) -> None:
    """
    Calls Qt's 'void QWidgetResizeHandler::setEnabled(bool b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetresizehandler.html#setEnabled

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QWidgetResizeHandler::setEnabled(bool b)
    self.uglySide.call('ritual_ZN20QWidgetResizeHandler10setEnabledEb', b)

  @overload(int)
  def setExtraHeight(self, h: int) -> None:
    """
    Calls Qt's 'void QWidgetResizeHandler::setExtraHeight(int h)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetresizehandler.html#setExtraHeight

    Parameters
    ----------

    h : int
      Passed on as it is.
    """
    #  void QWidgetResizeHandler::setExtraHeight(int h)
    self.uglySide.call(
        'ritual_ZN20QWidgetResizeHandler14setExtraHeightEi', h,
    )

  @overload(int)
  def setFrameWidth(self, w: int) -> None:
    """
    Calls Qt's 'void QWidgetResizeHandler::setFrameWidth(int w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetresizehandler.html#setFrameWidth

    Parameters
    ----------

    w : int
      Passed on as it is.
    """
    #  void QWidgetResizeHandler::setFrameWidth(int w)
    self.uglySide.call('ritual_ZN20QWidgetResizeHandler13setFrameWidthEi', w)

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
    Qt's 'QWidgetResizeHandler::QWidgetResizeHandler(QWidget *parent, QWidget
    *cw)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier 'RANGE'.
    """
    raise NotImplementedError(
        "'QWidgetResizeHandler.__init__' has no cute function yet. Qt's "
        "'QWidgetResizeHandler::QWidgetResizeHandler(QWidget *parent, "
        "QWidget *cw)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'RANGE'.")

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

  def activate(self) -> None:
    """
    Calls Qt's 'void QWidgetResizeHandler::activate()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetresizehandler.html#activate
    """
    #  void QWidgetResizeHandler::activate()
    self.uglySide.call('ritual_ZN20QWidgetResizeHandler8activateEv')

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def eventFilter(self, o: Optional[QObject], e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QWidgetResizeHandler::eventFilter(QObject *o, QEvent
    *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetresizehandler.html#eventFilter

    Parameters
    ----------

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QWidgetResizeHandler::eventFilter(QObject *o, QEvent *e)
    return self.uglySide.call(
        'ritual_ZN20QWidgetResizeHandler11eventFilterEP7QObjectP6QEvent',
        self._addressOf(o, 'QObject'), self._addressOf(e),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, e: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QWidgetResizeHandler::mouseMoveEvent(QMouseEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetresizehandler.html#mouseMoveEvent

    Parameters
    ----------

    e : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetResizeHandler::mouseMoveEvent(QMouseEvent *e)
    self.uglySide.call(
        'ritual_ZN20QWidgetResizeHandler14mouseMoveEventEP11QMouseEvent',
        self._addressOf(e),
    )

  @staticmethod
  def doResize(*__, **_) -> Never:
    """
    Qt's 'void QWidgetResizeHandler::doResize()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'resizeHorizontalDirectionFixed'.
    """
    raise NotImplementedError(
        "'QWidgetResizeHandler.doResize' has no cute function yet. Qt's "
        "'void QWidgetResizeHandler::doResize()': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier "
        "'resizeHorizontalDirectionFixed'.")

  @staticmethod
  def keyPressEvent(*__, **_) -> Never:
    """
    Qt's 'void QWidgetResizeHandler::keyPressEvent(QKeyEvent *e)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier
    'resizeHorizontalDirectionFixed'.
    """
    raise NotImplementedError(
        "'QWidgetResizeHandler.keyPressEvent' has no cute function yet. "
        "Qt's 'void QWidgetResizeHandler::keyPressEvent(QKeyEvent *e)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'resizeHorizontalDirectionFixed'.")

  @staticmethod
  def setMouseCursor(*__, **_) -> Never:
    """
    Qt's 'void QWidgetResizeHandler::setMouseCursor(MousePosition m)': names
    the enum 'QWidgetResizeHandler::MousePosition', whose class cannot be
    named here.
    """
    raise NotImplementedError(
        "'QWidgetResizeHandler.setMouseCursor' has no cute function yet. "
        "Qt's 'void QWidgetResizeHandler::setMouseCursor(MousePosition m)': "
        "names the enum 'QWidgetResizeHandler::MousePosition', whose class "
        "cannot be named here.")
