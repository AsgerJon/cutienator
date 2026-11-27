//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebEngineCore/qwebengineregisterprotocolhandlerrequest.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWebEngineCore/qwebengineregisterprotocolhandlerrequest.h>
#include <QtCore/qurl.h>
#include <QtCore/qstring.h>
#include <QtCore/QSharedPointer>
#include <QtWebEngineCore/QtWebEngineCore>

//  QWebEngineRegisterProtocolHandlerRequest::QWebEngineRegisterProtocolHandl
//      erRequest()
extern "C" Q_DECL_EXPORT
QWebEngineRegisterProtocolHandlerRequest *ritual_ZN40QWebEngineRegisterProtocolHandlerRequestC1Ev() {
  return new QWebEngineRegisterProtocolHandlerRequest();
}

//  void QWebEngineRegisterProtocolHandlerRequest::accept()
extern "C" Q_DECL_EXPORT
void ritual_ZN40QWebEngineRegisterProtocolHandlerRequest6acceptEv(
    QWebEngineRegisterProtocolHandlerRequest *self) {
  self->accept();
}

//  void QWebEngineRegisterProtocolHandlerRequest::reject()
extern "C" Q_DECL_EXPORT
void ritual_ZN40QWebEngineRegisterProtocolHandlerRequest6rejectEv(
    QWebEngineRegisterProtocolHandlerRequest *self) {
  self->reject();
}

//  QUrl QWebEngineRegisterProtocolHandlerRequest::origin() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK40QWebEngineRegisterProtocolHandlerRequest6originEv(
    const QWebEngineRegisterProtocolHandlerRequest *self) {
  return new QUrl(self->origin());
}

//  QString QWebEngineRegisterProtocolHandlerRequest::scheme() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK40QWebEngineRegisterProtocolHandlerRequest6schemeEv(
    const QWebEngineRegisterProtocolHandlerRequest *self) {
  return new QString(self->scheme());
}

//  bool QWebEngineRegisterProtocolHandlerRequest::operator==(const
//      QWebEngineRegisterProtocolHandlerRequest &that) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK40QWebEngineRegisterProtocolHandlerRequesteqERKS_(
    const QWebEngineRegisterProtocolHandlerRequest *self,
    const QWebEngineRegisterProtocolHandlerRequest *that) {
  return self->operator==(*that);
}

//  bool QWebEngineRegisterProtocolHandlerRequest::operator!=(const
//      QWebEngineRegisterProtocolHandlerRequest &that) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK40QWebEngineRegisterProtocolHandlerRequestneERKS_(
    const QWebEngineRegisterProtocolHandlerRequest *self,
    const QWebEngineRegisterProtocolHandlerRequest *that) {
  return self->operator!=(*that);
}

//  QWebEngineRegisterProtocolHandlerRequest::QWebEngineRegisterProtocolHandl
//      erRequest(QSharedPointer<QtWebEngineCore::RegisterProtocolHandlerRequ
//      estController> a0)
extern "C" Q_DECL_EXPORT
QWebEngineRegisterProtocolHandlerRequest *ritual_ZN40QWebEngineRegisterProtocolHandlerRequestC1E14QSharedPointerIN15QtWebEngineCore40RegisterProtocolHandlerRequestControllerEE(
    const QSharedPointer<QtWebEngineCore::RegisterProtocolHandlerRequestController> *a0) {
  return new QWebEngineRegisterProtocolHandlerRequest(*a0);
}

//  QWebEngineRegisterProtocolHandlerRequest::~QWebEngineRegisterProtocolHand
//      lerRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN40QWebEngineRegisterProtocolHandlerRequestD1Ev(
    QWebEngineRegisterProtocolHandlerRequest *self) {
  delete self;
}
