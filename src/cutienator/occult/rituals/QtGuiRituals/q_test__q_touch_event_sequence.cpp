//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qtestsupport_gui.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/QtGui>
#include <QtGui/qtestsupport_gui.h>
#include <QtCore/qpoint.h>
#include <cstring>

//  A QTest::QTouchEventSequence that Python can take functions over in. Every QTest::QTouchEventSequence
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQTest_QTouchEventSequenceCall0)(const void *, bool, int *);
class CuteQTest_QTouchEventSequence : public QTest::QTouchEventSequence {
public:
  using QTest::QTouchEventSequence::QTouchEventSequence;
  CuteQTest_QTouchEventSequence(const QTest::QTouchEventSequence & other) : QTest::QTouchEventSequence(other) {}
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN5QTest19QTouchEventSequence6commitEb")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  bool QTest::QTouchEventSequence::commit(bool processEvents)
  bool commit(bool processEvents) override {
    if (taken[0]) {
      int handled = 0;
      CuteQTest_QTouchEventSequenceCall0 call = reinterpret_cast<CuteQTest_QTouchEventSequenceCall0>(taken[0]);
      bool given = call(this, processEvents, &handled);
      if (handled) return given;
    }
    return QTest::QTouchEventSequence::commit(processEvents);
  }
};

//  QTest::QTouchEventSequence::~QTouchEventSequence()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QTest19QTouchEventSequenceD1Ev(
    QTest::QTouchEventSequence *self) {
  delete self;
}

//  QTouchEventSequence &QTest::QTouchEventSequence::press(int touchId, const
//      QPoint &pt, QWindow *window)
extern "C" Q_DECL_EXPORT
QTest::QTouchEventSequence *ritual_ZN5QTest19QTouchEventSequence5pressEiRK6QPointP7QWindow(
    QTest::QTouchEventSequence *self,
    int touchId,
    const QPoint *pt,
    QWindow *window) {
  return &(self->press(touchId, *pt, window));
}

//  QTouchEventSequence &QTest::QTouchEventSequence::move(int touchId, const
//      QPoint &pt, QWindow *window)
extern "C" Q_DECL_EXPORT
QTest::QTouchEventSequence *ritual_ZN5QTest19QTouchEventSequence4moveEiRK6QPointP7QWindow(
    QTest::QTouchEventSequence *self,
    int touchId,
    const QPoint *pt,
    QWindow *window) {
  return &(self->move(touchId, *pt, window));
}

//  QTouchEventSequence &QTest::QTouchEventSequence::release(int touchId,
//      const QPoint &pt, QWindow *window)
extern "C" Q_DECL_EXPORT
QTest::QTouchEventSequence *ritual_ZN5QTest19QTouchEventSequence7releaseEiRK6QPointP7QWindow(
    QTest::QTouchEventSequence *self,
    int touchId,
    const QPoint *pt,
    QWindow *window) {
  return &(self->release(touchId, *pt, window));
}

//  QTouchEventSequence &QTest::QTouchEventSequence::stationary(int touchId)
extern "C" Q_DECL_EXPORT
QTest::QTouchEventSequence *ritual_ZN5QTest19QTouchEventSequence10stationaryEi(
    QTest::QTouchEventSequence *self,
    int touchId) {
  return &(self->stationary(touchId));
}

//  bool QTest::QTouchEventSequence::commit(bool processEvents)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QTest19QTouchEventSequence6commitEb(
    QTest::QTouchEventSequence *self,
    bool processEvents) {
  return self->commit(processEvents);
}

//  bool QTest::QTouchEventSequence::cancel(bool processEvents)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QTest19QTouchEventSequence6cancelEb(
    QTest::QTouchEventSequence *self,
    bool processEvents) {
  return self->cancel(processEvents);
}

//  QTest::QTouchEventSequence::QTouchEventSequence(QWindow *window,
//      QPointingDevice *aDevice, bool autoCommit)
extern "C" Q_DECL_EXPORT
QTest::QTouchEventSequence *ritual_ZN5QTest19QTouchEventSequenceC1EP7QWindowP15QPointingDeviceb(
    QWindow *window,
    QPointingDevice *aDevice,
    bool autoCommit) {
  return new CuteQTest_QTouchEventSequence(window, aDevice, autoCommit);
}

//  QPointF QTest::QTouchEventSequence::mapToScreen(QWindow *window, const
//      QPoint &pt)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN5QTest19QTouchEventSequence11mapToScreenEP7QWindowRK6QPoint(
    QTest::QTouchEventSequence *self,
    QWindow *window,
    const QPoint *pt) {
  return new QPointF(self->mapToScreen(window, *pt));
}

//  QEventPoint &QTest::QTouchEventSequence::point(int touchId)
extern "C" Q_DECL_EXPORT
QEventPoint *ritual_ZN5QTest19QTouchEventSequence5pointEi(
    QTest::QTouchEventSequence *self,
    int touchId) {
  return &(self->point(touchId));
}

//  QEventPoint &QTest::QTouchEventSequence::pointOrPreviousPoint(int
//      touchId)
extern "C" Q_DECL_EXPORT
QEventPoint *ritual_ZN5QTest19QTouchEventSequence20pointOrPreviousPointEi(
    QTest::QTouchEventSequence *self,
    int touchId) {
  return &(self->pointOrPreviousPoint(touchId));
}

//  a Python function taken by a CuteQTest_QTouchEventSequence, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTest_QTouchEventSequence(
    QTest::QTouchEventSequence *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTest_QTouchEventSequence *>(self)->take(key, call);
}

//  bool QTest::QTouchEventSequence::commit(bool processEvents)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN5QTest19QTouchEventSequence6commitEb(
    QTest::QTouchEventSequence *self,
    bool processEvents) {
  return self->QTest::QTouchEventSequence::commit(processEvents);
}
