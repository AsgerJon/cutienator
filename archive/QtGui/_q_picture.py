"""
QPicture binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qpicture.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QPaintDevice

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QIODevice, QRect
  from . import QPaintEngine, QPainter
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QIODevice = WAIT['QIODevice']
  QPainter = WAIT['QPainter']
  QRect = WAIT['QRect']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPicture(QPaintDevice):
  """
  The cute side of Qt's QPicture: a plain Python object standing in front of
  one C++ QPicture.

  It is built on the cute 'QPaintDevice', as Qt's QPicture is built on Qt's
  QPaintDevice, and has everything that class has.

  C++ hands a QPicture around as a copy, so every C++ QPicture behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPicture that has a ritual and that Python can call
  so far, 14 names in all: 'isNull', 'devType', 'size', 'data', 'setData',
  'play', 'load', 'save', 'boundingRect', 'setBoundingRect', 'detach',
  'isDetached', 'paintEngine', 'metric'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPicture::~QPicture()': the destructor: Python removes its C++
    QPicture by it, and has no other use for it.

  What has no ritual
  ------------------

  10 of the 29 functions Qt declares: 10 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QPicture is created at the first use, not by 'QPicture(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPicture back gives a copy the ritual made for
    Python, in a new cute QPicture.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPicture'

  #  A C++ QPicture Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPicture'

  #  The functions Qt calls itself that QPicture is the first to declare and
  #  that cannot be handed to Python yet, each as Qt declares it. A class of
  #  a program that writes one of them anew is refused, since Qt would never
  #  call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'setData': (
          'void QPicture::setData(const char *, uint)',
      ),
  }

  #  Qt's '~QPicture()'. Naming it makes this a value class: Python owns
  #  every C++ QPicture behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN8QPictureD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QPicture::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpicture.html#isNull
    """
    #  bool QPicture::isNull() const
    return self.uglySide.call('ritual_ZNK8QPicture6isNullEv')

  def devType(self) -> int:
    """
    Calls Qt's 'int QPicture::devType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpicture.html#devType
    """
    #  int QPicture::devType() const
    ritual = 'ritual_ZNK8QPicture7devTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK8QPicture7devTypeEv'
    return self.uglySide.call(ritual)

  def size(self) -> int:
    """
    Calls Qt's 'uint QPicture::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpicture.html#size
    """
    #  uint QPicture::size() const
    return self.uglySide.call('ritual_ZNK8QPicture4sizeEv')

  def data(self) -> Optional[str]:
    """
    Calls Qt's 'const char *QPicture::data() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpicture.html#data

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QPicture::data() const
    chars = self.uglySide.call('ritual_ZNK8QPicture4dataEv')
    return None if chars is None else chars.decode()

  def boundingRect(self) -> QRect:
    """
    Calls Qt's 'QRect QPicture::boundingRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpicture.html#boundingRect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QPicture::boundingRect() const
    address = self.uglySide.call('ritual_ZNK8QPicture12boundingRectEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def isDetached(self) -> bool:
    """
    Calls Qt's 'bool QPicture::isDetached() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpicture.html#isDetached
    """
    #  bool QPicture::isDetached() const
    return self.uglySide.call('ritual_ZNK8QPicture10isDetachedEv')

  def paintEngine(self) -> Optional[QPaintEngine]:
    """
    Calls Qt's 'QPaintEngine *QPicture::paintEngine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpicture.html#paintEngine

    Returns
    -------

    Optional[QPaintEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPaintEngine *QPicture::paintEngine() const
    ritual = 'ritual_ZNK8QPicture11paintEngineEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK8QPicture11paintEngineEv'
    address = self.uglySide.call(ritual)
    from . import QPaintEngine
    return QPaintEngine._cuteAt(address)

  @overload(QPaintDevice.PaintDeviceMetric)
  def metric(self, m: QPaintDevice.PaintDeviceMetric) -> int:
    """
    Calls Qt's 'int QPicture::metric(PaintDeviceMetric m) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpicture.html#metric

    Parameters
    ----------

    m : QPaintDevice.PaintDeviceMetric
      Passed on as its number.
    """
    #  int QPicture::metric(PaintDeviceMetric m) const
    ritual = 'ritual_ZNK8QPicture6metricEN12QPaintDevice17PaintDeviceMetricE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK8QPicture6metricEN12QPaintDevice17PaintDeviceMetri'
          'cE')
    return self.uglySide.call(ritual, m.value)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str, int)
  @overload(NoneType, int)
  def setData(self, data: Optional[str], size: int) -> None:
    """
    Calls Qt's 'void QPicture::setData(const char *data, uint size)'.

    Qt's own words: https://doc.qt.io/qt-6/qpicture.html#setData

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    size : int
      Passed on as it is.
    """
    #  void QPicture::setData(const char *data, uint size)
    self.uglySide.call(
        'ritual_ZN8QPicture7setDataEPKcj', self._bytesOf(data), size,
    )

  @overload(QRect)
  def setBoundingRect(self, r: QRect) -> None:
    """
    Calls Qt's 'void QPicture::setBoundingRect(const QRect &r)'.

    Qt's own words: https://doc.qt.io/qt-6/qpicture.html#setBoundingRect

    Parameters
    ----------

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QPicture::setBoundingRect(const QRect &r)
    self.uglySide.call(
        'ritual_ZN8QPicture15setBoundingRectERK5QRect', self._valueOf(r),
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

  @overload()
  @overload(int)
  def __init__(self, formatVersion: int = -1) -> None:
    """
    Notes what was given, for Qt's 'QPicture::QPicture(int formatVersion)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpicture.html#QPicture

    Parameters
    ----------

    formatVersion : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  QPicture::QPicture(int formatVersion)
    self._noteCreation(QPicture, lambda: Rituals.call(
        'ritual_ZN8QPictureC1Ei', formatVersion,
    ))

  @overload(THIS)
  def __init__(self, a0: QPicture) -> None:
    """
    Notes what was given, for Qt's 'QPicture::QPicture(const QPicture &a0)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpicture.html#QPicture

    Parameters
    ----------

    a0 : QPicture
      Passed on as a value: Qt reads the C++ QPicture, which stays Python's
      own.
    """
    #  QPicture::QPicture(const QPicture &a0)
    self._noteCreation(QPicture, lambda: Rituals.call(
        'ritual_ZN8QPictureC1ERKS_', self._valueOf(a0),
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

  @overload(QPainter)
  @overload(NoneType)
  def play(self, p: Optional[QPainter]) -> bool:
    """
    Calls Qt's 'bool QPicture::play(QPainter *p)'.

    Qt's own words: https://doc.qt.io/qt-6/qpicture.html#play

    Parameters
    ----------

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPicture::play(QPainter *p)
    return self.uglySide.call(
        'ritual_ZN8QPicture4playEP8QPainter', self._addressOf(p),
    )

  @overload(QIODevice)
  @overload(NoneType)
  def load(self, dev: Optional[QIODevice]) -> bool:
    """
    Calls Qt's 'bool QPicture::load(QIODevice *dev)'.

    Qt's own words: https://doc.qt.io/qt-6/qpicture.html#load

    Parameters
    ----------

    dev : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPicture::load(QIODevice *dev)
    return self.uglySide.call(
        'ritual_ZN8QPicture4loadEP9QIODevice', self._addressOf(dev),
    )

  @overload(str)
  def load(self, fileName: str) -> bool:
    """
    Calls Qt's 'bool QPicture::load(const QString &fileName)'.

    Qt's own words: https://doc.qt.io/qt-6/qpicture.html#load

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QPicture::load(const QString &fileName)
    return self.uglySide.call('ritual_ZN8QPicture4loadERK7QString', fileName)

  @overload(QIODevice)
  @overload(NoneType)
  def save(self, dev: Optional[QIODevice]) -> bool:
    """
    Calls Qt's 'bool QPicture::save(QIODevice *dev)'.

    Qt's own words: https://doc.qt.io/qt-6/qpicture.html#save

    Parameters
    ----------

    dev : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPicture::save(QIODevice *dev)
    return self.uglySide.call(
        'ritual_ZN8QPicture4saveEP9QIODevice', self._addressOf(dev),
    )

  @overload(str)
  def save(self, fileName: str) -> bool:
    """
    Calls Qt's 'bool QPicture::save(const QString &fileName)'.

    Qt's own words: https://doc.qt.io/qt-6/qpicture.html#save

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QPicture::save(const QString &fileName)
    return self.uglySide.call('ritual_ZN8QPicture4saveERK7QString', fileName)

  def detach(self) -> None:
    """
    Calls Qt's 'void QPicture::detach()'.

    Qt's own words: https://doc.qt.io/qt-6/qpicture.html#detach
    """
    #  void QPicture::detach()
    self.uglySide.call('ritual_ZN8QPicture6detachEv')
