"""
qdesigner_internal::ZoomProxyWidget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/zoomwidget_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means qdesigner_internal::ZoomProxyWidget to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtWidgets import QGraphicsItem, QGraphicsProxyWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ZoomProxyWidget(QGraphicsProxyWidget):
  """
  The cute side of Qt's qdesigner_internal::ZoomProxyWidget: a plain Python
  object standing in front of one C++ qdesigner_internal::ZoomProxyWidget.

  It is built on the cute 'QGraphicsProxyWidget', as Qt's
  qdesigner_internal::ZoomProxyWidget is built on Qt's QGraphicsProxyWidget,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::ZoomProxyWidget that has a
  ritual and that Python can call so far, 1 name in all: 'itemChange'. It can
  be made from Python, in 1 way; see '__init__'.

  What has no ritual
  ------------------

  4 of the 6 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ qdesigner_internal::ZoomProxyWidget is created at the first use,
    not by 'qdesigner_internal::ZoomProxyWidget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::ZoomProxyWidget.
  - Qt tells when it has removed the C++ qdesigner_internal::ZoomProxyWidget.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::ZoomProxyWidget'

  #  A C++ qdesigner_internal::ZoomProxyWidget Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_qdesigner_internal_ZoomProxyWidget'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @overload()
  @overload(QGraphicsItem)
  @overload(NoneType)
  @overload(QGraphicsItem, Qt.WindowFlags)
  @overload(NoneType, Qt.WindowFlags)
  def __init__(
      self,
      parent: Optional[QGraphicsItem] = None,
      wFlags: Qt.WindowFlags = Qt.WindowFlags(),
  ) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::ZoomProxyWidget::ZoomProxyWidget(QGraphicsItem
    *parent, Qt::WindowFlags wFlags)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-zoomproxywidget.html

    Parameters
    ----------

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    wFlags : Qt.WindowFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.WindowFlags().
    """
    #  qdesigner_internal::ZoomProxyWidget::ZoomProxyWidget(QGraphicsItem
    #      *parent, Qt::WindowFlags wFlags)
    self._noteCreation(ZoomProxyWidget, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal15ZoomProxyWidgetC1EP13QGraphicsItem6'
        'QFlagsIN2Qt10WindowTypeEE',
        self._addressOf(parent, 'QGraphicsItem'), wFlags.value,
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

  @overload(QGraphicsItem.GraphicsItemChange, QVariant)
  def itemChange(
      self,
      change: QGraphicsItem.GraphicsItemChange,
      value: QVariant,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant
    qdesigner_internal::ZoomProxyWidget::itemChange(GraphicsItemChange
    change, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-zoomproxywidget.html#itemChange

    Parameters
    ----------

    change : QGraphicsItem.GraphicsItemChange
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant
    #      qdesigner_internal::ZoomProxyWidget::itemChange(GraphicsItemChange
    #      change, const QVariant &value)
    ritual = (
        'ritual_ZN18qdesigner_internal15ZoomProxyWidget10itemChangeEN13QGra'
        'phicsItem18GraphicsItemChangeERK8QVariant')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal15ZoomProxyWidget10itemChangeEN'
          '13QGraphicsItem18GraphicsItemChangeERK8QVariant')
    address = self.uglySide.call(ritual, change.value, self._valueOf(value))
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)
