//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickpositioners_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25:
//  took out the ritual of the protected constructor
//  QQuickFlow(QQuickFlowPrivate &, QQuickItem *), which Qt declares
//  but its library does not offer (undefined reference when
//  linking), and its row.
//  Kept as it is when the generator runs again.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_positioners)
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

//  void *QQuickFlow::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10QQuickFlow11qt_metacastEPKc(
    QQuickFlow *self,
    const char *a0) {
  return self->qt_metacast(a0);
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

//  QQuickFlowPrivate *QQuickFlow::d_func()
extern "C" Q_DECL_EXPORT
QQuickFlowPrivate *ritual_ZN10QQuickFlow6d_funcEv(QQuickFlow *self) {
  return self->d_func();
}

//  const QQuickFlowPrivate *QQuickFlow::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickFlowPrivate *ritual_ZNK10QQuickFlow6d_funcEv(
    const QQuickFlow *self) {
  return self->d_func();
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
#endif  // QT_CONFIG(quick_positioners)
