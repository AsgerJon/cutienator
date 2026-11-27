//  Written by dev_tooling.RitualGenerator from the records of QtWebEngineQui
//  ck/6.12.0/QtWebEngineQuick/private/qquickwebengineclientcertificateselect
//  ion_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qtwebenginequickglobal_p.h>
#include <QtWebEngineQuick/QtWebEngineQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebengineclientcertificateselection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qdatetime.h>

//  const QMetaObject *QQuickWebEngineClientCertificateOption::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK38QQuickWebEngineClientCertificateOption10metaObjectEv(
    const QQuickWebEngineClientCertificateOption *self) {
  return self->metaObject();
}

//  void *QQuickWebEngineClientCertificateOption::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN38QQuickWebEngineClientCertificateOption11qt_metacastEPKc(
    QQuickWebEngineClientCertificateOption *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickWebEngineClientCertificateOption::qt_metacall(QMetaObject::Call
//      a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN38QQuickWebEngineClientCertificateOption11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickWebEngineClientCertificateOption *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickWebEngineClientCertificateOption::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN38QQuickWebEngineClientCertificateOption2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickWebEngineClientCertificateOption::tr(s, c, n));
}

//  void QQuickWebEngineClientCertificateOption::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN38QQuickWebEngineClientCertificateOption24qt_qmlMarker_uncreatableEv(
    QQuickWebEngineClientCertificateOption *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QString QQuickWebEngineClientCertificateOption::issuer() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK38QQuickWebEngineClientCertificateOption6issuerEv(
    const QQuickWebEngineClientCertificateOption *self) {
  return new QString(self->issuer());
}

//  QString QQuickWebEngineClientCertificateOption::subject() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK38QQuickWebEngineClientCertificateOption7subjectEv(
    const QQuickWebEngineClientCertificateOption *self) {
  return new QString(self->subject());
}

//  QDateTime QQuickWebEngineClientCertificateOption::effectiveDate() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK38QQuickWebEngineClientCertificateOption13effectiveDateEv(
    const QQuickWebEngineClientCertificateOption *self) {
  return new QDateTime(self->effectiveDate());
}

//  QDateTime QQuickWebEngineClientCertificateOption::expiryDate() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK38QQuickWebEngineClientCertificateOption10expiryDateEv(
    const QQuickWebEngineClientCertificateOption *self) {
  return new QDateTime(self->expiryDate());
}

//  bool QQuickWebEngineClientCertificateOption::isSelfSigned() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK38QQuickWebEngineClientCertificateOption12isSelfSignedEv(
    const QQuickWebEngineClientCertificateOption *self) {
  return self->isSelfSigned();
}

//  void QQuickWebEngineClientCertificateOption::select()
extern "C" Q_DECL_EXPORT
void ritual_ZN38QQuickWebEngineClientCertificateOption6selectEv(
    QQuickWebEngineClientCertificateOption *self) {
  self->select();
}

//  QQuickWebEngineClientCertificateOption::QQuickWebEngineClientCertificateO
//      ption(QQuickWebEngineClientCertificateSelection *selection, int
//      index)
extern "C" Q_DECL_EXPORT
QQuickWebEngineClientCertificateOption *ritual_ZN38QQuickWebEngineClientCertificateOptionC1EP41QQuickWebEngineClientCertificateSelectioni(
    QQuickWebEngineClientCertificateSelection *selection,
    int index) {
  return new QQuickWebEngineClientCertificateOption(selection, index);
}
