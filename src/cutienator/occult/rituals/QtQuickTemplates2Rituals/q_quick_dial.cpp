//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickdial_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickdial_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  Only a class built on QQuickDial may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickDial : QQuickDial {
  using QQuickDial::keyPressEvent;
  using QQuickDial::keyReleaseEvent;
  using QQuickDial::mousePressEvent;
  using QQuickDial::touchEvent;
  using QQuickDial::wheelEvent;
  using QQuickDial::mirrorChange;
  using QQuickDial::componentComplete;
  using QQuickDial::accessibilityActiveChanged;
  using QQuickDial::accessibleRole;
};

//  const QMetaObject *QQuickDial::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QQuickDial10metaObjectEv(
    const QQuickDial *self) {
  return self->metaObject();
}

//  void *QQuickDial::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10QQuickDial11qt_metacastEPKc(
    QQuickDial *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickDial::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QQuickDial11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickDial *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickDial::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QQuickDial2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickDial::tr(s, c, n));
}

//  QQuickDial::QQuickDial(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickDial *ritual_ZN10QQuickDialC1EP10QQuickItem(QQuickItem *parent) {
  return new QQuickDial(parent);
}

//  qreal QQuickDial::from() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QQuickDial4fromEv(const QQuickDial *self) {
  return self->from();
}

//  void QQuickDial::setFrom(qreal from)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDial7setFromEd(QQuickDial *self, qreal from) {
  self->setFrom(from);
}

//  qreal QQuickDial::to() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QQuickDial2toEv(const QQuickDial *self) {
  return self->to();
}

//  void QQuickDial::setTo(qreal to)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDial5setToEd(QQuickDial *self, qreal to) {
  self->setTo(to);
}

//  qreal QQuickDial::value() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QQuickDial5valueEv(const QQuickDial *self) {
  return self->value();
}

//  void QQuickDial::setValue(qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDial8setValueEd(QQuickDial *self, qreal value) {
  self->setValue(value);
}

//  qreal QQuickDial::position() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QQuickDial8positionEv(const QQuickDial *self) {
  return self->position();
}

//  qreal QQuickDial::angle() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QQuickDial5angleEv(const QQuickDial *self) {
  return self->angle();
}

//  qreal QQuickDial::stepSize() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QQuickDial8stepSizeEv(const QQuickDial *self) {
  return self->stepSize();
}

//  void QQuickDial::setStepSize(qreal step)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDial11setStepSizeEd(QQuickDial *self, qreal step) {
  self->setStepSize(step);
}

//  qreal QQuickDial::startAngle() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QQuickDial10startAngleEv(const QQuickDial *self) {
  return self->startAngle();
}

//  void QQuickDial::setStartAngle(qreal startAngle)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDial13setStartAngleEd(
    QQuickDial *self,
    qreal startAngle) {
  self->setStartAngle(startAngle);
}

//  qreal QQuickDial::endAngle() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QQuickDial8endAngleEv(const QQuickDial *self) {
  return self->endAngle();
}

//  void QQuickDial::setEndAngle(qreal endAngle)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDial11setEndAngleEd(QQuickDial *self, qreal endAngle) {
  self->setEndAngle(endAngle);
}

//  SnapMode QQuickDial::snapMode() const
extern "C" Q_DECL_EXPORT
QQuickDial::SnapMode ritual_ZNK10QQuickDial8snapModeEv(
    const QQuickDial *self) {
  return self->snapMode();
}

//  void QQuickDial::setSnapMode(SnapMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDial11setSnapModeENS_8SnapModeE(
    QQuickDial *self,
    QQuickDial::SnapMode mode) {
  self->setSnapMode(mode);
}

//  bool QQuickDial::wrap() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QQuickDial4wrapEv(const QQuickDial *self) {
  return self->wrap();
}

//  void QQuickDial::setWrap(bool wrap)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDial7setWrapEb(QQuickDial *self, bool wrap) {
  self->setWrap(wrap);
}

//  bool QQuickDial::isPressed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QQuickDial9isPressedEv(const QQuickDial *self) {
  return self->isPressed();
}

