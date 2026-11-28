"""
QTextBlockGroupPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qtextobject_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QTextBlockGroupPrivate to be private: it declares the class in a
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

  from . import QTextBlockGroup, QTextDocument
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTextDocument = WAIT['QTextDocument']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextBlockGroupPrivate(QTextObjectPrivate):
  """
  The cute side of Qt's QTextBlockGroupPrivate: a plain Python object
  standing in front of one C++ QTextBlockGroupPrivate.

  It is built on the cute 'QTextObjectPrivate', as Qt's
  QTextBlockGroupPrivate is built on Qt's QTextObjectPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QTextBlockGroupPrivate that has a ritual and that
  Python can call so far, 2 names in all: 'q_func', 'markBlocksDirty'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QTextBlockGroup *QTextBlockGroupPrivate::q_func() const':
    takes in Python what 'QTextBlockGroup *QTextBlockGroupPrivate::q_func()'
    takes.

  What to expect
  --------------

  - The C++ QTextBlockGroupPrivate is created at the first use, not by
    'QTextBlockGroupPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTextBlockGroupPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextBlockGroupPrivate'

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
    'QTextBlockGroupPrivate::QTextBlockGroupPrivate(QTextDocument *doc)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextblockgroupprivate.html#QTextBlockGroupPrivate

    Parameters
    ----------

    doc : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QTextBlockGroupPrivate::QTextBlockGroupPrivate(QTextDocument *doc)
    self._noteCreation(QTextBlockGroupPrivate, lambda: Rituals.call(
        'ritual_ZN22QTextBlockGroupPrivateC1EP13QTextDocument',
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

  def q_func(self) -> Optional[QTextBlockGroup]:
    """
    Calls Qt's 'QTextBlockGroup *QTextBlockGroupPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblockgroupprivate.html#q_func

    Returns
    -------

    Optional[QTextBlockGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextBlockGroup *QTextBlockGroupPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN22QTextBlockGroupPrivate6q_funcEv',
    )
    from . import QTextBlockGroup
    return QTextBlockGroup._cuteAt(address)

  def markBlocksDirty(self) -> None:
    """
    Calls Qt's 'void QTextBlockGroupPrivate::markBlocksDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextblockgroupprivate.html#markBlocksDirty
    """
    #  void QTextBlockGroupPrivate::markBlocksDirty()
    self.uglySide.call(
        'ritual_ZN22QTextBlockGroupPrivate15markBlocksDirtyEv',
    )
