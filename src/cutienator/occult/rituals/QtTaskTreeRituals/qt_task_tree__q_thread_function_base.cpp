//  Written by dev_tooling.RitualGenerator from the records of
//  QtTaskTree/qthreadfunctiontask.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: 'd_func' gives the private class as
//  QtTaskTree::<Class>Private, as the compiler needs it written.
//  Kept as it is when the generator runs again.
#include <QtCore/qglobal.h>
#include <QtTaskTree/qttasktreeglobal.h>
#if QT_CONFIG(concurrent)
#if QT_CONFIG(concurrent)
#include <QtTaskTree/qthreadfunctiontask.h>

//  QThreadFunctionBasePrivate *QtTaskTree::QThreadFunctionBase::d_func()
extern "C" Q_DECL_EXPORT
QtTaskTree::QThreadFunctionBasePrivate *ritual_ZN10QtTaskTree19QThreadFunctionBase6d_funcEv(
    QtTaskTree::QThreadFunctionBase *self) {
  return self->d_func();
}

//  const QThreadFunctionBasePrivate
//      *QtTaskTree::QThreadFunctionBase::d_func() const
extern "C" Q_DECL_EXPORT
const QtTaskTree::QThreadFunctionBasePrivate *ritual_ZNK10QtTaskTree19QThreadFunctionBase6d_funcEv(
    const QtTaskTree::QThreadFunctionBase *self) {
  return self->d_func();
}

//  QtTaskTree::QThreadFunctionBase::~QThreadFunctionBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QtTaskTree19QThreadFunctionBaseD1Ev(
    QtTaskTree::QThreadFunctionBase *self) {
  delete self;
}

#endif  // QT_CONFIG(concurrent)
#endif  // QT_CONFIG(concurrent)
