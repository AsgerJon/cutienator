//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickitemdelegate_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickitemdelegate_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>

//  Only a class built on QQuickItemDelegate may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickItemDelegate : QQuickItemDelegate {
  using QQuickItemDelegate::defaultFont;
  using QQuickItemDelegate::accessibleRole;
};

//  const QMetaObject *QQuickItemDelegate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QQuickItemDelegate10metaObjectEv(
    const QQuickItemDelegate *self) {
  return self->metaObject();
}

//  QString QQuickItemDelegate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QQuickItemDelegate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickItemDelegate::tr(s, c, n));
}

//  QQuickItemDelegate::QQuickItemDelegate(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickItemDelegate *ritual_ZN18QQuickItemDelegateC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickItemDelegate(parent);
}

//  bool QQuickItemDelegate::isHighlighted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQuickItemDelegate13isHighlightedEv(
    const QQuickItemDelegate *self) {
  return self->isHighlighted();
}

//  void QQuickItemDelegate::setHighlighted(bool highlighted)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickItemDelegate14setHighlightedEb(
    QQuickItemDelegate *self,
    bool highlighted) {
  self->setHighlighted(highlighted);
}

//  QFont QQuickItemDelegate::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK18QQuickItemDelegate11defaultFontEv(
    const QQuickItemDelegate *self) {
  return new QFont(self->defaultFont());
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickItemDelegate::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK18QQuickItemDelegate14accessibleRoleEv(
    const QQuickItemDelegate *self) {
  return self->accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

//  QQuickItemDelegatePrivate *QQuickItemDelegate::d_func()
extern "C" Q_DECL_EXPORT
QQuickItemDelegatePrivate *ritual_ZN18QQuickItemDelegate6d_funcEv(
    QQuickItemDelegate *self) {
  return self->d_func();
}

//  const QQuickItemDelegatePrivate *QQuickItemDelegate::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickItemDelegatePrivate *ritual_ZNK18QQuickItemDelegate6d_funcEv(
    const QQuickItemDelegate *self) {
  return self->d_func();
}

//  QFont QQuickItemDelegate::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_own_ZNK18QQuickItemDelegate11defaultFontEv(
    const QQuickItemDelegate *self) {
  return new QFont(
      static_cast<const OwnQQuickItemDelegate *>(self)->OwnQQuickItemDelegate::defaultFont());
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickItemDelegate::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK18QQuickItemDelegate14accessibleRoleEv(
    const QQuickItemDelegate *self) {
  return static_cast<const OwnQQuickItemDelegate *>(self)->OwnQQuickItemDelegate::accessibleRole();
}
#endif  // QT_CONFIG(accessibility)
