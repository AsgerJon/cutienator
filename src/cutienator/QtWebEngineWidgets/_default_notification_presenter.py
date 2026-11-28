"""
DefaultNotificationPresenter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineWidgets/6.12.0/QtWebEngineWidgets/private/qwebenginenotificationpresenter_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means DefaultNotificationPresenter to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class DefaultNotificationPresenter(QObject):
  """
  The cute side of Qt's DefaultNotificationPresenter: a plain Python object
  standing in front of one C++ DefaultNotificationPresenter.

  It is built on the cute 'QObject', as Qt's DefaultNotificationPresenter is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's DefaultNotificationPresenter that has a ritual and
  that Python can call so far, 3 names in all: 'metaObject',
  'messageClicked', 'closeNotification'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *DefaultNotificationPresenter::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int DefaultNotificationPresenter::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'DefaultNotificationPresenter::~DefaultNotificationPresenter()': the
    destructor: Python never removes a C++ DefaultNotificationPresenter.

  What has no ritual
  ------------------

  5 of the 11 functions Qt declares: 2 not a gap; 2 leans on
  'DefaultNotificationPresenter; 1 the compiler refuses its ritual as it
  would be written here.

  What to expect
  --------------

  - The C++ DefaultNotificationPresenter is created at the first use, not by
    'DefaultNotificationPresenter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DefaultNotificationPresenter.
  - Qt tells when it has removed the C++ DefaultNotificationPresenter. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's DefaultNotificationPresenter that has no cute function
    yet, '__init__', 'show', holds a function that raises
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
  __qt_class__ = 'DefaultNotificationPresenter'

  #  A C++ DefaultNotificationPresenter Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_DefaultNotificationPresenter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *DefaultNotificationPresenter::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/defaultnotificationpresenter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *DefaultNotificationPresenter::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK28DefaultNotificationPresenter10metaObjectEv',
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
    Qt's 'DefaultNotificationPresenter::DefaultNotificationPresenter(QObject
    *parent)': leans on
    'DefaultNotificationPresenter::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'DefaultNotificationPresenter.__init__' has no cute function yet. "
        "Qt's "
        "'DefaultNotificationPresenter::DefaultNotificationPresenter(QObject"
        " *parent)': leans on "
        "'DefaultNotificationPresenter::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  def messageClicked(self) -> None:
    """
    Calls Qt's 'void DefaultNotificationPresenter::messageClicked()'.

    Qt's own words:
    https://doc.qt.io/qt-6/defaultnotificationpresenter.html#messageClicked
    """
    #  void DefaultNotificationPresenter::messageClicked()
    self.uglySide.call(
        'ritual_ZN28DefaultNotificationPresenter14messageClickedEv',
    )

  def closeNotification(self) -> None:
    """
    Calls Qt's 'void DefaultNotificationPresenter::closeNotification()'.

    Qt's own words:
    https://doc.qt.io/qt-6/defaultnotificationpresenter.html
    """
    #  void DefaultNotificationPresenter::closeNotification()
    self.uglySide.call(
        'ritual_ZN28DefaultNotificationPresenter17closeNotificationEv',
    )

  @staticmethod
  def show(*__, **_) -> Never:
    """
    Qt's 'void DefaultNotificationPresenter::show(std::
    unique_ptr<QWebEngineNotification> notification)': the compiler refuses
    its ritual as it would be written here: call to deleted constructor of
    'std::unique_ptr<QWebEngineNotification>'.
    """
    raise NotImplementedError(
        "'DefaultNotificationPresenter.show' has no cute function yet. Qt's "
        "'void "
        "DefaultNotificationPresenter::show(std::unique_ptr<QWebEngineNotifi"
        "cation> notification)': the compiler refuses its ritual as it "
        "would be written here: call to deleted constructor of "
        "'std::unique_ptr<QWebEngineNotification>'.")
