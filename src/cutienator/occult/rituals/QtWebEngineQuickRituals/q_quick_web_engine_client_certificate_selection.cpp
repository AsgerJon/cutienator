//  Written by dev_tooling.RitualGenerator from the records of QtWebEngineQui
//  ck/6.12.0/QtWebEngineQuick/private/qquickwebengineclientcertificateselect
//  ion_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qtwebenginequickglobal_p.h>
#include <QtWebEngineQuick/QtWebEngineQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebengineclientcertificateselection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtQml/QQmlListProperty>
#include <QtCore/QSharedPointer>
#include <QtWebEngineCore/QtWebEngineCore>

//  const QMetaObject
//      *QQuickWebEngineClientCertificateSelection::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK41QQuickWebEngineClientCertificateSelection10metaObjectEv(
    const QQuickWebEngineClientCertificateSelection *self) {
  return self->metaObject();
}

//  void *QQuickWebEngineClientCertificateSelection::qt_metacast(const char
//      *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN41QQuickWebEngineClientCertificateSelection11qt_metacastEPKc(
    QQuickWebEngineClientCertificateSelection *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int
//      QQuickWebEngineClientCertificateSelection::qt_metacall(QMetaObject::C
//      all a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN41QQuickWebEngineClientCertificateSelection11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickWebEngineClientCertificateSelection *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickWebEngineClientCertificateSelection::tr(const char *s,
//      const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN41QQuickWebEngineClientCertificateSelection2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickWebEngineClientCertificateSelection::tr(s, c, n));
}

//  void
//      QQuickWebEngineClientCertificateSelection::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN41QQuickWebEngineClientCertificateSelection24qt_qmlMarker_uncreatableEv(
    QQuickWebEngineClientCertificateSelection *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuickWebEngineClientCertificateSelection::QQuickWebEngineClientCertifica
//      teSelection()
extern "C" Q_DECL_EXPORT
QQuickWebEngineClientCertificateSelection *ritual_ZN41QQuickWebEngineClientCertificateSelectionC1Ev() {
  return new QQuickWebEngineClientCertificateSelection();
}

//  QUrl QQuickWebEngineClientCertificateSelection::host() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK41QQuickWebEngineClientCertificateSelection4hostEv(
    const QQuickWebEngineClientCertificateSelection *self) {
  return new QUrl(self->host());
}

//  void QQuickWebEngineClientCertificateSelection::select(int idx)
extern "C" Q_DECL_EXPORT
void ritual_ZN41QQuickWebEngineClientCertificateSelection6selectEi(
    QQuickWebEngineClientCertificateSelection *self,
    int idx) {
  self->select(idx);
}

//  void QQuickWebEngineClientCertificateSelection::select(const
//      QQuickWebEngineClientCertificateOption *certificate)
extern "C" Q_DECL_EXPORT
void ritual_ZN41QQuickWebEngineClientCertificateSelection6selectEPK38QQuickWebEngineClientCertificateOption(
    QQuickWebEngineClientCertificateSelection *self,
    const QQuickWebEngineClientCertificateOption *certificate) {
  self->select(certificate);
}

//  void QQuickWebEngineClientCertificateSelection::selectNone()
extern "C" Q_DECL_EXPORT
void ritual_ZN41QQuickWebEngineClientCertificateSelection10selectNoneEv(
    QQuickWebEngineClientCertificateSelection *self) {
  self->selectNone();
}

//  QQmlListProperty<QQuickWebEngineClientCertificateOption>
//      QQuickWebEngineClientCertificateSelection::certificates()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QQuickWebEngineClientCertificateOption> *ritual_ZN41QQuickWebEngineClientCertificateSelection12certificatesEv(
    QQuickWebEngineClientCertificateSelection *self) {
  return new QQmlListProperty<QQuickWebEngineClientCertificateOption>(
      self->certificates());
}

//  qsizetype QQuickWebEngineClientCertificateSelection::certificates_count(Q
//      QmlListProperty<QQuickWebEngineClientCertificateOption> *p)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN41QQuickWebEngineClientCertificateSelection18certificates_countEP16QQmlListPropertyI38QQuickWebEngineClientCertificateOptionE(
    QQmlListProperty<QQuickWebEngineClientCertificateOption> *p) {
  return QQuickWebEngineClientCertificateSelection::certificates_count(p);
}

//  QQuickWebEngineClientCertificateOption *QQuickWebEngineClientCertificateS
//      election::certificates_at(QQmlListProperty<QQuickWebEngineClientCerti
//      ficateOption> *p, qsizetype idx)
extern "C" Q_DECL_EXPORT
QQuickWebEngineClientCertificateOption *ritual_ZN41QQuickWebEngineClientCertificateSelection15certificates_atEP16QQmlListPropertyI38QQuickWebEngineClientCertificateOptionEx(
    QQmlListProperty<QQuickWebEngineClientCertificateOption> *p,
    qsizetype idx) {
  return QQuickWebEngineClientCertificateSelection::certificates_at(p, idx);
}

//  QQuickWebEngineClientCertificateSelection::QQuickWebEngineClientCertifica
//      teSelection(QSharedPointer<QtWebEngineCore::ClientCertSelectControlle
//      r> a0)
extern "C" Q_DECL_EXPORT
QQuickWebEngineClientCertificateSelection *ritual_ZN41QQuickWebEngineClientCertificateSelectionC1E14QSharedPointerIN15QtWebEngineCore26ClientCertSelectControllerEE(
    const QSharedPointer<QtWebEngineCore::ClientCertSelectController> *a0) {
  return new QQuickWebEngineClientCertificateSelection(*a0);
}

//  a QQmlListProperty<QQuickWebEngineClientCertificateOption> a ritual of
//      QQuickWebEngineClientCertificateSelection gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickWebEngineClientCertificateSelection__QQmlListProperty_QQuickWebEngineClientCertificateOption(
    QQmlListProperty<QQuickWebEngineClientCertificateOption> *self) {
  delete self;
}
