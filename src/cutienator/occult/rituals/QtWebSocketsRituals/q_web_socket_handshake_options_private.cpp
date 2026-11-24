//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebSockets/6.12.0/QtWebSockets/private/qwebsockethandshakeoptions_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtWebSockets/QtWebSockets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebSockets/6.12.0/QtWebSockets/private/qwebsockethandshakeoptions_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool QWebSocketHandshakeOptionsPrivate::operator==(const
//      QWebSocketHandshakeOptionsPrivate &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK33QWebSocketHandshakeOptionsPrivateeqERKS_(
    const QWebSocketHandshakeOptionsPrivate *self,
    const QWebSocketHandshakeOptionsPrivate *other) {
  return self->operator==(*other);
}

//  QWebSocketHandshakeOptionsPrivate::~QWebSocketHandshakeOptionsPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QWebSocketHandshakeOptionsPrivateD1Ev(
    QWebSocketHandshakeOptionsPrivate *self) {
  delete self;
}
