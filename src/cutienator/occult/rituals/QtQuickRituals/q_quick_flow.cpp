//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickpositioners_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_positioners)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickpositioners_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  Only a class built on QQuickFlow may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickFlow : QQuickFlow {
  using QQuickFlow::doPositioning;
  using QQuickFlow::reportConflictingAnchors;
};

//  const QMetaObject *QQuickFlow::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QQuickFlow10metaObjectEv(
    const QQuickFlow *self) {
  return self->metaObject();
}

//  QString QQuickFlow::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QQuickFlow2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickFlow::tr(s, c, n));
}

//  QQuickFlow::QQuickFlow(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickFlow *ritual_ZN10QQuickFlowC1EP10QQuickItem(QQuickItem *parent) {
  return new QQuickFlow(parent);
}

//  Flow QQuickFlow::flow() const
extern "C" Q_DECL_EXPORT
QQuickFlow::Flow ritual_ZNK10QQuickFlow4flowEv(const QQuickFlow *self) {
  return self->flow();
}

//  void QQuickFlow::setFlow(Flow a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickFlow7setFlowENS_4FlowE(
    QQuickFlow *self,
    QQuickFlow::Flow a0) {
  self->setFlow(a0);
}

//  Qt::LayoutDirection QQuickFlow::layoutDirection() const
extern "C" Q_DECL_EXPORT
Qt::LayoutDirection ritual_ZNK10QQuickFlow15layoutDirectionEv(
    const QQuickFlow *self) {
  return self->layoutDirection();
}

//  void QQuickFlow::setLayoutDirection(Qt::LayoutDirection a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickFlow18setLayoutDirectionEN2Qt15LayoutDirectionE(
    QQuickFlow *self,
    Qt::LayoutDirection a0) {
  self->setLayoutDirection(a0);
}

//  Qt::LayoutDirection QQuickFlow::effectiveLayoutDirection() const
extern "C" Q_DECL_EXPORT
Qt::LayoutDirection ritual_ZNK10QQuickFlow24effectiveLayoutDirectionEv(
    const QQuickFlow *self) {
  return self->effectiveLayoutDirection();
}

//  void QQuickFlow::doPositioning(QSizeF *contentSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickFlow13doPositioningEP6QSizeF(
    QQuickFlow *self,
    QSizeF *contentSize) {
  self->doPositioning(contentSize);
}

//  void QQuickFlow::reportConflictingAnchors()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickFlow24reportConflictingAnchorsEv(QQuickFlow *self) {
  self->reportConflictingAnchors();
}

//  void QQuickFlow::doPositioning(QSizeF *contentSize)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickFlow13doPositioningEP6QSizeF(
    QQuickFlow *self,
    QSizeF *contentSize) {
  static_cast<OwnQQuickFlow *>(self)->OwnQQuickFlow::doPositioning(
      contentSize);
}

//  void QQuickFlow::reportConflictingAnchors()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickFlow24reportConflictingAnchorsEv(
    QQuickFlow *self) {
  static_cast<OwnQQuickFlow *>(self)->OwnQQuickFlow::reportConflictingAnchors();
}

#endif  // QT_CONFIG(quick_positioners)
