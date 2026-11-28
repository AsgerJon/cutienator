"""
QQuickGraphsColor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/qquickgraphscolor_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickGraphsColor to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QColor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']


class QQuickGraphsColor(QObject):
  """
  The cute side of Qt's QQuickGraphsColor: a plain Python object standing in
  front of one C++ QQuickGraphsColor.

  It is built on the cute 'QObject', as Qt's QQuickGraphsColor is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickGraphsColor that has a ritual and that Python
  can call so far, 3 names in all: 'metaObject', 'color', 'colorChanged'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickGraphsColor::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickGraphsColor::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickGraphsColor::~QQuickGraphsColor()': the destructor: Python
    never removes a C++ QQuickGraphsColor.

  What has no ritual
  ------------------

  5 of the 11 functions Qt declares: 3 leans on 'QQuickGraphsColor; 2 not a
  gap.

  What to expect
  --------------

  - The C++ QQuickGraphsColor is created at the first use, not by
    'QQuickGraphsColor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickGraphsColor.
  - Qt tells when it has removed the C++ QQuickGraphsColor. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickGraphsColor that has no cute function yet,
    '__init__', 'setColor', holds a function that raises
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
  __qt_class__ = 'QQuickGraphsColor'

  #  A C++ QQuickGraphsColor Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickGraphsColor'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickGraphsColor::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphscolor.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickGraphsColor::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickGraphsColor10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickGraphsColor::color() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphscolor.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickGraphsColor::color() const
    address = self.uglySide.call('ritual_ZNK17QQuickGraphsColor5colorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

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
    Qt's 'QQuickGraphsColor::QQuickGraphsColor(QObject *parent)': leans on
    'QQuickGraphsColor::qt_metacall(QMetaObject::Call, int, void**)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQuickGraphsColor.__init__' has no cute function yet. Qt's "
        "'QQuickGraphsColor::QQuickGraphsColor(QObject *parent)': leans on "
        "'QQuickGraphsColor::qt_metacall(QMetaObject::Call, int, void**)', "
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

  @overload(QColor)
  def colorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickGraphsColor::colorChanged(QColor color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphscolor.html#colorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickGraphsColor::colorChanged(QColor color)
    self.uglySide.call(
        'ritual_ZN17QQuickGraphsColor12colorChangedE6QColor',
        self._valueOf(color),
    )

  @staticmethod
  def setColor(*__, **_) -> Never:
    """
    Qt's 'void QQuickGraphsColor::setColor(QColor color)': leans on
    'QQuickGraphsColor::colorChanged(QColor)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickGraphsColor.setColor' has no cute function yet. Qt's 'void "
        "QQuickGraphsColor::setColor(QColor color)': leans on "
        "'QQuickGraphsColor::colorChanged(QColor)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")


#  Qt's 'QList<QQuickGraphsColor *>': the list of QQuickGraphsColor, which
#  'QList[QQuickGraphsColor]' gives. It is made here, so that there is one as
#  soon as there can be a QQuickGraphsColor.
QList.createKind(
    QQuickGraphsColor, 'address',
    make='ritual_list_make_QQuickGraphsColor_ptr',
    add='ritual_list_add_QQuickGraphsColor_ptr',
    size='ritual_list_size_QQuickGraphsColor_ptr',
    at='ritual_list_at_QQuickGraphsColor_ptr',
    drop='ritual_list_drop_QQuickGraphsColor_ptr',
)
