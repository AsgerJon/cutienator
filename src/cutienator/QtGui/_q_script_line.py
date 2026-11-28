"""
QScriptLine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qtextengine_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QScriptLine to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QFixed, QTextEngine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTextEngine = WAIT['QTextEngine']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QScriptLine(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QScriptLine: a plain Python object standing in front
  of one C++ QScriptLine.

  C++ hands a QScriptLine around as a copy, so every C++ QScriptLine behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QScriptLine that has a ritual and that Python can
  call so far, 3 names in all: 'height', 'base', 'setDefaultHeight'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QScriptLine::operator+=(const QScriptLine &other)': an
    operator Python has no name for.
  - Qt's 'QScriptLine::~QScriptLine()': the destructor: Python removes its
    C++ QScriptLine by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QScriptLine is created at the first use, not by
    'QScriptLine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QScriptLine back gives a copy the ritual made for
    Python, in a new cute QScriptLine.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScriptLine'

  #  Qt's '~QScriptLine()'. Naming it makes this a value class: Python owns
  #  every C++ QScriptLine behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QScriptLineD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def height(self) -> QFixed:
    """
    Calls Qt's 'QFixed QScriptLine::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscriptline.html#height

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QScriptLine::height() const
    address = self.uglySide.call('ritual_ZNK11QScriptLine6heightEv')
    from . import QFixed
    return QFixed._cuteOwning(address)

  def base(self) -> QFixed:
    """
    Calls Qt's 'QFixed QScriptLine::base() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscriptline.html#base

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QScriptLine::base() const
    address = self.uglySide.call('ritual_ZNK11QScriptLine4baseEv')
    from . import QFixed
    return QFixed._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QTextEngine)
  @overload(NoneType)
  def setDefaultHeight(self, eng: Optional[QTextEngine]) -> None:
    """
    Calls Qt's 'void QScriptLine::setDefaultHeight(QTextEngine *eng)'.

    Qt's own words: https://doc.qt.io/qt-6/qscriptline.html#setDefaultHeight

    Parameters
    ----------

    eng : Optional[QTextEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScriptLine::setDefaultHeight(QTextEngine *eng)
    self.uglySide.call(
        'ritual_ZN11QScriptLine16setDefaultHeightEP11QTextEngine',
        self._addressOf(eng),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QScriptLine::QScriptLine()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qscriptline.html#QScriptLine
    """
    #  QScriptLine::QScriptLine()
    self._noteCreation(QScriptLine, lambda: Rituals.call(
        'ritual_ZN11QScriptLineC1Ev',
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
