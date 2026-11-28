"""
QVideoFrameTextures binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qhwvideobuffer_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QVideoFrameTextures to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QRhiTexture
  from . import QVideoFrame
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVideoFrame = WAIT['QVideoFrame']


class QVideoFrameTextures(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QVideoFrameTextures: a plain Python object standing
  in front of one C++ QVideoFrameTextures.

  What exists
  -----------

  Every function of Qt's QVideoFrameTextures that has a ritual and that
  Python can call so far, 3 names in all: 'texture', 'onFrameEndInvoked',
  'setSourceFrame'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QVideoFrameTextures::~QVideoFrameTextures()': the destructor:
    Python never removes a C++ QVideoFrameTextures.
  - Qt's 'QVideoFrameTexturesHandlesUPtr QVideoFrameTextures::takeHandles()':
    gives a type Python has no way to take yet.

  What to expect
  --------------

  - The C++ QVideoFrameTextures is created at the first use, not by
    'QVideoFrameTextures(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QVideoFrameTextures.
  - Each name of Qt's QVideoFrameTextures that has no cute function yet,
    'takeHandles', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QVideoFrameTextures'

  #  A C++ QVideoFrameTextures Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QVideoFrameTextures'

  #  The functions Qt calls itself that QVideoFrameTextures is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'takeHandles': (
          'QVideoFrameTexturesHandlesUPtr '
          'QVideoFrameTextures::takeHandles()',
      ),
  }

  #  The functions Qt calls itself that QVideoFrameTextures is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'texture': (
          ('_ZNK19QVideoFrameTextures7textureEj',
           ('address', 'address', 'QtGui:QRhiTexture'),
           (
               ('unsigned int', 'number', ''),
           )),
      ),
      'onFrameEndInvoked': (
          ('_ZN19QVideoFrameTextures17onFrameEndInvokedEv',
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

  @overload(int)
  def texture(self, plane: int) -> Optional[QRhiTexture]:
    """
    Calls Qt's 'QRhiTexture *QVideoFrameTextures::texture(uint plane) const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframetextures.html#texture

    Parameters
    ----------

    plane : int
      Passed on as it is.

    Returns
    -------

    Optional[QRhiTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTexture *QVideoFrameTextures::texture(uint plane) const
    address = self.uglySide.call(
        'ritual_ZNK19QVideoFrameTextures7textureEj', plane,
    )
    from ..QtGui import QRhiTexture
    return QRhiTexture._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVideoFrame)
  def setSourceFrame(self, sourceFrame: QVideoFrame) -> None:
    """
    Calls Qt's 'void QVideoFrameTextures::setSourceFrame(QVideoFrame
    sourceFrame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideoframetextures.html#setSourceFrame

    Parameters
    ----------

    sourceFrame : QVideoFrame
      Passed on as a value: Qt reads the C++ QVideoFrame, which stays
      Python's own.
    """
    #  void QVideoFrameTextures::setSourceFrame(QVideoFrame sourceFrame)
    self.uglySide.call(
        'ritual_ZN19QVideoFrameTextures14setSourceFrameE11QVideoFrame',
        self._valueOf(sourceFrame),
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

  def onFrameEndInvoked(self) -> None:
    """
    Calls Qt's 'void QVideoFrameTextures::onFrameEndInvoked()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideoframetextures.html#onFrameEndInvoked
    """
    #  void QVideoFrameTextures::onFrameEndInvoked()
    ritual = 'ritual_ZN19QVideoFrameTextures17onFrameEndInvokedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QVideoFrameTextures17onFrameEndInvokedEv'
    self.uglySide.call(ritual)

  @staticmethod
  def takeHandles(*__, **_) -> Never:
    """
    Qt's 'QVideoFrameTexturesHandlesUPtr QVideoFrameTextures::takeHandles()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QVideoFrameTextures.takeHandles' has no cute function yet. Qt's "
        "'QVideoFrameTexturesHandlesUPtr "
        "QVideoFrameTextures::takeHandles()': gives a type Python has no "
        "way to take yet.")
