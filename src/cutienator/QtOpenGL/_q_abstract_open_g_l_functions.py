"""
QAbstractOpenGLFunctions binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/qopenglversionfunctions.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QOpenGLContext
  from . import QAbstractOpenGLFunctionsPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpenGLContext = WAIT['QOpenGLContext']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractOpenGLFunctions(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QAbstractOpenGLFunctions: a plain Python object
  standing in front of one C++ QAbstractOpenGLFunctions.

  What exists
  -----------

  Every function of Qt's QAbstractOpenGLFunctions that has a ritual and that
  Python can call so far, 5 names in all: 'initializeOpenGLFunctions',
  'd_func', 'isInitialized', 'setOwningContext', 'owningContext'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAbstractOpenGLFunctions::~QAbstractOpenGLFunctions()': the
    destructor: Python never removes a C++ QAbstractOpenGLFunctions.
  - Qt's 'const QAbstractOpenGLFunctionsPrivate
    *QAbstractOpenGLFunctions::d_func() const': takes in Python what
    'QAbstractOpenGLFunctionsPrivate *QAbstractOpenGLFunctions::d_func()'
    takes.

  What has no ritual
  ------------------

  2 of the 10 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QAbstractOpenGLFunctions is created at the first use, not by
    'QAbstractOpenGLFunctions(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractOpenGLFunctions.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractOpenGLFunctions'

  #  A C++ QAbstractOpenGLFunctions Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractOpenGLFunctions'

  #  The functions Qt calls itself that QAbstractOpenGLFunctions is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'initializeOpenGLFunctions': (
          ('_ZN24QAbstractOpenGLFunctions25initializeOpenGLFunctionsEv',
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

  def isInitialized(self) -> bool:
    """
    Calls Qt's 'bool QAbstractOpenGLFunctions::isInitialized() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractopenglfunctions.html#isInitialized
    """
    #  bool QAbstractOpenGLFunctions::isInitialized() const
    return self.uglySide.call(
        'ritual_ZNK24QAbstractOpenGLFunctions13isInitializedEv',
    )

  def owningContext(self) -> Optional[QOpenGLContext]:
    """
    Calls Qt's 'QOpenGLContext *QAbstractOpenGLFunctions::owningContext()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractopenglfunctions.html#owningContext

    Returns
    -------

    Optional[QOpenGLContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLContext *QAbstractOpenGLFunctions::owningContext() const
    address = self.uglySide.call(
        'ritual_ZNK24QAbstractOpenGLFunctions13owningContextEv',
    )
    from ..QtGui import QOpenGLContext
    return QOpenGLContext._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QOpenGLContext)
  @overload(NoneType)
  def setOwningContext(self, context: Optional[QOpenGLContext]) -> None:
    """
    Calls Qt's 'void QAbstractOpenGLFunctions::setOwningContext(const
    QOpenGLContext *context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractopenglfunctions.html#setOwningContext

    Parameters
    ----------

    context : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractOpenGLFunctions::setOwningContext(const QOpenGLContext
    #      *context)
    self.uglySide.call(
        'ritual_ZN24QAbstractOpenGLFunctions16setOwningContextEPK14QOpenGLC'
        'ontext',
        self._addressOf(context),
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
    Notes what was given, for Qt's
    'QAbstractOpenGLFunctions::QAbstractOpenGLFunctions()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractopenglfunctions.html
    """
    #  QAbstractOpenGLFunctions::QAbstractOpenGLFunctions()
    self._noteCreation(QAbstractOpenGLFunctions, lambda: Rituals.call(
        'ritual_ZN24QAbstractOpenGLFunctionsC1Ev',
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

  def initializeOpenGLFunctions(self) -> bool:
    """
    Calls Qt's 'bool QAbstractOpenGLFunctions::initializeOpenGLFunctions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractopenglfunctions.html
    """
    #  bool QAbstractOpenGLFunctions::initializeOpenGLFunctions()
    ritual = (
        'ritual_ZN24QAbstractOpenGLFunctions25initializeOpenGLFunctionsEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QAbstractOpenGLFunctions25initializeOpenGLFunctio'
          'nsEv')
    return self.uglySide.call(ritual)

  def d_func(self) -> Optional[QAbstractOpenGLFunctionsPrivate]:
    """
    Calls Qt's 'QAbstractOpenGLFunctionsPrivate
    *QAbstractOpenGLFunctions::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractopenglfunctions.html#d_func

    Returns
    -------

    Optional[QAbstractOpenGLFunctionsPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractOpenGLFunctionsPrivate *QAbstractOpenGLFunctions::d_func()
    address = self.uglySide.call(
        'ritual_ZN24QAbstractOpenGLFunctions6d_funcEv',
    )
    from . import QAbstractOpenGLFunctionsPrivate
    return QAbstractOpenGLFunctionsPrivate._cuteAt(address)
