"""
QShortcutPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qshortcut_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QShortcutPrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject
  from . import QShortcut
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QShortcutPrivate(QObjectPrivate):
  """
  The cute side of Qt's QShortcutPrivate: a plain Python object standing in
  front of one C++ QShortcutPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QShortcutPrivate is built
  on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QShortcutPrivate that has a ritual and that Python
  can call so far, 3 names in all: 'q_func', 'handleWhatsThis',
  'simpleContextMatcher'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QShortcut *QShortcutPrivate::q_func() const': takes in Python
    what 'QShortcut *QShortcutPrivate::q_func()' takes.
  - Qt's 'QShortcutMap::ContextMatcher QShortcutPrivate::contextMatcher()
    const': gives a type Python has no way to take yet.
  - Qt's 'void QShortcutPrivate::redoGrab(QShortcutMap &map)': takes a type
    Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QShortcutPrivate is created at the first use, not by
    'QShortcutPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QShortcutPrivate.
  - Each name of Qt's QShortcutPrivate that has no cute function yet,
    'contextMatcher', 'redoGrab', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QObject, Qt.ShortcutContext)
  @overload(NoneType, Qt.ShortcutContext)
  def simpleContextMatcher(
      object: Optional[QObject],
      context: Qt.ShortcutContext,
  ) -> bool:
    """
    Calls Qt's 'bool QShortcutPrivate::simpleContextMatcher(QObject *object,
    Qt::ShortcutContext context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qshortcutprivate.html#simpleContextMatcher

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    context : Qt.ShortcutContext
      Passed on as its number.
    """
    #  bool QShortcutPrivate::simpleContextMatcher(QObject *object,
    #      Qt::ShortcutContext context)
    return Rituals.call(
        'ritual_ZN16QShortcutPrivate20simpleContextMatcherEP7QObjectN2Qt15S'
        'hortcutContextE',
        CuteMixin._addressOf(object, 'QObject'), context.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QShortcutPrivate'

  #  A C++ QShortcutPrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QShortcutPrivate'

  #  The functions Qt calls itself that QShortcutPrivate is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'contextMatcher': (
          'QShortcutMap::ContextMatcher QShortcutPrivate::contextMatcher() '
          'const',
      ),
  }

  #  The functions Qt calls itself that QShortcutPrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'handleWhatsThis': (
          ('_ZN16QShortcutPrivate15handleWhatsThisEv',
           ('bool', 'number', ''),
           ()),
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QShortcutPrivate::QShortcutPrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qshortcutprivate.html#QShortcutPrivate
    """
    #  QShortcutPrivate::QShortcutPrivate()
    self._noteCreation(QShortcutPrivate, lambda: Rituals.call(
        'ritual_ZN16QShortcutPrivateC1Ev',
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

  def q_func(self) -> Optional[QShortcut]:
    """
    Calls Qt's 'QShortcut *QShortcutPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qshortcutprivate.html#q_func

    Returns
    -------

    Optional[QShortcut]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QShortcut *QShortcutPrivate::q_func()
    address = self.uglySide.call('ritual_ZN16QShortcutPrivate6q_funcEv')
    from . import QShortcut
    return QShortcut._cuteAt(address)

  def handleWhatsThis(self) -> bool:
    """
    Calls Qt's 'bool QShortcutPrivate::handleWhatsThis()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qshortcutprivate.html#handleWhatsThis
    """
    #  bool QShortcutPrivate::handleWhatsThis()
    ritual = 'ritual_ZN16QShortcutPrivate15handleWhatsThisEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QShortcutPrivate15handleWhatsThisEv'
    return self.uglySide.call(ritual)

  @staticmethod
  def contextMatcher(*__, **_) -> Never:
    """
    Qt's 'QShortcutMap::ContextMatcher QShortcutPrivate::contextMatcher()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QShortcutPrivate.contextMatcher' has no cute function yet. Qt's "
        "'QShortcutMap::ContextMatcher QShortcutPrivate::contextMatcher() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def redoGrab(*__, **_) -> Never:
    """
    Qt's 'void QShortcutPrivate::redoGrab(QShortcutMap &map)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QShortcutPrivate.redoGrab' has no cute function yet. Qt's 'void "
        "QShortcutPrivate::redoGrab(QShortcutMap &map)': takes a type "
        "Python has no way to hand over yet.")
