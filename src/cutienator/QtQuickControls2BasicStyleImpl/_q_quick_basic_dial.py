"""
QQuickBasicDial binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickControls2BasicStyleImpl/6.12.0/QtQuickControls2BasicStyleImpl/private/qquickbasicdial_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickBasicDial to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
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


class QQuickBasicDial(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickBasicDial: a plain Python object standing in
  front of one C++ QQuickBasicDial.

  What exists
  -----------

  Every function of Qt's QQuickBasicDial that has a ritual and that Python
  can call so far, 10 names in all: 'metaObject', 'progress', 'setProgress',
  'startAngle', 'setStartAngle', 'endAngle', 'setEndAngle', 'color',
  'setColor', 'paint'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickBasicDial::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickBasicDial::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 2 not a gap; 1 leans on
  'QQuickBasicDial; 1 leans on 'vtable for QQuickBasicDial', which Qt's
  source does not mark for use from outside Qt and has no code for that could
  be taken.

  What to expect
  --------------

  - The C++ QQuickBasicDial is created at the first use, not by
    'QQuickBasicDial(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickBasicDial.
  - Qt tells when it has removed the C++ QQuickBasicDial. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickBasicDial that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickBasicDial'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickBasicDial::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbasicdial.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickBasicDial::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QQuickBasicDial10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def progress(self) -> float:
    """
    Calls Qt's 'qreal QQuickBasicDial::progress() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbasicdial.html#progress
    """
    #  qreal QQuickBasicDial::progress() const
    return self.uglySide.call('ritual_ZNK15QQuickBasicDial8progressEv')

  def startAngle(self) -> float:
    """
    Calls Qt's 'qreal QQuickBasicDial::startAngle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbasicdial.html#startAngle
    """
    #  qreal QQuickBasicDial::startAngle() const
    return self.uglySide.call('ritual_ZNK15QQuickBasicDial10startAngleEv')

  def endAngle(self) -> float:
    """
    Calls Qt's 'qreal QQuickBasicDial::endAngle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbasicdial.html#endAngle
    """
    #  qreal QQuickBasicDial::endAngle() const
    return self.uglySide.call('ritual_ZNK15QQuickBasicDial8endAngleEv')

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickBasicDial::color() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbasicdial.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickBasicDial::color() const
    address = self.uglySide.call('ritual_ZNK15QQuickBasicDial5colorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setProgress(self, progress: float) -> None:
    """
    Calls Qt's 'void QQuickBasicDial::setProgress(qreal progress)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbasicdial.html#setProgress

    Parameters
    ----------

    progress : float
      Passed on as it is.
    """
    #  void QQuickBasicDial::setProgress(qreal progress)
    self.uglySide.call('ritual_ZN15QQuickBasicDial11setProgressEd', progress)

  @overload(float)
  def setStartAngle(self, startAngle: float) -> None:
    """
    Calls Qt's 'void QQuickBasicDial::setStartAngle(qreal startAngle)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbasicdial.html#setStartAngle

    Parameters
    ----------

    startAngle : float
      Passed on as it is.
    """
    #  void QQuickBasicDial::setStartAngle(qreal startAngle)
    self.uglySide.call(
        'ritual_ZN15QQuickBasicDial13setStartAngleEd', startAngle,
    )

  @overload(float)
  def setEndAngle(self, endAngle: float) -> None:
    """
    Calls Qt's 'void QQuickBasicDial::setEndAngle(qreal endAngle)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbasicdial.html#setEndAngle

    Parameters
    ----------

    endAngle : float
      Passed on as it is.
    """
    #  void QQuickBasicDial::setEndAngle(qreal endAngle)
    self.uglySide.call('ritual_ZN15QQuickBasicDial11setEndAngleEd', endAngle)

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickBasicDial::setColor(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbasicdial.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickBasicDial::setColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN15QQuickBasicDial8setColorERK6QColor',
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
    Qt's 'QQuickBasicDial::QQuickBasicDial(QQuickItem *parent)': leans on
    'vtable for QQuickBasicDial', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickBasicDial.__init__' has no cute function yet. Qt's "
        "'QQuickBasicDial::QQuickBasicDial(QQuickItem *parent)': leans on "
        "'vtable for QQuickBasicDial', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

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
    Calls Qt's 'void QQuickBasicDial::paint(QPainter *painter)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbasicdial.html#paint

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickBasicDial::paint(QPainter *painter)
    ritual = 'ritual_ZN15QQuickBasicDial5paintEP8QPainter'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickBasicDial5paintEP8QPainter'
    self.uglySide.call(ritual, self._addressOf(painter))
