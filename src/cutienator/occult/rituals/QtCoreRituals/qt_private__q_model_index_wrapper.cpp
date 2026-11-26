//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qabstractitemmodel_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qabstractitemmodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#if QT_CONFIG(itemmodel)
#include <QtCore/qabstractitemmodel.h>
#endif

//  QtPrivate::QModelIndexWrapper::QModelIndexWrapper(const QModelIndex &i)
extern "C" Q_DECL_EXPORT
QtPrivate::QModelIndexWrapper *ritual_ZN9QtPrivate18QModelIndexWrapperC1ERK11QModelIndex(
    const QModelIndex *i) {
  return new QtPrivate::QModelIndexWrapper(*i);
}

//  QModelIndex QtPrivate::QModelIndexWrapper::operator QModelIndex() const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK9QtPrivate18QModelIndexWrappercv11QModelIndexEv(
    const QtPrivate::QModelIndexWrapper *self) {
  return new QModelIndex(self->operator QModelIndex());
}

//  bool operator==(const QModelIndexWrapper &l, const QModelIndexWrapper &r)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivateeqERKNS_18QModelIndexWrapperES2_(
    const QtPrivate::QModelIndexWrapper *l,
    const QtPrivate::QModelIndexWrapper *r) {
  return operator==(*l, *r);
}

//  bool operator!=(const QModelIndexWrapper &l, const QModelIndexWrapper &r)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivateneERKNS_18QModelIndexWrapperES2_(
    const QtPrivate::QModelIndexWrapper *l,
    const QtPrivate::QModelIndexWrapper *r) {
  return operator!=(*l, *r);
}

//  bool operator==(const QModelIndexWrapper &l, const QModelIndex &r)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivateeqERKNS_18QModelIndexWrapperERK11QModelIndex(
    const QtPrivate::QModelIndexWrapper *l,
    const QModelIndex *r) {
  return operator==(*l, *r);
}

//  bool operator!=(const QModelIndexWrapper &l, const QModelIndex &r)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivateneERKNS_18QModelIndexWrapperERK11QModelIndex(
    const QtPrivate::QModelIndexWrapper *l,
    const QModelIndex *r) {
  return operator!=(*l, *r);
}

//  bool operator==(const QModelIndex &l, const QModelIndexWrapper &r)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivateeqERK11QModelIndexRKNS_18QModelIndexWrapperE(
    const QModelIndex *l,
    const QtPrivate::QModelIndexWrapper *r) {
  return operator==(*l, *r);
}

//  bool operator!=(const QModelIndex &l, const QModelIndexWrapper &r)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivateneERK11QModelIndexRKNS_18QModelIndexWrapperE(
    const QModelIndex *l,
    const QtPrivate::QModelIndexWrapper *r) {
  return operator!=(*l, *r);
}

//  QtPrivate::QModelIndexWrapper::~QModelIndexWrapper()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate18QModelIndexWrapperD1Ev(
    QtPrivate::QModelIndexWrapper *self) {
  delete self;
}

#endif  // QT_CONFIG(itemmodel)
#endif  // QT_CONFIG(itemmodel)
