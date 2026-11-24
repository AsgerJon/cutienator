//  Written by dev_tooling.RitualGenerator from the records of
//  QtProtobuf/6.12.0/QtProtobuf/private/qprotobufserializer_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtProtobuf/QtProtobuf>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtProtobuf/6.12.0/QtProtobuf/private/qprotobufserializer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtProtobuf/qprotobufserializer.h>
#include <QtProtobuf/private/protobufscalarserializers_p.h>
#include <QtProtobuf/private/qprotobufmessage_p.h>
#include <QtProtobuf/private/qprotobufregistration_p.h>
#include <QtProtobuf/private/qprotobufserializer_p.h>
#include <QtProtobuf/private/qprotobufserializerbase_p.h>
#include <QtProtobuf/private/qtprotobufdefs_p.h>
#include <QtProtobuf/private/qtprotobufserializerhelpers_p.h>
#include <QtProtobuf/qprotobufmessage.h>
#include <QtProtobuf/qtprotobuftypes.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qlist.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qmetatype.h>
#include <QtCore/qreadwritelock.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtgrpc/src/protobuf/qprotobufserializer.cpp, line 183, as _ZN23QProtobufSerializerImpl5resetEv
inline void QProtobufSerializerImpl::reset()
{
    m_state.clear();
    m_result = {};
}

//  from ../qtgrpc/src/protobuf/qprotobufserializer.cpp, line 189, as _ZN23QProtobufSerializerImpl22serializeUnknownFieldsEPK16QProtobufMessage
inline void QProtobufSerializerImpl::serializeUnknownFields(const QProtobufMessage *message)
{
    if (m_parent->preserveUnknownFields) {
        // Restore any unknown fields we have stored away:
        for (const auto &fields :
             std::as_const(QProtobufMessagePrivate::get(message)->unknownEntries)) {
            m_result += fields.join();
        }
    }
}

//  from ../qtgrpc/src/protobuf/qprotobufserializer.cpp, line 254, as _ZN23QProtobufSerializerImpl26serializeMessageFieldBeginEv
inline void QProtobufSerializerImpl::serializeMessageFieldBegin()
{
    m_state.emplaceBack(std::move(m_result));
    m_result = {};
}
//  -----------------------------------------------------------------------

//  const QByteArray &QProtobufSerializerImpl::result() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK23QProtobufSerializerImpl6resultEv(
    const QProtobufSerializerImpl *self) {
  return new QByteArray(self->result());
}

//  void QProtobufSerializerImpl::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QProtobufSerializerImpl5resetEv(
    QProtobufSerializerImpl *self) {
  self->reset();
}

//  void QProtobufSerializerImpl::serializeUnknownFields(const
//      QProtobufMessage *message)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QProtobufSerializerImpl22serializeUnknownFieldsEPK16QProtobufMessage(
    QProtobufSerializerImpl *self,
    const QProtobufMessage *message) {
  self->serializeUnknownFields(message);
}

//  void QProtobufSerializerImpl::serializeMessageFieldBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QProtobufSerializerImpl26serializeMessageFieldBeginEv(
    QProtobufSerializerImpl *self) {
  self->serializeMessageFieldBegin();
}
