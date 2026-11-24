//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qfutureinterface_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(future)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qfutureinterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QFutureInterfaceBasePrivate::RefCount::RefCount(int r, int rt)
extern "C" Q_DECL_EXPORT
QFutureInterfaceBasePrivate::RefCount *ritual_ZN27QFutureInterfaceBasePrivate8RefCountC1Eii(
    int r,
    int rt) {
  return new QFutureInterfaceBasePrivate::RefCount(r, rt);
}

//  bool QFutureInterfaceBasePrivate::RefCount::ref()
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QFutureInterfaceBasePrivate8RefCount3refEv(
    QFutureInterfaceBasePrivate::RefCount *self) {
  return self->ref();
}

//  bool QFutureInterfaceBasePrivate::RefCount::deref()
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QFutureInterfaceBasePrivate8RefCount5derefEv(
    QFutureInterfaceBasePrivate::RefCount *self) {
  return self->deref();
}

//  int QFutureInterfaceBasePrivate::RefCount::load() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QFutureInterfaceBasePrivate8RefCount4loadEv(
    const QFutureInterfaceBasePrivate::RefCount *self) {
  return self->load();
}

//  bool QFutureInterfaceBasePrivate::RefCount::refT()
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QFutureInterfaceBasePrivate8RefCount4refTEv(
    QFutureInterfaceBasePrivate::RefCount *self) {
  return self->refT();
}

//  bool QFutureInterfaceBasePrivate::RefCount::derefT()
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QFutureInterfaceBasePrivate8RefCount6derefTEv(
    QFutureInterfaceBasePrivate::RefCount *self) {
  return self->derefT();
}

//  int QFutureInterfaceBasePrivate::RefCount::loadT() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QFutureInterfaceBasePrivate8RefCount5loadTEv(
    const QFutureInterfaceBasePrivate::RefCount *self) {
  return self->loadT();
}

//  QFutureInterfaceBasePrivate::RefCount::~RefCount()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QFutureInterfaceBasePrivate8RefCountD1Ev(
    QFutureInterfaceBasePrivate::RefCount *self) {
  delete self;
}

#endif  // QT_CONFIG(future)
