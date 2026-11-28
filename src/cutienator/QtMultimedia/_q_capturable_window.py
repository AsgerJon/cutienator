"""
QCapturableWindow binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/qcapturablewindow.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QDebug
  from ..QtGui import QWindow
  from . import QCapturableWindowPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCapturableWindowPrivate = WAIT['QCapturableWindowPrivate']
  QDebug = WAIT['QDebug']
  QWindow = WAIT['QWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCapturableWindow(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCapturableWindow: a plain Python object standing in
  front of one C++ QCapturableWindow.

  C++ hands a QCapturableWindow around as a copy, so every C++
  QCapturableWindow behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCapturableWindow that has a ritual and that Python
  can call so far, 5 names in all: '__eq__', '__ne__', 'isValid',
  'description', '__rlshift__'. It can be made from Python, in 4 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCapturableWindow::~QCapturableWindow()': the destructor: Python
    removes its C++ QCapturableWindow by it, and has no other use for it.
  - Qt's 'QCapturableWindow::QCapturableWindow(QCapturableWindow &&other)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QCapturableWindow &QCapturableWindow::operator=(const
    QCapturableWindow &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QCapturableWindow &QCapturableWindow::operator=(QCapturableWindow
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'void QCapturableWindow::swap(QCapturableWindow &other)': takes a
    type Python has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 17 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QCapturableWindow is created at the first use, not by
    'QCapturableWindow(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCapturableWindow back gives a copy the ritual made
    for Python, in a new cute QCapturableWindow.
  - Each name of Qt's QCapturableWindow that has no cute function yet,
    'swap', holds a function that raises 'NotImplementedError', and its
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
  __qt_class__ = 'QCapturableWindow'

  #  Qt's '~QCapturableWindow()'. Naming it makes this a value class: Python
  #  owns every C++ QCapturableWindow behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QCapturableWindowD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QCapturableWindow::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcapturablewindow.html#isValid
    """
    #  bool QCapturableWindow::isValid() const
    return self.uglySide.call('ritual_ZNK17QCapturableWindow7isValidEv')

  def description(self) -> str:
    """
    Calls Qt's 'QString QCapturableWindow::description() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcapturablewindow.html#description

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCapturableWindow::description() const
    return self.uglySide.call('ritual_ZNK17QCapturableWindow11descriptionEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QCapturableWindow) -> bool:
    """
    Calls Qt's 'bool operator==(const QCapturableWindow &lhs, const
    QCapturableWindow &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcapturablewindow.html#operator==

    Parameters
    ----------

    rhs : QCapturableWindow
      Passed on as a value: Qt reads the C++ QCapturableWindow, which stays
      Python's own.
    """
    #  bool operator==(const QCapturableWindow &lhs, const QCapturableWindow
    #      &rhs)
    return Rituals.call(
        'ritual_ZeqRK17QCapturableWindowS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: QCapturableWindow) -> bool:
    """
    Calls Qt's 'bool operator!=(const QCapturableWindow &lhs, const
    QCapturableWindow &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcapturablewindow.html#operator!=

    Parameters
    ----------

    rhs : QCapturableWindow
      Passed on as a value: Qt reads the C++ QCapturableWindow, which stays
      Python's own.
    """
    #  bool operator!=(const QCapturableWindow &lhs, const QCapturableWindow
    #      &rhs)
    return Rituals.call(
        'ritual_ZneRK17QCapturableWindowS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(QDebug)
  def __rlshift__(self, a0: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug a0, const QCapturableWindow &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qcapturablewindow.html#operator<<

    Parameters
    ----------

    a0 : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug a0, const QCapturableWindow &a1)
    address = Rituals.call(
        'ritual_Zls6QDebugRK17QCapturableWindow',
        CuteMixin._valueOf(a0), CuteMixin._valueOf(self),
    )
    from ..QtCore import QDebug
    return QDebug._cuteOwning(address)

  @overload.fallback
  def __rlshift__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QCapturableWindow::QCapturableWindow()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcapturablewindow.html#QCapturableWindow
    """
    #  QCapturableWindow::QCapturableWindow()
    self._noteCreation(QCapturableWindow, lambda: Rituals.call(
        'ritual_ZN17QCapturableWindowC1Ev',
    ))

  @overload(QWindow)
  @overload(NoneType)
  def __init__(self, window: Optional[QWindow]) -> None:
    """
    Notes what was given, for Qt's
    'QCapturableWindow::QCapturableWindow(QWindow *window)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcapturablewindow.html#QCapturableWindow

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QCapturableWindow::QCapturableWindow(QWindow *window)
    self._noteCreation(QCapturableWindow, lambda: Rituals.call(
        'ritual_ZN17QCapturableWindowC1EP7QWindow', self._addressOf(window),
    ))

  @overload(THIS)
  def __init__(self, other: QCapturableWindow) -> None:
    """
    Notes what was given, for Qt's
    'QCapturableWindow::QCapturableWindow(const QCapturableWindow &other)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcapturablewindow.html#QCapturableWindow

    Parameters
    ----------

    other : QCapturableWindow
      Passed on as a value: Qt reads the C++ QCapturableWindow, which stays
      Python's own.
    """
    #  QCapturableWindow::QCapturableWindow(const QCapturableWindow &other)
    self._noteCreation(QCapturableWindow, lambda: Rituals.call(
        'ritual_ZN17QCapturableWindowC1ERKS_', self._valueOf(other),
    ))

  @overload(QCapturableWindowPrivate)
  def __init__(
      self,
      capturablePrivate: Optional[QCapturableWindowPrivate],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QCapturableWindow::QCapturableWindow(QCapturableWindowPrivate
    *capturablePrivate)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcapturablewindow.html#QCapturableWindow

    Parameters
    ----------

    capturablePrivate : Optional[QCapturableWindowPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QCapturableWindow::QCapturableWindow(QCapturableWindowPrivate
    #      *capturablePrivate)
    self._noteCreation(QCapturableWindow, lambda: Rituals.call(
        'ritual_ZN17QCapturableWindowC1EP24QCapturableWindowPrivate',
        self._addressOf(capturablePrivate),
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
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QCapturableWindow::swap(QCapturableWindow &other)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCapturableWindow.swap' has no cute function yet. Qt's 'void "
        "QCapturableWindow::swap(QCapturableWindow &other)': takes a type "
        "Python has no way to hand over yet.")


#  Qt's 'QList<QCapturableWindow>': the list of QCapturableWindow, which
#  'QList[QCapturableWindow]' gives. It is made here, so that there is one as
#  soon as there can be a QCapturableWindow.
QList.createKind(
    QCapturableWindow, 'value',
    make='ritual_list_make_QCapturableWindow',
    add='ritual_list_add_QCapturableWindow',
    size='ritual_list_size_QCapturableWindow',
    at='ritual_list_at_QCapturableWindow',
    drop='ritual_list_drop_QCapturableWindow',
)
