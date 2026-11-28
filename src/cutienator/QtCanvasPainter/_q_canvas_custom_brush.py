"""
QCanvasCustomBrush binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCanvasPainter/qcanvascustombrush.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QDebug
  from ..QtGui import QShader, QVector4D
  from . import QCanvasCustomBrushPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCanvasCustomBrushPrivate = WAIT['QCanvasCustomBrushPrivate']
  QDebug = WAIT['QDebug']
  QShader = WAIT['QShader']
  QVector4D = WAIT['QVector4D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCanvasCustomBrush(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCanvasCustomBrush: a plain Python object standing in
  front of one C++ QCanvasCustomBrush.

  C++ hands a QCanvasCustomBrush around as a copy, so every C++
  QCanvasCustomBrush behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCanvasCustomBrush that has a ritual and that Python
  can call so far, 11 names in all: 'setFragmentShader', 'setVertexShader',
  'isAnimationRunning', 'setAnimationRunning', 'setData1', 'setData2',
  'setData3', 'setData4', '__eq__', '__ne__', '__rlshift__'. It can be made
  from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCanvasCustomBrush &QCanvasCustomBrush::operator=(const
    QCanvasCustomBrush &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QCanvasCustomBrush::QCanvasCustomBrush(QCanvasCustomBrush &&a0)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QCanvasCustomBrush
    &QCanvasCustomBrush::operator=(QCanvasCustomBrush &&other)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'QCanvasCustomBrush::~QCanvasCustomBrush()': the destructor: Python
    removes its C++ QCanvasCustomBrush by it, and has no other use for it.
  - Qt's 'QCanvasBrush QCanvasCustomBrush::operator QCanvasBrush() const': an
    operator Python has no name for.
  - Qt's 'QVariant QCanvasCustomBrush::operator QVariant() const': an
    operator Python has no name for.
  - Qt's 'void QCanvasCustomBrush::swap(QCanvasCustomBrush &other)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QDataStream &operator<<(QDataStream &a0, const QCanvasCustomBrush
    &a1)': takes a type Python has no way to hand over yet.
  - Qt's 'QDataStream &operator>>(QDataStream &a0, QCanvasCustomBrush &a1)':
    an operator between other classes, written inside this one.

  What has no ritual
  ------------------

  1 of the 26 functions Qt declares: 1 leans on 'QCanvasCustomBrushPrivate.

  What to expect
  --------------

  - The C++ QCanvasCustomBrush is created at the first use, not by
    'QCanvasCustomBrush(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCanvasCustomBrush back gives a copy the ritual made
    for Python, in a new cute QCanvasCustomBrush.
  - Each name of Qt's QCanvasCustomBrush that has no cute function yet,
    'detach', 'swap', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCanvasCustomBrush'

  #  Qt's '~QCanvasCustomBrush()'. Naming it makes this a value class: Python
  #  owns every C++ QCanvasCustomBrush behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QCanvasCustomBrushD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isAnimationRunning(self) -> bool:
    """
    Calls Qt's 'bool QCanvasCustomBrush::isAnimationRunning() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvascustombrush.html#isAnimationRunning
    """
    #  bool QCanvasCustomBrush::isAnimationRunning() const
    return self.uglySide.call(
        'ritual_ZNK18QCanvasCustomBrush18isAnimationRunningEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setFragmentShader(self, fragmentShader: str) -> None:
    """
    Calls Qt's 'void QCanvasCustomBrush::setFragmentShader(const QString
    &fragmentShader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvascustombrush.html#setFragmentShader

    Parameters
    ----------

    fragmentShader : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QCanvasCustomBrush::setFragmentShader(const QString
    #      &fragmentShader)
    self.uglySide.call(
        'ritual_ZN18QCanvasCustomBrush17setFragmentShaderERK7QString',
        fragmentShader,
    )

  @overload(QShader)
  def setFragmentShader(self, fragmentShader: QShader) -> None:
    """
    Calls Qt's 'void QCanvasCustomBrush::setFragmentShader(const QShader
    &fragmentShader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvascustombrush.html#setFragmentShader

    Parameters
    ----------

    fragmentShader : QShader
      Passed on as a value: Qt reads the C++ QShader, which stays Python's
      own.
    """
    #  void QCanvasCustomBrush::setFragmentShader(const QShader
    #      &fragmentShader)
    self.uglySide.call(
        'ritual_ZN18QCanvasCustomBrush17setFragmentShaderERK7QShader',
        self._valueOf(fragmentShader),
    )

  @overload(str)
  def setVertexShader(self, vertexShader: str) -> None:
    """
    Calls Qt's 'void QCanvasCustomBrush::setVertexShader(const QString
    &vertexShader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvascustombrush.html#setVertexShader

    Parameters
    ----------

    vertexShader : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QCanvasCustomBrush::setVertexShader(const QString &vertexShader)
    self.uglySide.call(
        'ritual_ZN18QCanvasCustomBrush15setVertexShaderERK7QString',
        vertexShader,
    )

  @overload(QShader)
  def setVertexShader(self, vertexShader: QShader) -> None:
    """
    Calls Qt's 'void QCanvasCustomBrush::setVertexShader(const QShader
    &vertexShader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvascustombrush.html#setVertexShader

    Parameters
    ----------

    vertexShader : QShader
      Passed on as a value: Qt reads the C++ QShader, which stays Python's
      own.
    """
    #  void QCanvasCustomBrush::setVertexShader(const QShader &vertexShader)
    self.uglySide.call(
        'ritual_ZN18QCanvasCustomBrush15setVertexShaderERK7QShader',
        self._valueOf(vertexShader),
    )

  @overload(bool)
  def setAnimationRunning(self, running: bool) -> None:
    """
    Calls Qt's 'void QCanvasCustomBrush::setAnimationRunning(bool running)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvascustombrush.html#setAnimationRunning

    Parameters
    ----------

    running : bool
      Passed on as it is.
    """
    #  void QCanvasCustomBrush::setAnimationRunning(bool running)
    self.uglySide.call(
        'ritual_ZN18QCanvasCustomBrush19setAnimationRunningEb', running,
    )

  @overload(QVector4D)
  def setData1(self, data: QVector4D) -> None:
    """
    Calls Qt's 'void QCanvasCustomBrush::setData1(const QVector4D &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvascustombrush.html#setData1

    Parameters
    ----------

    data : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.
    """
    #  void QCanvasCustomBrush::setData1(const QVector4D &data)
    self.uglySide.call(
        'ritual_ZN18QCanvasCustomBrush8setData1ERK9QVector4D',
        self._valueOf(data),
    )

  @overload(QVector4D)
  def setData2(self, data: QVector4D) -> None:
    """
    Calls Qt's 'void QCanvasCustomBrush::setData2(const QVector4D &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvascustombrush.html#setData2

    Parameters
    ----------

    data : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.
    """
    #  void QCanvasCustomBrush::setData2(const QVector4D &data)
    self.uglySide.call(
        'ritual_ZN18QCanvasCustomBrush8setData2ERK9QVector4D',
        self._valueOf(data),
    )

  @overload(QVector4D)
  def setData3(self, data: QVector4D) -> None:
    """
    Calls Qt's 'void QCanvasCustomBrush::setData3(const QVector4D &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvascustombrush.html#setData3

    Parameters
    ----------

    data : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.
    """
    #  void QCanvasCustomBrush::setData3(const QVector4D &data)
    self.uglySide.call(
        'ritual_ZN18QCanvasCustomBrush8setData3ERK9QVector4D',
        self._valueOf(data),
    )

  @overload(QVector4D)
  def setData4(self, data: QVector4D) -> None:
    """
    Calls Qt's 'void QCanvasCustomBrush::setData4(const QVector4D &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvascustombrush.html#setData4

    Parameters
    ----------

    data : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.
    """
    #  void QCanvasCustomBrush::setData4(const QVector4D &data)
    self.uglySide.call(
        'ritual_ZN18QCanvasCustomBrush8setData4ERK9QVector4D',
        self._valueOf(data),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QCanvasCustomBrush) -> bool:
    """
    Calls Qt's 'bool operator==(const QCanvasCustomBrush &lhs, const
    QCanvasCustomBrush &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvascustombrush.html#operator==

    Parameters
    ----------

    rhs : QCanvasCustomBrush
      Passed on as a value: Qt reads the C++ QCanvasCustomBrush, which stays
      Python's own.
    """
    #  bool operator==(const QCanvasCustomBrush &lhs, const
    #      QCanvasCustomBrush &rhs)
    return Rituals.call(
        'ritual_ZeqRK18QCanvasCustomBrushS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: QCanvasCustomBrush) -> bool:
    """
    Calls Qt's 'bool operator!=(const QCanvasCustomBrush &lhs, const
    QCanvasCustomBrush &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvascustombrush.html#operator!=

    Parameters
    ----------

    rhs : QCanvasCustomBrush
      Passed on as a value: Qt reads the C++ QCanvasCustomBrush, which stays
      Python's own.
    """
    #  bool operator!=(const QCanvasCustomBrush &lhs, const
    #      QCanvasCustomBrush &rhs)
    return Rituals.call(
        'ritual_ZneRK18QCanvasCustomBrushS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(QDebug)
  def __rlshift__(self, a0: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug a0, const QCanvasCustomBrush &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvascustombrush.html#operator<<

    Parameters
    ----------

    a0 : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug a0, const QCanvasCustomBrush &a1)
    address = Rituals.call(
        'ritual_Zls6QDebugRK18QCanvasCustomBrush',
        CuteMixin._valueOf(a0), CuteMixin._valueOf(self),
    )
    from ..QtCore import QDebug
    return QDebug._cuteOwning(address)

  @overload.fallback
  def __rlshift__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasCustomBrush::QCanvasCustomBrush()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvascustombrush.html#QCanvasCustomBrush
    """
    #  QCanvasCustomBrush::QCanvasCustomBrush()
    self._noteCreation(QCanvasCustomBrush, lambda: Rituals.call(
        'ritual_ZN18QCanvasCustomBrushC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QCanvasCustomBrush) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasCustomBrush::QCanvasCustomBrush(const QCanvasCustomBrush &a0)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvascustombrush.html#QCanvasCustomBrush

    Parameters
    ----------

    a0 : QCanvasCustomBrush
      Passed on as a value: Qt reads the C++ QCanvasCustomBrush, which stays
      Python's own.
    """
    #  QCanvasCustomBrush::QCanvasCustomBrush(const QCanvasCustomBrush &a0)
    self._noteCreation(QCanvasCustomBrush, lambda: Rituals.call(
        'ritual_ZN18QCanvasCustomBrushC1ERKS_', self._valueOf(a0),
    ))

  @overload(QCanvasCustomBrushPrivate)
  @overload(NoneType)
  def __init__(self, p: Optional[QCanvasCustomBrushPrivate]) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasCustomBrush::QCanvasCustomBrush(QCanvasCustomBrushPrivate *p)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvascustombrush.html#QCanvasCustomBrush

    Parameters
    ----------

    p : Optional[QCanvasCustomBrushPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QCanvasCustomBrush::QCanvasCustomBrush(QCanvasCustomBrushPrivate *p)
    self._noteCreation(QCanvasCustomBrush, lambda: Rituals.call(
        'ritual_ZN18QCanvasCustomBrushC1EP25QCanvasCustomBrushPrivate',
        self._addressOf(p),
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

  @staticmethod
  def detach(*__, **_) -> Never:
    """
    Qt's 'void QCanvasCustomBrush::detach()': leans on
    'QCanvasCustomBrushPrivate::createPaint(QCanvasPainter*) const', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QCanvasCustomBrush.detach' has no cute function yet. Qt's 'void "
        "QCanvasCustomBrush::detach()': leans on "
        "'QCanvasCustomBrushPrivate::createPaint(QCanvasPainter*) const', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QCanvasCustomBrush::swap(QCanvasCustomBrush &other)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCanvasCustomBrush.swap' has no cute function yet. Qt's 'void "
        "QCanvasCustomBrush::swap(QCanvasCustomBrush &other)': takes a type "
        "Python has no way to hand over yet.")
