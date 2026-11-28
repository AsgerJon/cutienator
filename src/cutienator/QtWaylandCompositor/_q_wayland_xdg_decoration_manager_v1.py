"""
QWaylandXdgDecorationManagerV1 binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/qwaylandxdgdecorationv1.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from . import QWaylandXdgToplevel

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWaylandXdgDecorationManagerV1(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWaylandXdgDecorationManagerV1: a plain Python object
  standing in front of one C++ QWaylandXdgDecorationManagerV1.

  What exists
  -----------

  Every function of Qt's QWaylandXdgDecorationManagerV1 that has a ritual and
  that Python can call so far, 6 names in all: 'metaObject', 'tr',
  'initialize', 'preferredMode', 'setPreferredMode', 'preferredModeChanged'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWaylandXdgDecorationManagerV1::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QWaylandXdgDecorationManagerV1::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QWaylandXdgDecorationManagerV1Private
    *QWaylandXdgDecorationManagerV1::d_func()': gives
    'QWaylandXdgDecorationManagerV1Private', which has no cute class yet.
  - Qt's 'const QWaylandXdgDecorationManagerV1Private
    *QWaylandXdgDecorationManagerV1::d_func() const': gives
    'QWaylandXdgDecorationManagerV1Private', which has no cute class yet.
  - Qt's 'const struct wl_interface
    *QWaylandXdgDecorationManagerV1::interface()': gives 'struct
    wl_interface', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWaylandXdgDecorationManagerV1 is created at the first use, not
    by 'QWaylandXdgDecorationManagerV1(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandXdgDecorationManagerV1.
  - Each name of Qt's QWaylandXdgDecorationManagerV1 that has no cute
    function yet, 'd_func', 'interface', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

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
    Calls Qt's 'QString QWaylandXdgDecorationManagerV1::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgdecorationmanagerv1.html#tr

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
    #  QString QWaylandXdgDecorationManagerV1::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN30QWaylandXdgDecorationManagerV12trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandXdgDecorationManagerV1'

  #  A C++ QWaylandXdgDecorationManagerV1 Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWaylandXdgDecorationManagerV1'

  #  The functions Qt calls itself that QWaylandXdgDecorationManagerV1 is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'initialize': (
          ('_ZN30QWaylandXdgDecorationManagerV110initializeEv',
           ('nothing', 'nothing', ''),
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QWaylandXdgDecorationManagerV1::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgdecorationmanagerv1.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWaylandXdgDecorationManagerV1::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK30QWaylandXdgDecorationManagerV110metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def preferredMode(self) -> QWaylandXdgToplevel.DecorationMode:
    """
    Calls Qt's 'QWaylandXdgToplevel::DecorationMode
    QWaylandXdgDecorationManagerV1::preferredMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgdecorationmanagerv1.html#preferredMode

    Returns
    -------

    QWaylandXdgToplevel.DecorationMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QWaylandXdgToplevel.DecorationMode(number)' gives.
    """
    #  QWaylandXdgToplevel::DecorationMode
    #      QWaylandXdgDecorationManagerV1::preferredMode() const
    return QWaylandXdgToplevel.DecorationMode(self.uglySide.call(
        'ritual_ZNK30QWaylandXdgDecorationManagerV113preferredModeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QWaylandXdgToplevel.DecorationMode)
  def setPreferredMode(
      self,
      preferredMode: QWaylandXdgToplevel.DecorationMode,
  ) -> None:
    """
    Calls Qt's 'void
    QWaylandXdgDecorationManagerV1::setPreferredMode(QWaylandXdgToplevel::
    DecorationMode preferredMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgdecorationmanagerv1.html

    Parameters
    ----------

    preferredMode : QWaylandXdgToplevel.DecorationMode
      Passed on as its number.
    """
    #  void QWaylandXdgDecorationManagerV1::setPreferredMode(
    #      QWaylandXdgToplevel::DecorationMode preferredMode)
    self.uglySide.call(
        'ritual_ZN30QWaylandXdgDecorationManagerV116setPreferredModeEN19QWa'
        'ylandXdgToplevel14DecorationModeE',
        preferredMode.value,
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
    'QWaylandXdgDecorationManagerV1::QWaylandXdgDecorationManagerV1()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgdecorationmanagerv1.html
    """
    #  QWaylandXdgDecorationManagerV1::QWaylandXdgDecorationManagerV1()
    self._noteCreation(QWaylandXdgDecorationManagerV1, lambda: Rituals.call(
        'ritual_ZN30QWaylandXdgDecorationManagerV1C1Ev',
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

  def initialize(self) -> None:
    """
    Calls Qt's 'void QWaylandXdgDecorationManagerV1::initialize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgdecorationmanagerv1.html#initialize
    """
    #  void QWaylandXdgDecorationManagerV1::initialize()
    ritual = 'ritual_ZN30QWaylandXdgDecorationManagerV110initializeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN30QWaylandXdgDecorationManagerV110initializeEv'
    self.uglySide.call(ritual)

  def preferredModeChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandXdgDecorationManagerV1::preferredModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgdecorationmanagerv1.html
    """
    #  void QWaylandXdgDecorationManagerV1::preferredModeChanged()
    self.uglySide.call(
        'ritual_ZN30QWaylandXdgDecorationManagerV120preferredModeChangedEv',
    )

  @staticmethod
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'QWaylandXdgDecorationManagerV1Private
      *QWaylandXdgDecorationManagerV1::d_func()': gives
      'QWaylandXdgDecorationManagerV1Private', which has no cute class yet.
    - Qt's 'const QWaylandXdgDecorationManagerV1Private
      *QWaylandXdgDecorationManagerV1::d_func() const': gives
      'QWaylandXdgDecorationManagerV1Private', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandXdgDecorationManagerV1.d_func' has no cute function yet. "
        "Qt's 'QWaylandXdgDecorationManagerV1Private "
        "*QWaylandXdgDecorationManagerV1::d_func()': gives "
        "'QWaylandXdgDecorationManagerV1Private', which has no cute class "
        "yet. Qt's 'const QWaylandXdgDecorationManagerV1Private "
        "*QWaylandXdgDecorationManagerV1::d_func() const': gives "
        "'QWaylandXdgDecorationManagerV1Private', which has no cute class "
        "yet.")

  @staticmethod
  def interface(*__, **_) -> Never:
    """
    Qt's 'const struct wl_interface
    *QWaylandXdgDecorationManagerV1::interface()': gives 'struct
    wl_interface', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandXdgDecorationManagerV1.interface' has no cute function "
        "yet. Qt's 'const struct wl_interface "
        "*QWaylandXdgDecorationManagerV1::interface()': gives 'struct "
        "wl_interface', which has no cute class yet.")
