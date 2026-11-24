//  Written by dev_tooling.RitualGenerator from the records of
//  QtTaskTree/qthreadfunctiontask.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtTaskTree/qttasktreeglobal.h>
#if QT_CONFIG(concurrent)
#if QT_CONFIG(concurrent)
#include <QtTaskTree/qthreadfunctiontask.h>

//  QtTaskTree::QThreadFunctionBase::~QThreadFunctionBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QtTaskTree19QThreadFunctionBaseD1Ev(
    QtTaskTree::QThreadFunctionBase *self) {
  delete self;
}

#endif  // QT_CONFIG(concurrent)
#endif  // QT_CONFIG(concurrent)
