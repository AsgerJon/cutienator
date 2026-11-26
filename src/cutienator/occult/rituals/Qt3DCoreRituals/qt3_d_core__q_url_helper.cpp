//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qurlhelper_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qurlhelper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <QtCore/qstring.h>

//  QString Qt3DCore::QUrlHelper::urlToLocalFileOrQrc(const QUrl &url)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Qt3DCore10QUrlHelper19urlToLocalFileOrQrcERK4QUrl(
    const QUrl *url) {
  return new QString(Qt3DCore::QUrlHelper::urlToLocalFileOrQrc(*url));
}

//  Qt3DCore::QUrlHelper::~QUrlHelper()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QUrlHelperD1Ev(Qt3DCore::QUrlHelper *self) {
  delete self;
}
