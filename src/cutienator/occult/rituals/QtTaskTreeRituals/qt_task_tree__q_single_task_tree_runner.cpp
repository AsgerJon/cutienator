//  Written by hand on 2026-11-25 from QtTaskTree/qtasktreerunner.h, Qt
//  6.12.0, from Qt's source. Kept as it is when the generator runs again.
//  'QSingleTaskTreeRunner' is final and has no virtual function: no Cute
//  class and no 'take'. Not written: 'start' or 'enqueue' (templates) and
//  'startImpl' or 'enqueueImpl' (they take std::function).
#include <QtTaskTree/qttasktreeglobal.h>
#include <QtTaskTree/qtasktreerunner.h>

//  QtTaskTree::QSingleTaskTreeRunner::QSingleTaskTreeRunner()
extern "C" Q_DECL_EXPORT
QtTaskTree::QSingleTaskTreeRunner *ritual_ZN10QtTaskTree21QSingleTaskTreeRunnerC1Ev() {
  return new QtTaskTree::QSingleTaskTreeRunner();
}

//  QtTaskTree::QSingleTaskTreeRunner::~QSingleTaskTreeRunner()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QtTaskTree21QSingleTaskTreeRunnerD1Ev(
    QtTaskTree::QSingleTaskTreeRunner *self) {
  delete self;
}

//  bool QtTaskTree::QSingleTaskTreeRunner::isRunning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QtTaskTree21QSingleTaskTreeRunner9isRunningEv(
    const QtTaskTree::QSingleTaskTreeRunner *self) {
  return self->isRunning();
}

//  void QtTaskTree::QSingleTaskTreeRunner::cancel()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QtTaskTree21QSingleTaskTreeRunner6cancelEv(
    QtTaskTree::QSingleTaskTreeRunner *self) {
  self->cancel();
}

//  void QtTaskTree::QSingleTaskTreeRunner::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QtTaskTree21QSingleTaskTreeRunner5resetEv(
    QtTaskTree::QSingleTaskTreeRunner *self) {
  self->reset();
}

//  QSingleTaskTreeRunnerPrivate *QtTaskTree::QSingleTaskTreeRunner::d_func()
extern "C" Q_DECL_EXPORT
QtTaskTree::QSingleTaskTreeRunnerPrivate *ritual_ZN10QtTaskTree21QSingleTaskTreeRunner6d_funcEv(
    QtTaskTree::QSingleTaskTreeRunner *self) {
  return self->d_func();
}

//  const QSingleTaskTreeRunnerPrivate
//      *QtTaskTree::QSingleTaskTreeRunner::d_func() const
extern "C" Q_DECL_EXPORT
const QtTaskTree::QSingleTaskTreeRunnerPrivate *ritual_ZNK10QtTaskTree21QSingleTaskTreeRunner6d_funcEv(
    const QtTaskTree::QSingleTaskTreeRunner *self) {
  return self->d_func();
}
