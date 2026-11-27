//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebEngineCore/qwebenginefullscreenrequest.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWebEngineCore/qwebenginefullscreenrequest.h>
#include <QtCore/qurl.h>

//  QWebEngineFullScreenRequest::QWebEngineFullScreenRequest()
extern "C" Q_DECL_EXPORT
QWebEngineFullScreenRequest *ritual_ZN27QWebEngineFullScreenRequestC1Ev() {
  return new QWebEngineFullScreenRequest();
}

//  QWebEngineFullScreenRequest::QWebEngineFullScreenRequest(const
//      QWebEngineFullScreenRequest &other)
extern "C" Q_DECL_EXPORT
QWebEngineFullScreenRequest *ritual_ZN27QWebEngineFullScreenRequestC1ERKS_(
    const QWebEngineFullScreenRequest *other) {
  return new QWebEngineFullScreenRequest(*other);
}

//  QWebEngineFullScreenRequest &QWebEngineFullScreenRequest::operator=(const
//      QWebEngineFullScreenRequest &other)
extern "C" Q_DECL_EXPORT
QWebEngineFullScreenRequest *ritual_ZN27QWebEngineFullScreenRequestaSERKS_(
    QWebEngineFullScreenRequest *self,
    const QWebEngineFullScreenRequest *other) {
  return &(self->operator=(*other));
}

//  QWebEngineFullScreenRequest::QWebEngineFullScreenRequest(QWebEngineFullSc
//      reenRequest &&other)
extern "C" Q_DECL_EXPORT
QWebEngineFullScreenRequest *ritual_ZN27QWebEngineFullScreenRequestC1EOS_(
    QWebEngineFullScreenRequest *other) {
  return new QWebEngineFullScreenRequest(std::move(*other));
}

//  QWebEngineFullScreenRequest
//      &QWebEngineFullScreenRequest::operator=(QWebEngineFullScreenRequest
//      &&other)
extern "C" Q_DECL_EXPORT
QWebEngineFullScreenRequest *ritual_ZN27QWebEngineFullScreenRequestaSEOS_(
    QWebEngineFullScreenRequest *self,
    QWebEngineFullScreenRequest *other) {
  return &(self->operator=(std::move(*other)));
}

//  QWebEngineFullScreenRequest::~QWebEngineFullScreenRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QWebEngineFullScreenRequestD1Ev(
    QWebEngineFullScreenRequest *self) {
  delete self;
}

//  void QWebEngineFullScreenRequest::reject()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QWebEngineFullScreenRequest6rejectEv(
    QWebEngineFullScreenRequest *self) {
  self->reject();
}

//  void QWebEngineFullScreenRequest::accept()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QWebEngineFullScreenRequest6acceptEv(
    QWebEngineFullScreenRequest *self) {
  self->accept();
}

//  bool QWebEngineFullScreenRequest::toggleOn() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QWebEngineFullScreenRequest8toggleOnEv(
    const QWebEngineFullScreenRequest *self) {
  return self->toggleOn();
}

//  QUrl QWebEngineFullScreenRequest::origin() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK27QWebEngineFullScreenRequest6originEv(
    const QWebEngineFullScreenRequest *self) {
  return new QUrl(self->origin());
}

//  QWebEngineFullScreenRequest::QWebEngineFullScreenRequest(const QUrl
//      &origin, bool toggleOn, const std::function<void (bool)>
//      &setFullScreenCallback)
extern "C" Q_DECL_EXPORT
QWebEngineFullScreenRequest *ritual_ZN27QWebEngineFullScreenRequestC1ERK4QUrlbRKSt8functionIFvbEE(
    const QUrl *origin,
    bool toggleOn,
    const std::function<void (bool)> *setFullScreenCallback) {
  return new QWebEngineFullScreenRequest(
      *origin,
      toggleOn,
      *setFullScreenCallback);
}
