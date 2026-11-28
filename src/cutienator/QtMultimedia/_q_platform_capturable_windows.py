"""
QPlatformCapturableWindows binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qplatformcapturablewindows_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QPlatformCapturableWindows to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QCapturableWindow, QCapturableWindowPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCapturableWindowPrivate = WAIT['QCapturableWindowPrivate']


class QPlatformCapturableWindows(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPlatformCapturableWindows: a plain Python object
  standing in front of one C++ QPlatformCapturableWindows.

  What exists
  -----------

  Every function of Qt's QPlatformCapturableWindows that has a ritual and
  that Python can call so far, 2 names in all: 'windows', 'isWindowValid'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlatformCapturableWindows::~QPlatformCapturableWindows()': the
    destructor: Python never removes a C++ QPlatformCapturableWindows.
  - Qt's 'q23::expected<QCapturableWindow, QString>
    QPlatformCapturableWindows::fromQWindow(QWindow *a0) const': gives a type
    Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 7 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QPlatformCapturableWindows is created at the first use, not by
    'QPlatformCapturableWindows(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformCapturableWindows.
  - Each name of Qt's QPlatformCapturableWindows that has no cute function
    yet, 'fromQWindow', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformCapturableWindows'

  #  A C++ QPlatformCapturableWindows Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlatformCapturableWindows'

  #  The functions Qt calls itself that QPlatformCapturableWindows is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'windows': (
          'QList<QCapturableWindow> QPlatformCapturableWindows::windows() '
          'const',
      ),
      'fromQWindow': (
          'q23::expected<QCapturableWindow, QString> '
          'QPlatformCapturableWindows::fromQWindow(QWindow *) const',
      ),
  }

  #  The functions Qt calls itself that QPlatformCapturableWindows is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'isWindowValid': (
          ('_ZNK26QPlatformCapturableWindows13isWindowValidERK24QCapturable'
           'WindowPrivate',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtMultimedia:QCapturableWindowPrivate'),
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

  def windows(self) -> QList[QCapturableWindow]:
    """
    Calls Qt's 'QList<QCapturableWindow>
    QPlatformCapturableWindows::windows() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformcapturablewindows.html#windows

    Returns
    -------

    QList[QCapturableWindow]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QCapturableWindow> QPlatformCapturableWindows::windows() const
    address = self.uglySide.call(
        'ritual_ZNK26QPlatformCapturableWindows7windowsEv',
    )
    from . import QCapturableWindow
    return QList[QCapturableWindow]._cuteOwning(address)

  @overload(QCapturableWindowPrivate)
  def isWindowValid(self, a0: QCapturableWindowPrivate) -> bool:
    """
    Calls Qt's 'bool QPlatformCapturableWindows::isWindowValid(const
    QCapturableWindowPrivate &a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformcapturablewindows.html#isWindowValid

    Parameters
    ----------

    a0 : QCapturableWindowPrivate
      Passed on as a value: Qt reads the C++ QCapturableWindowPrivate, which
      stays Python's own.
    """
    #  bool QPlatformCapturableWindows::isWindowValid(const
    #      QCapturableWindowPrivate &a0) const
    ritual = (
        'ritual_ZNK26QPlatformCapturableWindows13isWindowValidERK24QCaptura'
        'bleWindowPrivate')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK26QPlatformCapturableWindows13isWindowValidERK24QC'
          'apturableWindowPrivate')
    return self.uglySide.call(ritual, self._valueOf(a0))

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
    Notes what was given, for Qt's
    'QPlatformCapturableWindows::QPlatformCapturableWindows()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformcapturablewindows.html
    """
    #  QPlatformCapturableWindows::QPlatformCapturableWindows()
    self._noteCreation(QPlatformCapturableWindows, lambda: Rituals.call(
        'ritual_ZN26QPlatformCapturableWindowsC1Ev',
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

  @staticmethod
  def fromQWindow(*__, **_) -> Never:
    """
    Qt's 'q23::expected<QCapturableWindow, QString>
    QPlatformCapturableWindows::fromQWindow(QWindow *a0) const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QPlatformCapturableWindows.fromQWindow' has no cute function yet. "
        "Qt's 'q23::expected<QCapturableWindow, QString> "
        "QPlatformCapturableWindows::fromQWindow(QWindow *a0) const': gives "
        "a type Python has no way to take yet.")
