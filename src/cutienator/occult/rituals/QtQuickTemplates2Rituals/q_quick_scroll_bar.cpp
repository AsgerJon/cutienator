//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickscrollbar_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickscrollbar_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  Only a class built on QQuickScrollBar may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickScrollBar : QQuickScrollBar {
  using QQuickScrollBar::mousePressEvent;
  using QQuickScrollBar::hoverChange;
  using QQuickScrollBar::hoverEnterEvent;
  using QQuickScrollBar::hoverMoveEvent;
  using QQuickScrollBar::hoverLeaveEvent;
  using QQuickScrollBar::classBegin;
  using QQuickScrollBar::componentComplete;
  using QQuickScrollBar::accessibilityActiveChanged;
  using QQuickScrollBar::accessibleRole;
};

//  const QMetaObject *QQuickScrollBar::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQuickScrollBar10metaObjectEv(
    const QQuickScrollBar *self) {
  return self->metaObject();
}

//  QString QQuickScrollBar::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQuickScrollBar2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickScrollBar::tr(s, c, n));
}

//  void QQuickScrollBar::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickScrollBar21qt_qmlMarker_attachedEv(
    QQuickScrollBar *self) {
  self->qt_qmlMarker_attached();
}

//  QQuickScrollBar::QQuickScrollBar(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickScrollBar *ritual_ZN15QQuickScrollBarC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickScrollBar(parent);
}

//  QQuickScrollBarAttached *QQuickScrollBar::qmlAttachedProperties(QObject
//      *object)
extern "C" Q_DECL_EXPORT
QQuickScrollBarAttached *ritual_ZN15QQuickScrollBar21qmlAttachedPropertiesEP7QObject(
    QObject *object) {
  return QQuickScrollBar::qmlAttachedProperties(object);
}

//  qreal QQuickScrollBar::size() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickScrollBar4sizeEv(const QQuickScrollBar *self) {
  return self->size();
}

//  qreal QQuickScrollBar::position() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickScrollBar8positionEv(const QQuickScrollBar *self) {
  return self->position();
}

//  qreal QQuickScrollBar::stepSize() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickScrollBar8stepSizeEv(const QQuickScrollBar *self) {
  return self->stepSize();
}

//  void QQuickScrollBar::setStepSize(qreal step)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickScrollBar11setStepSizeEd(
    QQuickScrollBar *self,
    qreal step) {
  self->setStepSize(step);
}

//  bool QQuickScrollBar::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickScrollBar8isActiveEv(const QQuickScrollBar *self) {
  return self->isActive();
}

//  void QQuickScrollBar::setActive(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickScrollBar9setActiveEb(
    QQuickScrollBar *self,
    bool active) {
  self->setActive(active);
}

//  bool QQuickScrollBar::isPressed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickScrollBar9isPressedEv(const QQuickScrollBar *self) {
  return self->isPressed();
}

//  void QQuickScrollBar::setPressed(bool pressed)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickScrollBar10setPressedEb(
    QQuickScrollBar *self,
    bool pressed) {
  self->setPressed(pressed);
}

//  Qt::Orientation QQuickScrollBar::orientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_ZNK15QQuickScrollBar11orientationEv(
    const QQuickScrollBar *self) {
  return self->orientation();
}

//  void QQuickScrollBar::setOrientation(Qt::Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickScrollBar14setOrientationEN2Qt11OrientationE(
    QQuickScrollBar *self,
    Qt::Orientation orientation) {
  self->setOrientation(orientation);
}

//  SnapMode QQuickScrollBar::snapMode() const
extern "C" Q_DECL_EXPORT
QQuickScrollBar::SnapMode ritual_ZNK15QQuickScrollBar8snapModeEv(
    const QQuickScrollBar *self) {
  return self->snapMode();
}

//  void QQuickScrollBar::setSnapMode(SnapMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickScrollBar11setSnapModeENS_8SnapModeE(
    QQuickScrollBar *self,
    QQuickScrollBar::SnapMode mode) {
  self->setSnapMode(mode);
}

//  bool QQuickScrollBar::isInteractive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickScrollBar13isInteractiveEv(
    const QQuickScrollBar *self) {
  return self->isInteractive();
}

//  void QQuickScrollBar::setInteractive(bool interactive)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickScrollBar14setInteractiveEb(
    QQuickScrollBar *self,
    bool interactive) {
  self->setInteractive(interactive);
}

