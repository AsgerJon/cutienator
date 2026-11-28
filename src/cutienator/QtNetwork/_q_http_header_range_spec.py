"""
QHttpHeaderRangeSpec binding of the Qt C++
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
  from ..QtCore import QDebug
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDebug = WAIT['QDebug']


class QHttpHeaderRangeSpec(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QHttpHeaderRangeSpec: a plain Python object standing
  in front of one C++ QHttpHeaderRangeSpec.

  C++ hands a QHttpHeaderRangeSpec around as a copy, so every C++
  QHttpHeaderRangeSpec behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QHttpHeaderRangeSpec that has a ritual and that
  Python can call so far, 4 names in all: 'isValid', '__rlshift__', '__eq__',
  '__ne__'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHttpHeaderRangeSpec::~QHttpHeaderRangeSpec()': the destructor:
    Python removes its C++ QHttpHeaderRangeSpec by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QHttpHeaderRangeSpec is created at the first use, not by
    'QHttpHeaderRangeSpec(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QHttpHeaderRangeSpec back gives a copy the ritual
    made for Python, in a new cute QHttpHeaderRangeSpec.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHttpHeaderRangeSpec'

  #  Qt's '~QHttpHeaderRangeSpec()'. Naming it makes this a value class:
  #  Python owns every C++ QHttpHeaderRangeSpec behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QHttpHeaderRangeSpecD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QHttpHeaderRangeSpec::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpheaderrangespec.html#isValid
    """
    #  bool QHttpHeaderRangeSpec::isValid() const
    return self.uglySide.call('ritual_ZNK20QHttpHeaderRangeSpec7isValidEv')

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
    Calls Qt's 'QDebug operator<<(QDebug debug, const QHttpHeaderRangeSpec
    &range)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpheaderrangespec.html#operator<<

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
    #  QDebug operator<<(QDebug debug, const QHttpHeaderRangeSpec &range)
    address = Rituals.call(
        'ritual_Zls6QDebugRK20QHttpHeaderRangeSpec',
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
  def __eq__(self, rhs: QHttpHeaderRangeSpec) -> bool:
    """
    Calls Qt's 'bool operator==(const QHttpHeaderRangeSpec &lhs, const
    QHttpHeaderRangeSpec &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpheaderrangespec.html#operator==

    Parameters
    ----------

    rhs : QHttpHeaderRangeSpec
      Passed on as a value: Qt reads the C++ QHttpHeaderRangeSpec, which
      stays Python's own.
    """
    #  bool operator==(const QHttpHeaderRangeSpec &lhs, const
    #      QHttpHeaderRangeSpec &rhs)
    return Rituals.call(
        'ritual_ZeqRK20QHttpHeaderRangeSpecS1_',
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
  def __ne__(self, rhs: QHttpHeaderRangeSpec) -> bool:
    """
    Calls Qt's 'bool operator!=(const QHttpHeaderRangeSpec &lhs, const
    QHttpHeaderRangeSpec &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpheaderrangespec.html#operator!=

    Parameters
    ----------

    rhs : QHttpHeaderRangeSpec
      Passed on as a value: Qt reads the C++ QHttpHeaderRangeSpec, which
      stays Python's own.
    """
    #  bool operator!=(const QHttpHeaderRangeSpec &lhs, const
    #      QHttpHeaderRangeSpec &rhs)
    return Rituals.call(
        'ritual_ZneRK20QHttpHeaderRangeSpecS1_',
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
