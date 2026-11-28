"""
QQuickWebEngineFrame binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebengineframe_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickWebEngineFrame to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QList
from ..QtWebEngineCore import QWebEngineFrame

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtQml import QJSValue
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJSValue = WAIT['QJSValue']


class QQuickWebEngineFrame(QWebEngineFrame):
  """
  The cute side of Qt's QQuickWebEngineFrame: a plain Python object standing
  in front of one C++ QQuickWebEngineFrame.

  It is built on the cute 'QWebEngineFrame', as Qt's QQuickWebEngineFrame is
  built on Qt's QWebEngineFrame, and has everything that class has.

  C++ hands a QQuickWebEngineFrame around as a copy, so every C++
  QQuickWebEngineFrame behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuickWebEngineFrame that has a ritual and that
  Python can call so far, 2 names in all: 'runJavaScript', 'printToPdf'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQuickWebEngineFrame::qt_qmlMarker_foreign()': one of Qt's own
    inner workings.
  - Qt's 'void QQuickWebEngineFrame::qt_qmlMarker_extended()': one of Qt's
    own inner workings.
  - Qt's 'QQuickWebEngineFrame::QQuickWebEngineFrame(
    QWeakPointer<QtWebEngineCore::WebContentsAdapter> adapter, quint64 id)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QQuickWebEngineFrame::~QQuickWebEngineFrame()': the destructor:
    Python removes its C++ QQuickWebEngineFrame by it, and has no other use
    for it.

  What has no ritual
  ------------------

  5 of the 12 functions Qt declares: 3 not a gap; 2 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QQuickWebEngineFrame is created at the first use, not by
    'QQuickWebEngineFrame(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickWebEngineFrame back gives a copy the ritual
    made for Python, in a new cute QQuickWebEngineFrame.
  - Each name of Qt's QQuickWebEngineFrame that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
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
  __qt_class__ = 'QQuickWebEngineFrame'

  #  Qt's '~QQuickWebEngineFrame()'. Naming it makes this a value class:
  #  Python owns every C++ QQuickWebEngineFrame behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QQuickWebEngineFrameD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    - Qt's 'QQuickWebEngineFrame::QQuickWebEngineFrame(
      QWeakPointer<QtWebEngineCore::WebContentsAdapter> adapter, quint64
      id)': takes a type Python has no way to hand over yet.
    - Qt's 'QQuickWebEngineFrame::QQuickWebEngineFrame()': Qt's library has
      no name for it, and its code in Qt's source does not compile apart from
      its file: incomplete type 'QtWebEngineCore::WebContentsAdapter' named
      in nested name specifier.
    """
    raise NotImplementedError(
        "'QQuickWebEngineFrame.__init__' has no cute function yet. Qt's "
        "'QQuickWebEngineFrame::QQuickWebEngineFrame(QWeakPointer<QtWebEngin"
        "eCore::WebContentsAdapter> adapter, quint64 id)': takes a type "
        "Python has no way to hand over yet. Qt's "
        "'QQuickWebEngineFrame::QQuickWebEngineFrame()': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: incomplete type "
        "'QtWebEngineCore::WebContentsAdapter' named in nested name "
        "specifier.")

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

  @overload(str, QJSValue)
  def runJavaScript(self, script: str, callback: QJSValue) -> None:
    """
    Calls Qt's 'void QQuickWebEngineFrame::runJavaScript(const QString
    &script, const QJSValue &callback)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineframe.html#runJavaScript

    Parameters
    ----------

    script : str
      Passed on as it is: a QString is made of it for the call.

    callback : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  void QQuickWebEngineFrame::runJavaScript(const QString &script, const
    #      QJSValue &callback)
    self.uglySide.call(
        'ritual_ZN20QQuickWebEngineFrame13runJavaScriptERK7QStringRK8QJSVal'
        'ue',
        script, self._valueOf(callback),
    )

  @overload(str, int, QJSValue)
  def runJavaScript(
      self,
      script: str,
      worldId: int,
      callback: QJSValue,
  ) -> None:
    """
    Calls Qt's 'void QQuickWebEngineFrame::runJavaScript(const QString
    &script, quint32 worldId, const QJSValue &callback)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineframe.html#runJavaScript

    Parameters
    ----------

    script : str
      Passed on as it is: a QString is made of it for the call.

    worldId : int
      Passed on as it is.

    callback : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  void QQuickWebEngineFrame::runJavaScript(const QString &script,
    #      quint32 worldId, const QJSValue &callback)
    self.uglySide.call(
        'ritual_ZN20QQuickWebEngineFrame13runJavaScriptERK7QStringjRK8QJSVa'
        'lue',
        script, worldId, self._valueOf(callback),
    )

  @overload(QJSValue)
  def printToPdf(self, callback: QJSValue) -> None:
    """
    Calls Qt's 'void QQuickWebEngineFrame::printToPdf(const QJSValue
    &callback)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineframe.html#printToPdf

    Parameters
    ----------

    callback : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  void QQuickWebEngineFrame::printToPdf(const QJSValue &callback)
    self.uglySide.call(
        'ritual_ZN20QQuickWebEngineFrame10printToPdfERK8QJSValue',
        self._valueOf(callback),
    )


#  Qt's 'QList<QQuickWebEngineFrame>': the list of QQuickWebEngineFrame,
#  which 'QList[QQuickWebEngineFrame]' gives. It is made here, so that there
#  is one as soon as there can be a QQuickWebEngineFrame.
QList.createKind(
    QQuickWebEngineFrame, 'value',
    make='ritual_list_make_QQuickWebEngineFrame',
    add='ritual_list_add_QQuickWebEngineFrame',
    size='ritual_list_size_QQuickWebEngineFrame',
    at='ritual_list_at_QQuickWebEngineFrame',
    drop='ritual_list_drop_QQuickWebEngineFrame',
)
