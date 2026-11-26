//  Written by hand on 2026-11-25 from QtTaskTree/qtasktreerunner.h, Qt
//  6.12.0, from Qt's source. Kept as it is when the generator runs again.
//  'QSequentialTaskTreeRunner' is final and has no virtual function: no Cute
//  class and no 'take'. Not written: 'start' or 'enqueue' (templates) and
//  'startImpl' or 'enqueueImpl' (they take std::function).
#include <QtTaskTree/qttasktreeglobal.h>
#include <QtTaskTree/qtasktreerunner.h>

//  QtTaskTree::QSequentialTaskTreeRunner::QSequentialTaskTreeRunner()
extern "C" Q_DECL_EXPORT
QtTaskTree::QSequentialTaskTreeRunner *ritual_ZN10QtTaskTree25QSequentialTaskTreeRunnerC1Ev() {
  return new QtTaskTree::QSequentialTaskTreeRunner();
}

//  QtTaskTree::QSequentialTaskTreeRunner::~QSequentialTaskTreeRunner()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QtTaskTree25QSequentialTaskTreeRunnerD1Ev(
    QtTaskTree::QSequentialTaskTreeRunner *self) {
  delete self;
}

//  bool QtTaskTree::QSequentialTaskTreeRunner::isRunning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QtTaskTree25QSequentialTaskTreeRunner9isRunningEv(
    const QtTaskTree::QSequentialTaskTreeRunner *self) {
  return self->isRunning();
}

//  void QtTaskTree::QSequentialTaskTreeRunner::cancel()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QtTaskTree25QSequentialTaskTreeRunner6cancelEv(
    QtTaskTree::QSequentialTaskTreeRunner *self) {
  self->cancel();
}

//  void QtTaskTree::QSequentialTaskTreeRunner::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QtTaskTree25QSequentialTaskTreeRunner5resetEv(
    QtTaskTree::QSequentialTaskTreeRunner *self) {
  self->reset();
}

//  void QtTaskTree::QSequentialTaskTreeRunner::cancelCurrent()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QtTaskTree25QSequentialTaskTreeRunner13cancelCurrentEv(
    QtTaskTree::QSequentialTaskTreeRunner *self) {
  self->cancelCurrent();
}

//  void QtTaskTree::QSequentialTaskTreeRunner::resetCurrent()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QtTaskTree25QSequentialTaskTreeRunner12resetCurrentEv(
    QtTaskTree::QSequentialTaskTreeRunner *self) {
  self->resetCurrent();
}

//  QSequentialTaskTreeRunnerPrivate
//      *QtTaskTree::QSequentialTaskTreeRunner::d_func()
extern "C" Q_DECL_EXPORT
QtTaskTree::QSequentialTaskTreeRunnerPrivate *ritual_ZN10QtTaskTree25QSequentialTaskTreeRunner6d_funcEv(
    QtTaskTree::QSequentialTaskTreeRunner *self) {
  return self->d_func();
}

//  const QSequentialTaskTreeRunnerPrivate
//      *QtTaskTree::QSequentialTaskTreeRunner::d_func() const
extern "C" Q_DECL_EXPORT
const QtTaskTree::QSequentialTaskTreeRunnerPrivate *ritual_ZNK10QtTaskTree25QSequentialTaskTreeRunner6d_funcEv(
    const QtTaskTree::QSequentialTaskTreeRunner *self) {
  return self->d_func();
}
