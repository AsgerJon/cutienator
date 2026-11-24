//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/qcandlestickmodelmapper_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/qcandlestickmodelmapper.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/qcandlestickmodelmapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCharts/qcandlestickset.h>
#include <QtCore/qlist.h>

//  const QMetaObject *QCandlestickModelMapperPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK30QCandlestickModelMapperPrivate10metaObjectEv(
    const QCandlestickModelMapperPrivate *self) {
  return self->metaObject();
}

//  QString QCandlestickModelMapperPrivate::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN30QCandlestickModelMapperPrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QCandlestickModelMapperPrivate::tr(s, c, n));
}

//  QCandlestickModelMapperPrivate::QCandlestickModelMapperPrivate(QCandlesti
//      ckModelMapper *q)
extern "C" Q_DECL_EXPORT
QCandlestickModelMapperPrivate *ritual_ZN30QCandlestickModelMapperPrivateC1EP23QCandlestickModelMapper(
    QCandlestickModelMapper *q) {
  return new QCandlestickModelMapperPrivate(q);
}

//  void QCandlestickModelMapperPrivate::initializeCandlestickFromModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QCandlestickModelMapperPrivate30initializeCandlestickFromModelEv(
    QCandlestickModelMapperPrivate *self) {
  self->initializeCandlestickFromModel();
}

//  void QCandlestickModelMapperPrivate::modelDataUpdated(QModelIndex
//      topLeft, QModelIndex bottomRight)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QCandlestickModelMapperPrivate16modelDataUpdatedE11QModelIndexS0_(
    QCandlestickModelMapperPrivate *self,
    const QModelIndex *topLeft,
    const QModelIndex *bottomRight) {
  self->modelDataUpdated(*topLeft, *bottomRight);
}

//  void
//      QCandlestickModelMapperPrivate::modelHeaderDataUpdated(Qt::Orientatio
//      n orientation, int first, int last)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QCandlestickModelMapperPrivate22modelHeaderDataUpdatedEN2Qt11OrientationEii(
    QCandlestickModelMapperPrivate *self,
    Qt::Orientation orientation,
    int first,
    int last) {
  self->modelHeaderDataUpdated(orientation, first, last);
}

//  void QCandlestickModelMapperPrivate::modelRowsInserted(QModelIndex
//      parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QCandlestickModelMapperPrivate17modelRowsInsertedE11QModelIndexii(
    QCandlestickModelMapperPrivate *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->modelRowsInserted(*parent, start, end);
}

//  void QCandlestickModelMapperPrivate::modelRowsRemoved(QModelIndex parent,
//      int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QCandlestickModelMapperPrivate16modelRowsRemovedE11QModelIndexii(
    QCandlestickModelMapperPrivate *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->modelRowsRemoved(*parent, start, end);
}

//  void QCandlestickModelMapperPrivate::modelColumnsInserted(QModelIndex
//      parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QCandlestickModelMapperPrivate20modelColumnsInsertedE11QModelIndexii(
    QCandlestickModelMapperPrivate *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->modelColumnsInserted(*parent, start, end);
}

//  void QCandlestickModelMapperPrivate::modelColumnsRemoved(QModelIndex
//      parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QCandlestickModelMapperPrivate19modelColumnsRemovedE11QModelIndexii(
    QCandlestickModelMapperPrivate *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->modelColumnsRemoved(*parent, start, end);
}

//  void QCandlestickModelMapperPrivate::modelDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QCandlestickModelMapperPrivate14modelDestroyedEv(
    QCandlestickModelMapperPrivate *self) {
  self->modelDestroyed();
}

//  void QCandlestickModelMapperPrivate::candlestickSetsAdded(const
//      QList<QCandlestickSet *> &sets)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QCandlestickModelMapperPrivate20candlestickSetsAddedERK5QListIP15QCandlestickSetE(
    QCandlestickModelMapperPrivate *self,
    const QList<QCandlestickSet *> *sets) {
  self->candlestickSetsAdded(*sets);
}

//  void QCandlestickModelMapperPrivate::candlestickSetsRemoved(const
//      QList<QCandlestickSet *> &sets)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QCandlestickModelMapperPrivate22candlestickSetsRemovedERK5QListIP15QCandlestickSetE(
    QCandlestickModelMapperPrivate *self,
    const QList<QCandlestickSet *> *sets) {
  self->candlestickSetsRemoved(*sets);
}

//  void QCandlestickModelMapperPrivate::candlestickSetChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QCandlestickModelMapperPrivate21candlestickSetChangedEv(
    QCandlestickModelMapperPrivate *self) {
  self->candlestickSetChanged();
}

//  void QCandlestickModelMapperPrivate::seriesDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QCandlestickModelMapperPrivate15seriesDestroyedEv(
    QCandlestickModelMapperPrivate *self) {
  self->seriesDestroyed();
}

//  QCandlestickSet
//      *QCandlestickModelMapperPrivate::candlestickSet(QModelIndex index)
extern "C" Q_DECL_EXPORT
QCandlestickSet *ritual_ZN30QCandlestickModelMapperPrivate14candlestickSetE11QModelIndex(
    QCandlestickModelMapperPrivate *self,
    const QModelIndex *index) {
  return self->candlestickSet(*index);
}

//  QModelIndex QCandlestickModelMapperPrivate::candlestickModelIndex(int
//      section, int pos)
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZN30QCandlestickModelMapperPrivate21candlestickModelIndexEii(
    QCandlestickModelMapperPrivate *self,
    int section,
    int pos) {
  return new QModelIndex(self->candlestickModelIndex(section, pos));
}

//  void QCandlestickModelMapperPrivate::insertData(int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QCandlestickModelMapperPrivate10insertDataEii(
    QCandlestickModelMapperPrivate *self,
    int start,
    int end) {
  self->insertData(start, end);
}

//  void QCandlestickModelMapperPrivate::removeData(int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QCandlestickModelMapperPrivate10removeDataEii(
    QCandlestickModelMapperPrivate *self,
    int start,
    int end) {
  self->removeData(start, end);
}

//  void QCandlestickModelMapperPrivate::blockModelSignals(bool block)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QCandlestickModelMapperPrivate17blockModelSignalsEb(
    QCandlestickModelMapperPrivate *self,
    bool block) {
  self->blockModelSignals(block);
}

//  void QCandlestickModelMapperPrivate::blockSeriesSignals(bool block)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QCandlestickModelMapperPrivate18blockSeriesSignalsEb(
    QCandlestickModelMapperPrivate *self,
    bool block) {
  self->blockSeriesSignals(block);
}

//  QCandlestickModelMapper *QCandlestickModelMapperPrivate::q_func()
extern "C" Q_DECL_EXPORT
QCandlestickModelMapper *ritual_ZN30QCandlestickModelMapperPrivate6q_funcEv(
    QCandlestickModelMapperPrivate *self) {
  return self->q_func();
}

//  const QCandlestickModelMapper *QCandlestickModelMapperPrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const QCandlestickModelMapper *ritual_ZNK30QCandlestickModelMapperPrivate6q_funcEv(
    const QCandlestickModelMapperPrivate *self) {
  return self->q_func();
}
