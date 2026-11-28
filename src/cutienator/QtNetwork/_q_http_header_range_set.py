"""
QHttpHeaderRangeSet binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qhttpheaders.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QDebug
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDebug = WAIT['QDebug']


class QHttpHeaderRangeSet(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QHttpHeaderRangeSet: a plain Python object standing
  in front of one C++ QHttpHeaderRangeSet.

  C++ hands a QHttpHeaderRangeSet around as a copy, so every C++
  QHttpHeaderRangeSet behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QHttpHeaderRangeSet that has a ritual and that
  Python can call so far, 3 names in all: '__rlshift__', '__eq__', '__ne__'.
  It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHttpHeaderRangeSetPrivate *QHttpHeaderRangeSet::d_func()': gives
    'QHttpHeaderRangeSetPrivate', which has no cute class yet.
  - Qt's 'const QHttpHeaderRangeSetPrivate *QHttpHeaderRangeSet::d_func()
    const': gives 'QHttpHeaderRangeSetPrivate', which has no cute class yet.
  - Qt's 'QHttpHeaderRangeSet::QHttpHeaderRangeSet(QHttpHeaderRangeSet
    &&a0)': takes a type Python has no way to hand over yet.
  - Qt's 'QHttpHeaderRangeSet::QHttpHeaderRangeSet(QSpan<const
    QHttpHeaderRangeSpec> r)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QHttpHeaderRangeSet::QHttpHeaderRangeSet(std::
    initializer_list<QHttpHeaderRangeSpec> r)': takes a type Python has no
    way to hand over yet.
  - Qt's 'QHttpHeaderRangeSet &QHttpHeaderRangeSet::operator=(const
    QHttpHeaderRangeSet &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QHttpHeaderRangeSet
    &QHttpHeaderRangeSet::operator=(QHttpHeaderRangeSet &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QHttpHeaderRangeSet::~QHttpHeaderRangeSet()': the destructor:
    Python removes its C++ QHttpHeaderRangeSet by it, and has no other use
    for it.
  - Qt's 'void QHttpHeaderRangeSet::swap(QHttpHeaderRangeSet &other)': takes
    a type Python has no way to hand over yet.
  - Qt's 'QSpan<const QHttpHeaderRangeSpec> QHttpHeaderRangeSet::ranges()
    const': gives a type Python has no way to take yet.
  - Qt's 'void QHttpHeaderRangeSet::setRanges(QSpan<const
    QHttpHeaderRangeSpec> r)': takes a type Python has no way to hand over
    yet.

  What to expect
  --------------

  - The C++ QHttpHeaderRangeSet is created at the first use, not by
    'QHttpHeaderRangeSet(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QHttpHeaderRangeSet back gives a copy the ritual made
    for Python, in a new cute QHttpHeaderRangeSet.
  - Each name of Qt's QHttpHeaderRangeSet that has no cute function yet,
    'd_func', 'ranges', 'setRanges', 'swap', holds a function that raises
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
  __qt_class__ = 'QHttpHeaderRangeSet'

  #  Qt's '~QHttpHeaderRangeSet()'. Naming it makes this a value class:
  #  Python owns every C++ QHttpHeaderRangeSet behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QHttpHeaderRangeSetD1Ev'

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

  @overload(QDebug)
  def __rlshift__(self, debug: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug debug, const QHttpHeaderRangeSet
    &ranges)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpheaderrangeset.html#operator<<

    Parameters
    ----------

    debug : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug debug, const QHttpHeaderRangeSet &ranges)
    address = Rituals.call(
        'ritual_Zls6QDebugRK19QHttpHeaderRangeSet',
        CuteMixin._valueOf(debug), CuteMixin._valueOf(self),
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

  @overload(THIS)
  def __eq__(self, rhs: QHttpHeaderRangeSet) -> bool:
    """
    Calls Qt's 'bool operator==(const QHttpHeaderRangeSet &lhs, const
    QHttpHeaderRangeSet &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpheaderrangeset.html#operator==

    Parameters
    ----------

    rhs : QHttpHeaderRangeSet
      Passed on as a value: Qt reads the C++ QHttpHeaderRangeSet, which stays
      Python's own.
    """
    #  bool operator==(const QHttpHeaderRangeSet &lhs, const
    #      QHttpHeaderRangeSet &rhs)
    return Rituals.call(
        'ritual_ZeqRK19QHttpHeaderRangeSetS1_',
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
  def __ne__(self, rhs: QHttpHeaderRangeSet) -> bool:
    """
    Calls Qt's 'bool operator!=(const QHttpHeaderRangeSet &lhs, const
    QHttpHeaderRangeSet &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpheaderrangeset.html#operator!=

    Parameters
    ----------

    rhs : QHttpHeaderRangeSet
      Passed on as a value: Qt reads the C++ QHttpHeaderRangeSet, which stays
      Python's own.
    """
    #  bool operator!=(const QHttpHeaderRangeSet &lhs, const
    #      QHttpHeaderRangeSet &rhs)
    return Rituals.call(
        'ritual_ZneRK19QHttpHeaderRangeSetS1_',
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QHttpHeaderRangeSet::QHttpHeaderRangeSet()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpheaderrangeset.html#QHttpHeaderRangeSet
    """
    #  QHttpHeaderRangeSet::QHttpHeaderRangeSet()
    self._noteCreation(QHttpHeaderRangeSet, lambda: Rituals.call(
        'ritual_ZN19QHttpHeaderRangeSetC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QHttpHeaderRangeSet) -> None:
    """
    Notes what was given, for Qt's
    'QHttpHeaderRangeSet::QHttpHeaderRangeSet(const QHttpHeaderRangeSet
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpheaderrangeset.html#QHttpHeaderRangeSet

    Parameters
    ----------

    other : QHttpHeaderRangeSet
      Passed on as a value: Qt reads the C++ QHttpHeaderRangeSet, which stays
      Python's own.
    """
    #  QHttpHeaderRangeSet::QHttpHeaderRangeSet(const QHttpHeaderRangeSet
    #      &other)
    self._noteCreation(QHttpHeaderRangeSet, lambda: Rituals.call(
        'ritual_ZN19QHttpHeaderRangeSetC1ERKS_', self._valueOf(other),
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
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'QHttpHeaderRangeSetPrivate *QHttpHeaderRangeSet::d_func()': gives
      'QHttpHeaderRangeSetPrivate', which has no cute class yet.
    - Qt's 'const QHttpHeaderRangeSetPrivate *QHttpHeaderRangeSet::d_func()
      const': gives 'QHttpHeaderRangeSetPrivate', which has no cute class
      yet.
    """
    raise NotImplementedError(
        "'QHttpHeaderRangeSet.d_func' has no cute function yet. Qt's "
        "'QHttpHeaderRangeSetPrivate *QHttpHeaderRangeSet::d_func()': gives "
        "'QHttpHeaderRangeSetPrivate', which has no cute class yet. Qt's "
        "'const QHttpHeaderRangeSetPrivate *QHttpHeaderRangeSet::d_func() "
        "const': gives 'QHttpHeaderRangeSetPrivate', which has no cute "
        "class yet.")

  @staticmethod
  def ranges(*__, **_) -> Never:
    """
    Qt's 'QSpan<const QHttpHeaderRangeSpec> QHttpHeaderRangeSet::ranges()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QHttpHeaderRangeSet.ranges' has no cute function yet. Qt's "
        "'QSpan<const QHttpHeaderRangeSpec> QHttpHeaderRangeSet::ranges() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def setRanges(*__, **_) -> Never:
    """
    Qt's 'void QHttpHeaderRangeSet::setRanges(QSpan<const
    QHttpHeaderRangeSpec> r)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QHttpHeaderRangeSet.setRanges' has no cute function yet. Qt's "
        "'void QHttpHeaderRangeSet::setRanges(QSpan<const "
        "QHttpHeaderRangeSpec> r)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QHttpHeaderRangeSet::swap(QHttpHeaderRangeSet &other)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QHttpHeaderRangeSet.swap' has no cute function yet. Qt's 'void "
        "QHttpHeaderRangeSet::swap(QHttpHeaderRangeSet &other)': takes a "
        "type Python has no way to hand over yet.")
