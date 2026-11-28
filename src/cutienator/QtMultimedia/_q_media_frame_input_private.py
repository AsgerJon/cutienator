"""
QMediaFrameInputPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qmediaframeinput_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QMediaFrameInputPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QMediaCaptureSession
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMediaCaptureSession = WAIT['QMediaCaptureSession']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMediaFrameInputPrivate(QObjectPrivate):
  """
  The cute side of Qt's QMediaFrameInputPrivate: a plain Python object
  standing in front of one C++ QMediaFrameInputPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QMediaFrameInputPrivate
  is built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QMediaFrameInputPrivate that has a ritual and that
  Python can call so far, 7 names in all: 'setCaptureSession',
  'captureSession', 'updateCanSendMediaFrame', 'postponeCheckReadyToSend',
  'checkIfCanSendMediaFrame', 'emitReadyToSendMediaFrame',
  'updateCaptureSessionConnections'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has no ritual
  ------------------

  3 of the 10 functions Qt declares: 3 a template.

  What to expect
  --------------

  - The C++ QMediaFrameInputPrivate is created at the first use, not by
    'QMediaFrameInputPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMediaFrameInputPrivate.
  - Each name of Qt's QMediaFrameInputPrivate that has no cute function yet,
    'addUpdateSignal', 'removeUpdateSignal', 'sendMediaFrame', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMediaFrameInputPrivate'

  #  The functions Qt calls itself that QMediaFrameInputPrivate is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'checkIfCanSendMediaFrame': (
          ('_ZNK23QMediaFrameInputPrivate24checkIfCanSendMediaFrameEv',
           ('bool', 'number', ''),
           ()),
      ),
      'emitReadyToSendMediaFrame': (
          ('_ZN23QMediaFrameInputPrivate25emitReadyToSendMediaFrameEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'updateCaptureSessionConnections': (
          ('_ZN23QMediaFrameInputPrivate31updateCaptureSessionConnectionsEP'
           '20QMediaCaptureSessionS1_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtMultimedia:QMediaCaptureSession'),
               ('address', 'address', 'QtMultimedia:QMediaCaptureSession'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def captureSession(self) -> Optional[QMediaCaptureSession]:
    """
    Calls Qt's 'QMediaCaptureSession
    *QMediaFrameInputPrivate::captureSession() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaframeinputprivate.html#captureSession

    Returns
    -------

    Optional[QMediaCaptureSession]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMediaCaptureSession *QMediaFrameInputPrivate::captureSession() const
    address = self.uglySide.call(
        'ritual_ZNK23QMediaFrameInputPrivate14captureSessionEv',
    )
    from . import QMediaCaptureSession
    return QMediaCaptureSession._cuteAt(address)

  def checkIfCanSendMediaFrame(self) -> bool:
    """
    Calls Qt's 'bool QMediaFrameInputPrivate::checkIfCanSendMediaFrame()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaframeinputprivate.html
    """
    #  bool QMediaFrameInputPrivate::checkIfCanSendMediaFrame() const
    return self.uglySide.call(
        'ritual_ZNK23QMediaFrameInputPrivate24checkIfCanSendMediaFrameEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QMediaCaptureSession)
  @overload(NoneType)
  def setCaptureSession(
      self,
      session: Optional[QMediaCaptureSession],
  ) -> None:
    """
    Calls Qt's 'void
    QMediaFrameInputPrivate::setCaptureSession(QMediaCaptureSession
    *session)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaframeinputprivate.html#setCaptureSession

    Parameters
    ----------

    session : Optional[QMediaCaptureSession]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMediaFrameInputPrivate::setCaptureSession(QMediaCaptureSession
    #      *session)
    self.uglySide.call(
        'ritual_ZN23QMediaFrameInputPrivate17setCaptureSessionEP20QMediaCap'
        'tureSession',
        self._addressOf(session),
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

  def updateCanSendMediaFrame(self) -> None:
    """
    Calls Qt's 'void QMediaFrameInputPrivate::updateCanSendMediaFrame()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaframeinputprivate.html
    """
    #  void QMediaFrameInputPrivate::updateCanSendMediaFrame()
    self.uglySide.call(
        'ritual_ZN23QMediaFrameInputPrivate23updateCanSendMediaFrameEv',
    )

  def postponeCheckReadyToSend(self) -> None:
    """
    Calls Qt's 'void QMediaFrameInputPrivate::postponeCheckReadyToSend()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaframeinputprivate.html
    """
    #  void QMediaFrameInputPrivate::postponeCheckReadyToSend()
    self.uglySide.call(
        'ritual_ZN23QMediaFrameInputPrivate24postponeCheckReadyToSendEv',
    )

  def emitReadyToSendMediaFrame(self) -> None:
    """
    Calls Qt's 'void QMediaFrameInputPrivate::emitReadyToSendMediaFrame()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaframeinputprivate.html
    """
    #  void QMediaFrameInputPrivate::emitReadyToSendMediaFrame()
    self.uglySide.call(
        'ritual_ZN23QMediaFrameInputPrivate25emitReadyToSendMediaFrameEv',
    )

  @overload(QMediaCaptureSession, QMediaCaptureSession)
  @overload(QMediaCaptureSession, NoneType)
  @overload(NoneType, QMediaCaptureSession)
  @overload(NoneType, NoneType)
  def updateCaptureSessionConnections(
      self,
      prevSession: Optional[QMediaCaptureSession],
      currentSession: Optional[QMediaCaptureSession],
  ) -> None:
    """
    Calls Qt's 'void
    QMediaFrameInputPrivate::updateCaptureSessionConnections(
    QMediaCaptureSession *prevSession, QMediaCaptureSession
    *currentSession)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediaframeinputprivate.html

    Parameters
    ----------

    prevSession : Optional[QMediaCaptureSession]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    currentSession : Optional[QMediaCaptureSession]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMediaFrameInputPrivate::updateCaptureSessionConnections(
    #      QMediaCaptureSession *prevSession, QMediaCaptureSession
    #      *currentSession)
    self.uglySide.call(
        'ritual_ZN23QMediaFrameInputPrivate31updateCaptureSessionConnection'
        'sEP20QMediaCaptureSessionS1_',
        self._addressOf(prevSession), self._addressOf(currentSession),
    )

  @staticmethod
  def addUpdateSignal(*__, **_) -> Never:
    """
    Qt's 'QMediaFrameInputPrivate::addUpdateSignal': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'QMediaFrameInputPrivate.addUpdateSignal' has no cute function "
        "yet. Qt's 'QMediaFrameInputPrivate::addUpdateSignal': a template: "
        "a pattern and no single function.")

  @staticmethod
  def removeUpdateSignal(*__, **_) -> Never:
    """
    Qt's 'QMediaFrameInputPrivate::removeUpdateSignal': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'QMediaFrameInputPrivate.removeUpdateSignal' has no cute function "
        "yet. Qt's 'QMediaFrameInputPrivate::removeUpdateSignal': a "
        "template: a pattern and no single function.")

  @staticmethod
  def sendMediaFrame(*__, **_) -> Never:
    """
    Qt's 'QMediaFrameInputPrivate::sendMediaFrame': a template: a pattern and
    no single function.
    """
    raise NotImplementedError(
        "'QMediaFrameInputPrivate.sendMediaFrame' has no cute function yet. "
        "Qt's 'QMediaFrameInputPrivate::sendMediaFrame': a template: a "
        "pattern and no single function.")
