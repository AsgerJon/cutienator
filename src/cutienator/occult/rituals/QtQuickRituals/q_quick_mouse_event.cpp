//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickevents_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickevents_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>

//  const QMetaObject *QQuickMouseEvent::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQuickMouseEvent10metaObjectEv(
    const QQuickMouseEvent *self) {
  return self->metaObject();
}

//  QString QQuickMouseEvent::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QQuickMouseEvent2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickMouseEvent::tr(s, c, n));
}

//  void QQuickMouseEvent::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickMouseEvent24qt_qmlMarker_uncreatableEv(
    QQuickMouseEvent *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuickMouseEvent::QQuickMouseEvent()
extern "C" Q_DECL_EXPORT
QQuickMouseEvent *ritual_ZN16QQuickMouseEventC1Ev() {
  return new QQuickMouseEvent();
}

//  void QQuickMouseEvent::reset(qreal x, qreal y, Qt::MouseButton button,
//      Qt::MouseButtons buttons, Qt::KeyboardModifiers modifiers, bool
//      isClick, bool wasHeld, Qt::MouseEventFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickMouseEvent5resetEddN2Qt11MouseButtonE6QFlagsIS1_ES2_INS0_16KeyboardModifierEEbbS2_INS0_14MouseEventFlagEE(
    QQuickMouseEvent *self,
    qreal x,
    qreal y,
    Qt::MouseButton button,
    int buttons,
    int modifiers,
    bool isClick,
    bool wasHeld,
    int flags) {
  self->reset(
      x,
      y,
      button,
      QFlags<Qt::MouseButton>::fromInt(buttons),
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers),
      isClick,
      wasHeld,
      QFlags<Qt::MouseEventFlag>::fromInt(flags));
}

//  qreal QQuickMouseEvent::x() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QQuickMouseEvent1xEv(const QQuickMouseEvent *self) {
  return self->x();
}

//  qreal QQuickMouseEvent::y() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QQuickMouseEvent1yEv(const QQuickMouseEvent *self) {
  return self->y();
}

//  int QQuickMouseEvent::button() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQuickMouseEvent6buttonEv(const QQuickMouseEvent *self) {
  return self->button();
}

//  int QQuickMouseEvent::buttons() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQuickMouseEvent7buttonsEv(const QQuickMouseEvent *self) {
  return self->buttons();
}

//  int QQuickMouseEvent::modifiers() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQuickMouseEvent9modifiersEv(const QQuickMouseEvent *self) {
  return self->modifiers();
}

#if QT_DEPRECATED_SINCE(6, 6)
//  int QQuickMouseEvent::source() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQuickMouseEvent6sourceEv(const QQuickMouseEvent *self) {
  return self->source();
}
#endif  // QT_DEPRECATED_SINCE(6, 6)

//  bool QQuickMouseEvent::wasHeld() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuickMouseEvent7wasHeldEv(const QQuickMouseEvent *self) {
  return self->wasHeld();
}

//  bool QQuickMouseEvent::isClick() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuickMouseEvent7isClickEv(const QQuickMouseEvent *self) {
  return self->isClick();
}

//  void QQuickMouseEvent::setX(qreal x)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickMouseEvent4setXEd(QQuickMouseEvent *self, qreal x) {
  self->setX(x);
}

//  void QQuickMouseEvent::setY(qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickMouseEvent4setYEd(QQuickMouseEvent *self, qreal y) {
  self->setY(y);
}

//  void QQuickMouseEvent::setPosition(const QPointF &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickMouseEvent11setPositionERK7QPointF(
    QQuickMouseEvent *self,
    const QPointF *point) {
  self->setPosition(*point);
}

#if QT_DEPRECATED_SINCE(6, 6)
//  void QQuickMouseEvent::setSource(Qt::MouseEventSource s)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickMouseEvent9setSourceEN2Qt16MouseEventSourceE(
    QQuickMouseEvent *self,
    Qt::MouseEventSource s) {
  self->setSource(s);
}
#endif  // QT_DEPRECATED_SINCE(6, 6)

//  bool QQuickMouseEvent::isAccepted()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QQuickMouseEvent10isAcceptedEv(QQuickMouseEvent *self) {
  return self->isAccepted();
}

//  void QQuickMouseEvent::setAccepted(bool accepted)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickMouseEvent11setAcceptedEb(
    QQuickMouseEvent *self,
    bool accepted) {
  self->setAccepted(accepted);
}

//  int QQuickMouseEvent::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQuickMouseEvent5flagsEv(const QQuickMouseEvent *self) {
  return self->flags();
}
