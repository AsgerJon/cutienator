//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/qboxplotmodelmapper_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCharts/qchartglobal.h>
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_boxplot_chart)
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_boxplot_chart)
#include <QtCharts/qboxplotmodelmapper.h>
#endif
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/qboxplotmodelmapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#if QT_CONFIG(itemmodel)
#include <QtCore/qabstractitemmodel.h>
#endif
#if QT_CONFIG(charts_boxplot_chart)
#include <QtCharts/qboxset.h>
#endif
#include <QtCore/qlist.h>

//  const QMetaObject *QBoxPlotModelMapperPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QBoxPlotModelMapperPrivate10metaObjectEv(
    const QBoxPlotModelMapperPrivate *self) {
  return self->metaObject();
}

//  void *QBoxPlotModelMapperPrivate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN26QBoxPlotModelMapperPrivate11qt_metacastEPKc(
    QBoxPlotModelMapperPrivate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QBoxPlotModelMapperPrivate::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN26QBoxPlotModelMapperPrivate11qt_metacallEN11QMetaObject4CallEiPPv(
    QBoxPlotModelMapperPrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QBoxPlotModelMapperPrivate::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QBoxPlotModelMapperPrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QBoxPlotModelMapperPrivate::tr(s, c, n));
}

//  QBoxPlotModelMapperPrivate::QBoxPlotModelMapperPrivate(QBoxPlotModelMappe
//      r *q)
extern "C" Q_DECL_EXPORT
QBoxPlotModelMapperPrivate *ritual_ZN26QBoxPlotModelMapperPrivateC1EP19QBoxPlotModelMapper(
    QBoxPlotModelMapper *q) {
  return new QBoxPlotModelMapperPrivate(q);
}

//  void QBoxPlotModelMapperPrivate::modelUpdated(QModelIndex topLeft,
//      QModelIndex bottomRight)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QBoxPlotModelMapperPrivate12modelUpdatedE11QModelIndexS0_(
    QBoxPlotModelMapperPrivate *self,
    const QModelIndex *topLeft,
    const QModelIndex *bottomRight) {
  self->modelUpdated(*topLeft, *bottomRight);
}

//  void QBoxPlotModelMapperPrivate::modelHeaderDataUpdated(Qt::Orientation
//      orientation, int first, int last)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QBoxPlotModelMapperPrivate22modelHeaderDataUpdatedEN2Qt11OrientationEii(
    QBoxPlotModelMapperPrivate *self,
    Qt::Orientation orientation,
    int first,
    int last) {
  self->modelHeaderDataUpdated(orientation, first, last);
}

//  void QBoxPlotModelMapperPrivate::modelRowsAdded(QModelIndex parent, int
//      start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QBoxPlotModelMapperPrivate14modelRowsAddedE11QModelIndexii(
    QBoxPlotModelMapperPrivate *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->modelRowsAdded(*parent, start, end);
}

//  void QBoxPlotModelMapperPrivate::modelRowsRemoved(QModelIndex parent, int
//      start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QBoxPlotModelMapperPrivate16modelRowsRemovedE11QModelIndexii(
    QBoxPlotModelMapperPrivate *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->modelRowsRemoved(*parent, start, end);
}

//  void QBoxPlotModelMapperPrivate::modelColumnsAdded(QModelIndex parent,
//      int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QBoxPlotModelMapperPrivate17modelColumnsAddedE11QModelIndexii(
    QBoxPlotModelMapperPrivate *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->modelColumnsAdded(*parent, start, end);
}

//  void QBoxPlotModelMapperPrivate::modelColumnsRemoved(QModelIndex parent,
//      int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QBoxPlotModelMapperPrivate19modelColumnsRemovedE11QModelIndexii(
    QBoxPlotModelMapperPrivate *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->modelColumnsRemoved(*parent, start, end);
}

//  void QBoxPlotModelMapperPrivate::handleModelDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QBoxPlotModelMapperPrivate20handleModelDestroyedEv(
    QBoxPlotModelMapperPrivate *self) {
  self->handleModelDestroyed();
}

