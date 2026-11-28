"""
QPrinterPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPrintSupport/6.12.0/QtPrintSupport/private/qprinter_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QPrinterPrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QPrintEngine, QPrinter

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QVariant
  from . import QPrinterInfo
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPrinterInfo = WAIT['QPrinterInfo']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPrinterPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPrinterPrivate: a plain Python object standing in
  front of one C++ QPrinterPrivate.

  C++ hands a QPrinterPrivate around as a copy, so every C++ QPrinterPrivate
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPrinterPrivate that has a ritual and that Python
  can call so far, 9 names in all: 'q_func', 'get', 'init',
  'findValidPrinter', 'initEngines', 'changeEngines', 'setPreviewMode',
  'previewMode', 'setProperty'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QPrinter *QPrinterPrivate::q_func() const': takes in Python
    what 'QPrinter *QPrinterPrivate::q_func()' takes.
  - Qt's 'QPrinterPrivate::~QPrinterPrivate()': the destructor: Python
    removes its C++ QPrinterPrivate by it, and has no other use for it.
  - Qt's 'QList<const QPicture *> QPrinterPrivate::previewPages() const':
    gives a type Python has no way to take yet.

  What to expect
  --------------

  - The C++ QPrinterPrivate is created at the first use, not by
    'QPrinterPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPrinterPrivate back gives a copy the ritual made for
    Python, in a new cute QPrinterPrivate.
  - Each name of Qt's QPrinterPrivate that has no cute function yet,
    'previewPages', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QPrinter)
  @overload(NoneType)
  def get(printer: Optional[QPrinter]) -> Optional[QPrinterPrivate]:
    """
    Calls Qt's 'QPrinterPrivate *QPrinterPrivate::get(QPrinter *printer)'.

    Qt's own words: https://doc.qt.io/qt-6/qprinterprivate.html#get

    Parameters
    ----------

    printer : Optional[QPrinter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QPrinterPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPrinterPrivate *QPrinterPrivate::get(QPrinter *printer)
    address = Rituals.call(
        'ritual_ZN15QPrinterPrivate3getEP8QPrinter',
        CuteMixin._addressOf(printer),
    )
    return QPrinterPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPrinterPrivate'

  #  Qt's '~QPrinterPrivate()'. Naming it makes this a value class: Python
  #  owns every C++ QPrinterPrivate behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QPrinterPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def previewMode(self) -> bool:
    """
    Calls Qt's 'bool QPrinterPrivate::previewMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprinterprivate.html#previewMode
    """
    #  bool QPrinterPrivate::previewMode() const
    return self.uglySide.call('ritual_ZNK15QPrinterPrivate11previewModeEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setPreviewMode(self, a0: bool) -> None:
    """
    Calls Qt's 'void QPrinterPrivate::setPreviewMode(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprinterprivate.html#setPreviewMode

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QPrinterPrivate::setPreviewMode(bool a0)
    self.uglySide.call('ritual_ZN15QPrinterPrivate14setPreviewModeEb', a0)

  @overload(QPrintEngine.PrintEnginePropertyKey, QVariant)
  def setProperty(
      self,
      key: QPrintEngine.PrintEnginePropertyKey,
      value: QVariant,
  ) -> None:
    """
    Calls Qt's 'void
    QPrinterPrivate::setProperty(QPrintEngine::PrintEnginePropertyKey key,
    const QVariant &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qprinterprivate.html#setProperty

    Parameters
    ----------

    key : QPrintEngine.PrintEnginePropertyKey
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QPrinterPrivate::setProperty(QPrintEngine::PrintEnginePropertyKey
    #      key, const QVariant &value)
    self.uglySide.call(
        'ritual_ZN15QPrinterPrivate11setPropertyEN12QPrintEngine22PrintEngi'
        'nePropertyKeyERK8QVariant',
        key.value, self._valueOf(value),
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

  @overload(QPrinter)
  @overload(NoneType)
  def __init__(self, printer: Optional[QPrinter]) -> None:
    """
    Notes what was given, for Qt's 'QPrinterPrivate::QPrinterPrivate(QPrinter
    *printer)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qprinterprivate.html#QPrinterPrivate

    Parameters
    ----------

    printer : Optional[QPrinter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QPrinterPrivate::QPrinterPrivate(QPrinter *printer)
    self._noteCreation(QPrinterPrivate, lambda: Rituals.call(
        'ritual_ZN15QPrinterPrivateC1EP8QPrinter', self._addressOf(printer),
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

  def q_func(self) -> Optional[QPrinter]:
    """
    Calls Qt's 'QPrinter *QPrinterPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qprinterprivate.html#q_func

    Returns
    -------

    Optional[QPrinter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPrinter *QPrinterPrivate::q_func()
    address = self.uglySide.call('ritual_ZN15QPrinterPrivate6q_funcEv')
    return QPrinter._cuteAt(address)

  @overload(QPrinterInfo, QPrinter.PrinterMode)
  def init(self, printer: QPrinterInfo, mode: QPrinter.PrinterMode) -> None:
    """
    Calls Qt's 'void QPrinterPrivate::init(const QPrinterInfo &printer,
    QPrinter::PrinterMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qprinterprivate.html#init

    Parameters
    ----------

    printer : QPrinterInfo
      Passed on as a value: Qt reads the C++ QPrinterInfo, which stays
      Python's own.

    mode : QPrinter.PrinterMode
      Passed on as its number.
    """
    #  void QPrinterPrivate::init(const QPrinterInfo &printer,
    #      QPrinter::PrinterMode mode)
    self.uglySide.call(
        'ritual_ZN15QPrinterPrivate4initERK12QPrinterInfoN8QPrinter11Printe'
        'rModeE',
        self._valueOf(printer), mode.value,
    )

  @overload()
  @overload(QPrinterInfo)
  def findValidPrinter(
      self,
      printer: Optional[QPrinterInfo] = None,
  ) -> QPrinterInfo:
    """
    Calls Qt's 'QPrinterInfo QPrinterPrivate::findValidPrinter(const
    QPrinterInfo &printer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprinterprivate.html#findValidPrinter

    Parameters
    ----------

    printer : Optional[QPrinterInfo]
      Passed on as a value: Qt reads the C++ QPrinterInfo, which stays
      Python's own. May be left out, as in Qt: a new 'QPrinterInfo()' is then
      passed on.

    Returns
    -------

    QPrinterInfo
      A new cute QPrinterInfo around the copy Qt gave back. Python owns it.
    """
    #  QPrinterInfo QPrinterPrivate::findValidPrinter(const QPrinterInfo
    #      &printer)
    if printer is None:
      from . import QPrinterInfo
      printer = QPrinterInfo()
    address = self.uglySide.call(
        'ritual_ZN15QPrinterPrivate16findValidPrinterERK12QPrinterInfo',
        self._valueOf(printer),
    )
    from . import QPrinterInfo
    return QPrinterInfo._cuteOwning(address)

  @overload(QPrinter.OutputFormat, QPrinterInfo)
  def initEngines(
      self,
      format: QPrinter.OutputFormat,
      printer: QPrinterInfo,
  ) -> None:
    """
    Calls Qt's 'void QPrinterPrivate::initEngines(QPrinter::OutputFormat
    format, const QPrinterInfo &printer)'.

    Qt's own words: https://doc.qt.io/qt-6/qprinterprivate.html#initEngines

    Parameters
    ----------

    format : QPrinter.OutputFormat
      Passed on as its number.

    printer : QPrinterInfo
      Passed on as a value: Qt reads the C++ QPrinterInfo, which stays
      Python's own.
    """
    #  void QPrinterPrivate::initEngines(QPrinter::OutputFormat format, const
    #      QPrinterInfo &printer)
    self.uglySide.call(
        'ritual_ZN15QPrinterPrivate11initEnginesEN8QPrinter12OutputFormatER'
        'K12QPrinterInfo',
        format.value, self._valueOf(printer),
    )

  @overload(QPrinter.OutputFormat, QPrinterInfo)
  def changeEngines(
      self,
      format: QPrinter.OutputFormat,
      printer: QPrinterInfo,
  ) -> None:
    """
    Calls Qt's 'void QPrinterPrivate::changeEngines(QPrinter::OutputFormat
    format, const QPrinterInfo &printer)'.

    Qt's own words: https://doc.qt.io/qt-6/qprinterprivate.html#changeEngines

    Parameters
    ----------

    format : QPrinter.OutputFormat
      Passed on as its number.

    printer : QPrinterInfo
      Passed on as a value: Qt reads the C++ QPrinterInfo, which stays
      Python's own.
    """
    #  void QPrinterPrivate::changeEngines(QPrinter::OutputFormat format,
    #      const QPrinterInfo &printer)
    self.uglySide.call(
        'ritual_ZN15QPrinterPrivate13changeEnginesEN8QPrinter12OutputFormat'
        'ERK12QPrinterInfo',
        format.value, self._valueOf(printer),
    )

  @staticmethod
  def previewPages(*__, **_) -> Never:
    """
    Qt's 'QList<const QPicture *> QPrinterPrivate::previewPages() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QPrinterPrivate.previewPages' has no cute function yet. Qt's "
        "'QList<const QPicture *> QPrinterPrivate::previewPages() const': "
        "gives a type Python has no way to take yet.")
