"""
QQuickWebEngineColorDialogRequest binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebenginedialogrequests_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickWebEngineColorDialogRequest to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QColor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickWebEngineColorDialogRequest(QObject):
  """
  The cute side of Qt's QQuickWebEngineColorDialogRequest: a plain Python
  object standing in front of one C++ QQuickWebEngineColorDialogRequest.

  It is built on the cute 'QObject', as Qt's
  QQuickWebEngineColorDialogRequest is built on Qt's QObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickWebEngineColorDialogRequest that has a ritual
  and that Python can call so far, 7 names in all: 'metaObject', 'tr',
  'color', 'isAccepted', 'setAccepted', 'dialogAccept', 'dialogReject'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickWebEngineColorDialogRequest::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QQuickWebEngineColorDialogRequest::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void
    QQuickWebEngineColorDialogRequest::qt_qmlMarker_uncreatable()': one of
    Qt's own inner workings.
  - Qt's
    'QQuickWebEngineColorDialogRequest::~QQuickWebEngineColorDialogRequest(
    )': the destructor: Python never removes a C++
    QQuickWebEngineColorDialogRequest.
  - Qt's
    'QQuickWebEngineColorDialogRequest::QQuickWebEngineColorDialogRequest(
    QSharedPointer<QtWebEngineCore::ColorChooserController> controller,
    QObject *parent)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickWebEngineColorDialogRequest is created at the first use,
    not by 'QQuickWebEngineColorDialogRequest(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickWebEngineColorDialogRequest.
  - Qt tells when it has removed the C++ QQuickWebEngineColorDialogRequest.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickWebEngineColorDialogRequest that has no cute
    function yet, '__init__', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuickWebEngineColorDialogRequest, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class QmlIsUncreatable(CuteNum, scoped=True):
    """
    The enum 'QQuickWebEngineColorDialogRequest::QmlIsUncreatable' of Qt,
    with the 1 names Qt gives in it. C++ keeps these names inside the enum,
    so the class that holds the enum does not have them.
    """

    yes = Kee[int](1)

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
    Calls Qt's 'QString QQuickWebEngineColorDialogRequest::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginecolordialogrequest.html#tr

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
    #  QString QQuickWebEngineColorDialogRequest::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN33QQuickWebEngineColorDialogRequest2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickWebEngineColorDialogRequest'

  #  A C++ QQuickWebEngineColorDialogRequest Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickWebEngineColorDialogRequest'

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
    *QQuickWebEngineColorDialogRequest::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginecolordialogrequest.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickWebEngineColorDialogRequest::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK33QQuickWebEngineColorDialogRequest10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickWebEngineColorDialogRequest::color() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginecolordialogrequest.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickWebEngineColorDialogRequest::color() const
    address = self.uglySide.call(
        'ritual_ZNK33QQuickWebEngineColorDialogRequest5colorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def isAccepted(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineColorDialogRequest::isAccepted() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginecolordialogrequest.html#isAccepted
    """
    #  bool QQuickWebEngineColorDialogRequest::isAccepted() const
    return self.uglySide.call(
        'ritual_ZNK33QQuickWebEngineColorDialogRequest10isAcceptedEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setAccepted(self, accepted: bool) -> None:
    """
    Calls Qt's 'void QQuickWebEngineColorDialogRequest::setAccepted(bool
    accepted)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginecolordialogrequest.html#setAccepted

    Parameters
    ----------

    accepted : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineColorDialogRequest::setAccepted(bool accepted)
    self.uglySide.call(
        'ritual_ZN33QQuickWebEngineColorDialogRequest11setAcceptedEb',
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
    Qt's
    'QQuickWebEngineColorDialogRequest::QQuickWebEngineColorDialogRequest(
    QSharedPointer<QtWebEngineCore::ColorChooserController> controller,
    QObject *parent)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickWebEngineColorDialogRequest.__init__' has no cute function "
        "yet. Qt's "
        "'QQuickWebEngineColorDialogRequest::QQuickWebEngineColorDialogReque"
        "st(QSharedPointer<QtWebEngineCore::ColorChooserController> "
        "controller, QObject *parent)': takes a type Python has no way to "
        "hand over yet.")

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

  @overload(QColor)
  def dialogAccept(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickWebEngineColorDialogRequest::dialogAccept(const
    QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginecolordialogrequest.html

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickWebEngineColorDialogRequest::dialogAccept(const QColor
    #      &color)
    self.uglySide.call(
        'ritual_ZN33QQuickWebEngineColorDialogRequest12dialogAcceptERK6QCol'
        'or',
        self._valueOf(color),
    )

  def dialogReject(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineColorDialogRequest::dialogReject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginecolordialogrequest.html
    """
    #  void QQuickWebEngineColorDialogRequest::dialogReject()
    self.uglySide.call(
        'ritual_ZN33QQuickWebEngineColorDialogRequest12dialogRejectEv',
    )
