//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qplugin_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qplugin_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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
