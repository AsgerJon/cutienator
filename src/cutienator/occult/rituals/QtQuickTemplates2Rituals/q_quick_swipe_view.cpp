//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickswipeview_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickswipeview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>

//  Only a class built on QQuickSwipeView may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickSwipeView : QQuickSwipeView {
  using QQuickSwipeView::componentComplete;
  using QQuickSwipeView::geometryChange;
  using QQuickSwipeView::itemAdded;
  using QQuickSwipeView::itemMoved;
  using QQuickSwipeView::itemRemoved;
  using QQuickSwipeView::accessibleRole;
};

//  const QMetaObject *QQuickSwipeView::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQuickSwipeView10metaObjectEv(
    const QQuickSwipeView *self) {
  return self->metaObject();
}

//  void *QQuickSwipeView::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QQuickSwipeView11qt_metacastEPKc(
    QQuickSwipeView *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickSwipeView::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QQuickSwipeView11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickSwipeView *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickSwipeView::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQuickSwipeView2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickSwipeView::tr(s, c, n));
}

//  void QQuickSwipeView::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickSwipeView21qt_qmlMarker_attachedEv(
    QQuickSwipeView *self) {
  self->qt_qmlMarker_attached();
}

//  QQuickSwipeView::QQuickSwipeView(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickSwipeView *ritual_ZN15QQuickSwipeViewC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickSwipeView(parent);
}

//  QQuickSwipeViewAttached *QQuickSwipeView::qmlAttachedProperties(QObject
//      *object)
extern "C" Q_DECL_EXPORT
QQuickSwipeViewAttached *ritual_ZN15QQuickSwipeView21qmlAttachedPropertiesEP7QObject(
    QObject *object) {
  return QQuickSwipeView::qmlAttachedProperties(object);
}

//  bool QQuickSwipeView::isInteractive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickSwipeView13isInteractiveEv(
    const QQuickSwipeView *self) {
  return self->isInteractive();
}

//  void QQuickSwipeView::setInteractive(bool interactive)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickSwipeView14setInteractiveEb(
    QQuickSwipeView *self,
    bool interactive) {
  self->setInteractive(interactive);
}

//  Qt::Orientation QQuickSwipeView::orientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_ZNK15QQuickSwipeView11orientationEv(
    const QQuickSwipeView *self) {
  return self->orientation();
}

//  void QQuickSwipeView::setOrientation(Qt::Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickSwipeView14setOrientationEN2Qt11OrientationE(
    QQuickSwipeView *self,
    Qt::Orientation orientation) {
  self->setOrientation(orientation);
}

//  bool QQuickSwipeView::isHorizontal() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickSwipeView12isHorizontalEv(
    const QQuickSwipeView *self) {
  return self->isHorizontal();
}

//  bool QQuickSwipeView::isVertical() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickSwipeView10isVerticalEv(const QQuickSwipeView *self) {
  return self->isVertical();
}

//  void QQuickSwipeView::interactiveChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickSwipeView18interactiveChangedEv(
    QQuickSwipeView *self) {
  self->interactiveChanged();
}

//  void QQuickSwipeView::orientationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickSwipeView18orientationChangedEv(
    QQuickSwipeView *self) {
  self->orientationChanged();
}

//  void QQuickSwipeView::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickSwipeView17componentCompleteEv(QQuickSwipeView *self) {
  self->componentComplete();
}

//  void QQuickSwipeView::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickSwipeView14geometryChangeERK6QRectFS2_(
    QQuickSwipeView *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  void QQuickSwipeView::itemAdded(int index, QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickSwipeView9itemAddedEiP10QQuickItem(
    QQuickSwipeView *self,
    int index,
    QQuickItem *item) {
  self->itemAdded(index, item);
}

//  void QQuickSwipeView::itemMoved(int index, QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickSwipeView9itemMovedEiP10QQuickItem(
    QQuickSwipeView *self,
    int index,
    QQuickItem *item) {
  self->itemMoved(index, item);
}

//  void QQuickSwipeView::itemRemoved(int index, QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickSwipeView11itemRemovedEiP10QQuickItem(
    QQuickSwipeView *self,
    int index,
    QQuickItem *item) {
  self->itemRemoved(index, item);
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickSwipeView::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK15QQuickSwipeView14accessibleRoleEv(
    const QQuickSwipeView *self) {
  return self->accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

//  QQuickSwipeViewPrivate *QQuickSwipeView::d_func()
extern "C" Q_DECL_EXPORT
QQuickSwipeViewPrivate *ritual_ZN15QQuickSwipeView6d_funcEv(
    QQuickSwipeView *self) {
  return self->d_func();
}

//  const QQuickSwipeViewPrivate *QQuickSwipeView::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickSwipeViewPrivate *ritual_ZNK15QQuickSwipeView6d_funcEv(
    const QQuickSwipeView *self) {
  return self->d_func();
}

//  void QQuickSwipeView::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickSwipeView17componentCompleteEv(
    QQuickSwipeView *self) {
  static_cast<OwnQQuickSwipeView *>(self)->OwnQQuickSwipeView::componentComplete();
}

//  void QQuickSwipeView::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickSwipeView14geometryChangeERK6QRectFS2_(
    QQuickSwipeView *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuickSwipeView *>(self)->OwnQQuickSwipeView::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  void QQuickSwipeView::itemAdded(int index, QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickSwipeView9itemAddedEiP10QQuickItem(
    QQuickSwipeView *self,
    int index,
    QQuickItem *item) {
  static_cast<OwnQQuickSwipeView *>(self)->OwnQQuickSwipeView::itemAdded(
      index,
      item);
}

//  void QQuickSwipeView::itemMoved(int index, QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickSwipeView9itemMovedEiP10QQuickItem(
    QQuickSwipeView *self,
    int index,
    QQuickItem *item) {
  static_cast<OwnQQuickSwipeView *>(self)->OwnQQuickSwipeView::itemMoved(
      index,
      item);
}

//  void QQuickSwipeView::itemRemoved(int index, QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickSwipeView11itemRemovedEiP10QQuickItem(
    QQuickSwipeView *self,
    int index,
    QQuickItem *item) {
  static_cast<OwnQQuickSwipeView *>(self)->OwnQQuickSwipeView::itemRemoved(
      index,
      item);
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickSwipeView::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK15QQuickSwipeView14accessibleRoleEv(
    const QQuickSwipeView *self) {
  return static_cast<const OwnQQuickSwipeView *>(self)->OwnQQuickSwipeView::accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

#endif  // QT_CONFIG(quicktemplates2_container)
#endif  // QT_CONFIG(quicktemplates2_container)
