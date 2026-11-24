//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/qbarmodelmapper_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/qbarmodelmapper.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/qbarmodelmapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCharts/qbarset.h>
#include <QtCore/qlist.h>

//  const QMetaObject *QBarModelMapperPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QBarModelMapperPrivate10metaObjectEv(
    const QBarModelMapperPrivate *self) {
  return self->metaObject();
}

//  QString QBarModelMapperPrivate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QBarModelMapperPrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QBarModelMapperPrivate::tr(s, c, n));
}

//  QBarModelMapperPrivate::QBarModelMapperPrivate(QBarModelMapper *q)
extern "C" Q_DECL_EXPORT
QBarModelMapperPrivate *ritual_ZN22QBarModelMapperPrivateC1EP15QBarModelMapper(
    QBarModelMapper *q) {
  return new QBarModelMapperPrivate(q);
}

//  void QBarModelMapperPrivate::modelUpdated(QModelIndex topLeft,
//      QModelIndex bottomRight)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QBarModelMapperPrivate12modelUpdatedE11QModelIndexS0_(
    QBarModelMapperPrivate *self,
    const QModelIndex *topLeft,
    const QModelIndex *bottomRight) {
  self->modelUpdated(*topLeft, *bottomRight);
}

//  void QBarModelMapperPrivate::modelHeaderDataUpdated(Qt::Orientation
//      orientation, int first, int last)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QBarModelMapperPrivate22modelHeaderDataUpdatedEN2Qt11OrientationEii(
    QBarModelMapperPrivate *self,
    Qt::Orientation orientation,
    int first,
    int last) {
  self->modelHeaderDataUpdated(orientation, first, last);
}

//  void QBarModelMapperPrivate::modelRowsAdded(QModelIndex parent, int
//      start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QBarModelMapperPrivate14modelRowsAddedE11QModelIndexii(
    QBarModelMapperPrivate *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->modelRowsAdded(*parent, start, end);
}

//  void QBarModelMapperPrivate::modelRowsRemoved(QModelIndex parent, int
//      start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QBarModelMapperPrivate16modelRowsRemovedE11QModelIndexii(
    QBarModelMapperPrivate *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->modelRowsRemoved(*parent, start, end);
}

//  void QBarModelMapperPrivate::modelColumnsAdded(QModelIndex parent, int
//      start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QBarModelMapperPrivate17modelColumnsAddedE11QModelIndexii(
    QBarModelMapperPrivate *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->modelColumnsAdded(*parent, start, end);
}

//  void QBarModelMapperPrivate::modelColumnsRemoved(QModelIndex parent, int
//      start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QBarModelMapperPrivate19modelColumnsRemovedE11QModelIndexii(
    QBarModelMapperPrivate *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->modelColumnsRemoved(*parent, start, end);
}

//  void QBarModelMapperPrivate::handleModelDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QBarModelMapperPrivate20handleModelDestroyedEv(
    QBarModelMapperPrivate *self) {
  self->handleModelDestroyed();
}

//  void QBarModelMapperPrivate::barSetsAdded(const QList<QBarSet *> &sets)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QBarModelMapperPrivate12barSetsAddedERK5QListIP7QBarSetE(
    QBarModelMapperPrivate *self,
    const QList<QBarSet *> *sets) {
  self->barSetsAdded(*sets);
}

//  void QBarModelMapperPrivate::barSetsRemoved(const QList<QBarSet *> &sets)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QBarModelMapperPrivate14barSetsRemovedERK5QListIP7QBarSetE(
    QBarModelMapperPrivate *self,
    const QList<QBarSet *> *sets) {
  self->barSetsRemoved(*sets);
}

//  void QBarModelMapperPrivate::valuesAdded(int index, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QBarModelMapperPrivate11valuesAddedEii(
    QBarModelMapperPrivate *self,
    int index,
    int count) {
  self->valuesAdded(index, count);
}

//  void QBarModelMapperPrivate::valuesRemoved(int index, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QBarModelMapperPrivate13valuesRemovedEii(
    QBarModelMapperPrivate *self,
    int index,
    int count) {
  self->valuesRemoved(index, count);
}

//  void QBarModelMapperPrivate::barLabelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QBarModelMapperPrivate15barLabelChangedEv(
    QBarModelMapperPrivate *self) {
  self->barLabelChanged();
}

//  void QBarModelMapperPrivate::barValueChanged(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QBarModelMapperPrivate15barValueChangedEi(
    QBarModelMapperPrivate *self,
    int index) {
  self->barValueChanged(index);
}

//  void QBarModelMapperPrivate::handleSeriesDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QBarModelMapperPrivate21handleSeriesDestroyedEv(
    QBarModelMapperPrivate *self) {
  self->handleSeriesDestroyed();
}

//  void QBarModelMapperPrivate::initializeBarFromModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QBarModelMapperPrivate22initializeBarFromModelEv(
    QBarModelMapperPrivate *self) {
  self->initializeBarFromModel();
}

//  QBarSet *QBarModelMapperPrivate::barSet(QModelIndex index)
extern "C" Q_DECL_EXPORT
QBarSet *ritual_ZN22QBarModelMapperPrivate6barSetE11QModelIndex(
    QBarModelMapperPrivate *self,
    const QModelIndex *index) {
  return self->barSet(*index);
}

//  QModelIndex QBarModelMapperPrivate::barModelIndex(int barSection, int
//      posInBar)
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZN22QBarModelMapperPrivate13barModelIndexEii(
    QBarModelMapperPrivate *self,
    int barSection,
    int posInBar) {
  return new QModelIndex(self->barModelIndex(barSection, posInBar));
}

//  void QBarModelMapperPrivate::insertData(int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QBarModelMapperPrivate10insertDataEii(
    QBarModelMapperPrivate *self,
    int start,
    int end) {
  self->insertData(start, end);
}

//  void QBarModelMapperPrivate::removeData(int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QBarModelMapperPrivate10removeDataEii(
    QBarModelMapperPrivate *self,
    int start,
    int end) {
  self->removeData(start, end);
}

//  void QBarModelMapperPrivate::blockModelSignals(bool block)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QBarModelMapperPrivate17blockModelSignalsEb(
    QBarModelMapperPrivate *self,
    bool block) {
  self->blockModelSignals(block);
}

//  void QBarModelMapperPrivate::blockSeriesSignals(bool block)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QBarModelMapperPrivate18blockSeriesSignalsEb(
    QBarModelMapperPrivate *self,
    bool block) {
  self->blockSeriesSignals(block);
}

//  QBarModelMapper *QBarModelMapperPrivate::q_func()
extern "C" Q_DECL_EXPORT
QBarModelMapper *ritual_ZN22QBarModelMapperPrivate6q_funcEv(
    QBarModelMapperPrivate *self) {
  return self->q_func();
}

//  const QBarModelMapper *QBarModelMapperPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QBarModelMapper *ritual_ZNK22QBarModelMapperPrivate6q_funcEv(
    const QBarModelMapperPrivate *self) {
  return self->q_func();
}
