//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickswitchdelegate_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickswitchdelegate_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>

//  Only a class built on QQuickSwitchDelegate may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickSwitchDelegate : QQuickSwitchDelegate {
  using QQuickSwitchDelegate::mouseMoveEvent;
  using QQuickSwitchDelegate::touchEvent;
  using QQuickSwitchDelegate::defaultFont;
  using QQuickSwitchDelegate::mirrorChange;
  using QQuickSwitchDelegate::nextCheckState;
};

//  const QMetaObject *QQuickSwitchDelegate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQuickSwitchDelegate10metaObjectEv(
    const QQuickSwitchDelegate *self) {
  return self->metaObject();
}

//  QString QQuickSwitchDelegate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQuickSwitchDelegate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickSwitchDelegate::tr(s, c, n));
}

//  QQuickSwitchDelegate::QQuickSwitchDelegate(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickSwitchDelegate *ritual_ZN20QQuickSwitchDelegateC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickSwitchDelegate(parent);
}

//  qreal QQuickSwitchDelegate::position() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickSwitchDelegate8positionEv(
    const QQuickSwitchDelegate *self) {
  return self->position();
}

//  void QQuickSwitchDelegate::setPosition(qreal position)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickSwitchDelegate11setPositionEd(
    QQuickSwitchDelegate *self,
    qreal position) {
  self->setPosition(position);
}

//  qreal QQuickSwitchDelegate::visualPosition() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickSwitchDelegate14visualPositionEv(
    const QQuickSwitchDelegate *self) {
  return self->visualPosition();
}

//  void QQuickSwitchDelegate::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickSwitchDelegate14mouseMoveEventEP11QMouseEvent(
    QQuickSwitchDelegate *self,
    QMouseEvent *event) {
  self->mouseMoveEvent(event);
}

#if QT_CONFIG(quicktemplates2_multitouch)
//  void QQuickSwitchDelegate::touchEvent(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickSwitchDelegate10touchEventEP11QTouchEvent(
    QQuickSwitchDelegate *self,
    QTouchEvent *event) {
  self->touchEvent(event);
}
#endif  // QT_CONFIG(quicktemplates2_multitouch)

//  QFont QQuickSwitchDelegate::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK20QQuickSwitchDelegate11defaultFontEv(
    const QQuickSwitchDelegate *self) {
  return new QFont(self->defaultFont());
}

//  void QQuickSwitchDelegate::mirrorChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickSwitchDelegate12mirrorChangeEv(
    QQuickSwitchDelegate *self) {
  self->mirrorChange();
}

//  void QQuickSwitchDelegate::nextCheckState()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickSwitchDelegate14nextCheckStateEv(
    QQuickSwitchDelegate *self) {
  self->nextCheckState();
}

//  void QQuickSwitchDelegate::buttonChange(ButtonChange change)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickSwitchDelegate12buttonChangeEN20QQuickAbstractButton12ButtonChangeE(
    QQuickSwitchDelegate *self,
    QQuickAbstractButton::ButtonChange change) {
  self->buttonChange(change);
}

//  void QQuickSwitchDelegate::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickSwitchDelegate14mouseMoveEventEP11QMouseEvent(
    QQuickSwitchDelegate *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickSwitchDelegate *>(self)->OwnQQuickSwitchDelegate::mouseMoveEvent(
      event);
}

#if QT_CONFIG(quicktemplates2_multitouch)
//  void QQuickSwitchDelegate::touchEvent(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickSwitchDelegate10touchEventEP11QTouchEvent(
    QQuickSwitchDelegate *self,
    QTouchEvent *event) {
  static_cast<OwnQQuickSwitchDelegate *>(self)->OwnQQuickSwitchDelegate::touchEvent(
      event);
}
#endif  // QT_CONFIG(quicktemplates2_multitouch)

//  QFont QQuickSwitchDelegate::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_own_ZNK20QQuickSwitchDelegate11defaultFontEv(
    const QQuickSwitchDelegate *self) {
  return new QFont(
      static_cast<const OwnQQuickSwitchDelegate *>(self)->OwnQQuickSwitchDelegate::defaultFont());
}

//  void QQuickSwitchDelegate::mirrorChange()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickSwitchDelegate12mirrorChangeEv(
    QQuickSwitchDelegate *self) {
  static_cast<OwnQQuickSwitchDelegate *>(self)->OwnQQuickSwitchDelegate::mirrorChange();
}

//  void QQuickSwitchDelegate::nextCheckState()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickSwitchDelegate14nextCheckStateEv(
    QQuickSwitchDelegate *self) {
  static_cast<OwnQQuickSwitchDelegate *>(self)->OwnQQuickSwitchDelegate::nextCheckState();
}
