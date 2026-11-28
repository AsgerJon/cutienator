"""
QQmlNotifyingBlob binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlnotifyingblob_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlNotifyingBlob to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlNotifyingBlob(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlNotifyingBlob: a plain Python object standing in
  front of one C++ QQmlNotifyingBlob.

  What exists
  -----------

  Every function of Qt's QQmlNotifyingBlob that has a ritual and that Python
  can call so far, 4 names in all: 'registerCallback', 'unregisterCallback',
  'completed', 'downloadProgressChanged'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has no ritual
  ------------------

  1 of the 5 functions Qt declares: 1 the class is abstract, so C++ cannot
  make one, and the C++ class of ours does not fill in every function it
  leaves open.

  What to expect
  --------------

  - The C++ QQmlNotifyingBlob is created at the first use, not by
    'QQmlNotifyingBlob(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlNotifyingBlob.
  - Each name of Qt's QQmlNotifyingBlob that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The classes Qt writes inside QQmlNotifyingBlob, each a class in here as
  #  in C++.

  class Callback(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlNotifyingBlob::Callback: a plain Python object
    standing in front of one C++ QQmlNotifyingBlob::Callback.

    C++ hands a QQmlNotifyingBlob::Callback around as a copy, so every C++
    QQmlNotifyingBlob::Callback behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QQmlNotifyingBlob::Callback that has a ritual and
    that Python can call so far, 2 names in all: 'ready', 'progress'. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlNotifyingBlob::Callback::~Callback()': the destructor: Python
      removes its C++ QQmlNotifyingBlob::Callback by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QQmlNotifyingBlob::Callback is created at the first use, not by
      'QQmlNotifyingBlob::Callback(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlNotifyingBlob::Callback back gives a copy the
      ritual made for Python, in a new cute QQmlNotifyingBlob::Callback.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QQmlNotifyingBlob = WAIT['QQmlNotifyingBlob']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlNotifyingBlob::Callback'

    #  A C++ QQmlNotifyingBlob::Callback Python makes is of a C++ class of
    #  ours, in which Python can take functions over. This ritual hands one
    #  over; see 'CuteMixin._takeOver'.
    __take_ritual__ = 'ritual_take_QQmlNotifyingBlob_Callback'

    #  The functions Qt calls itself that QQmlNotifyingBlob::Callback is the
    #  first to declare. A class of a program built on it can write one anew,
    #  and Qt then calls that. For each name: the key C++ knows the function
    #  by, what it gives, and what it takes.
    __virtual_functions__ = {
        'ready': (
            ('_ZN17QQmlNotifyingBlob8Callback5readyEPS_',
             ('nothing', 'nothing', ''),
             (
                 ('address', 'address', 'QtQml:QQmlNotifyingBlob'),
             )),
        ),
        'progress': (
            ('_ZN17QQmlNotifyingBlob8Callback8progressEPS_d',
             ('nothing', 'nothing', ''),
             (
                 ('address', 'address', 'QtQml:QQmlNotifyingBlob'),
                 ('double', 'number', ''),
             )),
        ),
    }

    #  Qt's '~QQmlNotifyingBlob::Callback()'. Naming it makes this a value
    #  class: Python owns every C++ QQmlNotifyingBlob::Callback behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN17QQmlNotifyingBlob8CallbackD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(QQmlNotifyingBlob)
    @overload(NoneType)
    def ready(self, a0: Optional[QQmlNotifyingBlob]) -> None:
      """
      Calls Qt's 'void QQmlNotifyingBlob::Callback::ready(QQmlNotifyingBlob
      *a0)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlnotifyingblob-callback.html#ready

      Parameters
      ----------

      a0 : Optional[QQmlNotifyingBlob]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  void QQmlNotifyingBlob::Callback::ready(QQmlNotifyingBlob *a0)
      ritual = 'ritual_ZN17QQmlNotifyingBlob8Callback5readyEPS_'
      if self.uglySide.isOurs():
        ritual = 'ritual_own_ZN17QQmlNotifyingBlob8Callback5readyEPS_'
      self._callAs(
          'QQmlNotifyingBlob::Callback', ritual, self._addressOf(a0),
      )

    @overload(QQmlNotifyingBlob, float)
    @overload(NoneType, float)
    def progress(self, a0: Optional[QQmlNotifyingBlob], a1: float) -> None:
      """
      Calls Qt's 'void
      QQmlNotifyingBlob::Callback::progress(QQmlNotifyingBlob *a0, qreal
      a1)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlnotifyingblob-callback.html#progress

      Parameters
      ----------

      a0 : Optional[QQmlNotifyingBlob]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      a1 : float
        Passed on as it is.
      """
      #  void QQmlNotifyingBlob::Callback::progress(QQmlNotifyingBlob *a0,
      #      qreal a1)
      ritual = 'ritual_ZN17QQmlNotifyingBlob8Callback8progressEPS_d'
      if self.uglySide.isOurs():
        ritual = 'ritual_own_ZN17QQmlNotifyingBlob8Callback8progressEPS_d'
      self._callAs(
          'QQmlNotifyingBlob::Callback', ritual, self._addressOf(a0), a1,
      )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlNotifyingBlob'

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
    Qt's 'QQmlNotifyingBlob::QQmlNotifyingBlob(const QUrl &url,
    QQmlDataBlob::Type type, QQmlTypeLoader *loader)': the class is abstract,
    so C++ cannot make one, and the C++ class of ours does not fill in every
    function it leaves open.
    """
    raise NotImplementedError(
        "'QQmlNotifyingBlob.__init__' has no cute function yet. Qt's "
        "'QQmlNotifyingBlob::QQmlNotifyingBlob(const QUrl &url, "
        "QQmlDataBlob::Type type, QQmlTypeLoader *loader)': the class is "
        "abstract, so C++ cannot make one, and the C++ class of ours does "
        "not fill in every function it leaves open.")

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

  @overload(Callback)
  @overload(NoneType)
  def registerCallback(self, callback: Optional[Callback]) -> None:
    """
    Calls Qt's 'void QQmlNotifyingBlob::registerCallback(Callback
    *callback)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlnotifyingblob.html#registerCallback

    Parameters
    ----------

    callback : Optional[Callback]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlNotifyingBlob::registerCallback(Callback *callback)
    self.uglySide.call(
        'ritual_ZN17QQmlNotifyingBlob16registerCallbackEPNS_8CallbackE',
        self._addressOf(callback, 'QQmlNotifyingBlob::Callback'),
    )

  @overload(Callback)
  @overload(NoneType)
  def unregisterCallback(self, callback: Optional[Callback]) -> None:
    """
    Calls Qt's 'void QQmlNotifyingBlob::unregisterCallback(Callback
    *callback)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlnotifyingblob.html#unregisterCallback

    Parameters
    ----------

    callback : Optional[Callback]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlNotifyingBlob::unregisterCallback(Callback *callback)
    self.uglySide.call(
        'ritual_ZN17QQmlNotifyingBlob18unregisterCallbackEPNS_8CallbackE',
        self._addressOf(callback, 'QQmlNotifyingBlob::Callback'),
    )

  def completed(self) -> None:
    """
    Calls Qt's 'void QQmlNotifyingBlob::completed()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlnotifyingblob.html#completed
    """
    #  void QQmlNotifyingBlob::completed()
    ritual = 'ritual_ZN17QQmlNotifyingBlob9completedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlNotifyingBlob9completedEv'
    self.uglySide.call(ritual)

  @overload(float)
  def downloadProgressChanged(self, a0: float) -> None:
    """
    Calls Qt's 'void QQmlNotifyingBlob::downloadProgressChanged(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlnotifyingblob.html#downloadProgressChanged

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQmlNotifyingBlob::downloadProgressChanged(qreal a0)
    ritual = 'ritual_ZN17QQmlNotifyingBlob23downloadProgressChangedEd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlNotifyingBlob23downloadProgressChangedEd'
    self.uglySide.call(ritual, a0)
