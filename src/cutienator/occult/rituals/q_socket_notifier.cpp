//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qsocketnotifier.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qsocketnotifier.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QSocketNotifier::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QSocketNotifier10metaObjectEv(
    const QSocketNotifier *self) {
  return self->metaObject();
}

//  QString QSocketNotifier::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QSocketNotifier2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSocketNotifier::tr(s, c, n));
}

//  QSocketNotifier::QSocketNotifier(Type a0, QObject *parent)
extern "C" Q_DECL_EXPORT
QSocketNotifier *ritual_ZN15QSocketNotifierC1ENS_4TypeEP7QObject(
    QSocketNotifier::Type a0,
    QObject *parent) {
  return new QSocketNotifier(a0, parent);
}

//  QSocketNotifier::QSocketNotifier(qintptr socket, Type a1, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QSocketNotifier *ritual_ZN15QSocketNotifierC1ExNS_4TypeEP7QObject(
    qintptr socket,
    QSocketNotifier::Type a1,
    QObject *parent) {
  return new QSocketNotifier(socket, a1, parent);
}

//  QSocketNotifier::~QSocketNotifier()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSocketNotifierD1Ev(QSocketNotifier *self) {
  delete self;
}

//  void QSocketNotifier::setSocket(qintptr socket)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSocketNotifier9setSocketEx(
    QSocketNotifier *self,
    qintptr socket) {
  self->setSocket(socket);
}

//  qintptr QSocketNotifier::socket() const
extern "C" Q_DECL_EXPORT
qintptr ritual_ZNK15QSocketNotifier6socketEv(const QSocketNotifier *self) {
  return self->socket();
}

//  Type QSocketNotifier::type() const
extern "C" Q_DECL_EXPORT
QSocketNotifier::Type ritual_ZNK15QSocketNotifier4typeEv(
    const QSocketNotifier *self) {
  return self->type();
}

//  bool QSocketNotifier::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QSocketNotifier7isValidEv(const QSocketNotifier *self) {
  return self->isValid();
}

//  bool QSocketNotifier::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QSocketNotifier9isEnabledEv(const QSocketNotifier *self) {
  return self->isEnabled();
}

//  void QSocketNotifier::setEnabled(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSocketNotifier10setEnabledEb(
    QSocketNotifier *self,
    bool a0) {
  self->setEnabled(a0);
}
