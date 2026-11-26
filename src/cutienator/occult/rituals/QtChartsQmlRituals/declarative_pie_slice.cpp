//  Written by dev_tooling.RitualGenerator from the records of
//  QtChartsQml/6.12.0/QtChartsQml/private/declarativepieseries_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCharts/qchartglobal.h>
#include <QtChartsQml/qtchartsqmlexports.h>
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativechartglobal_p.h>
#if QT_CONFIG(charts_pie_chart)
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativechartglobal_p.h>
#include <QtChartsQml/QtChartsQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativepieseries_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *DeclarativePieSlice::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19DeclarativePieSlice10metaObjectEv(
    const DeclarativePieSlice *self) {
  return self->metaObject();
}

//  void *DeclarativePieSlice::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19DeclarativePieSlice11qt_metacastEPKc(
    DeclarativePieSlice *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int DeclarativePieSlice::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19DeclarativePieSlice11qt_metacallEN11QMetaObject4CallEiPPv(
    DeclarativePieSlice *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString DeclarativePieSlice::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19DeclarativePieSlice2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(DeclarativePieSlice::tr(s, c, n));
}

//  DeclarativePieSlice::DeclarativePieSlice(QObject *parent)
extern "C" Q_DECL_EXPORT
DeclarativePieSlice *ritual_ZN19DeclarativePieSliceC1EP7QObject(
    QObject *parent) {
  return new DeclarativePieSlice(parent);
}

//  QString DeclarativePieSlice::brushFilename() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19DeclarativePieSlice13brushFilenameEv(
    const DeclarativePieSlice *self) {
  return new QString(self->brushFilename());
}

//  void DeclarativePieSlice::setBrushFilename(const QString &brushFilename)
extern "C" Q_DECL_EXPORT
void ritual_ZN19DeclarativePieSlice16setBrushFilenameERK7QString(
    DeclarativePieSlice *self,
    const QString *brushFilename) {
  self->setBrushFilename(*brushFilename);
}

//  void DeclarativePieSlice::brushFilenameChanged(const QString
//      &brushFilename)
extern "C" Q_DECL_EXPORT
void ritual_ZN19DeclarativePieSlice20brushFilenameChangedERK7QString(
    DeclarativePieSlice *self,
    const QString *brushFilename) {
  self->brushFilenameChanged(*brushFilename);
}

//  void DeclarativePieSlice::handleBrushChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19DeclarativePieSlice18handleBrushChangedEv(
    DeclarativePieSlice *self) {
  self->handleBrushChanged();
}

#endif  // QT_CONFIG(charts_pie_chart)
