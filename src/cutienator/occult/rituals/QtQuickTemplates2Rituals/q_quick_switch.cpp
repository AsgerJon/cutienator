//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickswitch_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickswitch_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>

//  Only a class built on QQuickSwitch may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickSwitch : QQuickSwitch {
  using QQuickSwitch::mouseMoveEvent;
  using QQuickSwitch::touchEvent;
  using QQuickSwitch::mirrorChange;
  using QQuickSwitch::nextCheckState;
  using QQuickSwitch::defaultFont;
};

//  const QMetaObject *QQuickSwitch::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QQuickSwitch10metaObjectEv(
    const QQuickSwitch *self) {
  return self->metaObject();
}

//  void *QQuickSwitch::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN12QQuickSwitch11qt_metacastEPKc(
    QQuickSwitch *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickSwitch::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QQuickSwitch11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickSwitch *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickSwitch::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QQuickSwitch2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickSwitch::tr(s, c, n));
}

//  QQuickSwitch::QQuickSwitch(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickSwitch *ritual_ZN12QQuickSwitchC1EP10QQuickItem(QQuickItem *parent) {
  return new QQuickSwitch(parent);
}

//  qreal QQuickSwitch::position() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QQuickSwitch8positionEv(const QQuickSwitch *self) {
  return self->position();
}

//  void QQuickSwitch::setPosition(qreal position)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSwitch11setPositionEd(
    QQuickSwitch *self,
    qreal position) {
  self->setPosition(position);
}

//  qreal QQuickSwitch::visualPosition() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QQuickSwitch14visualPositionEv(const QQuickSwitch *self) {
  return self->visualPosition();
}

//  void QQuickSwitch::positionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSwitch15positionChangedEv(QQuickSwitch *self) {
  self->positionChanged();
}

//  void QQuickSwitch::visualPositionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSwitch21visualPositionChangedEv(QQuickSwitch *self) {
  self->visualPositionChanged();
}

//  void QQuickSwitch::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSwitch14mouseMoveEventEP11QMouseEvent(
    QQuickSwitch *self,
    QMouseEvent *event) {
  self->mouseMoveEvent(event);
}

#if QT_CONFIG(quicktemplates2_multitouch)
//  void QQuickSwitch::touchEvent(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSwitch10touchEventEP11QTouchEvent(
    QQuickSwitch *self,
    QTouchEvent *event) {
  self->touchEvent(event);
}
#endif  // QT_CONFIG(quicktemplates2_multitouch)

//  void QQuickSwitch::mirrorChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSwitch12mirrorChangeEv(QQuickSwitch *self) {
  self->mirrorChange();
}

//  void QQuickSwitch::nextCheckState()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSwitch14nextCheckStateEv(QQuickSwitch *self) {
  self->nextCheckState();
}

//  void QQuickSwitch::buttonChange(ButtonChange change)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickSwitch12buttonChangeEN20QQuickAbstractButton12ButtonChangeE(
    QQuickSwitch *self,
    QQuickAbstractButton::ButtonChange change) {
  self->buttonChange(change);
}

//  QFont QQuickSwitch::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK12QQuickSwitch11defaultFontEv(const QQuickSwitch *self) {
  return new QFont(self->defaultFont());
}

//  QQuickSwitchPrivate *QQuickSwitch::d_func()
extern "C" Q_DECL_EXPORT
QQuickSwitchPrivate *ritual_ZN12QQuickSwitch6d_funcEv(QQuickSwitch *self) {
  return self->d_func();
}

//  const QQuickSwitchPrivate *QQuickSwitch::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickSwitchPrivate *ritual_ZNK12QQuickSwitch6d_funcEv(
    const QQuickSwitch *self) {
  return self->d_func();
}

//  void QQuickSwitch::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickSwitch14mouseMoveEventEP11QMouseEvent(
    QQuickSwitch *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickSwitch *>(self)->OwnQQuickSwitch::mouseMoveEvent(
      event);
}

#if QT_CONFIG(quicktemplates2_multitouch)
//  void QQuickSwitch::touchEvent(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickSwitch10touchEventEP11QTouchEvent(
    QQuickSwitch *self,
    QTouchEvent *event) {
  static_cast<OwnQQuickSwitch *>(self)->OwnQQuickSwitch::touchEvent(event);
}
#endif  // QT_CONFIG(quicktemplates2_multitouch)

//  void QQuickSwitch::mirrorChange()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickSwitch12mirrorChangeEv(QQuickSwitch *self) {
  static_cast<OwnQQuickSwitch *>(self)->OwnQQuickSwitch::mirrorChange();
}

//  void QQuickSwitch::nextCheckState()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQuickSwitch14nextCheckStateEv(QQuickSwitch *self) {
  static_cast<OwnQQuickSwitch *>(self)->OwnQQuickSwitch::nextCheckState();
}

//  QFont QQuickSwitch::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_own_ZNK12QQuickSwitch11defaultFontEv(
    const QQuickSwitch *self) {
  return new QFont(
      static_cast<const OwnQQuickSwitch *>(self)->OwnQQuickSwitch::defaultFont());
}
