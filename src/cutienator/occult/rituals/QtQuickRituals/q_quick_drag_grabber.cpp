//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickdrag_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_draganddrop)
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

//  iterator QQuickDragGrabber::begin()
extern "C" Q_DECL_EXPORT
QQuickDragGrabber::iterator *ritual_ZN17QQuickDragGrabber5beginEv(
    QQuickDragGrabber *self) {
  return new QQuickDragGrabber::iterator(self->begin());
}

//  iterator QQuickDragGrabber::end()
extern "C" Q_DECL_EXPORT
QQuickDragGrabber::iterator *ritual_ZN17QQuickDragGrabber3endEv(
    QQuickDragGrabber *self) {
  return new QQuickDragGrabber::iterator(self->end());
}

//  void QQuickDragGrabber::grab(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickDragGrabber4grabEP10QQuickItem(
    QQuickDragGrabber *self,
    QQuickItem *item) {
  self->grab(item);
}

//  iterator QQuickDragGrabber::release(iterator at)
extern "C" Q_DECL_EXPORT
QQuickDragGrabber::iterator *ritual_ZN17QQuickDragGrabber7releaseEN14QIntrusiveListINS_4ItemEXadL_ZNS1_4nodeEEEE8iteratorE(
    QQuickDragGrabber *self,
    const QQuickDragGrabber::iterator *at) {
  return new QQuickDragGrabber::iterator(self->release(*at));
}

//  QVarLengthArray<QQuickItem *, 4> &QQuickDragGrabber::ignoreList()
extern "C" Q_DECL_EXPORT
QVarLengthArray<QQuickItem *, 4> *ritual_ZN17QQuickDragGrabber10ignoreListEv(
    QQuickDragGrabber *self) {
  return &(self->ignoreList());
}

//  a QQuickDragGrabber::iterator a ritual of QQuickDragGrabber gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickDragGrabber__QQuickDragGrabber_iterator(
    QQuickDragGrabber::iterator *self) {
  delete self;
}

#endif  // QT_CONFIG(quick_draganddrop)
#endif  // QT_CONFIG(quick_draganddrop)
