//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebSockets/qwebsocketcorsauthenticator.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtWebSockets/qwebsocketcorsauthenticator.h>
#include <QtCore/qstring.h>

//  QWebSocketCorsAuthenticatorPrivate *QWebSocketCorsAuthenticator::d_func()
extern "C" Q_DECL_EXPORT
QWebSocketCorsAuthenticatorPrivate *ritual_ZN27QWebSocketCorsAuthenticator6d_funcEv(
    QWebSocketCorsAuthenticator *self) {
  return self->d_func();
}

//  const QWebSocketCorsAuthenticatorPrivate
//      *QWebSocketCorsAuthenticator::d_func() const
extern "C" Q_DECL_EXPORT
const QWebSocketCorsAuthenticatorPrivate *ritual_ZNK27QWebSocketCorsAuthenticator6d_funcEv(
    const QWebSocketCorsAuthenticator *self) {
  return self->d_func();
}

//  QWebSocketCorsAuthenticator::QWebSocketCorsAuthenticator(const QString
//      &origin)
extern "C" Q_DECL_EXPORT
QWebSocketCorsAuthenticator *ritual_ZN27QWebSocketCorsAuthenticatorC1ERK7QString(
    const QString *origin) {
  return new QWebSocketCorsAuthenticator(*origin);
}

//  QWebSocketCorsAuthenticator::~QWebSocketCorsAuthenticator()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QWebSocketCorsAuthenticatorD1Ev(
    QWebSocketCorsAuthenticator *self) {
  delete self;
}

//  QWebSocketCorsAuthenticator::QWebSocketCorsAuthenticator(const
//      QWebSocketCorsAuthenticator &other)
extern "C" Q_DECL_EXPORT
QWebSocketCorsAuthenticator *ritual_ZN27QWebSocketCorsAuthenticatorC1ERKS_(
    const QWebSocketCorsAuthenticator *other) {
  return new QWebSocketCorsAuthenticator(*other);
}

//  QString QWebSocketCorsAuthenticator::origin() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QWebSocketCorsAuthenticator6originEv(
    const QWebSocketCorsAuthenticator *self) {
  return new QString(self->origin());
}

//  void QWebSocketCorsAuthenticator::setAllowed(bool allowed)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QWebSocketCorsAuthenticator10setAllowedEb(
    QWebSocketCorsAuthenticator *self,
    bool allowed) {
  self->setAllowed(allowed);
}

//  bool QWebSocketCorsAuthenticator::allowed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QWebSocketCorsAuthenticator7allowedEv(
    const QWebSocketCorsAuthenticator *self) {
  return self->allowed();
}
