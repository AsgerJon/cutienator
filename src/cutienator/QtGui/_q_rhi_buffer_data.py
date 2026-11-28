"""
QRhiBufferData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qrhi_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QRhiBufferData to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRhiBufferData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRhiBufferData: a plain Python object standing in
  front of one C++ QRhiBufferData.

  C++ hands a QRhiBufferData around as a copy, so every C++ QRhiBufferData
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QRhiBufferData that has a ritual and that Python can
  call so far, 4 names in all: 'constData', 'size', 'largeAlloc', 'assign'.
  It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRhiBufferData::~QRhiBufferData()': the destructor: Python removes
    its C++ QRhiBufferData by it, and has no other use for it.
  - Qt's 'QRhiBufferData &QRhiBufferData::operator=(const QRhiBufferData
    &other)': assignment: Python binds a name and has no operator for it.

  What to expect
  --------------

  - The C++ QRhiBufferData is created at the first use, not by
    'QRhiBufferData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QRhiBufferData back gives a copy the ritual made for
    Python, in a new cute QRhiBufferData.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRhiBufferData'

  #  Qt's '~QRhiBufferData()'. Naming it makes this a value class: Python
  #  owns every C++ QRhiBufferData behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QRhiBufferDataD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def constData(self) -> Optional[str]:
    """
    Calls Qt's 'const char *QRhiBufferData::constData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhibufferdata.html#constData

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QRhiBufferData::constData() const
    chars = self.uglySide.call('ritual_ZNK14QRhiBufferData9constDataEv')
    return None if chars is None else chars.decode()

  def size(self) -> int:
    """
    Calls Qt's 'quint32 QRhiBufferData::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhibufferdata.html#size
    """
    #  quint32 QRhiBufferData::size() const
    return self.uglySide.call('ritual_ZNK14QRhiBufferData4sizeEv')

  def largeAlloc(self) -> int:
    """
    Calls Qt's 'quint32 QRhiBufferData::largeAlloc() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhibufferdata.html#largeAlloc
    """
    #  quint32 QRhiBufferData::largeAlloc() const
    return self.uglySide.call('ritual_ZNK14QRhiBufferData10largeAllocEv')

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QRhiBufferData::QRhiBufferData()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qrhibufferdata.html#QRhiBufferData
    """
    #  QRhiBufferData::QRhiBufferData()
    self._noteCreation(QRhiBufferData, lambda: Rituals.call(
        'ritual_ZN14QRhiBufferDataC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QRhiBufferData) -> None:
    """
    Notes what was given, for Qt's 'QRhiBufferData::QRhiBufferData(const
    QRhiBufferData &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qrhibufferdata.html#QRhiBufferData

    Parameters
    ----------

    other : QRhiBufferData
      Passed on as a value: Qt reads the C++ QRhiBufferData, which stays
      Python's own.
    """
    #  QRhiBufferData::QRhiBufferData(const QRhiBufferData &other)
    self._noteCreation(QRhiBufferData, lambda: Rituals.call(
        'ritual_ZN14QRhiBufferDataC1ERKS_', self._valueOf(other),
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

  @overload(str, int)
  @overload(NoneType, int)
  def assign(self, s: Optional[str], size: int) -> None:
    """
    Calls Qt's 'void QRhiBufferData::assign(const char *s, quint32 size)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhibufferdata.html#assign

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    size : int
      Passed on as it is.
    """
    #  void QRhiBufferData::assign(const char *s, quint32 size)
    self.uglySide.call(
        'ritual_ZN14QRhiBufferData6assignEPKcj', self._bytesOf(s), size,
    )

  @overload(QByteArray)
  def assign(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void QRhiBufferData::assign(QByteArray data)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhibufferdata.html#assign

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QRhiBufferData::assign(QByteArray data)
    self.uglySide.call(
        'ritual_ZN14QRhiBufferData6assignE10QByteArray', self._valueOf(data),
    )
