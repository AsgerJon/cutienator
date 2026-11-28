"""
FaviconImageRequester binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebenginefaviconprovider_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means FaviconImageRequester to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QIcon, QPixmap
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QIcon = WAIT['QIcon']
  QPixmap = WAIT['QPixmap']


class FaviconImageRequester(QObject):
  """
  The cute side of Qt's FaviconImageRequester: a plain Python object standing
  in front of one C++ FaviconImageRequester.

  It is built on the cute 'QObject', as Qt's FaviconImageRequester is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's FaviconImageRequester that has a ritual and that
  Python can call so far, 3 names in all: 'metaObject', 'iconRequestDone',
  'done'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *FaviconImageRequester::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int FaviconImageRequester::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  8 of the 13 functions Qt declares: 3 leans on 'FaviconImageRequester; 2 not
  a gap; 2 Qt's library has no name for it, and its code in Qt's source does
  not compile apart from its file; 1 leans on 'vtable for
  FaviconImageRequester', which Qt's source does not mark for use from
  outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ FaviconImageRequester is created at the first use, not by
    'FaviconImageRequester(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ FaviconImageRequester.
  - Qt tells when it has removed the C++ FaviconImageRequester. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's FaviconImageRequester that has no cute function yet,
    '__init__', 'getNextViewForProcessing', 'requestFaviconFromDatabase',
    'start', 'tryNextView', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'FaviconImageRequester'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *FaviconImageRequester::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/faviconimagerequester.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *FaviconImageRequester::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21FaviconImageRequester10metaObjectEv',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'FaviconImageRequester::FaviconImageRequester(const QUrl
    &imageSource, const QSize &requestedSize, bool isIconUrl)': leans on
    'vtable for FaviconImageRequester', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'FaviconImageRequester.__init__' has no cute function yet. Qt's "
        "'FaviconImageRequester::FaviconImageRequester(const QUrl "
        "&imageSource, const QSize &requestedSize, bool isIconUrl)': leans "
        "on 'vtable for FaviconImageRequester', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

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

  @overload(QIcon)
  def iconRequestDone(self, icon: QIcon) -> None:
    """
    Calls Qt's 'void FaviconImageRequester::iconRequestDone(const QIcon
    &icon)'.

    Qt's own words:
    https://doc.qt.io/qt-6/faviconimagerequester.html#iconRequestDone

    Parameters
    ----------

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.
    """
    #  void FaviconImageRequester::iconRequestDone(const QIcon &icon)
    self.uglySide.call(
        'ritual_ZN21FaviconImageRequester15iconRequestDoneERK5QIcon',
        self._valueOf(icon),
    )

  @overload(QPixmap)
  def done(self, pixmap: QPixmap) -> None:
    """
    Calls Qt's 'void FaviconImageRequester::done(QPixmap pixmap)'.

    Qt's own words: https://doc.qt.io/qt-6/faviconimagerequester.html#done

    Parameters
    ----------

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.
    """
    #  void FaviconImageRequester::done(QPixmap pixmap)
    self.uglySide.call(
        'ritual_ZN21FaviconImageRequester4doneE7QPixmap',
        self._valueOf(pixmap),
    )

  @staticmethod
  def getNextViewForProcessing(*__, **_) -> Never:
    """
    Qt's 'QPointer<QQuickWebEngineView>
    FaviconImageRequester::getNextViewForProcessing()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'QQuickWebEngineView'.
    """
    raise NotImplementedError(
        "'FaviconImageRequester.getNextViewForProcessing' has no cute "
        "function yet. Qt's 'QPointer<QQuickWebEngineView> "
        "FaviconImageRequester::getNextViewForProcessing()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: member access into incomplete type "
        "'QQuickWebEngineView'.")

  @staticmethod
  def requestFaviconFromDatabase(*__, **_) -> Never:
    """
    Qt's 'void FaviconImageRequester::requestFaviconFromDatabase(
    QPointer<QQuickWebEngineView> view)': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: member
    access into incomplete type 'QQuickWebEngineView'.
    """
    raise NotImplementedError(
        "'FaviconImageRequester.requestFaviconFromDatabase' has no cute "
        "function yet. Qt's 'void "
        "FaviconImageRequester::requestFaviconFromDatabase(QPointer<QQuickWe"
        "bEngineView> view)': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: member access "
        "into incomplete type 'QQuickWebEngineView'.")

  @staticmethod
  def start(*__, **_) -> Never:
    """
    Qt's 'void FaviconImageRequester::start()': leans on
    'FaviconImageRequester::done(QPixmap)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'FaviconImageRequester.start' has no cute function yet. Qt's 'void "
        "FaviconImageRequester::start()': leans on "
        "'FaviconImageRequester::done(QPixmap)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def tryNextView(*__, **_) -> Never:
    """
    Qt's 'bool FaviconImageRequester::tryNextView()': leans on
    'FaviconImageRequester::requestFaviconFromDatabase(
    QPointer<QQuickWebEngineView>)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'FaviconImageRequester.tryNextView' has no cute function yet. Qt's "
        "'bool FaviconImageRequester::tryNextView()': leans on "
        "'FaviconImageRequester::requestFaviconFromDatabase(QPointer<QQuickW"
        "ebEngineView>)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")
