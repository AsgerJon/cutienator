//  Written by dev_tooling.RitualGenerator from the records of
//  QtTaskTree/qprocesstask.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtTaskTree/qttasktreeglobal.h>
#if (QT_CONFIG(process)) || (!QT_CONFIG(process))
#if QT_CONFIG(process)
#include <QtTaskTree/qprocesstask.h>

//  QtTaskTree::QProcessTaskAdapter::~QProcessTaskAdapter()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QtTaskTree19QProcessTaskAdapterD1Ev(
    QtTaskTree::QProcessTaskAdapter *self) {
  delete self;
}

#endif  // QT_CONFIG(process)
#endif  // (QT_CONFIG(process)) || (!QT_CONFIG(process))
