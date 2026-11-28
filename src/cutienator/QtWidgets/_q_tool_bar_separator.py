"""
QToolBarSeparator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qtoolbarseparator_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QToolBarSeparator to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import Qt
from . import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QSize
  from ..QtGui import QPaintEvent
  from . import QStyleOption
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPaintEvent = WAIT['QPaintEvent']
  QStyleOption = WAIT['QStyleOption']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QToolBarSeparator(QWidget):
  """
  The cute side of Qt's QToolBarSeparator: a plain Python object standing in
  front of one C++ QToolBarSeparator.

  It is built on the cute 'QWidget', as Qt's QToolBarSeparator is built on
  Qt's QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QToolBarSeparator that has a ritual and that Python
  can call so far, 6 names in all: 'metaObject', 'orientation', 'sizeHint',
  'paintEvent', 'initStyleOption', 'setOrientation'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QToolBarSeparator::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QToolBarSeparator::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  4 of the 12 functions Qt declares: 2 not a gap; 2 leans on
  'QToolBarSeparator.

  What to expect
  --------------

  - The C++ QToolBarSeparator is created at the first use, not by
    'QToolBarSeparator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QToolBarSeparator.
  - Qt tells when it has removed the C++ QToolBarSeparator. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QToolBarSeparator that has no cute function yet,
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
  __qt_class__ = 'QToolBarSeparator'

  #  A C++ QToolBarSeparator Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QToolBarSeparator'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QToolBarSeparator::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbarseparator.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QToolBarSeparator::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QToolBarSeparator10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def orientation(self) -> Qt.Orientation:
    """
    Calls Qt's 'Qt::Orientation QToolBarSeparator::orientation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbarseparator.html#orientation

    Returns
    -------

    Qt.Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Orientation(number)'
      gives.
    """
    #  Qt::Orientation QToolBarSeparator::orientation() const
    return Qt.Orientation(self.uglySide.call(
        'ritual_ZNK17QToolBarSeparator11orientationEv',
    ))

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QToolBarSeparator::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbarseparator.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QToolBarSeparator::sizeHint() const
    ritual = 'ritual_ZNK17QToolBarSeparator8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QToolBarSeparator8sizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.Orientation)
  def setOrientation(self, orientation: Qt.Orientation) -> None:
    """
    Calls Qt's 'void QToolBarSeparator::setOrientation(Qt::Orientation
    orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolbarseparator.html#setOrientation

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  void QToolBarSeparator::setOrientation(Qt::Orientation orientation)
    self.uglySide.call(
        'ritual_ZN17QToolBarSeparator14setOrientationEN2Qt11OrientationE',
        orientation.value,
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
    Qt's 'QToolBarSeparator::QToolBarSeparator(QToolBar *parent)': leans on
    'QToolBarSeparator::qt_metacall(QMetaObject::Call, int, void**)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QToolBarSeparator.__init__' has no cute function yet. Qt's "
        "'QToolBarSeparator::QToolBarSeparator(QToolBar *parent)': leans on "
        "'QToolBarSeparator::qt_metacall(QMetaObject::Call, int, void**)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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
    Calls Qt's 'void QToolBarSeparator::paintEvent(QPaintEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbarseparator.html#paintEvent

    Parameters
    ----------

    a0 : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QToolBarSeparator::paintEvent(QPaintEvent *a0)
    ritual = 'ritual_ZN17QToolBarSeparator10paintEventEP11QPaintEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QToolBarSeparator10paintEventEP11QPaintEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QStyleOption)
  @overload(NoneType)
  def initStyleOption(self, option: Optional[QStyleOption]) -> None:
    """
    Calls Qt's 'void QToolBarSeparator::initStyleOption(QStyleOption *option)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolbarseparator.html#initStyleOption

    Parameters
    ----------

    option : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QToolBarSeparator::initStyleOption(QStyleOption *option) const
    self.uglySide.call(
        'ritual_ZNK17QToolBarSeparator15initStyleOptionEP12QStyleOption',
        self._addressOf(option),
    )
