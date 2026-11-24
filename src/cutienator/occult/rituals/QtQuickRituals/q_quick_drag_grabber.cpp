//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickdrag_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_draganddrop)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickdrag_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQuickDragGrabber::QQuickDragGrabber()
extern "C" Q_DECL_EXPORT
QQuickDragGrabber *ritual_ZN17QQuickDragGrabberC1Ev() {
  return new QQuickDragGrabber();
}

//  QQuickDragGrabber::~QQuickDragGrabber()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickDragGrabberD1Ev(QQuickDragGrabber *self) {
  delete self;
}

//  QObject *QQuickDragGrabber::target() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK17QQuickDragGrabber6targetEv(
    const QQuickDragGrabber *self) {
  return self->target();
}

//  void QQuickDragGrabber::setTarget(QObject *target)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickDragGrabber9setTargetEP7QObject(
    QQuickDragGrabber *self,
    QObject *target) {
  self->setTarget(target);
}

//  void QQuickDragGrabber::resetTarget()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickDragGrabber11resetTargetEv(QQuickDragGrabber *self) {
  self->resetTarget();
}

//  bool QQuickDragGrabber::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickDragGrabber7isEmptyEv(const QQuickDragGrabber *self) {
  return self->isEmpty();
}

//  void QQuickDragGrabber::grab(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickDragGrabber4grabEP10QQuickItem(
    QQuickDragGrabber *self,
    QQuickItem *item) {
  self->grab(item);
}

#endif  // QT_CONFIG(quick_draganddrop)
