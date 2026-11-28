"""
QtPrivate::QCheckedIntegers::AssertReportPolicy binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qcheckedint_impl.h, Qt 6.12.0. Changes made here are lost.
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


class AssertReportPolicy(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtPrivate::QCheckedIntegers::AssertReportPolicy: a
  plain Python object standing in front of one C++
  QtPrivate::QCheckedIntegers::AssertReportPolicy.

  C++ hands a QtPrivate::QCheckedIntegers::AssertReportPolicy around as a
  copy, so every C++ QtPrivate::QCheckedIntegers::AssertReportPolicy behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QtPrivate::QCheckedIntegers::AssertReportPolicy that
  has a ritual and that Python can call so far, 1 name in all: 'check'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QtPrivate::QCheckedIntegers::AssertReportPolicy::~AssertReportPolicy()':
    the destructor: Python removes its C++
    QtPrivate::QCheckedIntegers::AssertReportPolicy by it, and has no other
    use for it.

  What to expect
  --------------

  - The C++ QtPrivate::QCheckedIntegers::AssertReportPolicy is created at the
    first use, not by 'QtPrivate::QCheckedIntegers::AssertReportPolicy(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtPrivate::QCheckedIntegers::AssertReportPolicy back
    gives a copy the ritual made for Python, in a new cute
    QtPrivate::QCheckedIntegers::AssertReportPolicy.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(bool, str, str)
  @overload(bool, str, NoneType)
  @overload(bool, NoneType, str)
  @overload(bool, NoneType, NoneType)
  def check(
      ok: bool,
      where: Optional[str],
      description: Optional[str],
  ) -> None:
    """
    Calls Qt's 'void
    QtPrivate::QCheckedIntegers::AssertReportPolicy::check(bool ok, const
    char *where, const char *description)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qcheckedintegers-assertreportpolicy.html

    Parameters
    ----------

    ok : bool
      Passed on as it is.

    where : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    description : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  void QtPrivate::QCheckedIntegers::AssertReportPolicy::check(bool ok,
    #      const char *where, const char *description)
    Rituals.call(
        'ritual_ZN9QtPrivate16QCheckedIntegers18AssertReportPolicy5checkEbP'
        'KcS3_',
        ok, CuteMixin._bytesOf(where), CuteMixin._bytesOf(description),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtPrivate::QCheckedIntegers::AssertReportPolicy'

  #  Qt's '~QtPrivate::QCheckedIntegers::AssertReportPolicy()'. Naming it
  #  makes this a value class: Python owns every C++
  #  QtPrivate::QCheckedIntegers::AssertReportPolicy behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN9QtPrivate16QCheckedIntegers18AssertReportPolicyD1Ev')

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
