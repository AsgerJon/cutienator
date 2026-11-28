"""
QQuickSelectable binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickselectable_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickSelectable to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..QtCore import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPointF, QRectF, QSizeF
  from . import QQuickItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QSizeF = WAIT['QSizeF']


class QQuickSelectable(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickSelectable: a plain Python object standing in
  front of one C++ QQuickSelectable.

  What exists
  -----------

  Every function of Qt's QQuickSelectable that has a ritual and that Python
  can call so far, 9 names in all: 'selectionPointerHandlerTarget',
  'hasSelection', 'startSelection', 'setSelectionStartPos',
  'setSelectionEndPos', 'clearSelection', 'normalizeSelection',
  'selectionRectangle', 'scrollTowardsPoint'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickSelectable::~QQuickSelectable()': the destructor: Python
    never removes a C++ QQuickSelectable.
  - Qt's 'void QQuickSelectable::setCallback(std::function<void
    (CallBackFlag)> func)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QQuickSelectable is created at the first use, not by
    'QQuickSelectable(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickSelectable.
  - Each name of Qt's QQuickSelectable that has no cute function yet,
    'setCallback', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QQuickSelectable, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class CallBackFlag(CuteNum, scoped=True):
    """
    The enum 'QQuickSelectable::CallBackFlag' of Qt, with the 2 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    CancelSelection = Kee[int](0)
    SelectionRectangleChanged = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickSelectable'

  #  A C++ QQuickSelectable Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickSelectable'

  #  The functions Qt calls itself that QQuickSelectable is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'setCallback': (
          'void QQuickSelectable::setCallback(std::function<void '
          '(CallBackFlag)>)',
      ),
  }

  #  The functions Qt calls itself that QQuickSelectable is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'selectionPointerHandlerTarget': (
          ('_ZNK16QQuickSelectable29selectionPointerHandlerTargetEv',
           ('address', 'address', 'QtQuick:QQuickItem'),
           ()),
      ),
      'hasSelection': (
          ('_ZNK16QQuickSelectable12hasSelectionEv',
           ('bool', 'number', ''),
           ()),
      ),
      'startSelection': (
          ('_ZN16QQuickSelectable14startSelectionERK7QPointF6QFlagsIN2Qt16K'
           'eyboardModifierEE',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore:QPointF'),
               ('int', 'flags', 'QtCore:Qt.KeyboardModifier'),
           )),
      ),
      'setSelectionStartPos': (
          ('_ZN16QQuickSelectable20setSelectionStartPosERK7QPointF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QPointF'),
           )),
      ),
      'setSelectionEndPos': (
          ('_ZN16QQuickSelectable18setSelectionEndPosERK7QPointF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QPointF'),
           )),
      ),
      'clearSelection': (
          ('_ZN16QQuickSelectable14clearSelectionEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'normalizeSelection': (
          ('_ZN16QQuickSelectable18normalizeSelectionEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'selectionRectangle': (
          ('_ZNK16QQuickSelectable18selectionRectangleEv',
           ('address', 'value', 'QtCore:QRectF'),
           ()),
      ),
      'scrollTowardsPoint': (
          ('_ZN16QQuickSelectable18scrollTowardsPointERK7QPointFRK6QSizeF',
           ('address', 'value', 'QtCore:QSizeF'),
           (
               ('address', 'value', 'QtCore:QPointF'),
               ('address', 'value', 'QtCore:QSizeF'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def selectionPointerHandlerTarget(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickSelectable::selectionPointerHandlerTarget()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectable.html

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickSelectable::selectionPointerHandlerTarget() const
    address = self._callAs(
        'QQuickSelectable',
        'ritual_ZNK16QQuickSelectable29selectionPointerHandlerTargetEv',
    )
    from . import QQuickItem
    return QQuickItem._cuteAt(address)

  def hasSelection(self) -> bool:
    """
    Calls Qt's 'bool QQuickSelectable::hasSelection() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickselectable.html#hasSelection
    """
    #  bool QQuickSelectable::hasSelection() const
    return self._callAs(
        'QQuickSelectable', 'ritual_ZNK16QQuickSelectable12hasSelectionEv',
    )

  def selectionRectangle(self) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickSelectable::selectionRectangle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectable.html#selectionRectangle

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickSelectable::selectionRectangle() const
    address = self._callAs(
        'QQuickSelectable',
        'ritual_ZNK16QQuickSelectable18selectionRectangleEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPointF)
  def setSelectionStartPos(self, pos: QPointF) -> None:
    """
    Calls Qt's 'void QQuickSelectable::setSelectionStartPos(const QPointF
    &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectable.html#setSelectionStartPos

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QQuickSelectable::setSelectionStartPos(const QPointF &pos)
    self._callAs(
        'QQuickSelectable',
        'ritual_ZN16QQuickSelectable20setSelectionStartPosERK7QPointF',
        self._valueOf(pos, 'QPointF'),
    )

  @overload(QPointF)
  def setSelectionEndPos(self, pos: QPointF) -> None:
    """
    Calls Qt's 'void QQuickSelectable::setSelectionEndPos(const QPointF
    &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectable.html#setSelectionEndPos

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QQuickSelectable::setSelectionEndPos(const QPointF &pos)
    self._callAs(
        'QQuickSelectable',
        'ritual_ZN16QQuickSelectable18setSelectionEndPosERK7QPointF',
        self._valueOf(pos, 'QPointF'),
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

  @overload(QPointF, Qt.KeyboardModifiers)
  def startSelection(
      self,
      pos: QPointF,
      modifiers: Qt.KeyboardModifiers,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickSelectable::startSelection(const QPointF &pos,
    Qt::KeyboardModifiers modifiers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectable.html#startSelection

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.
    """
    #  bool QQuickSelectable::startSelection(const QPointF &pos,
    #      Qt::KeyboardModifiers modifiers)
    return self._callAs(
        'QQuickSelectable',
        'ritual_ZN16QQuickSelectable14startSelectionERK7QPointF6QFlagsIN2Qt'
        '16KeyboardModifierEE',
        self._valueOf(pos, 'QPointF'), modifiers.value,
    )

  def clearSelection(self) -> None:
    """
    Calls Qt's 'void QQuickSelectable::clearSelection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectable.html#clearSelection
    """
    #  void QQuickSelectable::clearSelection()
    self._callAs(
        'QQuickSelectable', 'ritual_ZN16QQuickSelectable14clearSelectionEv',
    )

  def normalizeSelection(self) -> None:
    """
    Calls Qt's 'void QQuickSelectable::normalizeSelection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectable.html#normalizeSelection
    """
    #  void QQuickSelectable::normalizeSelection()
    self._callAs(
        'QQuickSelectable',
        'ritual_ZN16QQuickSelectable18normalizeSelectionEv',
    )

  @overload(QPointF, QSizeF)
  def scrollTowardsPoint(self, pos: QPointF, step: QSizeF) -> QSizeF:
    """
    Calls Qt's 'QSizeF QQuickSelectable::scrollTowardsPoint(const QPointF
    &pos, const QSizeF &step)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectable.html#scrollTowardsPoint

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    step : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QQuickSelectable::scrollTowardsPoint(const QPointF &pos, const
    #      QSizeF &step)
    address = self._callAs(
        'QQuickSelectable',
        'ritual_ZN16QQuickSelectable18scrollTowardsPointERK7QPointFRK6QSize'
        'F',
        self._valueOf(pos, 'QPointF'), self._valueOf(step),
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  @staticmethod
  def setCallback(*__, **_) -> Never:
    """
    Qt's 'void QQuickSelectable::setCallback(std::function<void
    (CallBackFlag)> func)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickSelectable.setCallback' has no cute function yet. Qt's "
        "'void QQuickSelectable::setCallback(std::function<void "
        "(CallBackFlag)> func)': takes a type Python has no way to hand "
        "over yet.")
