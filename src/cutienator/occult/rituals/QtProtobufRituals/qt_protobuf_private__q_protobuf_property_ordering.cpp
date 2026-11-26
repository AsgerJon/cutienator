//  Written by dev_tooling.RitualGenerator from the records of
//  QtProtobuf/qprotobufpropertyordering.h, Qt 6.12.0. Edited by hand on
//  2026-11-25: added by hand, rituals for functions the generator leaves
//  out: 1. Kept as it is when the generator runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtProtobuf/qprotobufpropertyordering.h>
#include <QtCore/QUtf8StringView>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtProtobuf/qprotobufpropertyordering.h>
#include <QtProtobuf/private/qprotobufpropertyorderingbuilder_p.h>
#include <QtProtobuf/private/qtprotobufdefs_p.h>
#include <QtProtobuf/private/qtprotobuflogging_p.h>
#include <QtProtobuf/qprotobufregistration.h>
#include <QtCore/q20utility.h>
#include <QtCore/qhash.h>
#include <QtCore/qmetatype.h>
#include <QtCore/qreadwritelock.h>
#include <QtCore/qstring.h>
#include <limits>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtgrpc/src/protobuf/qprotobufpropertyordering.cpp, line 83, as local:qprotobufpropertyordering.cpp:jsonNameOffsetsOffset
namespace QtProtobufPrivate {
constexpr uint jsonNameOffsetsOffset = 0;
}  // namespace QtProtobufPrivate

//  from ../qtgrpc/src/protobuf/qprotobufpropertyordering.cpp, line 154, as _ZNK17QtProtobufPrivate25QProtobufPropertyOrdering9uint_dataENS0_11NonConstTagE
namespace QtProtobufPrivate {
inline uint *QProtobufPropertyOrdering::uint_data(NonConstTag /*unused*/) const
{
    Q_ASSERT(data);
    Q_ASSERT(data->version == 0);
    quintptr dataPtr = quintptr(data);
    dataPtr += sizeof(Data);
#if 0 // if Data is ever not just a bunch of uints, remove the #if 0
        if (dataPtr % alignof(uint) != 0)
            dataPtr += alignof(uint) - (dataPtr % alignof(uint));
#else
    static_assert(alignof(Data) == alignof(uint));
#endif
    return reinterpret_cast<uint *>(dataPtr);
}
}  // namespace QtProtobufPrivate

//  from ../qtgrpc/src/protobuf/qprotobufpropertyordering.cpp, line 180, as _ZNK17QtProtobufPrivate25QProtobufPropertyOrdering9char_dataENS0_11NonConstTagE
namespace QtProtobufPrivate {
inline char *QProtobufPropertyOrdering::char_data(NonConstTag /*unused*/) const
{
    Q_ASSERT(data);
    uint* uintDataPtr = uint_data(NonConstTag{});
    // char_data starts after the last field flag (flagsOffset + numFields)
    uint charDataOffset = data->flagsOffset + data->numFields;
    return reinterpret_cast<char *>(uintDataPtr + charDataOffset);
}
}  // namespace QtProtobufPrivate

//  from ../qtgrpc/src/protobuf/qprotobufpropertyordering.cpp, line 169, as _ZNK17QtProtobufPrivate25QProtobufPropertyOrdering9uint_dataEv
namespace QtProtobufPrivate {
inline const uint *QProtobufPropertyOrdering::uint_data() const
{
    return uint_data(NonConstTag{});
}
}  // namespace QtProtobufPrivate

//  from ../qtgrpc/src/protobuf/qprotobufpropertyordering.cpp, line 189, as _ZNK17QtProtobufPrivate25QProtobufPropertyOrdering9char_dataEv
namespace QtProtobufPrivate {
inline const char *QProtobufPropertyOrdering::char_data() const
{
    return char_data(NonConstTag{});
}
}  // namespace QtProtobufPrivate

//  from ../qtgrpc/src/protobuf/qprotobufpropertyordering.cpp, line 194, as _ZNK17QtProtobufPrivate25QProtobufPropertyOrdering17uint_dataForIndexEij
namespace QtProtobufPrivate {
inline const uint &QProtobufPropertyOrdering::uint_dataForIndex(int index, uint offset) const
{
    Q_ASSERT(data);
    Q_ASSERT(index >= 0);
    Q_ASSERT(uint(index) < data->numFields
             || (offset == jsonNameOffsetsOffset && uint(index) == data->numFields));
    return *(uint_data() + offset + index);
}
}  // namespace QtProtobufPrivate
//  -----------------------------------------------------------------------

//  QUtf8StringView
//      QtProtobufPrivate::QProtobufPropertyOrdering::messageFullName() const
extern "C" Q_DECL_EXPORT
QUtf8StringView *ritual_ZNK17QtProtobufPrivate25QProtobufPropertyOrdering15messageFullNameEv(
    const QtProtobufPrivate::QProtobufPropertyOrdering *self) {
  return new QUtf8StringView(self->messageFullName());
}

