//  Written by dev_tooling.RitualGenerator from the records of
//  QtChartsQml/6.12.0/QtChartsQml/private/declarativecategoryaxis_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativechartglobal_p.h>
#include <QtChartsQml/QtChartsQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativecategoryaxis_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *DeclarativeCategoryRange::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24DeclarativeCategoryRange10metaObjectEv(
    const DeclarativeCategoryRange *self) {
  return self->metaObject();
}

//  void *DeclarativeCategoryRange::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24DeclarativeCategoryRange11qt_metacastEPKc(
    DeclarativeCategoryRange *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int DeclarativeCategoryRange::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN24DeclarativeCategoryRange11qt_metacallEN11QMetaObject4CallEiPPv(
    DeclarativeCategoryRange *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString DeclarativeCategoryRange::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24DeclarativeCategoryRange2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(DeclarativeCategoryRange::tr(s, c, n));
}

//  DeclarativeCategoryRange::DeclarativeCategoryRange(QObject *parent)
extern "C" Q_DECL_EXPORT
DeclarativeCategoryRange *ritual_ZN24DeclarativeCategoryRangeC1EP7QObject(
    QObject *parent) {
  return new DeclarativeCategoryRange(parent);
}

//  qreal DeclarativeCategoryRange::endValue()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN24DeclarativeCategoryRange8endValueEv(
    DeclarativeCategoryRange *self) {
  return self->endValue();
}

//  void DeclarativeCategoryRange::setEndValue(qreal endValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN24DeclarativeCategoryRange11setEndValueEd(
    DeclarativeCategoryRange *self,
    qreal endValue) {
  self->setEndValue(endValue);
}

//  QString DeclarativeCategoryRange::label()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24DeclarativeCategoryRange5labelEv(
    DeclarativeCategoryRange *self) {
  return new QString(self->label());
}

//  void DeclarativeCategoryRange::setLabel(const QString &label)
extern "C" Q_DECL_EXPORT
void ritual_ZN24DeclarativeCategoryRange8setLabelERK7QString(
    DeclarativeCategoryRange *self,
    const QString *label) {
  self->setLabel(*label);
}
