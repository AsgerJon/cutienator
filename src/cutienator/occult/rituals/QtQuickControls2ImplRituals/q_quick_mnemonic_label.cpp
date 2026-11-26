//  Written by dev_tooling.RitualGenerator from the records of QtQuickControl
//  s2Impl/6.12.0/QtQuickControls2Impl/private/qquickmnemoniclabel_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qtquickcontrols2implglobal_p.h>
#include <QtQuickControls2Impl/QtQuickControls2Impl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qquickmnemoniclabel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuickMnemonicLabel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuickMnemonicLabel10metaObjectEv(
    const QQuickMnemonicLabel *self) {
  return self->metaObject();
}

//  void *QQuickMnemonicLabel::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QQuickMnemonicLabel11qt_metacastEPKc(
    QQuickMnemonicLabel *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickMnemonicLabel::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QQuickMnemonicLabel11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickMnemonicLabel *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickMnemonicLabel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQuickMnemonicLabel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickMnemonicLabel::tr(s, c, n));
}

//  QQuickMnemonicLabel::QQuickMnemonicLabel(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickMnemonicLabel *ritual_ZN19QQuickMnemonicLabelC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickMnemonicLabel(parent);
}

//  QString QQuickMnemonicLabel::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQuickMnemonicLabel4textEv(
    const QQuickMnemonicLabel *self) {
  return new QString(self->text());
}

//  void QQuickMnemonicLabel::setText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMnemonicLabel7setTextERK7QString(
    QQuickMnemonicLabel *self,
    const QString *text) {
  self->setText(*text);
}

//  bool QQuickMnemonicLabel::isMnemonicVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickMnemonicLabel17isMnemonicVisibleEv(
    const QQuickMnemonicLabel *self) {
  return self->isMnemonicVisible();
}

//  void QQuickMnemonicLabel::setMnemonicVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMnemonicLabel18setMnemonicVisibleEb(
    QQuickMnemonicLabel *self,
    bool visible) {
  self->setMnemonicVisible(visible);
}

//  void QQuickMnemonicLabel::updateMnemonic()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickMnemonicLabel14updateMnemonicEv(
    QQuickMnemonicLabel *self) {
  self->updateMnemonic();
}
