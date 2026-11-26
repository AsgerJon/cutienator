//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickevents_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/qglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickevents_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuickKeyEvent::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQuickKeyEvent10metaObjectEv(
    const QQuickKeyEvent *self) {
  return self->metaObject();
}

//  void *QQuickKeyEvent::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QQuickKeyEvent11qt_metacastEPKc(
    QQuickKeyEvent *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickKeyEvent::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QQuickKeyEvent11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickKeyEvent *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickKeyEvent::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QQuickKeyEvent2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickKeyEvent::tr(s, c, n));
}

//  void QQuickKeyEvent::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickKeyEvent24qt_qmlMarker_uncreatableEv(
    QQuickKeyEvent *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuickKeyEvent::QQuickKeyEvent()
extern "C" Q_DECL_EXPORT
QQuickKeyEvent *ritual_ZN14QQuickKeyEventC1Ev() {
  return new QQuickKeyEvent();
}

//  void QQuickKeyEvent::reset(QEvent::Type type, int key,
//      Qt::KeyboardModifiers modifiers, const QString &text, bool autorep,
//      ushort count)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickKeyEvent5resetEN6QEvent4TypeEi6QFlagsIN2Qt16KeyboardModifierEERK7QStringbt(
    QQuickKeyEvent *self,
    QEvent::Type type,
    int key,
    int modifiers,
    const QString *text,
    bool autorep,
    ushort count) {
  self->reset(
      type,
      key,
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers),
      *text,
      autorep,
      count);
}

//  void QQuickKeyEvent::reset(const QKeyEvent &ke)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickKeyEvent5resetERK9QKeyEvent(
    QQuickKeyEvent *self,
    const QKeyEvent *ke) {
  self->reset(*ke);
}

//  int QQuickKeyEvent::key() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQuickKeyEvent3keyEv(const QQuickKeyEvent *self) {
  return self->key();
}

//  QString QQuickKeyEvent::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QQuickKeyEvent4textEv(const QQuickKeyEvent *self) {
  return new QString(self->text());
}

//  int QQuickKeyEvent::modifiers() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQuickKeyEvent9modifiersEv(const QQuickKeyEvent *self) {
  return self->modifiers();
}

//  bool QQuickKeyEvent::isAutoRepeat() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuickKeyEvent12isAutoRepeatEv(const QQuickKeyEvent *self) {
  return self->isAutoRepeat();
}

//  int QQuickKeyEvent::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQuickKeyEvent5countEv(const QQuickKeyEvent *self) {
  return self->count();
}

//  quint32 QQuickKeyEvent::nativeScanCode() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK14QQuickKeyEvent14nativeScanCodeEv(
    const QQuickKeyEvent *self) {
  return self->nativeScanCode();
}

//  bool QQuickKeyEvent::isAccepted()
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QQuickKeyEvent10isAcceptedEv(QQuickKeyEvent *self) {
  return self->isAccepted();
}

//  void QQuickKeyEvent::setAccepted(bool accepted)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickKeyEvent11setAcceptedEb(
    QQuickKeyEvent *self,
    bool accepted) {
  self->setAccepted(accepted);
}

#if QT_CONFIG(shortcut)
//  bool QQuickKeyEvent::matches(QKeySequence::StandardKey key) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuickKeyEvent7matchesEN12QKeySequence11StandardKeyE(
    const QQuickKeyEvent *self,
    QKeySequence::StandardKey key) {
  return self->matches(key);
}
#endif  // QT_CONFIG(shortcut)
