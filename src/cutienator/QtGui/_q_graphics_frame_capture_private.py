"""
QGraphicsFrameCapturePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qgraphicsframecapture_p_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QGraphicsFrameCapturePrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QRhi
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhi = WAIT['QRhi']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsFrameCapturePrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGraphicsFrameCapturePrivate: a plain Python object
  standing in front of one C++ QGraphicsFrameCapturePrivate.

  What exists
  -----------

  Every function of Qt's QGraphicsFrameCapturePrivate that has a ritual and
  that Python can call so far, 12 names in all: 'setRhi',
  'startCaptureFrame', 'endCaptureFrame', 'capturePath', 'setCapturePath',
  'capturePrefix', 'setCapturePrefix', 'capturedFileName',
  'capturedFilesNames', 'initialized', 'isCapturing', 'openCapture'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGraphicsFrameCapturePrivate::~QGraphicsFrameCapturePrivate()': the
    destructor: Python never removes a C++ QGraphicsFrameCapturePrivate.

  What to expect
  --------------

  - The C++ QGraphicsFrameCapturePrivate is created at the first use, not by
    'QGraphicsFrameCapturePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsFrameCapturePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsFrameCapturePrivate'

  #  A C++ QGraphicsFrameCapturePrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphicsFrameCapturePrivate'

  #  The functions Qt calls itself that QGraphicsFrameCapturePrivate is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'capturedFilesNames': (
          'QStringList QGraphicsFrameCapturePrivate::capturedFilesNames() '
          'const',
      ),
  }

  #  The functions Qt calls itself that QGraphicsFrameCapturePrivate is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'setRhi': (
          ('_ZN28QGraphicsFrameCapturePrivate6setRhiEP4QRhi',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QRhi'),
           )),
      ),
      'startCaptureFrame': (
          ('_ZN28QGraphicsFrameCapturePrivate17startCaptureFrameEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'endCaptureFrame': (
          ('_ZN28QGraphicsFrameCapturePrivate15endCaptureFrameEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'setCapturePath': (
          ('_ZN28QGraphicsFrameCapturePrivate14setCapturePathERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'setCapturePrefix': (
          ('_ZN28QGraphicsFrameCapturePrivate16setCapturePrefixERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'capturedFileName': (
          ('_ZNK28QGraphicsFrameCapturePrivate16capturedFileNameEv',
           ('address', 'text', ''),
           ()),
      ),
      'initialized': (
          ('_ZNK28QGraphicsFrameCapturePrivate11initializedEv',
           ('bool', 'number', ''),
           ()),
      ),
      'isCapturing': (
          ('_ZNK28QGraphicsFrameCapturePrivate11isCapturingEv',
           ('bool', 'number', ''),
           ()),
      ),
      'openCapture': (
          ('_ZN28QGraphicsFrameCapturePrivate11openCaptureEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def capturePath(self) -> str:
    """
    Calls Qt's 'QString QGraphicsFrameCapturePrivate::capturePath() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsframecaptureprivate.html#capturePath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGraphicsFrameCapturePrivate::capturePath() const
    return self.uglySide.call(
        'ritual_ZNK28QGraphicsFrameCapturePrivate11capturePathEv',
    )

  def capturePrefix(self) -> str:
    """
    Calls Qt's 'QString QGraphicsFrameCapturePrivate::capturePrefix() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsframecaptureprivate.html#capturePrefix

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGraphicsFrameCapturePrivate::capturePrefix() const
    return self.uglySide.call(
        'ritual_ZNK28QGraphicsFrameCapturePrivate13capturePrefixEv',
    )

  def capturedFileName(self) -> str:
    """
    Calls Qt's 'QString QGraphicsFrameCapturePrivate::capturedFileName()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsframecaptureprivate.html#capturedFileName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGraphicsFrameCapturePrivate::capturedFileName() const
    ritual = 'ritual_ZNK28QGraphicsFrameCapturePrivate16capturedFileNameEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK28QGraphicsFrameCapturePrivate16capturedFileNameEv')
    return self.uglySide.call(ritual)

  def capturedFilesNames(self) -> QStringList:
    """
    Calls Qt's 'QStringList
    QGraphicsFrameCapturePrivate::capturedFilesNames() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsframecaptureprivate.html

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QGraphicsFrameCapturePrivate::capturedFilesNames() const
    address = self.uglySide.call(
        'ritual_ZNK28QGraphicsFrameCapturePrivate18capturedFilesNamesEv',
    )
    return QStringList._cuteOwning(address)

  def initialized(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsFrameCapturePrivate::initialized() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsframecaptureprivate.html#initialized
    """
    #  bool QGraphicsFrameCapturePrivate::initialized() const
    return self.uglySide.call(
        'ritual_ZNK28QGraphicsFrameCapturePrivate11initializedEv',
    )

  def isCapturing(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsFrameCapturePrivate::isCapturing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsframecaptureprivate.html#isCapturing
    """
    #  bool QGraphicsFrameCapturePrivate::isCapturing() const
    return self.uglySide.call(
        'ritual_ZNK28QGraphicsFrameCapturePrivate11isCapturingEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRhi)
  @overload(NoneType)
  def setRhi(self, rhi: Optional[QRhi]) -> None:
    """
    Calls Qt's 'void QGraphicsFrameCapturePrivate::setRhi(QRhi *rhi)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsframecaptureprivate.html#setRhi

    Parameters
    ----------

    rhi : Optional[QRhi]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsFrameCapturePrivate::setRhi(QRhi *rhi)
    self.uglySide.call(
        'ritual_ZN28QGraphicsFrameCapturePrivate6setRhiEP4QRhi',
        self._addressOf(rhi),
    )

  @overload(str)
  def setCapturePath(self, path: str) -> None:
    """
    Calls Qt's 'void QGraphicsFrameCapturePrivate::setCapturePath(const
    QString &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsframecaptureprivate.html#setCapturePath

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGraphicsFrameCapturePrivate::setCapturePath(const QString &path)
    ritual = (
        'ritual_ZN28QGraphicsFrameCapturePrivate14setCapturePathERK7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QGraphicsFrameCapturePrivate14setCapturePathERK7Q'
          'String')
    self.uglySide.call(ritual, path)

  @overload(str)
  def setCapturePrefix(self, prefix: str) -> None:
    """
    Calls Qt's 'void QGraphicsFrameCapturePrivate::setCapturePrefix(const
    QString &prefix)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsframecaptureprivate.html#setCapturePrefix

    Parameters
    ----------

    prefix : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGraphicsFrameCapturePrivate::setCapturePrefix(const QString
    #      &prefix)
    ritual = (
        'ritual_ZN28QGraphicsFrameCapturePrivate16setCapturePrefixERK7QStri'
        'ng')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QGraphicsFrameCapturePrivate16setCapturePrefixERK'
          '7QString')
    self.uglySide.call(ritual, prefix)

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
    'QGraphicsFrameCapturePrivate::QGraphicsFrameCapturePrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsframecaptureprivate.html
    """
    #  QGraphicsFrameCapturePrivate::QGraphicsFrameCapturePrivate()
    self._noteCreation(QGraphicsFrameCapturePrivate, lambda: Rituals.call(
        'ritual_ZN28QGraphicsFrameCapturePrivateC1Ev',
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

  def startCaptureFrame(self) -> None:
    """
    Calls Qt's 'void QGraphicsFrameCapturePrivate::startCaptureFrame()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsframecaptureprivate.html
    """
    #  void QGraphicsFrameCapturePrivate::startCaptureFrame()
    self.uglySide.call(
        'ritual_ZN28QGraphicsFrameCapturePrivate17startCaptureFrameEv',
    )

  def endCaptureFrame(self) -> None:
    """
    Calls Qt's 'void QGraphicsFrameCapturePrivate::endCaptureFrame()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsframecaptureprivate.html#endCaptureFrame
    """
    #  void QGraphicsFrameCapturePrivate::endCaptureFrame()
    self.uglySide.call(
        'ritual_ZN28QGraphicsFrameCapturePrivate15endCaptureFrameEv',
    )

  def openCapture(self) -> None:
    """
    Calls Qt's 'void QGraphicsFrameCapturePrivate::openCapture()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsframecaptureprivate.html#openCapture
    """
    #  void QGraphicsFrameCapturePrivate::openCapture()
    self.uglySide.call(
        'ritual_ZN28QGraphicsFrameCapturePrivate11openCaptureEv',
    )
