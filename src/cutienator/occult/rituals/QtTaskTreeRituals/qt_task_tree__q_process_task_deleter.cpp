//  Written by dev_tooling.RitualGenerator from the records of
//  QtTaskTree/qprocesstask.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtTaskTree/qttasktreeglobal.h>
#if (QT_CONFIG(process)) || (!QT_CONFIG(process))
#if QT_CONFIG(process)
#include <QtTaskTree/qprocesstask.h>

//  QtTaskTree::QProcessTaskDeleter::~QProcessTaskDeleter()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QtTaskTree19QProcessTaskDeleterD1Ev(
    QtTaskTree::QProcessTaskDeleter *self) {
  delete self;
}

#endif  // QT_CONFIG(process)
#endif  // (QT_CONFIG(process)) || (!QT_CONFIG(process))
