"""
QQuickWebEngineTouchSelectionMenuRequest binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebenginetouchselectionmenurequest_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickWebEngineTouchSelectionMenuRequest to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QRect

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickWebEngineTouchSelectionMenuRequest(QObject):
  """
  The cute side of Qt's QQuickWebEngineTouchSelectionMenuRequest: a plain
  Python object standing in front of one C++
  QQuickWebEngineTouchSelectionMenuRequest.

  It is built on the cute 'QObject', as Qt's
  QQuickWebEngineTouchSelectionMenuRequest is built on Qt's QObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickWebEngineTouchSelectionMenuRequest that has a
  ritual and that Python can call so far, 7 names in all: 'metaObject', 'tr',
  'buttonCount', 'isAccepted', 'setAccepted', 'selectionBounds',
  'touchSelectionCommandFlags'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickWebEngineTouchSelectionMenuRequest::qt_metacast(const
    char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QQuickWebEngineTouchSelectionMenuRequest::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void
    QQuickWebEngineTouchSelectionMenuRequest::qt_qmlMarker_uncreatable()':
    one of Qt's own inner workings.
  - Qt's 'QQuickWebEngineTouchSelectionMenuRequest::
    QQuickWebEngineTouchSelectionMenuRequest(QRect bounds,
    QtWebEngineCore::TouchSelectionMenuController
    *touchSelectionMenuController)': names
    'QtWebEngineCore::TouchSelectionMenuController', which has no cute class
    yet.
  - Qt's 'QQuickWebEngineTouchSelectionMenuRequest::
    ~QQuickWebEngineTouchSelectionMenuRequest()': the destructor: Python
    never removes a C++ QQuickWebEngineTouchSelectionMenuRequest.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickWebEngineTouchSelectionMenuRequest is created at the first
    use, not by 'QQuickWebEngineTouchSelectionMenuRequest(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickWebEngineTouchSelectionMenuRequest.
  - Qt tells when it has removed the C++
    QQuickWebEngineTouchSelectionMenuRequest. Every call on the cute object,
    and every use of it as an argument, then raises 'RuntimeError', and
    nothing reaches C++.
  - Each name of Qt's QQuickWebEngineTouchSelectionMenuRequest that has no
    cute function yet, '__init__', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuickWebEngineTouchSelectionMenuRequest,
  #  each a class in here as in C++, and the names Qt has for the
  #  combinations of its flags enums.

  class QmlIsUncreatable(CuteNum, scoped=True):
    """
    The enum 'QQuickWebEngineTouchSelectionMenuRequest::QmlIsUncreatable' of
    Qt, with the 1 names Qt gives in it. C++ keeps these names inside the
    enum, so the class that holds the enum does not have them.
    """

    yes = Kee[int](1)

  class TouchSelectionCommandFlag(CuteFlags):
    """
    The flags enum
    'QQuickWebEngineTouchSelectionMenuRequest::TouchSelectionCommandFlag' of
    Qt, with the 3 names Qt gives in it. Qt names the type of its
    combinations
    'QQuickWebEngineTouchSelectionMenuRequest::TouchSelectionCommandFlags'.
    """

    Cut = 0x1
    Copy = 0x2
    Paste = 0x4

  TouchSelectionCommandFlags = TouchSelectionCommandFlag

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
    Calls Qt's 'QString QQuickWebEngineTouchSelectionMenuRequest::tr(const
    char *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginetouchselectionmenurequest.html#tr

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
    #  QString QQuickWebEngineTouchSelectionMenuRequest::tr(const char *s,
    #      const char *c, int n)
    return Rituals.call(
        'ritual_ZN40QQuickWebEngineTouchSelectionMenuRequest2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickWebEngineTouchSelectionMenuRequest'

  #  A C++ QQuickWebEngineTouchSelectionMenuRequest Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickWebEngineTouchSelectionMenuRequest'

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
    *QQuickWebEngineTouchSelectionMenuRequest::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginetouchselectionmenurequest.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *QQuickWebEngineTouchSelectionMenuRequest::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK40QQuickWebEngineTouchSelectionMenuRequest10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isAccepted(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineTouchSelectionMenuRequest::isAccepted()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginetouchselectionmenurequest.html
    """
    #  bool QQuickWebEngineTouchSelectionMenuRequest::isAccepted() const
    return self.uglySide.call(
        'ritual_ZNK40QQuickWebEngineTouchSelectionMenuRequest10isAcceptedEv',
    )

  def touchSelectionCommandFlags(self) -> TouchSelectionCommandFlags:
    """
    Calls Qt's 'TouchSelectionCommandFlags
    QQuickWebEngineTouchSelectionMenuRequest::touchSelectionCommandFlags()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginetouchselectionmenurequest.html

    Returns
    -------

    TouchSelectionCommandFlags
      The value standing for the combination Qt gave back.
    """
    #  TouchSelectionCommandFlags QQuickWebEngineTouchSelectionMenuRequest::
    #      touchSelectionCommandFlags() const
    return QQuickWebEngineTouchSelectionMenuRequest.TouchSelectionCommandFlags(
        self.uglySide.call(
            'ritual_ZNK40QQuickWebEngineTouchSelectionMenuRequest26touchSel'
            'ectionCommandFlagsEv',
        ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setAccepted(self, accepted: bool) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineTouchSelectionMenuRequest::setAccepted(bool accepted)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginetouchselectionmenurequest.html

    Parameters
    ----------

    accepted : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineTouchSelectionMenuRequest::setAccepted(bool
    #      accepted)
    self.uglySide.call(
        'ritual_ZN40QQuickWebEngineTouchSelectionMenuRequest11setAcceptedEb',
        accepted,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQuickWebEngineTouchSelectionMenuRequest::
    QQuickWebEngineTouchSelectionMenuRequest(QRect bounds,
    QtWebEngineCore::TouchSelectionMenuController
    *touchSelectionMenuController)': names
    'QtWebEngineCore::TouchSelectionMenuController', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QQuickWebEngineTouchSelectionMenuRequest.__init__' has no cute "
        "function yet. Qt's "
        "'QQuickWebEngineTouchSelectionMenuRequest::QQuickWebEngineTouchSele"
        "ctionMenuRequest(QRect bounds, "
        "QtWebEngineCore::TouchSelectionMenuController "
        "*touchSelectionMenuController)': names "
        "'QtWebEngineCore::TouchSelectionMenuController', which has no cute "
        "class yet.")

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

  def buttonCount(self) -> int:
    """
    Calls Qt's 'int QQuickWebEngineTouchSelectionMenuRequest::buttonCount()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginetouchselectionmenurequest.html
    """
    #  int QQuickWebEngineTouchSelectionMenuRequest::buttonCount()
    return self.uglySide.call(
        'ritual_ZN40QQuickWebEngineTouchSelectionMenuRequest11buttonCountEv',
    )

  def selectionBounds(self) -> QRect:
    """
    Calls Qt's 'QRect
    QQuickWebEngineTouchSelectionMenuRequest::selectionBounds()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginetouchselectionmenurequest.html

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QQuickWebEngineTouchSelectionMenuRequest::selectionBounds()
    address = self.uglySide.call(
        'ritual_ZN40QQuickWebEngineTouchSelectionMenuRequest15selectionBoun'
        'dsEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)
