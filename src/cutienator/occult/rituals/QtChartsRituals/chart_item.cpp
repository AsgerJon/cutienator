//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/chartitem_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/chartitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  const QMetaObject *ChartItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9ChartItem10metaObjectEv(
    const ChartItem *self) {
  return self->metaObject();
}

//  QString ChartItem::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9ChartItem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(ChartItem::tr(s, c, n));
}

//  AbstractDomain *ChartItem::domain() const
extern "C" Q_DECL_EXPORT
AbstractDomain *ritual_ZNK9ChartItem6domainEv(const ChartItem *self) {
  return self->domain();
}

//  void ChartItem::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN9ChartItem7cleanupEv(ChartItem *self) {
  self->cleanup();
}

//  QAbstractSeriesPrivate *ChartItem::seriesPrivate() const
extern "C" Q_DECL_EXPORT
QAbstractSeriesPrivate *ritual_ZNK9ChartItem13seriesPrivateEv(
    const ChartItem *self) {
  return self->seriesPrivate();
}

//  void ChartItem::handleDomainUpdated()
extern "C" Q_DECL_EXPORT
void ritual_ZN9ChartItem19handleDomainUpdatedEv(ChartItem *self) {
  self->handleDomainUpdated();
}

//  void ChartItem::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9ChartItem7cleanupEv(ChartItem *self) {
  self->ChartItem::cleanup();
}

//  void ChartItem::handleDomainUpdated()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9ChartItem19handleDomainUpdatedEv(ChartItem *self) {
  self->ChartItem::handleDomainUpdated();
}

//  QList<ChartItem *>::QList()
extern "C" Q_DECL_EXPORT
QList<ChartItem *> *ritual_list_make_ChartItem_ptr() {
  return new QList<ChartItem *>();
}

//  void QList<ChartItem *>::append(const ChartItem * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_ChartItem_ptr(
    QList<ChartItem *> *self,
    ChartItem *element) {
  self->append(element);
}

//  qsizetype QList<ChartItem *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_ChartItem_ptr(const QList<ChartItem *> *self) {
  return self->size();
}

//  const ChartItem * &QList<ChartItem *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
ChartItem *ritual_list_at_ChartItem_ptr(
    const QList<ChartItem *> *self,
    long long index) {
  return self->at(index);
}

//  QList<ChartItem *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_ChartItem_ptr(QList<ChartItem *> *self) {
  delete self;
}
