"""
QQuickGraphsTextureData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/qquickgraphstexturedata_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickGraphsTextureData to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QColor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']


class QQuickGraphsTextureData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickGraphsTextureData: a plain Python object
  standing in front of one C++ QQuickGraphsTextureData.

  What exists
  -----------

  Every function of Qt's QQuickGraphsTextureData that has a ritual and that
  Python can call so far, 2 names in all: 'metaObject', 'linearInterpolate'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickGraphsTextureData::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickGraphsTextureData::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickGraphsTextureData::~QQuickGraphsTextureData()': the
    destructor: Python never removes a C++ QQuickGraphsTextureData.

  What has no ritual
  ------------------

  5 of the 10 functions Qt declares: 2 not a gap; 2 leans on
  'QQuickGraphsTextureData; 1 Qt's library has no name for it, and its code
  in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QQuickGraphsTextureData is created at the first use, not by
    'QQuickGraphsTextureData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickGraphsTextureData.
  - Qt tells when it has removed the C++ QQuickGraphsTextureData. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickGraphsTextureData that has no cute function yet,
    '__init__', 'createGradient', holds a function that raises
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
  __qt_class__ = 'QQuickGraphsTextureData'

  #  A C++ QQuickGraphsTextureData Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickGraphsTextureData'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickGraphsTextureData::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphstexturedata.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickGraphsTextureData::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickGraphsTextureData10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
    Qt's 'QQuickGraphsTextureData::QQuickGraphsTextureData()': leans on
    'QQuickGraphsTextureData::qt_metacall(QMetaObject::Call, int, void**)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickGraphsTextureData.__init__' has no cute function yet. Qt's "
        "'QQuickGraphsTextureData::QQuickGraphsTextureData()': leans on "
        "'QQuickGraphsTextureData::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  @overload(QColor, QColor, float)
  def linearInterpolate(
      self,
      startColor: QColor,
      endColor: QColor,
      value: float,
  ) -> QColor:
    """
    Calls Qt's 'QColor QQuickGraphsTextureData::linearInterpolate(QColor
    startColor, QColor endColor, float value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphstexturedata.html#linearInterpolate

    Parameters
    ----------

    startColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    endColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    value : float
      Passed on as it is.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickGraphsTextureData::linearInterpolate(QColor startColor,
    #      QColor endColor, float value)
    address = self.uglySide.call(
        'ritual_ZN23QQuickGraphsTextureData17linearInterpolateE6QColorS0_f',
        self._valueOf(startColor), self._valueOf(endColor), value,
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @staticmethod
  def createGradient(*__, **_) -> Never:
    """
    Qt's 'void QQuickGraphsTextureData::createGradient(QLinearGradient
    gradient)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'QGraphs3DCreateGradient'.
    """
    raise NotImplementedError(
        "'QQuickGraphsTextureData.createGradient' has no cute function yet. "
        "Qt's 'void QQuickGraphsTextureData::createGradient(QLinearGradient "
        "gradient)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'QGraphs3DCreateGradient'.")
