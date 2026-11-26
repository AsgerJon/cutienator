//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickswipedelegate_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickswipedelegate_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtGui/qfont.h>

//  Only a class built on QQuickSwipeDelegate may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickSwipeDelegate : QQuickSwipeDelegate {
  using QQuickSwipeDelegate::childMouseEventFilter;
  using QQuickSwipeDelegate::mousePressEvent;
  using QQuickSwipeDelegate::mouseMoveEvent;
  using QQuickSwipeDelegate::mouseReleaseEvent;
  using QQuickSwipeDelegate::mouseUngrabEvent;
  using QQuickSwipeDelegate::touchEvent;
  using QQuickSwipeDelegate::componentComplete;
  using QQuickSwipeDelegate::geometryChange;
  using QQuickSwipeDelegate::defaultFont;
  using QQuickSwipeDelegate::accessibleRole;
};

//  const QMetaObject *QQuickSwipeDelegate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuickSwipeDelegate10metaObjectEv(
    const QQuickSwipeDelegate *self) {
  return self->metaObject();
}

//  void *QQuickSwipeDelegate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QQuickSwipeDelegate11qt_metacastEPKc(
    QQuickSwipeDelegate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickSwipeDelegate::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QQuickSwipeDelegate11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickSwipeDelegate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickSwipeDelegate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQuickSwipeDelegate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickSwipeDelegate::tr(s, c, n));
}

//  void QQuickSwipeDelegate::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickSwipeDelegate21qt_qmlMarker_attachedEv(
    QQuickSwipeDelegate *self) {
  self->qt_qmlMarker_attached();
}

//  QQuickSwipeDelegate::QQuickSwipeDelegate(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickSwipeDelegate *ritual_ZN19QQuickSwipeDelegateC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickSwipeDelegate(parent);
}

//  QQuickSwipe *QQuickSwipeDelegate::swipe() const
extern "C" Q_DECL_EXPORT
QQuickSwipe *ritual_ZNK19QQuickSwipeDelegate5swipeEv(
    const QQuickSwipeDelegate *self) {
  return self->swipe();
}

//  QQuickSwipeDelegateAttached
//      *QQuickSwipeDelegate::qmlAttachedProperties(QObject *object)
extern "C" Q_DECL_EXPORT
QQuickSwipeDelegateAttached *ritual_ZN19QQuickSwipeDelegate21qmlAttachedPropertiesEP7QObject(
    QObject *object) {
  return QQuickSwipeDelegate::qmlAttachedProperties(object);
}

//  bool QQuickSwipeDelegate::childMouseEventFilter(QQuickItem *child, QEvent
//      *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQuickSwipeDelegate21childMouseEventFilterEP10QQuickItemP6QEvent(
    QQuickSwipeDelegate *self,
    QQuickItem *child,
    QEvent *event) {
  return self->childMouseEventFilter(child, event);
}

//  void QQuickSwipeDelegate::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickSwipeDelegate15mousePressEventEP11QMouseEvent(
    QQuickSwipeDelegate *self,
    QMouseEvent *event) {
  self->mousePressEvent(event);
}

//  void QQuickSwipeDelegate::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickSwipeDelegate14mouseMoveEventEP11QMouseEvent(
    QQuickSwipeDelegate *self,
    QMouseEvent *event) {
  self->mouseMoveEvent(event);
}

//  void QQuickSwipeDelegate::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickSwipeDelegate17mouseReleaseEventEP11QMouseEvent(
    QQuickSwipeDelegate *self,
    QMouseEvent *event) {
  self->mouseReleaseEvent(event);
}

//  void QQuickSwipeDelegate::mouseUngrabEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickSwipeDelegate16mouseUngrabEventEv(
    QQuickSwipeDelegate *self) {
  self->mouseUngrabEvent();
}

//  void QQuickSwipeDelegate::touchEvent(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickSwipeDelegate10touchEventEP11QTouchEvent(
    QQuickSwipeDelegate *self,
    QTouchEvent *event) {
  self->touchEvent(event);
}

//  void QQuickSwipeDelegate::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickSwipeDelegate17componentCompleteEv(
    QQuickSwipeDelegate *self) {
  self->componentComplete();
}

