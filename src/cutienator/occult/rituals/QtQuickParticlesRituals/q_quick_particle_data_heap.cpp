//  Written by dev_tooling.RitualGenerator from the records of QtQuickParticl
//  es/6.12.0/QtQuickParticles/private/qquickparticlesystem_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qtquickparticlesglobal_p.h>
#include <QtQuickParticles/QtQuickParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qquickparticlesystem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QSet>

//  QQuickParticleDataHeap::QQuickParticleDataHeap()
extern "C" Q_DECL_EXPORT
QQuickParticleDataHeap *ritual_ZN22QQuickParticleDataHeapC1Ev() {
  return new QQuickParticleDataHeap();
}

//  void QQuickParticleDataHeap::insert(QQuickParticleData *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickParticleDataHeap6insertEP18QQuickParticleData(
    QQuickParticleDataHeap *self,
    QQuickParticleData *data) {
  self->insert(data);
}

//  void QQuickParticleDataHeap::insertTimed(QQuickParticleData *data, int
//      time)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickParticleDataHeap11insertTimedEP18QQuickParticleDatai(
    QQuickParticleDataHeap *self,
    QQuickParticleData *data,
    int time) {
  self->insertTimed(data, time);
}

//  int QQuickParticleDataHeap::top()
extern "C" Q_DECL_EXPORT
int ritual_ZN22QQuickParticleDataHeap3topEv(QQuickParticleDataHeap *self) {
  return self->top();
}

//  bool QQuickParticleDataHeap::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickParticleDataHeap7isEmptyEv(
    const QQuickParticleDataHeap *self) {
  return self->isEmpty();
}

//  QSet<QQuickParticleData *> QQuickParticleDataHeap::pop()
extern "C" Q_DECL_EXPORT
QSet<QQuickParticleData *> *ritual_ZN22QQuickParticleDataHeap3popEv(
    QQuickParticleDataHeap *self) {
  return new QSet<QQuickParticleData *>(self->pop());
}

//  void QQuickParticleDataHeap::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickParticleDataHeap5clearEv(
    QQuickParticleDataHeap *self) {
  self->clear();
}

//  bool QQuickParticleDataHeap::contains(QQuickParticleData *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickParticleDataHeap8containsEP18QQuickParticleData(
    QQuickParticleDataHeap *self,
    QQuickParticleData *a0) {
  return self->contains(a0);
}

//  void QQuickParticleDataHeap::grow()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickParticleDataHeap4growEv(QQuickParticleDataHeap *self) {
  self->grow();
}

//  void QQuickParticleDataHeap::swap(int a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickParticleDataHeap4swapEii(
    QQuickParticleDataHeap *self,
    int a0,
    int a1) {
  self->swap(a0, a1);
}

//  void QQuickParticleDataHeap::bubbleUp(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickParticleDataHeap8bubbleUpEi(
    QQuickParticleDataHeap *self,
    int a0) {
  self->bubbleUp(a0);
}

//  void QQuickParticleDataHeap::bubbleDown(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickParticleDataHeap10bubbleDownEi(
    QQuickParticleDataHeap *self,
    int a0) {
  self->bubbleDown(a0);
}

//  QQuickParticleDataHeap::~QQuickParticleDataHeap()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickParticleDataHeapD1Ev(QQuickParticleDataHeap *self) {
  delete self;
}

//  a QSet<QQuickParticleData *> a ritual of QQuickParticleDataHeap gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickParticleDataHeap__QSet_QQuickParticleData(
    QSet<QQuickParticleData *> *self) {
  delete self;
}
