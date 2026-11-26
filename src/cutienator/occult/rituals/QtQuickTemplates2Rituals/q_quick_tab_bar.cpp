//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktabbar_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktabbar_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtGui/qfont.h>

//  Only a class built on QQuickTabBar may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickTabBar : QQuickTabBar {
  using QQuickTabBar::updatePolish;
  using QQuickTabBar::componentComplete;
  using QQuickTabBar::geometryChange;
  using QQuickTabBar::isContent;
  using QQuickTabBar::itemAdded;
  using QQuickTabBar::itemMoved;
  using QQuickTabBar::itemRemoved;
  using QQuickTabBar::wheelEvent;
  using QQuickTabBar::defaultFont;
  using QQuickTabBar::accessibleRole;
};

//  const QMetaObject *QQuickTabBar::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QQuickTabBar10metaObjectEv(
    const QQuickTabBar *self) {
  return self->metaObject();
}

//  void *QQuickTabBar::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN12QQuickTabBar11qt_metacastEPKc(
    QQuickTabBar *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickTabBar::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QQuickTabBar11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickTabBar *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickTabBar::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QQuickTabBar2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickTabBar::tr(s, c, n));
}

//  void QQuickTabBar::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickTabBar21qt_qmlMarker_attachedEv(QQuickTabBar *self) {
  self->qt_qmlMarker_attached();
}

//  QQuickTabBar::QQuickTabBar(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickTabBar *ritual_ZN12QQuickTabBarC1EP10QQuickItem(QQuickItem *parent) {
  return new QQuickTabBar(parent);
}

//  Position QQuickTabBar::position() const
extern "C" Q_DECL_EXPORT
QQuickTabBar::Position ritual_ZNK12QQuickTabBar8positionEv(
    const QQuickTabBar *self) {
  return self->position();
}

//  void QQuickTabBar::setPosition(Position position)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickTabBar11setPositionENS_8PositionE(
    QQuickTabBar *self,
    QQuickTabBar::Position position) {
  self->setPosition(position);
}

//  QQuickTabBarAttached *QQuickTabBar::qmlAttachedProperties(QObject
//      *object)
extern "C" Q_DECL_EXPORT
QQuickTabBarAttached *ritual_ZN12QQuickTabBar21qmlAttachedPropertiesEP7QObject(
    QObject *object) {
  return QQuickTabBar::qmlAttachedProperties(object);
}

//  void QQuickTabBar::positionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickTabBar15positionChangedEv(QQuickTabBar *self) {
  self->positionChanged();
}

//  void QQuickTabBar::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickTabBar12updatePolishEv(QQuickTabBar *self) {
  self->updatePolish();
}

//  void QQuickTabBar::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickTabBar17componentCompleteEv(QQuickTabBar *self) {
  self->componentComplete();
}

//  void QQuickTabBar::geometryChange(const QRectF &newGeometry, const QRectF
//      &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickTabBar14geometryChangeERK6QRectFS2_(
    QQuickTabBar *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  bool QQuickTabBar::isContent(QQuickItem *item) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQuickTabBar9isContentEP10QQuickItem(
    const QQuickTabBar *self,
    QQuickItem *item) {
  return self->isContent(item);
}

//  void QQuickTabBar::itemAdded(int index, QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickTabBar9itemAddedEiP10QQuickItem(
    QQuickTabBar *self,
    int index,
    QQuickItem *item) {
  self->itemAdded(index, item);
}

//  void QQuickTabBar::itemMoved(int index, QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickTabBar9itemMovedEiP10QQuickItem(
    QQuickTabBar *self,
    int index,
    QQuickItem *item) {
  self->itemMoved(index, item);
}

//  void QQuickTabBar::itemRemoved(int index, QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickTabBar11itemRemovedEiP10QQuickItem(
    QQuickTabBar *self,
    int index,
    QQuickItem *item) {
  self->itemRemoved(index, item);
}

