"""
QtMetaContainerPrivate stands for the namespace 'QtMetaContainerPrivate' of
Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class QtMetaContainerPrivate:
  """
  The namespace 'QtMetaContainerPrivate' of Qt, which holds no objects. It
  holds the 2 enums Qt writes in it, each under its name, and the 2 names Qt
  has for the combinations of a flags enum, each holding the class of that
  enum. It is never made into an object.
  """

  class AddRemoveCapability(CuteFlags, number='unsigned char'):
    """
    The flags enum 'QtMetaContainerPrivate::AddRemoveCapability' of Qt, with
    the 4 names Qt gives in it. Qt names the type of its combinations
    'QtMetaContainerPrivate::AddRemoveCapabilities'.
    """

    CanAddAtBegin = 0x1
    CanRemoveAtBegin = 0x2
    CanAddAtEnd = 0x4
    CanRemoveAtEnd = 0x8

  AddRemoveCapabilities = AddRemoveCapability

  class IteratorCapability(CuteFlags, number='unsigned char'):
    """
    The flags enum 'QtMetaContainerPrivate::IteratorCapability' of Qt, with
    the 4 names Qt gives in it. Qt names the type of its combinations
    'QtMetaContainerPrivate::IteratorCapabilities'.
    """

    InputCapability = 0x1
    ForwardCapability = 0x2
    BiDirectionalCapability = 0x4
    RandomAccessCapability = 0x8

  IteratorCapabilities = IteratorCapability