//  void QQuickSwipeDelegate::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickSwipeDelegate14geometryChangeERK6QRectFS2_(
    QQuickSwipeDelegate *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  QFont QQuickSwipeDelegate::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK19QQuickSwipeDelegate11defaultFontEv(
    const QQuickSwipeDelegate *self) {
  return new QFont(self->defaultFont());
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickSwipeDelegate::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK19QQuickSwipeDelegate14accessibleRoleEv(
    const QQuickSwipeDelegate *self) {
  return self->accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

//  QQuickSwipeDelegatePrivate *QQuickSwipeDelegate::d_func()
extern "C" Q_DECL_EXPORT
QQuickSwipeDelegatePrivate *ritual_ZN19QQuickSwipeDelegate6d_funcEv(
    QQuickSwipeDelegate *self) {
  return self->d_func();
}

//  const QQuickSwipeDelegatePrivate *QQuickSwipeDelegate::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickSwipeDelegatePrivate *ritual_ZNK19QQuickSwipeDelegate6d_funcEv(
    const QQuickSwipeDelegate *self) {
  return self->d_func();
}

//  bool QQuickSwipeDelegate::childMouseEventFilter(QQuickItem *child, QEvent
//      *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QQuickSwipeDelegate21childMouseEventFilterEP10QQuickItemP6QEvent(
    QQuickSwipeDelegate *self,
    QQuickItem *child,
    QEvent *event) {
  return static_cast<OwnQQuickSwipeDelegate *>(self)->OwnQQuickSwipeDelegate::childMouseEventFilter(
      child,
      event);
}

//  void QQuickSwipeDelegate::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickSwipeDelegate15mousePressEventEP11QMouseEvent(
    QQuickSwipeDelegate *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickSwipeDelegate *>(self)->OwnQQuickSwipeDelegate::mousePressEvent(
      event);
}

//  void QQuickSwipeDelegate::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickSwipeDelegate14mouseMoveEventEP11QMouseEvent(
    QQuickSwipeDelegate *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickSwipeDelegate *>(self)->OwnQQuickSwipeDelegate::mouseMoveEvent(
      event);
}

//  void QQuickSwipeDelegate::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickSwipeDelegate17mouseReleaseEventEP11QMouseEvent(
    QQuickSwipeDelegate *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickSwipeDelegate *>(self)->OwnQQuickSwipeDelegate::mouseReleaseEvent(
      event);
}

//  void QQuickSwipeDelegate::mouseUngrabEvent()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickSwipeDelegate16mouseUngrabEventEv(
    QQuickSwipeDelegate *self) {
  static_cast<OwnQQuickSwipeDelegate *>(self)->OwnQQuickSwipeDelegate::mouseUngrabEvent();
}

//  void QQuickSwipeDelegate::touchEvent(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickSwipeDelegate10touchEventEP11QTouchEvent(
    QQuickSwipeDelegate *self,
    QTouchEvent *event) {
  static_cast<OwnQQuickSwipeDelegate *>(self)->OwnQQuickSwipeDelegate::touchEvent(
      event);
}

//  void QQuickSwipeDelegate::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickSwipeDelegate17componentCompleteEv(
    QQuickSwipeDelegate *self) {
  static_cast<OwnQQuickSwipeDelegate *>(self)->OwnQQuickSwipeDelegate::componentComplete();
}

//  void QQuickSwipeDelegate::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickSwipeDelegate14geometryChangeERK6QRectFS2_(
    QQuickSwipeDelegate *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuickSwipeDelegate *>(self)->OwnQQuickSwipeDelegate::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  QFont QQuickSwipeDelegate::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_own_ZNK19QQuickSwipeDelegate11defaultFontEv(
    const QQuickSwipeDelegate *self) {
  return new QFont(
      static_cast<const OwnQQuickSwipeDelegate *>(self)->OwnQQuickSwipeDelegate::defaultFont());
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickSwipeDelegate::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK19QQuickSwipeDelegate14accessibleRoleEv(
    const QQuickSwipeDelegate *self) {
  return static_cast<const OwnQQuickSwipeDelegate *>(self)->OwnQQuickSwipeDelegate::accessibleRole();
}
#endif  // QT_CONFIG(accessibility)
