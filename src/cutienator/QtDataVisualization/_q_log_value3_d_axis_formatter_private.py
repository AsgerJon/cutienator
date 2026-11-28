"""
QLogValue3DAxisFormatterPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/qlogvalue3daxisformatter_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QLogValue3DAxisFormatterPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from . import QValue3DAxisFormatterPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QLogValue3DAxisFormatter


class QLogValue3DAxisFormatterPrivate(QValue3DAxisFormatterPrivate):
  """
  The cute side of Qt's QLogValue3DAxisFormatterPrivate: a plain Python
  object standing in front of one C++ QLogValue3DAxisFormatterPrivate.

  It is built on the cute 'QValue3DAxisFormatterPrivate', as Qt's
  QLogValue3DAxisFormatterPrivate is built on Qt's
  QValue3DAxisFormatterPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QLogValue3DAxisFormatterPrivate that has a ritual
  and that Python can call so far, 5 names in all: 'metaObject',
  'recalculate', 'positionAt', 'valueAt', 'qptr'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QLogValue3DAxisFormatterPrivate::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QLogValue3DAxisFormatterPrivate::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's
    'QLogValue3DAxisFormatterPrivate::~QLogValue3DAxisFormatterPrivate()':
    the destructor: Python never removes a C++
    QLogValue3DAxisFormatterPrivate.
  - Qt's 'void
    QLogValue3DAxisFormatterPrivate::populateCopy(QValue3DAxisFormatter
    &copy) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 13 functions Qt declares: 2 not a gap; 2 leans on
  'QLogValue3DAxisFormatterPrivate.

  What to expect
  --------------

  - The C++ QLogValue3DAxisFormatterPrivate is created at the first use, not
    by 'QLogValue3DAxisFormatterPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QLogValue3DAxisFormatterPrivate.
  - Qt tells when it has removed the C++ QLogValue3DAxisFormatterPrivate.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QLogValue3DAxisFormatterPrivate that has no cute
    function yet, '__init__', holds a function that raises
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
  __qt_class__ = 'QLogValue3DAxisFormatterPrivate'

  #  A C++ QLogValue3DAxisFormatterPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLogValue3DAxisFormatterPrivate'

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
    *QLogValue3DAxisFormatterPrivate::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlogvalue3daxisformatterprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QLogValue3DAxisFormatterPrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK31QLogValue3DAxisFormatterPrivate10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(float)
  def positionAt(self, value: float) -> float:
    """
    Calls Qt's 'float QLogValue3DAxisFormatterPrivate::positionAt(float
    value) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlogvalue3daxisformatterprivate.html#positionAt

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  float QLogValue3DAxisFormatterPrivate::positionAt(float value) const
    return self.uglySide.call(
        'ritual_ZNK31QLogValue3DAxisFormatterPrivate10positionAtEf', value,
    )

  @overload(float)
  def valueAt(self, position: float) -> float:
    """
    Calls Qt's 'float QLogValue3DAxisFormatterPrivate::valueAt(float
    position) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlogvalue3daxisformatterprivate.html#valueAt

    Parameters
    ----------

    position : float
      Passed on as it is.
    """
    #  float QLogValue3DAxisFormatterPrivate::valueAt(float position) const
    return self.uglySide.call(
        'ritual_ZNK31QLogValue3DAxisFormatterPrivate7valueAtEf', position,
    )

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
    Qt's 'QLogValue3DAxisFormatterPrivate::QLogValue3DAxisFormatterPrivate(
    QLogValue3DAxisFormatter *q)': leans on
    'QLogValue3DAxisFormatterPrivate::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QLogValue3DAxisFormatterPrivate.__init__' has no cute function "
        "yet. Qt's "
        "'QLogValue3DAxisFormatterPrivate::QLogValue3DAxisFormatterPrivate(Q"
        "LogValue3DAxisFormatter *q)': leans on "
        "'QLogValue3DAxisFormatterPrivate::qt_metacall(QMetaObject::Call, "
        "int, void**)', which Qt's source does not mark for use from "
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

  def recalculate(self) -> None:
    """
    Calls Qt's 'void QLogValue3DAxisFormatterPrivate::recalculate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlogvalue3daxisformatterprivate.html#recalculate
    """
    #  void QLogValue3DAxisFormatterPrivate::recalculate()
    self.uglySide.call(
        'ritual_ZN31QLogValue3DAxisFormatterPrivate11recalculateEv',
    )

  def qptr(self) -> Optional[QLogValue3DAxisFormatter]:
    """
    Calls Qt's 'QLogValue3DAxisFormatter
    *QLogValue3DAxisFormatterPrivate::qptr()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlogvalue3daxisformatterprivate.html#qptr

    Returns
    -------

    Optional[QLogValue3DAxisFormatter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLogValue3DAxisFormatter *QLogValue3DAxisFormatterPrivate::qptr()
    address = self.uglySide.call(
        'ritual_ZN31QLogValue3DAxisFormatterPrivate4qptrEv',
    )
    from . import QLogValue3DAxisFormatter
    return QLogValue3DAxisFormatter._cuteAt(address)