//  void QBoxPlotModelMapperPrivate::boxSetsAdded(const QList<QBoxSet *>
//      &sets)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QBoxPlotModelMapperPrivate12boxSetsAddedERK5QListIP7QBoxSetE(
    QBoxPlotModelMapperPrivate *self,
    const QList<QBoxSet *> *sets) {
  self->boxSetsAdded(*sets);
}

//  void QBoxPlotModelMapperPrivate::boxSetsRemoved(const QList<QBoxSet *>
//      &sets)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QBoxPlotModelMapperPrivate14boxSetsRemovedERK5QListIP7QBoxSetE(
    QBoxPlotModelMapperPrivate *self,
    const QList<QBoxSet *> *sets) {
  self->boxSetsRemoved(*sets);
}

//  void QBoxPlotModelMapperPrivate::boxValueChanged(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QBoxPlotModelMapperPrivate15boxValueChangedEi(
    QBoxPlotModelMapperPrivate *self,
    int index) {
  self->boxValueChanged(index);
}

//  void QBoxPlotModelMapperPrivate::handleSeriesDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QBoxPlotModelMapperPrivate21handleSeriesDestroyedEv(
    QBoxPlotModelMapperPrivate *self) {
  self->handleSeriesDestroyed();
}

//  void QBoxPlotModelMapperPrivate::initializeBoxFromModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QBoxPlotModelMapperPrivate22initializeBoxFromModelEv(
    QBoxPlotModelMapperPrivate *self) {
  self->initializeBoxFromModel();
}

//  QBoxSet *QBoxPlotModelMapperPrivate::boxSet(QModelIndex index)
extern "C" Q_DECL_EXPORT
QBoxSet *ritual_ZN26QBoxPlotModelMapperPrivate6boxSetE11QModelIndex(
    QBoxPlotModelMapperPrivate *self,
    const QModelIndex *index) {
  return self->boxSet(*index);
}

//  QModelIndex QBoxPlotModelMapperPrivate::boxModelIndex(int boxSection, int
//      posInBox)
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZN26QBoxPlotModelMapperPrivate13boxModelIndexEii(
    QBoxPlotModelMapperPrivate *self,
    int boxSection,
    int posInBox) {
  return new QModelIndex(self->boxModelIndex(boxSection, posInBox));
}

//  void QBoxPlotModelMapperPrivate::insertData(int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QBoxPlotModelMapperPrivate10insertDataEii(
    QBoxPlotModelMapperPrivate *self,
    int start,
    int end) {
  self->insertData(start, end);
}

//  void QBoxPlotModelMapperPrivate::removeData(int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QBoxPlotModelMapperPrivate10removeDataEii(
    QBoxPlotModelMapperPrivate *self,
    int start,
    int end) {
  self->removeData(start, end);
}

//  void QBoxPlotModelMapperPrivate::blockModelSignals(bool block)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QBoxPlotModelMapperPrivate17blockModelSignalsEb(
    QBoxPlotModelMapperPrivate *self,
    bool block) {
  self->blockModelSignals(block);
}

//  void QBoxPlotModelMapperPrivate::blockSeriesSignals(bool block)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QBoxPlotModelMapperPrivate18blockSeriesSignalsEb(
    QBoxPlotModelMapperPrivate *self,
    bool block) {
  self->blockSeriesSignals(block);
}

//  QBoxPlotModelMapper *QBoxPlotModelMapperPrivate::q_func()
extern "C" Q_DECL_EXPORT
QBoxPlotModelMapper *ritual_ZN26QBoxPlotModelMapperPrivate6q_funcEv(
    QBoxPlotModelMapperPrivate *self) {
  return self->q_func();
}

//  const QBoxPlotModelMapper *QBoxPlotModelMapperPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QBoxPlotModelMapper *ritual_ZNK26QBoxPlotModelMapperPrivate6q_funcEv(
    const QBoxPlotModelMapperPrivate *self) {
  return self->q_func();
}

#endif  // QT_CONFIG(charts_boxplot_chart)
