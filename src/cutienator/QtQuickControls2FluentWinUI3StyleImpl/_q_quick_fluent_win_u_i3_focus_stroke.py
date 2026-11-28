"""
QQuickFluentWinUI3FocusStroke binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickControls2FluentWinUI3StyleImpl/6.12.0/QtQuickControls2FluentWinUI3StyleImpl/private/qquickfluentwinui3focusstroke_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickFluentWinUI3FocusStroke to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QColor, QPainter
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QPainter = WAIT['QPainter']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickFluentWinUI3FocusStroke(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickFluentWinUI3FocusStroke: a plain Python object
  standing in front of one C++ QQuickFluentWinUI3FocusStroke.

  What exists
  -----------

  Every function of Qt's QQuickFluentWinUI3FocusStroke that has a ritual and
  that Python can call so far, 6 names in all: 'metaObject', 'radius',
  'setRadius', 'color', 'setColor', 'paint'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickFluentWinUI3FocusStroke::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQuickFluentWinUI3FocusStroke::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  4 of the 12 functions Qt declares: 2 not a gap; 1 leans on
  'QQuickFluentWinUI3FocusStroke; 1 leans on 'vtable for
  QQuickFluentWinUI3FocusStroke', which Qt's source does not mark for use
  from outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QQuickFluentWinUI3FocusStroke is created at the first use, not by
    'QQuickFluentWinUI3FocusStroke(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickFluentWinUI3FocusStroke.
  - Qt tells when it has removed the C++ QQuickFluentWinUI3FocusStroke. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickFluentWinUI3FocusStroke that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickFluentWinUI3FocusStroke'

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
    *QQuickFluentWinUI3FocusStroke::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfluentwinui3focusstroke.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickFluentWinUI3FocusStroke::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK29QQuickFluentWinUI3FocusStroke10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def radius(self) -> int:
    """
    Calls Qt's 'int QQuickFluentWinUI3FocusStroke::radius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfluentwinui3focusstroke.html#radius
    """
    #  int QQuickFluentWinUI3FocusStroke::radius() const
    return self.uglySide.call(
        'ritual_ZNK29QQuickFluentWinUI3FocusStroke6radiusEv',
    )

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickFluentWinUI3FocusStroke::color() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfluentwinui3focusstroke.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickFluentWinUI3FocusStroke::color() const
    address = self.uglySide.call(
        'ritual_ZNK29QQuickFluentWinUI3FocusStroke5colorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setRadius(self, radius: int) -> None:
    """
    Calls Qt's 'void QQuickFluentWinUI3FocusStroke::setRadius(int radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfluentwinui3focusstroke.html#setRadius

    Parameters
    ----------

    radius : int
      Passed on as it is.
    """
    #  void QQuickFluentWinUI3FocusStroke::setRadius(int radius)
    self.uglySide.call(
        'ritual_ZN29QQuickFluentWinUI3FocusStroke9setRadiusEi', radius,
    )

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickFluentWinUI3FocusStroke::setColor(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfluentwinui3focusstroke.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickFluentWinUI3FocusStroke::setColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN29QQuickFluentWinUI3FocusStroke8setColorERK6QColor',
        self._valueOf(color),
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
    Qt's
    'QQuickFluentWinUI3FocusStroke::QQuickFluentWinUI3FocusStroke(QQuickItem
    *parent)': leans on 'vtable for QQuickFluentWinUI3FocusStroke', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQuickFluentWinUI3FocusStroke.__init__' has no cute function yet. "
        "Qt's "
        "'QQuickFluentWinUI3FocusStroke::QQuickFluentWinUI3FocusStroke(QQuic"
        "kItem *parent)': leans on 'vtable for "
        "QQuickFluentWinUI3FocusStroke', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

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

  @overload(QPainter)
  @overload(NoneType)
  def paint(self, painter: Optional[QPainter]) -> None:
    """
    Calls Qt's 'void QQuickFluentWinUI3FocusStroke::paint(QPainter
    *painter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfluentwinui3focusstroke.html#paint

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFluentWinUI3FocusStroke::paint(QPainter *painter)
    ritual = 'ritual_ZN29QQuickFluentWinUI3FocusStroke5paintEP8QPainter'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QQuickFluentWinUI3FocusStroke5paintEP8QPainter')
    self.uglySide.call(ritual, self._addressOf(painter))
