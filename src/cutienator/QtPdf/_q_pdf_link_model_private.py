"""
QPdfLinkModelPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPdf/6.12.0/QtPdf/private/qpdflinkmodel_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QPdfLinkModelPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QPdfLinkModel
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPdfLinkModel = WAIT['QPdfLinkModel']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPdfLinkModelPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPdfLinkModelPrivate: a plain Python object standing
  in front of one C++ QPdfLinkModelPrivate.

  C++ hands a QPdfLinkModelPrivate around as a copy, so every C++
  QPdfLinkModelPrivate behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPdfLinkModelPrivate that has a ritual and that
  Python can call so far, 1 name in all: 'q_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QPdfLinkModel *QPdfLinkModelPrivate::q_func() const': takes
    in Python what 'QPdfLinkModel *QPdfLinkModelPrivate::q_func()' takes.
  - Qt's 'QPdfLinkModelPrivate::~QPdfLinkModelPrivate()': the destructor:
    Python removes its C++ QPdfLinkModelPrivate by it, and has no other use
    for it.

  What has no ritual
  ------------------

  1 of the 5 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QPdfLinkModelPrivate is created at the first use, not by
    'QPdfLinkModelPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPdfLinkModelPrivate back gives a copy the ritual
    made for Python, in a new cute QPdfLinkModelPrivate.
  - Each name of Qt's QPdfLinkModelPrivate that has no cute function yet,
    'update', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPdfLinkModelPrivate'

  #  Qt's '~QPdfLinkModelPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QPdfLinkModelPrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QPdfLinkModelPrivateD1Ev'

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

  @overload(QPdfLinkModel)
  @overload(NoneType)
  def __init__(self, qq: Optional[QPdfLinkModel]) -> None:
    """
    Notes what was given, for Qt's
    'QPdfLinkModelPrivate::QPdfLinkModelPrivate(QPdfLinkModel *qq)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdflinkmodelprivate.html#QPdfLinkModelPrivate

    Parameters
    ----------

    qq : Optional[QPdfLinkModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QPdfLinkModelPrivate::QPdfLinkModelPrivate(QPdfLinkModel *qq)
    self._noteCreation(QPdfLinkModelPrivate, lambda: Rituals.call(
        'ritual_ZN20QPdfLinkModelPrivateC1EP13QPdfLinkModel',
        self._addressOf(qq),
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

  def q_func(self) -> Optional[QPdfLinkModel]:
    """
    Calls Qt's 'QPdfLinkModel *QPdfLinkModelPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qpdflinkmodelprivate.html#q_func

    Returns
    -------

    Optional[QPdfLinkModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPdfLinkModel *QPdfLinkModelPrivate::q_func()
    address = self.uglySide.call('ritual_ZN20QPdfLinkModelPrivate6q_funcEv')
    from . import QPdfLinkModel
    return QPdfLinkModel._cuteAt(address)

  @staticmethod
  def update(*__, **_) -> Never:
    """
    Qt's 'void QPdfLinkModelPrivate::update()': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'QPdfDocumentPrivate'.
    """
    raise NotImplementedError(
        "'QPdfLinkModelPrivate.update' has no cute function yet. Qt's 'void "
        "QPdfLinkModelPrivate::update()': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "member access into incomplete type 'QPdfDocumentPrivate'.")
