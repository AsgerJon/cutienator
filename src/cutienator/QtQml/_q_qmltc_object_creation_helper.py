"""
QQmltcObjectCreationHelper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmltcobjectcreationhelper_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmltcObjectCreationHelper to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmltcObjectCreationHelper(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmltcObjectCreationHelper: a plain Python object
  standing in front of one C++ QQmltcObjectCreationHelper.

  C++ hands a QQmltcObjectCreationHelper around as a copy, so every C++
  QQmltcObjectCreationHelper behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QQmltcObjectCreationHelper that has a ritual and
  that Python can call so far, 2 names in all: 'offset', 'set'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmltcObjectCreationHelper::QQmltcObjectCreationHelper(QObject
    **data, qsizetype size)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QQmltcObjectCreationHelper::~QQmltcObjectCreationHelper()': the
    destructor: Python removes its C++ QQmltcObjectCreationHelper by it, and
    has no other use for it.

  What has no ritual
  ------------------

  2 of the 7 functions Qt declares: 2 a template.

  What to expect
  --------------

  - The C++ QQmltcObjectCreationHelper is created at the first use, not by
    'QQmltcObjectCreationHelper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmltcObjectCreationHelper back gives a copy the
    ritual made for Python, in a new cute QQmltcObjectCreationHelper.
  - Each name of Qt's QQmltcObjectCreationHelper that has no cute function
    yet, 'get', 'typeCount', holds a function that raises
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
  __qt_class__ = 'QQmltcObjectCreationHelper'

  #  Qt's '~QQmltcObjectCreationHelper()'. Naming it makes this a value
  #  class: Python owns every C++ QQmltcObjectCreationHelper behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN26QQmltcObjectCreationHelperD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def offset(self) -> int:
    """
    Calls Qt's 'qsizetype QQmltcObjectCreationHelper::offset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltcobjectcreationhelper.html#offset
    """
    #  qsizetype QQmltcObjectCreationHelper::offset() const
    return self.uglySide.call(
        'ritual_ZNK26QQmltcObjectCreationHelper6offsetEv',
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

  @overload(THIS, int)
  @overload(NoneType, int)
  def __init__(
      self,
      base: Optional[QQmltcObjectCreationHelper],
      localOffset: int,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmltcObjectCreationHelper::QQmltcObjectCreationHelper(const
    QQmltcObjectCreationHelper *base, qsizetype localOffset)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltcobjectcreationhelper.html

    Parameters
    ----------

    base : Optional[QQmltcObjectCreationHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    localOffset : int
      Passed on as it is.
    """
    #  QQmltcObjectCreationHelper::QQmltcObjectCreationHelper(const
    #      QQmltcObjectCreationHelper *base, qsizetype localOffset)
    self._noteCreation(QQmltcObjectCreationHelper, lambda: Rituals.call(
        'ritual_ZN26QQmltcObjectCreationHelperC1EPKS_x',
        self._addressOf(base), localOffset,
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

  @overload(int, QObject)
  @overload(int, NoneType)
  def set(self, i: int, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQmltcObjectCreationHelper::set(qsizetype i, QObject
    *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltcobjectcreationhelper.html#set

    Parameters
    ----------

    i : int
      Passed on as it is.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmltcObjectCreationHelper::set(qsizetype i, QObject *object)
    self.uglySide.call(
        'ritual_ZN26QQmltcObjectCreationHelper3setExP7QObject',
        i, self._addressOf(object, 'QObject'),
    )

  @staticmethod
  def get(*__, **_) -> Never:
    """
    Qt's 'QQmltcObjectCreationHelper::get': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QQmltcObjectCreationHelper.get' has no cute function yet. Qt's "
        "'QQmltcObjectCreationHelper::get': a template: a pattern and no "
        "single function.")

  @staticmethod
  def typeCount(*__, **_) -> Never:
    """
    Qt's 'QQmltcObjectCreationHelper::typeCount': a template: a pattern and
    no single function.
    """
    raise NotImplementedError(
        "'QQmltcObjectCreationHelper.typeCount' has no cute function yet. "
        "Qt's 'QQmltcObjectCreationHelper::typeCount': a template: a "
        "pattern and no single function.")
