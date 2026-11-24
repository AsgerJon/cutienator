//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qscrollerproperties.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(scroller)
#include <QtWidgets/qscrollerproperties.h>
#include <QtCore/qvariant.h>

//  QScrollerProperties::QScrollerProperties()
extern "C" Q_DECL_EXPORT
QScrollerProperties *ritual_ZN19QScrollerPropertiesC1Ev() {
  return new QScrollerProperties();
}

//  QScrollerProperties::QScrollerProperties(const QScrollerProperties &sp)
extern "C" Q_DECL_EXPORT
QScrollerProperties *ritual_ZN19QScrollerPropertiesC1ERKS_(
    const QScrollerProperties *sp) {
  return new QScrollerProperties(*sp);
}

//  QScrollerProperties::~QScrollerProperties()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QScrollerPropertiesD1Ev(QScrollerProperties *self) {
  delete self;
}

//  bool QScrollerProperties::operator==(const QScrollerProperties &sp) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QScrollerPropertieseqERKS_(
    const QScrollerProperties *self,
    const QScrollerProperties *sp) {
  return self->operator==(*sp);
}

//  bool QScrollerProperties::operator!=(const QScrollerProperties &sp) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QScrollerPropertiesneERKS_(
    const QScrollerProperties *self,
    const QScrollerProperties *sp) {
  return self->operator!=(*sp);
}

//  void QScrollerProperties::setDefaultScrollerProperties(const
//      QScrollerProperties &sp)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QScrollerProperties28setDefaultScrollerPropertiesERKS_(
    const QScrollerProperties *sp) {
  QScrollerProperties::setDefaultScrollerProperties(*sp);
}

//  void QScrollerProperties::unsetDefaultScrollerProperties()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QScrollerProperties30unsetDefaultScrollerPropertiesEv() {
  QScrollerProperties::unsetDefaultScrollerProperties();
}

//  QVariant QScrollerProperties::scrollMetric(ScrollMetric metric) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK19QScrollerProperties12scrollMetricENS_12ScrollMetricE(
    const QScrollerProperties *self,
    QScrollerProperties::ScrollMetric metric) {
  return new QVariant(self->scrollMetric(metric));
}

//  void QScrollerProperties::setScrollMetric(ScrollMetric metric, const
//      QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QScrollerProperties15setScrollMetricENS_12ScrollMetricERK8QVariant(
    QScrollerProperties *self,
    QScrollerProperties::ScrollMetric metric,
    const QVariant *value) {
  self->setScrollMetric(metric, *value);
}

#endif  // QT_CONFIG(scroller)
