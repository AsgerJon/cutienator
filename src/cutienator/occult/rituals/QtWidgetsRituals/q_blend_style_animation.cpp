//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qstyleanimation_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/QtWidgets>
#include <QtWidgets/6.12.0/QtWidgets/private/qstyleanimation_p.h>
#include <QtCore/qstring.h>
#include <QtGui/qimage.h>

//  Only a class built on QBlendStyleAnimation may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQBlendStyleAnimation : QBlendStyleAnimation {
  using QBlendStyleAnimation::updateCurrentTime;
};

//  const QMetaObject *QBlendStyleAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QBlendStyleAnimation10metaObjectEv(
    const QBlendStyleAnimation *self) {
  return self->metaObject();
}

//  QString QBlendStyleAnimation::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QBlendStyleAnimation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QBlendStyleAnimation::tr(s, c, n));
}

//  QBlendStyleAnimation::QBlendStyleAnimation(Type type, QObject *target)
extern "C" Q_DECL_EXPORT
QBlendStyleAnimation *ritual_ZN20QBlendStyleAnimationC1ENS_4TypeEP7QObject(
    QBlendStyleAnimation::Type type,
    QObject *target) {
  return new QBlendStyleAnimation(type, target);
}

//  QImage QBlendStyleAnimation::startImage() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK20QBlendStyleAnimation10startImageEv(
    const QBlendStyleAnimation *self) {
  return new QImage(self->startImage());
}

//  void QBlendStyleAnimation::setStartImage(const QImage &image)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QBlendStyleAnimation13setStartImageERK6QImage(
    QBlendStyleAnimation *self,
    const QImage *image) {
  self->setStartImage(*image);
}

//  QImage QBlendStyleAnimation::endImage() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK20QBlendStyleAnimation8endImageEv(
    const QBlendStyleAnimation *self) {
  return new QImage(self->endImage());
}

//  void QBlendStyleAnimation::setEndImage(const QImage &image)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QBlendStyleAnimation11setEndImageERK6QImage(
    QBlendStyleAnimation *self,
    const QImage *image) {
  self->setEndImage(*image);
}

//  QImage QBlendStyleAnimation::currentImage() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK20QBlendStyleAnimation12currentImageEv(
    const QBlendStyleAnimation *self) {
  return new QImage(self->currentImage());
}

//  void QBlendStyleAnimation::updateCurrentTime(int time)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QBlendStyleAnimation17updateCurrentTimeEi(
    QBlendStyleAnimation *self,
    int time) {
  self->updateCurrentTime(time);
}

//  void QBlendStyleAnimation::updateCurrentTime(int time)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QBlendStyleAnimation17updateCurrentTimeEi(
    QBlendStyleAnimation *self,
    int time) {
  static_cast<OwnQBlendStyleAnimation *>(self)->OwnQBlendStyleAnimation::updateCurrentTime(
      time);
}
