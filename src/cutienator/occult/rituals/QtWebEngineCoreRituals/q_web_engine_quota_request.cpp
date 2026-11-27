//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebEngineCore/qwebenginequotarequest.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtWebEngineCore/qtwebenginecoreglobal.h>
#if QT_DEPRECATED_SINCE(6, 5)
#include <QtWebEngineCore/qwebenginequotarequest.h>
#include <QtCore/qurl.h>

//  QWebEngineQuotaRequest::QWebEngineQuotaRequest()
extern "C" Q_DECL_EXPORT
QWebEngineQuotaRequest *ritual_ZN22QWebEngineQuotaRequestC1Ev() {
  return new QWebEngineQuotaRequest();
}

//  void QWebEngineQuotaRequest::accept()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWebEngineQuotaRequest6acceptEv(
    QWebEngineQuotaRequest *self) {
  self->accept();
}

//  void QWebEngineQuotaRequest::reject()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWebEngineQuotaRequest6rejectEv(
    QWebEngineQuotaRequest *self) {
  self->reject();
}

//  QUrl QWebEngineQuotaRequest::origin() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK22QWebEngineQuotaRequest6originEv(
    const QWebEngineQuotaRequest *self) {
  return new QUrl(self->origin());
}

//  qint64 QWebEngineQuotaRequest::requestedSize() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK22QWebEngineQuotaRequest13requestedSizeEv(
    const QWebEngineQuotaRequest *self) {
  return self->requestedSize();
}

//  bool QWebEngineQuotaRequest::operator==(const QWebEngineQuotaRequest &a0)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QWebEngineQuotaRequesteqERKS_(
    const QWebEngineQuotaRequest *self,
    const QWebEngineQuotaRequest *a0) {
  return self->operator==(*a0);
}

//  bool QWebEngineQuotaRequest::operator!=(const QWebEngineQuotaRequest &a0)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QWebEngineQuotaRequestneERKS_(
    const QWebEngineQuotaRequest *self,
    const QWebEngineQuotaRequest *a0) {
  return self->operator!=(*a0);
}

//  QWebEngineQuotaRequest::~QWebEngineQuotaRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWebEngineQuotaRequestD1Ev(QWebEngineQuotaRequest *self) {
  delete self;
}

#endif  // QT_DEPRECATED_SINCE(6, 5)
