//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qmimetype_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(mimetype)
#if QT_CONFIG(mimetype)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qmimetype_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QMimeTypePrivate::QMimeTypePrivate()
extern "C" Q_DECL_EXPORT
QMimeTypePrivate *ritual_ZN16QMimeTypePrivateC1Ev() {
  return new QMimeTypePrivate();
}

//  QMimeTypePrivate::QMimeTypePrivate(const QString &name)
extern "C" Q_DECL_EXPORT
QMimeTypePrivate *ritual_ZN16QMimeTypePrivateC1ERK7QString(
    const QString *name) {
  return new QMimeTypePrivate(*name);
}

//  QMimeTypePrivate::~QMimeTypePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QMimeTypePrivateD1Ev(QMimeTypePrivate *self) {
  delete self;
}

#endif  // QT_CONFIG(mimetype)
#endif  // QT_CONFIG(mimetype)