//  void QQuickDial::setPressed(bool pressed)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDial10setPressedEb(QQuickDial *self, bool pressed) {
  self->setPressed(pressed);
}

//  QQuickItem *QQuickDial::handle() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK10QQuickDial6handleEv(const QQuickDial *self) {
  return self->handle();
}

//  void QQuickDial::setHandle(QQuickItem *handle)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDial9setHandleEP10QQuickItem(
    QQuickDial *self,
    QQuickItem *handle) {
  self->setHandle(handle);
}

//  bool QQuickDial::live() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QQuickDial4liveEv(const QQuickDial *self) {
  return self->live();
}

//  void QQuickDial::setLive(bool live)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDial7setLiveEb(QQuickDial *self, bool live) {
  self->setLive(live);
}

//  InputMode QQuickDial::inputMode() const
extern "C" Q_DECL_EXPORT
QQuickDial::InputMode ritual_ZNK10QQuickDial9inputModeEv(
    const QQuickDial *self) {
  return self->inputMode();
}

//  void QQuickDial::setInputMode(InputMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDial12setInputModeENS_9InputModeE(
    QQuickDial *self,
    QQuickDial::InputMode mode) {
  self->setInputMode(mode);
}

//  void QQuickDial::increase()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDial8increaseEv(QQuickDial *self) {
  self->increase();
}

//  void QQuickDial::decrease()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDial8decreaseEv(QQuickDial *self) {
  self->decrease();
}

//  void QQuickDial::fromChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDial11fromChangedEv(QQuickDial *self) {
  self->fromChanged();
}

//  void QQuickDial::toChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDial9toChangedEv(QQuickDial *self) {
  self->toChanged();
}

//  void QQuickDial::valueChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDial12valueChangedEv(QQuickDial *self) {
  self->valueChanged();
}

//  void QQuickDial::positionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDial15positionChangedEv(QQuickDial *self) {
  self->positionChanged();
}

//  void QQuickDial::angleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDial12angleChangedEv(QQuickDial *self) {
  self->angleChanged();
}

//  void QQuickDial::stepSizeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDial15stepSizeChangedEv(QQuickDial *self) {
  self->stepSizeChanged();
}

//  void QQuickDial::snapModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDial15snapModeChangedEv(QQuickDial *self) {
  self->snapModeChanged();
}

//  void QQuickDial::wrapChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDial11wrapChangedEv(QQuickDial *self) {
  self->wrapChanged();
}

//  void QQuickDial::pressedChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDial14pressedChangedEv(QQuickDial *self) {
  self->pressedChanged();
}

//  void QQuickDial::handleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDial13handleChangedEv(QQuickDial *self) {
  self->handleChanged();
}

//  void QQuickDial::moved()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDial5movedEv(QQuickDial *self) {
  self->moved();
}

//  void QQuickDial::liveChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDial11liveChangedEv(QQuickDial *self) {
  self->liveChanged();
}

//  void QQuickDial::inputModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDial16inputModeChangedEv(QQuickDial *self) {
  self->inputModeChanged();
}

//  void QQuickDial::startAngleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDial17startAngleChangedEv(QQuickDial *self) {
  self->startAngleChanged();
}

//  void QQuickDial::endAngleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDial15endAngleChangedEv(QQuickDial *self) {
  self->endAngleChanged();
}

//  void QQuickDial::wrapped(WrapDirection a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDial7wrappedENS_13WrapDirectionE(
    QQuickDial *self,
    QQuickDial::WrapDirection a0) {
  self->wrapped(a0);
}

//  void QQuickDial::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDial13keyPressEventEP9QKeyEvent(
    QQuickDial *self,
    QKeyEvent *event) {
  self->keyPressEvent(event);
}

//  void QQuickDial::keyReleaseEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDial15keyReleaseEventEP9QKeyEvent(
    QQuickDial *self,
    QKeyEvent *event) {
  self->keyReleaseEvent(event);
}

