//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickmenubaritem_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickmenubaritem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtGui/qfont.h>

//  Only a class built on QQuickMenuBarItem may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickMenuBarItem : QQuickMenuBarItem {
  using QQuickMenuBarItem::event;
  using QQuickMenuBarItem::keyPressEvent;
  using QQuickMenuBarItem::keyReleaseEvent;
  using QQuickMenuBarItem::geometryChange;
  using QQuickMenuBarItem::defaultFont;
  using QQuickMenuBarItem::accessibleRole;
};

//  const QMetaObject *QQuickMenuBarItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQuickMenuBarItem10metaObjectEv(
    const QQuickMenuBarItem *self) {
  return self->metaObject();
}

//  void *QQuickMenuBarItem::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QQuickMenuBarItem11qt_metacastEPKc(
    QQuickMenuBarItem *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickMenuBarItem::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QQuickMenuBarItem11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickMenuBarItem *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickMenuBarItem::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QQuickMenuBarItem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickMenuBarItem::tr(s, c, n));
}

//  QQuickMenuBarItem::QQuickMenuBarItem(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickMenuBarItem *ritual_ZN17QQuickMenuBarItemC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickMenuBarItem(parent);
}

//  QQuickMenuBar *QQuickMenuBarItem::menuBar() const
extern "C" Q_DECL_EXPORT
QQuickMenuBar *ritual_ZNK17QQuickMenuBarItem7menuBarEv(
    const QQuickMenuBarItem *self) {
  return self->menuBar();
}

//  QQuickMenu *QQuickMenuBarItem::menu() const
extern "C" Q_DECL_EXPORT
QQuickMenu *ritual_ZNK17QQuickMenuBarItem4menuEv(
    const QQuickMenuBarItem *self) {
  return self->menu();
}

//  void QQuickMenuBarItem::setMenu(QQuickMenu *menu)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMenuBarItem7setMenuEP10QQuickMenu(
    QQuickMenuBarItem *self,
    QQuickMenu *menu) {
  self->setMenu(menu);
}

//  bool QQuickMenuBarItem::isHighlighted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickMenuBarItem13isHighlightedEv(
    const QQuickMenuBarItem *self) {
  return self->isHighlighted();
}

//  void QQuickMenuBarItem::setHighlighted(bool highlighted)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMenuBarItem14setHighlightedEb(
    QQuickMenuBarItem *self,
    bool highlighted) {
  self->setHighlighted(highlighted);
}

//  void QQuickMenuBarItem::triggered()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMenuBarItem9triggeredEv(QQuickMenuBarItem *self) {
  self->triggered();
}

//  void QQuickMenuBarItem::menuBarChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMenuBarItem14menuBarChangedEv(
    QQuickMenuBarItem *self) {
  self->menuBarChanged();
}

//  void QQuickMenuBarItem::menuChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMenuBarItem11menuChangedEv(QQuickMenuBarItem *self) {
  self->menuChanged();
}

//  void QQuickMenuBarItem::highlightedChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMenuBarItem18highlightedChangedEv(
    QQuickMenuBarItem *self) {
  self->highlightedChanged();
}

//  bool QQuickMenuBarItem::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QQuickMenuBarItem5eventEP6QEvent(
    QQuickMenuBarItem *self,
    QEvent *event) {
  return self->event(event);
}

//  void QQuickMenuBarItem::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMenuBarItem13keyPressEventEP9QKeyEvent(
    QQuickMenuBarItem *self,
    QKeyEvent *event) {
  self->keyPressEvent(event);
}

//  void QQuickMenuBarItem::keyReleaseEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMenuBarItem15keyReleaseEventEP9QKeyEvent(
    QQuickMenuBarItem *self,
    QKeyEvent *event) {
  self->keyReleaseEvent(event);
}

//  void QQuickMenuBarItem::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMenuBarItem14geometryChangeERK6QRectFS2_(
    QQuickMenuBarItem *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  QFont QQuickMenuBarItem::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK17QQuickMenuBarItem11defaultFontEv(
    const QQuickMenuBarItem *self) {
  return new QFont(self->defaultFont());
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickMenuBarItem::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK17QQuickMenuBarItem14accessibleRoleEv(
    const QQuickMenuBarItem *self) {
  return self->accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

//  QQuickMenuBarItemPrivate *QQuickMenuBarItem::d_func()
extern "C" Q_DECL_EXPORT
QQuickMenuBarItemPrivate *ritual_ZN17QQuickMenuBarItem6d_funcEv(
    QQuickMenuBarItem *self) {
  return self->d_func();
}

//  const QQuickMenuBarItemPrivate *QQuickMenuBarItem::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickMenuBarItemPrivate *ritual_ZNK17QQuickMenuBarItem6d_funcEv(
    const QQuickMenuBarItem *self) {
  return self->d_func();
}

//  bool QQuickMenuBarItem::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QQuickMenuBarItem5eventEP6QEvent(
    QQuickMenuBarItem *self,
    QEvent *event) {
  return static_cast<OwnQQuickMenuBarItem *>(self)->OwnQQuickMenuBarItem::event(
      event);
}

//  void QQuickMenuBarItem::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickMenuBarItem13keyPressEventEP9QKeyEvent(
    QQuickMenuBarItem *self,
    QKeyEvent *event) {
  static_cast<OwnQQuickMenuBarItem *>(self)->OwnQQuickMenuBarItem::keyPressEvent(
      event);
}

//  void QQuickMenuBarItem::keyReleaseEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickMenuBarItem15keyReleaseEventEP9QKeyEvent(
    QQuickMenuBarItem *self,
    QKeyEvent *event) {
  static_cast<OwnQQuickMenuBarItem *>(self)->OwnQQuickMenuBarItem::keyReleaseEvent(
      event);
}

//  void QQuickMenuBarItem::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickMenuBarItem14geometryChangeERK6QRectFS2_(
    QQuickMenuBarItem *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuickMenuBarItem *>(self)->OwnQQuickMenuBarItem::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  QFont QQuickMenuBarItem::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_own_ZNK17QQuickMenuBarItem11defaultFontEv(
    const QQuickMenuBarItem *self) {
  return new QFont(
      static_cast<const OwnQQuickMenuBarItem *>(self)->OwnQQuickMenuBarItem::defaultFont());
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickMenuBarItem::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK17QQuickMenuBarItem14accessibleRoleEv(
    const QQuickMenuBarItem *self) {
  return static_cast<const OwnQQuickMenuBarItem *>(self)->OwnQQuickMenuBarItem::accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

#endif  // QT_CONFIG(quicktemplates2_container)
#endif  // QT_CONFIG(quicktemplates2_container)
