//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qgeocodereply_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeocodereply_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QGeoCodeReplyPrivate::QGeoCodeReplyPrivate()
extern "C" Q_DECL_EXPORT
QGeoCodeReplyPrivate *ritual_ZN20QGeoCodeReplyPrivateC1Ev() {
  return new QGeoCodeReplyPrivate();
}

//  QGeoCodeReplyPrivate::QGeoCodeReplyPrivate(QGeoCodeReply::Error error,
//      const QString &errorString)
extern "C" Q_DECL_EXPORT
QGeoCodeReplyPrivate *ritual_ZN20QGeoCodeReplyPrivateC1EN13QGeoCodeReply5ErrorERK7QString(
    QGeoCodeReply::Error error,
    const QString *errorString) {
  return new QGeoCodeReplyPrivate(error, *errorString);
}

//  const QGeoCodeReplyPrivate *QGeoCodeReplyPrivate::get(const QGeoCodeReply
//      &reply)
extern "C" Q_DECL_EXPORT
const QGeoCodeReplyPrivate *ritual_ZN20QGeoCodeReplyPrivate3getERK13QGeoCodeReply(
    const QGeoCodeReply *reply) {
  return QGeoCodeReplyPrivate::get(*reply);
}

//  QGeoCodeReplyPrivate *QGeoCodeReplyPrivate::get(QGeoCodeReply &reply)
extern "C" Q_DECL_EXPORT
QGeoCodeReplyPrivate *ritual_ZN20QGeoCodeReplyPrivate3getER13QGeoCodeReply(
    QGeoCodeReply *reply) {
  return QGeoCodeReplyPrivate::get(*reply);
}
