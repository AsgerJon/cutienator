"""
QStaticByteArrayMatcherBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qbytearraymatcher.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QStaticByteArrayMatcherBase(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QStaticByteArrayMatcherBase: a plain Python object
  standing in front of one C++ QStaticByteArrayMatcherBase.

  What exists
  -----------

  Every function of Qt's QStaticByteArrayMatcherBase that has a ritual and
  that Python can call so far, 1 name in all: 'indexOfIn'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStaticByteArrayMatcherBase::~QStaticByteArrayMatcherBase()': the
    destructor: Python never removes a C++ QStaticByteArrayMatcherBase.

  What has no ritual
  ------------------

  1 of the 4 functions Qt declares: 1 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QStaticByteArrayMatcherBase is created at the first use, not by
    'QStaticByteArrayMatcherBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QStaticByteArrayMatcherBase.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStaticByteArrayMatcherBase'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str, int, str, int, int)
  @overload(str, int, NoneType, int, int)
  @overload(NoneType, int, str, int, int)
  @overload(NoneType, int, NoneType, int, int)
  def indexOfIn(
      self,
      needle: Optional[str],
      nlen: int,
      haystack: Optional[str],
      hlen: int,
      from_: int,
  ) -> int:
    """
    Calls Qt's 'qsizetype QStaticByteArrayMatcherBase::indexOfIn(const char
    *needle, size_t nlen, const char *haystack, qsizetype hlen, qsizetype
    from) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstaticbytearraymatcherbase.html#indexOfIn

    Parameters
    ----------

    needle : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    nlen : int
      Passed on as it is.

    haystack : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    hlen : int
      Passed on as it is.

    from_ : int
      Passed on as it is.
    """
    #  qsizetype QStaticByteArrayMatcherBase::indexOfIn(const char *needle,
    #      size_t nlen, const char *haystack, qsizetype hlen, qsizetype from)
    #      const
    return self.uglySide.call(
        'ritual_ZNK27QStaticByteArrayMatcherBase9indexOfInEPKcmS1_xx',
        self._bytesOf(needle), nlen, self._bytesOf(haystack), hlen, from_,
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

  @overload(str, int)
  @overload(NoneType, int)
  def __init__(self, pattern: Optional[str], n: int) -> None:
    """
    Notes what was given, for Qt's
    'QStaticByteArrayMatcherBase::QStaticByteArrayMatcherBase(const char
    *pattern, size_t n)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstaticbytearraymatcherbase.html

    Parameters
    ----------

    pattern : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    n : int
      Passed on as it is.
    """
    #  QStaticByteArrayMatcherBase::QStaticByteArrayMatcherBase(const char
    #      *pattern, size_t n)
    self._noteCreation(QStaticByteArrayMatcherBase, lambda: Rituals.call(
        'ritual_ZN27QStaticByteArrayMatcherBaseC1EPKcm',
        self._bytesOf(pattern), n,
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
