//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgesturerecognizer.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgesturerecognizer.h>

//  QGestureRecognizer::~QGestureRecognizer()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGestureRecognizerD1Ev(QGestureRecognizer *self) {
  delete self;
}

//  QGesture *QGestureRecognizer::create(QObject *target)
extern "C" Q_DECL_EXPORT
QGesture *ritual_ZN18QGestureRecognizer6createEP7QObject(
    QGestureRecognizer *self,
    QObject *target) {
  return self->create(target);
}

//  Result QGestureRecognizer::recognize(QGesture *state, QObject *watched,
//      QEvent *event)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QGestureRecognizer9recognizeEP8QGestureP7QObjectP6QEvent(
    QGestureRecognizer *self,
    QGesture *state,
    QObject *watched,
    QEvent *event) {
  return static_cast<int>(self->recognize(state, watched, event).toInt());
}

//  void QGestureRecognizer::reset(QGesture *state)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGestureRecognizer5resetEP8QGesture(
    QGestureRecognizer *self,
    QGesture *state) {
  self->reset(state);
}

//  Qt::GestureType QGestureRecognizer::registerRecognizer(QGestureRecognizer
//      *recognizer)
extern "C" Q_DECL_EXPORT
Qt::GestureType ritual_ZN18QGestureRecognizer18registerRecognizerEPS_(
    QGestureRecognizer *recognizer) {
  return QGestureRecognizer::registerRecognizer(recognizer);
}

//  void QGestureRecognizer::unregisterRecognizer(Qt::GestureType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGestureRecognizer20unregisterRecognizerEN2Qt11GestureTypeE(
    Qt::GestureType type) {
  QGestureRecognizer::unregisterRecognizer(type);
}
