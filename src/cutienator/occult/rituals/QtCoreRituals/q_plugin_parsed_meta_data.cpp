//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qplugin_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qplugin_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qplugin.h>
#include <QtCore/qjsonobject.h>
#include <QtCore/qcbormap.h>
#include <QtCore/qcborvalue.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/private/qfactoryloader_p.h>
#include <QtCore/private/qcoreapplication_p.h>
#include <QtCore/private/qloggingregistry_p.h>
#include <QtCore/qcborarray.h>
#include <QtCore/qcbormap.h>
#include <QtCore/qcborstreamreader.h>
#include <QtCore/qcborvalue.h>
#include <QtCore/qdirlisting.h>
#include <QtCore/qfileinfo.h>
#include <QtCore/qjsonarray.h>
#include <QtCore/qjsondocument.h>
#include <QtCore/qjsonobject.h>
#include <QtCore/qplugin.h>
#include <QtCore/qpluginloader.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/corelib/plugin/qfactoryloader.cpp, line 31, as local:qfactoryloader.cpp:IterationResult
namespace {
struct IterationResult
{
    enum Result {
        FinishedSearch = 0,
        ContinueSearch,

        // parse errors
        ParsingError = -1,
        InvalidMetaDataVersion = -2,
        InvalidTopLevelItem = -3,
        InvalidHeaderItem = -4,
    };
    Result result;
    QCborError error = { QCborError::NoError };

    Q_IMPLICIT IterationResult(Result r) : result(r) {}
    Q_IMPLICIT IterationResult(QCborError e) : result(ParsingError), error(e) {}
};
}  // namespace

//  from src/corelib/plugin/qfactoryloader.cpp, line 117, as local:qfactoryloader.cpp:iterateInPluginMetaData
template <typename F> static IterationResult iterateInPluginMetaData(QByteArrayView raw, F &&f)
{
    QPluginMetaData::Header header;
    Q_ASSERT(raw.size() >= qsizetype(sizeof(header)));
    memcpy(&header, raw.data(), sizeof(header));
    if (Q_UNLIKELY(header.version > QPluginMetaData::CurrentMetaDataVersion))
        return IterationResult::InvalidMetaDataVersion;

    // use fromRawData to keep QCborStreamReader from copying
    raw = raw.sliced(sizeof(header));
    QByteArray ba = QByteArray::fromRawData(raw.data(), raw.size());
    QCborStreamReader reader(ba);
    if (reader.isInvalid())
        return reader.lastError();
    if (!reader.isMap())
        return IterationResult::InvalidTopLevelItem;
    if (!reader.enterContainer())
        return reader.lastError();
    while (reader.isValid()) {
        IterationResult::Result r;
        if (reader.isInteger()) {
            // integer key, one of ours
            qint64 value = reader.toInteger();
            auto key = QtPluginMetaDataKeys(value);
            if (qint64(key) != value)
                return IterationResult::InvalidHeaderItem;
            if (!reader.next())
                return reader.lastError();
            r = f(key, reader);
        } else if (reader.isString()) {
            QByteArray key = reader.readAllUtf8String();
            if (key.isNull())
                return reader.lastError();
            r = f(QUtf8StringView(key), reader);
        } else {
            return IterationResult::InvalidTopLevelItem;
        }

        if (QCborError e = reader.lastError())
            return e;
        if (r != IterationResult::ContinueSearch)
            return r;
    }

    if (!reader.leaveContainer())
        return reader.lastError();
    return IterationResult::FinishedSearch;
}