//  void QQuickScrollBar::resetInteractive()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickScrollBar16resetInteractiveEv(QQuickScrollBar *self) {
  self->resetInteractive();
}

//  Policy QQuickScrollBar::policy() const
extern "C" Q_DECL_EXPORT
QQuickScrollBar::Policy ritual_ZNK15QQuickScrollBar6policyEv(
    const QQuickScrollBar *self) {
  return self->policy();
}

//  void QQuickScrollBar::setPolicy(Policy policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickScrollBar9setPolicyENS_6PolicyE(
    QQuickScrollBar *self,
    QQuickScrollBar::Policy policy) {
  self->setPolicy(policy);
}

//  bool QQuickScrollBar::isHorizontal() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickScrollBar12isHorizontalEv(
    const QQuickScrollBar *self) {
  return self->isHorizontal();
}

//  bool QQuickScrollBar::isVertical() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickScrollBar10isVerticalEv(const QQuickScrollBar *self) {
  return self->isVertical();
}

//  qreal QQuickScrollBar::minimumSize() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickScrollBar11minimumSizeEv(
    const QQuickScrollBar *self) {
  return self->minimumSize();
}

//  void QQuickScrollBar::setMinimumSize(qreal minimumSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickScrollBar14setMinimumSizeEd(
    QQuickScrollBar *self,
    qreal minimumSize) {
  self->setMinimumSize(minimumSize);
}

//  qreal QQuickScrollBar::visualSize() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickScrollBar10visualSizeEv(
    const QQuickScrollBar *self) {
  return self->visualSize();
}

//  qreal QQuickScrollBar::visualPosition() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickScrollBar14visualPositionEv(
    const QQuickScrollBar *self) {
  return self->visualPosition();
}

//  QQuickIndicatorButton *QQuickScrollBar::decreaseVisual()
extern "C" Q_DECL_EXPORT
QQuickIndicatorButton *ritual_ZN15QQuickScrollBar14decreaseVisualEv(
    QQuickScrollBar *self) {
  return self->decreaseVisual();
}

//  QQuickIndicatorButton *QQuickScrollBar::increaseVisual()
extern "C" Q_DECL_EXPORT
QQuickIndicatorButton *ritual_ZN15QQuickScrollBar14increaseVisualEv(
    QQuickScrollBar *self) {
  return self->increaseVisual();
}

//  void QQuickScrollBar::increase()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickScrollBar8increaseEv(QQuickScrollBar *self) {
  self->increase();
}

//  void QQuickScrollBar::decrease()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickScrollBar8decreaseEv(QQuickScrollBar *self) {
  self->decrease();
}

//  void QQuickScrollBar::setSize(qreal size)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickScrollBar7setSizeEd(
    QQuickScrollBar *self,
    qreal size) {
  self->setSize(size);
}

//  void QQuickScrollBar::setPosition(qreal position)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickScrollBar11setPositionEd(
    QQuickScrollBar *self,
    qreal position) {
  self->setPosition(position);
}

//  void QQuickScrollBar::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickScrollBar15mousePressEventEP11QMouseEvent(
    QQuickScrollBar *self,
    QMouseEvent *event) {
  self->mousePressEvent(event);
}

#if QT_CONFIG(quicktemplates2_hover)
//  void QQuickScrollBar::hoverChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickScrollBar11hoverChangeEv(QQuickScrollBar *self) {
  self->hoverChange();
}
#endif  // QT_CONFIG(quicktemplates2_hover)

#if QT_CONFIG(quicktemplates2_hover)
//  void QQuickScrollBar::hoverEnterEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickScrollBar15hoverEnterEventEP11QHoverEvent(
    QQuickScrollBar *self,
    QHoverEvent *event) {
  self->hoverEnterEvent(event);
}
#endif  // QT_CONFIG(quicktemplates2_hover)

#if QT_CONFIG(quicktemplates2_hover)
//  void QQuickScrollBar::hoverMoveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickScrollBar14hoverMoveEventEP11QHoverEvent(
    QQuickScrollBar *self,
    QHoverEvent *event) {
  self->hoverMoveEvent(event);
}
#endif  // QT_CONFIG(quicktemplates2_hover)

#if QT_CONFIG(quicktemplates2_hover)
//  void QQuickScrollBar::hoverLeaveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickScrollBar15hoverLeaveEventEP11QHoverEvent(
    QQuickScrollBar *self,
    QHoverEvent *event) {
  self->hoverLeaveEvent(event);
}
#endif  // QT_CONFIG(quicktemplates2_hover)

