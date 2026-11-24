//  Written by dev_tooling.RitualGenerator from the records of
//  QtProtobuf/6.12.0/QtProtobuf/private/qprotobufserializer_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtProtobuf/QtProtobuf>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtProtobuf/6.12.0/QtProtobuf/private/qprotobufserializer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearrayview.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtProtobuf/private/qprotobufdeserializerbase_p.h>
#include <QtProtobuf/private/qprotobufregistration_p.h>
#include <QtProtobuf/private/qtprotobuflogging_p.h>
#include <QtProtobuf/private/qtprotobufserializerhelpers_p.h>
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

//  from ../qtgrpc/src/protobuf/qprotobufdeserializerbase.cpp, line 18, as _ZN25QProtobufDeserializerBase23deserializeMessageFieldEP16QProtobufMessage
inline bool QProtobufDeserializerBase::deserializeMessageField(QProtobufMessage *message)
{
    Q_ASSERT(message != nullptr);

    auto prevCachedRepeatedIterator = std::move(m_cachedRepeatedIterator);
    auto prevCachedPropertyValue = m_cachedPropertyValue;
    auto prevCachedIndex = m_cachedIndex;
    clearCachedValue();
    bool result = deserializeMessage(message);
    m_cachedPropertyValue = prevCachedPropertyValue;
    m_cachedIndex = prevCachedIndex;
    m_cachedRepeatedIterator = std::move(prevCachedRepeatedIterator);

    return result;
}

//  from ../qtgrpc/src/protobuf/qprotobufdeserializerbase.cpp, line 129, as _ZN25QProtobufDeserializerBase16clearCachedValueEv
inline void QProtobufDeserializerBase::clearCachedValue()
{
    m_cachedPropertyValue.clear();
    m_cachedIndex = -1;
    m_cachedRepeatedIterator = {};
}

//  from ../qtgrpc/src/protobuf/qprotobufserializer.cpp, line 303, as _ZN25QProtobufDeserializerImpl5resetE14QByteArrayView
inline void QProtobufDeserializerImpl::reset(QByteArrayView data)
{
    m_it = QProtobufSelfcheckIterator::fromView(data);
    m_state.push_back(data.end());
    clearCachedValue();
}

//  from ../qtgrpc/src/protobuf/qprotobufserializer.cpp, line 310, as _ZN25QProtobufDeserializerImpl8setErrorEN27QAbstractProtobufSerializer5ErrorE14QAnyStringView
inline void QProtobufDeserializerImpl::setError(QAbstractProtobufSerializer::Error error,
                                         QAnyStringView errorString)
{
    m_parent->lastError = error;
    m_parent->lastErrorString = errorString.toString();
}

//  from ../qtgrpc/src/protobuf/qprotobufserializer.cpp, line 466, as _ZN25QProtobufDeserializerImpl10skipVarintEv
inline void QProtobufDeserializerImpl::skipVarint()
{
    while ((*m_it) & 0x80)
        ++m_it;
    ++m_it;
}

//  from ../qtgrpc/src/protobuf/qprotobufserializer.cpp, line 485, as _ZN25QProtobufDeserializerImpl29setUnexpectedEndOfStreamErrorEv
inline void QProtobufDeserializerImpl::setUnexpectedEndOfStreamError()
{
    setError(QAbstractProtobufSerializer::Error::UnexpectedEndOfStream,
             QCoreApplication::translate("QtProtobuf", "Unexpected end of stream"));
}
//  -----------------------------------------------------------------------

//  void QProtobufDeserializerImpl::reset(QByteArrayView data)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QProtobufDeserializerImpl5resetE14QByteArrayView(
    QProtobufDeserializerImpl *self,
    const QByteArrayView *data) {
  self->reset(*data);
}

//  void
//      QProtobufDeserializerImpl::setError(QAbstractProtobufSerializer::Erro
//      r error, QAnyStringView errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QProtobufDeserializerImpl8setErrorEN27QAbstractProtobufSerializer5ErrorE14QAnyStringView(
    QProtobufDeserializerImpl *self,
    QAbstractProtobufSerializer::Error error,
    const QString *errorString) {
  self->setError(error, QAnyStringView(*errorString));
}

//  void QProtobufDeserializerImpl::skipVarint()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QProtobufDeserializerImpl10skipVarintEv(
    QProtobufDeserializerImpl *self) {
  self->skipVarint();
}

//  void QProtobufDeserializerImpl::setUnexpectedEndOfStreamError()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QProtobufDeserializerImpl29setUnexpectedEndOfStreamErrorEv(
    QProtobufDeserializerImpl *self) {
  self->setUnexpectedEndOfStreamError();
}
