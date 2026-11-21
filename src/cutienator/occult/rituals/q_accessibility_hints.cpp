//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessibilityhints.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessibilityhints.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QAccessibilityHints::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QAccessibilityHints10metaObjectEv(
    const QAccessibilityHints *self) {
  return self->metaObject();
}

//  QString QAccessibilityHints::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QAccessibilityHints2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAccessibilityHints::tr(s, c, n));
}

//  QAccessibilityHints::QAccessibilityHints(QObject *parent)
extern "C" Q_DECL_EXPORT
QAccessibilityHints *ritual_ZN19QAccessibilityHintsC1EP7QObject(
    QObject *parent) {
  return new QAccessibilityHints(parent);
}

//  QAccessibilityHints::~QAccessibilityHints()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAccessibilityHintsD1Ev(QAccessibilityHints *self) {
  delete self;
}

//  Qt::ContrastPreference QAccessibilityHints::contrastPreference() const
extern "C" Q_DECL_EXPORT
Qt::ContrastPreference ritual_ZNK19QAccessibilityHints18contrastPreferenceEv(
    const QAccessibilityHints *self) {
  return self->contrastPreference();
}

//  Qt::MotionPreference QAccessibilityHints::motionPreference() const
extern "C" Q_DECL_EXPORT
Qt::MotionPreference ritual_ZNK19QAccessibilityHints16motionPreferenceEv(
    const QAccessibilityHints *self) {
  return self->motionPreference();
}
