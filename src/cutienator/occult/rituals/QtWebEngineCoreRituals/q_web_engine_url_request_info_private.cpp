//  Written by dev_tooling.RitualGenerator from the records of QtWebEngineCor
//  e/6.12.0/QtWebEngineCore/private/qwebengineurlrequestinfo_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWebEngineCore/6.12.0/QtWebEngineCore/private/qtwebenginecoreglobal_p.h>
#include <QtWebEngineCore/qwebengineurlrequestinfo.h>
#include <QtWebEngineCore/QtWebEngineCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineCore/6.12.0/QtWebEngineCore/private/qwebengineurlrequestinfo_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <QtCore/qbytearray.h>

//  QWebEngineUrlRequestInfo *QWebEngineUrlRequestInfoPrivate::q_func()
extern "C" Q_DECL_EXPORT
QWebEngineUrlRequestInfo *ritual_ZN31QWebEngineUrlRequestInfoPrivate6q_funcEv(
    QWebEngineUrlRequestInfoPrivate *self) {
  return self->q_func();
}

//  const QWebEngineUrlRequestInfo *QWebEngineUrlRequestInfoPrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const QWebEngineUrlRequestInfo *ritual_ZNK31QWebEngineUrlRequestInfoPrivate6q_funcEv(
    const QWebEngineUrlRequestInfoPrivate *self) {
  return self->q_func();
}

//  QWebEngineUrlRequestInfoPrivate::QWebEngineUrlRequestInfoPrivate(QWebEngi
//      neUrlRequestInfo::ResourceType resource,
//      QWebEngineUrlRequestInfo::NavigationType navigation, const QUrl &u,
//      const QUrl &fpu, const QUrl &i, const QByteArray &m,
//      QtWebEngineCore::ResourceRequestBody *const rb, const
//      QHash<QByteArray, QByteArray> &h, bool isDownload)
extern "C" Q_DECL_EXPORT
QWebEngineUrlRequestInfoPrivate *ritual_ZN31QWebEngineUrlRequestInfoPrivateC1EN24QWebEngineUrlRequestInfo12ResourceTypeENS0_14NavigationTypeERK4QUrlS5_S5_RK10QByteArrayPN15QtWebEngineCore19ResourceRequestBodyERK5QHashIS6_S6_Eb(
    QWebEngineUrlRequestInfo::ResourceType resource,
    QWebEngineUrlRequestInfo::NavigationType navigation,
    const QUrl *u,
    const QUrl *fpu,
    const QUrl *i,
    const QByteArray *m,
    QtWebEngineCore::ResourceRequestBody *const rb,
    const QHash<QByteArray, QByteArray> *h,
    bool isDownload) {
  return new QWebEngineUrlRequestInfoPrivate(
      resource,
      navigation,
      *u,
      *fpu,
      *i,
      *m,
      rb,
      *h,
      isDownload);
}

//  QWebEngineUrlRequestInfoPrivate::~QWebEngineUrlRequestInfoPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QWebEngineUrlRequestInfoPrivateD1Ev(
    QWebEngineUrlRequestInfoPrivate *self) {
  delete self;
}
