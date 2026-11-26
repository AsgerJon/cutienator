//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgesturerecognizer.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if !defined(QT_NO_GESTURES)
#include <QtWidgets/qgesturerecognizer.h>
#include <cstring>

//  A QGestureRecognizer that Python can take functions over in. Every QGestureRecognizer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_GESTURES)
typedef void * (*CuteQGestureRecognizerCall0)(const void *, QObject *, int *);
#endif  // !defined(QT_NO_GESTURES)
#if !defined(QT_NO_GESTURES)
typedef int (*CuteQGestureRecognizerCall1)(const void *, QGesture *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_GESTURES)
#if !defined(QT_NO_GESTURES)
typedef void (*CuteQGestureRecognizerCall2)(const void *, QGesture *, int *);
#endif  // !defined(QT_NO_GESTURES)
class CuteQGestureRecognizer : public QGestureRecognizer {
public:
  using QGestureRecognizer::QGestureRecognizer;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_GESTURES)
    if (!std::strcmp(key, "_ZN18QGestureRecognizer6createEP7QObject")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_GESTURES)
#if !defined(QT_NO_GESTURES)
    if (!std::strcmp(key, "_ZN18QGestureRecognizer9recognizeEP8QGestureP7QObjectP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_GESTURES)
#if !defined(QT_NO_GESTURES)
    if (!std::strcmp(key, "_ZN18QGestureRecognizer5resetEP8QGesture")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_GESTURES)
    return false;
  }

#if !defined(QT_NO_GESTURES)
  //  QGesture *QGestureRecognizer::create(QObject *target)
  QGesture *create(QObject *target) override {
    if (taken[0]) {
      int handled = 0;
      CuteQGestureRecognizerCall0 call = reinterpret_cast<CuteQGestureRecognizerCall0>(taken[0]);
      void * given = call(this, target, &handled);
      if (handled) return static_cast<QGesture *>(given);
    }
    return QGestureRecognizer::create(target);
  }
#endif  // !defined(QT_NO_GESTURES)

#if !defined(QT_NO_GESTURES)
  //  Result QGestureRecognizer::recognize(QGesture *state, QObject
  //      *watched, QEvent *event)
  QGestureRecognizer::Result recognize(
      QGesture *state,
      QObject *watched,
      QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQGestureRecognizerCall1 call = reinterpret_cast<CuteQGestureRecognizerCall1>(taken[1]);
      int given = call(this, state, watched, event, &handled);
      if (handled) return QFlags<QGestureRecognizer::ResultFlag>::fromInt(given);
    }
    return {};
  }
#endif  // !defined(QT_NO_GESTURES)

#if !defined(QT_NO_GESTURES)
  //  void QGestureRecognizer::reset(QGesture *state)
  void reset(QGesture *state) override {
    if (taken[2]) {
      int handled = 0;
      CuteQGestureRecognizerCall2 call = reinterpret_cast<CuteQGestureRecognizerCall2>(taken[2]);
      call(this, state, &handled);
      if (handled) return;
    }
    QGestureRecognizer::reset(state);
  }
#endif  // !defined(QT_NO_GESTURES)
};

//  QGestureRecognizer::QGestureRecognizer()
extern "C" Q_DECL_EXPORT
QGestureRecognizer *ritual_ZN18QGestureRecognizerC1Ev() {
  return new CuteQGestureRecognizer();
}

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

//  a Python function taken by a CuteQGestureRecognizer, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGestureRecognizer(
    QGestureRecognizer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGestureRecognizer *>(self)->take(key, call);
}

//  QGesture *QGestureRecognizer::create(QObject *target)
extern "C" Q_DECL_EXPORT
QGesture *ritual_own_ZN18QGestureRecognizer6createEP7QObject(
    QGestureRecognizer *self,
    QObject *target) {
  return self->QGestureRecognizer::create(target);
}

//  void QGestureRecognizer::reset(QGesture *state)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QGestureRecognizer5resetEP8QGesture(
    QGestureRecognizer *self,
    QGesture *state) {
  self->QGestureRecognizer::reset(state);
}

#endif  // !defined(QT_NO_GESTURES)
