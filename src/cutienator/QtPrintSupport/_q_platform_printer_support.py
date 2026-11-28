"""
QPlatformPrinterSupport binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPrintSupport/6.12.0/QtPrintSupport/qpa/qplatformprintersupport.h, Qt
#  6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QStringList
from . import QPrinter

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QSize
  from ..QtGui import QPageSize, QPaintEngine
  from . import QPrintEngine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPrintEngine = WAIT['QPrintEngine']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlatformPrinterSupport(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPlatformPrinterSupport: a plain Python object
  standing in front of one C++ QPlatformPrinterSupport.

  C++ hands a QPlatformPrinterSupport around as a copy, so every C++
  QPlatformPrinterSupport behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPlatformPrinterSupport that has a ritual and that
  Python can call so far, 5 names in all: 'createNativePrintEngine',
  'createPaintEngine', 'availablePrintDeviceIds', 'defaultPrintDeviceId',
  'createPageSize'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlatformPrinterSupport::~QPlatformPrinterSupport()': the
    destructor: Python removes its C++ QPlatformPrinterSupport by it, and has
    no other use for it.

  What has no ritual
  ------------------

  2 of the 9 functions Qt declares: 2 the compiler refuses its ritual as it
  would be written here.

  What to expect
  --------------

  - The C++ QPlatformPrinterSupport is created at the first use, not by
    'QPlatformPrinterSupport(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPlatformPrinterSupport back gives a copy the ritual
    made for Python, in a new cute QPlatformPrinterSupport.
  - Each name of Qt's QPlatformPrinterSupport that has no cute function yet,
    'createPrintDevice', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str, QSize, str)
  def createPageSize(id: str, size: QSize, localizedName: str) -> QPageSize:
    """
    Calls Qt's 'QPageSize QPlatformPrinterSupport::createPageSize(const
    QString &id, QSize size, const QString &localizedName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformprintersupport.html#createPageSize

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    localizedName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QPageSize
      A new cute QPageSize around the copy Qt gave back. Python owns it.
    """
    #  QPageSize QPlatformPrinterSupport::createPageSize(const QString &id,
    #      QSize size, const QString &localizedName)
    address = Rituals.call(
        'ritual_ZN23QPlatformPrinterSupport14createPageSizeERK7QString5QSiz'
        'eS2_',
        id, CuteMixin._valueOf(size), localizedName,
    )
    from ..QtGui import QPageSize
    return QPageSize._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformPrinterSupport'

  #  A C++ QPlatformPrinterSupport Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlatformPrinterSupport'

  #  The functions Qt calls itself that QPlatformPrinterSupport is the first
  #  to declare and that cannot be handed to Python yet, each as Qt declares
  #  it. A class of a program that writes one of them anew is refused, since
  #  Qt would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'createPrintDevice': (
          'QPrintDevice QPlatformPrinterSupport::createPrintDevice(const '
          'QString &)',
      ),
      'availablePrintDeviceIds': (
          'QStringList QPlatformPrinterSupport::availablePrintDeviceIds() '
          'const',
      ),
  }

  #  The functions Qt calls itself that QPlatformPrinterSupport is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'createNativePrintEngine': (
          ('_ZN23QPlatformPrinterSupport23createNativePrintEngineEN8QPrinte'
           'r11PrinterModeERK7QString',
           ('address', 'address', 'QtPrintSupport:QPrintEngine'),
           (
               ('int', 'enum', 'QtPrintSupport:QPrinter.PrinterMode'),
               ('address', 'text', ''),
           )),
      ),
      'createPaintEngine': (
          ('_ZN23QPlatformPrinterSupport17createPaintEngineEP12QPrintEngine'
           'N8QPrinter11PrinterModeE',
           ('address', 'address', 'QtGui:QPaintEngine'),
           (
               ('address', 'address', 'QtPrintSupport:QPrintEngine'),
               ('int', 'enum', 'QtPrintSupport:QPrinter.PrinterMode'),
           )),
      ),
      'defaultPrintDeviceId': (
          ('_ZNK23QPlatformPrinterSupport20defaultPrintDeviceIdEv',
           ('address', 'text', ''),
           ()),
      ),
  }

  #  Qt's '~QPlatformPrinterSupport()'. Naming it makes this a value class:
  #  Python owns every C++ QPlatformPrinterSupport behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QPlatformPrinterSupportD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def availablePrintDeviceIds(self) -> QStringList:
    """
    Calls Qt's 'QStringList
    QPlatformPrinterSupport::availablePrintDeviceIds() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformprintersupport.html

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QPlatformPrinterSupport::availablePrintDeviceIds() const
    address = self.uglySide.call(
        'ritual_ZNK23QPlatformPrinterSupport23availablePrintDeviceIdsEv',
    )
    return QStringList._cuteOwning(address)

  def defaultPrintDeviceId(self) -> str:
    """
    Calls Qt's 'QString QPlatformPrinterSupport::defaultPrintDeviceId()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformprintersupport.html#defaultPrintDeviceId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlatformPrinterSupport::defaultPrintDeviceId() const
    ritual = 'ritual_ZNK23QPlatformPrinterSupport20defaultPrintDeviceIdEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK23QPlatformPrinterSupport20defaultPrintDeviceIdEv')
    return self.uglySide.call(ritual)

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
    'QPlatformPrinterSupport::QPlatformPrinterSupport()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformprintersupport.html
    """
    #  QPlatformPrinterSupport::QPlatformPrinterSupport()
    self._noteCreation(QPlatformPrinterSupport, lambda: Rituals.call(
        'ritual_ZN23QPlatformPrinterSupportC1Ev',
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

  @overload(QPrinter.PrinterMode)
  @overload(QPrinter.PrinterMode, str)
  def createNativePrintEngine(
      self,
      printerMode: QPrinter.PrinterMode,
      deviceId: str = '',
  ) -> Optional[QPrintEngine]:
    """
    Calls Qt's 'QPrintEngine
    *QPlatformPrinterSupport::createNativePrintEngine(QPrinter::PrinterMode
    printerMode, const QString &deviceId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformprintersupport.html

    Parameters
    ----------

    printerMode : QPrinter.PrinterMode
      Passed on as its number.

    deviceId : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    Optional[QPrintEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPrintEngine
    #      *QPlatformPrinterSupport::createNativePrintEngine(QPrinter::
    #      PrinterMode printerMode, const QString &deviceId)
    ritual = (
        'ritual_ZN23QPlatformPrinterSupport23createNativePrintEngineEN8QPri'
        'nter11PrinterModeERK7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QPlatformPrinterSupport23createNativePrintEngineE'
          'N8QPrinter11PrinterModeERK7QString')
    address = self.uglySide.call(ritual, printerMode.value, deviceId)
    from . import QPrintEngine
    return QPrintEngine._cuteAt(address)

  @overload(QPrintEngine, QPrinter.PrinterMode)
  @overload(NoneType, QPrinter.PrinterMode)
  def createPaintEngine(
      self,
      a0: Optional[QPrintEngine],
      printerMode: QPrinter.PrinterMode,
  ) -> Optional[QPaintEngine]:
    """
    Calls Qt's 'QPaintEngine
    *QPlatformPrinterSupport::createPaintEngine(QPrintEngine *a0,
    QPrinter::PrinterMode printerMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformprintersupport.html#createPaintEngine

    Parameters
    ----------

    a0 : Optional[QPrintEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    printerMode : QPrinter.PrinterMode
      Passed on as its number.

    Returns
    -------

    Optional[QPaintEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPaintEngine *QPlatformPrinterSupport::createPaintEngine(QPrintEngine
    #      *a0, QPrinter::PrinterMode printerMode)
    ritual = (
        'ritual_ZN23QPlatformPrinterSupport17createPaintEngineEP12QPrintEng'
        'ineN8QPrinter11PrinterModeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QPlatformPrinterSupport17createPaintEngineEP12QPr'
          'intEngineN8QPrinter11PrinterModeE')
    address = self.uglySide.call(
        ritual, self._addressOf(a0, 'QPrintEngine'), printerMode.value,
    )
    from ..QtGui import QPaintEngine
    return QPaintEngine._cuteAt(address)

  @staticmethod
  def createPrintDevice(*__, **_) -> Never:
    """
    - Qt's 'QPrintDevice QPlatformPrinterSupport::createPrintDevice(const
      QString &id)': the compiler refuses its ritual as it would be written
      here: calling 'createPrintDevice' with incomplete return type
      'QPrintDevice'.
    - Qt's 'QPrintDevice
      QPlatformPrinterSupport::createPrintDevice(QPlatformPrintDevice
      *device)': the compiler refuses its ritual as it would be written here:
      allocation of incomplete type 'QPrintDevice'.
    """
    raise NotImplementedError(
        "'QPlatformPrinterSupport.createPrintDevice' has no cute function "
        "yet. Qt's 'QPrintDevice "
        "QPlatformPrinterSupport::createPrintDevice(const QString &id)': "
        "the compiler refuses its ritual as it would be written here: "
        "calling 'createPrintDevice' with incomplete return type "
        "'QPrintDevice'. Qt's 'QPrintDevice "
        "QPlatformPrinterSupport::createPrintDevice(QPlatformPrintDevice "
        "*device)': the compiler refuses its ritual as it would be written "
        "here: allocation of incomplete type 'QPrintDevice'.")
