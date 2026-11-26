//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickpath_p_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_path)
#if QT_CONFIG(quick_path)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_path)
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickpath_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#endif
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickpath_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQuickPath *QQuickPathPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickPath *ritual_ZN17QQuickPathPrivate6q_funcEv(QQuickPathPrivate *self) {
  return self->q_func();
}

//  const QQuickPath *QQuickPathPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickPath *ritual_ZNK17QQuickPathPrivate6q_funcEv(
    const QQuickPathPrivate *self) {
  return self->q_func();
}

//  QQuickPathPrivate *QQuickPathPrivate::get(QQuickPath *path)
extern "C" Q_DECL_EXPORT
QQuickPathPrivate *ritual_ZN17QQuickPathPrivate3getEP10QQuickPath(
    QQuickPath *path) {
  return QQuickPathPrivate::get(path);
}

//  const QQuickPathPrivate *QQuickPathPrivate::get(const QQuickPath *path)
extern "C" Q_DECL_EXPORT
const QQuickPathPrivate *ritual_ZN17QQuickPathPrivate3getEPK10QQuickPath(
    const QQuickPath *path) {
  return QQuickPathPrivate::get(path);
}

//  QQuickPathPrivate::QQuickPathPrivate()
extern "C" Q_DECL_EXPORT
QQuickPathPrivate *ritual_ZN17QQuickPathPrivateC1Ev() {
  return new QQuickPathPrivate();
}

//  void QQuickPathPrivate::appendPathElement(QQuickPathElement *pathElement,
//      ProcessPathPolicy processPathPolicy)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPathPrivate17appendPathElementEP17QQuickPathElementNS_17ProcessPathPolicyE(
    QQuickPathPrivate *self,
    QQuickPathElement *pathElement,
    QQuickPathPrivate::ProcessPathPolicy processPathPolicy) {
  self->appendPathElement(pathElement, processPathPolicy);
}

//  void QQuickPathPrivate::removeLastPathElement()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPathPrivate21removeLastPathElementEv(
    QQuickPathPrivate *self) {
  self->removeLastPathElement();
}

//  void QQuickPathPrivate::replacePathElement(qsizetype position,
//      QQuickPathElement *pathElement)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPathPrivate18replacePathElementExP17QQuickPathElement(
    QQuickPathPrivate *self,
    qsizetype position,
    QQuickPathElement *pathElement) {
  self->replacePathElement(position, pathElement);
}

//  void QQuickPathPrivate::clearPathElements(DeleteElementPolicy
//      deleteElementPolicy)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPathPrivate17clearPathElementsENS_19DeleteElementPolicyE(
    QQuickPathPrivate *self,
    QQuickPathPrivate::DeleteElementPolicy deleteElementPolicy) {
  self->clearPathElements(deleteElementPolicy);
}

//  void QQuickPathPrivate::enablePathElement(QQuickPathElement *pathElement)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPathPrivate17enablePathElementEP17QQuickPathElement(
    QQuickPathPrivate *self,
    QQuickPathElement *pathElement) {
  self->enablePathElement(pathElement);
}

//  void QQuickPathPrivate::disablePathElement(QQuickPathElement
//      *pathElement)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPathPrivate18disablePathElementEP17QQuickPathElement(
    QQuickPathPrivate *self,
    QQuickPathElement *pathElement) {
  self->disablePathElement(pathElement);
}

#endif  // QT_CONFIG(quick_path)
#endif  // QT_CONFIG(quick_path)
