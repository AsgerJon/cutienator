"""
QTextFramePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qtextobject_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QTextFramePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QTextObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QChar
  from . import QTextDocument, QTextFrame
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QChar = WAIT['QChar']
  QTextDocument = WAIT['QTextDocument']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextFramePrivate(QTextObjectPrivate):
  """
  The cute side of Qt's QTextFramePrivate: a plain Python object standing in
  front of one C++ QTextFramePrivate.

  It is built on the cute 'QTextObjectPrivate', as Qt's QTextFramePrivate is
  built on Qt's QTextObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTextFramePrivate that has a ritual and that Python
  can call so far, 4 names in all: 'q_func', 'fragmentAdded',
  'fragmentRemoved', 'remove_me'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QTextFrame *QTextFramePrivate::q_func() const': takes in
    Python what 'QTextFrame *QTextFramePrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QTextFramePrivate is created at the first use, not by
    'QTextFramePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTextFramePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextFramePrivate'

  #  A C++ QTextFramePrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTextFramePrivate'

  #  The functions Qt calls itself that QTextFramePrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'fragmentAdded': (
          ('_ZN17QTextFramePrivate13fragmentAddedE5QCharj',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QChar'),
               ('unsigned int', 'number', ''),
           )),
      ),
      'fragmentRemoved': (
          ('_ZN17QTextFramePrivate15fragmentRemovedE5QCharj',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QChar'),
               ('unsigned int', 'number', ''),
           )),
      ),
  }

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

  @overload(QTextDocument)
  @overload(NoneType)
  def __init__(self, doc: Optional[QTextDocument]) -> None:
    """
    Notes what was given, for Qt's
    'QTextFramePrivate::QTextFramePrivate(QTextDocument *doc)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextframeprivate.html#QTextFramePrivate

    Parameters
    ----------

    doc : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QTextFramePrivate::QTextFramePrivate(QTextDocument *doc)
    self._noteCreation(QTextFramePrivate, lambda: Rituals.call(
        'ritual_ZN17QTextFramePrivateC1EP13QTextDocument',
        self._addressOf(doc),
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

  def q_func(self) -> Optional[QTextFrame]:
    """
    Calls Qt's 'QTextFrame *QTextFramePrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextframeprivate.html#q_func

    Returns
    -------

    Optional[QTextFrame]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextFrame *QTextFramePrivate::q_func()
    address = self.uglySide.call('ritual_ZN17QTextFramePrivate6q_funcEv')
    from . import QTextFrame
    return QTextFrame._cuteAt(address)

  @overload(QChar, int)
  def fragmentAdded(self, type: QChar, fragment: int) -> None:
    """
    Calls Qt's 'void QTextFramePrivate::fragmentAdded(QChar type, uint
    fragment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextframeprivate.html#fragmentAdded

    Parameters
    ----------

    type : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    fragment : int
      Passed on as it is.
    """
    #  void QTextFramePrivate::fragmentAdded(QChar type, uint fragment)
    ritual = 'ritual_ZN17QTextFramePrivate13fragmentAddedE5QCharj'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QTextFramePrivate13fragmentAddedE5QCharj'
    self.uglySide.call(ritual, self._valueOf(type), fragment)

  @overload(QChar, int)
  def fragmentRemoved(self, type: QChar, fragment: int) -> None:
    """
    Calls Qt's 'void QTextFramePrivate::fragmentRemoved(QChar type, uint
    fragment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextframeprivate.html#fragmentRemoved

    Parameters
    ----------

    type : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    fragment : int
      Passed on as it is.
    """
    #  void QTextFramePrivate::fragmentRemoved(QChar type, uint fragment)
    ritual = 'ritual_ZN17QTextFramePrivate15fragmentRemovedE5QCharj'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QTextFramePrivate15fragmentRemovedE5QCharj'
    self.uglySide.call(ritual, self._valueOf(type), fragment)

  def remove_me(self) -> None:
    """
    Calls Qt's 'void QTextFramePrivate::remove_me()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextframeprivate.html#remove_me
    """
    #  void QTextFramePrivate::remove_me()
    self.uglySide.call('ritual_ZN17QTextFramePrivate9remove_meEv')