#if QT_CONFIG(wheelevent)
//  void QQuickTabBar::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickTabBar10wheelEventEP11QWheelEvent(
    QQuickTabBar *self,
    QWheelEvent *event) {
  self->wheelEvent(event);
}
#endif  // QT_CONFIG(wheelevent)

//  QFont QQuickTabBar::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK12QQuickTabBar11defaultFontEv(const QQuickTabBar *self) {
  return new QFont(self->defaultFont());
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickTabBar::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK12QQuickTabBar14accessibleRoleEv(
    const QQuickTabBar *self) {
  return self->accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

//  QQuickTabBarPrivate *QQuickTabBar::d_func()
extern "C" Q_DECL_EXPORT
QQuickTabBarPrivate *ritual_ZN12QQuickTabBar6d_funcEv(QQuickTabBar *self) {
  return self->d_func();
}

//  const QQuickTabBarPrivate *QQuickTabBar::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickTabBarPrivate *ritual_ZNK12QQuickTabBar6d_funcEv(
    const QQuickTabBar *self) {
  return self->d_func();
}

//  void QQuickTabBar::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickTabBar12updatePolishEv(QQuickTabBar *self) {
  static_cast<OwnQQuickTabBar *>(self)->OwnQQuickTabBar::updatePolish();
}

//  void QQuickTabBar::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickTabBar17componentCompleteEv(QQuickTabBar *self) {
  static_cast<OwnQQuickTabBar *>(self)->OwnQQuickTabBar::componentComplete();
}

//  void QQuickTabBar::geometryChange(const QRectF &newGeometry, const QRectF
//      &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickTabBar14geometryChangeERK6QRectFS2_(
    QQuickTabBar *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuickTabBar *>(self)->OwnQQuickTabBar::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  bool QQuickTabBar::isContent(QQuickItem *item) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK12QQuickTabBar9isContentEP10QQuickItem(
    const QQuickTabBar *self,
    QQuickItem *item) {
  return static_cast<const OwnQQuickTabBar *>(self)->OwnQQuickTabBar::isContent(
      item);
}

//  void QQuickTabBar::itemAdded(int index, QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickTabBar9itemAddedEiP10QQuickItem(
    QQuickTabBar *self,
    int index,
    QQuickItem *item) {
  static_cast<OwnQQuickTabBar *>(self)->OwnQQuickTabBar::itemAdded(
      index,
      item);
}

//  void QQuickTabBar::itemMoved(int index, QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickTabBar9itemMovedEiP10QQuickItem(
    QQuickTabBar *self,
    int index,
    QQuickItem *item) {
  static_cast<OwnQQuickTabBar *>(self)->OwnQQuickTabBar::itemMoved(
      index,
      item);
}

//  void QQuickTabBar::itemRemoved(int index, QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickTabBar11itemRemovedEiP10QQuickItem(
    QQuickTabBar *self,
    int index,
    QQuickItem *item) {
  static_cast<OwnQQuickTabBar *>(self)->OwnQQuickTabBar::itemRemoved(
      index,
      item);
}

#if QT_CONFIG(wheelevent)
//  void QQuickTabBar::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickTabBar10wheelEventEP11QWheelEvent(
    QQuickTabBar *self,
    QWheelEvent *event) {
  static_cast<OwnQQuickTabBar *>(self)->OwnQQuickTabBar::wheelEvent(event);
}
#endif  // QT_CONFIG(wheelevent)

//  QFont QQuickTabBar::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_own_ZNK12QQuickTabBar11defaultFontEv(
    const QQuickTabBar *self) {
  return new QFont(
      static_cast<const OwnQQuickTabBar *>(self)->OwnQQuickTabBar::defaultFont());
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickTabBar::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK12QQuickTabBar14accessibleRoleEv(
    const QQuickTabBar *self) {
  return static_cast<const OwnQQuickTabBar *>(self)->OwnQQuickTabBar::accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

#endif  // QT_CONFIG(quicktemplates2_container)
#endif  // QT_CONFIG(quicktemplates2_container)
