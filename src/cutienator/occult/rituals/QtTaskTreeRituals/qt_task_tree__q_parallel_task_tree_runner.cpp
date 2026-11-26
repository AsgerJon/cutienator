//  Written by hand on 2026-11-25 from QtTaskTree/qtasktreerunner.h, Qt
//  6.12.0, from Qt's source. Kept as it is when the generator runs again.
//  'QParallelTaskTreeRunner' is final and has no virtual function: no Cute
//  class and no 'take'. Not written: 'start' (a template) and
//  'startImpl' (it takes std::function).
#include <QtTaskTree/qttasktreeglobal.h>
#include <QtTaskTree/qtasktreerunner.h>

//  QtTaskTree::QParallelTaskTreeRunner::QParallelTaskTreeRunner()
extern "C" Q_DECL_EXPORT
QtTaskTree::QParallelTaskTreeRunner *ritual_ZN10QtTaskTree23QParallelTaskTreeRunnerC1Ev() {
  return new QtTaskTree::QParallelTaskTreeRunner();
}

//  QtTaskTree::QParallelTaskTreeRunner::~QParallelTaskTreeRunner()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QtTaskTree23QParallelTaskTreeRunnerD1Ev(
    QtTaskTree::QParallelTaskTreeRunner *self) {
  delete self;
}

//  bool QtTaskTree::QParallelTaskTreeRunner::isRunning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QtTaskTree23QParallelTaskTreeRunner9isRunningEv(
    const QtTaskTree::QParallelTaskTreeRunner *self) {
  return self->isRunning();
}

//  void QtTaskTree::QParallelTaskTreeRunner::cancel()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QtTaskTree23QParallelTaskTreeRunner6cancelEv(
    QtTaskTree::QParallelTaskTreeRunner *self) {
  self->cancel();
}

//  void QtTaskTree::QParallelTaskTreeRunner::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QtTaskTree23QParallelTaskTreeRunner5resetEv(
    QtTaskTree::QParallelTaskTreeRunner *self) {
  self->reset();
}

//  QParallelTaskTreeRunnerPrivate *QtTaskTree::QParallelTaskTreeRunner::d_func()
extern "C" Q_DECL_EXPORT
QtTaskTree::QParallelTaskTreeRunnerPrivate *ritual_ZN10QtTaskTree23QParallelTaskTreeRunner6d_funcEv(
    QtTaskTree::QParallelTaskTreeRunner *self) {
  return self->d_func();
}

//  const QParallelTaskTreeRunnerPrivate
//      *QtTaskTree::QParallelTaskTreeRunner::d_func() const
extern "C" Q_DECL_EXPORT
const QtTaskTree::QParallelTaskTreeRunnerPrivate *ritual_ZNK10QtTaskTree23QParallelTaskTreeRunner6d_funcEv(
    const QtTaskTree::QParallelTaskTreeRunner *self) {
  return self->d_func();
}
