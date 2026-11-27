"""
UnsupportedMeta makes the classes that stand in a cute class for a
class of Qt that has no cute class yet.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class UnsupportedMeta(type):
  """
  The metaclass of a class that stands in a cute class for a class of
  Qt that has none yet, as 'Q3DBarsWidgetItemPrivate' of
  QtGraphsWidgets. It lies where the cute class would, in the package
  of its part, so a program finds it by the name C++ has. Its docstring
  names the class of Qt and says why it has no cute class:

    class Q3DBarsWidgetItemPrivate(metaclass=UnsupportedMeta):
      \"\"\"
      Qt's class 'Q3DBarsWidgetItemPrivate' of QtGraphsWidgets: the
      dev tooling cannot write its ritual file yet, for ...
      \"\"\"

    Q3DBarsWidgetItemPrivate()       # NotImplementedError
    Q3DBarsWidgetItemPrivate.oops    # NotImplementedError

  You never use it by name: the dev tooling writes such a class into
  the file the cute class would have. A function of Qt that is missing
  from a cute class gets a stub of its own instead, raising
  NotImplementedError as well. A class of Qt that gets its cute class
  later loses its stand-in when the dev tooling writes it.

  What to expect
  --------------

  - Calling the class, as to make an object of it, raises
    'NotImplementedError'. No object of it is ever made.
  - Reading an attribute the class does not have raises
    'NotImplementedError' as well, saying what the class stands for.
  - A name with two underscores before and after it, as '__wrapped__',
    is refused with 'AttributeError', as any class refuses a name it
    lacks. Python and its tools ask for such names with 'hasattr',
    which lets only that error pass.
  - The message is the docstring. Under 'python -OO', which drops
    docstrings, it names the class alone.
  - A stand-in with a '__qt_class__' of its own is noted as the class of
    that name, as a cute class is: a 'WAIT' for it holds the stand-in,
    and what takes or gives one raises when it is used.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getInfo(cls) -> str:
    """Gives the docstring of the class on one line: the class of Qt it
    stands for, and why that has no cute class."""
    return ' '.join((cls.__doc__ or '').split())

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def __init__(cls, name: str, bases: tuple, space: dict, **kw) -> None:
    """
    Finishes the class, and notes a stand-in with a '__qt_class__' of
    its own as the class of that name, as 'MetaCute' notes a cute
    class; see 'MetaCute.noteStandIn'. A 'WAIT' for it then holds the
    stand-in.
    """
    super().__init__(name, bases, space, **kw)
    if '__qt_class__' in space:
      #  Brought in here: 'MetaCute' is made after this metaclass.
      from ._meta_cute import MetaCute
      MetaCute.noteStandIn(cls)

  def __call__(cls, *__, **_) -> Never:
    """
    Refuses the call, which would make an object of the class.

    Raises
    ------

    NotImplementedError
      Always, naming the class of Qt and why it has no cute class.
    """
    infoSpec = """'%s' cannot be called: it stands for a class of Qt that
    has no cute class yet. %s"""
    info = infoSpec % (cls.__qualname__, cls.getInfo())
    raise NotImplementedError(' '.join(info.split()))

  def __getattr__(cls, key: str) -> Never:
    """
    Refuses an attribute the class does not have. Python asks this only
    after the class and its metaclass have nothing at the name.

    Raises
    ------

    AttributeError
      The name has two underscores before and after it.

    NotImplementedError
      Any other name, naming the class of Qt and why it has no cute
      class.
    """
    if key.startswith('__') and key.endswith('__'):
      infoSpec = """type object '%s' has no attribute '%s'"""
      raise AttributeError(infoSpec % (cls.__qualname__, key))
    infoSpec = """'%s' has no attribute '%s': it stands for a class of
    Qt that has no cute class yet. %s"""
    info = infoSpec % (cls.__qualname__, key, cls.getInfo())
    raise NotImplementedError(' '.join(info.split()))
