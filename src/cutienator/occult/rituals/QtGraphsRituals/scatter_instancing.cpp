//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/scatterinstancing_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_scatter3d))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/scatterinstancing_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>

//  const QMetaObject *ScatterInstancing::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17ScatterInstancing10metaObjectEv(
    const ScatterInstancing *self) {
  return self->metaObject();
}

//  QString ScatterInstancing::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17ScatterInstancing2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(ScatterInstancing::tr(s, c, n));
}

//  ScatterInstancing::ScatterInstancing()
extern "C" Q_DECL_EXPORT
ScatterInstancing *ritual_ZN17ScatterInstancingC1Ev() {
  return new ScatterInstancing();
}

//  const QList<DataItemHolder> &ScatterInstancing::dataArray() const
extern "C" Q_DECL_EXPORT
QList<DataItemHolder> *ritual_ZNK17ScatterInstancing9dataArrayEv(
    const ScatterInstancing *self) {
  return new QList<DataItemHolder>(self->dataArray());
}

//  void ScatterInstancing::setDataArray(const QList<DataItemHolder>
//      &newDataArray)
extern "C" Q_DECL_EXPORT
void ritual_ZN17ScatterInstancing12setDataArrayERK5QListI14DataItemHolderE(
    ScatterInstancing *self,
    const QList<DataItemHolder> *newDataArray) {
  self->setDataArray(*newDataArray);
}

//  void ScatterInstancing::hideDataItem(qsizetype index)
extern "C" Q_DECL_EXPORT
void ritual_ZN17ScatterInstancing12hideDataItemEx(
    ScatterInstancing *self,
    qsizetype index) {
  self->hideDataItem(index);
}

//  void ScatterInstancing::unhidePreviousDataItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN17ScatterInstancing22unhidePreviousDataItemEv(
    ScatterInstancing *self) {
  self->unhidePreviousDataItem();
}

//  void ScatterInstancing::resetVisibilty()
extern "C" Q_DECL_EXPORT
void ritual_ZN17ScatterInstancing14resetVisibiltyEv(
    ScatterInstancing *self) {
  self->resetVisibilty();
}

//  void ScatterInstancing::markDataDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN17ScatterInstancing13markDataDirtyEv(ScatterInstancing *self) {
  self->markDataDirty();
}

//  bool ScatterInstancing::rangeGradient() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17ScatterInstancing13rangeGradientEv(
    const ScatterInstancing *self) {
  return self->rangeGradient();
}

//  void ScatterInstancing::setRangeGradient(bool newRangeGradient)
extern "C" Q_DECL_EXPORT
void ritual_ZN17ScatterInstancing16setRangeGradientEb(
    ScatterInstancing *self,
    bool newRangeGradient) {
  self->setRangeGradient(newRangeGradient);
}

//  void ScatterInstancing::setTransparency(bool transparency)
extern "C" Q_DECL_EXPORT
void ritual_ZN17ScatterInstancing15setTransparencyEb(
    ScatterInstancing *self,
    bool transparency) {
  self->setTransparency(transparency);
}

//  bool ScatterInstancing::isDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17ScatterInstancing7isDirtyEv(const ScatterInstancing *self) {
  return self->isDirty();
}

//  QByteArray ScatterInstancing::getInstanceBuffer(int *instanceCount)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN17ScatterInstancing17getInstanceBufferEPi(
    ScatterInstancing *self,
    int *instanceCount) {
  return new QByteArray(self->getInstanceBuffer(instanceCount));
}

#endif  // (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_scatter3d))
