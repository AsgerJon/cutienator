"""
QWaylandViewporter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/qwaylandviewporter.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QWaylandCompositor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWaylandCompositor = WAIT['QWaylandCompositor']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWaylandViewporter(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWaylandViewporter: a plain Python object standing in
  front of one C++ QWaylandViewporter.

  What exists
  -----------

  Every function of Qt's QWaylandViewporter that has a ritual and that Python
  can call so far, 3 names in all: 'metaObject', 'tr', 'initialize'. It can
  be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWaylandViewporter::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QWaylandViewporter::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QWaylandViewporterPrivate *QWaylandViewporter::d_func()': gives
    'QWaylandViewporterPrivate', which has no cute class yet.
  - Qt's 'const QWaylandViewporterPrivate *QWaylandViewporter::d_func()
    const': gives 'QWaylandViewporterPrivate', which has no cute class yet.
  - Qt's 'const struct wl_interface *QWaylandViewporter::interface()': gives
    'struct wl_interface', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 12 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWaylandViewporter is created at the first use, not by
    'QWaylandViewporter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandViewporter.
  - Each name of Qt's QWaylandViewporter that has no cute function yet,
    'd_func', 'interface', holds a function that raises
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
    Calls Qt's 'QString QWaylandViewporter::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandviewporter.html#tr

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
    #  QString QWaylandViewporter::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QWaylandViewporter2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandViewporter'

  #  A C++ QWaylandViewporter Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWaylandViewporter'

  #  The functions Qt calls itself that QWaylandViewporter is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'initialize': (
          ('_ZN18QWaylandViewporter10initializeEv',
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
    Calls Qt's 'const QMetaObject *QWaylandViewporter::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandviewporter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWaylandViewporter::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QWaylandViewporter10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
    'QWaylandViewporter::QWaylandViewporter()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandviewporter.html#QWaylandViewporter
    """
    #  QWaylandViewporter::QWaylandViewporter()
    self._noteCreation(QWaylandViewporter, lambda: Rituals.call(
        'ritual_ZN18QWaylandViewporterC1Ev',
    ))

  @overload(QWaylandCompositor)
  @overload(NoneType)
  def __init__(self, compositor: Optional[QWaylandCompositor]) -> None:
    """
    Notes what was given, for Qt's
    'QWaylandViewporter::QWaylandViewporter(QWaylandCompositor *compositor)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandviewporter.html#QWaylandViewporter

    Parameters
    ----------

    compositor : Optional[QWaylandCompositor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QWaylandViewporter::QWaylandViewporter(QWaylandCompositor *compositor)
    self._noteCreation(QWaylandViewporter, lambda: Rituals.call(
        'ritual_ZN18QWaylandViewporterC1EP18QWaylandCompositor',
        self._addressOf(compositor),
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
    Calls Qt's 'void QWaylandViewporter::initialize()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandviewporter.html#initialize
    """
    #  void QWaylandViewporter::initialize()
    ritual = 'ritual_ZN18QWaylandViewporter10initializeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QWaylandViewporter10initializeEv'
    self.uglySide.call(ritual)

  @staticmethod
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'QWaylandViewporterPrivate *QWaylandViewporter::d_func()': gives
      'QWaylandViewporterPrivate', which has no cute class yet.
    - Qt's 'const QWaylandViewporterPrivate *QWaylandViewporter::d_func()
      const': gives 'QWaylandViewporterPrivate', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandViewporter.d_func' has no cute function yet. Qt's "
        "'QWaylandViewporterPrivate *QWaylandViewporter::d_func()': gives "
        "'QWaylandViewporterPrivate', which has no cute class yet. Qt's "
        "'const QWaylandViewporterPrivate *QWaylandViewporter::d_func() "
        "const': gives 'QWaylandViewporterPrivate', which has no cute class "
        "yet.")

  @staticmethod
  def interface(*__, **_) -> Never:
    """
    Qt's 'const struct wl_interface *QWaylandViewporter::interface()': gives
    'struct wl_interface', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandViewporter.interface' has no cute function yet. Qt's "
        "'const struct wl_interface *QWaylandViewporter::interface()': "
        "gives 'struct wl_interface', which has no cute class yet.")
