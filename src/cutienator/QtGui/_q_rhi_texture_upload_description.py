"""
QRhiTextureUploadDescription binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QRhiTextureUploadEntry
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhiTextureUploadEntry = WAIT['QRhiTextureUploadEntry']


class QRhiTextureUploadDescription(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRhiTextureUploadDescription: a plain Python object
  standing in front of one C++ QRhiTextureUploadDescription.

  C++ hands a QRhiTextureUploadDescription around as a copy, so every C++
  QRhiTextureUploadDescription behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QRhiTextureUploadDescription that has a ritual and
  that Python can call so far, 4 names in all: 'cbeginEntries',
  'cendEntries', 'entryAt', 'entryCount'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRhiTextureUploadDescription::QRhiTextureUploadDescription(std::
    initializer_list<QRhiTextureUploadEntry> list)': takes a type Python has
    no way to hand over yet.
  - Qt's 'void QRhiTextureUploadDescription::setEntries(std::
    initializer_list<QRhiTextureUploadEntry> list)': takes a type Python has
    no way to hand over yet.
  - Qt's 'QRhiTextureUploadDescription::~QRhiTextureUploadDescription()': the
    destructor: Python removes its C++ QRhiTextureUploadDescription by it,
    and has no other use for it.

  What has no ritual
  ------------------

  1 of the 10 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QRhiTextureUploadDescription is created at the first use, not by
    'QRhiTextureUploadDescription(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QRhiTextureUploadDescription back gives a copy the
    ritual made for Python, in a new cute QRhiTextureUploadDescription.
  - Each name of Qt's QRhiTextureUploadDescription that has no cute function
    yet, 'setEntries', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRhiTextureUploadDescription'

  #  Qt's '~QRhiTextureUploadDescription()'. Naming it makes this a value
  #  class: Python owns every C++ QRhiTextureUploadDescription behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN28QRhiTextureUploadDescriptionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def cbeginEntries(self) -> Optional[QRhiTextureUploadEntry]:
    """
    Calls Qt's 'const QRhiTextureUploadEntry
    *QRhiTextureUploadDescription::cbeginEntries() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitextureuploaddescription.html#cbeginEntries

    Returns
    -------

    Optional[QRhiTextureUploadEntry]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QRhiTextureUploadEntry
    #      *QRhiTextureUploadDescription::cbeginEntries() const
    address = self.uglySide.call(
        'ritual_ZNK28QRhiTextureUploadDescription13cbeginEntriesEv',
    )
    from . import QRhiTextureUploadEntry
    return QRhiTextureUploadEntry._cuteAt(address)

  def cendEntries(self) -> Optional[QRhiTextureUploadEntry]:
    """
    Calls Qt's 'const QRhiTextureUploadEntry
    *QRhiTextureUploadDescription::cendEntries() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitextureuploaddescription.html#cendEntries

    Returns
    -------

    Optional[QRhiTextureUploadEntry]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QRhiTextureUploadEntry
    #      *QRhiTextureUploadDescription::cendEntries() const
    address = self.uglySide.call(
        'ritual_ZNK28QRhiTextureUploadDescription11cendEntriesEv',
    )
    from . import QRhiTextureUploadEntry
    return QRhiTextureUploadEntry._cuteAt(address)

  @overload(int)
  def entryAt(self, index: int) -> Optional[QRhiTextureUploadEntry]:
    """
    Calls Qt's 'const QRhiTextureUploadEntry
    *QRhiTextureUploadDescription::entryAt(qsizetype index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitextureuploaddescription.html#entryAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QRhiTextureUploadEntry]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QRhiTextureUploadEntry
    #      *QRhiTextureUploadDescription::entryAt(qsizetype index) const
    address = self.uglySide.call(
        'ritual_ZNK28QRhiTextureUploadDescription7entryAtEx', index,
    )
    from . import QRhiTextureUploadEntry
    return QRhiTextureUploadEntry._cuteAt(address)

  def entryCount(self) -> int:
    """
    Calls Qt's 'qsizetype QRhiTextureUploadDescription::entryCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitextureuploaddescription.html#entryCount
    """
    #  qsizetype QRhiTextureUploadDescription::entryCount() const
    return self.uglySide.call(
        'ritual_ZNK28QRhiTextureUploadDescription10entryCountEv',
    )

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
    Notes what was given, for Qt's
    'QRhiTextureUploadDescription::QRhiTextureUploadDescription()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitextureuploaddescription.html
    """
    #  QRhiTextureUploadDescription::QRhiTextureUploadDescription()
    self._noteCreation(QRhiTextureUploadDescription, lambda: Rituals.call(
        'ritual_ZN28QRhiTextureUploadDescriptionC1Ev',
    ))

  @overload(QRhiTextureUploadEntry)
  def __init__(self, entry: QRhiTextureUploadEntry) -> None:
    """
    Notes what was given, for Qt's
    'QRhiTextureUploadDescription::QRhiTextureUploadDescription(const
    QRhiTextureUploadEntry &entry)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitextureuploaddescription.html

    Parameters
    ----------

    entry : QRhiTextureUploadEntry
      Passed on as a value: Qt reads the C++ QRhiTextureUploadEntry, which
      stays Python's own.
    """
    #  QRhiTextureUploadDescription::QRhiTextureUploadDescription(const
    #      QRhiTextureUploadEntry &entry)
    self._noteCreation(QRhiTextureUploadDescription, lambda: Rituals.call(
        'ritual_ZN28QRhiTextureUploadDescriptionC1ERK22QRhiTextureUploadEnt'
        'ry',
        self._valueOf(entry),
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

  @staticmethod
  def setEntries(*__, **_) -> Never:
    """
    - Qt's 'void QRhiTextureUploadDescription::setEntries(std::
      initializer_list<QRhiTextureUploadEntry> list)': takes a type Python
      has no way to hand over yet.
    - Qt's 'QRhiTextureUploadDescription::setEntries': a template: a pattern
      and no single function.
    """
    raise NotImplementedError(
        "'QRhiTextureUploadDescription.setEntries' has no cute function "
        "yet. Qt's 'void "
        "QRhiTextureUploadDescription::setEntries(std::initializer_list<QRhi"
        "TextureUploadEntry> list)': takes a type Python has no way to hand "
        "over yet. Qt's 'QRhiTextureUploadDescription::setEntries': a "
        "template: a pattern and no single function.")