//  QUtf8StringView
//      QtProtobufPrivate::QProtobufPropertyOrdering::jsonName(int index)
//      const
extern "C" Q_DECL_EXPORT
QUtf8StringView *ritual_ZNK17QtProtobufPrivate25QProtobufPropertyOrdering8jsonNameEi(
    const QtProtobufPrivate::QProtobufPropertyOrdering *self,
    int index) {
  return new QUtf8StringView(self->jsonName(index));
}

//  int QtProtobufPrivate::QProtobufPropertyOrdering::fieldNumber(int index)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QtProtobufPrivate25QProtobufPropertyOrdering11fieldNumberEi(
    const QtProtobufPrivate::QProtobufPropertyOrdering *self,
    int index) {
  return self->fieldNumber(index);
}

//  int QtProtobufPrivate::QProtobufPropertyOrdering::propertyIndex(int
//      index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QtProtobufPrivate25QProtobufPropertyOrdering13propertyIndexEi(
    const QtProtobufPrivate::QProtobufPropertyOrdering *self,
    int index) {
  return self->propertyIndex(index);
}

//  FieldFlags QtProtobufPrivate::QProtobufPropertyOrdering::fieldFlags(int
//      index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QtProtobufPrivate25QProtobufPropertyOrdering10fieldFlagsEi(
    const QtProtobufPrivate::QProtobufPropertyOrdering *self,
    int index) {
  return static_cast<int>(self->fieldFlags(index).toInt());
}

//  int QtProtobufPrivate::QProtobufPropertyOrdering::indexOfFieldNumber(int
//      fieldNumber) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QtProtobufPrivate25QProtobufPropertyOrdering18indexOfFieldNumberEi(
    const QtProtobufPrivate::QProtobufPropertyOrdering *self,
    int fieldNumber) {
  return self->indexOfFieldNumber(fieldNumber);
}

//  int QtProtobufPrivate::QProtobufPropertyOrdering::fieldCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QtProtobufPrivate25QProtobufPropertyOrdering10fieldCountEv(
    const QtProtobufPrivate::QProtobufPropertyOrdering *self) {
  return self->fieldCount();
}

//  char *QtProtobufPrivate::QProtobufPropertyOrdering::char_data(NonConstTag
//      a0) const
extern "C" Q_DECL_EXPORT
char *ritual_ZNK17QtProtobufPrivate25QProtobufPropertyOrdering9char_dataENS0_11NonConstTagE(
    const QtProtobufPrivate::QProtobufPropertyOrdering *self,
    const QtProtobufPrivate::QProtobufPropertyOrdering::NonConstTag *a0) {
  return self->char_data(*a0);
}

//  const uint *QtProtobufPrivate::QProtobufPropertyOrdering::uint_data()
//      const
extern "C" Q_DECL_EXPORT
const uint *ritual_ZNK17QtProtobufPrivate25QProtobufPropertyOrdering9uint_dataEv(
    const QtProtobufPrivate::QProtobufPropertyOrdering *self) {
  return self->uint_data();
}

//  const char *QtProtobufPrivate::QProtobufPropertyOrdering::char_data()
//      const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK17QtProtobufPrivate25QProtobufPropertyOrdering9char_dataEv(
    const QtProtobufPrivate::QProtobufPropertyOrdering *self) {
  return self->char_data();
}

//  const uint
//      &QtProtobufPrivate::QProtobufPropertyOrdering::uint_dataForIndex(int
//      index, uint offset) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK17QtProtobufPrivate25QProtobufPropertyOrdering17uint_dataForIndexEij(
    const QtProtobufPrivate::QProtobufPropertyOrdering *self,
    int index,
    uint offset) {
  return self->uint_dataForIndex(index, offset);
}

//  QtProtobufPrivate::QProtobufPropertyOrdering::~QProtobufPropertyOrdering(
//      )
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtProtobufPrivate25QProtobufPropertyOrderingD1Ev(
    QtProtobufPrivate::QProtobufPropertyOrdering *self) {
  delete self;
}

//  a QUtf8StringView a ritual of
//      QtProtobufPrivate::QProtobufPropertyOrdering gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QtProtobufPrivate_QProtobufPropertyOrdering__QUtf8StringView(
    QUtf8StringView *self) {
  delete self;
}

//  uint *QtProtobufPrivate::QProtobufPropertyOrdering::uint_data(NonConstTag
//      a0) const
extern "C" Q_DECL_EXPORT
uint *ritual_ZNK17QtProtobufPrivate25QProtobufPropertyOrdering9uint_dataENS0_11NonConstTagE(
    const QtProtobufPrivate::QProtobufPropertyOrdering *self) {
  return self->uint_data(
      QtProtobufPrivate::QProtobufPropertyOrdering::NonConstTag());
}
