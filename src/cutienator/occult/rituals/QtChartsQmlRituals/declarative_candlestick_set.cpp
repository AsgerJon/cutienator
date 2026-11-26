//  Written by dev_tooling.RitualGenerator from the records of
//  QtChartsQml/6.12.0/QtChartsQml/private/declarativecandlestickseries_p.h,
//  Qt 6.12.0.
//  Edited by hand on 2026-11-25: the header of 'DeclarativeAxes' is
//  included before Qt's header of the class, which only declares
//  'DeclarativeAxes' and then calls its functions inline, so the
//  compiler refused it as an incomplete type. Kept as it is when the
//  generator runs again.
#include <QtCharts/qchartglobal.h>
#include <QtChartsQml/qtchartsqmlexports.h>
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativechartglobal_p.h>
#if QT_CONFIG(charts_candlestick_chart)
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativechartglobal_p.h>
#include <QtChartsQml/QtChartsQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativeaxes_p.h>
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativecandlestickseries_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *DeclarativeCandlestickSet::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25DeclarativeCandlestickSet10metaObjectEv(
    const DeclarativeCandlestickSet *self) {
  return self->metaObject();
}

//  void *DeclarativeCandlestickSet::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN25DeclarativeCandlestickSet11qt_metacastEPKc(
    DeclarativeCandlestickSet *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  QString DeclarativeCandlestickSet::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25DeclarativeCandlestickSet2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(DeclarativeCandlestickSet::tr(s, c, n));
}

//  DeclarativeCandlestickSet::DeclarativeCandlestickSet(qreal timestamp,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
DeclarativeCandlestickSet *ritual_ZN25DeclarativeCandlestickSetC1EdP7QObject(
    qreal timestamp,
    QObject *parent) {
  return new DeclarativeCandlestickSet(timestamp, parent);
}

//  void DeclarativeCandlestickSet::setBrushFilename(const QString
//      &brushFilename)
extern "C" Q_DECL_EXPORT
void ritual_ZN25DeclarativeCandlestickSet16setBrushFilenameERK7QString(
    DeclarativeCandlestickSet *self,
    const QString *brushFilename) {
  self->setBrushFilename(*brushFilename);
}

//  QString DeclarativeCandlestickSet::brushFilename() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25DeclarativeCandlestickSet13brushFilenameEv(
    const DeclarativeCandlestickSet *self) {
  return new QString(self->brushFilename());
}

//  void DeclarativeCandlestickSet::handleBrushChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25DeclarativeCandlestickSet18handleBrushChangedEv(
    DeclarativeCandlestickSet *self) {
  self->handleBrushChanged();
}

#endif  // QT_CONFIG(charts_candlestick_chart)
