"""
QTest::QTouchEventWidgetSequence binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qtestsupport_widgets.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtGui import QTest

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPoint, QPointF
  from ..QtGui import QPointingDevice
  from . import QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']
  QPointingDevice = WAIT['QPointingDevice']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTouchEventWidgetSequence(QTest.QTouchEventSequence):
  """
  The cute side of Qt's QTest::QTouchEventWidgetSequence: a plain Python
  object standing in front of one C++ QTest::QTouchEventWidgetSequence.

  It is built on the cute 'QTest::QTouchEventSequence', as Qt's
  QTest::QTouchEventWidgetSequence is built on Qt's
  QTest::QTouchEventSequence, and has everything that class has.

  C++ hands a QTest::QTouchEventWidgetSequence around as a copy, so every C++
  QTest::QTouchEventWidgetSequence behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QTest::QTouchEventWidgetSequence that has a ritual
  and that Python can call so far, 2 names in all: 'commit', 'mapToScreen'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTest::QTouchEventWidgetSequence::~QTouchEventWidgetSequence()':
    the destructor: Python removes its C++ QTest::QTouchEventWidgetSequence
    by it, and has no other use for it.
  - Qt's 'QTouchEventWidgetSequence
    &QTest::QTouchEventWidgetSequence::press(int touchId, const QPoint &pt,
    QWidget *widget)': gives a type Python has no way to take yet.
  - Qt's 'QTouchEventWidgetSequence
    &QTest::QTouchEventWidgetSequence::move(int touchId, const QPoint &pt,
    QWidget *widget)': gives a type Python has no way to take yet.
  - Qt's 'QTouchEventWidgetSequence
    &QTest::QTouchEventWidgetSequence::release(int touchId, const QPoint &pt,
    QWidget *widget)': gives a type Python has no way to take yet.
  - Qt's 'QTouchEventWidgetSequence
    &QTest::QTouchEventWidgetSequence::stationary(int touchId)': gives a type
    Python has no way to take yet.

  What to expect
  --------------

  - The C++ QTest::QTouchEventWidgetSequence is created at the first use, not
    by 'QTest::QTouchEventWidgetSequence(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTest::QTouchEventWidgetSequence back gives a copy
    the ritual made for Python, in a new cute
    QTest::QTouchEventWidgetSequence.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTest::QTouchEventWidgetSequence'

  #  A C++ QTest::QTouchEventWidgetSequence Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTest_QTouchEventWidgetSequence'

  #  Qt's '~QTest::QTouchEventWidgetSequence()'. Naming it makes this a value
  #  class: Python owns every C++ QTest::QTouchEventWidgetSequence behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN5QTest25QTouchEventWidgetSequenceD1Ev'

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

  @overload(QWidget, QPointingDevice, bool)
  @overload(QWidget, NoneType, bool)
  @overload(NoneType, QPointingDevice, bool)
  @overload(NoneType, NoneType, bool)
  def __init__(
      self,
      widget: Optional[QWidget],
      aDevice: Optional[QPointingDevice],
      autoCommit: bool,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QTest::QTouchEventWidgetSequence::QTouchEventWidgetSequence(QWidget
    *widget, QPointingDevice *aDevice, bool autoCommit)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtest-qtoucheventwidgetsequence.html

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    aDevice : Optional[QPointingDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    autoCommit : bool
      Passed on as it is.
    """
    #  QTest::QTouchEventWidgetSequence::QTouchEventWidgetSequence(QWidget
    #      *widget, QPointingDevice *aDevice, bool autoCommit)
    self._noteCreation(QTouchEventWidgetSequence, lambda: Rituals.call(
        'ritual_ZN5QTest25QTouchEventWidgetSequenceC1EP7QWidgetP15QPointing'
        'Deviceb',
        self._addressOf(widget), self._addressOf(aDevice), autoCommit,
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

  @overload()
  @overload(bool)
  def commit(self, processEvents: bool = True) -> bool:
    """
    Calls Qt's 'bool QTest::QTouchEventWidgetSequence::commit(bool
    processEvents)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtest-qtoucheventwidgetsequence.html#commit

    Parameters
    ----------

    processEvents : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  bool QTest::QTouchEventWidgetSequence::commit(bool processEvents)
    ritual = 'ritual_ZN5QTest25QTouchEventWidgetSequence6commitEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN5QTest25QTouchEventWidgetSequence6commitEb'
    return self.uglySide.call(ritual, processEvents)

  @overload(QWidget, QPoint)
  @overload(NoneType, QPoint)
  def mapToScreen(self, widget: Optional[QWidget], pt: QPoint) -> QPointF:
    """
    Calls Qt's 'QPointF QTest::QTouchEventWidgetSequence::mapToScreen(QWidget
    *widget, const QPoint &pt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtest-qtoucheventwidgetsequence.html#mapToScreen

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pt : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QTest::QTouchEventWidgetSequence::mapToScreen(QWidget *widget,
    #      const QPoint &pt)
    address = self.uglySide.call(
        'ritual_ZN5QTest25QTouchEventWidgetSequence11mapToScreenEP7QWidgetR'
        'K6QPoint',
        self._addressOf(widget), self._valueOf(pt),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)
