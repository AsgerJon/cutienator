"""
QQuickImageCapture binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimediaQuick/6.12.0/QtMultimediaQuick/private/qquickimagecapture_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickImageCapture to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtMultimedia import QImageCapture

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QImage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QImage = WAIT['QImage']


class QQuickImageCapture(QImageCapture):
  """
  The cute side of Qt's QQuickImageCapture: a plain Python object standing in
  front of one C++ QQuickImageCapture.

  It is built on the cute 'QImageCapture', as Qt's QQuickImageCapture is
  built on Qt's QImageCapture, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickImageCapture that has a ritual and that Python
  can call so far, 4 names in all: 'metaObject', 'preview', 'previewChanged',
  '_q_imageCaptured'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickImageCapture::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickImageCapture::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickImageCapture::~QQuickImageCapture()': the destructor: Python
    never removes a C++ QQuickImageCapture.

  What has no ritual
  ------------------

  5 of the 12 functions Qt declares: 2 not a gap; 2 leans on
  'QQuickImageCapture; 1 the compiler refuses its ritual as it would be
  written here.

  What to expect
  --------------

  - The C++ QQuickImageCapture is created at the first use, not by
    'QQuickImageCapture(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickImageCapture.
  - Qt tells when it has removed the C++ QQuickImageCapture. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickImageCapture that has no cute function yet,
    '__init__', 'saveToFile', holds a function that raises
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
  __qt_class__ = 'QQuickImageCapture'

  #  A C++ QQuickImageCapture Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickImageCapture'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickImageCapture::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimagecapture.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickImageCapture::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickImageCapture10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def preview(self) -> str:
    """
    Calls Qt's 'QString QQuickImageCapture::preview() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimagecapture.html#preview

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickImageCapture::preview() const
    return self.uglySide.call('ritual_ZNK18QQuickImageCapture7previewEv')

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
    Qt's 'QQuickImageCapture::QQuickImageCapture(QObject *parent)': leans on
    'QQuickImageCapture::qt_metacall(QMetaObject::Call, int, void**)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQuickImageCapture.__init__' has no cute function yet. Qt's "
        "'QQuickImageCapture::QQuickImageCapture(QObject *parent)': leans "
        "on 'QQuickImageCapture::qt_metacall(QMetaObject::Call, int, "
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

  def previewChanged(self) -> None:
    """
    Calls Qt's 'void QQuickImageCapture::previewChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimagecapture.html#previewChanged
    """
    #  void QQuickImageCapture::previewChanged()
    self.uglySide.call('ritual_ZN18QQuickImageCapture14previewChangedEv')

  @overload(int, QImage)
  def _q_imageCaptured(self, a0: int, a1: QImage) -> None:
    """
    Calls Qt's 'void QQuickImageCapture::_q_imageCaptured(int a0, const
    QImage &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimagecapture.html#_q_imageCaptured

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void QQuickImageCapture::_q_imageCaptured(int a0, const QImage &a1)
    self.uglySide.call(
        'ritual_ZN18QQuickImageCapture16_q_imageCapturedEiRK6QImage',
        a0, self._valueOf(a1),
    )

  @staticmethod
  def saveToFile(*__, **_) -> Never:
    """
    Qt's 'void QQuickImageCapture::saveToFile(const QUrl &location) const':
    the compiler refuses its ritual as it would be written here: static_cast
    from 'const QQuickImageCapture *' to 'QObject *', which are not related
    by inheritance, is not allowed.
    """
    raise NotImplementedError(
        "'QQuickImageCapture.saveToFile' has no cute function yet. Qt's "
        "'void QQuickImageCapture::saveToFile(const QUrl &location) const': "
        "the compiler refuses its ritual as it would be written here: "
        "static_cast from 'const QQuickImageCapture *' to 'QObject *', "
        "which are not related by inheritance, is not allowed.")
