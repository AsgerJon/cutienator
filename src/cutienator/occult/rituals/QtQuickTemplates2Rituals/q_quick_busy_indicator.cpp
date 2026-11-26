//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickbusyindicator_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickbusyindicator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  Only a class built on QQuickBusyIndicator may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickBusyIndicator : QQuickBusyIndicator {
  using QQuickBusyIndicator::touchEvent;
  using QQuickBusyIndicator::accessibleRole;
};

//  const QMetaObject *QQuickBusyIndicator::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuickBusyIndicator10metaObjectEv(
    const QQuickBusyIndicator *self) {
  return self->metaObject();
}

//  void *QQuickBusyIndicator::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QQuickBusyIndicator11qt_metacastEPKc(
    QQuickBusyIndicator *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickBusyIndicator::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QQuickBusyIndicator11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickBusyIndicator *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickBusyIndicator::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQuickBusyIndicator2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickBusyIndicator::tr(s, c, n));
}

//  QQuickBusyIndicator::QQuickBusyIndicator(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickBusyIndicator *ritual_ZN19QQuickBusyIndicatorC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickBusyIndicator(parent);
}

//  bool QQuickBusyIndicator::isRunning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickBusyIndicator9isRunningEv(
    const QQuickBusyIndicator *self) {
  return self->isRunning();
}

//  void QQuickBusyIndicator::setRunning(bool running)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickBusyIndicator10setRunningEb(
    QQuickBusyIndicator *self,
    bool running) {
  self->setRunning(running);
}

//  void QQuickBusyIndicator::runningChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickBusyIndicator14runningChangedEv(
    QQuickBusyIndicator *self) {
  self->runningChanged();
}

#if QT_CONFIG(quicktemplates2_multitouch)
//  void QQuickBusyIndicator::touchEvent(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickBusyIndicator10touchEventEP11QTouchEvent(
    QQuickBusyIndicator *self,
    QTouchEvent *event) {
  self->touchEvent(event);
}
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickBusyIndicator::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK19QQuickBusyIndicator14accessibleRoleEv(
    const QQuickBusyIndicator *self) {
  return self->accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

//  QQuickBusyIndicatorPrivate *QQuickBusyIndicator::d_func()
extern "C" Q_DECL_EXPORT
QQuickBusyIndicatorPrivate *ritual_ZN19QQuickBusyIndicator6d_funcEv(
    QQuickBusyIndicator *self) {
  return self->d_func();
}

//  const QQuickBusyIndicatorPrivate *QQuickBusyIndicator::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickBusyIndicatorPrivate *ritual_ZNK19QQuickBusyIndicator6d_funcEv(
    const QQuickBusyIndicator *self) {
  return self->d_func();
}

#if QT_CONFIG(quicktemplates2_multitouch)
//  void QQuickBusyIndicator::touchEvent(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickBusyIndicator10touchEventEP11QTouchEvent(
    QQuickBusyIndicator *self,
    QTouchEvent *event) {
  static_cast<OwnQQuickBusyIndicator *>(self)->OwnQQuickBusyIndicator::touchEvent(
      event);
}
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickBusyIndicator::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK19QQuickBusyIndicator14accessibleRoleEv(
    const QQuickBusyIndicator *self) {
  return static_cast<const OwnQQuickBusyIndicator *>(self)->OwnQQuickBusyIndicator::accessibleRole();
}
#endif  // QT_CONFIG(accessibility)
