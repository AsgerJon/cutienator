"""
QQuickFusionDial binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickControls2FusionStyleImpl/6.12.0/QtQuickControls2FusionStyleImpl/private/qquickfusiondial_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickFusionDial to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QPainter
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainter = WAIT['QPainter']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickFusionDial(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickFusionDial: a plain Python object standing in
  front of one C++ QQuickFusionDial.

  What exists
  -----------

  Every function of Qt's QQuickFusionDial that has a ritual and that Python
  can call so far, 4 names in all: 'metaObject', 'highlight', 'setHighlight',
  'paint'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickFusionDial::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickFusionDial::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  4 of the 10 functions Qt declares: 2 not a gap; 1 leans on
  'QQuickFusionDial; 1 leans on 'vtable for QQuickFusionDial', which Qt's
  source does not mark for use from outside Qt and has no code for that could
  be taken.

  What to expect
  --------------

  - The C++ QQuickFusionDial is created at the first use, not by
    'QQuickFusionDial(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickFusionDial.
  - Qt tells when it has removed the C++ QQuickFusionDial. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickFusionDial that has no cute function yet,
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
  __qt_class__ = 'QQuickFusionDial'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickFusionDial::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfusiondial.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickFusionDial::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickFusionDial10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def highlight(self) -> bool:
    """
    Calls Qt's 'bool QQuickFusionDial::highlight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfusiondial.html#highlight
    """
    #  bool QQuickFusionDial::highlight() const
    return self.uglySide.call('ritual_ZNK16QQuickFusionDial9highlightEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setHighlight(self, highlight: bool) -> None:
    """
    Calls Qt's 'void QQuickFusionDial::setHighlight(bool highlight)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfusiondial.html#setHighlight

    Parameters
    ----------

    highlight : bool
      Passed on as it is.
    """
    #  void QQuickFusionDial::setHighlight(bool highlight)
    self.uglySide.call(
        'ritual_ZN16QQuickFusionDial12setHighlightEb', highlight,
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
    Qt's 'QQuickFusionDial::QQuickFusionDial(QQuickItem *parent)': leans on
    'vtable for QQuickFusionDial', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickFusionDial.__init__' has no cute function yet. Qt's "
        "'QQuickFusionDial::QQuickFusionDial(QQuickItem *parent)': leans on "
        "'vtable for QQuickFusionDial', which Qt's source does not mark for "
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
    Calls Qt's 'void QQuickFusionDial::paint(QPainter *painter)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfusiondial.html#paint

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFusionDial::paint(QPainter *painter)
    ritual = 'ritual_ZN16QQuickFusionDial5paintEP8QPainter'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickFusionDial5paintEP8QPainter'
    self.uglySide.call(ritual, self._addressOf(painter))
