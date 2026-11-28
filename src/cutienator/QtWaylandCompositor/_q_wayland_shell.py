"""
QWaylandShell binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/qwaylandshell.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum
from ..occult import Rituals
from . import QWaylandCompositorExtension, QWaylandObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QWaylandShellPrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWaylandShell(QWaylandCompositorExtension):
  """
  The cute side of Qt's QWaylandShell: a plain Python object standing in
  front of one C++ QWaylandShell.

  It is built on the cute 'QWaylandCompositorExtension', as Qt's
  QWaylandShell is built on Qt's QWaylandCompositorExtension, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QWaylandShell that has a ritual and that Python can
  call so far, 6 names in all: 'metaObject', 'tr', 'd_func', 'focusPolicy',
  'setFocusPolicy', 'focusPolicyChanged'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWaylandShell::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QWaylandShell::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QWaylandShellPrivate *QWaylandShell::d_func() const': takes
    in Python what 'QWaylandShellPrivate *QWaylandShell::d_func()' takes.
  - Qt's 'void QWaylandShell::qt_qmlMarker_uncreatable()': one of Qt's own
    inner workings.
  - Qt's 'QWaylandShell::QWaylandShell(QWaylandShellPrivate &dd)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QWaylandShell::QWaylandShell(QWaylandObject *container,
    QWaylandShellPrivate &dd)': takes a type Python has no way to hand over
    yet.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWaylandShell is created at the first use, not by
    'QWaylandShell(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandShell.
  - Qt tells when it has removed the C++ QWaylandShell. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QWaylandShell, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class FocusPolicy(CuteNum):
    """
    The enum 'QWaylandShell::FocusPolicy' of Qt, with the 2 names Qt gives in
    it.
    """

    AutomaticFocus = Kee[int](0)
    ManualFocus = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QWaylandShell::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandshell.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWaylandShell::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QWaylandShell2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandShell'

  #  A C++ QWaylandShell Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWaylandShell'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWaylandShell::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandshell.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWaylandShell::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QWaylandShell10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def focusPolicy(self) -> FocusPolicy:
    """
    Calls Qt's 'FocusPolicy QWaylandShell::focusPolicy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandshell.html#focusPolicy

    Returns
    -------

    FocusPolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'FocusPolicy(number)'
      gives.
    """
    #  FocusPolicy QWaylandShell::focusPolicy() const
    return QWaylandShell.FocusPolicy(self.uglySide.call(
        'ritual_ZNK13QWaylandShell11focusPolicyEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(FocusPolicy)
  def setFocusPolicy(self, focusPolicy: FocusPolicy) -> None:
    """
    Calls Qt's 'void QWaylandShell::setFocusPolicy(FocusPolicy focusPolicy)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandshell.html#setFocusPolicy

    Parameters
    ----------

    focusPolicy : FocusPolicy
      Passed on as its number.
    """
    #  void QWaylandShell::setFocusPolicy(FocusPolicy focusPolicy)
    self.uglySide.call(
        'ritual_ZN13QWaylandShell14setFocusPolicyENS_11FocusPolicyE',
        focusPolicy.value,
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
    Notes what was given, for Qt's 'QWaylandShell::QWaylandShell()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandshell.html#QWaylandShell
    """
    #  QWaylandShell::QWaylandShell()
    self._noteCreation(QWaylandShell, lambda: Rituals.call(
        'ritual_ZN13QWaylandShellC1Ev',
    ))

  @overload(QWaylandObject)
  @overload(NoneType)
  def __init__(self, waylandObject: Optional[QWaylandObject]) -> None:
    """
    Notes what was given, for Qt's
    'QWaylandShell::QWaylandShell(QWaylandObject *waylandObject)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandshell.html#QWaylandShell

    Parameters
    ----------

    waylandObject : Optional[QWaylandObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QWaylandShell::QWaylandShell(QWaylandObject *waylandObject)
    self._noteCreation(QWaylandShell, lambda: Rituals.call(
        'ritual_ZN13QWaylandShellC1EP14QWaylandObject',
        self._addressOf(waylandObject),
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

  def d_func(self) -> Optional[QWaylandShellPrivate]:
    """
    Calls Qt's 'QWaylandShellPrivate *QWaylandShell::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandshell.html#d_func

    Returns
    -------

    Optional[QWaylandShellPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandShellPrivate *QWaylandShell::d_func()
    address = self.uglySide.call('ritual_ZN13QWaylandShell6d_funcEv')
    from . import QWaylandShellPrivate
    return QWaylandShellPrivate._cuteAt(address)

  def focusPolicyChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandShell::focusPolicyChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandshell.html#focusPolicyChanged
    """
    #  void QWaylandShell::focusPolicyChanged()
    self.uglySide.call('ritual_ZN13QWaylandShell18focusPolicyChangedEv')
