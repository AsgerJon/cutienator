//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qtestsupport_widgets.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/QtWidgets>
#include <QtWidgets/qtestsupport_widgets.h>
#include <QtCore/qpoint.h>
#include <cstring>

//  A QTest::QTouchEventWidgetSequence that Python can take functions over in. Every QTest::QTouchEventWidgetSequence
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQTest_QTouchEventWidgetSequenceCall0)(const void *, bool, int *);
class CuteQTest_QTouchEventWidgetSequence : public QTest::QTouchEventWidgetSequence {
public:
  using QTest::QTouchEventWidgetSequence::QTouchEventWidgetSequence;
  CuteQTest_QTouchEventWidgetSequence(const QTest::QTouchEventWidgetSequence & other) : QTest::QTouchEventWidgetSequence(other) {}
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN5QTest19QTouchEventSequence6commitEb")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  bool QTest::QTouchEventWidgetSequence::commit(bool processEvents)
  bool commit(bool processEvents) override {
    if (taken[0]) {
      int handled = 0;
      CuteQTest_QTouchEventWidgetSequenceCall0 call = reinterpret_cast<CuteQTest_QTouchEventWidgetSequenceCall0>(taken[0]);
      bool given = call(this, processEvents, &handled);
      if (handled) return given;
    }
    return QTest::QTouchEventWidgetSequence::commit(processEvents);
  }
};

//  QTest::QTouchEventWidgetSequence::~QTouchEventWidgetSequence()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QTest25QTouchEventWidgetSequenceD1Ev(
    QTest::QTouchEventWidgetSequence *self) {
  delete self;
}

//  QTouchEventWidgetSequence &QTest::QTouchEventWidgetSequence::press(int
//      touchId, const QPoint &pt, QWidget *widget)
extern "C" Q_DECL_EXPORT
QTest::QTouchEventWidgetSequence *ritual_ZN5QTest25QTouchEventWidgetSequence5pressEiRK6QPointP7QWidget(
    QTest::QTouchEventWidgetSequence *self,
    int touchId,
    const QPoint *pt,
    QWidget *widget) {
  return &(self->press(touchId, *pt, widget));
}

//  QTouchEventWidgetSequence &QTest::QTouchEventWidgetSequence::move(int
//      touchId, const QPoint &pt, QWidget *widget)
extern "C" Q_DECL_EXPORT
QTest::QTouchEventWidgetSequence *ritual_ZN5QTest25QTouchEventWidgetSequence4moveEiRK6QPointP7QWidget(
    QTest::QTouchEventWidgetSequence *self,
    int touchId,
    const QPoint *pt,
    QWidget *widget) {
  return &(self->move(touchId, *pt, widget));
}

//  QTouchEventWidgetSequence &QTest::QTouchEventWidgetSequence::release(int
//      touchId, const QPoint &pt, QWidget *widget)
extern "C" Q_DECL_EXPORT
QTest::QTouchEventWidgetSequence *ritual_ZN5QTest25QTouchEventWidgetSequence7releaseEiRK6QPointP7QWidget(
    QTest::QTouchEventWidgetSequence *self,
    int touchId,
    const QPoint *pt,
    QWidget *widget) {
  return &(self->release(touchId, *pt, widget));
}

//  QTouchEventWidgetSequence
//      &QTest::QTouchEventWidgetSequence::stationary(int touchId)
extern "C" Q_DECL_EXPORT
QTest::QTouchEventWidgetSequence *ritual_ZN5QTest25QTouchEventWidgetSequence10stationaryEi(
    QTest::QTouchEventWidgetSequence *self,
    int touchId) {
  return &(self->stationary(touchId));
}

//  bool QTest::QTouchEventWidgetSequence::commit(bool processEvents)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QTest25QTouchEventWidgetSequence6commitEb(
    QTest::QTouchEventWidgetSequence *self,
    bool processEvents) {
  return self->commit(processEvents);
}

//  QTest::QTouchEventWidgetSequence::QTouchEventWidgetSequence(QWidget
//      *widget, QPointingDevice *aDevice, bool autoCommit)
extern "C" Q_DECL_EXPORT
QTest::QTouchEventWidgetSequence *ritual_ZN5QTest25QTouchEventWidgetSequenceC1EP7QWidgetP15QPointingDeviceb(
    QWidget *widget,
    QPointingDevice *aDevice,
    bool autoCommit) {
  return new CuteQTest_QTouchEventWidgetSequence(
      widget,
      aDevice,
      autoCommit);
}

//  QPointF QTest::QTouchEventWidgetSequence::mapToScreen(QWidget *widget,
//      const QPoint &pt)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN5QTest25QTouchEventWidgetSequence11mapToScreenEP7QWidgetRK6QPoint(
    QTest::QTouchEventWidgetSequence *self,
    QWidget *widget,
    const QPoint *pt) {
  return new QPointF(self->mapToScreen(widget, *pt));
}

//  a Python function taken by a CuteQTest_QTouchEventWidgetSequence, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTest_QTouchEventWidgetSequence(
    QTest::QTouchEventWidgetSequence *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTest_QTouchEventWidgetSequence *>(self)->take(key, call);
}

//  bool QTest::QTouchEventWidgetSequence::commit(bool processEvents)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN5QTest25QTouchEventWidgetSequence6commitEb(
    QTest::QTouchEventWidgetSequence *self,
    bool processEvents) {
  return self->QTest::QTouchEventWidgetSequence::commit(processEvents);
}
