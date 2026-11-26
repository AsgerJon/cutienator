//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickmenuitem_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtGui/qtguiglobal.h>
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickmenuitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>

//  Only a class built on QQuickMenuItem may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickMenuItem : QQuickMenuItem {
  using QQuickMenuItem::componentComplete;
  using QQuickMenuItem::defaultFont;
  using QQuickMenuItem::accessibleRole;
};

//  const QMetaObject *QQuickMenuItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQuickMenuItem10metaObjectEv(
    const QQuickMenuItem *self) {
  return self->metaObject();
}

//  void *QQuickMenuItem::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QQuickMenuItem11qt_metacastEPKc(
    QQuickMenuItem *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickMenuItem::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QQuickMenuItem11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickMenuItem *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickMenuItem::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QQuickMenuItem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickMenuItem::tr(s, c, n));
}

//  QQuickMenuItem::QQuickMenuItem(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickMenuItem *ritual_ZN14QQuickMenuItemC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickMenuItem(parent);
}

//  bool QQuickMenuItem::isHighlighted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuickMenuItem13isHighlightedEv(
    const QQuickMenuItem *self) {
  return self->isHighlighted();
}

//  void QQuickMenuItem::setHighlighted(bool highlighted)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickMenuItem14setHighlightedEb(
    QQuickMenuItem *self,
    bool highlighted) {
  self->setHighlighted(highlighted);
}

//  QQuickItem *QQuickMenuItem::arrow() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK14QQuickMenuItem5arrowEv(const QQuickMenuItem *self) {
  return self->arrow();
}

//  void QQuickMenuItem::setArrow(QQuickItem *arrow)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickMenuItem8setArrowEP10QQuickItem(
    QQuickMenuItem *self,
    QQuickItem *arrow) {
  self->setArrow(arrow);
}

//  QQuickMenu *QQuickMenuItem::menu() const
extern "C" Q_DECL_EXPORT
QQuickMenu *ritual_ZNK14QQuickMenuItem4menuEv(const QQuickMenuItem *self) {
  return self->menu();
}

//  QQuickMenu *QQuickMenuItem::subMenu() const
extern "C" Q_DECL_EXPORT
QQuickMenu *ritual_ZNK14QQuickMenuItem7subMenuEv(
    const QQuickMenuItem *self) {
  return self->subMenu();
}

//  qreal QQuickMenuItem::textPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickMenuItem11textPaddingEv(const QQuickMenuItem *self) {
  return self->textPadding();
}

//  qreal QQuickMenuItem::implicitTextPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickMenuItem19implicitTextPaddingEv(
    const QQuickMenuItem *self) {
  return self->implicitTextPadding();
}

//  void QQuickMenuItem::setImplicitTextPadding(qreal newImplicitTextPadding)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickMenuItem22setImplicitTextPaddingEd(
    QQuickMenuItem *self,
    qreal newImplicitTextPadding) {
  self->setImplicitTextPadding(newImplicitTextPadding);
}

//  void QQuickMenuItem::triggered()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickMenuItem9triggeredEv(QQuickMenuItem *self) {
  self->triggered();
}

//  void QQuickMenuItem::highlightedChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickMenuItem18highlightedChangedEv(QQuickMenuItem *self) {
  self->highlightedChanged();
}

//  void QQuickMenuItem::arrowChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickMenuItem12arrowChangedEv(QQuickMenuItem *self) {
  self->arrowChanged();
}

//  void QQuickMenuItem::menuChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickMenuItem11menuChangedEv(QQuickMenuItem *self) {
  self->menuChanged();
}

//  void QQuickMenuItem::subMenuChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickMenuItem14subMenuChangedEv(QQuickMenuItem *self) {
  self->subMenuChanged();
}

//  void QQuickMenuItem::implicitTextPaddingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickMenuItem26implicitTextPaddingChangedEv(
    QQuickMenuItem *self) {
  self->implicitTextPaddingChanged();
}

//  void QQuickMenuItem::textPaddingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickMenuItem18textPaddingChangedEv(QQuickMenuItem *self) {
  self->textPaddingChanged();
}

//  void QQuickMenuItem::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickMenuItem17componentCompleteEv(QQuickMenuItem *self) {
  self->componentComplete();
}

//  QFont QQuickMenuItem::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK14QQuickMenuItem11defaultFontEv(
    const QQuickMenuItem *self) {
  return new QFont(self->defaultFont());
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickMenuItem::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK14QQuickMenuItem14accessibleRoleEv(
    const QQuickMenuItem *self) {
  return self->accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

//  QQuickMenuItemPrivate *QQuickMenuItem::d_func()
extern "C" Q_DECL_EXPORT
QQuickMenuItemPrivate *ritual_ZN14QQuickMenuItem6d_funcEv(
    QQuickMenuItem *self) {
  return self->d_func();
}

//  const QQuickMenuItemPrivate *QQuickMenuItem::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickMenuItemPrivate *ritual_ZNK14QQuickMenuItem6d_funcEv(
    const QQuickMenuItem *self) {
  return self->d_func();
}

//  void QQuickMenuItem::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickMenuItem17componentCompleteEv(
    QQuickMenuItem *self) {
  static_cast<OwnQQuickMenuItem *>(self)->OwnQQuickMenuItem::componentComplete();
}

//  QFont QQuickMenuItem::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_own_ZNK14QQuickMenuItem11defaultFontEv(
    const QQuickMenuItem *self) {
  return new QFont(
      static_cast<const OwnQQuickMenuItem *>(self)->OwnQQuickMenuItem::defaultFont());
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickMenuItem::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK14QQuickMenuItem14accessibleRoleEv(
    const QQuickMenuItem *self) {
  return static_cast<const OwnQQuickMenuItem *>(self)->OwnQQuickMenuItem::accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

#endif  // QT_CONFIG(qml_object_model)
#endif  // QT_CONFIG(qml_object_model)
