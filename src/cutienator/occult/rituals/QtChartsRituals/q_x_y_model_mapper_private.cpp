//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/qxymodelmapper_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/qxymodelmapper.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/qxymodelmapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>

//  const QMetaObject *QXYModelMapperPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QXYModelMapperPrivate10metaObjectEv(
    const QXYModelMapperPrivate *self) {
  return self->metaObject();
}

//  QString QXYModelMapperPrivate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QXYModelMapperPrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QXYModelMapperPrivate::tr(s, c, n));
}

//  QXYModelMapperPrivate::QXYModelMapperPrivate(QXYModelMapper *q)
extern "C" Q_DECL_EXPORT
QXYModelMapperPrivate *ritual_ZN21QXYModelMapperPrivateC1EP14QXYModelMapper(
    QXYModelMapper *q) {
  return new QXYModelMapperPrivate(q);
}

//  void QXYModelMapperPrivate::modelUpdated(QModelIndex topLeft, QModelIndex
//      bottomRight)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QXYModelMapperPrivate12modelUpdatedE11QModelIndexS0_(
    QXYModelMapperPrivate *self,
    const QModelIndex *topLeft,
    const QModelIndex *bottomRight) {
  self->modelUpdated(*topLeft, *bottomRight);
}

//  void QXYModelMapperPrivate::modelRowsAdded(QModelIndex parent, int start,
//      int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QXYModelMapperPrivate14modelRowsAddedE11QModelIndexii(
    QXYModelMapperPrivate *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->modelRowsAdded(*parent, start, end);
}

//  void QXYModelMapperPrivate::modelRowsRemoved(QModelIndex parent, int
//      start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QXYModelMapperPrivate16modelRowsRemovedE11QModelIndexii(
    QXYModelMapperPrivate *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->modelRowsRemoved(*parent, start, end);
}

//  void QXYModelMapperPrivate::modelColumnsAdded(QModelIndex parent, int
//      start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QXYModelMapperPrivate17modelColumnsAddedE11QModelIndexii(
    QXYModelMapperPrivate *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->modelColumnsAdded(*parent, start, end);
}

//  void QXYModelMapperPrivate::modelColumnsRemoved(QModelIndex parent, int
//      start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QXYModelMapperPrivate19modelColumnsRemovedE11QModelIndexii(
    QXYModelMapperPrivate *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->modelColumnsRemoved(*parent, start, end);
}

//  void QXYModelMapperPrivate::handleModelDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QXYModelMapperPrivate20handleModelDestroyedEv(
    QXYModelMapperPrivate *self) {
  self->handleModelDestroyed();
}

//  void QXYModelMapperPrivate::handlePointAdded(int pointPos)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QXYModelMapperPrivate16handlePointAddedEi(
    QXYModelMapperPrivate *self,
    int pointPos) {
  self->handlePointAdded(pointPos);
}

//  void QXYModelMapperPrivate::handlePointRemoved(int pointPos)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QXYModelMapperPrivate18handlePointRemovedEi(
    QXYModelMapperPrivate *self,
    int pointPos) {
  self->handlePointRemoved(pointPos);
}

//  void QXYModelMapperPrivate::handlePointsRemoved(int pointPos, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QXYModelMapperPrivate19handlePointsRemovedEii(
    QXYModelMapperPrivate *self,
    int pointPos,
    int count) {
  self->handlePointsRemoved(pointPos, count);
}

//  void QXYModelMapperPrivate::handlePointReplaced(int pointPos)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QXYModelMapperPrivate19handlePointReplacedEi(
    QXYModelMapperPrivate *self,
    int pointPos) {
  self->handlePointReplaced(pointPos);
}

//  void QXYModelMapperPrivate::handleSeriesDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QXYModelMapperPrivate21handleSeriesDestroyedEv(
    QXYModelMapperPrivate *self) {
  self->handleSeriesDestroyed();
}

//  void QXYModelMapperPrivate::initializeXYFromModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QXYModelMapperPrivate21initializeXYFromModelEv(
    QXYModelMapperPrivate *self) {
  self->initializeXYFromModel();
}

//  QModelIndex QXYModelMapperPrivate::xModelIndex(int xPos)
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZN21QXYModelMapperPrivate11xModelIndexEi(
    QXYModelMapperPrivate *self,
    int xPos) {
  return new QModelIndex(self->xModelIndex(xPos));
}

//  QModelIndex QXYModelMapperPrivate::yModelIndex(int yPos)
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZN21QXYModelMapperPrivate11yModelIndexEi(
    QXYModelMapperPrivate *self,
    int yPos) {
  return new QModelIndex(self->yModelIndex(yPos));
}

//  void QXYModelMapperPrivate::insertData(int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QXYModelMapperPrivate10insertDataEii(
    QXYModelMapperPrivate *self,
    int start,
    int end) {
  self->insertData(start, end);
}

//  void QXYModelMapperPrivate::removeData(int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QXYModelMapperPrivate10removeDataEii(
    QXYModelMapperPrivate *self,
    int start,
    int end) {
  self->removeData(start, end);
}

//  void QXYModelMapperPrivate::blockModelSignals(bool block)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QXYModelMapperPrivate17blockModelSignalsEb(
    QXYModelMapperPrivate *self,
    bool block) {
  self->blockModelSignals(block);
}

//  void QXYModelMapperPrivate::blockSeriesSignals(bool block)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QXYModelMapperPrivate18blockSeriesSignalsEb(
    QXYModelMapperPrivate *self,
    bool block) {
  self->blockSeriesSignals(block);
}

//  qreal QXYModelMapperPrivate::valueFromModel(QModelIndex index)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN21QXYModelMapperPrivate14valueFromModelE11QModelIndex(
    QXYModelMapperPrivate *self,
    const QModelIndex *index) {
  return self->valueFromModel(*index);
}

//  void QXYModelMapperPrivate::setValueToModel(QModelIndex index, qreal
//      value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QXYModelMapperPrivate15setValueToModelE11QModelIndexd(
    QXYModelMapperPrivate *self,
    const QModelIndex *index,
    qreal value) {
  self->setValueToModel(*index, value);
}

//  QXYModelMapper *QXYModelMapperPrivate::q_func()
extern "C" Q_DECL_EXPORT
QXYModelMapper *ritual_ZN21QXYModelMapperPrivate6q_funcEv(
    QXYModelMapperPrivate *self) {
  return self->q_func();
}

//  const QXYModelMapper *QXYModelMapperPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QXYModelMapper *ritual_ZNK21QXYModelMapperPrivate6q_funcEv(
    const QXYModelMapperPrivate *self) {
  return self->q_func();
}
