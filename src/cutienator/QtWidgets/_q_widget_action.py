"""
QWidgetAction binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qwidgetaction.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtGui import QAction

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWidgetAction(QAction):
  """
  The cute side of Qt's QWidgetAction: a plain Python object standing in
  front of one C++ QWidgetAction.

  It is built on the cute 'QAction', as Qt's QWidgetAction is built on Qt's
  QAction, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWidgetAction that has a ritual and that Python can
  call so far, 6 names in all: 'metaObject', 'tr', 'setDefaultWidget',
  'defaultWidget', 'requestWidget', 'releaseWidget'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWidgetAction::~QWidgetAction()': the destructor: Python never
    removes a C++ QWidgetAction.

  What has no ritual
  ------------------

  13 of the 21 functions Qt declares: 5 protected; 3 private; 2 takes or
  gives a type that cannot be passed yet; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QWidgetAction is created at the first use, not by
    'QWidgetAction(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWidgetAction.
  - Qt tells when it has removed the C++ QWidgetAction. Every call on the
    cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QWidgetAction::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetaction.html#tr

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
    #  QString QWidgetAction::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QWidgetAction2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWidgetAction'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWidgetAction::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetaction.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWidgetAction::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QWidgetAction10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def defaultWidget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QWidgetAction::defaultWidget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetaction.html#defaultWidget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QWidgetAction::defaultWidget() const
    address = self.uglySide.call(
        'ritual_ZNK13QWidgetAction13defaultWidgetEv',
    )
    from . import QWidget
    return QWidget._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QWidget)
  @overload(NoneType)
  def setDefaultWidget(self, w: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QWidgetAction::setDefaultWidget(QWidget *w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetaction.html#setDefaultWidget

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetAction::setDefaultWidget(QWidget *w)
    self.uglySide.call(
        'ritual_ZN13QWidgetAction16setDefaultWidgetEP7QWidget',
        self._addressOf(w),
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

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's 'QWidgetAction::QWidgetAction(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetaction.html#QWidgetAction

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QWidgetAction::QWidgetAction(QObject *parent)
    self._noteCreation(QWidgetAction, lambda: Rituals.call(
        'ritual_ZN13QWidgetActionC1EP7QObject', self._addressOf(parent),
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

  @overload(QWidget)
  @overload(NoneType)
  def requestWidget(self, parent: Optional[QWidget]) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QWidgetAction::requestWidget(QWidget *parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetaction.html#requestWidget

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QWidgetAction::requestWidget(QWidget *parent)
    address = self.uglySide.call(
        'ritual_ZN13QWidgetAction13requestWidgetEP7QWidget',
        self._addressOf(parent),
    )
    from . import QWidget
    return QWidget._cuteAt(address)

  @overload(QWidget)
  @overload(NoneType)
  def releaseWidget(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QWidgetAction::releaseWidget(QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetaction.html#releaseWidget

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetAction::releaseWidget(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN13QWidgetAction13releaseWidgetEP7QWidget',
        self._addressOf(widget),
    )
