"""
QQuickFluentWinUI3FocusFrame binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickControls2FluentWinUI3StyleImpl/6.12.0/QtQuickControls2FluentWinUI3StyleImpl/private/qquickfluentwinui3focusframe_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickFluentWinUI3FocusFrame to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtQml import QQmlContext
  from ..QtQuick import QQuickItem
  from ..QtQuickTemplates2 import QQuickControl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlContext = WAIT['QQmlContext']
  QQuickControl = WAIT['QQuickControl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickFluentWinUI3FocusFrame(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickFluentWinUI3FocusFrame: a plain Python object
  standing in front of one C++ QQuickFluentWinUI3FocusFrame.

  What exists
  -----------

  Every function of Qt's QQuickFluentWinUI3FocusFrame that has a ritual and
  that Python can call so far, 5 names in all: 'metaObject', 'tr',
  'createFocusFrame', 'moveToItem', 'getFocusTarget'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickFluentWinUI3FocusFrame::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQuickFluentWinUI3FocusFrame::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 10 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickFluentWinUI3FocusFrame is created at the first use, not by
    'QQuickFluentWinUI3FocusFrame(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickFluentWinUI3FocusFrame.
  - Qt tells when it has removed the C++ QQuickFluentWinUI3FocusFrame. Every
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
    Calls Qt's 'QString QQuickFluentWinUI3FocusFrame::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfluentwinui3focusframe.html#tr

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
    #  QString QQuickFluentWinUI3FocusFrame::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN28QQuickFluentWinUI3FocusFrame2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickFluentWinUI3FocusFrame'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickFluentWinUI3FocusFrame::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfluentwinui3focusframe.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickFluentWinUI3FocusFrame::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickFluentWinUI3FocusFrame10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QQuickControl)
  @overload(NoneType)
  def getFocusTarget(
      self,
      focusItem: Optional[QQuickControl],
  ) -> Optional[QQuickControl]:
    """
    Calls Qt's 'QQuickControl
    *QQuickFluentWinUI3FocusFrame::getFocusTarget(QQuickControl *focusItem)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfluentwinui3focusframe.html#getFocusTarget

    Parameters
    ----------

    focusItem : Optional[QQuickControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickControl]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickControl
    #      *QQuickFluentWinUI3FocusFrame::getFocusTarget(QQuickControl
    #      *focusItem) const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickFluentWinUI3FocusFrame14getFocusTargetEP13QQuick'
        'Control',
        self._addressOf(focusItem),
    )
    from ..QtQuickTemplates2 import QQuickControl
    return QQuickControl._cuteAt(address)

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
    'QQuickFluentWinUI3FocusFrame::QQuickFluentWinUI3FocusFrame()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfluentwinui3focusframe.html
    """
    #  QQuickFluentWinUI3FocusFrame::QQuickFluentWinUI3FocusFrame()
    self._noteCreation(QQuickFluentWinUI3FocusFrame, lambda: Rituals.call(
        'ritual_ZN28QQuickFluentWinUI3FocusFrameC1Ev',
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

  @overload(QQmlContext)
  @overload(NoneType)
  def createFocusFrame(
      self,
      context: Optional[QQmlContext],
  ) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem
    *QQuickFluentWinUI3FocusFrame::createFocusFrame(QQmlContext *context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfluentwinui3focusframe.html#createFocusFrame

    Parameters
    ----------

    context : Optional[QQmlContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickFluentWinUI3FocusFrame::createFocusFrame(QQmlContext
    #      *context)
    address = self.uglySide.call(
        'ritual_ZN28QQuickFluentWinUI3FocusFrame16createFocusFrameEP11QQmlC'
        'ontext',
        self._addressOf(context),
    )
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  @overload(QQuickControl)
  @overload(NoneType)
  def moveToItem(self, item: Optional[QQuickControl]) -> None:
    """
    Calls Qt's 'void QQuickFluentWinUI3FocusFrame::moveToItem(QQuickControl
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfluentwinui3focusframe.html#moveToItem

    Parameters
    ----------

    item : Optional[QQuickControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFluentWinUI3FocusFrame::moveToItem(QQuickControl *item)
    self.uglySide.call(
        'ritual_ZN28QQuickFluentWinUI3FocusFrame10moveToItemEP13QQuickContr'
        'ol',
        self._addressOf(item),
    )
