//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qsslcertificate_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qsslcertificate_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qsslcertificateextension.h>
#include <QtNetwork/qsslcertificate.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qtnetworkglobal.h>
#if QT_CONFIG(regularexpression)
#include <QtCore/qregularexpression.h>
#endif
#include <QtNetwork/private/qsslcertificateextension_p.h>
#include <QtNetwork/private/qsslcertificate_p.h>
#include <QtNetwork/qsslcertificate.h>
#include <QtNetwork/private/qssl_p.h>
#ifndef QT_NO_SSL
#include <QtNetwork/private/qsslsocket_p.h>
#include <QtNetwork/private/qsslkey_p.h>
#endif
#include <QtCore/qdir.h>
#include <QtCore/qdirlisting.h>
#include <QtCore/qfile.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/ssl/qsslcertificate.cpp, line 845, as _ZNK22QSslCertificatePrivate10extensionsEv
inline QList<QSslCertificateExtension> QSslCertificatePrivate::extensions() const
{
    QList<QSslCertificateExtension> result;

    if (backend.get()) {
        auto nExt = backend->numberOfExtensions();
        for (decltype (nExt) i = 0; i < nExt; ++i) {
            QSslCertificateExtension ext;
            ext.d->oid = backend->oidForExtension(i);
            ext.d->name = backend->nameForExtension(i);
            ext.d->value = backend->valueForExtension(i);
            ext.d->critical = backend->isExtensionCritical(i);
            ext.d->supported = backend->isExtensionSupported(i);
            result << ext;
        }
    }

    return result;
}
//  -----------------------------------------------------------------------

//  QList<QSslCertificateExtension> QSslCertificatePrivate::extensions()
//      const
extern "C" Q_DECL_EXPORT
QList<QSslCertificateExtension> *ritual_ZNK22QSslCertificatePrivate10extensionsEv(
    const QSslCertificatePrivate *self) {
  return new QList<QSslCertificateExtension>(self->extensions());
}

//  bool QSslCertificatePrivate::isBlacklisted(const QSslCertificate
//      &certificate)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QSslCertificatePrivate13isBlacklistedERK15QSslCertificate(
    const QSslCertificate *certificate) {
  return QSslCertificatePrivate::isBlacklisted(*certificate);
}

//  QByteArray
//      QSslCertificatePrivate::subjectInfoToString(QSslCertificate::SubjectI
//      nfo info)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN22QSslCertificatePrivate19subjectInfoToStringEN15QSslCertificate11SubjectInfoE(
    QSslCertificate::SubjectInfo info) {
  return new QByteArray(QSslCertificatePrivate::subjectInfoToString(info));
}
