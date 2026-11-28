"""
QBalloonTip binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qsystemtrayicon_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QBalloonTip to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QTimerEvent
  from ..QtGui import QMouseEvent, QPaintEvent, QResizeEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMouseEvent = WAIT['QMouseEvent']
  QPaintEvent = WAIT['QPaintEvent']
  QResizeEvent = WAIT['QResizeEvent']
  QTimerEvent = WAIT['QTimerEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBalloonTip(QWidget):
  """
  The cute side of Qt's QBalloonTip: a plain Python object standing in front
  of one C++ QBalloonTip.

  It is built on the cute 'QWidget', as Qt's QBalloonTip is built on Qt's
  QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QBalloonTip that has a ritual and that Python can
  call so far, 5 names in all: 'metaObject', 'paintEvent', 'resizeEvent',
  'mousePressEvent', 'timerEvent'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QBalloonTip::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QBalloonTip::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  10 of the 17 functions Qt declares: 6 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 not a gap;
  1 leans on 'QBalloonTip; 1 leans on 'vtable for QBalloonTip', which Qt's
  source does not mark for use from outside Qt and has no code for that could
  be taken.

  What to expect
  --------------

  - The C++ QBalloonTip is created at the first use, not by
    'QBalloonTip(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBalloonTip.
  - Qt tells when it has removed the C++ QBalloonTip. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QBalloonTip that has no cute function yet, '__init__',
    'balloon', 'hideBalloon', 'isBalloonVisible', 'showBalloon',
    'updateBalloonPosition', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBalloonTip'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QBalloonTip::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qballoontip.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QBalloonTip::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QBalloonTip10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QBalloonTip::QBalloonTip(const QIcon &icon, const QString &title,
    const QString &msg, QSystemTrayIcon *trayIcon)': leans on 'vtable for
    QBalloonTip', which Qt's source does not mark for use from outside Qt and
    has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QBalloonTip.__init__' has no cute function yet. Qt's "
        "'QBalloonTip::QBalloonTip(const QIcon &icon, const QString &title, "
        "const QString &msg, QSystemTrayIcon *trayIcon)': leans on 'vtable "
        "for QBalloonTip', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

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

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, a0: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QBalloonTip::paintEvent(QPaintEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qballoontip.html#paintEvent

    Parameters
    ----------

    a0 : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBalloonTip::paintEvent(QPaintEvent *a0)
    ritual = 'ritual_ZN11QBalloonTip10paintEventEP11QPaintEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QBalloonTip10paintEventEP11QPaintEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QResizeEvent)
  @overload(NoneType)
  def resizeEvent(self, a0: Optional[QResizeEvent]) -> None:
    """
    Calls Qt's 'void QBalloonTip::resizeEvent(QResizeEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qballoontip.html#resizeEvent

    Parameters
    ----------

    a0 : Optional[QResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBalloonTip::resizeEvent(QResizeEvent *a0)
    ritual = 'ritual_ZN11QBalloonTip11resizeEventEP12QResizeEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QBalloonTip11resizeEventEP12QResizeEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, e: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QBalloonTip::mousePressEvent(QMouseEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qballoontip.html#mousePressEvent

    Parameters
    ----------

    e : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBalloonTip::mousePressEvent(QMouseEvent *e)
    ritual = 'ritual_ZN11QBalloonTip15mousePressEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QBalloonTip15mousePressEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, e: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QBalloonTip::timerEvent(QTimerEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qballoontip.html#timerEvent

    Parameters
    ----------

    e : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBalloonTip::timerEvent(QTimerEvent *e)
    ritual = 'ritual_ZN11QBalloonTip10timerEventEP11QTimerEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QBalloonTip10timerEventEP11QTimerEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  @staticmethod
  def balloon(*__, **_) -> Never:
    """
    Qt's 'void QBalloonTip::balloon(const QPoint &a0, int a1, bool a2)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: no matching literal operator for call to
    'operator""ms' with argument of type 'unsigned long long' or 'const char
    *', and no matching literal operator template.
    """
    raise NotImplementedError(
        "'QBalloonTip.balloon' has no cute function yet. Qt's 'void "
        "QBalloonTip::balloon(const QPoint &a0, int a1, bool a2)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: no matching literal operator for call "
        "to 'operator\"\"ms' with argument of type 'unsigned long long' or "
        "'const char *', and no matching literal operator template.")

  @staticmethod
  def hideBalloon(*__, **_) -> Never:
    """
    Qt's 'void QBalloonTip::hideBalloon()': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'theSolitaryBalloonTip'.
    """
    raise NotImplementedError(
        "'QBalloonTip.hideBalloon' has no cute function yet. Qt's 'void "
        "QBalloonTip::hideBalloon()': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'theSolitaryBalloonTip'.")

  @staticmethod
  def isBalloonVisible(*__, **_) -> Never:
    """
    Qt's 'bool QBalloonTip::isBalloonVisible()': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file: use
    of undeclared identifier 'theSolitaryBalloonTip'.
    """
    raise NotImplementedError(
        "'QBalloonTip.isBalloonVisible' has no cute function yet. Qt's "
        "'bool QBalloonTip::isBalloonVisible()': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'theSolitaryBalloonTip'.")

  @staticmethod
  def showBalloon(*__, **_) -> Never:
    """
    Qt's 'void QBalloonTip::showBalloon(const QIcon &icon, const QString
    &title, const QString &msg, QSystemTrayIcon *trayIcon, const QPoint &pos,
    int timeout, bool showArrow)': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'theSolitaryBalloonTip'.
    """
    raise NotImplementedError(
        "'QBalloonTip.showBalloon' has no cute function yet. Qt's 'void "
        "QBalloonTip::showBalloon(const QIcon &icon, const QString &title, "
        "const QString &msg, QSystemTrayIcon *trayIcon, const QPoint &pos, "
        "int timeout, bool showArrow)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "use of undeclared identifier 'theSolitaryBalloonTip'.")

  @staticmethod
  def updateBalloonPosition(*__, **_) -> Never:
    """
    Qt's 'void QBalloonTip::updateBalloonPosition(const QPoint &pos)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier
    'theSolitaryBalloonTip'.
    """
    raise NotImplementedError(
        "'QBalloonTip.updateBalloonPosition' has no cute function yet. Qt's "
        "'void QBalloonTip::updateBalloonPosition(const QPoint &pos)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'theSolitaryBalloonTip'.")