//  void QQuickScrollBar::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickScrollBar10classBeginEv(QQuickScrollBar *self) {
  self->classBegin();
}

//  void QQuickScrollBar::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickScrollBar17componentCompleteEv(QQuickScrollBar *self) {
  self->componentComplete();
}

#if QT_CONFIG(accessibility)
//  void QQuickScrollBar::accessibilityActiveChanged(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickScrollBar26accessibilityActiveChangedEb(
    QQuickScrollBar *self,
    bool active) {
  self->accessibilityActiveChanged(active);
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickScrollBar::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK15QQuickScrollBar14accessibleRoleEv(
    const QQuickScrollBar *self) {
  return self->accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

//  QQuickScrollBarPrivate *QQuickScrollBar::d_func()
extern "C" Q_DECL_EXPORT
QQuickScrollBarPrivate *ritual_ZN15QQuickScrollBar6d_funcEv(
    QQuickScrollBar *self) {
  return self->d_func();
}

//  const QQuickScrollBarPrivate *QQuickScrollBar::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickScrollBarPrivate *ritual_ZNK15QQuickScrollBar6d_funcEv(
    const QQuickScrollBar *self) {
  return self->d_func();
}

//  void QQuickScrollBar::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickScrollBar15mousePressEventEP11QMouseEvent(
    QQuickScrollBar *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickScrollBar *>(self)->OwnQQuickScrollBar::mousePressEvent(
      event);
}

#if QT_CONFIG(quicktemplates2_hover)
//  void QQuickScrollBar::hoverChange()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickScrollBar11hoverChangeEv(QQuickScrollBar *self) {
  static_cast<OwnQQuickScrollBar *>(self)->OwnQQuickScrollBar::hoverChange();
}
#endif  // QT_CONFIG(quicktemplates2_hover)

#if QT_CONFIG(quicktemplates2_hover)
//  void QQuickScrollBar::hoverEnterEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickScrollBar15hoverEnterEventEP11QHoverEvent(
    QQuickScrollBar *self,
    QHoverEvent *event) {
  static_cast<OwnQQuickScrollBar *>(self)->OwnQQuickScrollBar::hoverEnterEvent(
      event);
}
#endif  // QT_CONFIG(quicktemplates2_hover)

#if QT_CONFIG(quicktemplates2_hover)
//  void QQuickScrollBar::hoverMoveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickScrollBar14hoverMoveEventEP11QHoverEvent(
    QQuickScrollBar *self,
    QHoverEvent *event) {
  static_cast<OwnQQuickScrollBar *>(self)->OwnQQuickScrollBar::hoverMoveEvent(
      event);
}
#endif  // QT_CONFIG(quicktemplates2_hover)

#if QT_CONFIG(quicktemplates2_hover)
//  void QQuickScrollBar::hoverLeaveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickScrollBar15hoverLeaveEventEP11QHoverEvent(
    QQuickScrollBar *self,
    QHoverEvent *event) {
  static_cast<OwnQQuickScrollBar *>(self)->OwnQQuickScrollBar::hoverLeaveEvent(
      event);
}
#endif  // QT_CONFIG(quicktemplates2_hover)

//  void QQuickScrollBar::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickScrollBar10classBeginEv(QQuickScrollBar *self) {
  static_cast<OwnQQuickScrollBar *>(self)->OwnQQuickScrollBar::classBegin();
}

//  void QQuickScrollBar::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickScrollBar17componentCompleteEv(
    QQuickScrollBar *self) {
  static_cast<OwnQQuickScrollBar *>(self)->OwnQQuickScrollBar::componentComplete();
}

#if QT_CONFIG(accessibility)
//  void QQuickScrollBar::accessibilityActiveChanged(bool active)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickScrollBar26accessibilityActiveChangedEb(
    QQuickScrollBar *self,
    bool active) {
  static_cast<OwnQQuickScrollBar *>(self)->OwnQQuickScrollBar::accessibilityActiveChanged(
      active);
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickScrollBar::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK15QQuickScrollBar14accessibleRoleEv(
    const QQuickScrollBar *self) {
  return static_cast<const OwnQQuickScrollBar *>(self)->OwnQQuickScrollBar::accessibleRole();
}
#endif  // QT_CONFIG(accessibility)
