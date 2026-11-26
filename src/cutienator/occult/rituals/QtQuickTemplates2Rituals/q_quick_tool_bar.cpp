//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktoolbar_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktoolbar_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>

//  Only a class built on QQuickToolBar may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickToolBar : QQuickToolBar {
  using QQuickToolBar::defaultFont;
  using QQuickToolBar::accessibleRole;
};

//  const QMetaObject *QQuickToolBar::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QQuickToolBar10metaObjectEv(
    const QQuickToolBar *self) {
  return self->metaObject();
}

//  void *QQuickToolBar::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13QQuickToolBar11qt_metacastEPKc(
    QQuickToolBar *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickToolBar::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QQuickToolBar11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickToolBar *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickToolBar::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QQuickToolBar2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickToolBar::tr(s, c, n));
}

//  QQuickToolBar::QQuickToolBar(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickToolBar *ritual_ZN13QQuickToolBarC1EP10QQuickItem(QQuickItem *parent) {
  return new QQuickToolBar(parent);
}

//  Position QQuickToolBar::position() const
extern "C" Q_DECL_EXPORT
QQuickToolBar::Position ritual_ZNK13QQuickToolBar8positionEv(
    const QQuickToolBar *self) {
  return self->position();
}

//  void QQuickToolBar::setPosition(Position position)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickToolBar11setPositionENS_8PositionE(
    QQuickToolBar *self,
    QQuickToolBar::Position position) {
  self->setPosition(position);
}

//  void QQuickToolBar::positionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickToolBar15positionChangedEv(QQuickToolBar *self) {
  self->positionChanged();
}

//  QFont QQuickToolBar::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK13QQuickToolBar11defaultFontEv(const QQuickToolBar *self) {
  return new QFont(self->defaultFont());
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickToolBar::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK13QQuickToolBar14accessibleRoleEv(
    const QQuickToolBar *self) {
  return self->accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

//  QQuickToolBarPrivate *QQuickToolBar::d_func()
extern "C" Q_DECL_EXPORT
QQuickToolBarPrivate *ritual_ZN13QQuickToolBar6d_funcEv(
    QQuickToolBar *self) {
  return self->d_func();
}

//  const QQuickToolBarPrivate *QQuickToolBar::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickToolBarPrivate *ritual_ZNK13QQuickToolBar6d_funcEv(
    const QQuickToolBar *self) {
  return self->d_func();
}

//  QFont QQuickToolBar::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_own_ZNK13QQuickToolBar11defaultFontEv(
    const QQuickToolBar *self) {
  return new QFont(
      static_cast<const OwnQQuickToolBar *>(self)->OwnQQuickToolBar::defaultFont());
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickToolBar::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK13QQuickToolBar14accessibleRoleEv(
    const QQuickToolBar *self) {
  return static_cast<const OwnQQuickToolBar *>(self)->OwnQQuickToolBar::accessibleRole();
}
#endif  // QT_CONFIG(accessibility)