//  void QQuickDial::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDial15mousePressEventEP11QMouseEvent(
    QQuickDial *self,
    QMouseEvent *event) {
  self->mousePressEvent(event);
}

#if QT_CONFIG(quicktemplates2_multitouch)
//  void QQuickDial::touchEvent(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDial10touchEventEP11QTouchEvent(
    QQuickDial *self,
    QTouchEvent *event) {
  self->touchEvent(event);
}
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(wheelevent)
//  void QQuickDial::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDial10wheelEventEP11QWheelEvent(
    QQuickDial *self,
    QWheelEvent *event) {
  self->wheelEvent(event);
}
#endif  // QT_CONFIG(wheelevent)

//  void QQuickDial::mirrorChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDial12mirrorChangeEv(QQuickDial *self) {
  self->mirrorChange();
}

//  void QQuickDial::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDial17componentCompleteEv(QQuickDial *self) {
  self->componentComplete();
}

#if QT_CONFIG(accessibility)
//  void QQuickDial::accessibilityActiveChanged(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDial26accessibilityActiveChangedEb(
    QQuickDial *self,
    bool active) {
  self->accessibilityActiveChanged(active);
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickDial::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK10QQuickDial14accessibleRoleEv(
    const QQuickDial *self) {
  return self->accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

//  QQuickDialPrivate *QQuickDial::d_func()
extern "C" Q_DECL_EXPORT
QQuickDialPrivate *ritual_ZN10QQuickDial6d_funcEv(QQuickDial *self) {
  return self->d_func();
}

//  const QQuickDialPrivate *QQuickDial::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickDialPrivate *ritual_ZNK10QQuickDial6d_funcEv(
    const QQuickDial *self) {
  return self->d_func();
}

//  void QQuickDial::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickDial13keyPressEventEP9QKeyEvent(
    QQuickDial *self,
    QKeyEvent *event) {
  static_cast<OwnQQuickDial *>(self)->OwnQQuickDial::keyPressEvent(event);
}

//  void QQuickDial::keyReleaseEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickDial15keyReleaseEventEP9QKeyEvent(
    QQuickDial *self,
    QKeyEvent *event) {
  static_cast<OwnQQuickDial *>(self)->OwnQQuickDial::keyReleaseEvent(event);
}

//  void QQuickDial::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickDial15mousePressEventEP11QMouseEvent(
    QQuickDial *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickDial *>(self)->OwnQQuickDial::mousePressEvent(event);
}

#if QT_CONFIG(quicktemplates2_multitouch)
//  void QQuickDial::touchEvent(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickDial10touchEventEP11QTouchEvent(
    QQuickDial *self,
    QTouchEvent *event) {
  static_cast<OwnQQuickDial *>(self)->OwnQQuickDial::touchEvent(event);
}
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(wheelevent)
//  void QQuickDial::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickDial10wheelEventEP11QWheelEvent(
    QQuickDial *self,
    QWheelEvent *event) {
  static_cast<OwnQQuickDial *>(self)->OwnQQuickDial::wheelEvent(event);
}
#endif  // QT_CONFIG(wheelevent)

//  void QQuickDial::mirrorChange()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickDial12mirrorChangeEv(QQuickDial *self) {
  static_cast<OwnQQuickDial *>(self)->OwnQQuickDial::mirrorChange();
}

//  void QQuickDial::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickDial17componentCompleteEv(QQuickDial *self) {
  static_cast<OwnQQuickDial *>(self)->OwnQQuickDial::componentComplete();
}

#if QT_CONFIG(accessibility)
//  void QQuickDial::accessibilityActiveChanged(bool active)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickDial26accessibilityActiveChangedEb(
    QQuickDial *self,
    bool active) {
  static_cast<OwnQQuickDial *>(self)->OwnQQuickDial::accessibilityActiveChanged(
      active);
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickDial::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK10QQuickDial14accessibleRoleEv(
    const QQuickDial *self) {
  return static_cast<const OwnQQuickDial *>(self)->OwnQQuickDial::accessibleRole();
}
#endif  // QT_CONFIG(accessibility)
