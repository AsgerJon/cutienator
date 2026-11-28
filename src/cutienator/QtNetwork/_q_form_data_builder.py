"""
QFormDataBuilder binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qformdatabuilder.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QFormDataPartBuilder


class QFormDataBuilder(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QFormDataBuilder: a plain Python object standing in
  front of one C++ QFormDataBuilder.

  What exists
  -----------

  Every function of Qt's QFormDataBuilder that has a ritual and that Python
  can call so far, 1 name in all: 'part'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFormDataBuilder::QFormDataBuilder(QFormDataBuilder &&other)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QFormDataBuilder &QFormDataBuilder::operator=(QFormDataBuilder
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'void QFormDataBuilder::swap(QFormDataBuilder &other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QFormDataBuilder::~QFormDataBuilder()': the destructor: Python
    never removes a C++ QFormDataBuilder.
  - Qt's 'std::unique_ptr<QHttpMultiPart>
    QFormDataBuilder::buildMultiPart(Options options)': gives a type Python
    has no way to take yet.
  - Qt's 'QFormDataBuilderPrivate *QFormDataBuilder::d_func()': gives
    'QFormDataBuilderPrivate', which has no cute class yet.
  - Qt's 'const QFormDataBuilderPrivate *QFormDataBuilder::d_func() const':
    gives 'QFormDataBuilderPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QFormDataBuilder is created at the first use, not by
    'QFormDataBuilder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QFormDataBuilder.
  - Each name of Qt's QFormDataBuilder that has no cute function yet,
    'buildMultiPart', 'd_func', 'swap', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QFormDataBuilder, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Option(CuteFlags, scoped=True):
    """
    The flags enum 'QFormDataBuilder::Option' of Qt, with the 5 names Qt
    gives in it. Qt names the type of its combinations
    'QFormDataBuilder::Options'. C++ keeps these names inside the enum, so
    the class that holds the enum does not have them.
    """

    Default = 0x0
    OmitRfc8187EncodedFilename = 0x1
    UseRfc7578PercentEncodedFilename = 0x2
    PreferLatin1EncodedFilename = 0x4
    StrictRfc7578 = 0x3

  Options = Option

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFormDataBuilder'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QFormDataBuilder::QFormDataBuilder()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qformdatabuilder.html#QFormDataBuilder
    """
    #  QFormDataBuilder::QFormDataBuilder()
    self._noteCreation(QFormDataBuilder, lambda: Rituals.call(
        'ritual_ZN16QFormDataBuilderC1Ev',
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

  @overload(str)
  def part(self, name: str) -> QFormDataPartBuilder:
    """
    Calls Qt's 'QFormDataPartBuilder QFormDataBuilder::part(QAnyStringView
    name)'.

    Qt's own words: https://doc.qt.io/qt-6/qformdatabuilder.html#part

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QFormDataPartBuilder
      A new cute QFormDataPartBuilder around the copy Qt gave back. Python
      owns it.
    """
    #  QFormDataPartBuilder QFormDataBuilder::part(QAnyStringView name)
    address = self.uglySide.call(
        'ritual_ZN16QFormDataBuilder4partE14QAnyStringView', name,
    )
    from . import QFormDataPartBuilder
    return QFormDataPartBuilder._cuteOwning(address)

  @staticmethod
  def buildMultiPart(*__, **_) -> Never:
    """
    Qt's 'std::unique_ptr<QHttpMultiPart>
    QFormDataBuilder::buildMultiPart(Options options)': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QFormDataBuilder.buildMultiPart' has no cute function yet. Qt's "
        "'std::unique_ptr<QHttpMultiPart> "
        "QFormDataBuilder::buildMultiPart(Options options)': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'QFormDataBuilderPrivate *QFormDataBuilder::d_func()': gives
      'QFormDataBuilderPrivate', which has no cute class yet.
    - Qt's 'const QFormDataBuilderPrivate *QFormDataBuilder::d_func() const':
      gives 'QFormDataBuilderPrivate', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QFormDataBuilder.d_func' has no cute function yet. Qt's "
        "'QFormDataBuilderPrivate *QFormDataBuilder::d_func()': gives "
        "'QFormDataBuilderPrivate', which has no cute class yet. Qt's "
        "'const QFormDataBuilderPrivate *QFormDataBuilder::d_func() const': "
        "gives 'QFormDataBuilderPrivate', which has no cute class yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QFormDataBuilder::swap(QFormDataBuilder &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QFormDataBuilder.swap' has no cute function yet. Qt's 'void "
        "QFormDataBuilder::swap(QFormDataBuilder &other)': takes a type "
        "Python has no way to hand over yet.")
