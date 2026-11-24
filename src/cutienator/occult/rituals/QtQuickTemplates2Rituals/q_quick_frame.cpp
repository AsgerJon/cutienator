//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickframe_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickframe_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  Only a class built on QQuickFrame may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickFrame : QQuickFrame {
  using QQuickFrame::accessibleRole;
};

//  const QMetaObject *QQuickFrame::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QQuickFrame10metaObjectEv(
    const QQuickFrame *self) {
  return self->metaObject();
}

//  QString QQuickFrame::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QQuickFrame2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickFrame::tr(s, c, n));
}

//  QQuickFrame::QQuickFrame(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickFrame *ritual_ZN11QQuickFrameC1EP10QQuickItem(QQuickItem *parent) {
  return new QQuickFrame(parent);
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickFrame::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK11QQuickFrame14accessibleRoleEv(
    const QQuickFrame *self) {
  return self->accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

//  QQuickFramePrivate *QQuickFrame::d_func()
extern "C" Q_DECL_EXPORT
QQuickFramePrivate *ritual_ZN11QQuickFrame6d_funcEv(QQuickFrame *self) {
  return self->d_func();
}

//  const QQuickFramePrivate *QQuickFrame::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickFramePrivate *ritual_ZNK11QQuickFrame6d_funcEv(
    const QQuickFrame *self) {
  return self->d_func();
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickFrame::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK11QQuickFrame14accessibleRoleEv(
    const QQuickFrame *self) {
  return static_cast<const OwnQQuickFrame *>(self)->OwnQQuickFrame::accessibleRole();
}
#endif  // QT_CONFIG(accessibility)
