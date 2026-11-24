//  Written by dev_tooling.RitualGenerator from the records of QtQuickDialogs
//  2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickcolorinputs_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#include <QtQuickDialogs2QuickImpl/QtQuickDialogs2QuickImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickcolorinputs_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>

//  Only a class built on QQuickColorInputs may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickColorInputs : QQuickColorInputs {
  using QQuickColorInputs::componentComplete;
};

//  const QMetaObject *QQuickColorInputs::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQuickColorInputs10metaObjectEv(
    const QQuickColorInputs *self) {
  return self->metaObject();
}

//  QString QQuickColorInputs::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QQuickColorInputs2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickColorInputs::tr(s, c, n));
}

//  QQuickColorInputs::QQuickColorInputs(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickColorInputs *ritual_ZN17QQuickColorInputsC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickColorInputs(parent);
}

//  Mode QQuickColorInputs::currentMode() const
extern "C" Q_DECL_EXPORT
QQuickColorInputs::Mode ritual_ZNK17QQuickColorInputs11currentModeEv(
    const QQuickColorInputs *self) {
  return self->currentMode();
}

//  void QQuickColorInputs::setCurrentMode(Mode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickColorInputs14setCurrentModeENS_4ModeE(
    QQuickColorInputs *self,
    QQuickColorInputs::Mode mode) {
  self->setCurrentMode(mode);
}

//  QQmlComponent *QQuickColorInputs::delegate() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK17QQuickColorInputs8delegateEv(
    const QQuickColorInputs *self) {
  return self->delegate();
}

//  void QQuickColorInputs::setDelegate(QQmlComponent *delegate)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickColorInputs11setDelegateEP13QQmlComponent(
    QQuickColorInputs *self,
    QQmlComponent *delegate) {
  self->setDelegate(delegate);
}

//  QColor QQuickColorInputs::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK17QQuickColorInputs5colorEv(
    const QQuickColorInputs *self) {
  return new QColor(self->color());
}

//  void QQuickColorInputs::setColor(const QColor &c)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickColorInputs8setColorERK6QColor(
    QQuickColorInputs *self,
    const QColor *c) {
  self->setColor(*c);
}

//  int QQuickColorInputs::red() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQuickColorInputs3redEv(const QQuickColorInputs *self) {
  return self->red();
}

//  int QQuickColorInputs::green() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQuickColorInputs5greenEv(const QQuickColorInputs *self) {
  return self->green();
}

//  int QQuickColorInputs::blue() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQuickColorInputs4blueEv(const QQuickColorInputs *self) {
  return self->blue();
}

//  qreal QQuickColorInputs::alpha() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickColorInputs5alphaEv(const QQuickColorInputs *self) {
  return self->alpha();
}

//  qreal QQuickColorInputs::hue() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickColorInputs3hueEv(const QQuickColorInputs *self) {
  return self->hue();
}

//  qreal QQuickColorInputs::hslSaturation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickColorInputs13hslSaturationEv(
    const QQuickColorInputs *self) {
  return self->hslSaturation();
}

//  qreal QQuickColorInputs::hsvSaturation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickColorInputs13hsvSaturationEv(
    const QQuickColorInputs *self) {
  return self->hsvSaturation();
}

//  qreal QQuickColorInputs::value() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickColorInputs5valueEv(const QQuickColorInputs *self) {
  return self->value();
}

//  qreal QQuickColorInputs::lightness() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickColorInputs9lightnessEv(
    const QQuickColorInputs *self) {
  return self->lightness();
}

//  bool QQuickColorInputs::showAlpha() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickColorInputs9showAlphaEv(
    const QQuickColorInputs *self) {
  return self->showAlpha();
}

//  void QQuickColorInputs::setShowAlpha(bool showAlpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickColorInputs12setShowAlphaEb(
    QQuickColorInputs *self,
    bool showAlpha) {
  self->setShowAlpha(showAlpha);
}

//  void QQuickColorInputs::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickColorInputs17componentCompleteEv(
    QQuickColorInputs *self) {
  self->componentComplete();
}

//  void QQuickColorInputs::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickColorInputs17componentCompleteEv(
    QQuickColorInputs *self) {
  static_cast<OwnQQuickColorInputs *>(self)->OwnQQuickColorInputs::componentComplete();
}
