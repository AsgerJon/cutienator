"""
QtMultimediaPrivate::QTlsfMemoryResource binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qmemory_resource_tlsf_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QtMultimediaPrivate::QTlsfMemoryResource to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QTlsfMemoryResource(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtMultimediaPrivate::QTlsfMemoryResource: a plain
  Python object standing in front of one C++
  QtMultimediaPrivate::QTlsfMemoryResource.

  What exists
  -----------

  No function of Qt's QtMultimediaPrivate::QTlsfMemoryResource yet. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtMultimediaPrivate::QTlsfMemoryResource::QTlsfMemoryResource(std::
    size_t preallocatedBytes, pmr::memory_resource *upstream)': names
    'QtMultimediaPrivate::pmr::memory_resource', which has no cute class yet.
  - Qt's 'QtMultimediaPrivate::QTlsfMemoryResource::~QTlsfMemoryResource()':
    the destructor: Python never removes a C++
    QtMultimediaPrivate::QTlsfMemoryResource.

  What has no ritual
  ------------------

  7 of the 9 functions Qt declares: 4 forbidden; 2 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file; 1
  the compiler refuses its ritual as it would be written here.

  What to expect
  --------------

  - The C++ QtMultimediaPrivate::QTlsfMemoryResource is created at the first
    use, not by 'QtMultimediaPrivate::QTlsfMemoryResource(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtMultimediaPrivate::QTlsfMemoryResource.
  - Each name of Qt's QtMultimediaPrivate::QTlsfMemoryResource that has no
    cute function yet, '__init__', 'do_allocate', 'do_deallocate',
    'do_is_equal', holds a function that raises 'NotImplementedError', and
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
  __qt_class__ = 'QtMultimediaPrivate::QTlsfMemoryResource'

  #  The functions Qt calls itself that
  #  QtMultimediaPrivate::QTlsfMemoryResource is the first to declare and
  #  that cannot be handed to Python yet, each as Qt declares it. A class of
  #  a program that writes one of them anew is refused, since Qt would never
  #  call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'do_allocate': (
          'void '
          '*QtMultimediaPrivate::QTlsfMemoryResource::do_allocate(size_t, '
          'size_t)',
      ),
      'do_deallocate': (
          'void '
          'QtMultimediaPrivate::QTlsfMemoryResource::do_deallocate(void *, '
          'size_t, size_t)',
      ),
      'do_is_equal': (
          'bool '
          'QtMultimediaPrivate::QTlsfMemoryResource::do_is_equal(const '
          'memory_resource &) const noexcept',
      ),
  }

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QtMultimediaPrivate::QTlsfMemoryResource::QTlsfMemoryResource(std::
    size_t preallocatedBytes, pmr::memory_resource *upstream)': names
    'QtMultimediaPrivate::pmr::memory_resource', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QtMultimediaPrivate.QTlsfMemoryResource.__init__' has no cute "
        "function yet. Qt's "
        "'QtMultimediaPrivate::QTlsfMemoryResource::QTlsfMemoryResource(std:"
        ":size_t preallocatedBytes, pmr::memory_resource *upstream)': names "
        "'QtMultimediaPrivate::pmr::memory_resource', which has no cute "
        "class yet.")

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
  def do_allocate(*__, **_) -> Never:
    """
    Qt's 'void *QtMultimediaPrivate::QTlsfMemoryResource::do_allocate(size_t
    bytes, size_t alignment)': Qt's library has no name for it, and its code
    in Qt's source does not compile apart from its file: no member named
    'tlsf_memalign' in namespace 'QtPrivate'; did you mean 'posix_memalign'?.
    """
    raise NotImplementedError(
        "'QtMultimediaPrivate.QTlsfMemoryResource.do_allocate' has no cute "
        "function yet. Qt's 'void "
        "*QtMultimediaPrivate::QTlsfMemoryResource::do_allocate(size_t "
        "bytes, size_t alignment)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: no "
        "member named 'tlsf_memalign' in namespace 'QtPrivate'; did you "
        "mean 'posix_memalign'?.")

  @staticmethod
  def do_deallocate(*__, **_) -> Never:
    """
    Qt's 'void QtMultimediaPrivate::QTlsfMemoryResource::do_deallocate(void
    *p, size_t bytes, size_t alignment)': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: no
    member named 'tlsf_free' in namespace 'QtPrivate'.
    """
    raise NotImplementedError(
        "'QtMultimediaPrivate.QTlsfMemoryResource.do_deallocate' has no "
        "cute function yet. Qt's 'void "
        "QtMultimediaPrivate::QTlsfMemoryResource::do_deallocate(void *p, "
        "size_t bytes, size_t alignment)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "no member named 'tlsf_free' in namespace 'QtPrivate'.")

  @staticmethod
  def do_is_equal(*__, **_) -> Never:
    """
    Qt's 'bool QtMultimediaPrivate::QTlsfMemoryResource::do_is_equal(const
    memory_resource &other) const': the compiler refuses its ritual as it
    would be written here: unknown type name 'memory_resource'.
    """
    raise NotImplementedError(
        "'QtMultimediaPrivate.QTlsfMemoryResource.do_is_equal' has no cute "
        "function yet. Qt's 'bool "
        "QtMultimediaPrivate::QTlsfMemoryResource::do_is_equal(const "
        "memory_resource &other) const': the compiler refuses its ritual as "
        "it would be written here: unknown type name 'memory_resource'.")
