//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebSockets/qwebsockethandshakeoptions.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtWebSockets/qwebsockethandshakeoptions.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QWebSocketHandshakeOptions::QWebSocketHandshakeOptions()
extern "C" Q_DECL_EXPORT
QWebSocketHandshakeOptions *ritual_ZN26QWebSocketHandshakeOptionsC1Ev() {
  return new QWebSocketHandshakeOptions();
}

//  QWebSocketHandshakeOptions::QWebSocketHandshakeOptions(const
//      QWebSocketHandshakeOptions &other)
extern "C" Q_DECL_EXPORT
QWebSocketHandshakeOptions *ritual_ZN26QWebSocketHandshakeOptionsC1ERKS_(
    const QWebSocketHandshakeOptions *other) {
  return new QWebSocketHandshakeOptions(*other);
}

//  QWebSocketHandshakeOptions::QWebSocketHandshakeOptions(QWebSocketHandshak
//      eOptions &&other)
extern "C" Q_DECL_EXPORT
QWebSocketHandshakeOptions *ritual_ZN26QWebSocketHandshakeOptionsC1EOS_(
    QWebSocketHandshakeOptions *other) {
  return new QWebSocketHandshakeOptions(std::move(*other));
}

//  QWebSocketHandshakeOptions::~QWebSocketHandshakeOptions()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWebSocketHandshakeOptionsD1Ev(
    QWebSocketHandshakeOptions *self) {
  delete self;
}

//  QWebSocketHandshakeOptions
//      &QWebSocketHandshakeOptions::operator=(QWebSocketHandshakeOptions
//      &&other)
extern "C" Q_DECL_EXPORT
QWebSocketHandshakeOptions *ritual_ZN26QWebSocketHandshakeOptionsaSEOS_(
    QWebSocketHandshakeOptions *self,
    QWebSocketHandshakeOptions *other) {
  return &(self->operator=(std::move(*other)));
}

//  QWebSocketHandshakeOptions &QWebSocketHandshakeOptions::operator=(const
//      QWebSocketHandshakeOptions &other)
extern "C" Q_DECL_EXPORT
QWebSocketHandshakeOptions *ritual_ZN26QWebSocketHandshakeOptionsaSERKS_(
    QWebSocketHandshakeOptions *self,
    const QWebSocketHandshakeOptions *other) {
  return &(self->operator=(*other));
}

//  void QWebSocketHandshakeOptions::swap(QWebSocketHandshakeOptions &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWebSocketHandshakeOptions4swapERS_(
    QWebSocketHandshakeOptions *self,
    QWebSocketHandshakeOptions *other) {
  self->swap(*other);
}

//  QStringList QWebSocketHandshakeOptions::subprotocols() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK26QWebSocketHandshakeOptions12subprotocolsEv(
    const QWebSocketHandshakeOptions *self) {
  return new QList<QString>(self->subprotocols());
}

//  void QWebSocketHandshakeOptions::setSubprotocols(const QStringList
//      &protocols)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWebSocketHandshakeOptions15setSubprotocolsERK5QListI7QStringE(
    QWebSocketHandshakeOptions *self,
    const QList<QString> *protocols) {
  self->setSubprotocols(*protocols);
}

//  bool QWebSocketHandshakeOptions::equals(const QWebSocketHandshakeOptions
//      &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QWebSocketHandshakeOptions6equalsERKS_(
    const QWebSocketHandshakeOptions *self,
    const QWebSocketHandshakeOptions *other) {
  return self->equals(*other);
}

//  bool operator==(const QWebSocketHandshakeOptions &lhs, const
//      QWebSocketHandshakeOptions &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK26QWebSocketHandshakeOptionsS1_(
    const QWebSocketHandshakeOptions *lhs,
    const QWebSocketHandshakeOptions *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QWebSocketHandshakeOptions &lhs, const
//      QWebSocketHandshakeOptions &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK26QWebSocketHandshakeOptionsS1_(
    const QWebSocketHandshakeOptions *lhs,
    const QWebSocketHandshakeOptions *rhs) {
  return operator!=(*lhs, *rhs);
}
