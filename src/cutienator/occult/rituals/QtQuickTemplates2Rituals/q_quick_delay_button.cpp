//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickdelaybutton_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickdelaybutton_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>

//  Only a class built on QQuickDelayButton may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickDelayButton : QQuickDelayButton {
  using QQuickDelayButton::nextCheckState;
  using QQuickDelayButton::defaultFont;
};

//  const QMetaObject *QQuickDelayButton::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQuickDelayButton10metaObjectEv(
    const QQuickDelayButton *self) {
  return self->metaObject();
}

//  void *QQuickDelayButton::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QQuickDelayButton11qt_metacastEPKc(
    QQuickDelayButton *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickDelayButton::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QQuickDelayButton11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickDelayButton *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickDelayButton::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QQuickDelayButton2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickDelayButton::tr(s, c, n));
}

//  QQuickDelayButton::QQuickDelayButton(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickDelayButton *ritual_ZN17QQuickDelayButtonC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickDelayButton(parent);
}

//  int QQuickDelayButton::delay() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQuickDelayButton5delayEv(const QQuickDelayButton *self) {
  return self->delay();
}

//  void QQuickDelayButton::setDelay(int delay)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickDelayButton8setDelayEi(
    QQuickDelayButton *self,
    int delay) {
  self->setDelay(delay);
}

//  qreal QQuickDelayButton::progress() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickDelayButton8progressEv(
    const QQuickDelayButton *self) {
  return self->progress();
}

//  void QQuickDelayButton::setProgress(qreal progress)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickDelayButton11setProgressEd(
    QQuickDelayButton *self,
    qreal progress) {
  self->setProgress(progress);
}

//  QQuickTransition *QQuickDelayButton::transition() const
extern "C" Q_DECL_EXPORT
QQuickTransition *ritual_ZNK17QQuickDelayButton10transitionEv(
    const QQuickDelayButton *self) {
  return self->transition();
}

//  void QQuickDelayButton::setTransition(QQuickTransition *transition)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickDelayButton13setTransitionEP16QQuickTransition(
    QQuickDelayButton *self,
    QQuickTransition *transition) {
  self->setTransition(transition);
}

//  void QQuickDelayButton::activated()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickDelayButton9activatedEv(QQuickDelayButton *self) {
  self->activated();
}

//  void QQuickDelayButton::delayChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickDelayButton12delayChangedEv(QQuickDelayButton *self) {
  self->delayChanged();
}

//  void QQuickDelayButton::progressChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickDelayButton15progressChangedEv(
    QQuickDelayButton *self) {
  self->progressChanged();
}

//  void QQuickDelayButton::transitionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickDelayButton17transitionChangedEv(
    QQuickDelayButton *self) {
  self->transitionChanged();
}

//  void QQuickDelayButton::buttonChange(ButtonChange change)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickDelayButton12buttonChangeEN20QQuickAbstractButton12ButtonChangeE(
    QQuickDelayButton *self,
    QQuickAbstractButton::ButtonChange change) {
  self->buttonChange(change);
}

//  void QQuickDelayButton::nextCheckState()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickDelayButton14nextCheckStateEv(
    QQuickDelayButton *self) {
  self->nextCheckState();
}

//  QFont QQuickDelayButton::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK17QQuickDelayButton11defaultFontEv(
    const QQuickDelayButton *self) {
  return new QFont(self->defaultFont());
}

//  QQuickDelayButtonPrivate *QQuickDelayButton::d_func()
extern "C" Q_DECL_EXPORT
QQuickDelayButtonPrivate *ritual_ZN17QQuickDelayButton6d_funcEv(
    QQuickDelayButton *self) {
  return self->d_func();
}

//  const QQuickDelayButtonPrivate *QQuickDelayButton::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickDelayButtonPrivate *ritual_ZNK17QQuickDelayButton6d_funcEv(
    const QQuickDelayButton *self) {
  return self->d_func();
}

//  void QQuickDelayButton::nextCheckState()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickDelayButton14nextCheckStateEv(
    QQuickDelayButton *self) {
  static_cast<OwnQQuickDelayButton *>(self)->OwnQQuickDelayButton::nextCheckState();
}

//  QFont QQuickDelayButton::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_own_ZNK17QQuickDelayButton11defaultFontEv(
    const QQuickDelayButton *self) {
  return new QFont(
      static_cast<const OwnQQuickDelayButton *>(self)->OwnQQuickDelayButton::defaultFont());
}
