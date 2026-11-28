"""
QQuickSelectionRectangleAttached binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickselectionrectangle_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickSelectionRectangleAttached to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQuickSelectionRectangle
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickSelectionRectangle = WAIT['QQuickSelectionRectangle']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickSelectionRectangleAttached(QObject):
  """
  The cute side of Qt's QQuickSelectionRectangleAttached: a plain Python
  object standing in front of one C++ QQuickSelectionRectangleAttached.

  It is built on the cute 'QObject', as Qt's QQuickSelectionRectangleAttached
  is built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickSelectionRectangleAttached that has a ritual
  and that Python can call so far, 8 names in all: 'metaObject', 'tr',
  'control', 'setControl', 'dragging', 'setDragging', 'controlChanged',
  'draggingChanged'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickSelectionRectangleAttached::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QQuickSelectionRectangleAttached::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickSelectionRectangleAttached is created at the first use, not
    by 'QQuickSelectionRectangleAttached(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickSelectionRectangleAttached.
  - Qt tells when it has removed the C++ QQuickSelectionRectangleAttached.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QQuickSelectionRectangleAttached::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectionrectangleattached.html#tr

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
    #  QString QQuickSelectionRectangleAttached::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN32QQuickSelectionRectangleAttached2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickSelectionRectangleAttached'

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
    *QQuickSelectionRectangleAttached::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectionrectangleattached.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickSelectionRectangleAttached::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK32QQuickSelectionRectangleAttached10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def control(self) -> Optional[QQuickSelectionRectangle]:
    """
    Calls Qt's 'QQuickSelectionRectangle
    *QQuickSelectionRectangleAttached::control() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectionrectangleattached.html#control

    Returns
    -------

    Optional[QQuickSelectionRectangle]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickSelectionRectangle *QQuickSelectionRectangleAttached::control()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK32QQuickSelectionRectangleAttached7controlEv',
    )
    from . import QQuickSelectionRectangle
    return QQuickSelectionRectangle._cuteAt(address)

  def dragging(self) -> bool:
    """
    Calls Qt's 'bool QQuickSelectionRectangleAttached::dragging() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectionrectangleattached.html#dragging
    """
    #  bool QQuickSelectionRectangleAttached::dragging() const
    return self.uglySide.call(
        'ritual_ZNK32QQuickSelectionRectangleAttached8draggingEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickSelectionRectangle)
  @overload(NoneType)
  def setControl(self, control: Optional[QQuickSelectionRectangle]) -> None:
    """
    Calls Qt's 'void
    QQuickSelectionRectangleAttached::setControl(QQuickSelectionRectangle
    *control)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectionrectangleattached.html#setControl

    Parameters
    ----------

    control : Optional[QQuickSelectionRectangle]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSelectionRectangleAttached::setControl(
    #      QQuickSelectionRectangle *control)
    self.uglySide.call(
        'ritual_ZN32QQuickSelectionRectangleAttached10setControlEP24QQuickS'
        'electionRectangle',
        self._addressOf(control),
    )

  @overload(bool)
  def setDragging(self, dragging: bool) -> None:
    """
    Calls Qt's 'void QQuickSelectionRectangleAttached::setDragging(bool
    dragging)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectionrectangleattached.html#setDragging

    Parameters
    ----------

    dragging : bool
      Passed on as it is.
    """
    #  void QQuickSelectionRectangleAttached::setDragging(bool dragging)
    self.uglySide.call(
        'ritual_ZN32QQuickSelectionRectangleAttached11setDraggingEb',
        dragging,
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

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's
    'QQuickSelectionRectangleAttached::QQuickSelectionRectangleAttached(
    QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectionrectangleattached.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickSelectionRectangleAttached::
    #      QQuickSelectionRectangleAttached(QObject *parent)
    self._noteCreation(
        QQuickSelectionRectangleAttached, lambda: Rituals.call(
            'ritual_ZN32QQuickSelectionRectangleAttachedC1EP7QObject',
            self._addressOf(parent, 'QObject'),
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

  def controlChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSelectionRectangleAttached::controlChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectionrectangleattached.html
    """
    #  void QQuickSelectionRectangleAttached::controlChanged()
    self.uglySide.call(
        'ritual_ZN32QQuickSelectionRectangleAttached14controlChangedEv',
    )

  def draggingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSelectionRectangleAttached::draggingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectionrectangleattached.html
    """
    #  void QQuickSelectionRectangleAttached::draggingChanged()
    self.uglySide.call(
        'ritual_ZN32QQuickSelectionRectangleAttached15draggingChangedEv',
    )
