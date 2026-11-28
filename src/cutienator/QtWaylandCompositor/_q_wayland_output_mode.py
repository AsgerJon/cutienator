"""
QWaylandOutputMode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/qwaylandoutputmode.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QSize
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSize = WAIT['QSize']


class QWaylandOutputMode(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWaylandOutputMode: a plain Python object standing in
  front of one C++ QWaylandOutputMode.

  C++ hands a QWaylandOutputMode around as a copy, so every C++
  QWaylandOutputMode behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QWaylandOutputMode that has a ritual and that Python
  can call so far, 6 names in all: '__eq__', '__ne__', 'isValid', 'size',
  'refreshRate', 'setSize'. It can be made from Python, in 3 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWaylandOutputMode::~QWaylandOutputMode()': the destructor: Python
    removes its C++ QWaylandOutputMode by it, and has no other use for it.
  - Qt's 'QWaylandOutputMode &QWaylandOutputMode::operator=(const
    QWaylandOutputMode &other)': assignment: Python binds a name and has no
    operator for it.

  What to expect
  --------------

  - The C++ QWaylandOutputMode is created at the first use, not by
    'QWaylandOutputMode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QWaylandOutputMode back gives a copy the ritual made
    for Python, in a new cute QWaylandOutputMode.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandOutputMode'

  #  Qt's '~QWaylandOutputMode()'. Naming it makes this a value class: Python
  #  owns every C++ QWaylandOutputMode behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QWaylandOutputModeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QWaylandOutputMode::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandoutputmode.html#isValid
    """
    #  bool QWaylandOutputMode::isValid() const
    return self.uglySide.call('ritual_ZNK18QWaylandOutputMode7isValidEv')

  def size(self) -> QSize:
    """
    Calls Qt's 'QSize QWaylandOutputMode::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandoutputmode.html#size

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QWaylandOutputMode::size() const
    address = self.uglySide.call('ritual_ZNK18QWaylandOutputMode4sizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def refreshRate(self) -> int:
    """
    Calls Qt's 'int QWaylandOutputMode::refreshRate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandoutputmode.html#refreshRate
    """
    #  int QWaylandOutputMode::refreshRate() const
    return self.uglySide.call(
        'ritual_ZNK18QWaylandOutputMode11refreshRateEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSize)
  def setSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void QWaylandOutputMode::setSize(const QSize &size)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandoutputmode.html#setSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QWaylandOutputMode::setSize(const QSize &size)
    self.uglySide.call(
        'ritual_ZN18QWaylandOutputMode7setSizeERK5QSize',
        self._valueOf(size),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QWaylandOutputMode) -> bool:
    """
    Calls Qt's 'bool QWaylandOutputMode::operator==(const QWaylandOutputMode
    &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandoutputmode.html#operator==

    Parameters
    ----------

    other : QWaylandOutputMode
      Passed on as a value: Qt reads the C++ QWaylandOutputMode, which stays
      Python's own.
    """
    #  bool QWaylandOutputMode::operator==(const QWaylandOutputMode &other)
    #      const
    return self.uglySide.call(
        'ritual_ZNK18QWaylandOutputModeeqERKS_', self._valueOf(other),
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
  def __ne__(self, other: QWaylandOutputMode) -> bool:
    """
    Calls Qt's 'bool QWaylandOutputMode::operator!=(const QWaylandOutputMode
    &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandoutputmode.html#operator!=

    Parameters
    ----------

    other : QWaylandOutputMode
      Passed on as a value: Qt reads the C++ QWaylandOutputMode, which stays
      Python's own.
    """
    #  bool QWaylandOutputMode::operator!=(const QWaylandOutputMode &other)
    #      const
    return self.uglySide.call(
        'ritual_ZNK18QWaylandOutputModeneERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
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
    'QWaylandOutputMode::QWaylandOutputMode()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandoutputmode.html#QWaylandOutputMode
    """
    #  QWaylandOutputMode::QWaylandOutputMode()
    self._noteCreation(QWaylandOutputMode, lambda: Rituals.call(
        'ritual_ZN18QWaylandOutputModeC1Ev',
    ))

  @overload(QSize, int)
  def __init__(self, size: QSize, refreshRate: int) -> None:
    """
    Notes what was given, for Qt's
    'QWaylandOutputMode::QWaylandOutputMode(const QSize &size, int
    refreshRate)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandoutputmode.html#QWaylandOutputMode

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    refreshRate : int
      Passed on as it is.
    """
    #  QWaylandOutputMode::QWaylandOutputMode(const QSize &size, int
    #      refreshRate)
    self._noteCreation(QWaylandOutputMode, lambda: Rituals.call(
        'ritual_ZN18QWaylandOutputModeC1ERK5QSizei',
        self._valueOf(size), refreshRate,
    ))

  @overload(THIS)
  def __init__(self, other: QWaylandOutputMode) -> None:
    """
    Notes what was given, for Qt's
    'QWaylandOutputMode::QWaylandOutputMode(const QWaylandOutputMode
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandoutputmode.html#QWaylandOutputMode

    Parameters
    ----------

    other : QWaylandOutputMode
      Passed on as a value: Qt reads the C++ QWaylandOutputMode, which stays
      Python's own.
    """
    #  QWaylandOutputMode::QWaylandOutputMode(const QWaylandOutputMode
    #      &other)
    self._noteCreation(QWaylandOutputMode, lambda: Rituals.call(
        'ritual_ZN18QWaylandOutputModeC1ERKS_', self._valueOf(other),
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


#  Qt's 'QList<QWaylandOutputMode>': the list of QWaylandOutputMode, which
#  'QList[QWaylandOutputMode]' gives. It is made here, so that there is one
#  as soon as there can be a QWaylandOutputMode.
QList.createKind(
    QWaylandOutputMode, 'value',
    make='ritual_list_make_QWaylandOutputMode',
    add='ritual_list_add_QWaylandOutputMode',
    size='ritual_list_size_QWaylandOutputMode',
    at='ritual_list_at_QWaylandOutputMode',
    drop='ritual_list_drop_QWaylandOutputMode',
)
