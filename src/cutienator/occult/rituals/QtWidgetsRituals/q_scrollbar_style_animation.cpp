//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qstyleanimation_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(animation)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qstyleanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QScrollbarStyleAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QScrollbarStyleAnimation10metaObjectEv(
    const QScrollbarStyleAnimation *self) {
  return self->metaObject();
}

//  QString QScrollbarStyleAnimation::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QScrollbarStyleAnimation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QScrollbarStyleAnimation::tr(s, c, n));
}

//  QScrollbarStyleAnimation::QScrollbarStyleAnimation(Mode mode, QObject
//      *target)
extern "C" Q_DECL_EXPORT
QScrollbarStyleAnimation *ritual_ZN24QScrollbarStyleAnimationC1ENS_4ModeEP7QObject(
    QScrollbarStyleAnimation::Mode mode,
    QObject *target) {
  return new QScrollbarStyleAnimation(mode, target);
}

//  Mode QScrollbarStyleAnimation::mode() const
extern "C" Q_DECL_EXPORT
QScrollbarStyleAnimation::Mode ritual_ZNK24QScrollbarStyleAnimation4modeEv(
    const QScrollbarStyleAnimation *self) {
  return self->mode();
}

//  bool QScrollbarStyleAnimation::wasActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QScrollbarStyleAnimation9wasActiveEv(
    const QScrollbarStyleAnimation *self) {
  return self->wasActive();
}

//  void QScrollbarStyleAnimation::setActive(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QScrollbarStyleAnimation9setActiveEb(
    QScrollbarStyleAnimation *self,
    bool active) {
  self->setActive(active);
}

//  void QScrollbarStyleAnimation::updateCurrentTime(int time)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QScrollbarStyleAnimation17updateCurrentTimeEi(
    QScrollbarStyleAnimation *self,
    int time) {
  self->updateCurrentTime(time);
}

//  void QScrollbarStyleAnimation::updateCurrentTime(int time)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QScrollbarStyleAnimation17updateCurrentTimeEi(
    QScrollbarStyleAnimation *self,
    int time) {
  self->QScrollbarStyleAnimation::updateCurrentTime(time);
}

#endif  // QT_CONFIG(animation)
