//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/qpiemodelmapper_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCharts/qchartglobal.h>
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_pie_chart)
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/qpiemodelmapper.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/qpiemodelmapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCharts/qpieslice.h>
#include <QtCore/qlist.h>

//  const QMetaObject *QPieModelMapperPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QPieModelMapperPrivate10metaObjectEv(
    const QPieModelMapperPrivate *self) {
  return self->metaObject();
}

//  QString QPieModelMapperPrivate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QPieModelMapperPrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPieModelMapperPrivate::tr(s, c, n));
}

//  QPieModelMapperPrivate::QPieModelMapperPrivate(QPieModelMapper *q)
extern "C" Q_DECL_EXPORT
QPieModelMapperPrivate *ritual_ZN22QPieModelMapperPrivateC1EP15QPieModelMapper(
    QPieModelMapper *q) {
  return new QPieModelMapperPrivate(q);
}

//  void QPieModelMapperPrivate::modelUpdated(QModelIndex topLeft,
//      QModelIndex bottomRight)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPieModelMapperPrivate12modelUpdatedE11QModelIndexS0_(
    QPieModelMapperPrivate *self,
    const QModelIndex *topLeft,
    const QModelIndex *bottomRight) {
  self->modelUpdated(*topLeft, *bottomRight);
}

//  void QPieModelMapperPrivate::modelRowsAdded(QModelIndex parent, int
//      start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPieModelMapperPrivate14modelRowsAddedE11QModelIndexii(
    QPieModelMapperPrivate *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->modelRowsAdded(*parent, start, end);
}

//  void QPieModelMapperPrivate::modelRowsRemoved(QModelIndex parent, int
//      start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPieModelMapperPrivate16modelRowsRemovedE11QModelIndexii(
    QPieModelMapperPrivate *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->modelRowsRemoved(*parent, start, end);
}

//  void QPieModelMapperPrivate::modelColumnsAdded(QModelIndex parent, int
//      start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPieModelMapperPrivate17modelColumnsAddedE11QModelIndexii(
    QPieModelMapperPrivate *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->modelColumnsAdded(*parent, start, end);
}

//  void QPieModelMapperPrivate::modelColumnsRemoved(QModelIndex parent, int
//      start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPieModelMapperPrivate19modelColumnsRemovedE11QModelIndexii(
    QPieModelMapperPrivate *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->modelColumnsRemoved(*parent, start, end);
}

//  void QPieModelMapperPrivate::handleModelDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPieModelMapperPrivate20handleModelDestroyedEv(
    QPieModelMapperPrivate *self) {
  self->handleModelDestroyed();
}

//  void QPieModelMapperPrivate::slicesAdded(const QList<QPieSlice *>
//      &slices)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPieModelMapperPrivate11slicesAddedERK5QListIP9QPieSliceE(
    QPieModelMapperPrivate *self,
    const QList<QPieSlice *> *slices) {
  self->slicesAdded(*slices);
}

//  void QPieModelMapperPrivate::slicesRemoved(const QList<QPieSlice *>
//      &slices)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPieModelMapperPrivate13slicesRemovedERK5QListIP9QPieSliceE(
    QPieModelMapperPrivate *self,
    const QList<QPieSlice *> *slices) {
  self->slicesRemoved(*slices);
}

//  void QPieModelMapperPrivate::sliceLabelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPieModelMapperPrivate17sliceLabelChangedEv(
    QPieModelMapperPrivate *self) {
  self->sliceLabelChanged();
}

//  void QPieModelMapperPrivate::sliceValueChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPieModelMapperPrivate17sliceValueChangedEv(
    QPieModelMapperPrivate *self) {
  self->sliceValueChanged();
}

//  void QPieModelMapperPrivate::handleSeriesDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPieModelMapperPrivate21handleSeriesDestroyedEv(
    QPieModelMapperPrivate *self) {
  self->handleSeriesDestroyed();
}

//  void QPieModelMapperPrivate::initializePieFromModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPieModelMapperPrivate22initializePieFromModelEv(
    QPieModelMapperPrivate *self) {
  self->initializePieFromModel();
}

//  QPieSlice *QPieModelMapperPrivate::pieSlice(QModelIndex index) const
extern "C" Q_DECL_EXPORT
QPieSlice *ritual_ZNK22QPieModelMapperPrivate8pieSliceE11QModelIndex(
    const QPieModelMapperPrivate *self,
    const QModelIndex *index) {
  return self->pieSlice(*index);
}

//  bool QPieModelMapperPrivate::isLabelIndex(QModelIndex index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QPieModelMapperPrivate12isLabelIndexE11QModelIndex(
    const QPieModelMapperPrivate *self,
    const QModelIndex *index) {
  return self->isLabelIndex(*index);
}

//  bool QPieModelMapperPrivate::isValueIndex(QModelIndex index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QPieModelMapperPrivate12isValueIndexE11QModelIndex(
    const QPieModelMapperPrivate *self,
    const QModelIndex *index) {
  return self->isValueIndex(*index);
}

//  QModelIndex QPieModelMapperPrivate::valueModelIndex(int slicePos)
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZN22QPieModelMapperPrivate15valueModelIndexEi(
    QPieModelMapperPrivate *self,
    int slicePos) {
  return new QModelIndex(self->valueModelIndex(slicePos));
}

//  QModelIndex QPieModelMapperPrivate::labelModelIndex(int slicePos)
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZN22QPieModelMapperPrivate15labelModelIndexEi(
    QPieModelMapperPrivate *self,
    int slicePos) {
  return new QModelIndex(self->labelModelIndex(slicePos));
}

//  void QPieModelMapperPrivate::insertData(int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPieModelMapperPrivate10insertDataEii(
    QPieModelMapperPrivate *self,
    int start,
    int end) {
  self->insertData(start, end);
}

//  void QPieModelMapperPrivate::removeData(int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPieModelMapperPrivate10removeDataEii(
    QPieModelMapperPrivate *self,
    int start,
    int end) {
  self->removeData(start, end);
}

//  void QPieModelMapperPrivate::blockModelSignals(bool block)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPieModelMapperPrivate17blockModelSignalsEb(
    QPieModelMapperPrivate *self,
    bool block) {
  self->blockModelSignals(block);
}

//  void QPieModelMapperPrivate::blockSeriesSignals(bool block)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPieModelMapperPrivate18blockSeriesSignalsEb(
    QPieModelMapperPrivate *self,
    bool block) {
  self->blockSeriesSignals(block);
}

//  QPieModelMapper *QPieModelMapperPrivate::q_func()
extern "C" Q_DECL_EXPORT
QPieModelMapper *ritual_ZN22QPieModelMapperPrivate6q_funcEv(
    QPieModelMapperPrivate *self) {
  return self->q_func();
}

//  const QPieModelMapper *QPieModelMapperPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QPieModelMapper *ritual_ZNK22QPieModelMapperPrivate6q_funcEv(
    const QPieModelMapperPrivate *self) {
  return self->q_func();
}

#endif  // QT_CONFIG(charts_pie_chart)
