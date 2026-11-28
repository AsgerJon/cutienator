"""
qdesigner_internal::GridPanel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/gridpanel_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means qdesigner_internal::GridPanel to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtWidgets import QWidget
from . import qdesigner_internal

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class GridPanel(QWidget):
  """
  The cute side of Qt's qdesigner_internal::GridPanel: a plain Python object
  standing in front of one C++ qdesigner_internal::GridPanel.

  It is built on the cute 'QWidget', as Qt's qdesigner_internal::GridPanel is
  built on Qt's QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::GridPanel that has a ritual and
  that Python can call so far, 11 names in all: 'metaObject', 'tr',
  'setTitle', 'setGrid', 'grid', 'setCheckable', 'isCheckable', 'isChecked',
  'setChecked', 'setResetButtonVisible', 'reset'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *qdesigner_internal::GridPanel::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int qdesigner_internal::GridPanel::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'qdesigner_internal::GridPanel::~GridPanel()': the destructor:
    Python never removes a C++ qdesigner_internal::GridPanel.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ qdesigner_internal::GridPanel is created at the first use, not by
    'qdesigner_internal::GridPanel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::GridPanel.
  - Qt tells when it has removed the C++ qdesigner_internal::GridPanel. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString qdesigner_internal::GridPanel::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-gridpanel.html#tr

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
    #  QString qdesigner_internal::GridPanel::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal9GridPanel2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::GridPanel'

  #  A C++ qdesigner_internal::GridPanel Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_qdesigner_internal_GridPanel'

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
    *qdesigner_internal::GridPanel::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-gridpanel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *qdesigner_internal::GridPanel::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal9GridPanel10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def grid(self) -> qdesigner_internal.Grid:
    """
    Calls Qt's 'Grid qdesigner_internal::GridPanel::grid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-gridpanel.html#grid

    Returns
    -------

    qdesigner_internal.Grid
      A new cute qdesigner_internal::Grid around the copy Qt gave back.
      Python owns it.
    """
    #  Grid qdesigner_internal::GridPanel::grid() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal9GridPanel4gridEv',
    )
    return qdesigner_internal.Grid._cuteOwning(address)

  def isCheckable(self) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::GridPanel::isCheckable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-gridpanel.html#isCheckable
    """
    #  bool qdesigner_internal::GridPanel::isCheckable() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal9GridPanel11isCheckableEv',
    )

  def isChecked(self) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::GridPanel::isChecked() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-gridpanel.html#isChecked
    """
    #  bool qdesigner_internal::GridPanel::isChecked() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal9GridPanel9isCheckedEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setTitle(self, title: str) -> None:
    """
    Calls Qt's 'void qdesigner_internal::GridPanel::setTitle(const QString
    &title)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-gridpanel.html#setTitle

    Parameters
    ----------

    title : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::GridPanel::setTitle(const QString &title)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal9GridPanel8setTitleERK7QString', title,
    )

  @overload(WAIT['qdesigner_internal.Grid'])
  def setGrid(self, g: qdesigner_internal.Grid) -> None:
    """
    Calls Qt's 'void qdesigner_internal::GridPanel::setGrid(const Grid &g)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-gridpanel.html#setGrid

    Parameters
    ----------

    g : qdesigner_internal.Grid
      Passed on as a value: Qt reads the C++ qdesigner_internal::Grid, which
      stays Python's own.
    """
    #  void qdesigner_internal::GridPanel::setGrid(const Grid &g)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal9GridPanel7setGridERKNS_4GridE',
        self._valueOf(g),
    )

  @overload(bool)
  def setCheckable(self, c: bool) -> None:
    """
    Calls Qt's 'void qdesigner_internal::GridPanel::setCheckable(bool c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-gridpanel.html#setCheckable

    Parameters
    ----------

    c : bool
      Passed on as it is.
    """
    #  void qdesigner_internal::GridPanel::setCheckable(bool c)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal9GridPanel12setCheckableEb', c,
    )

  @overload(bool)
  def setChecked(self, c: bool) -> None:
    """
    Calls Qt's 'void qdesigner_internal::GridPanel::setChecked(bool c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-gridpanel.html#setChecked

    Parameters
    ----------

    c : bool
      Passed on as it is.
    """
    #  void qdesigner_internal::GridPanel::setChecked(bool c)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal9GridPanel10setCheckedEb', c,
    )

  @overload(bool)
  def setResetButtonVisible(self, v: bool) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::GridPanel::setResetButtonVisible(bool v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-gridpanel.html

    Parameters
    ----------

    v : bool
      Passed on as it is.
    """
    #  void qdesigner_internal::GridPanel::setResetButtonVisible(bool v)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal9GridPanel21setResetButtonVisibleEb',
        v,
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
  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::GridPanel::GridPanel(QWidget *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-gridpanel.html#GridPanel

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  qdesigner_internal::GridPanel::GridPanel(QWidget *parent)
    self._noteCreation(GridPanel, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal9GridPanelC1EP7QWidget',
        self._addressOf(parent),
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

  def reset(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::GridPanel::reset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-gridpanel.html#reset
    """
    #  void qdesigner_internal::GridPanel::reset()
    self.uglySide.call('ritual_ZN18qdesigner_internal9GridPanel5resetEv')