//  from src/corelib/plugin/qfactoryloader.cpp, line 173, as _ZN21QPluginParsedMetaData5parseE14QByteArrayView
inline bool QPluginParsedMetaData::parse(QByteArrayView raw)
{
    QCborMap map;
    auto r = iterateInPluginMetaData(raw, [&](const auto &key, QCborStreamReader &reader) {
        QCborValue item = QCborValue::fromCbor(reader);
        if (item.isInvalid())
            return IterationResult::ParsingError;
        if constexpr (std::is_enum_v<std::decay_t<decltype(key)>>)
            map[int(key)] = item;
        else
            map[QString::fromUtf8(key)] = item;
        return IterationResult::ContinueSearch;
    });

    switch (r.result) {
    case IterationResult::FinishedSearch:
    case IterationResult::ContinueSearch:
        break;

    // parse errors
    case IterationResult::ParsingError:
        return setError(QFactoryLoader::tr("Metadata parsing error: %1").arg(r.error.toString()));
    case IterationResult::InvalidMetaDataVersion:
        return setError(QFactoryLoader::tr("Invalid metadata version"));
    case IterationResult::InvalidTopLevelItem:
    case IterationResult::InvalidHeaderItem:
        return setError(QFactoryLoader::tr("Unexpected metadata contents"));
    }

    // header was validated
    auto header = qFromUnaligned<QPluginMetaData::Header>(raw.data());

    DecodedArchRequirements archReq =
            header.version == 0 ? decodeVersion0ArchRequirements(header.plugin_arch_requirements)
                                : decodeVersion1ArchRequirements(header.plugin_arch_requirements);

    // insert the keys not stored in the top-level CBOR map
    map[int(QtPluginMetaDataKeys::QtVersion)] =
               QT_VERSION_CHECK(header.qt_major_version, header.qt_minor_version, 0);
    map[int(QtPluginMetaDataKeys::IsDebug)] = archReq.isDebug;
    map[int(QtPluginMetaDataKeys::Requirements)] = archReq.level;

    data = std::move(map);
    return true;
}

//  from src/corelib/plugin/qfactoryloader.cpp, line 219, as _ZNK21QPluginParsedMetaData6toJsonEv
inline QJsonObject QPluginParsedMetaData::toJson() const
{
    // convert from the internal CBOR representation to an external JSON one
    QJsonObject o;
    for (auto it : data.toMap()) {
        QString key;
        if (it.first.isInteger()) {
            switch (it.first.toInteger()) {
#define CONVERT_TO_STRING(IntKey, StringKey, Description) \
            case int(IntKey): key = QStringLiteral(StringKey); break;
                QT_PLUGIN_FOREACH_METADATA(CONVERT_TO_STRING)
            }
        } else {
            key = it.first.toString();
        }

        if (!key.isEmpty())
            o.insert(key, it.second.toJsonValue());
    }
    return o;
}
//  -----------------------------------------------------------------------

//  bool QPluginParsedMetaData::setError(const QString &errorString)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QPluginParsedMetaData8setErrorERK7QString(
    QPluginParsedMetaData *self,
    const QString *errorString) {
  return self->setError(*errorString);
}

//  QPluginParsedMetaData::QPluginParsedMetaData()
extern "C" Q_DECL_EXPORT
QPluginParsedMetaData *ritual_ZN21QPluginParsedMetaDataC1Ev() {
  return new QPluginParsedMetaData();
}

//  QPluginParsedMetaData::QPluginParsedMetaData(QByteArrayView input)
extern "C" Q_DECL_EXPORT
QPluginParsedMetaData *ritual_ZN21QPluginParsedMetaDataC1E14QByteArrayView(
    const QByteArrayView *input) {
  return new QPluginParsedMetaData(*input);
}

//  bool QPluginParsedMetaData::isError() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QPluginParsedMetaData7isErrorEv(
    const QPluginParsedMetaData *self) {
  return self->isError();
}

//  QString QPluginParsedMetaData::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QPluginParsedMetaData11errorStringEv(
    const QPluginParsedMetaData *self) {
  return new QString(self->errorString());
}

//  bool QPluginParsedMetaData::parse(QPluginMetaData metaData)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QPluginParsedMetaData5parseE15QPluginMetaData(
    QPluginParsedMetaData *self,
    const QPluginMetaData *metaData) {
  return self->parse(*metaData);
}

//  QJsonObject QPluginParsedMetaData::toJson() const
extern "C" Q_DECL_EXPORT
QJsonObject *ritual_ZNK21QPluginParsedMetaData6toJsonEv(
    const QPluginParsedMetaData *self) {
  return new QJsonObject(self->toJson());
}

//  QCborMap QPluginParsedMetaData::toCbor() const
extern "C" Q_DECL_EXPORT
QCborMap *ritual_ZNK21QPluginParsedMetaData6toCborEv(
    const QPluginParsedMetaData *self) {
  return new QCborMap(self->toCbor());
}

//  QCborValue QPluginParsedMetaData::value(QtPluginMetaDataKeys k) const
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZNK21QPluginParsedMetaData5valueE20QtPluginMetaDataKeys(
    const QPluginParsedMetaData *self,
    QtPluginMetaDataKeys k) {
  return new QCborValue(self->value(k));
}

//  QPluginParsedMetaData::~QPluginParsedMetaData()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPluginParsedMetaDataD1Ev(QPluginParsedMetaData *self) {
  delete self;
}
