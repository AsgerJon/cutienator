//  Written by dev_tooling.RitualGenerator from the records of
//  QtNfc/6.12.0/QtNfc/private/qiosndefnotifier_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtNfc/qtnfcglobal.h>
#include <QtNfc/6.12.0/QtNfc/private/qtnfcglobal_p.h>
#if defined(Q_OS_IOS)
#include <QtNfc/6.12.0/QtNfc/private/qtnfcglobal_p.h>
#include <QtNfc/QtNfc>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNfc/6.12.0/QtNfc/private/qiosndefnotifier_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QNfcNdefNotifier::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QNfcNdefNotifier10metaObjectEv(
    const QNfcNdefNotifier *self) {
  return self->metaObject();
}

//  QString QNfcNdefNotifier::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QNfcNdefNotifier2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QNfcNdefNotifier::tr(s, c, n));
}

//  QNfcNdefNotifier::QNfcNdefNotifier()
extern "C" Q_DECL_EXPORT
QNfcNdefNotifier *ritual_ZN16QNfcNdefNotifierC1Ev() {
  return new QNfcNdefNotifier();
}

#endif  // defined(Q_OS_IOS)
