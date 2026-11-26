//  Written by dev_tooling.RitualGenerator from the records of QtQuickTimelin
//  e/6.12.0/QtQuickTimeline/private/qquicktimelineanimation_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuickTimeline/6.12.0/QtQuickTimeline/private/qtquicktimelineglobal_p.h>
#include <QtQuickTimeline/QtQuickTimeline>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTimeline/6.12.0/QtQuickTimeline/private/qquicktimelineanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  const QMetaObject *QQuickTimelineAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQuickTimelineAnimation10metaObjectEv(
    const QQuickTimelineAnimation *self) {
  return self->metaObject();
}

//  void *QQuickTimelineAnimation::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN23QQuickTimelineAnimation11qt_metacastEPKc(
    QQuickTimelineAnimation *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickTimelineAnimation::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QQuickTimelineAnimation11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickTimelineAnimation *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickTimelineAnimation::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QQuickTimelineAnimation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickTimelineAnimation::tr(s, c, n));
}

//  QQuickTimelineAnimation::QQuickTimelineAnimation(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickTimelineAnimation *ritual_ZN23QQuickTimelineAnimationC1EP7QObject(
    QObject *parent) {
  return new QQuickTimelineAnimation(parent);
}

//  void QQuickTimelineAnimation::setPingPong(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickTimelineAnimation11setPingPongEb(
    QQuickTimelineAnimation *self,
    bool b) {
  self->setPingPong(b);
}

//  bool QQuickTimelineAnimation::pingPong() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickTimelineAnimation8pingPongEv(
    const QQuickTimelineAnimation *self) {
  return self->pingPong();
}

//  void QQuickTimelineAnimation::pingPongChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickTimelineAnimation15pingPongChangedEv(
    QQuickTimelineAnimation *self) {
  self->pingPongChanged();
}

//  void QQuickTimelineAnimation::finished()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickTimelineAnimation8finishedEv(
    QQuickTimelineAnimation *self) {
  self->finished();
}

//  void QQuickTimelineAnimation::handleStarted()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickTimelineAnimation13handleStartedEv(
    QQuickTimelineAnimation *self) {
  self->handleStarted();
}

//  void QQuickTimelineAnimation::handleStopped()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickTimelineAnimation13handleStoppedEv(
    QQuickTimelineAnimation *self) {
  self->handleStopped();
}

//  QList<QQuickTimelineAnimation *>::QList()
extern "C" Q_DECL_EXPORT
QList<QQuickTimelineAnimation *> *ritual_list_make_QQuickTimelineAnimation_ptr() {
  return new QList<QQuickTimelineAnimation *>();
}

//  void QList<QQuickTimelineAnimation *>::append(const
//      QQuickTimelineAnimation * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QQuickTimelineAnimation_ptr(
    QList<QQuickTimelineAnimation *> *self,
    QQuickTimelineAnimation *element) {
  self->append(element);
}

//  qsizetype QList<QQuickTimelineAnimation *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QQuickTimelineAnimation_ptr(
    const QList<QQuickTimelineAnimation *> *self) {
  return self->size();
}

//  const QQuickTimelineAnimation * &QList<QQuickTimelineAnimation
//      *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QQuickTimelineAnimation *ritual_list_at_QQuickTimelineAnimation_ptr(
    const QList<QQuickTimelineAnimation *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QQuickTimelineAnimation *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QQuickTimelineAnimation_ptr(
    QList<QQuickTimelineAnimation *> *self) {
  delete self;
}
